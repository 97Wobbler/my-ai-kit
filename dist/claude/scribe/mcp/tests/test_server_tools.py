from __future__ import annotations

import json
import sys
import tempfile
import threading
import time
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


MCP_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MCP_DIR))

import server  # noqa: E402


class ScribeServerToolsTest(unittest.TestCase):
    def request(self, method, params=None, request_id=1):
        protocol = server.build_protocol()
        payload = {"jsonrpc": "2.0", "id": request_id, "method": method}
        if params is not None:
            payload["params"] = params
        response = protocol.handle_line(json.dumps(payload))
        self.assertIsNotNone(response)
        return json.loads(response)

    def test_tools_list_exposes_all_scribe_tools(self) -> None:
        response = self.request("tools/list")

        tools = response["result"]["tools"]
        self.assertEqual(
            [tool["name"] for tool in tools],
            [
                server.TOOL_SCRIBE_BUILD_REVIEW_STATE,
                server.TOOL_SCRIBE_STT_STATUS,
                server.TOOL_SCRIBE_SETUP_STT,
                server.TOOL_SCRIBE_TRANSCRIBE_FILE,
                server.TOOL_SCRIBE_TRANSCRIBE_VARIANTS,
                server.TOOL_SCRIBE_TRANSCRIBE_JOB_START,
                server.TOOL_SCRIBE_TRANSCRIBE_JOB_STATUS,
                server.TOOL_SCRIBE_TRANSCRIBE_JOB_COLLECT,
                server.TOOL_SCRIBE_TRANSCRIBE_JOB_CANCEL,
            ],
        )

    def test_build_review_state_returns_machine_readable_gate(self) -> None:
        response = self.request(
            "tools/call",
            {
                "name": server.TOOL_SCRIBE_BUILD_REVIEW_STATE,
                "arguments": {
                    "transcript_path": "transcripts/run-1/variants/balanced.md",
                    "review_path": "transcripts/run-1/transcript-review.md",
                    "manifest_path": "transcripts/run-1/manifest.json",
                    "max_items": 1,
                    "packet_id": "review-custom",
                    "high_impact_items": [
                        {
                            "id": "term-001",
                            "kind": "term_confirmation",
                            "impact": "high",
                            "question": "Confirm this recurring product term.",
                            "candidate": "Scribe Canon",
                            "alternatives": ["scribe cannon"],
                            "evidence": [
                                {
                                    "source": "transcript_span",
                                    "span_ref": "balanced.md#approx-00:01:00",
                                    "excerpt": "Scribe Canon",
                                }
                            ],
                        },
                        {
                            "id": "term-002",
                            "impact": "medium",
                            "candidate": "deferred",
                        },
                    ],
                },
            },
        )

        self.assertNotIn("error", response)
        structured = response["result"]["structuredContent"]
        self.assertEqual(structured["tool"], server.TOOL_SCRIBE_BUILD_REVIEW_STATE)
        self.assertTrue(structured["requires_user_response"])

        packet = structured["clarification_packet"]
        self.assertEqual(packet["packet_id"], "review-custom")
        self.assertEqual(packet["max_items"], 1)
        self.assertEqual(len(packet["items"]), 1)
        self.assertEqual(packet["items"][0]["id"], "term-001")

        review_state = structured["review_state"]
        self.assertEqual(review_state["state"], "review_needed")
        self.assertTrue(review_state["requires_user_response"])
        self.assertEqual(structured["clarification_packet"], review_state["clarification_packet"])
        self.assertEqual(
            review_state["transcript_path"],
            "transcripts/run-1/variants/balanced.md",
        )
        self.assertEqual(
            review_state["review_path"],
            "transcripts/run-1/transcript-review.md",
        )
        self.assertEqual(
            review_state["manifest_path"],
            "transcripts/run-1/manifest.json",
        )

    def test_build_review_state_returns_ready_without_high_impact_items(self) -> None:
        response = self.request(
            "tools/call",
            {
                "name": server.TOOL_SCRIBE_BUILD_REVIEW_STATE,
                "arguments": {
                    "high_impact_items": [
                        {
                            "impact": "medium",
                            "candidate": "non-blocking wording",
                        }
                    ]
                },
            },
        )

        self.assertNotIn("error", response)
        structured = response["result"]["structuredContent"]
        self.assertFalse(structured["requires_user_response"])
        self.assertEqual(structured["clarification_packet"]["items"], [])
        self.assertEqual(structured["review_state"]["state"], "ready")

    def test_invalid_audio_paths_return_tool_errors(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            missing_audio = str(Path(tmp) / "missing.wav")
            output_root = str(Path(tmp) / "out")

            cases = (
                (
                    server.TOOL_SCRIBE_TRANSCRIBE_FILE,
                    {
                        "audio_path": missing_audio,
                        "output_root": output_root,
                    },
                ),
                (
                    server.TOOL_SCRIBE_TRANSCRIBE_VARIANTS,
                    {
                        "audio_path": missing_audio,
                        "output_root": output_root,
                        "variant_count": 1,
                    },
                ),
            )

            for tool_name, arguments in cases:
                with self.subTest(tool_name=tool_name):
                    response = self.request(
                        "tools/call",
                        {"name": tool_name, "arguments": arguments},
                    )

                    self.assertEqual(response["error"]["code"], server.TOOL_ERROR)
                    self.assertEqual(response["error"]["message"], "Invalid tool arguments")
                    self.assertEqual(response["error"]["data"]["field"], "audio_path")
                    self.assertIn("existing file", response["error"]["data"]["error"])

    def test_transcribe_variants_writes_manifest_and_relative_variant_paths(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            audio_path = root / "sample.wav"
            output_root = root / "outputs"
            audio_path.write_bytes(b"not real audio")
            calls = []

            def fake_transcribe_audio(
                audio_path_arg,
                preset,
                language=None,
                model_size=None,
                device="auto",
                compute_type="default",
                progress_callback=None,
            ):
                calls.append(
                    {
                        "audio_path": audio_path_arg,
                        "preset_id": preset.id,
                        "language": language,
                        "model_size": model_size,
                        "device": device,
                        "compute_type": compute_type,
                    }
                )
                return SimpleNamespace(
                    backend="fake-stt",
                    model=model_size or preset.model_size,
                    preset_id=preset.id,
                    language=language,
                    params={
                        "beam_size": preset.beam_size,
                        "device": device,
                        "compute_type": compute_type,
                    },
                    segments=(
                        SimpleNamespace(
                            start=0.0,
                            end=1.25,
                            text=f"{preset.id} segment one",
                        ),
                        {
                            "start": 1.25,
                            "end": 2.5,
                            "text": f"{preset.id} segment two",
                        },
                    ),
                )

            with patch("server.transcribe_audio", side_effect=fake_transcribe_audio):
                response = self.request(
                    "tools/call",
                    {
                        "name": server.TOOL_SCRIBE_TRANSCRIBE_VARIANTS,
                        "arguments": {
                            "audio_path": str(audio_path),
                            "output_root": str(output_root),
                            "variant_count": 2,
                            "preset_ids": ["fast", "strict"],
                            "language": "en",
                            "model_size": "tiny",
                            "device": "cpu",
                            "compute_type": "int8",
                        },
                    },
                )

            self.assertNotIn("error", response)
            self.assertEqual([call["preset_id"] for call in calls], ["fast", "strict"])
            self.assertEqual(calls[0]["audio_path"], audio_path)
            self.assertEqual(calls[0]["language"], "en")
            self.assertEqual(calls[0]["model_size"], "tiny")
            self.assertEqual(calls[0]["device"], "cpu")
            self.assertEqual(calls[0]["compute_type"], "int8")

            structured = response["result"]["structuredContent"]
            self.assertEqual(structured["tool"], server.TOOL_SCRIBE_TRANSCRIBE_VARIANTS)
            self.assertEqual(structured["output_root"], str(output_root))
            self.assertEqual(structured["manifest_path"], "manifest.json")
            self.assertFalse(Path(structured["manifest_path"]).is_absolute())
            self.assertEqual(structured["variant_count"], 2)
            self.assertEqual(
                [variant["preset_id"] for variant in structured["variants"]],
                ["fast", "strict"],
            )

            manifest_path = output_root / structured["manifest_path"]
            self.assertTrue(manifest_path.exists())
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            self.assertEqual(manifest, structured["manifest"])

            for variant in structured["variants"]:
                self.assertFalse(Path(variant["text_path"]).is_absolute())
                self.assertFalse(Path(variant["json_path"]).is_absolute())
                self.assertTrue((output_root / variant["text_path"]).exists())
                self.assertTrue((output_root / variant["json_path"]).exists())
                self.assertEqual(variant["segment_count"], 2)

            fast_json = json.loads(
                (output_root / "variants" / "fast.json").read_text(encoding="utf-8")
            )
            self.assertEqual(fast_json["model"], "tiny")
            self.assertEqual(fast_json["language"], "en")
            self.assertEqual(fast_json["segments"][0]["text"], "fast segment one")
            self.assertEqual(fast_json["segments"][0]["language"], "en")

    def test_sync_guard_recommends_background_job_for_large_audio(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            audio_path = root / "sample.wav"
            output_root = root / "outputs"
            audio_path.write_bytes(b"not real audio")

            response = self.request(
                "tools/call",
                {
                    "name": server.TOOL_SCRIBE_TRANSCRIBE_VARIANTS,
                    "arguments": {
                        "audio_path": str(audio_path),
                        "output_root": str(output_root),
                        "variant_count": 2,
                        "max_sync_audio_bytes": 1,
                    },
                },
            )

            self.assertNotIn("error", response)
            structured = response["result"]["structuredContent"]
            self.assertFalse(structured["success"])
            self.assertEqual(structured["status"], "sync_guard_blocked")
            self.assertEqual(
                structured["recommendation"]["tool"],
                server.TOOL_SCRIBE_TRANSCRIBE_JOB_START,
            )
            self.assertFalse((output_root / "manifest.json").exists())

    def test_background_job_persists_variants_and_collects_for_canon(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            audio_path = root / "sample.wav"
            output_root = root / "job-output"
            audio_path.write_bytes(b"not real audio")

            def fake_transcribe_audio(
                audio_path_arg,
                preset,
                language=None,
                model_size=None,
                device="auto",
                compute_type="default",
                progress_callback=None,
            ):
                return SimpleNamespace(
                    backend="fake-stt",
                    model=model_size or preset.model_size,
                    preset_id=preset.id,
                    language=language,
                    params={"beam_size": preset.beam_size},
                    segments=(
                        SimpleNamespace(
                            start=0.0,
                            end=1.0,
                            text=f"{preset.id} segment",
                        ),
                    ),
                )

            with patch("server.transcribe_audio", side_effect=fake_transcribe_audio):
                start_response = self.request(
                    "tools/call",
                    {
                        "name": server.TOOL_SCRIBE_TRANSCRIBE_JOB_START,
                        "arguments": {
                            "audio_path": str(audio_path),
                            "output_root": str(output_root),
                            "variant_count": 2,
                            "preset_ids": ["fast", "strict"],
                            "language": "ko",
                            "model_size": "tiny",
                        },
                    },
                )

            self.assertNotIn("error", start_response)
            structured_start = start_response["result"]["structuredContent"]
            job_path = Path(structured_start["job_path"])
            self.assert_durable_handle(structured_start, job_path)

            job = self.wait_for_terminal_job(job_path)
            self.assertEqual(job["status"], server.JOB_STATUS_COMPLETED)
            self.assertEqual(
                [variant["status"] for variant in job["variants"]],
                [server.VARIANT_STATUS_COMPLETED, server.VARIANT_STATUS_COMPLETED],
            )

            manifest_path = output_root / "manifest.json"
            self.assertTrue(manifest_path.exists())
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            self.assertEqual(
                [variant["variant_id"] for variant in manifest["variants"]],
                ["fast", "strict"],
            )
            self.assertTrue((output_root / "variants" / "fast.md").exists())
            self.assertTrue((output_root / "variants" / "strict.json").exists())

            status_response = self.request(
                "tools/call",
                {
                    "name": server.TOOL_SCRIBE_TRANSCRIBE_JOB_STATUS,
                    "arguments": {"job_path": str(job_path)},
                },
            )
            structured_status = status_response["result"]["structuredContent"]
            self.assertEqual(structured_status["status"], server.JOB_STATUS_COMPLETED)
            self.assert_durable_handle(structured_status, job_path)

            collect_response = self.request(
                "tools/call",
                {
                    "name": server.TOOL_SCRIBE_TRANSCRIBE_JOB_COLLECT,
                    "arguments": {"job_path": str(job_path)},
                },
            )

            structured = collect_response["result"]["structuredContent"]
            self.assertTrue(structured["ready_for_canon"])
            self.assertEqual(structured["completed_variant_count"], 2)
            self.assertEqual(structured["manifest_file"], str(manifest_path))
            self.assert_durable_handle(structured, job_path)

    def test_background_job_stops_after_completed_variant_threshold(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            audio_path = root / "sample.wav"
            output_root = root / "job-output"
            audio_path.write_bytes(b"not real audio")
            calls = []

            def fake_transcribe_audio(
                audio_path_arg,
                preset,
                language=None,
                model_size=None,
                device="auto",
                compute_type="default",
                progress_callback=None,
            ):
                calls.append(preset.id)
                return SimpleNamespace(
                    backend="fake-stt",
                    model=model_size or preset.model_size,
                    preset_id=preset.id,
                    language=language,
                    params={"beam_size": preset.beam_size},
                    segments=(
                        SimpleNamespace(
                            start=0.0,
                            end=1.0,
                            text=f"{preset.id} segment",
                        ),
                    ),
                )

            with patch("server.transcribe_audio", side_effect=fake_transcribe_audio):
                start_response = self.request(
                    "tools/call",
                    {
                        "name": server.TOOL_SCRIBE_TRANSCRIBE_JOB_START,
                        "arguments": {
                            "audio_path": str(audio_path),
                            "output_root": str(output_root),
                            "variant_count": 3,
                            "preset_ids": ["fast", "strict", "balanced"],
                            "stop_after_completed_variants": 2,
                        },
                    },
                )
                self.assertNotIn("error", start_response)
                structured_start = start_response["result"]["structuredContent"]
                self.assertEqual(structured_start["stop_after_completed_variants"], 2)
                job_path = Path(structured_start["job_path"])
                self.assert_durable_handle(structured_start, job_path)
                job = self.wait_for_terminal_job(job_path)

            self.assertEqual(calls, ["fast", "strict"])
            self.assertEqual(job["status"], server.JOB_STATUS_THRESHOLD_REACHED)
            self.assertTrue(job["threshold_reached"])
            self.assertIsNotNone(job["threshold_reached_at"])
            self.assertEqual(job["threshold_note"], server.THRESHOLD_REACHED_NOTE)
            self.assertEqual(job["parameters"]["stop_after_completed_variants"], 2)
            self.assertEqual(
                [variant["status"] for variant in job["variants"]],
                [
                    server.VARIANT_STATUS_COMPLETED,
                    server.VARIANT_STATUS_COMPLETED,
                    server.VARIANT_STATUS_SKIPPED,
                ],
            )
            self.assertEqual(job["variants"][2]["skip_reason"], "completed_variant_threshold")

            manifest_path = output_root / "manifest.json"
            self.assertTrue(manifest_path.exists())
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            self.assertEqual(
                [variant["variant_id"] for variant in manifest["variants"]],
                ["fast", "strict"],
            )
            self.assertTrue((output_root / "variants" / "fast.md").exists())
            self.assertTrue((output_root / "variants" / "strict.json").exists())
            self.assertFalse((output_root / "variants" / "balanced.md").exists())

            status_response = self.request(
                "tools/call",
                {
                    "name": server.TOOL_SCRIBE_TRANSCRIBE_JOB_STATUS,
                    "arguments": {"job_path": str(job_path)},
                },
            )
            structured_status = status_response["result"]["structuredContent"]
            self.assertEqual(structured_status["status"], server.JOB_STATUS_THRESHOLD_REACHED)
            self.assertEqual(
                structured_status["variant_status_counts"],
                {
                    server.VARIANT_STATUS_COMPLETED: 2,
                    server.VARIANT_STATUS_SKIPPED: 1,
                },
            )
            self.assertEqual(structured_status["skipped_variant_count"], 1)
            self.assertEqual(structured_status["threshold_skipped_variant_count"], 1)
            self.assertEqual(
                [variant["preset_id"] for variant in structured_status["skipped_variants"]],
                ["balanced"],
            )
            self.assertEqual(
                [variant["skip_reason"] for variant in structured_status["threshold_skipped_variants"]],
                ["completed_variant_threshold"],
            )
            self.assertTrue(structured_status["threshold_stop"]["terminal"])
            self.assertEqual(
                structured_status["threshold_stop"]["status"],
                server.JOB_STATUS_THRESHOLD_REACHED,
            )
            self.assertEqual(structured_status["threshold_stop"]["skipped_variant_count"], 1)
            self.assertTrue(structured_status["canon_readiness"]["ready"])
            self.assertTrue(structured_status["canon_readiness"]["manifest_exists"])
            self.assertEqual(
                structured_status["canon_readiness"]["reason"],
                "enough_completed_variants",
            )
            self.assertEqual(
                structured_status["canon_readiness"]["manifest_file"],
                str(manifest_path),
            )
            self.assertTrue(structured_status["canon_readiness"]["threshold_terminal"])
            self.assert_durable_handle(structured_status, job_path)

            collect_response = self.request(
                "tools/call",
                {
                    "name": server.TOOL_SCRIBE_TRANSCRIBE_JOB_COLLECT,
                    "arguments": {"job_path": str(job_path)},
                },
            )
            structured_collect = collect_response["result"]["structuredContent"]
            self.assertTrue(structured_collect["ready_for_canon"])
            self.assertEqual(structured_collect["completed_variant_count"], 2)
            self.assertEqual(structured_collect["status"], server.JOB_STATUS_THRESHOLD_REACHED)
            self.assertEqual(structured_collect["stop_after_completed_variants"], 2)
            self.assertTrue(structured_collect["threshold_reached"])
            self.assertEqual(structured_collect["threshold_skipped_variant_count"], 1)
            self.assertTrue(structured_collect["threshold_stop"]["terminal"])
            self.assertEqual(
                structured_collect["canon_readiness"],
                {
                    "ready": True,
                    "ready_for_canon": True,
                    "reason": "enough_completed_variants",
                    "completed_variant_count": 2,
                    "minimum_completed_variants": 2,
                    "manifest_exists": True,
                    "manifest_path": "manifest.json",
                    "manifest_file": str(manifest_path),
                    "threshold_reached": True,
                    "threshold_terminal": True,
                },
            )
            self.assertEqual(
                structured_collect["handoff"]["reason"],
                "enough_completed_variants",
            )
            self.assert_durable_handle(structured_collect, job_path)

    def test_background_job_rejects_invalid_completed_variant_threshold(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            audio_path = root / "sample.wav"
            output_root = root / "job-output"
            audio_path.write_bytes(b"not real audio")

            cases = (0, 3, "1", True)
            for threshold in cases:
                with self.subTest(threshold=threshold):
                    response = self.request(
                        "tools/call",
                        {
                            "name": server.TOOL_SCRIBE_TRANSCRIBE_JOB_START,
                            "arguments": {
                                "audio_path": str(audio_path),
                                "output_root": str(output_root),
                                "variant_count": 2,
                                "preset_ids": ["fast", "strict"],
                                "stop_after_completed_variants": threshold,
                            },
                        },
                    )

                    self.assertEqual(response["error"]["code"], server.TOOL_ERROR)
                    self.assertEqual(response["error"]["message"], "Invalid tool arguments")
                    self.assertEqual(
                        response["error"]["data"]["field"],
                        "stop_after_completed_variants",
                    )

    def test_background_job_exposes_segment_progress_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            audio_path = root / "sample.wav"
            output_root = root / "job-output"
            audio_path.write_bytes(b"not real audio")
            first_segment_recorded = threading.Event()
            release_transcription = threading.Event()
            self.addCleanup(release_transcription.set)

            def fake_transcribe_audio(
                audio_path_arg,
                preset,
                language=None,
                model_size=None,
                device="auto",
                compute_type="default",
                progress_callback=None,
            ):
                self.assertIsNotNone(progress_callback)
                progress_callback(
                    {
                        "segment_count": 1,
                        "segment": {
                            "start": 0.0,
                            "end": 1.5,
                            "text": "x" * (server.PROGRESS_TEXT_PREVIEW_CHARS + 25),
                        },
                    }
                )
                first_segment_recorded.set()
                self.assertTrue(release_transcription.wait(timeout=2.0))
                progress_callback(
                    {
                        "segment_count": 2,
                        "segment": {
                            "start": 1.5,
                            "end": 2.0,
                            "text": "second segment",
                        },
                    }
                )
                return SimpleNamespace(
                    backend="fake-stt",
                    model=model_size or preset.model_size,
                    preset_id=preset.id,
                    language=language,
                    params={"beam_size": preset.beam_size},
                    segments=(
                        SimpleNamespace(start=0.0, end=1.5, text="first segment"),
                        SimpleNamespace(start=1.5, end=2.0, text="second segment"),
                    ),
                )

            with patch("server.transcribe_audio", side_effect=fake_transcribe_audio):
                start_response = self.request(
                    "tools/call",
                    {
                        "name": server.TOOL_SCRIBE_TRANSCRIBE_JOB_START,
                        "arguments": {
                            "audio_path": str(audio_path),
                            "output_root": str(output_root),
                            "variant_count": 1,
                            "preset_ids": ["fast"],
                        },
                    },
                )
                self.assertNotIn("error", start_response)
                structured_start = start_response["result"]["structuredContent"]
                job_path = Path(structured_start["job_path"])
                self.assertTrue(first_segment_recorded.wait(timeout=2.0))

                status_response = self.request(
                    "tools/call",
                    {
                        "name": server.TOOL_SCRIBE_TRANSCRIBE_JOB_STATUS,
                        "arguments": {"job_id": structured_start["job_id"]},
                    },
                )
                structured_status = status_response["result"]["structuredContent"]
                progress = structured_status["progress"]
                self.assertEqual(progress["current_variant_id"], "fast")
                self.assertEqual(progress["current_preset_id"], "fast")
                self.assertEqual(progress["segment_count"], 1)
                self.assertIsNotNone(progress["updated_at"])
                self.assertEqual(progress["last_segment"]["start"], 0.0)
                self.assertEqual(progress["last_segment"]["end"], 1.5)
                self.assertEqual(
                    len(progress["last_segment"]["text"]),
                    server.PROGRESS_TEXT_PREVIEW_CHARS,
                )
                self.assertTrue(progress["last_segment"]["text_truncated"])
                self.assertEqual(
                    structured_status["job"]["variants"][0]["progress"]["segment_count"],
                    1,
                )

                release_transcription.set()
                job = self.wait_for_terminal_job(job_path)

            self.assertEqual(job["status"], server.JOB_STATUS_COMPLETED)
            self.assertEqual(job["progress"]["current_variant_id"], "fast")
            self.assertEqual(job["progress"]["segment_count"], 2)
            self.assertEqual(job["progress"]["last_segment"]["text"], "second segment")
            self.assertFalse(job["progress"]["last_segment"]["text_truncated"])
            self.assertEqual(job["variants"][0]["progress"]["segment_count"], 2)

    def test_background_job_persists_cancellation_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            audio_path = root / "sample.wav"
            output_root = root / "job-output"
            audio_path.write_bytes(b"not real audio")
            first_variant_started = threading.Event()
            release_first_variant = threading.Event()
            self.addCleanup(release_first_variant.set)

            def fake_transcribe_audio(
                audio_path_arg,
                preset,
                language=None,
                model_size=None,
                device="auto",
                compute_type="default",
                progress_callback=None,
            ):
                first_variant_started.set()
                self.assertTrue(release_first_variant.wait(timeout=2.0))
                return SimpleNamespace(
                    backend="fake-stt",
                    model=model_size or preset.model_size,
                    preset_id=preset.id,
                    language=language,
                    params={"beam_size": preset.beam_size},
                    segments=(
                        SimpleNamespace(
                            start=0.0,
                            end=1.0,
                            text=f"{preset.id} segment",
                        ),
                    ),
                )

            with patch("server.transcribe_audio", side_effect=fake_transcribe_audio):
                start_response = self.request(
                    "tools/call",
                    {
                        "name": server.TOOL_SCRIBE_TRANSCRIBE_JOB_START,
                        "arguments": {
                            "audio_path": str(audio_path),
                            "output_root": str(output_root),
                            "variant_count": 2,
                            "preset_ids": ["fast", "strict"],
                        },
                    },
                )
                self.assertNotIn("error", start_response)
                structured_start = start_response["result"]["structuredContent"]
                job_path = Path(structured_start["job_path"])
                self.assertFalse(structured_start["cancel_requested"])
                self.assertFalse(structured_start["cancellation"]["cancel_effective"])
                self.assert_durable_handle(structured_start, job_path)
                self.assertTrue(first_variant_started.wait(timeout=2.0))

                active_status_response = self.request(
                    "tools/call",
                    {
                        "name": server.TOOL_SCRIBE_TRANSCRIBE_JOB_STATUS,
                        "arguments": {"job_id": structured_start["job_id"]},
                    },
                )
                structured_active_status = active_status_response["result"]["structuredContent"]
                self.assertEqual(structured_active_status["job_path"], str(job_path))
                self.assertIn(
                    structured_active_status["status"],
                    {server.JOB_STATUS_QUEUED, server.JOB_STATUS_RUNNING},
                )
                self.assert_durable_handle(structured_active_status, job_path)

                cancel_response = self.request(
                    "tools/call",
                    {
                        "name": server.TOOL_SCRIBE_TRANSCRIBE_JOB_CANCEL,
                        "arguments": {"job_id": structured_start["job_id"]},
                    },
                )

                self.assertNotIn("error", cancel_response)
                structured_cancel = cancel_response["result"]["structuredContent"]
                self.assertEqual(structured_cancel["status"], server.JOB_STATUS_CANCEL_REQUESTED)
                self.assertTrue(structured_cancel["cancel_requested"])
                self.assertIsNotNone(structured_cancel["cancel_requested_at"])
                self.assertIsNone(structured_cancel["cancel_observed_at"])
                self.assertFalse(structured_cancel["cancel_effective"])
                self.assertEqual(
                    structured_cancel["cancellation"]["cancel_requested_at"],
                    structured_cancel["cancel_requested_at"],
                )
                self.assert_durable_handle(structured_cancel, job_path)

                requested_job = json.loads(job_path.read_text(encoding="utf-8"))
                self.assertTrue(requested_job["cancel_requested"])
                self.assertEqual(
                    requested_job["cancellation"]["cancel_requested_at"],
                    structured_cancel["cancel_requested_at"],
                )

                release_first_variant.set()
                job = self.wait_for_terminal_job(job_path)

            self.assertEqual(job["status"], server.JOB_STATUS_CANCELLED)
            self.assertTrue(job["cancel_requested"])
            self.assertIsNotNone(job["cancel_requested_at"])
            self.assertIsNotNone(job["cancel_observed_at"])
            self.assertTrue(job["cancel_effective"])
            self.assertEqual(job["cancellation"]["cancel_effective"], job["cancel_effective"])
            self.assertEqual(
                [variant["status"] for variant in job["variants"]],
                [server.VARIANT_STATUS_COMPLETED, server.VARIANT_STATUS_CANCELLED],
            )
            self.assertIsNotNone(job["variants"][1]["cancelled_at"])
            self.assertEqual(job["variants"][1]["cancel_note"], server.CANCEL_OBSERVED_NOTE)

            status_response = self.request(
                "tools/call",
                {
                    "name": server.TOOL_SCRIBE_TRANSCRIBE_JOB_STATUS,
                    "arguments": {"job_path": str(job_path)},
                },
            )
            structured_status = status_response["result"]["structuredContent"]
            self.assertEqual(structured_status["status"], server.JOB_STATUS_CANCELLED)
            self.assertEqual(structured_status["cancel_requested_at"], job["cancel_requested_at"])
            self.assertEqual(structured_status["cancel_observed_at"], job["cancel_observed_at"])
            self.assertTrue(structured_status["cancellation"]["cancel_effective"])
            self.assert_durable_handle(structured_status, job_path)

            collect_response = self.request(
                "tools/call",
                {
                    "name": server.TOOL_SCRIBE_TRANSCRIBE_JOB_COLLECT,
                    "arguments": {"job_path": str(job_path)},
                },
            )
            structured_collect = collect_response["result"]["structuredContent"]
            self.assertFalse(structured_collect["ready_for_canon"])
            self.assertEqual(structured_collect["completed_variant_count"], 1)
            self.assertEqual(structured_collect["cancel_requested_at"], job["cancel_requested_at"])
            self.assertTrue(structured_collect["cancel_effective"])
            self.assert_durable_handle(structured_collect, job_path)

    def test_inactive_job_id_requires_durable_job_path(self) -> None:
        response = self.request(
            "tools/call",
            {
                "name": server.TOOL_SCRIBE_TRANSCRIBE_JOB_STATUS,
                "arguments": {"job_id": "job-not-active"},
            },
        )

        self.assertEqual(response["error"]["code"], server.TOOL_ERROR)
        self.assertEqual(response["error"]["data"]["field"], "job_id")
        self.assertIn("pass job_path", response["error"]["data"]["error"])

    def assert_durable_handle(self, structured: dict, job_path: Path) -> None:
        self.assertEqual(structured["durable_job_path"], str(job_path))
        self.assertEqual(structured["durable_handle"]["type"], "job_path")
        self.assertEqual(structured["durable_handle"]["job_path"], str(job_path))
        self.assertTrue(structured["durable_handle"]["restart_safe"])
        self.assertIn("job_id only resolves", structured["durable_handle"]["note"])
        self.assertEqual(
            structured["resume_arguments"],
            {
                "status": {"job_path": str(job_path)},
                "collect": {"job_path": str(job_path)},
                "cancel": {"job_path": str(job_path)},
            },
        )

    def wait_for_terminal_job(self, job_path: Path) -> dict:
        terminal_statuses = {
            server.JOB_STATUS_COMPLETED,
            server.JOB_STATUS_THRESHOLD_REACHED,
            server.JOB_STATUS_PARTIAL_FAILED,
            server.JOB_STATUS_FAILED,
            server.JOB_STATUS_CANCELLED,
        }
        for _ in range(100):
            if job_path.exists():
                job = json.loads(job_path.read_text(encoding="utf-8"))
                if job["status"] in terminal_statuses:
                    return job
            time.sleep(0.02)
        self.fail(f"job did not finish: {job_path}")


if __name__ == "__main__":
    unittest.main()
