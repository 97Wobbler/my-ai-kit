"""Filesystem state backend for experimental Autorun MCP workers."""

from __future__ import annotations

import json
import os
import signal
import subprocess
import tempfile
import hashlib
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping

from .state import resolve_repo_root, resolve_workplan_path

STATE_FILENAME = "state.json"
PROMPT_FILENAME = "prompt.md"
EVENTS_FILENAME = "events.jsonl"
STDERR_FILENAME = "stderr.log"
FINAL_FILENAME = "final.md"
RESULT_FILENAME = "result.json"

PENDING = "pending"
RUNNING = "running"
SUCCEEDED = "succeeded"
FAILED = "failed"
CANCELLED = "cancelled"
DEFAULT_RUNTIME = "codex"
SUPPORTED_RUNTIMES = {DEFAULT_RUNTIME}
TERMINAL_STATUSES = {SUCCEEDED, FAILED, CANCELLED}
DEFAULT_ARTIFACT_SUMMARY_BYTES = 16_384
MAX_ARTIFACT_SUMMARY_BYTES = 65_536

_PROCESSES: dict[str, subprocess.Popen[bytes]] = {}


def validate_worker_id(worker_id: str) -> str:
    if (
        not isinstance(worker_id, str)
        or not worker_id
        or "/" in worker_id
        or "\\" in worker_id
        or worker_id in {".", ".."}
        or worker_id != worker_id.strip()
        or any(ord(char) < 32 for char in worker_id)
    ):
        raise ValueError("worker_id must be a non-empty file-safe id")
    return worker_id


def resolve_artifact_root(arguments: Mapping[str, Any], repo_root: Path | None = None) -> Path:
    explicit = arguments.get("artifact_dir")
    if explicit is None:
        explicit = arguments.get("state_dir")
    if explicit is not None:
        if not isinstance(explicit, str) or not explicit:
            raise ValueError("artifact_dir must be a non-empty string when provided")
        path = Path(os.path.expanduser(explicit))
        if not path.is_absolute():
            path = Path.cwd().resolve() / path
        return path.resolve()

    repo = repo_root or resolve_repo_root(arguments.get("repo_root"), required=True)
    repo_hash = hashlib.sha256(str(repo).encode("utf-8")).hexdigest()[:16]
    claude_plugin_data = os.environ.get("CLAUDE_PLUGIN_DATA")
    if claude_plugin_data:
        base = Path(os.path.expanduser(claude_plugin_data)) / "autorun"
    elif sys.platform == "darwin":
        base = Path.home() / "Library" / "Application Support" / "autorun"
    elif os.environ.get("XDG_STATE_HOME"):
        base = Path(os.path.expanduser(os.environ["XDG_STATE_HOME"])) / "autorun"
    elif sys.platform.startswith("win") and os.environ.get("APPDATA"):
        base = Path(os.path.expanduser(os.environ["APPDATA"])) / "autorun"
    else:
        base = Path.home() / ".local" / "state" / "autorun"
    return (base / repo_hash).resolve()


def workers_dir(state_root: Path) -> Path:
    return state_root / "workers"


def worker_dir(state_root: Path, worker_id: str) -> Path:
    return workers_dir(state_root) / validate_worker_id(worker_id)


def worker_state_path(state_root: Path, worker_id: str) -> Path:
    return worker_dir(state_root, worker_id) / STATE_FILENAME


def worker_prompt_path(state_root: Path, worker_id: str) -> Path:
    return worker_dir(state_root, worker_id) / PROMPT_FILENAME


def worker_events_path(state_root: Path, worker_id: str) -> Path:
    return worker_dir(state_root, worker_id) / EVENTS_FILENAME


def worker_stderr_path(state_root: Path, worker_id: str) -> Path:
    return worker_dir(state_root, worker_id) / STDERR_FILENAME


def worker_final_path(state_root: Path, worker_id: str) -> Path:
    return worker_dir(state_root, worker_id) / FINAL_FILENAME


