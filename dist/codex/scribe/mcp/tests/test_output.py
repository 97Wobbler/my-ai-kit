from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

MCP_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MCP_ROOT))

from scribe_mcp.output import (  # noqa: E402
    TranscriptionSegment,
    TranscriptionVariant,
    write_partial_transcription_variant,
    write_transcription_manifest,
    write_transcription_outputs,
    write_transcription_variant,
)


class OutputWriterTests(unittest.TestCase):
    def test_writes_manifest_and_variant_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output_root = Path(tmp)
            variant = TranscriptionVariant(
                variant_id="balanced",
                backend="faster-whisper",
                preset_id="balanced",
                preset_params={
                    "beam_size": 5,
                    "word_timestamps": True,
                    "vad_parameters": {"speech_pad_ms": 200},
                },
                model="medium",
                language="en",
                segments=(
                    TranscriptionSegment(start=0.0, end=1.25, text="hello world"),
                    {
                        "start": 1.25,
                        "end": 2.5,
                        "text": "second segment",
                        "language": "es",
                    },
                ),
            )

            manifest = write_transcription_outputs(
                output_root,
                "audio/input.wav",
                (variant,),
                created_at="2026-05-26T10:00:00Z",
            )

            manifest_path = output_root / "manifest.json"
            text_path = output_root / "variants" / "balanced.md"
            json_path = output_root / "variants" / "balanced.json"

            self.assertTrue(manifest_path.exists())
            self.assertTrue(text_path.exists())
            self.assertTrue(json_path.exists())
            self.assertEqual(json.loads(manifest_path.read_text(encoding="utf-8")), manifest)

            self.assertEqual(manifest["audio_path"], "audio/input.wav")
            self.assertEqual(manifest["created_at"], "2026-05-26T10:00:00Z")
            self.assertEqual(len(manifest["variants"]), 1)

            manifest_variant = manifest["variants"][0]
            self.assertEqual(manifest_variant["variant_id"], "balanced")
            self.assertEqual(manifest_variant["backend"], "faster-whisper")
            self.assertEqual(manifest_variant["preset_id"], "balanced")
            self.assertEqual(manifest_variant["preset_params"]["beam_size"], 5)
            self.assertEqual(manifest_variant["preset_params"]["vad_parameters"]["speech_pad_ms"], 200)
            self.assertEqual(manifest_variant["model"], "medium")
            self.assertEqual(manifest_variant["language"], "en")
            self.assertEqual(manifest_variant["text_path"], "variants/balanced.md")
            self.assertEqual(manifest_variant["json_path"], "variants/balanced.json")
            self.assertEqual(manifest_variant["segment_count"], 2)

            self.assertFalse(Path(manifest_variant["text_path"]).is_absolute())
            self.assertFalse(Path(manifest_variant["json_path"]).is_absolute())

            markdown = text_path.read_text(encoding="utf-8")
            self.assertIn("- backend: faster-whisper", markdown)
            self.assertIn("- preset_id: balanced", markdown)
            self.assertIn("[00:00.000-00:01.250] hello world", markdown)
            self.assertIn("[00:01.250-00:02.500] second segment", markdown)

            variant_json = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertEqual(variant_json["backend"], "faster-whisper")
            self.assertEqual(variant_json["preset_params"]["word_timestamps"], True)
            self.assertEqual(
                variant_json["segments"],
                [
                    {"start": 0.0, "end": 1.25, "text": "hello world", "language": "en"},
                    {"start": 1.25, "end": 2.5, "text": "second segment", "language": "es"},
                ],
            )

    def test_untimed_segments_are_written_without_timestamp_prefix(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output_root = Path(tmp)
            variant = TranscriptionVariant(
                variant_id="fast",
                backend="fake-backend",
                preset_id="fast",
                preset_params={"beam_size": 1},
                model="small",
                language=None,
                segments=(TranscriptionSegment(text="no clock here"),),
            )

            write_transcription_outputs(
                output_root,
                "relative/audio.wav",
                (variant,),
                created_at="2026-05-26T10:00:00Z",
            )

            markdown = (output_root / "variants" / "fast.md").read_text(encoding="utf-8")
            self.assertIn("\nno clock here\n", markdown)
            self.assertNotIn("[]", markdown)

            variant_json = json.loads((output_root / "variants" / "fast.json").read_text(encoding="utf-8"))
            self.assertEqual(
                variant_json["segments"],
                [{"start": None, "end": None, "text": "no clock here", "language": None}],
            )

    def test_can_write_variant_before_manifest_for_partial_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output_root = Path(tmp)
            variant = TranscriptionVariant(
                variant_id="fast",
                backend="fake-backend",
                preset_id="fast",
                preset_params={"beam_size": 1},
                model="tiny",
                language="ko",
                segments=({"start": 0.0, "end": 1.0, "text": "partial"},),
            )

            manifest_variant = write_transcription_variant(output_root, variant)

            self.assertFalse((output_root / "manifest.json").exists())
            self.assertTrue((output_root / "variants" / "fast.md").exists())
            self.assertEqual(manifest_variant["text_path"], "variants/fast.md")

            manifest = write_transcription_manifest(
                output_root,
                "audio.wav",
                (manifest_variant,),
                created_at="2026-05-26T10:00:00Z",
            )

            self.assertEqual(manifest["variants"], [manifest_variant])
            self.assertEqual(
                json.loads((output_root / "manifest.json").read_text(encoding="utf-8")),
                manifest,
            )

    def test_writes_partial_variant_json_without_final_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output_root = Path(tmp)
            variant = TranscriptionVariant(
                variant_id="fast",
                backend="faster-whisper",
                preset_id="fast",
                preset_params={"beam_size": 1},
                model="small",
                language="en",
                segments=(
                    TranscriptionSegment(start=0.0, end=1.0, text="first"),
                    {"start": 1.0, "end": 2.0, "text": "second"},
                ),
            )

            partial = write_partial_transcription_variant(
                output_root,
                variant,
                updated_at="2026-05-26T10:00:00Z",
            )

            partial_path = output_root / "variants" / "fast.partial.json"
            self.assertTrue(partial_path.exists())
            self.assertFalse((output_root / "variants" / "fast.json").exists())
            self.assertFalse((output_root / "variants" / "fast.md").exists())
            self.assertFalse((output_root / "manifest.json").exists())
            self.assertEqual(partial["partial_json_path"], "variants/fast.partial.json")
            self.assertEqual(partial["segment_count"], 2)
            self.assertFalse(Path(partial["partial_json_path"]).is_absolute())

            payload = json.loads(partial_path.read_text(encoding="utf-8"))
            self.assertTrue(payload["partial"])
            self.assertEqual(payload["updated_at"], "2026-05-26T10:00:00Z")
            self.assertEqual(payload["segment_count"], 2)
            self.assertEqual(
                payload["segments"],
                [
                    {"start": 0.0, "end": 1.0, "text": "first", "language": "en"},
                    {"start": 1.0, "end": 2.0, "text": "second", "language": "en"},
                ],
            )

    def test_partial_variant_json_can_be_overwritten_with_more_segments(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output_root = Path(tmp)
            base = {
                "variant_id": "balanced",
                "backend": "faster-whisper",
                "preset_id": "balanced",
                "preset_params": {"beam_size": 5},
                "model": "medium",
                "language": None,
            }

            write_partial_transcription_variant(
                output_root,
                TranscriptionVariant(
                    **base,
                    segments=({"start": 0.0, "end": 1.0, "text": "first"},),
                ),
                updated_at="2026-05-26T10:00:00Z",
            )
            write_partial_transcription_variant(
                output_root,
                TranscriptionVariant(
                    **base,
                    segments=(
                        {"start": 0.0, "end": 1.0, "text": "first"},
                        {"start": 1.0, "end": 2.0, "text": "second"},
                    ),
                ),
                updated_at="2026-05-26T10:00:05Z",
            )

            payload = json.loads(
                (output_root / "variants" / "balanced.partial.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(payload["updated_at"], "2026-05-26T10:00:05Z")
            self.assertEqual(payload["segment_count"], 2)
            self.assertEqual(
                [segment["text"] for segment in payload["segments"]],
                ["first", "second"],
            )

    def test_variant_id_rejects_path_separators(self) -> None:
        variant = TranscriptionVariant(
            variant_id="../bad",
            backend="fake-backend",
            preset_id="fast",
            preset_params={},
            model="small",
            language="en",
            segments=(),
        )

        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(ValueError, "path separators"):
                write_transcription_outputs(tmp, "audio.wav", (variant,), created_at="2026-05-26T10:00:00Z")


if __name__ == "__main__":
    unittest.main()
