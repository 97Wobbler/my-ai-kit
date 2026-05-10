"""Deterministic Autorun MCP plan operations."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import PurePosixPath
from typing import Any, Mapping
from uuid import uuid4

from .schema import (
    has_metadata_issue,
    has_split_issue,
    normalize_human_gate,
    normalize_output,
    validate_plan,
)
from .state import load_plan, resolve_state_root, save_plan

PENDING = "pending"
STARTED = "started"
VERIFIED = "verified"
COMMITTED = "committed"
RETIRED = "retired"


def plan_create(arguments: Mapping[str, Any]) -> dict[str, Any]:
    meta = arguments.get("meta")
    tasks = arguments.get("tasks")
    if not isinstance(meta, dict):
        raise ValueError("meta must be an object")
    if not isinstance(tasks, list) or not all(isinstance(task, dict) for task in tasks):
        raise ValueError("tasks must be a list of objects")

    now = _now()
    plan_id = arguments.get("plan_id")
    if plan_id is None:
        plan_id = f"plan-{uuid4().hex[:12]}"
    if not isinstance(plan_id, str) or not plan_id:
        raise ValueError("plan_id must be a non-empty string")

    run_policy = arguments.get("run_policy", {})
    if not isinstance(run_policy, dict):
        raise ValueError("run_policy must be an object when provided")

    normalized_tasks = [_normalize_task(task) for task in tasks]
    plan = {
        "plan_id": plan_id,
        "created_at": now,
        "updated_at": now,
        "run_policy": run_policy,
        "task_status": {
            task["id"]: COMMITTED if task.get("done") else PENDING
            for task in normalized_tasks
            if isinstance(task.get("id"), str)
        },
        "meta": meta,
        "tasks": normalized_tasks,
    }
    state_root = resolve_state_root(arguments)
    path = save_plan(state_root, plan)
    validation = validate_plan(plan)
    return {"plan": plan, "path": str(path), "validation": validation}


def plan_validate(arguments: Mapping[str, Any]) -> dict[str, Any]:
    plan = _load(arguments)
    return {"plan_id": plan["plan_id"], "validation": validate_plan(plan)}


def plan_refine(arguments: Mapping[str, Any]) -> dict[str, Any]:
    plan = _load(arguments)
    validation = validate_plan(plan)
    ready_human_gates = _ready_human_gates(plan)

    if validation.get("errors"):
        action = "needs_metadata" if has_metadata_issue(validation) else "needs_metadata"
    elif has_split_issue(validation):
        action = "needs_split"
    elif has_metadata_issue(validation):
        action = "needs_metadata"
    elif ready_human_gates:
        action = "blocked_by_human_gate"
    else:
        action = "ready"

    return {
        "plan_id": plan["plan_id"],
        "next_action": action,
        "validation": validation,
        "human_gates": ready_human_gates,
    }


def task_split(arguments: Mapping[str, Any]) -> dict[str, Any]:
    task_id = _required_str(arguments, "task_id")
    replacements = arguments.get("replacement_tasks")
    if not isinstance(replacements, list) or not all(isinstance(task, dict) for task in replacements):
        raise ValueError("replacement_tasks must be a list of objects")

    plan = _load(arguments)
    tasks = plan["tasks"]
    original = _task_by_id(plan, task_id)
    if original.get("done") and not original.get("retired"):
        raise ValueError(f"cannot split completed task {task_id}")

    existing_ids = {task.get("id") for task in tasks if isinstance(task, dict)}
    normalized_replacements = []
    for task in replacements:
        replacement = _normalize_task(task)
        replacement_id = replacement.get("id")
        if not isinstance(replacement_id, str) or not replacement_id:
            raise ValueError("replacement task id must be a non-empty string")
        if replacement_id in existing_ids:
            raise ValueError(f"replacement task id already exists: {replacement_id}")
        replacement["replaces"] = task_id
        normalized_replacements.append(replacement)
        existing_ids.add(replacement_id)

    original["retired"] = True
    original["done"] = True
    plan["task_status"][task_id] = RETIRED
    for replacement in normalized_replacements:
        tasks.append(replacement)
        plan["task_status"][replacement["id"]] = PENDING

    _touch_and_save(arguments, plan)
    return {"plan_id": plan["plan_id"], "retired": task_id, "added": [task["id"] for task in normalized_replacements]}


def next_batch(arguments: Mapping[str, Any]) -> dict[str, Any]:
    plan = _load(arguments)
    done_ids = _done_ids(plan)
    selected: list[dict[str, Any]] = []
    selected_outputs: list[str] = []

    for task in _active_tasks(plan):
        task_id = task["id"]
        if task.get("done"):
            continue
        if normalize_human_gate(task.get("human_gate")) is not None:
            continue
        if plan.get("task_status", {}).get(task_id) not in (None, PENDING):
            continue
        if not all(dep in done_ids for dep in task.get("blocked_by") or []):
            continue

        outputs = normalize_output(task.get("output"))
        if not outputs:
            continue
        if any(_paths_overlap(output, existing) for output in outputs for existing in selected_outputs):
            continue
        selected.append(task)
        selected_outputs.extend(outputs)

    return {"plan_id": plan["plan_id"], "tasks": selected, "task_ids": [task["id"] for task in selected]}


def task_mark_started(arguments: Mapping[str, Any]) -> dict[str, Any]:
    return _transition(arguments, PENDING, STARTED, done=False)


def task_mark_verified(arguments: Mapping[str, Any]) -> dict[str, Any]:
    return _transition(arguments, STARTED, VERIFIED, done=False)


def task_mark_committed(arguments: Mapping[str, Any]) -> dict[str, Any]:
    return _transition(arguments, VERIFIED, COMMITTED, done=True)


def plan_status(arguments: Mapping[str, Any]) -> dict[str, Any]:
    plan = _load(arguments)
    done_ids = _done_ids(plan)
    tasks = _active_tasks(plan)
    runnable = []
    blocked = []
    human_gates = []
    active = []

    for task in tasks:
        task_id = task["id"]
        status = plan.get("task_status", {}).get(task_id, PENDING)
        blockers_done = all(dep in done_ids for dep in task.get("blocked_by") or [])
        gate = normalize_human_gate(task.get("human_gate"))

        if status in (STARTED, VERIFIED):
            active.append(task_id)
        if task.get("done"):
            continue
        if blockers_done and gate is None and status in (PENDING, None):
            runnable.append(task_id)
        elif blockers_done and gate is not None:
            human_gates.append(task_id)
        elif not blockers_done:
            blocked.append(task_id)

    total = len(tasks)
    done = len([task for task in tasks if task.get("done")])
    return {
        "plan_id": plan["plan_id"],
        "progress": {"total": total, "done": done, "pending": total - done, "percent": 100 if total == 0 else round(done * 100 / total, 2)},
        "runnable": runnable,
        "blocked": blocked,
        "human_gates": human_gates,
        "active": active,
    }


def _transition(arguments: Mapping[str, Any], expected: str, next_status: str, done: bool) -> dict[str, Any]:
    task_id = _required_str(arguments, "task_id")
    plan = _load(arguments)
    task = _task_by_id(plan, task_id)
    current = plan.setdefault("task_status", {}).get(task_id, COMMITTED if task.get("done") else PENDING)
    if current != expected:
        raise ValueError(f"{task_id}: invalid lifecycle transition {current} -> {next_status}; expected {expected}")
    task["done"] = done
    plan["task_status"][task_id] = next_status
    _touch_and_save(arguments, plan)
    return {"plan_id": plan["plan_id"], "task_id": task_id, "status": next_status}


def _load(arguments: Mapping[str, Any]) -> dict[str, Any]:
    plan_id = _required_str(arguments, "plan_id")
    return load_plan(resolve_state_root(arguments), plan_id)


def _touch_and_save(arguments: Mapping[str, Any], plan: dict[str, Any]) -> None:
    plan["updated_at"] = _now()
    save_plan(resolve_state_root(arguments), plan)


def _normalize_task(task: Mapping[str, Any]) -> dict[str, Any]:
    normalized = dict(task)
    if "blocked_by" not in normalized:
        normalized["blocked_by"] = []
    if "done" not in normalized:
        normalized["done"] = False
    if "human_gate" in normalized:
        normalized["human_gate"] = normalize_human_gate(normalized["human_gate"])
    else:
        normalized["human_gate"] = None
    return normalized


def _task_by_id(plan: Mapping[str, Any], task_id: str) -> dict[str, Any]:
    for task in plan.get("tasks", []):
        if isinstance(task, dict) and task.get("id") == task_id:
            return task
    raise ValueError(f"task not found: {task_id}")


def _active_tasks(plan: Mapping[str, Any]) -> list[dict[str, Any]]:
    return [
        task
        for task in plan.get("tasks", [])
        if isinstance(task, dict) and isinstance(task.get("id"), str) and not task.get("retired")
    ]


def _done_ids(plan: Mapping[str, Any]) -> set[str]:
    return {
        task["id"]
        for task in plan.get("tasks", [])
        if isinstance(task, dict) and isinstance(task.get("id"), str) and task.get("done")
    }


def _ready_human_gates(plan: Mapping[str, Any]) -> list[str]:
    done_ids = _done_ids(plan)
    ready = []
    for task in _active_tasks(plan):
        if task.get("done"):
            continue
        if normalize_human_gate(task.get("human_gate")) is None:
            continue
        if all(dep in done_ids for dep in task.get("blocked_by") or []):
            ready.append(task["id"])
    return ready


def _paths_overlap(left: str, right: str) -> bool:
    left_norm = _normalize_path(left)
    right_norm = _normalize_path(right)
    if left_norm == right_norm:
        return True
    left_parts = PurePosixPath(left_norm).parts
    right_parts = PurePosixPath(right_norm).parts
    return left_parts == right_parts[: len(left_parts)] or right_parts == left_parts[: len(right_parts)]


def _normalize_path(path: str) -> str:
    normalized = str(PurePosixPath(path.replace("\\", "/")))
    return normalized.rstrip("/") or "."


def _required_str(arguments: Mapping[str, Any], key: str) -> str:
    value = arguments.get(key)
    if not isinstance(value, str) or not value:
        raise ValueError(f"{key} must be a non-empty string")
    return value


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
