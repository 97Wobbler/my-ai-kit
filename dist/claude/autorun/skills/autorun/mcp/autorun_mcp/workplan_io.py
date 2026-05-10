"""Import/export bridge between root workplan.yaml and Autorun MCP state."""

from __future__ import annotations

import json
from datetime import date
from datetime import datetime, timezone
from typing import Any, Mapping
from uuid import uuid4

from .schema import normalize_human_gate, validate_plan
from .state import load_plan, resolve_repo_root, resolve_state_root, save_plan

PENDING = "pending"
COMMITTED = "committed"
BLOCK_SCALAR_KEYS = {"spec", "as_is", "to_be", "notes"}
TASK_FIELD_ORDER = (
    "id",
    "name",
    "blocked_by",
    "human_gate",
    "done",
    "category",
    "estimated_size",
    "output",
    "spec",
    "verify_checks",
    "notes",
)


def import_workplan(arguments: Mapping[str, Any]) -> dict[str, Any]:
    repo_root = resolve_repo_root(arguments.get("repo_root"))
    workplan_path = repo_root / "workplan.yaml"
    if not workplan_path.exists():
        raise FileNotFoundError(f"workplan.yaml not found: {workplan_path}")

    yaml = _load_pyyaml()
    with workplan_path.open("r", encoding="utf-8") as handle:
        loaded = yaml.safe_load(handle)
    if loaded is None:
        loaded = {}
    if not isinstance(loaded, dict):
        raise ValueError("workplan.yaml must contain a mapping")

    meta = loaded.get("meta")
    tasks = loaded.get("tasks")
    if not isinstance(meta, dict):
        raise ValueError("workplan.yaml meta must be an object")
    if not isinstance(tasks, list) or not all(isinstance(task, dict) for task in tasks):
        raise ValueError("workplan.yaml tasks must be a list of objects")

    plan_id = arguments.get("plan_id")
    if plan_id is None:
        plan_id = f"workplan-{uuid4().hex[:12]}"
    if not isinstance(plan_id, str) or not plan_id:
        raise ValueError("plan_id must be a non-empty string")

    run_policy = arguments.get("run_policy", {})
    if not isinstance(run_policy, dict):
        raise ValueError("run_policy must be an object when provided")

    now = _now()
    normalized_meta = _json_safe(dict(meta))
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
        "meta": normalized_meta,
        "tasks": normalized_tasks,
    }

    state_root = resolve_state_root(arguments)
    state_path = save_plan(state_root, plan)
    validation = validate_plan(plan)
    return {
        "plan_id": plan_id,
        "path": str(state_path),
        "workplan_path": str(workplan_path),
        "validation": validation,
    }


def export_workplan(arguments: Mapping[str, Any]) -> dict[str, Any]:
    plan_id = arguments.get("plan_id")
    if not isinstance(plan_id, str) or not plan_id:
        raise ValueError("plan_id must be a non-empty string")

    force = arguments.get("force", False)
    if not isinstance(force, bool):
        raise ValueError("force must be a boolean when provided")

    repo_root = resolve_repo_root(arguments.get("repo_root"))
    workplan_path = repo_root / "workplan.yaml"
    plan = load_plan(resolve_state_root(arguments), plan_id)
    validation = validate_plan(plan)
    if validation.get("errors") and not force:
        raise ValueError("plan validation failed; pass force=true to export anyway")

    overwrote = workplan_path.exists()
    payload = emit_workplan_yaml(plan)
    workplan_path.write_text(payload, encoding="utf-8")
    return {
        "plan_id": plan_id,
        "workplan_path": str(workplan_path),
        "validation": validation,
        "forced": force,
        "overwrote": overwrote,
    }


def emit_workplan_yaml(plan: Mapping[str, Any]) -> str:
    workplan = {
        "meta": plan.get("meta") if isinstance(plan.get("meta"), dict) else {},
        "tasks": plan.get("tasks") if isinstance(plan.get("tasks"), list) else [],
    }
    return _emit_mapping(workplan, 0) + "\n"


def _load_pyyaml() -> Any:
    try:
        import yaml  # type: ignore[import-not-found]
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "PyYAML is required to import workplan.yaml; install PyYAML or continue using MCP core tools"
        ) from exc
    return yaml


def _normalize_task(task: Mapping[str, Any]) -> dict[str, Any]:
    normalized = _json_safe(dict(task))
    normalized.setdefault("blocked_by", [])
    normalized.setdefault("done", False)
    normalized["human_gate"] = normalize_human_gate(normalized.get("human_gate"))
    return normalized


def _json_safe(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_json_safe(item) for item in value]
    if isinstance(value, tuple):
        return [_json_safe(item) for item in value]
    if isinstance(value, datetime):
        return value.replace(microsecond=0).isoformat()
    if isinstance(value, date):
        return value.isoformat()
    if value is None or isinstance(value, str | int | float | bool):
        return value
    return str(value)


def _emit_mapping(mapping: Mapping[str, Any], indent: int) -> str:
    lines: list[str] = []
    for key, value in mapping.items():
        lines.extend(_emit_key_value(str(key), value, indent))
    return "\n".join(lines)


def _emit_key_value(key: str, value: Any, indent: int) -> list[str]:
    prefix = " " * indent + f"{key}:"
    if _is_block_scalar(key, value):
        return [f"{prefix} |", *_block_lines(str(value), indent + 2)]
    if isinstance(value, dict):
        if not value:
            return [f"{prefix} {{}}"]
        return [prefix, *_emit_mapping(value, indent + 2).splitlines()]
    if isinstance(value, list):
        if not value:
            return [f"{prefix} []"]
        if key == "tasks":
            return [prefix, *_emit_task_list(value, indent + 2)]
        return [prefix, *_emit_list(value, indent + 2)]
    return [f"{prefix} {_format_scalar(value)}"]


def _emit_task_list(items: list[Any], indent: int) -> list[str]:
    lines: list[str] = []
    for item in items:
        if not isinstance(item, dict):
            lines.append(" " * indent + f"- {_format_scalar(item)}")
            continue
        ordered = _ordered_task(item)
        first = True
        for key, value in ordered.items():
            child_lines = _emit_key_value(key, value, indent + 2)
            if first:
                child_lines[0] = " " * indent + "-" + child_lines[0][indent + 1 :]
                first = False
            lines.extend(child_lines)
    return lines


def _emit_list(items: list[Any], indent: int) -> list[str]:
    lines: list[str] = []
    for item in items:
        if isinstance(item, dict):
            lines.append(" " * indent + "-")
            lines.extend(_emit_mapping(item, indent + 2).splitlines())
        elif isinstance(item, list):
            lines.append(" " * indent + "-")
            lines.extend(_emit_list(item, indent + 2))
        else:
            lines.append(" " * indent + f"- {_format_scalar(item)}")
    return lines


def _ordered_task(task: Mapping[str, Any]) -> dict[str, Any]:
    ordered: dict[str, Any] = {}
    for key in TASK_FIELD_ORDER:
        if key in task:
            ordered[key] = task[key]
    for key, value in task.items():
        if key not in ordered:
            ordered[key] = value
    return ordered


def _is_block_scalar(key: str, value: Any) -> bool:
    return key in BLOCK_SCALAR_KEYS and isinstance(value, str) and "\n" in value


def _block_lines(value: str, indent: int) -> list[str]:
    prefix = " " * indent
    return [prefix + line if line else prefix for line in value.splitlines()]


def _format_scalar(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int | float) and not isinstance(value, bool):
        return str(value)
    return json.dumps(str(value), ensure_ascii=False)


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