def worker_result_path(state_root: Path, worker_id: str) -> Path:
    return worker_dir(state_root, worker_id) / RESULT_FILENAME


def worker_artifact_paths(state_root: Path, worker_id: str) -> dict[str, Path]:
    return {
        "state_path": worker_state_path(state_root, worker_id),
        "prompt_path": worker_prompt_path(state_root, worker_id),
        "events_path": worker_events_path(state_root, worker_id),
        "stderr_path": worker_stderr_path(state_root, worker_id),
        "final_path": worker_final_path(state_root, worker_id),
        "result_path": worker_result_path(state_root, worker_id),
    }


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"json file not found: {path}")
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"json file is not an object: {path}")
    return data


def save_json(path: Path, data: Mapping[str, Any]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n"

    fd, tmp_name = tempfile.mkstemp(prefix=f".{path.stem}.", suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_name, path)
    except Exception:
        try:
            os.unlink(tmp_name)
        except FileNotFoundError:
            pass
        raise
    return path


def load_worker_state(state_root: Path, worker_id: str) -> dict[str, Any]:
    return load_json(worker_state_path(state_root, worker_id))


def save_worker_state(state_root: Path, worker: Mapping[str, Any]) -> Path:
    worker_id = worker.get("worker_id")
    if not isinstance(worker_id, str):
        raise ValueError("worker_id is required")
    return save_json(worker_state_path(state_root, worker_id), worker)


def build_worker_state(
    state_root: Path,
    worker_id: str,
    plan_id: str,
    task_id: str,
    runtime: str,
    repo_root: str,
    workplan_path: str,
    command: Any,
    timeout_seconds: int | None,
    *,
    status: str = PENDING,
    pid: int | None = None,
    started_at: str | None = None,
    updated_at: str | None = None,
    returncode: int | None = None,
) -> dict[str, Any]:
    worker_id = validate_worker_id(worker_id)
    now = _now()
    started_at = started_at or now
    updated_at = updated_at or started_at
    paths = worker_artifact_paths(state_root, worker_id)
    return {
        "worker_id": worker_id,
        "plan_id": plan_id,
        "task_id": task_id,
        "runtime": runtime,
        "repo_root": repo_root,
        "workplan_path": workplan_path,
        "status": status,
        "command": command,
        "pid": pid,
        "started_at": started_at,
        "updated_at": updated_at,
        "timeout_seconds": timeout_seconds,
        "prompt_path": str(paths["prompt_path"]),
        "events_path": str(paths["events_path"]),
        "stderr_path": str(paths["stderr_path"]),
        "final_path": str(paths["final_path"]),
        "result_path": str(paths["result_path"]),
        "returncode": returncode,
    }


def worker_start(arguments: Mapping[str, Any]) -> dict[str, Any]:
    repo_root = _validate_repo_root(arguments)
    state_root = resolve_artifact_root(arguments, repo_root)
    workplan_path = resolve_workplan_path(arguments)
    plan_id = _required_file_safe_id(arguments, "plan_id")
    task_id = _required_file_safe_id(arguments, "task_id")
    worker_id = _worker_id(arguments, plan_id, task_id)
    prompt = _required_prompt(arguments)
    runtime = _runtime(arguments)
    timeout_seconds = _timeout_seconds(arguments)
    command = _command(arguments, runtime, repo_root, prompt)

    paths = worker_artifact_paths(state_root, worker_id)
    paths["prompt_path"].parent.mkdir(parents=True, exist_ok=True)
    paths["prompt_path"].write_text(prompt, encoding="utf-8")

    worker = build_worker_state(
        state_root,
        worker_id,
        plan_id,
        task_id,
        runtime,
        str(repo_root),
        str(workplan_path),
        command,
        timeout_seconds,
        status=PENDING,
        pid=None,
        returncode=None,
    )
    save_worker_state(state_root, worker)

    try:
        with (
            paths["prompt_path"].open("rb") as stdin,
            paths["events_path"].open("wb") as stdout,
            paths["stderr_path"].open("wb") as stderr,
        ):
            process = subprocess.Popen(
                command,
                cwd=str(repo_root),
                stdout=stdout,
                stderr=stderr,
                stdin=stdin,
                close_fds=True,
            )
    except Exception as exc:
        worker["status"] = FAILED
        worker["updated_at"] = _now()
        worker["error"] = str(exc)
        save_worker_state(state_root, worker)
        raise

    _PROCESSES[worker_id] = process
    worker["pid"] = process.pid
    worker["status"] = RUNNING
    worker["updated_at"] = _now()
    save_worker_state(state_root, worker)

    return _worker_result(worker)


def worker_status(arguments: Mapping[str, Any]) -> dict[str, Any]:
    state_root = resolve_artifact_root(arguments)
    worker_id = _worker_id_from_status_arguments(arguments)
    worker = load_worker_state(state_root, worker_id)
    refreshed = _refresh_worker_state(state_root, worker)
    return _worker_result(refreshed)


def worker_collect(arguments: Mapping[str, Any]) -> dict[str, Any]:
    state_root = resolve_artifact_root(arguments)
    worker_id = _worker_id_from_status_arguments(arguments)
    worker = load_worker_state(state_root, worker_id)
    refreshed = _refresh_worker_state(state_root, worker)
    paths = worker_artifact_paths(state_root, worker_id)
    summaries = _artifact_summaries(paths, _artifact_summary_limit(arguments))

    result = _worker_result(refreshed)
    result["state"] = dict(refreshed)
    result["artifact_paths"] = _string_artifact_paths(paths)
    result["artifact_summaries"] = summaries
    result["stdout_summary"] = summaries["stdout"]
    result["stderr_summary"] = summaries["stderr"]
    result["final_summary"] = summaries["final"]
    result["result_summary"] = summaries["result"]
    return result


def worker_cancel(arguments: Mapping[str, Any]) -> dict[str, Any]:
    state_root = resolve_artifact_root(arguments)
    worker_id = _worker_id_from_status_arguments(arguments)
    worker = load_worker_state(state_root, worker_id)
    refreshed = _refresh_worker_state(state_root, worker)
    if refreshed.get("status") in TERMINAL_STATUSES:
        result = _worker_result(refreshed)
        result["cancelled"] = refreshed.get("status") == CANCELLED
        return result

    process = _PROCESSES.get(worker_id)
    cancelled = False
    returncode: int | None = None

    if process is not None:
        polled = process.poll()
        if polled is None:
            _terminate_process(process)
            cancelled = True
        else:
            returncode = polled
        if process.returncode is not None:
            returncode = process.returncode
        if returncode is not None and not cancelled:
            refreshed["returncode"] = returncode
            refreshed["status"] = SUCCEEDED if returncode == 0 else FAILED
            refreshed["updated_at"] = _now()
            _PROCESSES.pop(worker_id, None)
            save_worker_state(state_root, refreshed)
            result = _worker_result(refreshed)
            result["cancelled"] = False
            return result
    else:
        pid = refreshed.get("pid")
        if isinstance(pid, int) and _pid_running(pid):
            _terminate_pid(pid)
            cancelled = True

    if cancelled:
        if process is not None:
            refreshed["returncode"] = process.returncode
            _PROCESSES.pop(worker_id, None)
        refreshed["status"] = CANCELLED
        refreshed["updated_at"] = _now()
        refreshed["cancelled_at"] = refreshed["updated_at"]
        save_worker_state(state_root, refreshed)
        result = _worker_result(refreshed)
        result["cancelled"] = True
        return result

    refreshed = _refresh_worker_state(state_root, refreshed)
    result = _worker_result(refreshed)
    result["cancelled"] = refreshed.get("status") == CANCELLED
    return result


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _validate_repo_root(arguments: Mapping[str, Any]) -> Path:
    repo_root = resolve_repo_root(arguments.get("repo_root"), required=True)
    if not repo_root.exists():
        raise ValueError(f"repo_root does not exist: {repo_root}")
    if not repo_root.is_dir():
        raise ValueError(f"repo_root must be a directory: {repo_root}")
    return repo_root


def _required_file_safe_id(arguments: Mapping[str, Any], field: str) -> str:
    value = arguments.get(field)
    if (
        not isinstance(value, str)
        or not value
        or "/" in value
        or "\\" in value
        or value in {".", ".."}
        or value != value.strip()
        or any(ord(char) < 32 for char in value)
    ):
        raise ValueError(f"{field} must be a non-empty file-safe id")
    return value


def _worker_id(arguments: Mapping[str, Any], plan_id: str, task_id: str) -> str:
    value = arguments.get("worker_id")
    if value is None:
        return validate_worker_id(f"{plan_id}-{task_id}")
    if not isinstance(value, str):
        raise ValueError("worker_id must be a string when provided")
    return validate_worker_id(value)


def _worker_id_from_status_arguments(arguments: Mapping[str, Any]) -> str:
    value = arguments.get("worker_id")
    if value is not None:
        if not isinstance(value, str):
            raise ValueError("worker_id must be a string when provided")
        return validate_worker_id(value)
    plan_id = _required_file_safe_id(arguments, "plan_id")
    task_id = _required_file_safe_id(arguments, "task_id")
    return validate_worker_id(f"{plan_id}-{task_id}")


def _required_prompt(arguments: Mapping[str, Any]) -> str:
    prompt = arguments.get("prompt")
    if not isinstance(prompt, str) or not prompt:
        raise ValueError("prompt must be a non-empty string")
    return prompt


def _runtime(arguments: Mapping[str, Any]) -> str:
    runtime = arguments.get("runtime", DEFAULT_RUNTIME)
    if runtime is None or runtime == "":
        runtime = DEFAULT_RUNTIME
    if not isinstance(runtime, str):
        raise ValueError("runtime must be a string when provided")
    normalized = runtime.lower()
    if normalized not in SUPPORTED_RUNTIMES:
        supported = ", ".join(sorted(SUPPORTED_RUNTIMES))
        raise ValueError(f"unsupported worker runtime: {runtime}; supported runtimes: {supported}")
    return normalized


def _timeout_seconds(arguments: Mapping[str, Any]) -> int | None:
    value = arguments.get("timeout_seconds")
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError("timeout_seconds must be an integer when provided")
    if value <= 0:
        raise ValueError("timeout_seconds must be greater than zero when provided")
    return value


def _command(arguments: Mapping[str, Any], runtime: str, repo_root: Path, prompt: str) -> list[str]:
    override = _command_override(arguments)
    if override is not None:
        return override
    if runtime == DEFAULT_RUNTIME:
        return ["codex", "exec", "--json", "-C", str(repo_root), "-"]
    raise ValueError(f"unsupported worker runtime: {runtime}")


def _command_override(arguments: Mapping[str, Any]) -> list[str] | None:
    has_command = "command" in arguments and arguments.get("command") is not None
    has_command_override = "command_override" in arguments and arguments.get("command_override") is not None
    if has_command and has_command_override:
        raise ValueError("provide only one of command or command_override")
    value = arguments.get("command") if has_command else arguments.get("command_override")
    if value is None:
        return None
    if not isinstance(value, list) or not value:
        raise ValueError("command override must be a non-empty JSON-compatible list[str]")
    if not all(isinstance(item, str) and item for item in value):
        raise ValueError("command override must contain only non-empty strings")
    return list(value)


def _artifact_summary_limit(arguments: Mapping[str, Any]) -> int:
    value = arguments.get("max_summary_bytes")
    if value is None:
        return DEFAULT_ARTIFACT_SUMMARY_BYTES
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError("max_summary_bytes must be an integer when provided")
    if value <= 0:
        raise ValueError("max_summary_bytes must be greater than zero when provided")
    return min(value, MAX_ARTIFACT_SUMMARY_BYTES)


def _string_artifact_paths(paths: Mapping[str, Path]) -> dict[str, str]:
    artifact_paths = {name: str(path) for name, path in paths.items()}
    artifact_paths["stdout_path"] = artifact_paths["events_path"]
    return artifact_paths


def _artifact_summaries(paths: Mapping[str, Path], limit: int) -> dict[str, dict[str, Any]]:
    return {
        "stdout": _text_artifact_summary(paths["events_path"], limit),
        "stderr": _text_artifact_summary(paths["stderr_path"], limit),
        "final": _text_artifact_summary(paths["final_path"], limit),
        "result": _text_artifact_summary(paths["result_path"], limit),
    }


def _text_artifact_summary(path: Path, limit: int) -> dict[str, Any]:
    summary: dict[str, Any] = {
        "path": str(path),
        "exists": path.exists(),
        "text": "",
        "truncated": False,
    }
    if not summary["exists"]:
        return summary
    if not path.is_file():
        summary["is_file"] = False
        return summary

    size = path.stat().st_size
    summary["is_file"] = True
    summary["size_bytes"] = size
    if size <= limit:
        data = path.read_bytes()
    else:
        with path.open("rb") as handle:
            handle.seek(-limit, os.SEEK_END)
            data = handle.read(limit)
        summary["truncated"] = True
        summary["omitted_bytes"] = size - limit
    summary["text"] = data.decode("utf-8", errors="replace")
    return summary


def _terminate_process(process: subprocess.Popen[bytes]) -> None:
    process.terminate()
    try:
        process.wait(timeout=2)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=2)


