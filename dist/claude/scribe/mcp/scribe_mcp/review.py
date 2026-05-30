"""Structured transcript review packet helpers for Scribe."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from os import PathLike
from typing import Any

SCHEMA_VERSION = "scribe.review_state.v1"
DEFAULT_PACKET_ID = "review-001"
DEFAULT_MAX_ITEMS = 5

READY = "ready"
REVIEW_NEEDED = "review_needed"

_DEFAULT_PROVENANCE = {
    "candidate_sources": ["transcript_evidence"],
    "used_context": False,
    "context_sources": [],
    "contamination_risk": "low",
    "risk_note": "No external or prior context used.",
}


def build_review_state(
    high_impact_items: Sequence[Mapping[str, Any]] | None = None,
    *,
    transcript_path: str | PathLike[str] | None = None,
    review_path: str | PathLike[str] | None = None,
    manifest_path: str | PathLike[str] | None = None,
    max_items: int = DEFAULT_MAX_ITEMS,
    packet_id: str = DEFAULT_PACKET_ID,
) -> dict[str, Any]:
    """Build the machine-readable review state for transcript completion gates.

    The caller supplies already-identified review items. This helper only
    normalizes the control contract, caps the user-facing clarification packet,
    and avoids depending on prose in ``transcript-review.md``.
    """

    item_cap = _validate_max_items(max_items)
    all_items = tuple(high_impact_items or ())
    blocking_items = [
        _normalize_review_item(item, index)
        for index, item in enumerate(all_items, start=1)
        if _is_high_impact(item)
    ]
    capped_items = blocking_items[:item_cap]
    requires_user_response = any(
        item["blocks_final_completion"] for item in capped_items
    )
    state = REVIEW_NEEDED if requires_user_response else READY

    review_state: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "state": state,
        "requires_user_response": requires_user_response,
        "reason": (
            "high_impact_uncertainty"
            if requires_user_response
            else "no_high_impact_items"
        ),
        "clarification_packet": {
            "packet_id": packet_id,
            "max_items": item_cap,
            "items": capped_items,
        },
        "resolution": {
            "status": "unresolved" if requires_user_response else "resolved",
            "resolved_at": None,
            "accepted_draft_risk": False,
            "user_response_summary": None,
        },
    }
    _add_path_if_present(review_state, "transcript_path", transcript_path)
    _add_path_if_present(review_state, "review_path", review_path)
    _add_path_if_present(review_state, "manifest_path", manifest_path)
    if len(blocking_items) > len(capped_items):
        review_state["clarification_packet"]["omitted_item_count"] = (
            len(blocking_items) - len(capped_items)
        )
    return review_state


def _normalize_review_item(item: Mapping[str, Any], index: int) -> dict[str, Any]:
    if not isinstance(item, Mapping):
        raise TypeError("high-impact review items must be mappings")

    return {
        "id": _optional_str(item.get("id")) or f"item-{index:03d}",
        "kind": _optional_str(item.get("kind")) or "term_confirmation",
        "impact": "high",
        "question": _optional_str(item.get("question"))
        or "Confirm the preferred wording for this high-impact transcript item.",
        "candidate": item.get("candidate"),
        "alternatives": _list_or_empty(item.get("alternatives")),
        "evidence": _list_or_empty(item.get("evidence")),
        "provenance": _normalize_provenance(item.get("provenance")),
        "default_if_unanswered": _optional_str(item.get("default_if_unanswered"))
        or "leave_as_transcribed",
        "blocks_final_completion": _optional_bool(
            item.get("blocks_final_completion"),
            default=True,
        ),
    }


def _normalize_provenance(value: Any) -> dict[str, Any]:
    if value is None:
        return _copy_jsonable(_DEFAULT_PROVENANCE)
    if not isinstance(value, Mapping):
        raise TypeError("review item provenance must be a mapping when provided")

    provenance = _copy_jsonable(_DEFAULT_PROVENANCE)
    provenance.update(_copy_jsonable(value))
    provenance["candidate_sources"] = _list_or_empty(
        provenance.get("candidate_sources")
    ) or ["transcript_evidence"]
    provenance["used_context"] = bool(provenance.get("used_context"))
    provenance["context_sources"] = _list_or_empty(provenance.get("context_sources"))
    provenance["contamination_risk"] = (
        _optional_str(provenance.get("contamination_risk")) or "low"
    )
    provenance["risk_note"] = _optional_str(provenance.get("risk_note")) or (
        "No external or prior context used."
    )
    return provenance


def _is_high_impact(item: Mapping[str, Any]) -> bool:
    if not isinstance(item, Mapping):
        raise TypeError("high-impact review items must be mappings")
    return str(item.get("impact", "high")).lower() == "high"


def _validate_max_items(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("max_items must be an integer")
    if value < 1:
        raise ValueError("max_items must be at least 1")
    return value


def _add_path_if_present(
    review_state: dict[str, Any],
    field: str,
    value: str | PathLike[str] | None,
) -> None:
    if value is not None:
        review_state[field] = str(value)


def _optional_str(value: Any) -> str | None:
    if value is None:
        return None
    return str(value)


def _optional_bool(value: Any, *, default: bool) -> bool:
    if value is None:
        return default
    return bool(value)


def _list_or_empty(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, tuple | list):
        return [_copy_jsonable(item) for item in value]
    raise TypeError("review item list fields must be lists or tuples when provided")


def _copy_jsonable(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _copy_jsonable(item) for key, item in value.items()}
    if isinstance(value, tuple | list):
        return [_copy_jsonable(item) for item in value]
    return value


__all__ = [
    "DEFAULT_MAX_ITEMS",
    "DEFAULT_PACKET_ID",
    "READY",
    "REVIEW_NEEDED",
    "SCHEMA_VERSION",
    "build_review_state",
]
