"""Output writers for Scribe STT transcript variants."""

from __future__ import annotations

import json
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime, timezone
from os import PathLike
from pathlib import Path, PurePosixPath
from typing import Any


@dataclass(frozen=True, slots=True)
class TranscriptionSegment:
    """One transcript segment from an STT backend."""

    text: str
    start: int | float | None = None
    end: int | float | None = None
    language: str | None = None


SegmentInput = TranscriptionSegment | Mapping[str, Any]


@dataclass(frozen=True, slots=True)
class TranscriptionVariant:
    """One STT output variant and the metadata needed to reconcile it later."""

    variant_id: str
    backend: str
    preset_id: str
    preset_params: Mapping[str, Any]
    model: str
    language: str | None
    segments: Sequence[SegmentInput]


def write_transcription_outputs(
    output_root: str | PathLike[str],
    audio_path: str | PathLike[str],
    variants: Sequence[TranscriptionVariant],
    created_at: str | datetime | None = None,
) -> dict[str, Any]:
    """Write a manifest and markdown/json files for each transcript variant."""

    formatted_created_at = _format_created_at(created_at)
    manifest_variants = [
        write_transcription_variant(output_root, variant) for variant in variants
    ]
    return write_transcription_manifest(
        output_root,
        audio_path,
        manifest_variants,
        created_at=formatted_created_at,
    )


def write_transcription_variant(
    output_root: str | PathLike[str],
    variant: TranscriptionVariant,
) -> dict[str, Any]:
    """Write one transcript variant and return its manifest entry."""

    root = Path(output_root)
    variants_dir = root / "variants"
    variants_dir.mkdir(parents=True, exist_ok=True)

    variant_id = _validate_variant_id(variant.variant_id)
    text_rel = PurePosixPath("variants") / f"{variant_id}.md"
    json_rel = PurePosixPath("variants") / f"{variant_id}.json"
    text_path = root / text_rel
    json_path = root / json_rel

    segments = [_normalize_segment(segment, variant.language) for segment in variant.segments]
    variant_payload = {
        "variant_id": variant_id,
        "backend": variant.backend,
        "preset_id": variant.preset_id,
        "preset_params": _jsonable(variant.preset_params),
        "model": variant.model,
        "language": variant.language,
        "segments": segments,
    }

    text_path.write_text(_render_markdown_variant(variant_payload), encoding="utf-8")
    json_path.write_text(_dumps_json(variant_payload), encoding="utf-8")

    return {
        "variant_id": variant_id,
        "backend": variant.backend,
        "preset_id": variant.preset_id,
        "preset_params": _jsonable(variant.preset_params),
        "model": variant.model,
        "language": variant.language,
        "text_path": text_rel.as_posix(),
        "json_path": json_rel.as_posix(),
        "segment_count": len(segments),
    }


def write_partial_transcription_variant(
    output_root: str | PathLike[str],
    variant: TranscriptionVariant,
    updated_at: str | datetime | None = None,
) -> dict[str, Any]:
    """Write an in-progress transcript variant JSON artifact."""

    root = Path(output_root)
    variants_dir = root / "variants"
    variants_dir.mkdir(parents=True, exist_ok=True)

    variant_id = _validate_variant_id(variant.variant_id)
    partial_rel = PurePosixPath("variants") / f"{variant_id}.partial.json"
    partial_path = root / partial_rel
    segments = [_normalize_segment(segment, variant.language) for segment in variant.segments]
    formatted_updated_at = _format_created_at(updated_at)
    variant_payload = {
        "variant_id": variant_id,
        "backend": variant.backend,
        "preset_id": variant.preset_id,
        "preset_params": _jsonable(variant.preset_params),
        "model": variant.model,
        "language": variant.language,
        "segments": segments,
        "partial": True,
        "updated_at": formatted_updated_at,
        "segment_count": len(segments),
    }

    partial_path.write_text(_dumps_json(variant_payload), encoding="utf-8")

    return {
        "variant_id": variant_id,
        "backend": variant.backend,
        "preset_id": variant.preset_id,
        "preset_params": _jsonable(variant.preset_params),
        "model": variant.model,
        "language": variant.language,
        "partial_json_path": partial_rel.as_posix(),
        "segment_count": len(segments),
        "updated_at": formatted_updated_at,
    }


