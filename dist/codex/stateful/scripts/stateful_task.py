#!/usr/bin/env python3
"""Claim or clear Stateful task WIP metadata."""
from __future__ import annotations

import argparse
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    print("ERROR: PyYAML is required. Install with `pip install PyYAML`.", file=sys.stderr)
    sys.exit(2)


VALID_TOOLS = {"claude", "codex", "human", "other", "unknown"}


def git(root: Path, *args: str) -> str:
    result = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else ""


def load(root: Path) -> tuple[Path, dict[str, Any]]:
    path = root / ".stateful" / "workplan.yaml"
    if not path.exists():
        raise FileNotFoundError("Stateful is not installed: .stateful/workplan.yaml missing")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("tasks"), list):
        raise ValueError("workplan must contain tasks: []")
    return path, data


def find_task(data: dict[str, Any], task_id: str) -> dict[str, Any]:
    for task in data.get("tasks") or []:
        if task.get("id") == task_id:
            return task
    raise ValueError(f"task not found: {task_id}")


def save(path: Path, data: dict[str, Any]) -> None:
    meta = data.setdefault("meta", {})
    meta["last_updated"] = datetime.now(timezone.utc).date().isoformat()
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    sub = parser.add_subparsers(dest="command", required=True)

    claim = sub.add_parser("claim", help="mark a task as actively in progress")
    claim.add_argument("task_id")
    claim.add_argument("--tool", default="unknown", choices=sorted(VALID_TOOLS))
    claim.add_argument("--summary", default="", help="short description of the partial work")
    claim.add_argument("--force", action="store_true", help="replace an existing active WIP claim")

    clear = sub.add_parser("clear", help="clear active WIP metadata for a task")
    clear.add_argument("task_id")

    args = parser.parse_args()
    root = Path(args.root).resolve()

    try:
        path, data = load(root)
        task = find_task(data, args.task_id)
        if args.command == "claim":
            existing = task.get("wip") or {}
            if existing.get("active") and not args.force:
                owner = existing.get("tool") or "unknown"
                started = existing.get("started_at") or "unknown time"
                print(
                    f"FAIL: {args.task_id} already has active WIP by {owner} since {started}; "
                    "use --force only after recovery.",
                    file=sys.stderr,
                )
                return 1
            task["wip"] = {
                "active": True,
                "tool": args.tool,
                "started_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
                "branch": git(root, "branch", "--show-current") or None,
                "commit": git(root, "rev-parse", "--short", "HEAD") or None,
                "summary": args.summary or None,
            }
            save(path, data)
            print(f"claimed {args.task_id} for {args.tool}")
        elif args.command == "clear":
            previous = task.get("wip") or {}
            task["wip"] = {
                "active": False,
                "tool": previous.get("tool"),
                "started_at": previous.get("started_at"),
                "cleared_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
                "summary": previous.get("summary"),
            }
            save(path, data)
            print(f"cleared WIP for {args.task_id}")
        return 0
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
