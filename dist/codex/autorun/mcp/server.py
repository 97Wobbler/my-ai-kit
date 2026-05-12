#!/usr/bin/env python3
"""Autorun MCP stdio JSON-RPC server skeleton."""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any, Mapping

from autorun_mcp import planner, workers, workplan_io
from autorun_mcp.protocol import JsonRpcError, JsonRpcProtocol, TOOL_ERROR
from autorun_mcp.state import legacy_plan_state_exists

SERVER_NAME = "autorun"
SERVER_VERSION = "0.2.0"
PROTOCOL_VERSION = "2024-11-05"
TOOL_AUTORUN_STATUS = "autorun_status"
TOOL_AUTORUN_PLAN_CREATE = "autorun_plan_create"
TOOL_AUTORUN_PLAN_VALIDATE = "autorun_plan_validate"
TOOL_AUTORUN_PLAN_REFINE = "autorun_plan_refine"
TOOL_AUTORUN_TASK_SPLIT = "autorun_task_split"
TOOL_AUTORUN_NEXT_BATCH = "autorun_next_batch"
TOOL_AUTORUN_TASK_MARK_STARTED = "autorun_task_mark_started"
TOOL_AUTORUN_TASK_MARK_VERIFIED = "autorun_task_mark_verified"
TOOL_AUTORUN_TASK_MARK_COMMITTED = "autorun_task_mark_committed"
TOOL_AUTORUN_PLAN_STATUS = "autorun_plan_status"
TOOL_AUTORUN_IMPORT_WORKPLAN = "autorun_import_workplan"
TOOL_AUTORUN_EXPORT_WORKPLAN = "autorun_export_workplan"
TOOL_AUTORUN_WORKER_START = "autorun_worker_start"
TOOL_AUTORUN_WORKER_STATUS = "autorun_worker_status"
TOOL_AUTORUN_WORKER_COLLECT = "autorun_worker_collect"
TOOL_AUTORUN_WORKER_CANCEL = "autorun_worker_cancel"
WORKER_TOOLS = {
    TOOL_AUTORUN_WORKER_START,
    TOOL_AUTORUN_WORKER_STATUS,
    TOOL_AUTORUN_WORKER_COLLECT,
    TOOL_AUTORUN_WORKER_CANCEL,
}


def initialize(_params: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "protocolVersion": PROTOCOL_VERSION,
        "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
        "capabilities": {"tools": {}},
    }


