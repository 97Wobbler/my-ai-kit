#!/usr/bin/env python3
"""Scribe MCP stdio JSON-RPC server."""

from __future__ import annotations

import importlib.util
import json
import os
import shutil
import shlex
import subprocess
import sys
import threading
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Mapping

from scribe_mcp.output import (
    TranscriptionVariant,
    write_partial_transcription_variant,
    write_transcription_manifest,
    write_transcription_variant,
)
from scribe_mcp.presets import (
    DEFAULT_PRESET_ORDER,
    MAX_VARIANT_COUNT,
    MIN_VARIANT_COUNT,
    PresetValidationError,
    get_preset,
    select_presets,
)
from scribe_mcp.protocol import JsonRpcError, JsonRpcProtocol, TOOL_ERROR
from scribe_mcp.review import DEFAULT_MAX_ITEMS, DEFAULT_PACKET_ID, build_review_state
from scribe_mcp.transcribe import MissingTranscriptionDependency, transcribe_audio

SERVER_NAME = "scribe"
SERVER_VERSION = "0.1.3"
PROTOCOL_VERSION = "2024-11-05"
TOOL_SCRIBE_BUILD_REVIEW_STATE = "scribe_build_review_state"
TOOL_SCRIBE_STT_STATUS = "scribe_stt_status"
TOOL_SCRIBE_SETUP_STT = "scribe_setup_stt"
TOOL_SCRIBE_TRANSCRIBE_FILE = "scribe_transcribe_file"
TOOL_SCRIBE_TRANSCRIBE_VARIANTS = "scribe_transcribe_variants"
TOOL_SCRIBE_TRANSCRIBE_JOB_START = "scribe_transcribe_job_start"
TOOL_SCRIBE_TRANSCRIBE_JOB_STATUS = "scribe_transcribe_job_status"
TOOL_SCRIBE_TRANSCRIBE_JOB_COLLECT = "scribe_transcribe_job_collect"
TOOL_SCRIBE_TRANSCRIBE_JOB_CANCEL = "scribe_transcribe_job_cancel"
DEFAULT_PRESET_ID = "balanced"
MANIFEST_PATH = "manifest.json"
JOB_PATH = "job.json"
_MISSING = object()
DEFAULT_SETUP_TIMEOUT_SECONDS = 600
MAX_CAPTURED_SETUP_OUTPUT = 4000
DEFAULT_SYNC_MAX_DURATION_SECONDS = 600
DEFAULT_SYNC_MAX_AUDIO_BYTES = 25 * 1024 * 1024
FFPROBE_TIMEOUT_SECONDS = 10
PROGRESS_TEXT_PREVIEW_CHARS = 200
JOB_STATUS_QUEUED = "queued"
JOB_STATUS_RUNNING = "running"
JOB_STATUS_COMPLETED = "completed"
JOB_STATUS_THRESHOLD_REACHED = "threshold_reached"
JOB_STATUS_PARTIAL_FAILED = "partial_failed"
JOB_STATUS_FAILED = "failed"
JOB_STATUS_CANCEL_REQUESTED = "cancel_requested"
JOB_STATUS_CANCELLED = "cancelled"
VARIANT_STATUS_QUEUED = "queued"
VARIANT_STATUS_RUNNING = "running"
VARIANT_STATUS_COMPLETED = "completed"
VARIANT_STATUS_FAILED = "failed"
VARIANT_STATUS_CANCELLED = "cancelled"
VARIANT_STATUS_SKIPPED = "skipped"
CANCEL_REQUEST_NOTE = (
    "Cancellation is cooperative. It stops before the next preset; an in-flight "
    "faster-whisper call may finish before the job exits."
)
CANCEL_OBSERVED_NOTE = "Cancellation observed before scheduling the next preset."
THRESHOLD_REACHED_NOTE = (
    "Completed variant threshold reached; remaining queued presets were not scheduled."
)
TERMINAL_JOB_STATUSES = {
    JOB_STATUS_COMPLETED,
    JOB_STATUS_THRESHOLD_REACHED,
    JOB_STATUS_PARTIAL_FAILED,
    JOB_STATUS_FAILED,
    JOB_STATUS_CANCELLED,
}
_ACTIVE_JOBS: dict[str, "_JobControl"] = {}
_ACTIVE_JOBS_LOCK = threading.Lock()


