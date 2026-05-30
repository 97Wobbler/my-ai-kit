"""Lazy faster-whisper transcription wrapper for Scribe."""

from __future__ import annotations

import os
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from typing import Any, Callable

from .presets import Preset, select_presets

BACKEND = "faster-whisper"
INSTALL_COMMAND = "python3 -m pip install faster-whisper"


class MissingTranscriptionDependency(ImportError):
    """Raised when the optional transcription backend is unavailable."""

    def __init__(self, message: str | None = None):
        self.dependency = BACKEND
        self.install_command = INSTALL_COMMAND
        self.install_guidance = (
            "Install faster-whisper in the Python environment that runs the "
            f"Scribe MCP server: {INSTALL_COMMAND}"
        )
        super().__init__(
            message
            or (
                "Missing optional transcription dependency faster-whisper. "
                f"{self.install_guidance}"
            )
        )


@dataclass(frozen=True, slots=True)
class TranscriptionSegment:
    """One normalized transcript segment."""

    start: float
    end: float
    text: str

    def to_dict(self) -> dict[str, float | str]:
        return {"start": self.start, "end": self.end, "text": self.text}


@dataclass(frozen=True, slots=True)
class TranscriptionResult:
    """Structured transcription output from the local STT backend."""

    backend: str
    model: str
    preset_id: str
    language: str | None
    segments: tuple[TranscriptionSegment, ...]
    text: str
    params: dict[str, Any]
    language_probability: float | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "backend": self.backend,
            "model": self.model,
            "preset_id": self.preset_id,
            "language": self.language,
            "language_probability": self.language_probability,
            "segments": [segment.to_dict() for segment in self.segments],
            "text": self.text,
            "params": _copy_params(self.params),
        }


def transcribe_audio(
    audio_path: str | os.PathLike[str],
    preset: Preset | str,
    language: str | None = None,
    model_size: str | None = None,
    device: str = "auto",
    compute_type: str = "default",
    progress_callback: Callable[[dict[str, Any]], None] | None = None,
) -> TranscriptionResult:
    """Transcribe an audio file with faster-whisper using a Scribe preset."""

    selected_preset = _coerce_preset(preset)
    selected_model = model_size or selected_preset.model_size
    transcribe_options = selected_preset.to_transcribe_options()
    if language is not None:
        transcribe_options["language"] = language

    WhisperModel = _load_whisper_model()
    model = WhisperModel(selected_model, device=device, compute_type=compute_type)
    raw_segments, info = model.transcribe(os.fspath(audio_path), **transcribe_options)
    segments = convert_segments(raw_segments, progress_callback=progress_callback)

    detected_language = _optional_str(_metadata_value(info, "language")) or language
    language_probability = _optional_float(
        _metadata_value(info, "language_probability")
    )

    return TranscriptionResult(
        backend=BACKEND,
        model=selected_model,
        preset_id=selected_preset.id,
        language=detected_language,
        language_probability=language_probability,
        segments=segments,
        text="".join(segment.text for segment in segments).strip(),
        params=_copy_params(transcribe_options),
    )


def convert_segments(
    segments: Iterable[Mapping[str, Any] | object],
    progress_callback: Callable[[dict[str, Any]], None] | None = None,
) -> tuple[TranscriptionSegment, ...]:
    """Convert faster-whisper segment objects or dicts into stable dataclasses."""

    converted: list[TranscriptionSegment] = []
    for segment in segments:
        normalized = segment_to_dataclass(segment)
        converted.append(normalized)
        if progress_callback is not None:
            progress_callback(
                {
                    "segment_count": len(converted),
                    "segment": normalized.to_dict(),
                }
            )
    return tuple(converted)


def segment_to_dataclass(segment: Mapping[str, Any] | object) -> TranscriptionSegment:
    """Convert a single segment object or mapping to a TranscriptionSegment."""

    return TranscriptionSegment(
        start=float(_segment_value(segment, "start")),
        end=float(_segment_value(segment, "end")),
        text=str(_segment_value(segment, "text")),
    )


def _load_whisper_model() -> Any:
    try:
        from faster_whisper import WhisperModel
    except ModuleNotFoundError as exc:
        raise MissingTranscriptionDependency() from exc
    return WhisperModel


def _coerce_preset(preset: Preset | str) -> Preset:
    if isinstance(preset, Preset):
        return preset
    if isinstance(preset, str):
        return select_presets(1, (preset,))[0]
    raise TypeError("preset must be a Preset instance or preset id string")


_MISSING = object()


def _segment_value(segment: Mapping[str, Any] | object, key: str) -> Any:
    if isinstance(segment, Mapping):
        value = segment.get(key, _MISSING)
    else:
        value = getattr(segment, key, _MISSING)

    if value is _MISSING:
        raise ValueError(f"Transcription segment is missing required field: {key}")
    return value


def _metadata_value(info: Mapping[str, Any] | object | None, key: str) -> Any:
    if info is None:
        return None
    if isinstance(info, Mapping):
        return info.get(key)
    return getattr(info, key, None)


def _optional_str(value: Any) -> str | None:
    if value is None:
        return None
    return str(value)


def _optional_float(value: Any) -> float | None:
    if value is None:
        return None
    return float(value)


def _copy_params(params: Mapping[str, Any]) -> dict[str, Any]:
    copied: dict[str, Any] = {}
    for key, value in params.items():
        if isinstance(value, Mapping):
            copied[key] = dict(value)
        else:
            copied[key] = value
    return copied


__all__ = [
    "BACKEND",
    "INSTALL_COMMAND",
    "MissingTranscriptionDependency",
    "TranscriptionResult",
    "TranscriptionSegment",
    "convert_segments",
    "segment_to_dataclass",
    "transcribe_audio",
]
