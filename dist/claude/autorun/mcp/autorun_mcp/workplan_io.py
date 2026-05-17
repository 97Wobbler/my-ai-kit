"""YAML workplan backend for Autorun MCP."""

from __future__ import annotations

import json
from datetime import date
from datetime import datetime, timezone
from typing import Any, Mapping

from .schema import OPTIONAL_PLAN_SECTIONS, normalize_human_gate, validate_plan
from .state import atomic_write_text, resolve_workplan_path

PENDING = "pending"
STARTED = "started"
VERIFIED = "verified"
COMMITTED = "committed"
RETIRED = "retired"
VALID_STATUSES = {PENDING, STARTED, VERIFIED, COMMITTED, RETIRED}
BLOCK_SCALAR_KEYS = {"spec", "as_is", "to_be", "notes"}
LIFECYCLE_FIELD_ORDER = (
    "started_at",
    "verified_at",
    "committed_at",
    "worker_id",
    "commit",
)
TASK_FIELD_ORDER = (
    "id",
    "name",
    "blocked_by",
    "human_gate",
    "done",
    "status",
    "category",
    "estimated_size",
    "output",
    "invariant_refs",
    "surface_refs",
    "criteria_refs",
    "spec",
    "verify_checks",
    "lifecycle",
    "notes",
)


def load_workplan(arguments: Mapping[str, Any]) -> dict[str, Any]:
    path = resolve_workplan_path(arguments)
    if not path.exists():
        raise FileNotFoundError(f"workplan.yaml not found: {path}")

    loaded = parse_workplan_yaml(path.read_text(encoding="utf-8"))
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

    plan = {
        "plan_id": _plan_id(arguments, loaded),
        "workplan_path": str(path),
        "meta": _json_safe(dict(meta)),
        "tasks": [_normalize_task(task) for task in tasks],
    }
    for section in OPTIONAL_PLAN_SECTIONS:
        value = loaded.get(section, [])
        plan[section] = _json_safe(value) if isinstance(value, list) else value
    return plan


def save_workplan(arguments: Mapping[str, Any], plan: Mapping[str, Any]) -> str:
    path = resolve_workplan_path(arguments)
    normalized: dict[str, Any] = {"meta": plan.get("meta") if isinstance(plan.get("meta"), dict) else {}}
    for section in OPTIONAL_PLAN_SECTIONS:
        value = plan.get(section)
        if isinstance(value, list) and value:
            normalized[section] = _json_safe(value)
    normalized["tasks"] = (
        [_normalize_task(task) for task in plan.get("tasks", []) if isinstance(task, dict)]
        if isinstance(plan.get("tasks"), list)
        else []
    )
    payload = emit_workplan_yaml(normalized)
    atomic_write_text(path, payload)
    return str(path)


def import_workplan(arguments: Mapping[str, Any]) -> dict[str, Any]:
    plan = load_workplan(arguments)
    validation = validate_plan(plan)
    return {
        "plan_id": plan["plan_id"],
        "workplan_path": plan["workplan_path"],
        "validation": validation,
        "compatibility": "noop: workplan.yaml is already the Autorun MCP state backend",
    }


def export_workplan(arguments: Mapping[str, Any]) -> dict[str, Any]:
    force = arguments.get("force", False)
    if not isinstance(force, bool):
        raise ValueError("force must be a boolean when provided")

    plan = load_workplan(arguments)
    validation = validate_plan(plan)
    if validation.get("errors") and not force:
        raise ValueError("plan validation failed; pass force=true to acknowledge existing workplan issues")
    return {
        "plan_id": plan["plan_id"],
        "workplan_path": plan["workplan_path"],
        "validation": validation,
        "forced": force,
        "overwrote": False,
        "compatibility": "noop: workplan.yaml is already the Autorun MCP state backend",
    }


