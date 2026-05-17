"""Proposal-only planning workers for Autorun MCP."""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path
from typing import Any, Mapping

from . import workers
from .schema import OPTIONAL_PLAN_SECTIONS, validate_plan
from .state import resolve_repo_root
from .workplan_io import load_workplan

DECOMPOSE_TASK_ID = "decompose"
REVIEW_TASK_ID = "review"
SPLIT_TASK_PREFIX = "split"


def plan_decompose(arguments: Mapping[str, Any]) -> dict[str, Any]:
    request = _required_str(arguments, "request")
    proposal_id = _proposal_id(arguments, "proposal_id", "proposal")
    worker_id = _worker_id(arguments, f"decompose-{proposal_id}")
    prompt = _decompose_prompt(request)
    return _start_proposal_worker(arguments, proposal_id, DECOMPOSE_TASK_ID, worker_id, prompt, "decompose")


def plan_decompose_collect(arguments: Mapping[str, Any]) -> dict[str, Any]:
    worker_id = _worker_id_from_arguments(arguments)
    state_root = workers.resolve_artifact_root(arguments)
    collected = workers.worker_collect({**arguments, "worker_id": worker_id})
    state = collected.get("state", {})
    proposal_type = state.get("proposal_type", "decompose") if isinstance(state, dict) else "decompose"
    repo_check = _repo_modification_check(state if isinstance(state, dict) else {})
    parsed = _parse_result_json(collected["artifact_paths"]["result_path"])
    result = {
        "worker_id": worker_id,
        "proposal_id": state.get("proposal_id") if isinstance(state, dict) else None,
        "proposal_type": proposal_type,
        "status": collected["status"],
        "artifact_paths": collected["artifact_paths"],
        "repo_modification_check": repo_check,
        "parse": parsed["parse"],
    }
    if parsed["parse"]["ok"]:
        proposal = parsed["proposal"]
        result["proposal"] = proposal
        result["proposal_validation"] = _validate_proposal(arguments, proposal_type, proposal)
    else:
        result["proposal"] = None
        result["proposal_validation"] = {"schema_valid": False, "errors": [{"code": "proposal_parse_failed"}], "warnings": []}
    result["classification"] = _proposal_collection_classification(
        collected["status"],
        repo_check,
        parsed["parse"],
        result["proposal_validation"],
    )
    result["accepted"] = result["classification"] == "completed_valid"
    result["state_root"] = str(state_root)
    return result


def task_split_with_worker(arguments: Mapping[str, Any]) -> dict[str, Any]:
    task_id = _required_str(arguments, "task_id")
    plan = load_workplan(arguments)
    task = _task_by_id(plan, task_id)
    proposal_id = _proposal_id(arguments, "proposal_id", f"split-{_file_safe(task_id)}", use_plan_id=False)
    worker_id = _worker_id(arguments, f"split-{proposal_id}")
    validation = validate_plan(plan)
    task_warnings = [issue for issue in validation.get("warnings", []) if issue.get("task_id") == task_id]
    prompt = _split_prompt(task, task_warnings)
    result = _start_proposal_worker(arguments, proposal_id, f"{SPLIT_TASK_PREFIX}-{_file_safe(task_id)}", worker_id, prompt, "split")
    result["task_id"] = task_id
    return result


def decomposition_review(arguments: Mapping[str, Any]) -> dict[str, Any]:
    proposal = arguments.get("proposal")
    if proposal is None:
        proposal = load_workplan(arguments)
    if not isinstance(proposal, dict):
        raise ValueError("proposal must be an object when provided")
    proposal_id = _proposal_id(arguments, "review_id", "review")
    worker_id = _worker_id(arguments, f"review-{proposal_id}")
    prompt = _review_prompt(proposal)
    return _start_proposal_worker(arguments, proposal_id, REVIEW_TASK_ID, worker_id, prompt, "review")


def _start_proposal_worker(
    arguments: Mapping[str, Any],
    proposal_id: str,
    task_id: str,
    worker_id: str,
    prompt: str,
    proposal_type: str,
) -> dict[str, Any]:
    repo_root = resolve_repo_root(arguments.get("repo_root"), required=True)
    state_root = workers.resolve_artifact_root(arguments, repo_root)
    paths = workers.worker_artifact_paths(state_root, worker_id)
    prompt = _render_prompt(prompt, paths)
    command = _prepared_command(arguments, paths, repo_root)
    start_args = dict(arguments)
    start_args.update(
        {
            "repo_root": str(repo_root),
            "plan_id": proposal_id,
            "task_id": task_id,
            "worker_id": worker_id,
            "prompt": prompt,
            "runtime": arguments.get("runtime", workers.DEFAULT_RUNTIME),
        }
    )
    if command is not None:
        start_args.pop("command_override", None)
        start_args["command"] = command

    status_before = _git_status(repo_root)
    result = workers.worker_start(start_args)
    state = workers.load_worker_state(state_root, worker_id)
    state.update(
        {
            "proposal_id": proposal_id,
            "proposal_type": proposal_type,
            "repo_status_before": status_before,
        }
    )
    workers.save_worker_state(state_root, state)
    result["proposal_id"] = proposal_id
    result["proposal_type"] = proposal_type
    result["artifact_paths"] = _string_paths(paths)
    return result


