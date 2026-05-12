"""Deterministic Autorun MCP plan operations."""

from __future__ import annotations

from pathlib import PurePosixPath
from typing import Any, Mapping

from .schema import (
    has_metadata_issue,
    has_split_issue,
    normalize_human_gate,
    normalize_output,
    validate_plan,
)
from .workplan_io import (
    COMMITTED,
    PENDING,
    RETIRED,
    STARTED,
    VERIFIED,
    load_workplan,
    normalize_lifecycle,
    normalize_task_status,
    now_utc,
    save_workplan,
)


def plan_create(arguments: Mapping[str, Any]) -> dict[str, Any]:
    meta = arguments.get("meta")
    tasks = arguments.get("tasks")
    if not isinstance(meta, dict):
        raise ValueError("meta must be an object")
    if not isinstance(tasks, list) or not all(isinstance(task, dict) for task in tasks):
        raise ValueError("tasks must be a list of objects")

    run_policy = arguments.get("run_policy", {})
    if run_policy is not None and not isinstance(run_policy, dict):
        raise ValueError("run_policy must be an object when provided")

    normalized_tasks = [_normalize_task(task) for task in tasks]
    plan = {
        "plan_id": _plan_id(arguments),
        "meta": dict(meta),
        "tasks": normalized_tasks,
    }
    if run_policy:
        plan["meta"].setdefault("run_policy", run_policy)

    path = save_workplan(arguments, plan)
    plan["workplan_path"] = path
    validation = validate_plan(plan)
    return {"plan": plan, "path": path, "workplan_path": path, "validation": validation}


def plan_validate(arguments: Mapping[str, Any]) -> dict[str, Any]:
    plan = _load(arguments)
    return {"plan_id": plan["plan_id"], "workplan_path": plan["workplan_path"], "validation": validate_plan(plan)}


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
        "workplan_path": plan["workplan_path"],
        "next_action": action,
        "validation": validation,
        "human_gates": ready_human_gates,
    }


def task_split(arguments: Mapping[str, Any]) -> dict[str, Any]:
    task_id = _required_str(arguments, "task_id")
    replacements = arguments.get("replacement_tasks")
    if not isinstance(replacements, list) or not all(isinstance(task, dict) for task in replacements):
        raise ValueError("replacement_tasks must be a list of objects")

    plan = _load_checked(arguments)
    tasks = plan["tasks"]
    original = _task_by_id(plan, task_id)
    if _task_status(original) == COMMITTED and not original.get("retired"):
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
    original["status"] = RETIRED
    original["lifecycle"] = _lifecycle(original)
    for replacement in normalized_replacements:
        tasks.append(replacement)

    _save(arguments, plan)
    return {
        "plan_id": plan["plan_id"],
        "workplan_path": plan["workplan_path"],
        "retired": task_id,
        "added": [task["id"] for task in normalized_replacements],
    }


def next_batch(arguments: Mapping[str, Any]) -> dict[str, Any]:
    plan = _load_checked(arguments)
    done_ids = _done_ids(plan)
    selected: list[dict[str, Any]] = []
    selected_outputs: list[str] = []

    for task in _active_tasks(plan):
        task_id = task["id"]
        if task.get("done"):
            continue
        if normalize_human_gate(task.get("human_gate")) is not None:
            continue
        if _task_status(task) != PENDING:
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

    return {
        "plan_id": plan["plan_id"],
        "workplan_path": plan["workplan_path"],
        "tasks": selected,
        "task_ids": [task["id"] for task in selected],
    }


def task_mark_started(arguments: Mapping[str, Any]) -> dict[str, Any]:
    return _transition(arguments, PENDING, STARTED, timestamp_field="started_at", done=False)


def task_mark_verified(arguments: Mapping[str, Any]) -> dict[str, Any]:
    worker_id = arguments.get("worker_id")
    return _transition(
        arguments,
        STARTED,
        VERIFIED,
        timestamp_field="verified_at",
        done=False,
        lifecycle_updates={"worker_id": worker_id} if isinstance(worker_id, str) and worker_id else None,
    )


