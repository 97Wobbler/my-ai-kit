#!/usr/bin/env python3
"""Print concise Stateful status."""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("ERROR: PyYAML is required. Install with `pip install PyYAML`.", file=sys.stderr)
    sys.exit(2)


def git(root: Path, *args: str) -> str:
    result = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--tool", choices=["claude", "codex", "human", "other", "unknown"], help="current tool for WIP ownership hints")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    workplan = root / ".stateful" / "workplan.yaml"
    if not workplan.exists():
        print("Stateful is not installed: .stateful/workplan.yaml missing", file=sys.stderr)
        return 1
    data = yaml.safe_load(workplan.read_text(encoding="utf-8"))
    tasks = data.get("tasks") or []
    done = {task["id"] for task in tasks if task.get("done")}

    runnable = []
    blocked_human = []
    blocked_deps = []
    active_wip = []
    for task in tasks:
        if task.get("done"):
            continue
        wip = task.get("wip") or {}
        if wip.get("active"):
            active_wip.append(task)
            continue
        deps_done = all(dep in done for dep in (task.get("blocked_by") or []))
        if deps_done:
            if task.get("human_gate") in (None, "null") and task.get("execution_gate") in (None, "null"):
                runnable.append(task)
            else:
                blocked_human.append(task)
        else:
            blocked_deps.append(task)

    print(f"branch: {git(root, 'branch', '--show-current') or '(unknown)'}")
    print(f"last_commit: {git(root, 'log', '--oneline', '-1') or '(none)'}")
    print(f"workplan: {len(tasks)} tasks / {len(done)} done / {len(tasks) - len(done)} pending")
    print()
    print("active WIP claims:")
    if active_wip:
        for task in active_wip:
            wip = task.get("wip") or {}
            owner = wip.get("tool") or "unknown"
            started = wip.get("started_at") or "unknown time"
            summary = wip.get("summary") or task.get("summary") or task.get("name")
            handoff = ""
            if args.tool and owner != args.tool:
                handoff = " (recover before continuing)"
            print(f"  - {task['id']} [{owner}, {started}]{handoff}: {summary}")
    else:
        print("  - none")
    print()
    print("runnable automatic tasks:")
    if runnable:
        for task in runnable:
            print(f"  - {task['id']}: {task.get('summary') or task.get('name')}")
    else:
        print("  - none")
    print()
    print("ready but gated:")
    if blocked_human:
        for task in blocked_human:
            gate = task.get("human_gate") or task.get("execution_gate")
            print(f"  - {task['id']} [{gate}]: {task.get('summary') or task.get('name')}")
    else:
        print("  - none")
    print()
    print(f"dependency-blocked pending tasks: {len(blocked_deps)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