def _prepared_command(
    arguments: Mapping[str, Any],
    paths: Mapping[str, Path],
    repo_root: Path,
) -> list[str] | None:
    value = arguments.get("command") if arguments.get("command") is not None else arguments.get("command_override")
    if value is None:
        return None
    if not isinstance(value, list) or not value or not all(isinstance(item, str) and item for item in value):
        raise ValueError("command override must be a non-empty list[str]")
    replacements = {
        "{repo_root}": str(repo_root),
        "{result_path}": str(paths["result_path"]),
        "{final_path}": str(paths["final_path"]),
        "{prompt_path}": str(paths["prompt_path"]),
    }
    command = []
    for item in value:
        for key, replacement in replacements.items():
            item = item.replace(key, replacement)
        command.append(item)
    return command


def _render_prompt(prompt: str, paths: Mapping[str, Path]) -> str:
    replacements = {
        "{result_path}": str(paths["result_path"]),
        "{final_path}": str(paths["final_path"]),
        "{prompt_path}": str(paths["prompt_path"]),
    }
    rendered = prompt
    for key, value in replacements.items():
        rendered = rendered.replace(key, value)
    return "\n".join(
        [
            rendered,
            "",
            "Artifact output requirement:",
            f"- Write the JSON proposal to this exact absolute path: {paths['result_path']}",
            "- Do not create result.json or any other proposal artifact inside the repository.",
        ]
    )


def _validate_proposal(arguments: Mapping[str, Any], proposal_type: str, proposal: Any) -> dict[str, Any]:
    if not isinstance(proposal, dict):
        return {"schema_valid": False, "errors": [{"code": "proposal_not_object"}], "warnings": []}
    if proposal_type == "review":
        return {"schema_valid": True, "errors": [], "warnings": []}
    if proposal_type == "split":
        replacements = proposal.get("replacement_tasks")
        if not isinstance(replacements, list):
            return {"schema_valid": False, "errors": [{"code": "missing_replacement_tasks"}], "warnings": []}
        try:
            plan = load_workplan(arguments)
            task_id = proposal.get("task_id")
            candidate = _split_validation_candidate(plan, task_id, replacements)
        except Exception:
            candidate = {"meta": {"goal": "split proposal"}, "tasks": replacements}
        return validate_plan(candidate)

    candidate = {
        "meta": proposal.get("meta") if isinstance(proposal.get("meta"), dict) else {},
        "tasks": proposal.get("tasks") if isinstance(proposal.get("tasks"), list) else [],
    }
    for section in OPTIONAL_PLAN_SECTIONS:
        value = proposal.get(section, [])
        if isinstance(value, list):
            candidate[section] = value
    return validate_plan(candidate)


def _parse_result_json(path_value: str) -> dict[str, Any]:
    path = Path(path_value)
    if not path.exists():
        return {"parse": {"ok": False, "code": "missing_result", "error": "result.json missing", "path": str(path)}, "proposal": None}
    try:
        payload = path.read_text(encoding="utf-8")
        parsed = json.loads(payload)
    except json.JSONDecodeError as exc:
        return {
            "parse": {
                "ok": False,
                "code": "parse_error",
                "error": "invalid JSON",
                "message": exc.msg,
                "line": exc.lineno,
                "column": exc.colno,
                "path": str(path),
            },
            "proposal": None,
        }
    return {"parse": {"ok": True, "path": str(path)}, "proposal": parsed}


def _proposal_collection_classification(
    status: Any,
    repo_check: Mapping[str, Any],
    parse: Mapping[str, Any],
    proposal_validation: Mapping[str, Any],
) -> str:
    if status == workers.TIMED_OUT_CANCELLED:
        return "timed_out_cancelled"
    if repo_check.get("ok") is False:
        return "repo_modified"
    if parse.get("ok") is not True:
        if parse.get("code") == "missing_result":
            return "missing_result"
        return "parse_error"
    if proposal_validation.get("schema_valid") is not True:
        return "schema_error"
    if status == workers.SUCCEEDED:
        return "completed_valid"
    return "completed_invalid"


def _repo_modification_check(state: Mapping[str, Any]) -> dict[str, Any]:
    repo_root = state.get("repo_root")
    before = state.get("repo_status_before")
    if not isinstance(repo_root, str) or before is None:
        return {"available": False, "ok": True, "reason": "not recorded"}
    after = _git_status(Path(repo_root))
    if before.get("available") is not True or after.get("available") is not True:
        return {"available": False, "ok": True, "before": before, "after": after}
    ok = before.get("status") == after.get("status")
    return {"available": True, "ok": ok, "before": before, "after": after}


