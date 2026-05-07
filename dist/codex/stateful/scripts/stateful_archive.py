#!/usr/bin/env python3
"""Dry-run review for archiving completed Stateful workplan tasks."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    print("ERROR: PyYAML is required. Install with `pip install PyYAML`.", file=sys.stderr)
    sys.exit(2)


def load_workplan(root: Path) -> dict[str, Any]:
    path = root / ".stateful" / "workplan.yaml"
    if not path.exists():
        raise FileNotFoundError(".stateful/workplan.yaml missing")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("tasks"), list):
        raise ValueError("workplan must contain tasks: []")
    return data


def recommendation(task: dict[str, Any]) -> dict[str, str]:
    track = str(task.get("track") or "")
    gate = task.get("human_gate")
    outputs = task.get("output") or []
    if isinstance(outputs, str):
        outputs = [outputs]

    if track in {"naming", "release"} or gate in {"approve", "review", "execute"}:
        target = ".stateful/docs/decisions.md"
        action = "summarize decision"
    elif track in {"planning", "research"}:
        target = ".stateful/docs/roadmap.md"
        action = "preserve planning outcome"
    elif track in {"infra", "plugin"}:
        target = ".stateful/docs/status.md"
        action = "summarize shipped capability"
    else:
        target = ".stateful/docs/status.md"
        action = "review for durable summary"

    if not outputs:
        confidence = "low"
    elif any(str(output).startswith(".stateful/") for output in outputs):
        confidence = "medium"
    else:
        confidence = "high"

    return {"action": action, "target": target, "confidence": confidence}


def build_report(root: Path) -> dict[str, Any]:
    tasks = load_workplan(root).get("tasks") or []
    completed = [task for task in tasks if isinstance(task, dict) and task.get("done")]
    pending = [task for task in tasks if isinstance(task, dict) and not task.get("done")]
    items = []
    for task in completed:
        rec = recommendation(task)
        items.append(
            {
                "id": task.get("id"),
                "name": task.get("name"),
                "track": task.get("track"),
                "summary": task.get("summary"),
                "recommendation": rec["action"],
                "target_doc": rec["target"],
                "confidence": rec["confidence"],
            }
        )
    return {
        "completed_tasks": len(completed),
        "pending_tasks": len(pending),
        "dry_run": True,
        "items": items,
        "next_step": (
            "Review these recommendations with the user. Only edit docs or archive "
            "records after explicit approval."
        ),
    }


def print_markdown(report: dict[str, Any]) -> None:
    print("# Stateful Archive Dry Run")
    print()
    print(f"- Completed tasks: {report['completed_tasks']}")
    print(f"- Pending tasks: {report['pending_tasks']}")
    print("- Writes performed: none")
    print()
    print("| Task | Recommendation | Target | Confidence |")
    print("|---|---|---|---|")
    for item in report["items"]:
        label = f"{item['id']} {item['name']}"
        print(f"| {label} | {item['recommendation']} | `{item['target_doc']}` | {item['confidence']} |")
    print()
    print(report["next_step"])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--dry-run", action="store_true", help="review archive candidates without editing files")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    try:
        report = build_report(root)
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_markdown(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
