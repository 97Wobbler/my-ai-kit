"""Deterministic plan schema checks for Autorun MCP."""

from __future__ import annotations

from typing import Any, Mapping

VALID_HUMAN_GATES = {None, "approve", "execute"}
BROAD_KEYWORDS = ("전체", "모든", "리팩토링", "마이그레이션")
REQUIRED_TASK_FIELDS = (
    "id",
    "name",
    "blocked_by",
    "human_gate",
    "done",
    "spec",
)


def normalize_human_gate(value: Any) -> str | None:
    if value == "null":
        return None
    if value is None:
        return None
    if isinstance(value, str):
        return value
    return str(value)


def normalize_output(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value] if value else []
    if isinstance(value, list):
        return [item for item in value if isinstance(item, str) and item]
    return []


def validate_plan(plan: Mapping[str, Any]) -> dict[str, Any]:
    """Validate a stored plan and return stable, repeatable issues."""

    errors: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []

    meta = plan.get("meta")
    tasks = plan.get("tasks")
    if not isinstance(meta, dict):
        errors.append(_issue("missing_meta", None, "plan meta must be an object"))
    if not isinstance(tasks, list):
        errors.append(_issue("missing_tasks", None, "plan tasks must be a list"))
        return _result(errors, warnings)

    ids: list[str] = []
    valid_tasks: list[Mapping[str, Any]] = []
    seen: set[str] = set()
    duplicates: set[str] = set()
    task_by_id: dict[str, Mapping[str, Any]] = {}

    for index, task in enumerate(tasks):
        if not isinstance(task, dict):
            errors.append(_issue("invalid_task", None, "task must be an object", index=index))
            continue

        task_id = task.get("id")
        if not isinstance(task_id, str) or not task_id:
            errors.append(_issue("missing_task_id", None, "task id is required", index=index))
            continue

        ids.append(task_id)
        valid_tasks.append(task)
        if task_id in seen:
            duplicates.add(task_id)
        else:
            seen.add(task_id)
            task_by_id[task_id] = task

        for field in REQUIRED_TASK_FIELDS:
            if field not in task:
                errors.append(
                    _issue(
                        "missing_required_field",
                        task_id,
                        f"{task_id}: missing required field {field}",
                        field=field,
                    )
                )

        blocked_by = task.get("blocked_by", [])
        if not isinstance(blocked_by, list) or not all(isinstance(dep, str) for dep in blocked_by):
            errors.append(_issue("invalid_blocked_by", task_id, f"{task_id}: blocked_by must be a list of ids"))

        human_gate = normalize_human_gate(task.get("human_gate"))
        if human_gate not in VALID_HUMAN_GATES:
            errors.append(
                _issue(
                    "invalid_human_gate",
                    task_id,
                    f"{task_id}: invalid human_gate {human_gate!r}",
                    human_gate=human_gate,
                )
            )

        output = normalize_output(task.get("output"))
        if not output:
            errors.append(_issue("missing_output", task_id, f"{task_id}: missing output"))

    for task_id in sorted(duplicates):
        errors.append(_issue("duplicate_id", task_id, f"duplicate task id {task_id}"))

    unique_ids = set(task_by_id)
    for task in valid_tasks:
        task_id = str(task["id"])
        for blocker in sorted(set(task.get("blocked_by") or [])):
            if blocker not in unique_ids:
                errors.append(
                    _issue(
                        "missing_blocker",
                        task_id,
                        f"{task_id}: blocker {blocker} is missing",
                        blocker=blocker,
                    )
                )

    for cycle in _dependency_cycles(task_by_id):
        errors.append(
            _issue(
                "dependency_cycle",
                cycle[0] if cycle else None,
                "dependency cycle: " + " -> ".join(cycle),
                cycle=cycle,
            )
        )

    for task_id in ids:
        task = task_by_id.get(task_id)
        if task is None:
            continue
        warnings.extend(granularity_issues(task))

    return _result(errors, warnings)


def granularity_issues(task: Mapping[str, Any]) -> list[dict[str, Any]]:
    task_id = str(task.get("id", ""))
    spec = task.get("spec")
    spec_text = spec if isinstance(spec, str) else ""
    output = normalize_output(task.get("output"))
    issues: list[dict[str, Any]] = []

    if task.get("estimated_size") == "L":
        issues.append(_issue("oversized_task", task_id, f"{task_id}: estimated_size L should be split"))

    if len(output) > 6:
        issues.append(_issue("too_many_outputs", task_id, f"{task_id}: more than 6 output files", output_count=len(output)))

    broad = _has_broad_keyword(spec_text)
    if broad and len(output) > 3:
        issues.append(
            _issue(
                "broad_spec_many_outputs",
                task_id,
                f"{task_id}: broad spec with more than 3 outputs should be split",
                output_count=len(output),
            )
        )

    if not output or (_only_directory_outputs(output) and broad):
        issues.append(_issue("needs_metadata", task_id, f"{task_id}: output metadata is too broad"))

    return issues


def has_split_issue(validation: Mapping[str, Any]) -> bool:
    split_codes = {"oversized_task", "too_many_outputs", "broad_spec_many_outputs"}
    return any(issue.get("code") in split_codes for issue in validation.get("warnings", []))


def has_metadata_issue(validation: Mapping[str, Any]) -> bool:
    metadata_codes = {"missing_output", "needs_metadata", "missing_required_field"}
    return any(issue.get("code") in metadata_codes for issue in validation.get("errors", [])) or any(
        issue.get("code") in metadata_codes for issue in validation.get("warnings", [])
    )


def _dependency_cycles(task_by_id: Mapping[str, Mapping[str, Any]]) -> list[list[str]]:
    adjacency = {
        task_id: sorted(dep for dep in (task.get("blocked_by") or []) if dep in task_by_id)
        for task_id, task in sorted(task_by_id.items())
    }
    cycles: list[list[str]] = []
    seen_cycles: set[tuple[str, ...]] = set()
    visited: set[str] = set()
    visiting: list[str] = []

    def visit(task_id: str) -> None:
        if task_id in visiting:
            cycle = visiting[visiting.index(task_id) :] + [task_id]
            canonical = _canonical_cycle(cycle)
            if canonical not in seen_cycles:
                seen_cycles.add(canonical)
                cycles.append(list(canonical) + [canonical[0]])
            return
        if task_id in visited:
            return
        visiting.append(task_id)
        for dep in adjacency.get(task_id, []):
            visit(dep)
        visiting.pop()
        visited.add(task_id)

    for task_id in sorted(adjacency):
        visit(task_id)

    cycles.sort(key=lambda item: "->".join(item))
    return cycles


def _canonical_cycle(cycle: list[str]) -> tuple[str, ...]:
    body = cycle[:-1] if len(cycle) > 1 and cycle[0] == cycle[-1] else cycle
    rotations = [tuple(body[index:] + body[:index]) for index in range(len(body))]
    return min(rotations)


def _only_directory_outputs(outputs: list[str]) -> bool:
    if not outputs:
        return False
    return all(path.endswith("/") or "." not in path.rsplit("/", 1)[-1] for path in outputs)


def _has_broad_keyword(spec: str) -> bool:
    return any(keyword in spec for keyword in BROAD_KEYWORDS)


def _issue(code: str, task_id: str | None, message: str, **details: Any) -> dict[str, Any]:
    issue = {"code": code, "task_id": task_id, "message": message}
    issue.update(details)
    return issue


def _result(errors: list[dict[str, Any]], warnings: list[dict[str, Any]]) -> dict[str, Any]:
    return {"valid": not errors, "errors": errors, "warnings": warnings}