def emit_workplan_yaml(plan: Mapping[str, Any]) -> str:
    workplan = {
        "meta": plan.get("meta") if isinstance(plan.get("meta"), dict) else {},
    }
    for section in OPTIONAL_PLAN_SECTIONS:
        value = plan.get(section)
        if isinstance(value, list) and value:
            workplan[section] = value
    workplan["tasks"] = plan.get("tasks") if isinstance(plan.get("tasks"), list) else []
    return _emit_mapping(workplan, 0) + "\n"


def normalize_task_status(task: Mapping[str, Any]) -> str:
    status = task.get("status")
    if isinstance(status, str) and status:
        return status
    if task.get("retired"):
        return RETIRED
    return COMMITTED if task.get("done") else PENDING


def normalize_lifecycle(value: Any) -> dict[str, Any]:
    lifecycle = _json_safe(value) if isinstance(value, dict) else {}
    normalized = {key: lifecycle.get(key) for key in LIFECYCLE_FIELD_ORDER}
    for key, item in lifecycle.items():
        if key not in normalized:
            normalized[str(key)] = item
    return normalized


def _normalize_task(task: Mapping[str, Any]) -> dict[str, Any]:
    normalized = _json_safe(dict(task))
    normalized.setdefault("blocked_by", [])
    normalized.setdefault("done", False)
    normalized["human_gate"] = normalize_human_gate(normalized.get("human_gate"))
    status = normalize_task_status(normalized)
    normalized["status"] = status
    if status == RETIRED:
        normalized["retired"] = True
    normalized["lifecycle"] = normalize_lifecycle(normalized.get("lifecycle"))
    return normalized


def parse_workplan_yaml(payload: str) -> Any:
    lines = payload.splitlines()
    parser = _YamlSubsetParser(lines)
    return parser.parse()


