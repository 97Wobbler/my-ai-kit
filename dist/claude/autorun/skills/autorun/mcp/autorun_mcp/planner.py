"""Deterministic Autorun MCP plan operations."""

from __future__ import annotations

import copy
from pathlib import PurePosixPath
from typing import Any, Mapping

from .schema import (
    METADATA_WARNING_CODES,
    OPTIONAL_PLAN_SECTIONS,
    SPLIT_WARNING_CODES,
    VALID_ESTIMATED_SIZES,
    has_metadata_issue,
    has_split_issue,
    blocking_warnings,
    nonblocking_warnings,
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
    for section in OPTIONAL_PLAN_SECTIONS:
        value = arguments.get(section, [])
        if value is None:
            value = []
        if not isinstance(value, list) or not all(isinstance(item, dict) for item in value):
            raise ValueError(f"{section} must be a list of objects when provided")
        plan[section] = [dict(item) for item in value]
    if run_policy:
        plan["meta"].setdefault("run_policy", run_policy)

    path = save_workplan(arguments, plan)
    plan["workplan_path"] = path
    validation = validate_plan(plan)
    return _with_readiness({"plan": plan, "path": path, "workplan_path": path}, plan, validation)


def plan_validate(arguments: Mapping[str, Any]) -> dict[str, Any]:
    plan = _load(arguments)
    validation = validate_plan(plan)
    return _with_readiness({"plan_id": plan["plan_id"], "workplan_path": plan["workplan_path"]}, plan, validation)


def plan_refine(arguments: Mapping[str, Any]) -> dict[str, Any]:
    plan = _load(arguments)
    validation = validate_plan(plan)
    ready_human_gates = _ready_human_gates(plan)
    result = {
        "plan_id": plan["plan_id"],
        "workplan_path": plan["workplan_path"],
        "human_gates": ready_human_gates,
    }
    return _with_readiness(result, plan, validation, human_gates=ready_human_gates)


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


def refine_apply(arguments: Mapping[str, Any]) -> dict[str, Any]:
    proposal = arguments.get("proposal")
    if proposal is None:
        proposal = {key: value for key, value in arguments.items() if key not in {"repo_root", "workplan_path", "state_dir", "plan_id"}}
    if not isinstance(proposal, dict):
        raise ValueError("proposal must be an object")

    plan = _load(arguments)
    before_validation = validate_plan(plan)
    candidate = copy.deepcopy(plan)
    summary = _apply_repair(candidate, proposal)
    after_validation = validate_plan(candidate)
    if after_validation.get("errors"):
        codes = ", ".join(str(issue.get("code")) for issue in after_validation["errors"])
        raise ValueError(f"repair leaves schema invalid: {codes}")
    _save(arguments, candidate)
    return _with_readiness(
        {
            "plan_id": candidate["plan_id"],
            "workplan_path": candidate["workplan_path"],
            "applied": True,
            "repair": summary,
            "previous_validation": before_validation,
        },
        candidate,
        after_validation,
    )


def refine_until_ready(arguments: Mapping[str, Any]) -> dict[str, Any]:
    max_iterations = arguments.get("max_iterations", 3)
    if isinstance(max_iterations, bool) or not isinstance(max_iterations, int) or max_iterations <= 0:
        raise ValueError("max_iterations must be a positive integer when provided")

    plan = _load(arguments)
    applied: list[dict[str, Any]] = []
    for _index in range(max_iterations):
        validation = validate_plan(plan)
        readiness = _with_readiness({}, plan, validation)
        if readiness["ready_to_run"]:
            readiness.update({"plan_id": plan["plan_id"], "workplan_path": plan["workplan_path"], "applied_repairs": applied})
            return readiness
        deterministic = [proposal for proposal in readiness["repair_proposals"] if proposal.get("requires_input") is False]
        if not deterministic:
            readiness.update(
                {
                    "plan_id": plan["plan_id"],
                    "workplan_path": plan["workplan_path"],
                    "applied_repairs": applied,
                    "stopped_reason": "needs_input",
                }
            )
            return readiness
        candidate = copy.deepcopy(plan)
        summary = _apply_repair(candidate, deterministic[0])
        candidate_validation = validate_plan(candidate)
        if candidate_validation.get("errors"):
            readiness.update(
                {
                    "plan_id": plan["plan_id"],
                    "workplan_path": plan["workplan_path"],
                    "applied_repairs": applied,
                    "stopped_reason": "repair_rejected",
                    "rejected_repair": summary,
                    "rejected_validation": candidate_validation,
                }
            )
            return readiness
        _save(arguments, candidate)
        plan = candidate
        applied.append(summary)

    validation = validate_plan(plan)
    readiness = _with_readiness({}, plan, validation)
    readiness.update(
        {
            "plan_id": plan["plan_id"],
            "workplan_path": plan["workplan_path"],
            "applied_repairs": applied,
            "stopped_reason": "max_iterations",
        }
    )
    return readiness


def next_batch(arguments: Mapping[str, Any]) -> dict[str, Any]:
    plan = _load_checked(arguments)
    _raise_if_run_blocked(plan)
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
        "progress_summary": _progress_projection(plan),
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
    projection = _progress_projection(plan)
    return {
        "plan_id": plan["plan_id"],
        "workplan_path": plan["workplan_path"],
        "progress": projection["progress"],
        "runnable": projection["runnable"],
        "blocked": projection["blocked"],
        "human_gates": projection["human_gates"],
        "active": projection["active"],
        "task_graph_budget": projection["task_graph_budget"],
    }


def progress_summary(arguments: Mapping[str, Any]) -> dict[str, Any]:
    plan = _load(arguments)
    projection = _progress_projection(plan)
    return {"plan_id": plan["plan_id"], "workplan_path": plan["workplan_path"], **projection}


def _progress_projection(plan: Mapping[str, Any]) -> dict[str, Any]:
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
    display_plan = _display_plan(tasks)
    phases = _phase_summary(display_plan)
    return {
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
        "display_plan": display_plan,
        "phases": phases,
        "task_graph_budget": _task_graph_budget(tasks, runnable, human_gates, phases),
    }


def _display_plan(tasks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    phase_by_task = _phase_by_task(tasks)
    return [
        {
            "id": task["id"],
            "name": task.get("name"),
            "status": _task_status(task),
            "done": bool(task.get("done")),
            "human_gate": normalize_human_gate(task.get("human_gate")),
            "blocked_by": list(task.get("blocked_by") or []),
            "phase": phase_by_task.get(task["id"], 0),
        }
        for task in tasks
    ]


def _phase_by_task(tasks: list[dict[str, Any]]) -> dict[str, int]:
    task_ids = {task["id"] for task in tasks}
    blockers = {
        task["id"]: [dep for dep in task.get("blocked_by") or [] if dep in task_ids]
        for task in tasks
    }
    phases: dict[str, int] = {}

    def phase(task_id: str, stack: set[str] | None = None) -> int:
        if task_id in phases:
            return phases[task_id]
        stack = set(stack or set())
        if task_id in stack:
            return 0
        stack.add(task_id)
        deps = blockers.get(task_id, [])
        phases[task_id] = 0 if not deps else max(phase(dep, stack) for dep in deps) + 1
        return phases[task_id]

    for task in tasks:
        phase(task["id"])
    return phases


def _phase_summary(display_plan: list[dict[str, Any]]) -> list[dict[str, Any]]:
    phases: dict[int, dict[str, Any]] = {}
    for item in display_plan:
        phase = int(item.get("phase", 0))
        summary = phases.setdefault(phase, {"phase": phase, "total": 0, "done": 0, "task_ids": []})
        summary["total"] += 1
        if item.get("done"):
            summary["done"] += 1
        summary["task_ids"].append(item["id"])
    return [phases[index] for index in sorted(phases)]


def _task_graph_budget(
    tasks: list[dict[str, Any]],
    runnable: list[str],
    human_gates: list[str],
    phases: list[dict[str, Any]],
) -> dict[str, Any]:
    unfinished = [task for task in tasks if not task.get("done")]
    active_count = len(unfinished)
    return {
        "active_task_count": active_count,
        "phase_count": len([phase for phase in phases if phase.get("done") != phase.get("total")]),
        "first_runnable_batch_size": len(runnable),
        "human_gate_count": len(human_gates),
        "high_conflict_outputs": _high_conflict_outputs(unfinished),
        "budget_band": _budget_band(active_count),
    }


def _budget_band(active_count: int) -> str:
    if active_count <= 2:
        return "tiny"
    if active_count <= 8:
        return "small"
    if active_count <= 18:
        return "medium"
    if active_count <= 30:
        return "large"
    return "over_budget"


def _high_conflict_outputs(tasks: list[dict[str, Any]]) -> list[dict[str, str]]:
    conflicts: list[dict[str, str]] = []
    outputs: list[tuple[str, str]] = []
    for task in tasks:
        task_id = task["id"]
        for output in normalize_output(task.get("output")):
            outputs.append((task_id, output))

    for index, (left_task, left_output) in enumerate(outputs):
        for right_task, right_output in outputs[index + 1 :]:
            if left_task == right_task:
                continue
            if _paths_overlap(left_output, right_output):
                conflicts.append(
                    {
                        "left_task": left_task,
                        "left_output": left_output,
                        "right_task": right_task,
                        "right_output": right_output,
                    }
                )
            if len(conflicts) >= 10:
                return conflicts
    return conflicts


def _readiness_blocking_warnings(
    plan: Mapping[str, Any],
    validation: Mapping[str, Any],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    active_unfinished_ids = {task["id"] for task in _active_tasks(plan) if not task.get("done")}
    active_blocking: list[dict[str, Any]] = []
    ignored_blocking: list[dict[str, Any]] = []

    for issue in blocking_warnings(validation):
        task_id = issue.get("task_id")
        if isinstance(task_id, str):
            if task_id in active_unfinished_ids:
                active_blocking.append(issue)
            else:
                ignored_blocking.append(issue)
            continue
        active_blocking.append(issue)
    return active_blocking, ignored_blocking


def _has_blocking_code(issues: list[dict[str, Any]], codes: set[str]) -> bool:
    return any(issue.get("code") in codes for issue in issues)


def _with_readiness(
    result: dict[str, Any],
    plan: Mapping[str, Any],
    validation: Mapping[str, Any],
    *,
    human_gates: list[str] | None = None,
) -> dict[str, Any]:
    human_gates = human_gates if human_gates is not None else _ready_human_gates(plan)
    blocking, ignored_blocking = _readiness_blocking_warnings(plan, validation)
    nonblocking = nonblocking_warnings(validation)
    schema_valid = not validation.get("errors")
    next_action = _next_action(validation, human_gates, blocking)
    ready_to_run = schema_valid and not blocking and not human_gates
    repair_proposals = _repair_proposals(plan, validation, blocking, nonblocking)
    task_graph_budget = _progress_projection(plan)["task_graph_budget"]
    enriched_validation = dict(validation)
    enriched_validation.update(
        {
            "schema_valid": schema_valid,
            "ready_to_run": ready_to_run,
            "blocking": not ready_to_run,
            "next_action": next_action,
            "legacy_next_action": _legacy_next_action(next_action),
            "blocking_warnings": blocking,
            "nonblocking_warnings": nonblocking,
            "ignored_blocking_warnings": ignored_blocking,
            "repair_proposals": repair_proposals,
            "task_graph_budget": task_graph_budget,
        }
    )
    result.update(
        {
            "validation": enriched_validation,
            "schema_valid": schema_valid,
            "ready_to_run": ready_to_run,
            "blocking": not ready_to_run,
            "next_action": next_action,
            "legacy_next_action": _legacy_next_action(next_action),
            "blocking_warnings": blocking,
            "nonblocking_warnings": nonblocking,
            "ignored_blocking_warnings": ignored_blocking,
            "repair_proposals": repair_proposals,
            "task_graph_budget": task_graph_budget,
        }
    )
    return result


def _next_action(validation: Mapping[str, Any], human_gates: list[str], blocking: list[dict[str, Any]]) -> str:
    if validation.get("errors"):
        return "add_metadata" if has_metadata_issue(validation) else "fix_schema"
    if _has_blocking_code(blocking, SPLIT_WARNING_CODES):
        return "split_tasks"
    if _has_blocking_code(blocking, METADATA_WARNING_CODES):
        return "add_metadata"
    if any(issue.get("code") == "blocking_not_assessed" for issue in blocking):
        return "assess_surfaces"
    if human_gates:
        return "resolve_human_gate"
    return "ready"


def _legacy_next_action(next_action: str) -> str:
    return {
        "add_metadata": "needs_metadata",
        "assess_surfaces": "needs_assessment",
        "fix_schema": "needs_metadata",
        "resolve_human_gate": "blocked_by_human_gate",
        "split_tasks": "needs_split",
    }.get(next_action, next_action)


def _repair_proposals(
    plan: Mapping[str, Any],
    validation: Mapping[str, Any],
    blocking: list[dict[str, Any]],
    nonblocking: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    proposals: list[dict[str, Any]] = []
    proposal_index = 1
    for issue in [*validation.get("errors", []), *blocking, *nonblocking]:
        proposal = _proposal_for_issue(plan, issue)
        if proposal is None:
            continue
        proposal["id"] = f"RP{proposal_index:02d}"
        proposal_index += 1
        proposals.append(proposal)
    return proposals


def _proposal_for_issue(plan: Mapping[str, Any], issue: Mapping[str, Any]) -> dict[str, Any] | None:
    code = issue.get("code")
    task_id = issue.get("task_id")
    if code in {"oversized_task", "medium_task_needs_split", "broad_spec_many_outputs", "too_many_outputs", "too_many_requirements", "too_many_surfaces", "broad_output_scope", "helper_rollout_combined", "contract_many_surfaces", "compound_scope"} and isinstance(task_id, str):
        return {
            "op": "split_task",
            "task_id": task_id,
            "reason": issue.get("message"),
            "requires_input": True,
            "replacement_tasks": [],
        }
    if code in {"needs_granularity_metadata", "missing_required_field"} and isinstance(task_id, str):
        field = issue.get("field") if isinstance(issue.get("field"), str) else "estimated_size"
        return {
            "op": "set_task_fields",
            "task_id": task_id,
            "reason": issue.get("message"),
            "requires_input": True,
            "fields": {field: None},
        }
    if code in {"missing_output", "needs_metadata"} and isinstance(task_id, str):
        return {
            "op": "set_task_fields",
            "task_id": task_id,
            "reason": issue.get("message"),
            "requires_input": True,
            "fields": {"output": []},
        }
    if code == "missing_verify_checks" and isinstance(task_id, str):
        return {
            "op": "add_verify_check",
            "task_id": task_id,
            "reason": issue.get("message"),
            "requires_input": True,
            "check": "",
        }
    if code == "blocking_not_assessed":
        return {
            "op": "update_not_assessed",
            "not_assessed_id": issue.get("not_assessed_id"),
            "reason": issue.get("message"),
            "requires_input": True,
            "updates": {"blocks_ready": False},
        }
    if code in {"missing_invariant_ref", "missing_surface_ref", "missing_criteria_ref", "missing_task_ref", "invalid_reference_list"}:
        proposal: dict[str, Any] = {
            "op": "update_references",
            "reason": issue.get("message"),
            "requires_input": True,
            "field": issue.get("field"),
            "ref": issue.get("ref"),
        }
        if isinstance(task_id, str):
            proposal["task_id"] = task_id
        if issue.get("section"):
            proposal["section"] = issue.get("section")
            proposal["item_id"] = issue.get("item_id")
        return proposal
    return None


def _apply_repair(plan: dict[str, Any], proposal: Mapping[str, Any]) -> dict[str, Any]:
    op = proposal.get("op")
    if not isinstance(op, str) or not op:
        raise ValueError("repair proposal op must be a non-empty string")
    if op == "set_task_fields":
        task_id = _proposal_task_id(proposal)
        fields = proposal.get("fields")
        if not isinstance(fields, dict) or not fields:
            raise ValueError("set_task_fields requires non-empty fields")
        task = _task_by_id(plan, task_id)
        allowed = {
            "blocked_by",
            "category",
            "criteria_refs",
            "estimated_size",
            "human_gate",
            "invariant_refs",
            "name",
            "output",
            "spec",
            "surface_refs",
            "verify_checks",
        }
        for field, value in fields.items():
            if field not in allowed:
                raise ValueError(f"set_task_fields cannot update {field}")
            if value in (None, ""):
                raise ValueError(f"set_task_fields requires an explicit value for {field}")
            task[field] = value
        normalized = _normalize_task(task)
        task.clear()
        task.update(normalized)
        return {"op": op, "task_id": task_id, "fields": sorted(fields)}

    if op == "add_verify_check":
        task_id = _proposal_task_id(proposal)
        check = proposal.get("check")
        if not isinstance(check, str) or not check.strip():
            raise ValueError("add_verify_check requires a non-empty check")
        task = _task_by_id(plan, task_id)
        checks = normalize_output(task.get("verify_checks"))
        checks.append(check.strip())
        task["verify_checks"] = checks
        return {"op": op, "task_id": task_id, "check": check.strip()}

    if op == "split_task":
        task_id = _proposal_task_id(proposal)
        replacements = proposal.get("replacement_tasks")
        if not isinstance(replacements, list) or not replacements or not all(isinstance(task, dict) for task in replacements):
            raise ValueError("split_task requires non-empty replacement_tasks")
        original = _task_by_id(plan, task_id)
        if _task_status(original) == COMMITTED and not original.get("retired"):
            raise ValueError(f"cannot split completed task {task_id}")
        existing_ids = {task.get("id") for task in plan.get("tasks", []) if isinstance(task, dict)}
        normalized_replacements = []
        for replacement_input in replacements:
            replacement = _normalize_task(_inherit_repair_refs(original, replacement_input))
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
        plan["tasks"].extend(normalized_replacements)
        return {"op": op, "retired": task_id, "added": [task["id"] for task in normalized_replacements]}

    if op in {"add_invariant", "add_surface", "add_criteria", "add_not_assessed"}:
        section = {
            "add_invariant": "invariants",
            "add_surface": "surfaces",
            "add_criteria": "criteria_map",
            "add_not_assessed": "not_assessed",
        }[op]
        item = proposal.get("item")
        if not isinstance(item, dict):
            raise ValueError(f"{op} requires item object")
        item_id = item.get("id")
        if not isinstance(item_id, str) or not item_id:
            raise ValueError(f"{op} item requires id")
        items = plan.setdefault(section, [])
        if not isinstance(items, list):
            raise ValueError(f"{section} is not a list")
        if any(isinstance(existing, dict) and existing.get("id") == item_id for existing in items):
            raise ValueError(f"{section} id already exists: {item_id}")
        items.append(dict(item))
        return {"op": op, "section": section, "id": item_id}

    if op == "update_not_assessed":
        item_id = proposal.get("not_assessed_id")
        updates = proposal.get("updates")
        if not isinstance(item_id, str) or not item_id:
            raise ValueError("update_not_assessed requires not_assessed_id")
        if not isinstance(updates, dict) or not updates:
            raise ValueError("update_not_assessed requires updates")
        item = _section_item_by_id(plan, "not_assessed", item_id)
        item.update(updates)
        return {"op": op, "not_assessed_id": item_id, "fields": sorted(updates)}

    if op == "update_references":
        refs = proposal.get("refs")
        field = proposal.get("field")
        if not isinstance(field, str) or not field:
            raise ValueError("update_references requires field")
        if not isinstance(refs, list) or not all(isinstance(ref, str) for ref in refs):
            raise ValueError("update_references requires refs list")
        task_id = proposal.get("task_id")
        if isinstance(task_id, str) and task_id:
            _task_by_id(plan, task_id)[field] = refs
            return {"op": op, "task_id": task_id, "field": field, "refs": refs}
        section = proposal.get("section")
        item_id = proposal.get("item_id")
        if not isinstance(section, str) or not isinstance(item_id, str):
            raise ValueError("update_references requires task_id or section/item_id")
        _section_item_by_id(plan, section, item_id)[field] = refs
        return {"op": op, "section": section, "item_id": item_id, "field": field, "refs": refs}

    raise ValueError(f"unsupported repair op: {op}")


def _proposal_task_id(proposal: Mapping[str, Any]) -> str:
    task_id = proposal.get("task_id")
    if not isinstance(task_id, str) or not task_id:
        raise ValueError("repair proposal requires task_id")
    return task_id


def _inherit_repair_refs(original: Mapping[str, Any], replacement: Mapping[str, Any]) -> dict[str, Any]:
    inherited = dict(replacement)
    for field in ("invariant_refs", "surface_refs", "criteria_refs"):
        if field not in inherited and field in original:
            inherited[field] = original[field]
    return inherited


def _section_item_by_id(plan: Mapping[str, Any], section: str, item_id: str) -> dict[str, Any]:
    value = plan.get(section)
    if not isinstance(value, list):
        raise ValueError(f"{section} is not a list")
    for item in value:
        if isinstance(item, dict) and item.get("id") == item_id:
            return item
    raise ValueError(f"{section} item not found: {item_id}")


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
    if expected == PENDING:
        _raise_if_run_blocked(plan)
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


def _raise_if_run_blocked(plan: Mapping[str, Any]) -> None:
    validation = validate_plan(plan)
    active_ids = {task["id"] for task in _active_tasks(plan) if not task.get("done")}
    blocking_issues = [
        issue
        for issue in validation.get("warnings", [])
        if issue.get("code") == "blocking_not_assessed"
        or (
            issue.get("task_id") in active_ids
            and (has_metadata_issue({"errors": [], "warnings": [issue]}) or has_split_issue({"warnings": [issue]}))
        )
    ]
    if blocking_issues:
        codes = ", ".join(str(issue.get("code")) for issue in blocking_issues)
        raise ValueError(f"plan refinement required before RUN: {codes}")


def _save(arguments: Mapping[str, Any], plan: dict[str, Any]) -> None:
    plan["workplan_path"] = save_workplan(arguments, plan)


def _normalize_task(task: Mapping[str, Any]) -> dict[str, Any]:
    normalized = dict(task)
    if "name" not in normalized and "title" in normalized:
        normalized["name"] = normalized["title"]
    if "spec" not in normalized and "summary" in normalized:
        normalized["spec"] = normalized["summary"]
    if "output" not in normalized and "outputs" in normalized:
        normalized["output"] = normalized["outputs"]
    if "verify_checks" not in normalized and "verification" in normalized:
        normalized["verify_checks"] = normalized["verification"]
    if "blocked_by" not in normalized:
        normalized["blocked_by"] = []
    if "done" not in normalized:
        normalized["done"] = False
    if "estimated_size" in normalized:
        normalized["estimated_size"] = _normalize_estimated_size(normalized.get("estimated_size"))
    normalized["human_gate"] = normalize_human_gate(normalized.get("human_gate"))
    status = normalize_task_status(normalized)
    normalized["status"] = status
    if status == RETIRED:
        normalized["retired"] = True
    normalized["lifecycle"] = _lifecycle(normalized)
    return normalized


def _normalize_estimated_size(value: Any) -> str:
    if not isinstance(value, str):
        raise ValueError("estimated_size must be S, M, or L when provided")
    mapping = {
        "s": "S",
        "small": "S",
        "m": "M",
        "medium": "M",
        "l": "L",
        "large": "L",
    }
    normalized = mapping.get(value.strip().lower(), value)
    if normalized not in VALID_ESTIMATED_SIZES:
        raise ValueError("estimated_size must be S, M, or L when provided")
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