def write_transcription_manifest(
    output_root: str | PathLike[str],
    audio_path: str | PathLike[str],
    manifest_variants: Sequence[Mapping[str, Any]],
    created_at: str | datetime | None = None,
) -> dict[str, Any]:
    """Write a manifest for completed transcript variants."""

    root = Path(output_root)
    root.mkdir(parents=True, exist_ok=True)
    manifest = {
        "audio_path": str(audio_path),
        "created_at": _format_created_at(created_at),
        "variants": [_jsonable(variant) for variant in manifest_variants],
    }
    (root / "manifest.json").write_text(_dumps_json(manifest), encoding="utf-8")
    return manifest


def _validate_variant_id(variant_id: str) -> str:
    if not isinstance(variant_id, str):
        raise TypeError("variant_id must be a string")
    if not variant_id or variant_id in {".", ".."}:
        raise ValueError("variant_id must be a non-empty file stem")
    if "/" in variant_id or "\\" in variant_id:
        raise ValueError("variant_id must not contain path separators")
    return variant_id


def _normalize_segment(segment: SegmentInput, default_language: str | None) -> dict[str, Any]:
    if isinstance(segment, TranscriptionSegment):
        return {
            "start": segment.start,
            "end": segment.end,
            "text": segment.text,
            "language": segment.language if segment.language is not None else default_language,
        }
    if isinstance(segment, Mapping):
        text = segment.get("text")
        if not isinstance(text, str):
            raise TypeError("segment text must be a string")
        language = segment.get("language", default_language)
        if language is not None and not isinstance(language, str):
            raise TypeError("segment language must be a string when provided")
        return {
            "start": segment.get("start"),
            "end": segment.get("end"),
            "text": text,
            "language": language,
        }
    raise TypeError("segments must be TranscriptionSegment instances or mappings")


def _render_markdown_variant(variant: Mapping[str, Any]) -> str:
    lines = [
        f"# Transcript Variant: {variant['variant_id']}",
        "",
        f"- backend: {variant['backend']}",
        f"- preset_id: {variant['preset_id']}",
        f"- model: {variant['model']}",
        f"- language: {variant['language']}",
        "",
        "## Transcript",
        "",
    ]

    for segment in variant["segments"]:
        lines.append(_render_markdown_segment(segment))

    return "\n".join(lines).rstrip() + "\n"


def _render_markdown_segment(segment: Mapping[str, Any]) -> str:
    prefix = _timestamp_prefix(segment.get("start"), segment.get("end"))
    return f"{prefix}{segment['text']}"


def _timestamp_prefix(start: Any, end: Any) -> str:
    if start is None and end is None:
        return ""
    if start is not None and end is not None:
        return f"[{_format_timestamp(start)}-{_format_timestamp(end)}] "
    if start is not None:
        return f"[{_format_timestamp(start)}] "
    return f"[-{_format_timestamp(end)}] "


def _format_timestamp(value: Any) -> str:
    total_millis = int(round(float(value) * 1000))
    hours, remainder = divmod(total_millis, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    seconds, millis = divmod(remainder, 1000)
    if hours:
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{millis:03d}"
    return f"{minutes:02d}:{seconds:02d}.{millis:03d}"


def _format_created_at(created_at: str | datetime | None) -> str:
    if created_at is None:
        now = datetime.now(timezone.utc).replace(microsecond=0)
        return now.isoformat().replace("+00:00", "Z")
    if isinstance(created_at, datetime):
        return created_at.isoformat(timespec="seconds")
    if isinstance(created_at, str):
        return created_at
    raise TypeError("created_at must be a string, datetime, or None")


def _jsonable(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _jsonable(item) for key, item in value.items()}
    if isinstance(value, tuple | list):
        return [_jsonable(item) for item in value]
    return value


def _dumps_json(payload: Mapping[str, Any]) -> str:
    return json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


__all__ = [
    "TranscriptionSegment",
    "TranscriptionVariant",
    "write_partial_transcription_variant",
    "write_transcription_manifest",
    "write_transcription_outputs",
    "write_transcription_variant",
]