class _YamlSubsetParser:
    """Parse the YAML subset emitted by Autorun plus common hand edits."""

    def __init__(self, lines: list[str]) -> None:
        self.lines = lines
        self.index = 0

    def parse(self) -> Any:
        self._skip_blank()
        if self.index >= len(self.lines):
            return {}
        return self._parse_block(self._indent(self.lines[self.index]))

    def _parse_block(self, indent: int) -> Any:
        self._skip_blank()
        if self.index >= len(self.lines):
            return {}
        current = self.lines[self.index]
        current_indent = self._indent(current)
        if current_indent < indent:
            return {}
        if current_indent != indent:
            raise ValueError(f"invalid YAML indentation at line {self.index + 1}")
        stripped = current.strip()
        if stripped.startswith("-"):
            return self._parse_list(indent)
        return self._parse_mapping(indent)

    def _parse_mapping(self, indent: int) -> dict[str, Any]:
        mapping: dict[str, Any] = {}
        while self.index < len(self.lines):
            self._skip_blank()
            if self.index >= len(self.lines):
                break
            line = self.lines[self.index]
            current_indent = self._indent(line)
            if current_indent < indent:
                break
            if current_indent != indent:
                raise ValueError(f"invalid YAML mapping indentation at line {self.index + 1}")
            stripped = line.strip()
            if stripped.startswith("-"):
                break
            key, value = self._split_key_value(stripped)
            self.index += 1
            mapping[key] = self._parse_value_after_key(value, indent)
        return mapping

    def _parse_list(self, indent: int) -> list[Any]:
        items: list[Any] = []
        while self.index < len(self.lines):
            self._skip_blank()
            if self.index >= len(self.lines):
                break
            line = self.lines[self.index]
            current_indent = self._indent(line)
            if current_indent < indent:
                break
            if current_indent != indent:
                raise ValueError(f"invalid YAML list indentation at line {self.index + 1}")
            stripped = line.strip()
            if not stripped.startswith("-"):
                break
            rest = stripped[1:].strip()
            self.index += 1
            if not rest:
                items.append(self._parse_nested_or_empty(indent))
            elif ":" in rest and not rest.startswith(("'", '"')):
                key, value = self._split_key_value(rest)
                item = {key: self._parse_value_after_key(value, indent)}
                while self.index < len(self.lines):
                    self._skip_blank()
                    if self.index >= len(self.lines):
                        break
                    next_indent = self._indent(self.lines[self.index])
                    if next_indent <= indent:
                        break
                    if next_indent != indent + 2:
                        raise ValueError(f"invalid YAML list item indentation at line {self.index + 1}")
                    key, value = self._split_key_value(self.lines[self.index].strip())
                    self.index += 1
                    item[key] = self._parse_value_after_key(value, indent + 2)
                items.append(item)
            else:
                items.append(self._parse_scalar(rest))
        return items

    def _parse_value_after_key(self, value: str, indent: int) -> Any:
        value = value.strip()
        if value == "|":
            return self._parse_block_scalar(indent + 2)
        if value == "":
            return self._parse_nested_or_empty(indent)
        return self._parse_scalar(value)

    def _parse_nested_or_empty(self, indent: int) -> Any:
        self._skip_blank()
        if self.index >= len(self.lines):
            return {}
        next_indent = self._indent(self.lines[self.index])
        if next_indent <= indent:
            return {}
        return self._parse_block(next_indent)

    def _parse_block_scalar(self, indent: int) -> str:
        values: list[str] = []
        while self.index < len(self.lines):
            line = self.lines[self.index]
            if not line.strip():
                values.append("")
                self.index += 1
                continue
            current_indent = self._indent(line)
            if current_indent < indent:
                break
            values.append(line[indent:] if len(line) >= indent else "")
            self.index += 1
        return "\n".join(values)

    def _split_key_value(self, stripped: str) -> tuple[str, str]:
        if ":" not in stripped:
            raise ValueError(f"invalid YAML mapping line at line {self.index + 1}")
        key, value = stripped.split(":", 1)
        key = key.strip()
        if not key:
            raise ValueError(f"empty YAML key at line {self.index + 1}")
        return key, value

    def _parse_scalar(self, value: str) -> Any:
        if value in {"null", "~"}:
            return None
        if value == "true":
            return True
        if value == "false":
            return False
        if value == "{}":
            return {}
        if value == "[]":
            return []
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            if not inner:
                return []
            return [self._parse_scalar(part.strip()) for part in inner.split(",")]
        if value.startswith('"') or value.startswith("'"):
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                return value[1:-1] if len(value) >= 2 and value[-1] == value[0] else value
        return value

    def _skip_blank(self) -> None:
        while self.index < len(self.lines):
            stripped = self.lines[self.index].strip()
            if stripped and not stripped.startswith("#"):
                return
            self.index += 1

    def _indent(self, line: str) -> int:
        return len(line) - len(line.lstrip(" "))


def _plan_id(arguments: Mapping[str, Any], loaded: Mapping[str, Any]) -> str:
    explicit = arguments.get("plan_id")
    if isinstance(explicit, str) and explicit:
        return explicit
    loaded_plan_id = loaded.get("plan_id")
    if isinstance(loaded_plan_id, str) and loaded_plan_id:
        return loaded_plan_id
    meta = loaded.get("meta")
    if isinstance(meta, dict) and isinstance(meta.get("plan_id"), str) and meta.get("plan_id"):
        return str(meta["plan_id"])
    return "workplan"


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
        return [prefix, *_emit_mapping(_ordered_mapping(key, value), indent + 2).splitlines()]
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


def _ordered_mapping(key: str, value: Mapping[str, Any]) -> dict[str, Any]:
    if key != "lifecycle":
        return dict(value)
    ordered: dict[str, Any] = {}
    for field in LIFECYCLE_FIELD_ORDER:
        if field in value:
            ordered[field] = value[field]
    for field, item in value.items():
        if field not in ordered:
            ordered[field] = item
    return ordered


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


def now_utc() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
