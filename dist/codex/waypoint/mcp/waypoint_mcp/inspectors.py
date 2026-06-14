"""Read-only Waypoint repository inspectors."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

WAYPOINT_START = "<!-- waypoint:start -->"
WAYPOINT_END = "<!-- waypoint:end -->"
DOC_SUFFIXES = {".md", ".markdown", ".mdown", ".txt", ".rst"}
IGNORED_DIR_NAMES = {
    ".git",
    ".hg",
    ".svn",
    ".venv",
    "venv",
    "node_modules",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "dist",
    "build",
}
DEFAULT_DOCUMENTS = {
    "agents": "AGENTS.md",
    "vision": "docs/vision.md",
    "ontology": "docs/ontology.md",
    "architecture": "docs/architecture.md",
    "workflows": "docs/workflows.md",
    "decisions": "docs/decisions.md",
    "plan": "docs/plan.md",
    "todo": "docs/todo.md",
    "ideas": "docs/ideas.md",
    "workbench": "docs/workbench",
}
CORE_DOCUMENT_ROLES = {
    "agents",
    "vision",
    "ontology",
    "architecture",
    "workflows",
    "decisions",
    "plan",
    "ideas",
}
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
TODO_RE = re.compile(r"(^|\s)(TODO|FIXME)\b|\[[ xX]\]", re.IGNORECASE)
DECISION_WORD_RE = re.compile(
    r"\b(decision|decided|rationale|superseded|reverted|reversal|adr)\b",
    re.IGNORECASE,
)
REVERSAL_WORD_RE = re.compile(
    r"\b(revert(?:ed|s|ing)?|rollback|rolled back|supersede(?:d|s)?|"
    r"replace(?:d|s)?|retire(?:d|s)?|remove(?:d|s)?|no longer|abandon(?:ed|s)?)\b",
    re.IGNORECASE,
)
POLICY_WORD_RE = re.compile(r"\b(must|never|always|required|do not|forbidden)\b", re.IGNORECASE)

ROLE_LINE_THRESHOLDS = {
    "router": 250,
    "runtime-wrapper": 80,
    "vision": 300,
    "ontology": 300,
    "architecture": 450,
    "workflows": 450,
    "decisions": 450,
    "plan": 450,
    "ideas": 450,
}
ROLE_BYTE_THRESHOLDS = {
    "router": 16_000,
    "runtime-wrapper": 6_000,
    "vision": 22_000,
    "ontology": 22_000,
    "architecture": 34_000,
    "workflows": 34_000,
    "decisions": 34_000,
    "plan": 34_000,
    "ideas": 34_000,
}


class WaypointInspectError(ValueError):
    """Raised when inspector input cannot be handled."""


def resolve_repo_root(repo_root: str | Path | None = None) -> Path:
    root = Path(repo_root or ".").expanduser().resolve()
    if not root.exists():
        raise WaypointInspectError(f"repository path does not exist: {root}")
    if not root.is_dir():
        raise WaypointInspectError(f"repository path is not a directory: {root}")
    return root


def discover_repo(repo_root: str | Path | None = None, max_files: int = 500) -> dict[str, Any]:
    root = resolve_repo_root(repo_root)
    docs = list(iter_candidate_docs(root, max_files=max_files))
    routers = [describe_router(root, path) for path in docs if is_router(path)]
    documents = [describe_document(root, path) for path in docs]
    config = read_waypoint_config(root)

    return {
        "repo_root": str(root),
        "routers": routers,
        "documents": documents,
        "waypoint": {
            "config": config,
            "marker_blocks": marker_summary(root, routers),
        },
        "summary": {
            "router_count": len(routers),
            "document_count": len(documents),
            "has_agents": (root / "AGENTS.md").is_file(),
            "has_claude": (root / "CLAUDE.md").is_file(),
            "has_docs_dir": (root / "docs").is_dir(),
            "has_waypoint_config": config["exists"],
        },
    }


def doctor_repo(repo_root: str | Path | None = None) -> dict[str, Any]:
    root = resolve_repo_root(repo_root)
    discovery = discover_repo(root)
    findings: list[dict[str, Any]] = []

    def add(level: str, code: str, message: str, path: str | None = None) -> None:
        item: dict[str, Any] = {"level": level, "code": code, "message": message}
        if path is not None:
            item["path"] = path
        findings.append(item)

    add("pass", "repo-found", "Repository path exists.", ".")

    agents_path = root / "AGENTS.md"
    if not agents_path.is_file():
        add("fail", "missing-agents", "AGENTS.md is missing.", "AGENTS.md")
    else:
        text = read_text(agents_path)
        add("pass", "agents-found", "AGENTS.md exists.", "AGENTS.md")
        if "Document Map" in text:
            add("pass", "document-map-found", "AGENTS.md includes a Document Map.", "AGENTS.md")
        else:
            add("warn", "document-map-missing", "AGENTS.md has no Document Map section.", "AGENTS.md")
        if "Read And Update Routing" in text or "Read/Update Routing" in text:
            add(
                "pass",
                "routing-table-found",
                "AGENTS.md includes read/update routing.",
                "AGENTS.md",
            )
        else:
            add(
                "warn",
                "routing-table-missing",
                "AGENTS.md has no read/update routing table.",
                "AGENTS.md",
            )
        add_marker_findings(add, agents_path)

    claude_path = root / "CLAUDE.md"
    if claude_path.is_file():
        claude_text = read_text(claude_path)
        if "AGENTS.md" in claude_text:
            add("pass", "claude-wrapper", "CLAUDE.md delegates to AGENTS.md.", "CLAUDE.md")
        else:
            add("warn", "claude-wrapper-drift", "CLAUDE.md does not mention AGENTS.md.", "CLAUDE.md")
        add_marker_findings(add, claude_path)

    config = read_waypoint_config(root)
    if config["exists"]:
        add("pass", "config-found", ".waypoint/config.yaml exists.", ".waypoint/config.yaml")
    else:
        add("warn", "config-missing", ".waypoint/config.yaml is missing.", ".waypoint/config.yaml")
    for error in config.get("errors", []):
        add("fail", "config-parse-error", error, ".waypoint/config.yaml")

    configured_docs = configured_document_homes(config)
    for role, relative in configured_docs.items():
        if relative is None:
            continue
        candidate = root / relative
        if candidate.exists():
            add("pass", "document-home-found", f"{role} home exists.", relative)
            continue
        level = "fail" if role == "agents" else "warn"
        add(level, "document-home-missing", f"{role} home is missing.", relative)

    cache_dir = root / ".waypoint" / "cache"
    if cache_dir.exists() and not gitignore_ignores_waypoint_cache(root):
        add(
            "warn",
            "cache-not-ignored",
            ".waypoint/cache/ exists but is not listed in .gitignore.",
            ".gitignore",
        )

    for broken in broken_markdown_links(root):
        add(
            "warn",
            "broken-markdown-link",
            f"Broken local Markdown link target: {broken['target']}",
            broken["path"],
        )

    status = "pass"
    if any(item["level"] == "fail" for item in findings):
        status = "fail"
    elif any(item["level"] == "warn" for item in findings):
        status = "warn"

    counts = {"pass": 0, "warn": 0, "fail": 0}
    for item in findings:
        counts[item["level"]] += 1

    return {
        "repo_root": str(root),
        "status": status,
        "counts": counts,
        "findings": findings,
        "discovery_summary": discovery["summary"],
    }


def audit_repo(repo_root: str | Path | None = None, max_files: int = 500) -> dict[str, Any]:
    """Return read-only document governance inventory and heuristic findings."""

    root = resolve_repo_root(repo_root)
    discovery = discover_repo(root, max_files=max_files)
    doctor = doctor_repo(root)
    docs = [describe_audit_document(root, path) for path in iter_candidate_docs(root, max_files=max_files)]
    findings: list[dict[str, Any]] = []

    def add(
        severity: str,
        confidence: str,
        code: str,
        message: str,
        path: str,
        recommendation: str,
    ) -> None:
        findings.append(
            {
                "severity": severity,
                "confidence": confidence,
                "code": code,
                "message": message,
                "path": path,
                "recommendation": recommendation,
            }
        )

    for item in doctor["findings"]:
        if item["level"] == "fail":
            add(
                "high",
                "high",
                f"doctor-{item['code']}",
                item["message"],
                item.get("path", "."),
                "Run Waypoint doctor remediation before document organization.",
            )
        elif item["level"] == "warn" and item["code"] in {
            "document-map-missing",
            "routing-table-missing",
            "claude-wrapper-drift",
            "config-parse-error",
            "document-home-missing",
        }:
            add(
                "medium",
                "high",
                f"doctor-{item['code']}",
                item["message"],
                item.get("path", "."),
                "Fix routing or configured homes before moving document content.",
            )

    for doc in docs:
        role = doc["role"]
        threshold_lines = ROLE_LINE_THRESHOLDS.get(role, 500)
        threshold_bytes = ROLE_BYTE_THRESHOLDS.get(role, 40_000)
        path = doc["path"]
        is_governance_doc = is_governance_document_path(path)
        if is_governance_doc and (
            doc["line_count"] > threshold_lines or doc["byte_count"] > threshold_bytes
        ):
            add(
                "medium" if role in CORE_DOCUMENT_ROLES | {"router", "runtime-wrapper"} else "low",
                "medium",
                "document-bloat-candidate",
                (
                    f"{path} is large for role {role}: "
                    f"{doc['line_count']} lines, {doc['byte_count']} bytes."
                ),
                path,
                "Inspect whether sections should be summarized, split, or archived.",
            )
        if role == "runtime-wrapper" and doc["line_count"] > 80:
            add(
                "medium",
                "medium",
                "wrapper-bloat-candidate",
                f"{path} is longer than a thin runtime wrapper should usually be.",
                path,
                "Consider delegating durable project rules back to AGENTS.md.",
            )
        if role == "decisions" and doc["todo_count"] > 0:
            add(
                "medium",
                "medium",
                "decisions-contain-active-work",
                f"{path} contains {doc['todo_count']} TODO or checkbox markers.",
                path,
                "Move active work to the live plan or todo document unless it is historical evidence.",
            )
        if role == "plan" and doc["decision_word_count"] > 3:
            add(
                "low",
                "low",
                "plan-may-contain-decisions",
                f"{path} contains repeated decision vocabulary.",
                path,
                "Check whether durable choices should move to the decisions document.",
            )
        if role == "ideas" and doc["todo_count"] > 3:
            add(
                "low",
                "medium",
                "ideas-may-contain-active-work",
                f"{path} contains multiple TODO or checkbox markers.",
                path,
                "Promote committed work to the live plan and keep exploratory ideas here.",
            )
        if is_governance_doc and role in {"report", "archive"} and doc["policy_word_count"] > 5:
            add(
                "low",
                "low",
                "historical-doc-may-act-live",
                f"{path} contains repeated policy vocabulary.",
                path,
                "Confirm whether live routers explicitly promote this historical material.",
            )

    decisions_docs = [doc for doc in docs if doc["role"] == "decisions"]
    for doc in decisions_docs:
        if doc["reversal_word_count"] > 0:
            add(
                "low",
                "medium",
                "decision-consolidation-candidate",
                f"{doc['path']} contains {doc['reversal_word_count']} reversal or supersession signals.",
                doc["path"],
                "Review whether reversed decisions should be preserved, consolidated, or archived.",
            )

    severity_counts = {"high": 0, "medium": 0, "low": 0}
    for item in findings:
        severity_counts[item["severity"]] += 1
    finding_paths = {item["path"] for item in findings}
    notable_docs = [
        doc
        for doc in docs
        if doc["path"] in finding_paths
        or doc["role"] in {"router", "runtime-wrapper"}
        or doc["path"] in {"README.md", "docs/decisions.md", "docs/plan.md", "docs/workflows.md"}
    ]

    return {
        "repo_root": str(root),
        "status": "findings" if findings else "clean",
        "summary": {
            "document_count": len(docs),
            "notable_document_count": len(notable_docs),
            "finding_count": len(findings),
            "severity_counts": severity_counts,
            "doctor_status": doctor["status"],
            "has_agents": discovery["summary"]["has_agents"],
            "has_claude": discovery["summary"]["has_claude"],
            "has_waypoint_config": discovery["summary"]["has_waypoint_config"],
        },
        "findings": findings,
        "documents": notable_docs,
        "doctor": {
            "status": doctor["status"],
            "counts": doctor["counts"],
        },
    }


def iter_candidate_docs(root: Path, max_files: int) -> list[Path]:
    files: list[Path] = []
    for path in sorted(root.rglob("*")):
        try:
            relative = path.relative_to(root)
        except ValueError:
            continue
        if should_ignore(relative):
            continue
        if not path.is_file():
            continue
        if path.name in {"AGENTS.md", "CLAUDE.md", "README.md"} or path.suffix.lower() in DOC_SUFFIXES:
            files.append(path)
        if len(files) >= max_files:
            break
    return files


def should_ignore(relative: Path) -> bool:
    parts = set(relative.parts)
    if parts & IGNORED_DIR_NAMES:
        return True
    return len(relative.parts) >= 2 and relative.parts[0] == ".waypoint" and relative.parts[1] == "cache"


def is_router(path: Path) -> bool:
    return path.name in {"AGENTS.md", "CLAUDE.md"}


def describe_router(root: Path, path: Path) -> dict[str, Any]:
    text = read_text(path)
    relative = rel(root, path)
    return {
        "path": relative,
        "kind": "agents" if path.name == "AGENTS.md" else "runtime-wrapper",
        "has_waypoint_marker": WAYPOINT_START in text or WAYPOINT_END in text,
        "waypoint_start_count": text.count(WAYPOINT_START),
        "waypoint_end_count": text.count(WAYPOINT_END),
    }


def describe_document(root: Path, path: Path) -> dict[str, Any]:
    role, confidence = classify_document(root, path)
    return {
        "path": rel(root, path),
        "role": role,
        "confidence": confidence,
    }


def describe_audit_document(root: Path, path: Path) -> dict[str, Any]:
    text = read_text(path)
    role, confidence = classify_document(root, path)
    headings = extract_headings(text)
    return {
        "path": rel(root, path),
        "role": role,
        "confidence": confidence,
        "line_count": len(text.splitlines()),
        "byte_count": len(text.encode("utf-8")),
        "heading_count": len(headings),
        "top_headings": [heading["text"] for heading in headings if heading["level"] <= 2][:12],
        "todo_count": len(TODO_RE.findall(text)),
        "decision_word_count": len(DECISION_WORD_RE.findall(text)),
        "reversal_word_count": len(REVERSAL_WORD_RE.findall(text)),
        "policy_word_count": len(POLICY_WORD_RE.findall(text)),
    }


def extract_headings(text: str) -> list[dict[str, Any]]:
    headings: list[dict[str, Any]] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        match = HEADING_RE.match(line)
        if not match:
            continue
        headings.append(
            {
                "level": len(match.group(1)),
                "text": match.group(2).strip(),
                "line": line_number,
            }
        )
    return headings


def is_governance_document_path(path: str) -> bool:
    return (
        path in {"AGENTS.md", "CLAUDE.md", "README.md"}
        or path.startswith("docs/")
        or "/docs/" in path
    )


def classify_document(root: Path, path: Path) -> tuple[str, str]:
    relative = rel(root, path).lower()
    name = path.name.lower()
    parent = path.parent.name.lower()

    if name == "agents.md":
        return "router", "high"
    if name == "claude.md":
        return "runtime-wrapper", "high"
    if name == "readme.md":
        return "readme", "medium"
    if "vision" in name or "purpose" in name:
        return "vision", "high"
    if "ontology" in name or "glossary" in name or "vocabulary" in name:
        return "ontology", "high"
    if "architecture" in name or "design" in name:
        return "architecture", "high"
    if "workflow" in name or "runbook" in name:
        return "workflows", "high"
    if "decision" in name or parent in {"adr", "adrs", "decisions"} or "/adr/" in relative:
        return "decisions", "high"
    if "plan" in name or "roadmap" in name:
        return "plan", "high"
    if "todo" in name or "task" in name:
        return "todo", "medium"
    if "idea" in name or parent == "ideas":
        return "ideas", "medium"
    if "report" in relative or "/reports/" in relative:
        return "report", "medium"
    if "archive" in relative or "/archives/" in relative:
        return "archive", "medium"
    return "document", "low"


def marker_summary(root: Path, routers: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "start_marker": WAYPOINT_START,
        "end_marker": WAYPOINT_END,
        "routers_with_markers": [item["path"] for item in routers if item["has_waypoint_marker"]],
        "total_start_count": sum(item["waypoint_start_count"] for item in routers),
        "total_end_count": sum(item["waypoint_end_count"] for item in routers),
    }


def add_marker_findings(add: Any, path: Path) -> None:
    text = read_text(path)
    start = text.count(WAYPOINT_START)
    end = text.count(WAYPOINT_END)
    relative = path.name
    if start == 0 and end == 0:
        add("warn", "waypoint-marker-missing", "No Waypoint marker block found.", relative)
        return
    if start != end:
        add("fail", "waypoint-marker-mismatch", "Waypoint marker start/end counts differ.", relative)
        return
    if start > 1:
        add("fail", "waypoint-marker-duplicate", "Duplicate Waypoint marker blocks found.", relative)
        return
    add("pass", "waypoint-marker-found", "One Waypoint marker block found.", relative)


def read_waypoint_config(root: Path) -> dict[str, Any]:
    path = root / ".waypoint" / "config.yaml"
    if not path.is_file():
        return {"exists": False, "path": ".waypoint/config.yaml", "data": {}, "errors": []}
    text = read_text(path)
    data, errors = parse_simple_yaml_map(text)
    return {"exists": True, "path": ".waypoint/config.yaml", "data": data, "errors": errors}


def parse_simple_yaml_map(text: str) -> tuple[dict[str, Any], list[str]]:
    """Parse the one-level locator YAML shape Waypoint writes.

    This is intentionally small and dependency-free. It supports top-level
    scalar keys and one nested mapping level, which is enough for
    `.waypoint/config.yaml`.
    """

    result: dict[str, Any] = {}
    errors: list[str] = []
    section: str | None = None

    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        stripped = line.strip()
        if indent == 0:
            if stripped.endswith(":"):
                section = stripped[:-1].strip()
                result[section] = {}
                continue
            if ":" not in stripped:
                errors.append(f"line {line_number}: expected key: value")
                section = None
                continue
            key, value = stripped.split(":", 1)
            result[key.strip()] = parse_scalar(value.strip())
            section = None
            continue
        if section is None:
            errors.append(f"line {line_number}: nested value without section")
            continue
        if ":" not in stripped:
            errors.append(f"line {line_number}: expected nested key: value")
            continue
        key, value = stripped.split(":", 1)
        nested = result.setdefault(section, {})
        if not isinstance(nested, dict):
            errors.append(f"line {line_number}: section {section!r} is not a mapping")
            continue
        nested[key.strip()] = parse_scalar(value.strip())

    return result, errors


def parse_scalar(value: str) -> Any:
    if value in {"", "null", "None", "~"}:
        return None
    if value in {"true", "True"}:
        return True
    if value in {"false", "False"}:
        return False
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    return value


def configured_document_homes(config: dict[str, Any]) -> dict[str, str | None]:
    data = config.get("data")
    documents = data.get("documents") if isinstance(data, dict) else None
    if not isinstance(documents, dict) or not documents:
        return dict(DEFAULT_DOCUMENTS)
    result: dict[str, str | None] = {}
    for key, value in documents.items():
        if value is None:
            result[str(key)] = None
        elif isinstance(value, str):
            result[str(key)] = value
    if "agents" not in result:
        result["agents"] = DEFAULT_DOCUMENTS["agents"]
    return result


def gitignore_ignores_waypoint_cache(root: Path) -> bool:
    path = root / ".gitignore"
    if not path.is_file():
        return False
    lines = [line.strip() for line in read_text(path).splitlines()]
    return ".waypoint/cache/" in lines or ".waypoint/cache" in lines


def broken_markdown_links(root: Path, max_links: int = 200) -> list[dict[str, str]]:
    broken: list[dict[str, str]] = []
    scanned = 0
    for path in iter_candidate_docs(root, max_files=500):
        if path.suffix.lower() not in {".md", ".markdown", ".mdown"} and path.name not in {
            "AGENTS.md",
            "CLAUDE.md",
            "README.md",
        }:
            continue
        text = read_text(path)
        for match in MARKDOWN_LINK_RE.finditer(text):
            scanned += 1
            if scanned > max_links:
                return broken
            target = match.group(1).strip()
            target_path = target.split("#", 1)[0]
            if not target_path or should_skip_link(target_path):
                continue
            candidate = (path.parent / target_path).resolve()
            try:
                candidate.relative_to(root)
            except ValueError:
                broken.append({"path": rel(root, path), "target": target})
                continue
            if not candidate.exists():
                broken.append({"path": rel(root, path), "target": target})
    return broken


def should_skip_link(target: str) -> bool:
    lowered = target.lower()
    return (
        lowered.startswith("http://")
        or lowered.startswith("https://")
        or lowered.startswith("mailto:")
        or lowered.startswith("tel:")
        or lowered.startswith("app://")
    )


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="replace")


def rel(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()
