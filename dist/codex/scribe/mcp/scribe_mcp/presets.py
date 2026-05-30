"""Deterministic STT preset definitions for Scribe MCP runs."""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass

SUPPORTED_PRESET_IDS = ("fast", "balanced", "strict", "no-vad")
DEFAULT_PRESET_ORDER = ("balanced", "fast", "strict", "no-vad")
MIN_VARIANT_COUNT = 1
MAX_VARIANT_COUNT = len(DEFAULT_PRESET_ORDER)


class PresetValidationError(ValueError):
    """Raised when preset selection input cannot be used safely."""


@dataclass(frozen=True, slots=True)
class Preset:
    """Configuration profile for one deterministic STT transcript variant."""

    id: str
    model_size: str
    beam_size: int
    best_of: int
    temperature: float
    vad_filter: bool
    word_timestamps: bool
    condition_on_previous_text: bool
    description: str
    vad_parameters: tuple[tuple[str, int | float], ...] = ()

    def to_transcribe_options(self) -> dict[str, object]:
        """Return a fresh kwargs dict for the transcription call."""

        options: dict[str, object] = {
            "beam_size": self.beam_size,
            "best_of": self.best_of,
            "temperature": self.temperature,
            "vad_filter": self.vad_filter,
            "word_timestamps": self.word_timestamps,
            "condition_on_previous_text": self.condition_on_previous_text,
        }
        if self.vad_parameters:
            options["vad_parameters"] = dict(self.vad_parameters)
        return options


_DEFAULT_VAD_PARAMETERS = (
    ("min_silence_duration_ms", 500),
    ("speech_pad_ms", 200),
)

_PRESETS = {
    "fast": Preset(
        id="fast",
        model_size="small",
        beam_size=1,
        best_of=1,
        temperature=0.0,
        vad_filter=True,
        word_timestamps=False,
        condition_on_previous_text=True,
        description="Low-latency pass with minimal search.",
        vad_parameters=_DEFAULT_VAD_PARAMETERS,
    ),
    "balanced": Preset(
        id="balanced",
        model_size="medium",
        beam_size=5,
        best_of=5,
        temperature=0.0,
        vad_filter=True,
        word_timestamps=True,
        condition_on_previous_text=True,
        description="Default pass balancing quality and runtime.",
        vad_parameters=_DEFAULT_VAD_PARAMETERS,
    ),
    "strict": Preset(
        id="strict",
        model_size="medium",
        beam_size=8,
        best_of=8,
        temperature=0.0,
        vad_filter=True,
        word_timestamps=True,
        condition_on_previous_text=False,
        description="Conservative pass for higher-confidence alternatives.",
        vad_parameters=(
            ("min_silence_duration_ms", 300),
            ("speech_pad_ms", 300),
        ),
    ),
    "no-vad": Preset(
        id="no-vad",
        model_size="medium",
        beam_size=5,
        best_of=5,
        temperature=0.0,
        vad_filter=False,
        word_timestamps=True,
        condition_on_previous_text=True,
        description="Default-quality pass without voice activity filtering.",
    ),
}

if set(_PRESETS) != set(SUPPORTED_PRESET_IDS):
    raise RuntimeError("Preset registry does not match SUPPORTED_PRESET_IDS")


def all_presets() -> tuple[Preset, ...]:
    """Return all supported presets in stable supported-id order."""

    return tuple(_PRESETS[preset_id] for preset_id in SUPPORTED_PRESET_IDS)


def get_preset(preset_id: str) -> Preset:
    """Return a preset by id or raise a validation error."""

    return _PRESETS[_validate_preset_id(preset_id)]


def select_preset_ids(
    variant_count: int,
    requested_ids: Iterable[str] | None = None,
) -> tuple[str, ...]:
    """Return ordered preset ids for the requested number of transcript variants."""

    count = _validate_variant_count(variant_count)
    if requested_ids is None:
        return DEFAULT_PRESET_ORDER[:count]

    normalized_ids = _normalize_requested_ids(requested_ids)
    if len(normalized_ids) != count:
        raise PresetValidationError(
            "requested_ids length must match variant_count: "
            f"expected {count}, got {len(normalized_ids)}"
        )
    return normalized_ids


def select_presets(
    variant_count: int,
    requested_ids: Iterable[str] | None = None,
) -> tuple[Preset, ...]:
    """Return ordered preset objects for the requested transcript variants."""

    return tuple(
        get_preset(preset_id)
        for preset_id in select_preset_ids(variant_count, requested_ids)
    )


def _validate_variant_count(variant_count: int) -> int:
    if isinstance(variant_count, bool) or not isinstance(variant_count, int):
        raise PresetValidationError("variant_count must be an integer from 1 through 4")
    if variant_count < MIN_VARIANT_COUNT or variant_count > MAX_VARIANT_COUNT:
        raise PresetValidationError("variant_count must be between 1 and 4")
    return variant_count


def _normalize_requested_ids(requested_ids: Iterable[str]) -> tuple[str, ...]:
    if isinstance(requested_ids, str):
        raise PresetValidationError(
            "requested_ids must be a sequence of preset id strings, not a single string"
        )

    try:
        normalized_ids = tuple(requested_ids)
    except TypeError as exc:
        raise PresetValidationError(
            "requested_ids must be an iterable of preset id strings"
        ) from exc

    if not normalized_ids:
        raise PresetValidationError("requested_ids cannot be empty")

    seen: set[str] = set()
    for preset_id in normalized_ids:
        _validate_preset_id(preset_id)
        if preset_id in seen:
            raise PresetValidationError(f"Duplicate preset id requested: {preset_id}")
        seen.add(preset_id)

    return normalized_ids


def _validate_preset_id(preset_id: str) -> str:
    if not isinstance(preset_id, str):
        raise PresetValidationError("Preset id must be a string")
    if not preset_id.strip():
        raise PresetValidationError("Preset id cannot be empty")
    if preset_id not in _PRESETS:
        supported = ", ".join(SUPPORTED_PRESET_IDS)
        raise PresetValidationError(
            f"Unknown preset id: {preset_id}. Supported preset ids: {supported}"
        )
    return preset_id


__all__ = [
    "DEFAULT_PRESET_ORDER",
    "MAX_VARIANT_COUNT",
    "MIN_VARIANT_COUNT",
    "Preset",
    "PresetValidationError",
    "SUPPORTED_PRESET_IDS",
    "all_presets",
    "get_preset",
    "select_preset_ids",
    "select_presets",
]