def tools_list(_params: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "tools": [
            {
                "name": TOOL_AUTORUN_STATUS,
                "description": "Report Autorun MCP server and repository state availability.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "repo_root": {
                            "type": "string",
                            "description": "Repository root path for the active user project.",
                        }
                    },
                    "required": ["repo_root"],
                    "additionalProperties": False,
                },
            },
            _tool(
                TOOL_AUTORUN_PLAN_CREATE,
                "Create or replace repo-root workplan.yaml from model-drafted meta/tasks.",
                {
                    "repo_root": _string("Repository root path for the active user project."),
                    "workplan_path": _string("Optional workplan path. Defaults to <repo_root>/workplan.yaml."),
                    "state_dir": _string("Deprecated compatibility input; plan state is stored in workplan.yaml."),
                    "plan_id": _string("Deprecated compatibility id. Does not select a state file."),
                    "meta": {"type": "object"},
                    "tasks": {"type": "array", "items": {"type": "object"}},
                    "run_policy": {"type": "object"},
                },
                ["meta", "tasks"],
                any_of=[{"required": ["repo_root"]}, {"required": ["workplan_path"]}],
            ),
            _plan_tool(
                TOOL_AUTORUN_PLAN_VALIDATE,
                "Validate required fields, dependencies, gates, outputs, and task granularity.",
            ),
            _plan_tool(
                TOOL_AUTORUN_PLAN_REFINE,
                "Return the deterministic next planning action for a stored plan.",
            ),
            _tool(
                TOOL_AUTORUN_TASK_SPLIT,
                "Retire an existing task and append replacement tasks.",
                {
                    **_plan_properties(),
                    "task_id": _string("Task id to retire."),
                    "replacement_tasks": {"type": "array", "items": {"type": "object"}},
                },
                ["task_id", "replacement_tasks"],
                any_of=[{"required": ["repo_root"]}, {"required": ["workplan_path"]}],
            ),
            _plan_tool(
                TOOL_AUTORUN_NEXT_BATCH,
                "Return runnable non-human-gated tasks with non-overlapping output paths.",
            ),
            _task_lifecycle_tool(
                TOOL_AUTORUN_TASK_MARK_STARTED,
                "Mark a pending task as started.",
            ),
            _task_lifecycle_tool(
                TOOL_AUTORUN_TASK_MARK_VERIFIED,
                "Mark a started task as verified.",
            ),
            _task_lifecycle_tool(
                TOOL_AUTORUN_TASK_MARK_COMMITTED,
                "Mark a verified task as committed and done.",
            ),
            _plan_tool(
                TOOL_AUTORUN_PLAN_STATUS,
                "Return progress, runnable tasks, blocked tasks, human gates, and active tasks.",
            ),
            _tool(
                TOOL_AUTORUN_IMPORT_WORKPLAN,
                "Deprecated compatibility shim: validate workplan.yaml, which is already MCP state.",
                {
                    "repo_root": _string("Repository root path for the active user project."),
                    "workplan_path": _string("Optional workplan path. Defaults to <repo_root>/workplan.yaml."),
                    "state_dir": _string("Deprecated compatibility input; ignored for plan state."),
                    "plan_id": _string("Deprecated compatibility id. Does not select a state file."),
                    "run_policy": {"type": "object"},
                },
                any_of=[{"required": ["repo_root"]}, {"required": ["workplan_path"]}],
            ),
            _tool(
                TOOL_AUTORUN_EXPORT_WORKPLAN,
                "Deprecated compatibility shim: validate and return current workplan.yaml.",
                {
                    **_plan_properties(),
                    "force": {"type": "boolean", "description": "Export even when validation has errors."},
                },
                any_of=[{"required": ["repo_root"]}, {"required": ["workplan_path"]}],
            ),
            _tool(
                TOOL_AUTORUN_WORKER_START,
                "Start an experimental Autorun worker process for a task.",
                {
                    "repo_root": _string("Repository root path for the active user project."),
                    "artifact_dir": _string("Optional worker artifact root. Defaults to user state outside the repo."),
                    "state_dir": _string("Deprecated alias for artifact_dir."),
                    "workplan_path": _string("Optional workplan path. Defaults to <repo_root>/workplan.yaml."),
                    "plan_id": _string("Deprecated compatibility id."),
                    "task_id": _string("Task id."),
                    "worker_id": _string("Optional file-safe worker id. Defaults to <plan_id>-<task_id>."),
                    "prompt": _string("Worker prompt to pass to the runtime."),
                    "runtime": _string("Optional worker runtime. Defaults to codex."),
                    "timeout_seconds": {
                        "type": "integer",
                        "description": "Optional positive timeout for callers to track.",
                    },
                    "command": _string_list("Optional command override list for tests."),
                    "command_override": _string_list("Optional command override list for tests."),
                },
                ["repo_root", "plan_id", "task_id", "prompt"],
            ),
            _worker_lookup_tool(
                TOOL_AUTORUN_WORKER_STATUS,
                "Return status for an experimental Autorun worker process.",
            ),
            _tool(
                TOOL_AUTORUN_WORKER_COLLECT,
                "Return worker status, artifact paths, and concise artifact summaries.",
                {
                    **_worker_lookup_properties(),
                    "max_summary_bytes": {
                        "type": "integer",
                        "description": "Optional positive maximum bytes per artifact summary.",
                    },
                },
                any_of=_worker_lookup_any_of(),
            ),
            _worker_lookup_tool(
                TOOL_AUTORUN_WORKER_CANCEL,
                "Cancel a running experimental Autorun worker process.",
            ),
        ]
    }


def tools_call(params: Mapping[str, Any]) -> dict[str, Any]:
    name = params.get("name")
    arguments = params.get("arguments", {})
    if arguments is None:
        arguments = {}
    if not isinstance(arguments, dict):
        raise JsonRpcError(TOOL_ERROR, "Tool arguments must be an object")

    try:
        result = _call_tool(name, arguments)
    except JsonRpcError:
        raise
    except Exception as exc:
        raise JsonRpcError(TOOL_ERROR, "Tool error", {"error": str(exc)}) from exc

    return {
        "content": [{"type": "text", "text": format_tool_result(name, result)}],
        "structuredContent": result,
    }