def _terminate_pid(pid: int) -> None:
    try:
        os.kill(pid, signal.SIGTERM)
    except ProcessLookupError:
        return
    except PermissionError as exc:
        raise ValueError(f"permission denied while cancelling pid {pid}") from exc


def _refresh_worker_state(state_root: Path, worker: dict[str, Any]) -> dict[str, Any]:
    status = worker.get("status")
    returncode = worker.get("returncode")
    if status == CANCELLED:
        return worker
    if isinstance(returncode, int):
        next_status = SUCCEEDED if returncode == 0 else FAILED
        if status != next_status:
            worker["status"] = next_status
            worker["updated_at"] = _now()
            save_worker_state(state_root, worker)
        return worker

    if status in TERMINAL_STATUSES:
        return worker

    worker_id = worker.get("worker_id")
    pid = worker.get("pid")
    if not isinstance(worker_id, str):
        raise ValueError("worker state is missing worker_id")
    if not isinstance(pid, int):
        worker["status"] = FAILED
        worker["updated_at"] = _now()
        save_worker_state(state_root, worker)
        return worker

    process = _PROCESSES.get(worker_id)
    if process is not None:
        polled = process.poll()
        if polled is None:
            if worker.get("status") != RUNNING:
                worker["status"] = RUNNING
                worker["updated_at"] = _now()
                save_worker_state(state_root, worker)
            return worker
        worker["returncode"] = polled
        worker["status"] = SUCCEEDED if polled == 0 else FAILED
        worker["updated_at"] = _now()
        _PROCESSES.pop(worker_id, None)
        save_worker_state(state_root, worker)
        return worker

    if _pid_running(pid):
        if worker.get("status") != RUNNING:
            worker["status"] = RUNNING
            worker["updated_at"] = _now()
            save_worker_state(state_root, worker)
        return worker

    worker["status"] = FAILED
    worker["updated_at"] = _now()
    save_worker_state(state_root, worker)
    return worker


def _pid_running(pid: int) -> bool:
    if pid <= 0:
        return False
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def _worker_result(worker: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "worker_id": worker["worker_id"],
        "plan_id": worker["plan_id"],
        "task_id": worker["task_id"],
        "status": worker["status"],
        "pid": worker.get("pid"),
        "returncode": worker.get("returncode"),
        "worker": dict(worker),
    }
