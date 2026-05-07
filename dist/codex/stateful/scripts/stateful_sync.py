#!/usr/bin/env python3
"""Generate .stateful/state.json from .stateful/workplan.yaml."""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    print("ERROR: PyYAML is required. Install with `pip install PyYAML`.", file=sys.stderr)
    sys.exit(2)


def normalize_gate(value: Any) -> Any:
    if value == "null":
        return None
    return value


def build_state(root: Path) -> dict[str, Any]:
    workplan_path = root / ".stateful" / "workplan.yaml"
    config_path = root / ".stateful" / "config.yaml"
    data = yaml.safe_load(workplan_path.read_text(encoding="utf-8"))
    config = yaml.safe_load(config_path.read_text(encoding="utf-8")) if config_path.exists() else {}
    tasks = data.get("tasks") or []
    done_ids = {task["id"] for task in tasks if task.get("done")}
    runnable = []
    blocked = []
    for task in tasks:
        if task.get("done"):
            continue
        blockers = task.get("blocked_by") or []
        deps_done = all(dep in done_ids for dep in blockers)
        node = {
            "id": task.get("id"),
            "name": task.get("name"),
            "summary": task.get("summary"),
            "track": task.get("track"),
            "human_gate": normalize_gate(task.get("human_gate")),
            "execution_gate": normalize_gate(task.get("execution_gate")),
            "blocked_by": blockers,
            "wip": task.get("wip"),
        }
        if deps_done:
            runnable.append(node)
        else:
            blocked.append(node)
    return {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "config": config,
        "meta": data.get("meta") or {},
        "counts": {
            "tasks": len(tasks),
            "done": len(done_ids),
            "pending": len(tasks) - len(done_ids),
        },
        "runnable": runnable,
        "blocked": blocked,
        "tasks": tasks,
    }


def comparable(payload: dict[str, Any]) -> dict[str, Any]:
    clone = dict(payload)
    clone["generated_at"] = "_"
    # Normalize YAML date objects and other scalar representation differences
    # through the same JSON boundary used for persisted state.
    return json.loads(json.dumps(clone, ensure_ascii=False, default=str))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    state_path = root / ".stateful" / "state.json"
    payload = build_state(root)
    new_text = json.dumps(payload, ensure_ascii=False, indent=2, default=str) + "\n"

    if args.check:
        if not state_path.exists():
            print("OUT OF DATE: .stateful/state.json missing", file=sys.stderr)
            return 1
        existing = json.loads(state_path.read_text(encoding="utf-8"))
        if comparable(existing) != comparable(payload):
            print("OUT OF DATE: .stateful/state.json differs from workplan", file=sys.stderr)
            return 1
        print("OK: .stateful/state.json is up to date")
        return 0

    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(new_text, encoding="utf-8")
    print(f"wrote {state_path.relative_to(root)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