def _call_tool(name: Any, arguments: Mapping[str, Any]) -> dict[str, Any]:
    if name == TOOL_AUTORUN_STATUS:
        return autorun_status(arguments)
    if name == TOOL_AUTORUN_PLAN_CREATE:
        return planner.plan_create(arguments)
    if name == TOOL_AUTORUN_PLAN_VALIDATE:
        return planner.plan_validate(arguments)
    if name == TOOL_AUTORUN_PLAN_REFINE:
        return planner.plan_refine(arguments)
    if name == TOOL_AUTORUN_TASK_SPLIT:
        return planner.task_split(arguments)
    if name == TOOL_AUTORUN_NEXT_BATCH:
        return planner.next_batch(arguments)
    if name == TOOL_AUTORUN_TASK_MARK_STARTED:
        return planner.task_mark_started(arguments)
    if name == TOOL_AUTORUN_TASK_MARK_VERIFIED:
        return planner.task_mark_verified(arguments)
    if name == TOOL_AUTORUN_TASK_MARK_COMMITTED:
        return planner.task_mark_committed(arguments)
    if name == TOOL_AUTORUN_PLAN_STATUS:
        return planner.plan_status(arguments)
    if name == TOOL_AUTORUN_IMPORT_WORKPLAN:
        return workplan_io.import_workplan(arguments)
    if name == TOOL_AUTORUN_EXPORT_WORKPLAN:
        return workplan_io.export_workplan(arguments)
    if name == TOOL_AUTORUN_WORKER_START:
        return workers.worker_start(arguments)
    if name == TOOL_AUTORUN_WORKER_STATUS:
        return workers.worker_status(arguments)
    if name == TOOL_AUTORUN_WORKER_COLLECT:
        return workers.worker_collect(arguments)
    if name == TOOL_AUTORUN_WORKER_CANCEL:
        return workers.worker_cancel(arguments)
    raise JsonRpcError(TOOL_ERROR, f"Unknown tool: {name}")


def autorun_status(arguments: Mapping[str, Any]) -> dict[str, Any]:
    repo_root_arg = arguments.get("repo_root")
    if not isinstance(repo_root_arg, str) or not repo_root_arg:
        raise ValueError("repo_root must be a non-empty string")

    cwd = Path.cwd().resolve()
    repo_root = _resolve_repo_root(repo_root_arg, cwd)
    state = _state_backend_availability(repo_root)

    return {
        "server": {"name": SERVER_NAME, "version": SERVER_VERSION},
        "cwd": str(cwd),
        "repo_root": str(repo_root),
        "state_backend": state,
    }


def _resolve_repo_root(repo_root_arg: str | None, cwd: Path) -> Path:
    if not repo_root_arg:
        return cwd
    path = Path(os.path.expanduser(repo_root_arg))
    if not path.is_absolute():
        path = cwd / path
    return path.resolve()


def _state_backend_availability(repo_root: Path) -> dict[str, Any]:
    workplan = repo_root / "workplan.yaml"
    git_dir = repo_root / ".git"
    return {
        "backend": "filesystem",
        "available": repo_root.exists() and repo_root.is_dir(),
        "repo_root_exists": repo_root.exists(),
        "workplan_exists": workplan.exists(),
        "legacy_json_plans_exist": legacy_plan_state_exists({"repo_root": str(repo_root)}),
        "git_metadata_exists": git_dir.exists(),
    }


def format_status(status: Mapping[str, Any]) -> str:
    state = status["state_backend"]
    return "\n".join(
        [
            f"Autorun MCP server {status['server']['version']}",
            f"cwd: {status['cwd']}",
            f"repo_root: {status['repo_root']}",
            f"state_backend: workplan.yaml available={state['available']}",
            f"workplan_exists: {state['workplan_exists']}",
            f"legacy_json_plans_exist: {state['legacy_json_plans_exist']}",
        ]
    )