class _JobControl:
    def __init__(self, job_id: str, job_path: Path):
        self.job_id = job_id
        self.job_path = job_path
        self.cancel_requested = threading.Event()
        self.thread: threading.Thread | None = None


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
                "name": TOOL_SCRIBE_BUILD_REVIEW_STATE,
                "description": (
                    "Build a machine-readable Scribe transcript review gate from "
                    "caller-identified high-impact review items."
                ),
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "high_impact_items": {
                            "type": "array",
                            "items": {"type": "object"},
                            "description": (
                                "Caller-identified review items. Only items with "
                                "impact=high are included in the clarification packet."
                            ),
                        },
                        "transcript_path": _nullable_string_schema(
                            "Optional transcript path associated with the review state."
                        ),
                        "review_path": _nullable_string_schema(
                            "Optional transcript-review.md path associated with the review state."
                        ),
                        "manifest_path": _nullable_string_schema(
                            "Optional manifest.json path associated with the review state."
                        ),
                        "max_items": {
                            "type": "integer",
                            "minimum": 1,
                            "maximum": 20,
                            "description": (
                                "Maximum items to include in the clarification packet. "
                                f"Defaults to {DEFAULT_MAX_ITEMS}."
                            ),
                        },
                        "packet_id": {
                            "type": "string",
                            "description": f"Clarification packet id. Defaults to {DEFAULT_PACKET_ID}.",
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
            {
                "name": TOOL_SCRIBE_STT_STATUS,
                "description": "Report local STT runtime dependency availability for Scribe.",
                "inputSchema": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                    "additionalProperties": False,
                },
            },
            {
                "name": TOOL_SCRIBE_SETUP_STT,
                "description": (
                    "Check Scribe local STT dependencies and optionally install missing "
                    "Python package dependencies in the MCP server environment."
                ),
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "install": _boolean_schema(
                            "When true, install missing Python package dependencies. Defaults to false."
                        ),
                        "upgrade": _boolean_schema(
                            "When true with install, pass --upgrade to pip. Defaults to false."
                        ),
                        "timeout_seconds": {
                            "type": "integer",
                            "minimum": 30,
                            "maximum": 3600,
                            "description": (
                                "Maximum seconds for each setup command. "
                                f"Defaults to {DEFAULT_SETUP_TIMEOUT_SECONDS}."
                            ),
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
            {
                "name": TOOL_SCRIBE_TRANSCRIBE_FILE,
                "description": "Transcribe one audio file with a single Scribe STT preset.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "audio_path": _path_schema("Existing audio file to transcribe."),
                        "output_root": _path_schema("Directory where transcript outputs will be written."),
                        "language": _nullable_string_schema("Optional BCP-47 language hint."),
                        "model_size": _nullable_string_schema("Optional faster-whisper model size override."),
                        "device": _string_schema("faster-whisper device. Defaults to auto."),
                        "compute_type": _string_schema("faster-whisper compute type. Defaults to default."),
                        "preset_id": {
                            "type": "string",
                            "description": f"Scribe preset id. Defaults to {DEFAULT_PRESET_ID}.",
                            "enum": list(DEFAULT_PRESET_ORDER),
                        },
                        "force_sync": _boolean_schema(
                            "When true, bypass the synchronous long-audio guard. Defaults to false."
                        ),
                        "max_sync_duration_seconds": _sync_duration_limit_schema(),
                        "max_sync_audio_bytes": _sync_audio_bytes_limit_schema(),
                    },
                    "required": ["audio_path", "output_root"],
                    "additionalProperties": False,
                },
            },
            {
                "name": TOOL_SCRIBE_TRANSCRIBE_VARIANTS,
                "description": "Transcribe one audio file into multiple deterministic Scribe STT variants.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "audio_path": _path_schema("Existing audio file to transcribe."),
                        "output_root": _path_schema("Directory where transcript outputs will be written."),
                        "language": _nullable_string_schema("Optional BCP-47 language hint."),
                        "model_size": _nullable_string_schema("Optional faster-whisper model size override."),
                        "device": _string_schema("faster-whisper device. Defaults to auto."),
                        "compute_type": _string_schema("faster-whisper compute type. Defaults to default."),
                        "variant_count": {
                            "type": "integer",
                            "minimum": MIN_VARIANT_COUNT,
                            "maximum": MAX_VARIANT_COUNT,
                            "description": "Number of transcript variants to generate.",
                        },
                        "preset_ids": _preset_ids_schema(),
                        "requested_preset_ids": _preset_ids_schema(),
                        "force_sync": _boolean_schema(
                            "When true, bypass the synchronous long-audio guard. Defaults to false."
                        ),
                        "max_sync_duration_seconds": _sync_duration_limit_schema(),
                        "max_sync_audio_bytes": _sync_audio_bytes_limit_schema(),
                    },
                    "required": ["audio_path", "output_root", "variant_count"],
                    "additionalProperties": False,
                },
            },
            {
                "name": TOOL_SCRIBE_TRANSCRIBE_JOB_START,
                "description": (
                    "Start a background Scribe STT job for one audio file and persist "
                    "completed variants incrementally."
                ),
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "audio_path": _path_schema("Existing audio file to transcribe."),
                        "output_root": _path_schema(
                            "Job/output directory where job.json, manifest.json, and variants are written."
                        ),
                        "language": _nullable_string_schema("Optional BCP-47 language hint."),
                        "model_size": _nullable_string_schema("Optional faster-whisper model size override."),
                        "device": _string_schema("faster-whisper device. Defaults to auto."),
                        "compute_type": _string_schema("faster-whisper compute type. Defaults to default."),
                        "variant_count": {
                            "type": "integer",
                            "minimum": MIN_VARIANT_COUNT,
                            "maximum": MAX_VARIANT_COUNT,
                            "description": "Number of transcript variants to generate.",
                        },
                        "preset_ids": _preset_ids_schema(),
                        "requested_preset_ids": _preset_ids_schema(),
                        "stop_after_completed_variants": {
                            "type": "integer",
                            "minimum": 1,
                            "maximum": MAX_VARIANT_COUNT,
                            "description": (
                                "Optional completed-variant threshold for background jobs. "
                                "When reached, remaining queued presets are skipped and the "
                                "job finishes with threshold_reached."
                            ),
                        },
                    },
                    "required": ["audio_path", "output_root", "variant_count"],
                    "additionalProperties": False,
                },
            },
            {
                "name": TOOL_SCRIBE_TRANSCRIBE_JOB_STATUS,
                "description": "Report a Scribe background STT job status from job_id or job.json path.",
                "inputSchema": _job_lookup_schema(),
            },
            {
                "name": TOOL_SCRIBE_TRANSCRIBE_JOB_COLLECT,
                "description": (
                    "Collect a Scribe background STT job and report whether enough "
                    "completed variants exist for scribe:canon."
                ),
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        **_job_lookup_properties(),
                        "minimum_completed_variants": {
                            "type": "integer",
                            "minimum": 1,
                            "maximum": MAX_VARIANT_COUNT,
                            "description": "Minimum completed variants needed to continue. Defaults to 2.",
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
            {
                "name": TOOL_SCRIBE_TRANSCRIBE_JOB_CANCEL,
                "description": (
                    "Request cancellation for a Scribe background STT job without "
                    "killing the MCP server transport."
                ),
                "inputSchema": _job_lookup_schema(),
            },
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
    if name == TOOL_SCRIBE_BUILD_REVIEW_STATE:
        return scribe_build_review_state(arguments)
    if name == TOOL_SCRIBE_STT_STATUS:
        return scribe_stt_status(arguments)
    if name == TOOL_SCRIBE_SETUP_STT:
        return scribe_setup_stt(arguments)
    if name == TOOL_SCRIBE_TRANSCRIBE_FILE:
        return scribe_transcribe_file(arguments)
    if name == TOOL_SCRIBE_TRANSCRIBE_VARIANTS:
        return scribe_transcribe_variants(arguments)
    if name == TOOL_SCRIBE_TRANSCRIBE_JOB_START:
        return scribe_transcribe_job_start(arguments)
    if name == TOOL_SCRIBE_TRANSCRIBE_JOB_STATUS:
        return scribe_transcribe_job_status(arguments)
    if name == TOOL_SCRIBE_TRANSCRIBE_JOB_COLLECT:
        return scribe_transcribe_job_collect(arguments)
    if name == TOOL_SCRIBE_TRANSCRIBE_JOB_CANCEL:
        return scribe_transcribe_job_cancel(arguments)
    raise JsonRpcError(TOOL_ERROR, f"Unknown tool: {name}")


def scribe_build_review_state(arguments: Mapping[str, Any]) -> dict[str, Any]:
    high_impact_items = _review_items_argument(arguments)
    max_items = _int_argument(
        arguments,
        "max_items",
        default=DEFAULT_MAX_ITEMS,
        minimum=1,
        maximum=20,
    )
    packet_id = _string_argument(
        arguments,
        "packet_id",
        default=DEFAULT_PACKET_ID,
    )
    review_state = build_review_state(
        high_impact_items,
        transcript_path=_nullable_string_argument(arguments, "transcript_path"),
        review_path=_nullable_string_argument(arguments, "review_path"),
        manifest_path=_nullable_string_argument(arguments, "manifest_path"),
        max_items=max_items,
        packet_id=packet_id,
    )

    return {
        "server": {"name": SERVER_NAME, "version": SERVER_VERSION},
        "tool": TOOL_SCRIBE_BUILD_REVIEW_STATE,
        "success": True,
        "requires_user_response": review_state["requires_user_response"],
        "clarification_packet": review_state["clarification_packet"],
        "review_state": review_state,
    }


def scribe_stt_status(_arguments: Mapping[str, Any] | None = None) -> dict[str, Any]:
    faster_whisper = _faster_whisper_status()
    ffmpeg = _ffmpeg_status()
    ready = faster_whisper["available"] and ffmpeg["available"]

    return {
        "server": {"name": SERVER_NAME, "version": SERVER_VERSION},
        "stt_ready": ready,
        "dependencies": {
            "faster_whisper": faster_whisper,
            "ffmpeg": ffmpeg,
        },
        "python": _python_status(),
        "install_guidance": _install_guidance(faster_whisper, ffmpeg),
    }


def scribe_setup_stt(arguments: Mapping[str, Any]) -> dict[str, Any]:
    install = _bool_argument(arguments, "install", default=False)
    upgrade = _bool_argument(arguments, "upgrade", default=False)
    timeout_seconds = _int_argument(
        arguments,
        "timeout_seconds",
        default=DEFAULT_SETUP_TIMEOUT_SECONDS,
        minimum=30,
        maximum=3600,
    )

    before = scribe_stt_status()
    actions: list[dict[str, Any]] = []

    if not before["dependencies"]["faster_whisper"]["available"]:
        command = _pip_install_command(upgrade=upgrade)
        if install:
            actions.append(
                _run_setup_command(
                    dependency="faster-whisper",
                    command=command,
                    timeout_seconds=timeout_seconds,
                )
            )
        else:
            actions.append(
                {
                    "dependency": "faster-whisper",
                    "status": "skipped",
                    "reason": "install=false",
                    "command": _format_command(command),
                    "note": (
                        "Call scribe_setup_stt with install=true to install this "
                        "Python package in the MCP server environment."
                    ),
                }
            )
    else:
        actions.append(
            {
                "dependency": "faster-whisper",
                "status": "already_available",
                "command": "",
                "note": "No Python package install needed.",
            }
        )

    if not before["dependencies"]["ffmpeg"]["available"]:
        actions.append(
            {
                "dependency": "ffmpeg",
                "status": "manual_required",
                "command": "brew install ffmpeg",
                "note": (
                    "Scribe does not install OS packages from the MCP server. "
                    "Install ffmpeg with the system package manager and make sure it is on PATH."
                ),
            }
        )
    else:
        actions.append(
            {
                "dependency": "ffmpeg",
                "status": "already_available",
                "command": "",
                "note": "No OS package install needed.",
            }
        )

    after = scribe_stt_status()
    failed = any(action["status"] == "failed" for action in actions)
    return {
        "server": {"name": SERVER_NAME, "version": SERVER_VERSION},
        "tool": TOOL_SCRIBE_SETUP_STT,
        "install_requested": install,
        "upgrade_requested": upgrade,
        "timeout_seconds": timeout_seconds,
        "setup_ready": after["stt_ready"],
        "success": after["stt_ready"] and not failed,
        "python": _python_status(),
        "before": before,
        "actions": actions,
        "after": after,
    }


def scribe_transcribe_file(arguments: Mapping[str, Any]) -> dict[str, Any]:
    audio_path = _required_path_argument(arguments, "audio_path", must_be_file=True)
    output_root = _required_path_argument(arguments, "output_root")
    language = _nullable_string_argument(arguments, "language")
    model_size = _nullable_string_argument(arguments, "model_size")
    device = _string_argument(arguments, "device", default="auto")
    compute_type = _string_argument(arguments, "compute_type", default="default")
    preset = _preset_argument(arguments)
    guard = _synchronous_transcription_guard(
        TOOL_SCRIBE_TRANSCRIBE_FILE,
        arguments,
        audio_path=audio_path,
        output_root=output_root,
    )
    if guard is not None:
        return guard

    return _transcribe_presets(
        TOOL_SCRIBE_TRANSCRIBE_FILE,
        audio_path=audio_path,
        output_root=output_root,
        presets=(preset,),
        language=language,
        model_size=model_size,
        device=device,
        compute_type=compute_type,
    )


def scribe_transcribe_variants(arguments: Mapping[str, Any]) -> dict[str, Any]:
    audio_path = _required_path_argument(arguments, "audio_path", must_be_file=True)
    output_root = _required_path_argument(arguments, "output_root")
    language = _nullable_string_argument(arguments, "language")
    model_size = _nullable_string_argument(arguments, "model_size")
    device = _string_argument(arguments, "device", default="auto")
    compute_type = _string_argument(arguments, "compute_type", default="default")
    variant_count = _variant_count_argument(arguments)
    requested_ids = _requested_preset_ids_argument(arguments)
    guard = _synchronous_transcription_guard(
        TOOL_SCRIBE_TRANSCRIBE_VARIANTS,
        arguments,
        audio_path=audio_path,
        output_root=output_root,
    )
    if guard is not None:
        return guard

    try:
        selected_presets = select_presets(variant_count, requested_ids)
    except PresetValidationError as exc:
        field = "preset_ids" if requested_ids is not None else "variant_count"
        _raise_invalid_argument(field, str(exc))

    return _transcribe_presets(
        TOOL_SCRIBE_TRANSCRIBE_VARIANTS,
        audio_path=audio_path,
        output_root=output_root,
        presets=selected_presets,
        language=language,
        model_size=model_size,
        device=device,
        compute_type=compute_type,
    )


def scribe_transcribe_job_start(arguments: Mapping[str, Any]) -> dict[str, Any]:
    audio_path = _required_path_argument(arguments, "audio_path", must_be_file=True)
    output_root = _required_path_argument(arguments, "output_root")
    language = _nullable_string_argument(arguments, "language")
    model_size = _nullable_string_argument(arguments, "model_size")
    device = _string_argument(arguments, "device", default="auto")
    compute_type = _string_argument(arguments, "compute_type", default="default")
    variant_count = _variant_count_argument(arguments)
    requested_ids = _requested_preset_ids_argument(arguments)
    stop_after_completed_variants = _completed_variant_threshold_argument(
        arguments,
        variant_count=variant_count,
    )

    try:
        selected_presets = select_presets(variant_count, requested_ids)
    except PresetValidationError as exc:
        field = "preset_ids" if requested_ids is not None else "variant_count"
        _raise_invalid_argument(field, str(exc))

    job_id = _new_job_id()
    output_root.mkdir(parents=True, exist_ok=True)
    job_path = output_root / JOB_PATH
    created_at = _utc_now()
    job = {
        "job_id": job_id,
        "status": JOB_STATUS_QUEUED,
        "audio_path": str(audio_path),
        "output_root": str(output_root),
        "job_path": JOB_PATH,
        "manifest_path": MANIFEST_PATH,
        "created_at": created_at,
        "updated_at": created_at,
        "completed_at": None,
        "cancel_requested": False,
        "cancel_requested_at": None,
        "cancel_observed_at": None,
        "cancel_effective": False,
        "cancel_note": None,
        "threshold_reached": False,
        "threshold_reached_at": None,
        "threshold_note": None,
        "progress": _empty_job_progress(),
        "cancellation": _cancellation_metadata(
            {
                "cancel_requested": False,
                "cancel_requested_at": None,
                "cancel_observed_at": None,
                "cancel_effective": False,
                "cancel_note": None,
            }
        ),
        "parameters": {
            "language": language,
            "model_size": model_size,
            "device": device,
            "compute_type": compute_type,
            "variant_count": variant_count,
            "preset_ids": [preset.id for preset in selected_presets],
            "stop_after_completed_variants": stop_after_completed_variants,
        },
        "audio": _audio_file_info(audio_path),
        "variants": [
            {
                "variant_id": preset.id,
                "preset_id": preset.id,
                "status": VARIANT_STATUS_QUEUED,
                "started_at": None,
                "completed_at": None,
                "error": None,
                "progress": _empty_variant_progress(),
            }
            for preset in selected_presets
        ],
        "errors": [],
        "handoff": _canon_handoff(output_root, ready=False, reason="job_not_collected"),
    }
    _write_job(job_path, job)

    control = _JobControl(job_id, job_path)
    thread = threading.Thread(
        target=_run_transcription_job,
        kwargs={
            "control": control,
            "job": job,
            "presets": selected_presets,
            "language": language,
            "model_size": model_size,
            "device": device,
            "compute_type": compute_type,
            "transcribe": transcribe_audio,
        },
        name=f"scribe-stt-{job_id}",
        daemon=True,
    )
    control.thread = thread
    with _ACTIVE_JOBS_LOCK:
        _ACTIVE_JOBS[job_id] = control
    thread.start()

    current = _read_job(job_path)
    cancellation = _cancellation_metadata(current)
    return {
        "server": {"name": SERVER_NAME, "version": SERVER_VERSION},
        "tool": TOOL_SCRIBE_TRANSCRIBE_JOB_START,
        "success": True,
        "job_id": job_id,
        "job_path": str(job_path),
        **_durable_job_handle(job_path),
        "output_root": str(output_root),
        "status": current["status"],
        "status_tool": TOOL_SCRIBE_TRANSCRIBE_JOB_STATUS,
        "collect_tool": TOOL_SCRIBE_TRANSCRIBE_JOB_COLLECT,
        "cancel_tool": TOOL_SCRIBE_TRANSCRIBE_JOB_CANCEL,
        "manifest_path": MANIFEST_PATH,
        "cancel_requested": cancellation["cancel_requested"],
        "cancel_requested_at": cancellation["cancel_requested_at"],
        "cancel_observed_at": cancellation["cancel_observed_at"],
        "cancel_effective": cancellation["cancel_effective"],
        "cancel_note": cancellation["cancel_note"],
        "cancellation": cancellation,
        "stop_after_completed_variants": stop_after_completed_variants,
        "threshold_reached": bool(current.get("threshold_reached")),
        "threshold_reached_at": current.get("threshold_reached_at"),
        "threshold_note": current.get("threshold_note"),
        "progress": current.get("progress", _empty_job_progress()),
        "job": current,
    }


def scribe_transcribe_job_status(arguments: Mapping[str, Any]) -> dict[str, Any]:
    job_path = _resolve_job_path(arguments)
    job = _read_job(job_path)
    _sync_active_cancel_state(job_path, job)
    job = _read_job(job_path)
    return _job_response(TOOL_SCRIBE_TRANSCRIBE_JOB_STATUS, job_path, job)


def scribe_transcribe_job_collect(arguments: Mapping[str, Any]) -> dict[str, Any]:
    job_path = _resolve_job_path(arguments)
    minimum_completed_variants = _int_argument(
        arguments,
        "minimum_completed_variants",
        default=2,
        minimum=1,
        maximum=MAX_VARIANT_COUNT,
    )
    job = _read_job(job_path)
    _sync_active_cancel_state(job_path, job)
    job = _read_job(job_path)
    completed = _completed_variant_count(job)
    manifest_file = job_path.parent / MANIFEST_PATH
    readiness = _canon_readiness(
        job_path,
        job,
        minimum_completed_variants=minimum_completed_variants,
    )
    ready = readiness["ready"]
    response = _job_response(TOOL_SCRIBE_TRANSCRIBE_JOB_COLLECT, job_path, job)
    response.update(
        {
            "minimum_completed_variants": minimum_completed_variants,
            "completed_variant_count": completed,
            "ready_for_canon": ready,
            "manifest_path": MANIFEST_PATH if manifest_file.is_file() else None,
            "manifest_file": str(manifest_file) if manifest_file.is_file() else None,
            "canon_readiness": readiness,
            "handoff": _canon_handoff(
                job_path.parent,
                ready=ready,
                reason=readiness["reason"],
            ),
        }
    )
    return response


def scribe_transcribe_job_cancel(arguments: Mapping[str, Any]) -> dict[str, Any]:
    job_path = _resolve_job_path(arguments)
    job = _read_job(job_path)
    job_id = job.get("job_id")
    control = _active_job(str(job_id)) if isinstance(job_id, str) else None
    if control is not None:
        control.cancel_requested.set()

    _record_cancel_request(job_path, job)

    response = _job_response(TOOL_SCRIBE_TRANSCRIBE_JOB_CANCEL, job_path, _read_job(job_path))
    response["cancel_requested"] = True
    response["note"] = response["cancellation"]["cancel_note"]
    return response


def _transcribe_presets(
    tool_name: str,
    *,
    audio_path: Path,
    output_root: Path,
    presets: tuple[Any, ...],
    language: str | None,
    model_size: str | None,
    device: str,
    compute_type: str,
) -> dict[str, Any]:
    manifest_variants: list[dict[str, Any]] = []
    created_at = _utc_now()
    for preset in presets:
        try:
            result = transcribe_audio(
                audio_path,
                preset,
                language=language,
                model_size=model_size,
                device=device,
                compute_type=compute_type,
            )
        except MissingTranscriptionDependency as exc:
            raise JsonRpcError(
                TOOL_ERROR,
                "Transcription dependency missing",
                {
                    "dependency": exc.dependency,
                    "install_command": exc.install_command,
                    "install_guidance": exc.install_guidance,
                },
            ) from exc

        manifest_variants.append(
            write_transcription_variant(
                output_root,
                _variant_from_result(preset.id, result),
            )
        )
        manifest = write_transcription_manifest(
            output_root,
            audio_path,
            manifest_variants,
            created_at=created_at,
        )

    return {
        "server": {"name": SERVER_NAME, "version": SERVER_VERSION},
        "tool": tool_name,
        "success": True,
        "audio_path": str(audio_path),
        "output_root": str(output_root),
        "manifest_path": MANIFEST_PATH,
        "variant_count": len(manifest["variants"]),
        "variants": manifest["variants"],
        "manifest": manifest,
        "handoff": _canon_handoff(
            output_root,
            ready=len(manifest["variants"]) >= 2,
            reason="transcription_complete",
        ),
    }


def _run_transcription_job(
    *,
    control: _JobControl,
    job: dict[str, Any],
    presets: tuple[Any, ...],
    language: str | None,
    model_size: str | None,
    device: str,
    compute_type: str,
    transcribe: Callable[..., Any],
) -> None:
    job_path = control.job_path
    output_root = Path(str(job["output_root"]))
    audio_path = Path(str(job["audio_path"]))
    parameters = job.get("parameters")
    threshold = None
    if isinstance(parameters, Mapping):
        threshold_value = parameters.get("stop_after_completed_variants")
        if isinstance(threshold_value, int) and not isinstance(threshold_value, bool):
            threshold = threshold_value
    manifest_variants: list[dict[str, Any]] = []

    try:
        _update_job(job_path, status=JOB_STATUS_RUNNING)
        for index, preset in enumerate(presets):
            if control.cancel_requested.is_set() or _job_cancel_requested(job_path):
                _record_cancel_observed(job_path)
                _mark_remaining_variants_cancelled(job_path, index)
                _finish_job(job_path, JOB_STATUS_CANCELLED, cancel_effective=True)
                return

            _update_variant(job_path, index, status=VARIANT_STATUS_RUNNING, started_at=_utc_now())
            try:
                _record_variant_progress_started(job_path, index, preset.id)
                partial_segments: list[dict[str, Any]] = []
                _write_partial_variant_progress(
                    output_root,
                    preset,
                    language,
                    model_size,
                    partial_segments,
                    updated_at=_utc_now(),
                )
                result = transcribe(
                    audio_path,
                    preset,
                    language=language,
                    model_size=model_size,
                    device=device,
                    compute_type=compute_type,
                    progress_callback=lambda event, variant_index=index, current_preset=preset: (
                        _record_partial_segment_progress(
                            output_root,
                            job_path,
                            variant_index,
                            current_preset,
                            language,
                            model_size,
                            partial_segments,
                            event,
                        )
                    ),
                )
                manifest_variant = write_transcription_variant(
                    output_root,
                    _variant_from_result(preset.id, result),
                )
                _record_variant_progress_completed(
                    job_path,
                    index,
                    preset.id,
                    result,
                    manifest_variant,
                )
                manifest_variants.append(manifest_variant)
                manifest = write_transcription_manifest(
                    output_root,
                    audio_path,
                    manifest_variants,
                    created_at=str(job["created_at"]),
                )
                _update_variant(
                    job_path,
                    index,
                    status=VARIANT_STATUS_COMPLETED,
                    completed_at=_utc_now(),
                    error=None,
                    manifest=manifest_variant,
                )
                _update_job(
                    job_path,
                    manifest=manifest,
                    handoff=_canon_handoff(
                        output_root,
                        ready=len(manifest["variants"]) >= 2,
                        reason="partial_variants_available",
                    ),
                )
                if threshold is not None and len(manifest_variants) >= threshold:
                    _record_threshold_reached(job_path)
                    _mark_remaining_variants_skipped(job_path, index + 1)
                    _finish_job(job_path, JOB_STATUS_THRESHOLD_REACHED)
                    return
            except MissingTranscriptionDependency as exc:
                _update_variant(
                    job_path,
                    index,
                    status=VARIANT_STATUS_FAILED,
                    completed_at=_utc_now(),
                    error=exc.install_guidance,
                )
                _append_job_error(
                    job_path,
                    {
                        "variant_id": preset.id,
                        "error_type": "missing_dependency",
                        "dependency": exc.dependency,
                        "install_command": exc.install_command,
                        "message": exc.install_guidance,
                    },
                )
                _mark_remaining_variants_cancelled(job_path, index + 1)
                _finish_job(
                    job_path,
                    JOB_STATUS_PARTIAL_FAILED if manifest_variants else JOB_STATUS_FAILED,
                )
                return
            except Exception as exc:
                _update_variant(
                    job_path,
                    index,
                    status=VARIANT_STATUS_FAILED,
                    completed_at=_utc_now(),
                    error=str(exc),
                )
                _append_job_error(
                    job_path,
                    {
                        "variant_id": preset.id,
                        "error_type": type(exc).__name__,
                        "message": str(exc),
                    },
                )
                continue

        current = _read_job(job_path)
        if _completed_variant_count(current) == len(presets):
            _finish_job(job_path, JOB_STATUS_COMPLETED)
        elif _completed_variant_count(current) > 0:
            _finish_job(job_path, JOB_STATUS_PARTIAL_FAILED)
        else:
            _finish_job(job_path, JOB_STATUS_FAILED)
    finally:
        with _ACTIVE_JOBS_LOCK:
            _ACTIVE_JOBS.pop(control.job_id, None)


def _variant_from_result(variant_id: str, result: Any) -> TranscriptionVariant:
    return TranscriptionVariant(
        variant_id=variant_id,
        backend=str(_result_value(result, "backend")),
        preset_id=str(_result_value(result, "preset_id")),
        preset_params=_copy_mapping(_result_value(result, "params")),
        model=str(_result_value(result, "model")),
        language=_nullable_result_string(_result_value(result, "language")),
        segments=_segments_to_mappings(_result_value(result, "segments")),
    )


def _synchronous_transcription_guard(
    tool_name: str,
    arguments: Mapping[str, Any],
    *,
    audio_path: Path,
    output_root: Path,
) -> dict[str, Any] | None:
    force_sync = _bool_argument(arguments, "force_sync", default=False)
    max_duration = _int_argument(
        arguments,
        "max_sync_duration_seconds",
        default=DEFAULT_SYNC_MAX_DURATION_SECONDS,
        minimum=0,
        maximum=24 * 60 * 60,
    )
    max_bytes = _int_argument(
        arguments,
        "max_sync_audio_bytes",
        default=DEFAULT_SYNC_MAX_AUDIO_BYTES,
        minimum=0,
        maximum=10 * 1024 * 1024 * 1024,
    )
    audio = _audio_file_info(audio_path)
    exceeded: list[dict[str, Any]] = []

    duration = audio.get("duration_seconds")
    if max_duration > 0 and isinstance(duration, int | float) and duration > max_duration:
        exceeded.append(
            {
                "field": "duration_seconds",
                "value": duration,
                "limit": max_duration,
            }
        )

    size_bytes = audio.get("size_bytes")
    if max_bytes > 0 and isinstance(size_bytes, int) and size_bytes > max_bytes:
        exceeded.append(
            {
                "field": "size_bytes",
                "value": size_bytes,
                "limit": max_bytes,
            }
        )

    if force_sync or not exceeded:
        return None

    return {
        "server": {"name": SERVER_NAME, "version": SERVER_VERSION},
        "tool": tool_name,
        "success": False,
        "status": "sync_guard_blocked",
        "audio_path": str(audio_path),
        "output_root": str(output_root),
        "audio": audio,
        "sync_limits": {
            "max_sync_duration_seconds": max_duration,
            "max_sync_audio_bytes": max_bytes,
            "exceeded": exceeded,
        },
        "recommendation": {
            "tool": TOOL_SCRIBE_TRANSCRIBE_JOB_START,
            "reason": (
                "This audio may exceed client-side MCP tool-call wait limits. "
                "Use the background job API so completed variants are persisted incrementally."
            ),
            "output_contract": f"{JOB_PATH}, {MANIFEST_PATH}, variants/<variant_id>.md",
        },
        "handoff": _canon_handoff(output_root, ready=False, reason="no_completed_variants"),
    }


def _audio_file_info(audio_path: Path) -> dict[str, Any]:
    info: dict[str, Any] = {
        "size_bytes": None,
        "duration_seconds": None,
        "duration_source": None,
    }
    try:
        info["size_bytes"] = audio_path.stat().st_size
    except OSError as exc:
        info["size_error"] = str(exc)

    ffprobe = shutil.which("ffprobe")
    if ffprobe is None:
        info["duration_source"] = "ffprobe_missing"
        return info

    command = [
        ffprobe,
        "-v",
        "error",
        "-show_entries",
        "format=duration",
        "-of",
        "json",
        str(audio_path),
    ]
    try:
        completed = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
            timeout=FFPROBE_TIMEOUT_SECONDS,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        info["duration_source"] = "ffprobe_error"
        info["duration_error"] = str(exc)
        return info

    if completed.returncode != 0:
        info["duration_source"] = "ffprobe_error"
        info["duration_error"] = _truncate_output(completed.stderr)
        return info

    try:
        payload = json.loads(completed.stdout)
        duration_value = payload.get("format", {}).get("duration")
        if duration_value is not None:
            info["duration_seconds"] = float(duration_value)
            info["duration_source"] = "ffprobe"
        else:
            info["duration_source"] = "ffprobe_missing_duration"
    except (TypeError, ValueError, json.JSONDecodeError) as exc:
        info["duration_source"] = "ffprobe_parse_error"
        info["duration_error"] = str(exc)
    return info


def _new_job_id() -> str:
    return f"job-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}-{uuid.uuid4().hex[:8]}"


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _write_job(job_path: Path, job: Mapping[str, Any]) -> None:
    job_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = job_path.with_name(f"{job_path.name}.tmp")
    tmp_path.write_text(
        json.dumps(job, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    tmp_path.replace(job_path)


def _read_job(job_path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(job_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        _raise_invalid_argument("job_path", f"job file does not exist: {job_path}")
    except json.JSONDecodeError as exc:
        _raise_invalid_argument("job_path", f"job file is not valid JSON: {exc}")
    if not isinstance(payload, dict):
        _raise_invalid_argument("job_path", "job file must contain a JSON object")
    return payload


def _update_job(job_path: Path, **fields: Any) -> dict[str, Any]:
    job = _read_job(job_path)
    job.update(fields)
    if _has_cancellation_field(fields):
        _refresh_cancellation_metadata(job)
    job["updated_at"] = _utc_now()
    _write_job(job_path, job)
    return job


def _update_variant(job_path: Path, index: int, **fields: Any) -> None:
    job = _read_job(job_path)
    variants = job.get("variants")
    if not isinstance(variants, list) or index >= len(variants):
        return
    variant = variants[index]
    if isinstance(variant, dict):
        variant.update(fields)
    job["updated_at"] = _utc_now()
    _write_job(job_path, job)


def _append_job_error(job_path: Path, error: Mapping[str, Any]) -> None:
    job = _read_job(job_path)
    errors = job.setdefault("errors", [])
    if isinstance(errors, list):
        errors.append(dict(error))
    job["updated_at"] = _utc_now()
    _write_job(job_path, job)


def _empty_job_progress() -> dict[str, Any]:
    return {
        "current_variant_id": None,
        "current_preset_id": None,
        "segment_count": 0,
        "last_segment": None,
        "updated_at": None,
    }


def _empty_variant_progress() -> dict[str, Any]:
    return {
        "segment_count": 0,
        "last_segment": None,
        "updated_at": None,
    }


def _record_variant_progress_started(job_path: Path, index: int, preset_id: str) -> None:
    now = _utc_now()
    job = _read_job(job_path)
    progress = {
        "current_variant_id": preset_id,
        "current_preset_id": preset_id,
        "segment_count": 0,
        "last_segment": None,
        "updated_at": now,
    }
    _update_variant_progress(job, index, progress)
    job["progress"] = progress
    job["updated_at"] = now
    _write_job(job_path, job)


def _record_segment_progress(
    job_path: Path,
    index: int,
    preset_id: str,
    event: Mapping[str, Any],
) -> None:
    segment_count = event.get("segment_count")
    if not isinstance(segment_count, int) or isinstance(segment_count, bool):
        return
    now = _utc_now()
    progress = {
        "current_variant_id": preset_id,
        "current_preset_id": preset_id,
        "segment_count": segment_count,
        "last_segment": _compact_progress_segment(event.get("segment")),
        "updated_at": now,
    }
    job = _read_job(job_path)
    _update_variant_progress(job, index, progress)
    job["progress"] = progress
    job["updated_at"] = now
    _write_job(job_path, job)


def _record_partial_segment_progress(
    output_root: Path,
    job_path: Path,
    index: int,
    preset: Any,
    language: str | None,
    model_size: str | None,
    partial_segments: list[dict[str, Any]],
    event: Mapping[str, Any],
) -> None:
    segment = event.get("segment")
    if segment is not None:
        try:
            partial_segments.append(_segment_to_mapping(segment))
        except TypeError:
            pass
    _write_partial_variant_progress(
        output_root,
        preset,
        language,
        model_size,
        partial_segments,
        updated_at=_utc_now(),
    )
    _record_segment_progress(job_path, index, preset.id, event)


def _write_partial_variant_progress(
    output_root: Path,
    preset: Any,
    language: str | None,
    model_size: str | None,
    partial_segments: list[dict[str, Any]],
    *,
    updated_at: str,
) -> Mapping[str, Any]:
    preset_params = preset.to_transcribe_options()
    if language is not None:
        preset_params["language"] = language
    return write_partial_transcription_variant(
        output_root,
        TranscriptionVariant(
            variant_id=preset.id,
            backend="faster-whisper",
            preset_id=preset.id,
            preset_params=preset_params,
            model=model_size or preset.model_size,
            language=language,
            segments=tuple(partial_segments),
        ),
        updated_at=updated_at,
    )


def _record_variant_progress_completed(
    job_path: Path,
    index: int,
    preset_id: str,
    result: Any,
    manifest_variant: Mapping[str, Any],
) -> None:
    segment_count = manifest_variant.get("segment_count")
    if not isinstance(segment_count, int) or isinstance(segment_count, bool):
        return
    last_segment = _last_result_segment(result)
    now = _utc_now()
    progress = {
        "current_variant_id": preset_id,
        "current_preset_id": preset_id,
        "segment_count": segment_count,
        "last_segment": _compact_progress_segment(last_segment),
        "updated_at": now,
    }
    job = _read_job(job_path)
    _update_variant_progress(job, index, progress)
    job["progress"] = progress
    job["updated_at"] = now
    _write_job(job_path, job)


def _update_variant_progress(
    job: dict[str, Any],
    index: int,
    progress: Mapping[str, Any],
) -> None:
    variants = job.get("variants")
    if not isinstance(variants, list) or index >= len(variants):
        return
    variant = variants[index]
    if isinstance(variant, dict):
        variant["progress"] = {
            "segment_count": progress.get("segment_count", 0),
            "last_segment": progress.get("last_segment"),
            "updated_at": progress.get("updated_at"),
        }


def _last_result_segment(result: Any) -> Any:
    try:
        segments = _result_value(result, "segments")
    except TypeError:
        return None
    if isinstance(segments, (str, bytes)):
        return None
    if isinstance(segments, list | tuple):
        return segments[-1] if segments else None
    return None


def _compact_progress_segment(segment: Any) -> dict[str, Any] | None:
    if segment is None:
        return None
    try:
        mapped = _segment_to_mapping(segment)
    except TypeError:
        return None

    compact: dict[str, Any] = {}
    for key in ("start", "end"):
        if key in mapped:
            compact[key] = mapped[key]
    text = mapped.get("text")
    if isinstance(text, str):
        compact["text"] = text[:PROGRESS_TEXT_PREVIEW_CHARS]
        compact["text_truncated"] = len(text) > PROGRESS_TEXT_PREVIEW_CHARS
    return compact or None


def _mark_remaining_variants_cancelled(job_path: Path, start_index: int) -> None:
    job = _read_job(job_path)
    variants = job.get("variants")
    now = _utc_now()
    if isinstance(variants, list):
        for variant in variants[start_index:]:
            if isinstance(variant, dict) and variant.get("status") == VARIANT_STATUS_QUEUED:
                variant["status"] = VARIANT_STATUS_CANCELLED
                variant["completed_at"] = now
                variant["cancelled_at"] = now
                variant["cancel_note"] = CANCEL_OBSERVED_NOTE
    job["updated_at"] = _utc_now()
    _write_job(job_path, job)


def _mark_remaining_variants_skipped(job_path: Path, start_index: int) -> None:
    job = _read_job(job_path)
    variants = job.get("variants")
    now = _utc_now()
    if isinstance(variants, list):
        for variant in variants[start_index:]:
            if isinstance(variant, dict) and variant.get("status") == VARIANT_STATUS_QUEUED:
                variant["status"] = VARIANT_STATUS_SKIPPED
                variant["completed_at"] = now
                variant["skipped_at"] = now
                variant["skip_reason"] = "completed_variant_threshold"
                variant["skip_note"] = THRESHOLD_REACHED_NOTE
    job["updated_at"] = _utc_now()
    _write_job(job_path, job)


def _finish_job(job_path: Path, status: str, *, cancel_effective: bool | None = None) -> None:
    job = _read_job(job_path)
    now = _utc_now()
    job["status"] = status
    job["updated_at"] = now
    job["completed_at"] = now
    if cancel_effective is not None:
        job["cancel_effective"] = cancel_effective
        if cancel_effective and not job.get("cancel_note"):
            job["cancel_note"] = CANCEL_OBSERVED_NOTE
        _refresh_cancellation_metadata(job)
    job["handoff"] = _canon_handoff(
        job_path.parent,
        ready=_completed_variant_count(job) >= 2 and (job_path.parent / MANIFEST_PATH).is_file(),
        reason="job_finished",
    )
    _write_job(job_path, job)


def _record_threshold_reached(job_path: Path) -> dict[str, Any]:
    job = _read_job(job_path)
    now = _utc_now()
    job["threshold_reached"] = True
    if not job.get("threshold_reached_at"):
        job["threshold_reached_at"] = now
    job["threshold_note"] = THRESHOLD_REACHED_NOTE
    job["updated_at"] = now
    _write_job(job_path, job)
    return job


def _job_cancel_requested(job_path: Path) -> bool:
    try:
        return bool(_read_job(job_path).get("cancel_requested"))
    except JsonRpcError:
        return False


def _has_cancellation_field(fields: Mapping[str, Any]) -> bool:
    return any(
        key in fields
        for key in {
            "cancel_requested",
            "cancel_requested_at",
            "cancel_observed_at",
            "cancel_effective",
            "cancel_note",
        }
    )


def _cancellation_metadata(job: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "cancel_requested": bool(job.get("cancel_requested")),
        "cancel_requested_at": job.get("cancel_requested_at"),
        "cancel_observed_at": job.get("cancel_observed_at"),
        "cancel_effective": bool(job.get("cancel_effective")),
        "cancel_note": job.get("cancel_note"),
    }


def _refresh_cancellation_metadata(job: dict[str, Any]) -> None:
    job["cancellation"] = _cancellation_metadata(job)


def _record_cancel_request(job_path: Path, job: Mapping[str, Any] | None = None) -> dict[str, Any]:
    updated = dict(job) if job is not None else _read_job(job_path)
    terminal = updated.get("status") in TERMINAL_JOB_STATUSES
    now = _utc_now()
    updated["cancel_requested"] = True
    updated.setdefault("cancel_observed_at", None)
    updated.setdefault("cancel_effective", False)
    if not updated.get("cancel_requested_at"):
        updated["cancel_requested_at"] = now
    if not updated.get("cancel_note"):
        updated["cancel_note"] = (
            "Cancellation requested after job was already terminal."
            if terminal
            else CANCEL_REQUEST_NOTE
        )
    if not terminal:
        updated["status"] = JOB_STATUS_CANCEL_REQUESTED
    updated["updated_at"] = now
    _refresh_cancellation_metadata(updated)
    _write_job(job_path, updated)
    return updated


def _record_cancel_observed(job_path: Path) -> dict[str, Any]:
    job = _read_job(job_path)
    now = _utc_now()
    job["cancel_requested"] = True
    if not job.get("cancel_requested_at"):
        job["cancel_requested_at"] = now
    if not job.get("cancel_observed_at"):
        job["cancel_observed_at"] = now
    job["cancel_effective"] = True
    job["cancel_note"] = CANCEL_OBSERVED_NOTE
    job["updated_at"] = now
    _refresh_cancellation_metadata(job)
    _write_job(job_path, job)
    return job


def _completed_variant_count(job: Mapping[str, Any]) -> int:
    variants = job.get("variants")
    if not isinstance(variants, list):
        return 0
    return sum(
        1
        for variant in variants
        if isinstance(variant, Mapping) and variant.get("status") == VARIANT_STATUS_COMPLETED
    )


def _variant_status_counts(job: Mapping[str, Any]) -> dict[str, int]:
    variants = job.get("variants")
    counts: dict[str, int] = {}
    if not isinstance(variants, list):
        return counts
    for variant in variants:
        if not isinstance(variant, Mapping):
            continue
        status = variant.get("status")
        if isinstance(status, str):
            counts[status] = counts.get(status, 0) + 1
    return counts


def _variants_with_status(job: Mapping[str, Any], status: str) -> list[dict[str, Any]]:
    variants = job.get("variants")
    if not isinstance(variants, list):
        return []
    return [
        dict(variant)
        for variant in variants
        if isinstance(variant, Mapping) and variant.get("status") == status
    ]


def _threshold_skipped_variants(job: Mapping[str, Any]) -> list[dict[str, Any]]:
    return [
        variant
        for variant in _variants_with_status(job, VARIANT_STATUS_SKIPPED)
        if variant.get("skip_reason") == "completed_variant_threshold"
    ]


def _canon_readiness(
    job_path: Path,
    job: Mapping[str, Any],
    *,
    minimum_completed_variants: int,
) -> dict[str, Any]:
    completed = _completed_variant_count(job)
    manifest_file = job_path.parent / MANIFEST_PATH
    manifest_exists = manifest_file.is_file()
    ready = completed >= minimum_completed_variants and manifest_exists
    if ready:
        reason = "enough_completed_variants"
    elif completed < minimum_completed_variants:
        reason = "not_enough_completed_variants"
    else:
        reason = "manifest_missing"
    return {
        "ready": ready,
        "ready_for_canon": ready,
        "reason": reason,
        "completed_variant_count": completed,
        "minimum_completed_variants": minimum_completed_variants,
        "manifest_exists": manifest_exists,
        "manifest_path": MANIFEST_PATH if manifest_exists else None,
        "manifest_file": str(manifest_file) if manifest_exists else None,
        "threshold_reached": bool(job.get("threshold_reached")),
        "threshold_terminal": job.get("status") == JOB_STATUS_THRESHOLD_REACHED,
    }


def _resolve_job_path(arguments: Mapping[str, Any]) -> Path:
    job_id = _nullable_string_argument(arguments, "job_id")
    job_path_value = _nullable_string_argument(arguments, "job_path")
    if job_id:
        control = _active_job(job_id)
        if control is not None:
            return control.job_path
    if job_path_value:
        path = Path(job_path_value)
        if path.is_dir():
            path = path / JOB_PATH
        return path
    if job_id:
        _raise_invalid_argument(
            "job_id",
            "job_id is not active in this MCP process; pass job_path to inspect persisted state",
        )
    _raise_invalid_argument("job_path", "Provide job_id for active jobs or job_path for persisted jobs")


def _active_job(job_id: str) -> _JobControl | None:
    with _ACTIVE_JOBS_LOCK:
        return _ACTIVE_JOBS.get(job_id)


def _sync_active_cancel_state(job_path: Path, job: Mapping[str, Any]) -> None:
    job_id = job.get("job_id")
    if not isinstance(job_id, str):
        return
    control = _active_job(job_id)
    if control is not None and control.cancel_requested.is_set() and not job.get("cancel_requested"):
        _record_cancel_request(job_path, job)


def _job_response(tool: str, job_path: Path, job: Mapping[str, Any]) -> dict[str, Any]:
    cancellation = _cancellation_metadata(job)
    status_counts = _variant_status_counts(job)
    skipped_variants = _variants_with_status(job, VARIANT_STATUS_SKIPPED)
    threshold_skipped_variants = _threshold_skipped_variants(job)
    threshold_terminal = job.get("status") == JOB_STATUS_THRESHOLD_REACHED
    return {
        "server": {"name": SERVER_NAME, "version": SERVER_VERSION},
        "tool": tool,
        "success": True,
        "job_id": job.get("job_id"),
        "job_path": str(job_path),
        **_durable_job_handle(job_path),
        "output_root": str(job_path.parent),
        "status": job.get("status"),
        "completed_variant_count": _completed_variant_count(job),
        "variant_count": len(job.get("variants", [])) if isinstance(job.get("variants"), list) else 0,
        "variant_status_counts": status_counts,
        "progress": job.get("progress", _empty_job_progress()),
        "skipped_variant_count": status_counts.get(VARIANT_STATUS_SKIPPED, 0),
        "skipped_variants": skipped_variants,
        "threshold_skipped_variant_count": len(threshold_skipped_variants),
        "threshold_skipped_variants": threshold_skipped_variants,
        "manifest_path": MANIFEST_PATH if (job_path.parent / MANIFEST_PATH).is_file() else None,
        "cancel_requested": cancellation["cancel_requested"],
        "cancel_requested_at": cancellation["cancel_requested_at"],
        "cancel_observed_at": cancellation["cancel_observed_at"],
        "cancel_effective": cancellation["cancel_effective"],
        "cancel_note": cancellation["cancel_note"],
        "cancellation": cancellation,
        "stop_after_completed_variants": _job_threshold(job),
        "threshold_reached": bool(job.get("threshold_reached")),
        "threshold_reached_at": job.get("threshold_reached_at"),
        "threshold_note": job.get("threshold_note"),
        "threshold_stop": {
            "reached": bool(job.get("threshold_reached")),
            "terminal": threshold_terminal,
            "status": job.get("status"),
            "stop_after_completed_variants": _job_threshold(job),
            "skipped_variant_count": len(threshold_skipped_variants),
            "skipped_variants": threshold_skipped_variants,
            "note": job.get("threshold_note"),
        },
        "canon_readiness": _canon_readiness(job_path, job, minimum_completed_variants=2),
        "job": dict(job),
    }


def _job_threshold(job: Mapping[str, Any]) -> int | None:
    parameters = job.get("parameters")
    if not isinstance(parameters, Mapping):
        return None
    value = parameters.get("stop_after_completed_variants")
    if isinstance(value, int) and not isinstance(value, bool):
        return value
    return None


def _durable_job_handle(job_path: Path) -> dict[str, Any]:
    durable_job_path = str(job_path)
    return {
        "durable_job_path": durable_job_path,
        "durable_handle": {
            "type": "job_path",
            "job_path": durable_job_path,
            "restart_safe": True,
            "note": (
                "Use this job_path with status, collect, or cancel after the MCP "
                "server process restarts. job_id only resolves while this MCP "
                "process still has the job active."
            ),
        },
        "resume_arguments": {
            "status": {"job_path": durable_job_path},
            "collect": {"job_path": durable_job_path},
            "cancel": {"job_path": durable_job_path},
        },
    }


def _canon_handoff(output_root: Path, *, ready: bool, reason: str) -> dict[str, Any]:
    manifest_file = output_root / MANIFEST_PATH
    return {
        "ready_for_canon": ready,
        "reason": reason,
        "manifest_path": str(manifest_file) if manifest_file.is_file() else None,
        "instruction": (
            "If the user asked for canonical output, invoke scribe:canon on the "
            "manifest as soon as enough variants are available. Start with the "
            "evidence-first scan and clarification packet before canonical prose."
        ),
    }


def _faster_whisper_status() -> dict[str, Any]:
    spec = importlib.util.find_spec("faster_whisper")
    status: dict[str, Any] = {
        "package": "faster-whisper",
        "module": "faster_whisper",
        "available": spec is not None,
        "origin": getattr(spec, "origin", None) if spec is not None else None,
        "install": {
            "pip": "python3 -m pip install faster-whisper",
        },
    }
    if spec is None:
        status["action"] = "Install faster-whisper in the Python environment that starts this MCP server."
    else:
        status["action"] = "No action needed."
    return status


def _pip_install_command(*, upgrade: bool) -> list[str]:
    command = [sys.executable, "-m", "pip", "install"]
    if upgrade:
        command.append("--upgrade")
    command.append("faster-whisper")
    return command


def _run_setup_command(
    *,
    dependency: str,
    command: list[str],
    timeout_seconds: int,
) -> dict[str, Any]:
    try:
        completed = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
        )
    except subprocess.TimeoutExpired as exc:
        return {
            "dependency": dependency,
            "status": "failed",
            "command": _format_command(command),
            "returncode": None,
            "stdout": _truncate_output(exc.stdout),
            "stderr": _truncate_output(exc.stderr),
            "note": f"Setup command timed out after {timeout_seconds} seconds.",
        }
    except OSError as exc:
        return {
            "dependency": dependency,
            "status": "failed",
            "command": _format_command(command),
            "returncode": None,
            "stdout": "",
            "stderr": str(exc),
            "note": "Setup command could not be started.",
        }

    return {
        "dependency": dependency,
        "status": "installed" if completed.returncode == 0 else "failed",
        "command": _format_command(command),
        "returncode": completed.returncode,
        "stdout": _truncate_output(completed.stdout),
        "stderr": _truncate_output(completed.stderr),
        "note": (
            "Install command completed."
            if completed.returncode == 0
            else "Install command failed; inspect stderr."
        ),
    }


def _format_command(command: list[str]) -> str:
    return " ".join(shlex.quote(part) for part in command)


def _truncate_output(value: str | bytes | None) -> str:
    if value is None:
        return ""
    if isinstance(value, bytes):
        value = value.decode("utf-8", errors="replace")
    if len(value) <= MAX_CAPTURED_SETUP_OUTPUT:
        return value
    return value[:MAX_CAPTURED_SETUP_OUTPUT] + "\n...[truncated]"


def _ffmpeg_status() -> dict[str, Any]:
    path = shutil.which("ffmpeg")
    status = {
        "binary": "ffmpeg",
        "available": path is not None,
        "path": path,
        "install": {
            "macos": "brew install ffmpeg",
            "linux": "Install ffmpeg with your distribution package manager.",
            "windows": "Install ffmpeg and add its bin directory to PATH.",
        },
    }
    if path is None:
        status["action"] = "Install ffmpeg and ensure the ffmpeg executable is on PATH."
    else:
        status["action"] = "No action needed."
    return status


def _python_status() -> dict[str, Any]:
    return {
        "executable": sys.executable,
        "version": sys.version.split()[0],
        "version_info": {
            "major": sys.version_info.major,
            "minor": sys.version_info.minor,
            "micro": sys.version_info.micro,
        },
    }


def _install_guidance(
    faster_whisper: Mapping[str, Any],
    ffmpeg: Mapping[str, Any],
) -> list[dict[str, str]]:
    guidance: list[dict[str, str]] = []
    if not faster_whisper["available"]:
        guidance.append(
            {
                "dependency": "faster-whisper",
                "command": "python3 -m pip install faster-whisper",
                "note": "Run this in the same Python environment used to launch the Scribe MCP server.",
            }
        )
    if not ffmpeg["available"]:
        guidance.append(
            {
                "dependency": "ffmpeg",
                "command": "brew install ffmpeg",
                "note": "On non-macOS systems, use the OS package manager and make sure ffmpeg is on PATH.",
            }
        )
    if not guidance:
        guidance.append(
            {
                "dependency": "all",
                "command": "",
                "note": "All checked STT dependencies are available.",
            }
        )
    return guidance


def format_status(status: Mapping[str, Any]) -> str:
    dependencies = status["dependencies"]
    faster_whisper = dependencies["faster_whisper"]
    ffmpeg = dependencies["ffmpeg"]
    python = status["python"]

    lines = [
        f"Scribe MCP server {status['server']['version']}",
        f"stt_ready: {status['stt_ready']}",
        f"faster-whisper: available={faster_whisper['available']}",
        f"ffmpeg: available={ffmpeg['available']} path={ffmpeg.get('path')}",
        f"python: {python['version']} executable={python['executable']}",
    ]
    for item in status["install_guidance"]:
        note = item["note"]
        command = item["command"]
        if command:
            lines.append(f"install_guidance: {item['dependency']}: {command} ({note})")
        else:
            lines.append(f"install_guidance: {item['dependency']}: {note}")
    return "\n".join(lines)


def format_tool_result(name: Any, result: Mapping[str, Any]) -> str:
    if name == TOOL_SCRIBE_BUILD_REVIEW_STATE:
        return format_review_state_result(result)
    if name == TOOL_SCRIBE_STT_STATUS:
        return format_status(result)
    if name == TOOL_SCRIBE_SETUP_STT:
        return format_setup_result(result)
    if name in {TOOL_SCRIBE_TRANSCRIBE_FILE, TOOL_SCRIBE_TRANSCRIBE_VARIANTS}:
        return format_transcription_result(result)
    if name in {
        TOOL_SCRIBE_TRANSCRIBE_JOB_START,
        TOOL_SCRIBE_TRANSCRIBE_JOB_STATUS,
        TOOL_SCRIBE_TRANSCRIBE_JOB_COLLECT,
        TOOL_SCRIBE_TRANSCRIBE_JOB_CANCEL,
    }:
        return format_job_result(result)
    return str(result)


def format_review_state_result(result: Mapping[str, Any]) -> str:
    review_state = result["review_state"]
    packet = result["clarification_packet"]
    return "\n".join(
        [
            f"Scribe review state: state={review_state['state']}",
            f"requires_user_response: {result['requires_user_response']}",
            f"packet_id: {packet['packet_id']}",
            f"clarification_items: {len(packet['items'])}",
        ]
    )


def format_setup_result(result: Mapping[str, Any]) -> str:
    lines = [
        f"Scribe STT setup: success={result['success']} setup_ready={result['setup_ready']}",
        f"install_requested: {result['install_requested']}",
        f"python: {result['python']['version']} executable={result['python']['executable']}",
    ]
    for action in result["actions"]:
        command = action.get("command") or ""
        detail = f"{action['dependency']}: {action['status']}"
        if command:
            detail += f" command={command}"
        note = action.get("note")
        if note:
            detail += f" ({note})"
        lines.append(detail)
    return "\n".join(lines)


def format_transcription_result(result: Mapping[str, Any]) -> str:
    if result.get("status") == "sync_guard_blocked":
        recommendation = result.get("recommendation", {})
        return "\n".join(
            [
                "Scribe synchronous transcription skipped: sync_guard_blocked",
                f"audio_path: {result['audio_path']}",
                f"output_root: {result['output_root']}",
                f"recommended_tool: {recommendation.get('tool')}",
                f"reason: {recommendation.get('reason')}",
            ]
        )

    lines = [
        f"Scribe transcription complete: {result['variant_count']} variant(s)",
        f"output_root: {result['output_root']}",
        f"manifest: {result['manifest_path']}",
    ]
    for variant in result["variants"]:
        lines.append(
            "variant "
            f"{variant['variant_id']}: "
            f"text={variant['text_path']} "
            f"json={variant['json_path']} "
            f"segments={variant['segment_count']}"
        )
    return "\n".join(lines)


def format_job_result(result: Mapping[str, Any]) -> str:
    lines = [
        f"Scribe STT job: status={result.get('status')} job_id={result.get('job_id')}",
        f"job_path: {result.get('job_path')}",
        f"durable_job_path: {result.get('durable_job_path')}",
        f"output_root: {result.get('output_root')}",
        f"completed_variants: {result.get('completed_variant_count')}/{result.get('variant_count')}",
    ]
    if result.get("manifest_path"):
        lines.append(f"manifest: {result['manifest_path']}")
    progress = result.get("progress")
    if isinstance(progress, Mapping) and progress.get("current_variant_id"):
        lines.append(
            "progress: "
            f"variant={progress.get('current_variant_id')} "
            f"segments={progress.get('segment_count')} "
            f"updated_at={progress.get('updated_at')}"
        )
    if result.get("cancel_requested"):
        lines.append(
            "cancellation: "
            f"requested_at={result.get('cancel_requested_at')} "
            f"observed_at={result.get('cancel_observed_at')} "
            f"effective={result.get('cancel_effective')}"
        )
    if result.get("stop_after_completed_variants") is not None:
        lines.append(
            "threshold: "
            f"stop_after_completed_variants={result.get('stop_after_completed_variants')} "
            f"reached={result.get('threshold_reached')}"
        )
    if "ready_for_canon" in result:
        lines.append(f"ready_for_canon: {result['ready_for_canon']}")
    if result.get("note"):
        lines.append(str(result["note"]))
    return "\n".join(lines)


def _path_schema(description: str) -> dict[str, str]:
    return {"type": "string", "description": description}


def _string_schema(description: str) -> dict[str, str]:
    return {"type": "string", "description": description}


def _boolean_schema(description: str) -> dict[str, str]:
    return {"type": "boolean", "description": description}


def _nullable_string_schema(description: str) -> dict[str, Any]:
    return {"type": ["string", "null"], "description": description}


def _preset_ids_schema() -> dict[str, Any]:
    return {
        "type": "array",
        "items": {"type": "string", "enum": list(DEFAULT_PRESET_ORDER)},
        "minItems": MIN_VARIANT_COUNT,
        "maxItems": MAX_VARIANT_COUNT,
        "uniqueItems": True,
        "description": "Optional ordered Scribe preset ids. Length must match variant_count.",
    }


def _sync_duration_limit_schema() -> dict[str, Any]:
    return {
        "type": "integer",
        "minimum": 0,
        "maximum": 24 * 60 * 60,
        "description": (
            "Maximum audio duration for synchronous transcription. "
            f"Defaults to {DEFAULT_SYNC_MAX_DURATION_SECONDS}; 0 disables this limit."
        ),
    }


def _sync_audio_bytes_limit_schema() -> dict[str, Any]:
    return {
        "type": "integer",
        "minimum": 0,
        "maximum": 10 * 1024 * 1024 * 1024,
        "description": (
            "Maximum audio size for synchronous transcription. "
            f"Defaults to {DEFAULT_SYNC_MAX_AUDIO_BYTES}; 0 disables this limit."
        ),
    }


def _job_lookup_properties() -> dict[str, Any]:
    return {
        "job_id": _nullable_string_schema(
            "Active in-process job id returned by scribe_transcribe_job_start."
        ),
        "job_path": _nullable_string_schema(
            "Path to job.json or its containing job output directory."
        ),
    }


def _job_lookup_schema() -> dict[str, Any]:
    return {
        "type": "object",
        "properties": _job_lookup_properties(),
        "required": [],
        "additionalProperties": False,
    }


def _required_path_argument(
    arguments: Mapping[str, Any],
    field: str,
    *,
    must_be_file: bool = False,
) -> Path:
    value = arguments.get(field, _MISSING)
    if value is _MISSING:
        _raise_invalid_argument(field, f"{field} is required")
    if not isinstance(value, (str, os.PathLike)):
        _raise_invalid_argument(field, f"{field} must be a string path")
    if isinstance(value, str) and not value:
        _raise_invalid_argument(field, f"{field} must not be empty")

    try:
        path = Path(value)
    except (TypeError, ValueError) as exc:
        _raise_invalid_argument(field, f"{field} must be a valid path: {exc}")

    if must_be_file:
        try:
            is_file = path.is_file()
        except OSError as exc:
            _raise_invalid_argument(field, f"{field} cannot be accessed: {exc}")
        if not is_file:
            _raise_invalid_argument(field, f"{field} must point to an existing file")

    return path


def _nullable_string_argument(arguments: Mapping[str, Any], field: str) -> str | None:
    value = arguments.get(field, _MISSING)
    if value is _MISSING or value is None:
        return None
    if not isinstance(value, str):
        _raise_invalid_argument(field, f"{field} must be a string or null")
    return value


def _string_argument(
    arguments: Mapping[str, Any],
    field: str,
    *,
    default: str,
) -> str:
    value = arguments.get(field, _MISSING)
    if value is _MISSING:
        return default
    if not isinstance(value, str):
        _raise_invalid_argument(field, f"{field} must be a string")
    return value


def _bool_argument(
    arguments: Mapping[str, Any],
    field: str,
    *,
    default: bool,
) -> bool:
    value = arguments.get(field, _MISSING)
    if value is _MISSING:
        return default
    if not isinstance(value, bool):
        _raise_invalid_argument(field, f"{field} must be a boolean")
    return value


def _int_argument(
    arguments: Mapping[str, Any],
    field: str,
    *,
    default: int,
    minimum: int,
    maximum: int,
) -> int:
    value = arguments.get(field, _MISSING)
    if value is _MISSING:
        return default
    if isinstance(value, bool) or not isinstance(value, int):
        _raise_invalid_argument(field, f"{field} must be an integer")
    if value < minimum or value > maximum:
        _raise_invalid_argument(field, f"{field} must be between {minimum} and {maximum}")
    return value


def _preset_argument(arguments: Mapping[str, Any]) -> Any:
    value = arguments.get("preset_id", DEFAULT_PRESET_ID)
    if value is None:
        value = DEFAULT_PRESET_ID
    if not isinstance(value, str):
        _raise_invalid_argument("preset_id", "preset_id must be a string")
    try:
        return get_preset(value)
    except PresetValidationError as exc:
        _raise_invalid_argument("preset_id", str(exc))


def _variant_count_argument(arguments: Mapping[str, Any]) -> int:
    value = arguments.get("variant_count", _MISSING)
    if value is _MISSING:
        _raise_invalid_argument("variant_count", "variant_count is required")
    if isinstance(value, bool) or not isinstance(value, int):
        _raise_invalid_argument(
            "variant_count",
            f"variant_count must be an integer from {MIN_VARIANT_COUNT} through {MAX_VARIANT_COUNT}",
        )
    if value < MIN_VARIANT_COUNT or value > MAX_VARIANT_COUNT:
        _raise_invalid_argument(
            "variant_count",
            f"variant_count must be between {MIN_VARIANT_COUNT} and {MAX_VARIANT_COUNT}",
        )
    return value


def _completed_variant_threshold_argument(
    arguments: Mapping[str, Any],
    *,
    variant_count: int,
) -> int | None:
    value = arguments.get("stop_after_completed_variants", _MISSING)
    if value is _MISSING or value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, int):
        _raise_invalid_argument(
            "stop_after_completed_variants",
            "stop_after_completed_variants must be an integer",
        )
    if value < 1 or value > variant_count:
        _raise_invalid_argument(
            "stop_after_completed_variants",
            f"stop_after_completed_variants must be between 1 and variant_count ({variant_count})",
        )
    return value


def _requested_preset_ids_argument(arguments: Mapping[str, Any]) -> tuple[str, ...] | None:
    has_preset_ids = "preset_ids" in arguments and arguments["preset_ids"] is not None
    has_requested_preset_ids = (
        "requested_preset_ids" in arguments
        and arguments["requested_preset_ids"] is not None
    )
    if has_preset_ids and has_requested_preset_ids:
        _raise_invalid_argument(
            "preset_ids",
            "Use either preset_ids or requested_preset_ids, not both",
        )

    value = _MISSING
    field = "preset_ids"
    if has_preset_ids:
        value = arguments["preset_ids"]
    elif has_requested_preset_ids:
        value = arguments["requested_preset_ids"]
        field = "requested_preset_ids"

    if value is _MISSING:
        return None
    if not isinstance(value, (list, tuple)):
        _raise_invalid_argument(field, f"{field} must be a list of preset id strings")
    for item in value:
        if not isinstance(item, str):
            _raise_invalid_argument(field, f"{field} must contain only strings")
    return tuple(value)


def _review_items_argument(arguments: Mapping[str, Any]) -> tuple[Mapping[str, Any], ...]:
    value = arguments.get("high_impact_items", ())
    if value is None:
        return ()
    if not isinstance(value, (list, tuple)):
        _raise_invalid_argument("high_impact_items", "high_impact_items must be a list")
    for item in value:
        if not isinstance(item, Mapping):
            _raise_invalid_argument(
                "high_impact_items",
                "high_impact_items must contain only objects",
            )
    return tuple(value)


def _result_value(result: Any, key: str) -> Any:
    if isinstance(result, Mapping):
        if key in result:
            return result[key]
    else:
        value = getattr(result, key, _MISSING)
        if value is not _MISSING:
            return value
    raise TypeError(f"Transcription result is missing required field: {key}")


def _copy_mapping(value: Any) -> dict[str, Any]:
    if not isinstance(value, Mapping):
        raise TypeError("Transcription result params must be a mapping")
    return dict(value)


def _nullable_result_string(value: Any) -> str | None:
    if value is None:
        return None
    return str(value)


def _segments_to_mappings(segments: Any) -> tuple[dict[str, Any], ...]:
    if isinstance(segments, (str, bytes)):
        raise TypeError("Transcription result segments must be an iterable of segment objects")
    return tuple(_segment_to_mapping(segment) for segment in segments)


def _segment_to_mapping(segment: Any) -> dict[str, Any]:
    if isinstance(segment, Mapping):
        return dict(segment)

    to_dict = getattr(segment, "to_dict", None)
    if callable(to_dict):
        value = to_dict()
        if not isinstance(value, Mapping):
            raise TypeError("segment.to_dict() must return a mapping")
        return dict(value)

    mapped = {}
    for key in ("start", "end", "text", "language"):
        value = getattr(segment, key, _MISSING)
        if value is not _MISSING:
            mapped[key] = value
    if "text" not in mapped:
        raise TypeError("Transcription segment is missing required field: text")
    return mapped


def _raise_invalid_argument(field: str, error: str) -> None:
    raise JsonRpcError(
        TOOL_ERROR,
        "Invalid tool arguments",
        {"field": field, "error": error},
    )


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