def _git_status(repo_root: Path) -> dict[str, Any]:
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=str(repo_root),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=5,
        )
    except Exception as exc:
        return {"available": False, "error": str(exc)}
    if result.returncode != 0:
        return {"available": False, "returncode": result.returncode, "stderr": result.stderr.strip()}
    return {"available": True, "status": result.stdout.splitlines()}


def _decompose_prompt(request: str) -> str:
    return "\n".join(
        [
            "Analyze the repository read-only and produce a JSON decomposition proposal.",
            "Do not edit files, commit, or mutate workplan.yaml.",
            "Write only JSON to {result_path} with keys: meta, tasks, invariants, surfaces, criteria_map, not_assessed, assumptions.",
            "Each task must be commit-sized and include id, name, blocked_by, human_gate, done, status, estimated_size, output, spec, and verify_checks.",
            "",
            "Request:",
            request,
        ]
    )


def _split_prompt(task: Mapping[str, Any], warnings: list[Mapping[str, Any]]) -> str:
    return "\n".join(
        [
            "Analyze this oversized Autorun task read-only and produce a JSON split proposal.",
            "Do not edit files, commit, or mutate workplan.yaml.",
            "Write only JSON to {result_path} with keys: task_id, replacement_tasks, assumptions, not_assessed.",
            "",
            "Task JSON:",
            json.dumps(task, ensure_ascii=False, indent=2, sort_keys=True),
            "",
            "Validation warnings:",
            json.dumps(warnings, ensure_ascii=False, indent=2, sort_keys=True),
        ]
    )


def _review_prompt(proposal: Mapping[str, Any]) -> str:
    return "\n".join(
        [
            "Review this Autorun decomposition proposal read-only.",
            "Do not edit files, commit, or mutate workplan.yaml.",
            "Write only JSON to {result_path} with keys: findings, missed_surfaces, hidden_dependencies, oversized_tasks, weak_outputs, verification_gaps, not_assessed.",
            "",
            "Proposal JSON:",
            json.dumps(proposal, ensure_ascii=False, indent=2, sort_keys=True),
        ]
    )


def _task_by_id(plan: Mapping[str, Any], task_id: str) -> Mapping[str, Any]:
    for task in plan.get("tasks", []):
        if isinstance(task, dict) and task.get("id") == task_id:
            return task
    raise ValueError(f"task not found: {task_id}")


def _split_validation_candidate(plan: Mapping[str, Any], task_id: Any, replacements: list[Any]) -> dict[str, Any]:
    candidate: dict[str, Any] = {
        "meta": plan.get("meta") if isinstance(plan.get("meta"), dict) else {"goal": "split proposal"},
        "tasks": [dict(task) for task in plan.get("tasks", []) if isinstance(task, dict)],
    }
    original = _task_by_id(candidate, task_id) if isinstance(task_id, str) else None
    inherited_replacements = []
    for replacement in replacements:
        if not isinstance(replacement, dict):
            inherited_replacements.append(replacement)
            continue
        item = dict(replacement)
        if original is not None:
            for field in ("invariant_refs", "surface_refs", "criteria_refs"):
                item.setdefault(field, original.get(field, []))
        inherited_replacements.append(item)
    candidate["tasks"].extend(inherited_replacements)
    for section in OPTIONAL_PLAN_SECTIONS:
        if isinstance(plan.get(section), list):
            candidate[section] = plan[section]
    return candidate


def _worker_id(arguments: Mapping[str, Any], default: str) -> str:
    value = arguments.get("worker_id")
    if value is None:
        value = default
    if not isinstance(value, str):
        raise ValueError("worker_id must be a string when provided")
    return workers.validate_worker_id(_file_safe(value))


def _worker_id_from_arguments(arguments: Mapping[str, Any]) -> str:
    value = arguments.get("worker_id")
    if isinstance(value, str) and value:
        return workers.validate_worker_id(value)
    proposal_id = _proposal_id(arguments, "proposal_id", "proposal")
    proposal_type = arguments.get("proposal_type", "decompose")
    prefix = str(proposal_type) if isinstance(proposal_type, str) and proposal_type else "decompose"
    return workers.validate_worker_id(_file_safe(f"{prefix}-{proposal_id}"))


def _proposal_id(arguments: Mapping[str, Any], field: str, default: str, *, use_plan_id: bool = True) -> str:
    value = arguments.get(field)
    if value is None and use_plan_id:
        value = arguments.get("plan_id")
    if value is None:
        value = default
    if not isinstance(value, str) or not value:
        raise ValueError(f"{field} must be a non-empty string when provided")
    return workers.validate_worker_id(_file_safe(value))


def _required_str(arguments: Mapping[str, Any], field: str) -> str:
    value = arguments.get(field)
    if not isinstance(value, str) or not value:
        raise ValueError(f"{field} must be a non-empty string")
    return value


def _file_safe(value: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9_.-]+", "-", value).strip(".-")
    return safe or "proposal"


def _string_paths(paths: Mapping[str, Path]) -> dict[str, str]:
    artifact_paths = {name: str(path) for name, path in paths.items()}
    artifact_paths["stdout_path"] = artifact_paths["events_path"]
    return artifact_paths
