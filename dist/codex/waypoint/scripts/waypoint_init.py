#!/usr/bin/env python3
"""Create or audit a Waypoint docs-first repository harness."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

PLUGIN_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = PLUGIN_ROOT / "templates"
sys.path.insert(0, str(PLUGIN_ROOT / "mcp"))

from waypoint_mcp.inspectors import discover_repo, doctor_repo, resolve_repo_root  # noqa: E402

GREENFIELD_FILES = {
    "AGENTS.md": "AGENTS.template.md",
    "docs/vision.md": "docs/vision.md",
    "docs/ontology.md": "docs/ontology.md",
    "docs/architecture.md": "docs/architecture.md",
    "docs/workflows.md": "docs/workflows.md",
    "docs/decisions.md": "docs/decisions.md",
    "docs/plan.md": "docs/plan.md",
    "docs/todo.md": "docs/todo.md",
    "docs/ideas.md": "docs/ideas.md",
    "docs/workbench/README.md": "docs/workbench.README.md",
    ".waypoint/config.yaml": "waypoint.config.yaml",
}


def run_auto(repo_root: str | Path, with_claude: bool = False) -> dict[str, Any]:
    root = resolve_repo_root(repo_root)
    preflight = classify_preflight(root)
    recommended_mode = preflight["recommended_mode"]

    if recommended_mode == "greenfield-create":
        result = run_greenfield(root, with_claude=with_claude)
        result["preflight"] = preflight
        return result

    return {
        "mode": recommended_mode,
        "repo_root": str(root),
        "success": True,
        "writes": [],
        "preflight": preflight,
        "message": mode_message(recommended_mode),
    }


def classify_preflight(repo_root: str | Path) -> dict[str, Any]:
    root = resolve_repo_root(repo_root)
    discovery = discover_repo(root)
    doctor = doctor_repo(root)
    summary = discovery["summary"]
    marker_blocks = discovery["waypoint"]["marker_blocks"]
    has_waypoint = summary["has_waypoint_config"] or bool(marker_blocks["routers_with_markers"])
    coherent_docs = has_coherent_docs(discovery)

    if has_waypoint and doctor["status"] == "fail":
        recommended_mode = "repair"
    elif has_waypoint:
        recommended_mode = "no-op"
    elif coherent_docs:
        recommended_mode = "brownfield-adopt"
    else:
        recommended_mode = "greenfield-create"

    return {
        "recommended_mode": recommended_mode,
        "has_waypoint": has_waypoint,
        "coherent_docs": coherent_docs,
        "discover": discovery,
        "doctor": doctor,
    }


def has_coherent_docs(discovery: dict[str, Any]) -> bool:
    summary = discovery["summary"]
    roles = {
        item["role"]
        for item in discovery["documents"]
        if item.get("confidence") in {"high", "medium"}
    }
    core_roles = {"router", "architecture", "workflows", "decisions", "plan", "vision", "ontology"}
    return bool(summary["has_agents"] and summary["has_docs_dir"] and roles & core_roles)


def mode_message(mode: str) -> str:
    if mode == "repair":
        return (
            "Waypoint appears to be installed, but doctor found structural problems. "
            "Review the findings and approve repairs before writing durable changes."
        )
    if mode == "brownfield-adopt":
        return (
            "This repository already has a coherent documentation system. Preserve existing "
            "document homes and propose a locator plus minimal AGENTS.md marker before writing."
        )
    if mode == "no-op":
        return "Waypoint already appears initialized. No files were created."
    return "Ready for greenfield creation."


def run_greenfield(repo_root: str | Path, with_claude: bool = False) -> dict[str, Any]:
    root = resolve_repo_root(repo_root)
    created: list[str] = []
    unchanged: list[str] = []
    updated: list[str] = []
    conflicts: list[str] = []

    files = dict(GREENFIELD_FILES)
    if with_claude:
        files["CLAUDE.md"] = "CLAUDE.template.md"

    for relative, template_name in files.items():
        target = root / relative
        template = TEMPLATE_ROOT / template_name
        text = render_template(template.read_text(encoding="utf-8"), with_claude=with_claude)
        outcome = write_if_absent_or_same(target, text)
        if outcome == "created":
            created.append(relative)
        elif outcome == "unchanged":
            unchanged.append(relative)
        else:
            conflicts.append(relative)

    cache_dir = root / ".waypoint" / "cache"
    if not cache_dir.exists():
        cache_dir.mkdir(parents=True)
        created.append(".waypoint/cache/")

    gitignore_result = ensure_gitignore(root)
    if gitignore_result == "created":
        created.append(".gitignore")
    elif gitignore_result == "updated":
        updated.append(".gitignore")
    elif gitignore_result == "unchanged":
        unchanged.append(".gitignore")

    doctor = doctor_repo(root)
    return {
        "mode": "greenfield",
        "repo_root": str(root),
        "with_claude": with_claude,
        "success": not conflicts,
        "created": created,
        "updated": updated,
        "unchanged": unchanged,
        "conflicts": conflicts,
        "doctor": doctor,
    }


def run_brownfield_audit(repo_root: str | Path) -> dict[str, Any]:
    root = resolve_repo_root(repo_root)
    return {
        "mode": "brownfield-audit",
        "repo_root": str(root),
        "success": True,
        "writes": [],
        "discover": discover_repo(root),
        "doctor": doctor_repo(root),
    }


def render_template(text: str, *, with_claude: bool) -> str:
    claude_path = "CLAUDE.md" if with_claude else "null"
    claude_wrapper = "true" if with_claude else "false"
    return text.replace("{{CLAUDE_PATH}}", claude_path).replace(
        "{{CLAUDE_WRAPPER}}",
        claude_wrapper,
    )


def write_if_absent_or_same(path: Path, text: str) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        existing = path.read_text(encoding="utf-8")
        if existing == text:
            return "unchanged"
        return "conflict"
    path.write_text(text, encoding="utf-8")
    return "created"


def ensure_gitignore(root: Path) -> str:
    path = root / ".gitignore"
    line = ".waypoint/cache/"
    if not path.exists():
        path.write_text("# Waypoint\n.waypoint/cache/\n", encoding="utf-8")
        return "created"
    text = path.read_text(encoding="utf-8")
    existing = {item.strip() for item in text.splitlines()}
    if line in existing or ".waypoint/cache" in existing:
        return "unchanged"
    prefix = "" if text.endswith("\n") else "\n"
    path.write_text(f"{text}{prefix}\n# Waypoint\n{line}\n", encoding="utf-8")
    return "updated"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".", help="Repository root.")
    parser.add_argument(
        "--mode",
        choices=["auto", "greenfield", "brownfield-audit"],
        default="auto",
        help="Creation or audit mode.",
    )
    parser.add_argument(
        "--with-claude",
        action="store_true",
        help="Generate a thin CLAUDE.md wrapper in greenfield mode.",
    )
    args = parser.parse_args()

    if args.mode == "auto":
        result = run_auto(args.repo_root, with_claude=args.with_claude)
    elif args.mode == "greenfield":
        result = run_greenfield(args.repo_root, with_claude=args.with_claude)
    else:
        result = run_brownfield_audit(args.repo_root)

    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result.get("success") else 2


if __name__ == "__main__":
    raise SystemExit(main())
