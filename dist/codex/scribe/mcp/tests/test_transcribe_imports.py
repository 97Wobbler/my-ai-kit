from __future__ import annotations

import builtins
import importlib
import sys
import unittest
from pathlib import Path
from types import ModuleType, SimpleNamespace
from unittest.mock import patch

MCP_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MCP_ROOT))


class TranscribeImportTests(unittest.TestCase):
    def setUp(self) -> None:
        self.saved_modules = {}
        for module_name in ("faster_whisper", "scribe_mcp.transcribe"):
            if module_name in sys.modules:
                self.saved_modules[module_name] = sys.modules.pop(module_name)

        package = sys.modules.get("scribe_mcp")
        if package is not None and hasattr(package, "transcribe"):
            delattr(package, "transcribe")

    def tearDown(self) -> None:
        for module_name in ("faster_whisper", "scribe_mcp.transcribe"):
            sys.modules.pop(module_name, None)
        sys.modules.update(self.saved_modules)

    def import_transcribe(self):
        return importlib.import_module("scribe_mcp.transcribe")

    def test_import_does_not_import_faster_whisper(self) -> None:
        self.import_transcribe()

        self.assertNotIn("faster_whisper", sys.modules)

    def test_missing_dependency_error_includes_install_guidance(self) -> None:
        transcribe = self.import_transcribe()
        real_import = builtins.__import__

        def fake_import(name, globals=None, locals=None, fromlist=(), level=0):
            if name == "faster_whisper":
                raise ModuleNotFoundError(
                    "No module named 'faster_whisper'",
                    name="faster_whisper",
                )
            return real_import(name, globals, locals, fromlist, level)

        with patch("builtins.__import__", side_effect=fake_import):
            with self.assertRaises(transcribe.MissingTranscriptionDependency) as raised:
                transcribe.transcribe_audio("sample.wav", "fast")

        self.assertIn("python3 -m pip install faster-whisper", str(raised.exception))
        self.assertIn(
            "python3 -m pip install faster-whisper",
            raised.exception.install_guidance,
        )

    def test_segment_conversion_preserves_start_end_text(self) -> None:
        transcribe = self.import_transcribe()

        segments = transcribe.convert_segments(
            (
                SimpleNamespace(start=0.25, end=1.5, text="first"),
                {"start": 2, "end": 3.75, "text": "second"},
            )
        )

        self.assertEqual(
            segments,
            (
                transcribe.TranscriptionSegment(start=0.25, end=1.5, text="first"),
                transcribe.TranscriptionSegment(start=2.0, end=3.75, text="second"),
            ),
        )

    def test_transcribe_audio_uses_fake_faster_whisper_module(self) -> None:
        transcribe = self.import_transcribe()
        fake_module = ModuleType("faster_whisper")

        class FakeWhisperModel:
            constructed = []
            transcribe_calls = []

            def __init__(self, model_size, device="auto", compute_type="default"):
                self.constructed.append(
                    {
                        "model_size": model_size,
                        "device": device,
                        "compute_type": compute_type,
                    }
                )

            def transcribe(self, audio_path, **kwargs):
                self.transcribe_calls.append(
                    {"audio_path": audio_path, "kwargs": dict(kwargs)}
                )
                return (
                    (
                        SimpleNamespace(start=0.0, end=1.0, text=" Hello"),
                        {"start": 1.0, "end": 2.0, "text": " world"},
                    ),
                    SimpleNamespace(language="en", language_probability=0.98),
                )

        fake_module.WhisperModel = FakeWhisperModel

        with patch.dict(sys.modules, {"faster_whisper": fake_module}):
            result = transcribe.transcribe_audio(
                Path("sample.wav"),
                "fast",
                language="ko",
                model_size="tiny",
                device="cpu",
                compute_type="int8",
            )

        self.assertEqual(
            FakeWhisperModel.constructed,
            [{"model_size": "tiny", "device": "cpu", "compute_type": "int8"}],
        )
        self.assertEqual(
            FakeWhisperModel.transcribe_calls[0]["audio_path"],
            "sample.wav",
        )
        kwargs = FakeWhisperModel.transcribe_calls[0]["kwargs"]
        self.assertEqual(kwargs["language"], "ko")
        self.assertEqual(kwargs["beam_size"], 1)
        self.assertTrue(kwargs["vad_filter"])

        self.assertEqual(result.backend, "faster-whisper")
        self.assertEqual(result.model, "tiny")
        self.assertEqual(result.preset_id, "fast")
        self.assertEqual(result.language, "en")
        self.assertEqual(result.language_probability, 0.98)
        self.assertEqual(result.text, "Hello world")
        self.assertEqual(
            [segment.to_dict() for segment in result.segments],
            [
                {"start": 0.0, "end": 1.0, "text": " Hello"},
                {"start": 1.0, "end": 2.0, "text": " world"},
            ],
        )
        self.assertEqual(result.params["language"], "ko")
        self.assertFalse(result.params["word_timestamps"])


if __name__ == "__main__":
    unittest.main()