def task_mark_committed(arguments: Mapping[str, Any]) -> dict[str, Any]:
    commit = arguments.get("commit")
    return _transition(
        arguments,
        VERIFIED,
        COMMITTED,
        timestamp_field="committed_at",
        done=True,
        lifecycle_updates={"commit": commit} if isinstance(commit, str) and commit else None,
    )


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
        status = _task_status(task)
        blockers_done = all(dep in done_ids for dep in task.get("blocked_by") or [])
        gate = normalize_human_gate(task.get("human_gate"))

        if status in (STARTED, VERIFIED):
            active.append(task_id)
        if task.get("done"):
            continue
        if blockers_done and gate is None and status == PENDING:
            runnable.append(task_id)
        elif blockers_done and gate is not None:
            human_gates.append(task_id)
        elif not blockers_done:
            blocked.append(task_id)

    total = len(tasks)
    done = len([task for task in tasks if task.get("done")])
    return {
        "plan_id": plan["plan_id"],
        "workplan_path": plan["workplan_path"],
        "progress": {
            "total": total,
            "done": done,
            "pending": total - done,
            "percent": 100 if total == 0 else round(done * 100 / total, 2),
        },
        "runnable": runnable,
        "blocked": blocked,
        "human_gates": human_gates,
        "active": active,
    }


def _transition(
    arguments: Mapping[str, Any],
    expected: str,
    next_status: str,
    *,
    timestamp_field: str,
    done: bool,
    lifecycle_updates: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    task_id = _required_str(arguments, "task_id")
    plan = _load(arguments)
    _raise_if_invalid(plan)
    task = _task_by_id(plan, task_id)
    current = _task_status(task)
    if current != expected:
        raise ValueError(f"{task_id}: invalid lifecycle transition {current} -> {next_status}; expected {expected}")
    task["done"] = done
    task["status"] = next_status
    lifecycle = _lifecycle(task)
    lifecycle[timestamp_field] = now_utc()
    if lifecycle_updates:
        for key, value in lifecycle_updates.items():
            if value is not None:
                lifecycle[key] = value
    task["lifecycle"] = lifecycle
    _save(arguments, plan)
    return {
        "plan_id": plan["plan_id"],
        "workplan_path": plan["workplan_path"],
        "task_id": task_id,
        "status": next_status,
    }


def _load(arguments: Mapping[str, Any]) -> dict[str, Any]:
    return load_workplan(arguments)


def _load_checked(arguments: Mapping[str, Any]) -> dict[str, Any]:
    plan = _load(arguments)
    _raise_if_invalid(plan)
    return plan


def _raise_if_invalid(plan: Mapping[str, Any]) -> None:
    validation = validate_plan(plan)
    if validation.get("errors"):
        codes = ", ".join(str(issue.get("code")) for issue in validation["errors"])
        raise ValueError(f"plan validation failed: {codes}")


def _save(arguments: Mapping[str, Any], plan: dict[str, Any]) -> None:
    plan["workplan_path"] = save_workplan(arguments, plan)


def _normalize_task(task: Mapping[str, Any]) -> dict[str, Any]:
    normalized = dict(task)
    if "blocked_by" not in normalized:
        normalized["blocked_by"] = []
    if "done" not in normalized:
        normalized["done"] = False
    normalized["human_gate"] = normalize_human_gate(normalized.get("human_gate"))
    status = normalize_task_status(normalized)
    normalized["status"] = status
    if status == RETIRED:
        normalized["retired"] = True
    normalized["lifecycle"] = _lifecycle(normalized)
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


def _task_status(task: Mapping[str, Any]) -> str:
    return normalize_task_status(task)


def _lifecycle(task: Mapping[str, Any]) -> dict[str, Any]:
    return normalize_lifecycle(task.get("lifecycle"))


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


def _plan_id(arguments: Mapping[str, Any]) -> str:
    value = arguments.get("plan_id")
    if isinstance(value, str) and value:
        return value
    return "workplan"
