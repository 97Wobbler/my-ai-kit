#!/usr/bin/env python3
"""Validate a Stateful workplan.

This script is designed to work both from the plugin repository and after it
has been copied into a target repository under scripts/stateful/.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover - depends on host environment
    print("ERROR: PyYAML is required. Install with `pip install PyYAML`.", file=sys.stderr)
    sys.exit(2)


VALID_HUMAN_GATES = {None, "approve", "execute", "debate", "review"}
VALID_EXECUTION_GATES = {None, "batch"}
VALID_WIP_TOOLS = {None, "claude", "codex", "human", "other", "unknown"}


def normalize_gate(value: Any) -> Any:
    if value == "null":
        return None
    return value


def load_workplan(root: Path) -> dict[str, Any]:
    path = root / ".stateful" / "workplan.yaml"
    if not path.exists():
        raise FileNotFoundError(f"{path} does not exist")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("workplan root must be a mapping")
    if not isinstance(data.get("tasks"), list):
        raise ValueError("workplan must contain tasks: []")
    return data


def validate(data: dict[str, Any], root: Path, check_outputs: bool = True) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    tasks = data.get("tasks") or []

    seen: set[str] = set()
    task_ids: set[str] = set()
    for task in tasks:
        if not isinstance(task, dict):
            errors.append("each task must be a mapping")
            continue
        tid = task.get("id")
        if not tid:
            errors.append("task missing id")
            continue
        if tid in seen:
            errors.append(f"duplicate task id: {tid}")
        seen.add(tid)
        task_ids.add(tid)

        for field in ("name", "summary", "track", "blocked_by", "human_gate", "done", "spec"):
            if field not in task:
                errors.append(f"{tid}: missing required field {field}")

        if not isinstance(task.get("blocked_by", []), list):
            errors.append(f"{tid}: blocked_by must be a list")

        human_gate = normalize_gate(task.get("human_gate"))
        if human_gate not in VALID_HUMAN_GATES:
            errors.append(f"{tid}: unknown human_gate {human_gate!r}")

        execution_gate = normalize_gate(task.get("execution_gate"))
        if execution_gate not in VALID_EXECUTION_GATES:
            errors.append(f"{tid}: unknown execution_gate {execution_gate!r}")

        if task.get("protected_human_only") and human_gate == "debate":
            errors.append(f"{tid}: protected_human_only tasks cannot use human_gate=debate")

        if human_gate == "execute" and not task.get("done") and not task.get("human_artifact_path"):
            warnings.append(f"{tid}: pending execute task should declare human_artifact_path")

        if task.get("done") and check_outputs:
            outputs = task.get("output") or []
            if isinstance(outputs, str):
                outputs = [outputs]
            for output in outputs:
                if output and not (root / output).exists():
                    warnings.append(f"{tid}: output path missing: {output}")

        wip = task.get("wip")
        if wip is not None:
            if not isinstance(wip, dict):
                errors.append(f"{tid}: wip must be a mapping")
            else:
                if not isinstance(wip.get("active", False), bool):
                    errors.append(f"{tid}: wip.active must be boolean")
                if wip.get("tool") not in VALID_WIP_TOOLS:
                    errors.append(f"{tid}: unknown wip.tool {wip.get('tool')!r}")
                if wip.get("active") and task.get("done"):
                    warnings.append(f"{tid}: done task still has active WIP claim")
                if wip.get("active") and not wip.get("summary"):
                    warnings.append(f"{tid}: active WIP should include wip.summary for cross-tool recovery")

    meta = data.get("meta") or {}
    retired_ids = meta.get("retired_ids") or {}
    if retired_ids and not isinstance(retired_ids, dict):
        errors.append("meta.retired_ids must be a mapping")
    for rid in retired_ids:
        matching = [t for t in tasks if isinstance(t, dict) and t.get("id") == rid]
        if not matching:
            errors.append(f"retired id {rid} has no tombstone task")
            continue
        task = matching[0]
        if not task.get("retired") or not task.get("done"):
            errors.append(f"retired id {rid} must have retired: true and done: true")

    for task in tasks:
        if not isinstance(task, dict) or not task.get("id"):
            continue
        for blocker in task.get("blocked_by") or []:
            if blocker not in task_ids:
                errors.append(f"{task['id']}: blocked_by references missing task {blocker!r}")

    deps = {
        task["id"]: [b for b in (task.get("blocked_by") or []) if b in task_ids]
        for task in tasks
        if isinstance(task, dict) and task.get("id")
    }
    color = {tid: 0 for tid in deps}
    cycle_members: set[str] = set()

    def visit(node: str, stack: list[str]) -> None:
        color[node] = 1
        stack.append(node)
        for nxt in deps.get(node, []):
            if color[nxt] == 1:
                cycle_members.update(stack[stack.index(nxt):])
            elif color[nxt] == 0:
                visit(nxt, stack)
        stack.pop()
        color[node] = 2

    for tid in list(deps):
        if color[tid] == 0:
            visit(tid, [])

    if cycle_members:
        errors.append(f"dependency cycle detected: {sorted(cycle_members)}")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="target repository root")
    parser.add_argument("--json", action="store_true", help="emit machine-readable result")
    parser.add_argument("--no-output-check", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    try:
        data = load_workplan(root)
        errors, warnings = validate(data, root, check_outputs=not args.no_output_check)
    except Exception as exc:
        errors, warnings = [str(exc)], []

    if args.json:
        print(json.dumps({"errors": errors, "warnings": warnings}, indent=2))
    else:
        for warning in warnings:
            print(f"WARN: {warning}", file=sys.stderr)
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        if not errors:
            print(f"OK: Stateful workplan valid ({len(warnings)} warnings)")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
