#!/usr/bin/env python3
"""Update .stateful/session/handoff.md."""
from __future__ import annotations

import argparse
import subprocess
import sys
from datetime import date
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
    parser.add_argument("--summary", default="Session closed.")
    parser.add_argument("--next", action="append", default=[], help="next action; repeatable")
    parser.add_argument("--tool", choices=["claude", "codex", "human", "other", "unknown"], default="unknown")
    parser.add_argument("--handoff-to", choices=["claude", "codex", "human", "other", "unknown"], default="unknown")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    workplan = root / ".stateful" / "workplan.yaml"
    if not workplan.exists():
        print("Stateful is not installed: .stateful/workplan.yaml missing", file=sys.stderr)
        return 1
    data = yaml.safe_load(workplan.read_text(encoding="utf-8"))
    tasks = data.get("tasks") or []
    done = {task["id"] for task in tasks if task.get("done")}
    pending = [task for task in tasks if not task.get("done")]
    active_wip = [task for task in pending if (task.get("wip") or {}).get("active")]
    runnable = [
        task for task in pending
        if all(dep in done for dep in (task.get("blocked_by") or [])) and not (task.get("wip") or {}).get("active")
    ]
    next_actions = args.next or [
        f"Review runnable task {task['id']}: {task.get('summary') or task.get('name')}"
        for task in runnable[:3]
    ] or ["Run `python3 scripts/stateful/status.py --tool <claude|codex>` and choose the next task."]

    text = f"""# Session Handoff

Updated: {date.today().isoformat()}

## Start Here

1. Read `CLAUDE.md` or `AGENTS.md`.
2. Read `.stateful/config.yaml`.
3. Read `.stateful/workplan.yaml`.
4. Read this handoff.
5. Run `python3 scripts/stateful/status.py --tool <claude|codex>`.
6. Check `git status --short --branch` and `git log --oneline -5`.

## Current Position

- Branch: {git(root, "branch", "--show-current") or "(unknown)"}
- Last commit: {git(root, "log", "--oneline", "-1") or "(none)"}
- Closing tool: {args.tool}
- Suggested next tool: {args.handoff_to}
- Uncommitted changes: {"yes" if git(root, "status", "--short") else "no"}
- Workplan: {len(tasks)} tasks / {len(done)} done / {len(pending)} pending

## Session Summary

{args.summary}

## Active WIP

"""
    if active_wip:
        for task in active_wip:
            wip = task.get("wip") or {}
            text += (
                f"- {task['id']} [{wip.get('tool') or 'unknown'}, "
                f"{wip.get('started_at') or 'unknown time'}]: "
                f"{wip.get('summary') or task.get('summary') or task.get('name')}\n"
            )
    else:
        text += "- None.\n"

    text += """
## Runnable Tasks

"""
    if runnable:
        for task in runnable:
            gate = task.get("human_gate") or task.get("execution_gate") or "auto"
            text += f"- {task['id']} [{gate}]: {task.get('summary') or task.get('name')}\n"
    else:
        text += "- None.\n"

    text += "\n## Next Actions\n\n"
    for item in next_actions:
        text += f"- {item}\n"
    text += "\n## Notes\n\n- Durable decisions belong in `.stateful/docs/decisions.md`.\n"

    handoff = root / ".stateful" / "session" / "handoff.md"
    handoff.parent.mkdir(parents=True, exist_ok=True)
    handoff.write_text(text, encoding="utf-8")
    print(f"updated {handoff.relative_to(root)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
