#!/usr/bin/env python3
"""Propose workplan tasks from .stateful/docs/roadmap.md."""
from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    print("ERROR: PyYAML is required. Install with `pip install PyYAML`.", file=sys.stderr)
    sys.exit(2)


HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


def load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a mapping")
    return data


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def roadmap_path(root: Path, config: dict[str, Any]) -> Path:
    paths = config.get("paths") or {}
    configured = paths.get("roadmap") or ".stateful/docs/roadmap.md"
    return root / configured


def parse_roadmap(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"roadmap missing: {path}")
    items: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    body: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = HEADING_RE.match(line)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            if current is not None and level <= 3:
                current["body"] = "\n".join(body).strip()
                items.append(current)
                current = None
                body = []
            if level == 3:
                current = {"title": title}
                body = []
            continue
        if current is not None:
            body.append(line)
    if current is not None:
        current["body"] = "\n".join(body).strip()
        items.append(current)
    return items


def next_task_id(tasks: list[dict[str, Any]], prefix: str) -> str:
    max_number = 0
    pattern = re.compile(rf"^{re.escape(prefix)}(\d+)$")
    for task in tasks:
        match = pattern.match(str(task.get("id") or ""))
        if match:
            max_number = max(max_number, int(match.group(1)))
    return f"{prefix}{max_number + 1:03d}"


def first_paragraph(text: str) -> str:
    for block in re.split(r"\n\s*\n", text.strip()):
        cleaned = " ".join(line.strip("- ").strip() for line in block.splitlines()).strip()
        if cleaned:
            return cleaned
    return "Convert this roadmap item into an executable Stateful task."


def build_proposals(root: Path) -> tuple[Path, dict[str, Any], list[dict[str, Any]]]:
    config_path = root / ".stateful" / "config.yaml"
    workplan_path = root / ".stateful" / "workplan.yaml"
    config = load_yaml(config_path)
    workplan = load_yaml(workplan_path)
    tasks = workplan.get("tasks") or []
    if not isinstance(tasks, list):
        raise ValueError("workplan tasks must be a list")

    existing_names = {
        normalize(str(task.get("name") or ""))
        for task in tasks
        if isinstance(task, dict)
    }
    existing_specs = normalize("\n".join(str(task.get("spec") or "") for task in tasks if isinstance(task, dict)))
    prefix = ((config.get("policies") or {}).get("task_id_prefix")) or "R"
    next_id = next_task_id(tasks, prefix)
    last_task_id = tasks[-1].get("id") if tasks and isinstance(tasks[-1], dict) else None

    proposals: list[dict[str, Any]] = []
    for item in parse_roadmap(roadmap_path(root, config)):
        title = item["title"]
        title_key = normalize(title)
        if not title_key or title_key in existing_names or title_key in existing_specs:
            continue
        proposal = {
            "id": next_id,
            "name": title,
            "summary": first_paragraph(item.get("body") or ""),
            "track": "planning",
            "blocked_by": [last_task_id] if last_task_id else [],
            "human_gate": "approve",
            "execution_gate": None,
            "done": False,
            "spec": (
                f"Convert the roadmap item `{title}` into a concrete implementation plan.\n\n"
                f"Roadmap context:\n{(item.get('body') or '').strip()}\n"
            ),
            "output": [],
            "verify_checks": [
                "python3 scripts/stateful/validate-workplan.py passes",
                "python3 scripts/stateful/sync-state.py --check passes",
            ],
            "wip": {
                "active": False,
                "tool": None,
                "started_at": None,
                "branch": None,
                "commit": None,
                "summary": None,
            },
        }
        proposals.append(proposal)
        last_task_id = next_id
        next_id = f"{prefix}{int(next_id.removeprefix(prefix)) + 1:03d}"
    return workplan_path, workplan, proposals


def print_proposals(proposals: list[dict[str, Any]]) -> None:
    if not proposals:
        print("No roadmap items without matching workplan coverage were found.")
        return
    print(f"Proposed {len(proposals)} workplan task(s):")
    print(yaml.safe_dump(proposals, sort_keys=False, allow_unicode=True).rstrip())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--dry-run", action="store_true", help="print proposed tasks without editing files")
    parser.add_argument("--apply", action="store_true", help="append proposed tasks to .stateful/workplan.yaml")
    args = parser.parse_args()

    if args.dry_run and args.apply:
        print("ERROR: choose only one of --dry-run or --apply", file=sys.stderr)
        return 2
    dry_run = args.dry_run or not args.apply
    root = Path(args.root).resolve()

    try:
        workplan_path, workplan, proposals = build_proposals(root)
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    if dry_run:
        print_proposals(proposals)
        return 0

    if not proposals:
        print("No workplan changes needed.")
        return 0

    workplan.setdefault("tasks", []).extend(proposals)
    meta = workplan.setdefault("meta", {})
    meta["last_updated"] = datetime.now(timezone.utc).date().isoformat()
    workplan_path.write_text(yaml.safe_dump(workplan, sort_keys=False, allow_unicode=True), encoding="utf-8")
    print(f"Appended {len(proposals)} task(s) to {workplan_path.relative_to(root)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