def format_tool_result(name: Any, result: Mapping[str, Any]) -> str:
    if name == TOOL_AUTORUN_STATUS:
        return format_status(result)
    if name in WORKER_TOOLS:
        return (
            f"{name}: worker_id={result.get('worker_id')} "
            f"task_id={result.get('task_id')} status={result.get('status')}"
        )
    plan_id = result.get("plan_id")
    if not plan_id and isinstance(result.get("plan"), dict):
        plan_id = result["plan"].get("plan_id")
    prefix = f"{name}: plan_id={plan_id}" if plan_id else str(name)
    if "next_action" in result:
        return f"{prefix} next_action={result['next_action']}"
    if "validation" in result:
        validation = result["validation"]
        return (
            f"{prefix} valid={validation.get('valid')} "
            f"errors={len(validation.get('errors', []))} "
            f"warnings={len(validation.get('warnings', []))}"
        )
    if "task_ids" in result:
        return f"{prefix} task_ids={', '.join(result['task_ids'])}"
    if "progress" in result:
        progress = result["progress"]
        return f"{prefix} done={progress['done']}/{progress['total']} runnable={len(result.get('runnable', []))}"
    if "workplan_path" in result:
        return f"{prefix} workplan_path={result['workplan_path']}"
    if "status" in result:
        return f"{prefix} task_id={result.get('task_id')} status={result['status']}"
    return prefix


def _tool(
    name: str,
    description: str,
    properties: Mapping[str, Any],
    required: list[str] | None = None,
    any_of: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    input_schema: dict[str, Any] = {
        "type": "object",
        "properties": dict(properties),
        "required": required or [],
        "additionalProperties": False,
    }
    if any_of:
        input_schema["anyOf"] = any_of
    return {
        "name": name,
        "description": description,
        "inputSchema": input_schema,
    }


def _plan_tool(name: str, description: str) -> dict[str, Any]:
    return _tool(
        name,
        description,
        _plan_properties(),
        any_of=[{"required": ["repo_root"]}, {"required": ["workplan_path"]}],
    )


def _task_lifecycle_tool(name: str, description: str) -> dict[str, Any]:
    return _tool(
        name,
        description,
        {
            **_plan_properties(),
            "task_id": _string("Task id."),
            "worker_id": _string("Optional worker id to record on verified lifecycle updates."),
            "commit": _string("Optional commit identifier to record on committed lifecycle updates."),
        },
        ["task_id"],
        any_of=[{"required": ["repo_root"]}, {"required": ["workplan_path"]}],
    )


def _worker_lookup_tool(name: str, description: str) -> dict[str, Any]:
    return _tool(
        name,
        description,
        _worker_lookup_properties(),
        any_of=_worker_lookup_any_of(),
    )


def _plan_properties() -> dict[str, Any]:
    return {
        "repo_root": _string("Repository root path for the active user project."),
        "workplan_path": _string("Optional workplan path. Defaults to <repo_root>/workplan.yaml."),
        "state_dir": _string("Deprecated compatibility input; plan state is stored in workplan.yaml."),
        "plan_id": _string("Deprecated compatibility id. Does not select a state file."),
    }


def _worker_lookup_properties() -> dict[str, Any]:
    return {
        "repo_root": _string("Repository root path for the active user project."),
        "artifact_dir": _string("Optional worker artifact root. Defaults to user state outside the repo."),
        "state_dir": _string("Deprecated alias for artifact_dir."),
        "plan_id": _string("Compatibility plan id, required when worker_id is omitted."),
        "task_id": _string("Task id, required when worker_id is omitted."),
        "worker_id": _string("Worker id, required when plan_id and task_id are omitted."),
    }


def _worker_lookup_any_of() -> list[dict[str, list[str]]]:
    return [
        {"required": ["artifact_dir", "worker_id"]},
        {"required": ["repo_root", "worker_id"]},
        {"required": ["artifact_dir", "plan_id", "task_id"]},
        {"required": ["repo_root", "plan_id", "task_id"]},
    ]


def _string(description: str) -> dict[str, str]:
    return {"type": "string", "description": description}


def _string_list(description: str) -> dict[str, Any]:
    return {
        "type": "array",
        "items": {"type": "string"},
        "minItems": 1,
        "description": description,
    }


def build_protocol() -> JsonRpcProtocol:
    return JsonRpcProtocol(
        {
            "initialize": initialize,
            "tools/list": tools_list,
            "tools/call": tools_call,
        }
    )


def main() -> int:
    protocol = build_protocol()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        response = protocol.handle_line(line)
        if response is not None:
            sys.stdout.write(response + "\n")
            sys.stdout.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
