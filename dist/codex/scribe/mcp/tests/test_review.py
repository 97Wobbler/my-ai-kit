from __future__ import annotations

import sys
import unittest
from pathlib import Path

MCP_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MCP_ROOT))

from scribe_mcp.review import (  # noqa: E402
    READY,
    REVIEW_NEEDED,
    SCHEMA_VERSION,
    build_review_state,
)


class ReviewStateTests(unittest.TestCase):
    def test_no_high_impact_items_returns_ready_without_user_gate(self) -> None:
        review_state = build_review_state()

        self.assertEqual(review_state["schema_version"], SCHEMA_VERSION)
        self.assertEqual(review_state["state"], READY)
        self.assertFalse(review_state["requires_user_response"])
        self.assertEqual(review_state["reason"], "no_high_impact_items")
        self.assertEqual(review_state["clarification_packet"]["items"], [])
        self.assertEqual(review_state["resolution"]["status"], "resolved")

    def test_high_impact_items_return_review_needed_packet(self) -> None:
        review_state = build_review_state(
            (
                {
                    "id": "term-001",
                    "kind": "name_confirmation",
                    "impact": "high",
                    "question": "Confirm this product name.",
                    "candidate": "Scribe Canon",
                    "alternatives": ["Scribe Cannon"],
                    "evidence": [
                        {
                            "source": "transcript_span",
                            "span_ref": "balanced.md#approx-00:01:00",
                            "excerpt": "Scribe Canon",
                        }
                    ],
                },
            )
        )

        self.assertEqual(review_state["state"], REVIEW_NEEDED)
        self.assertTrue(review_state["requires_user_response"])
        self.assertEqual(review_state["reason"], "high_impact_uncertainty")
        self.assertEqual(review_state["resolution"]["status"], "unresolved")

        packet = review_state["clarification_packet"]
        self.assertEqual(packet["packet_id"], "review-001")
        self.assertEqual(packet["max_items"], 5)
        self.assertEqual(len(packet["items"]), 1)

        item = packet["items"][0]
        self.assertEqual(item["id"], "term-001")
        self.assertEqual(item["kind"], "name_confirmation")
        self.assertEqual(item["impact"], "high")
        self.assertEqual(item["question"], "Confirm this product name.")
        self.assertEqual(item["candidate"], "Scribe Canon")
        self.assertEqual(item["alternatives"], ["Scribe Cannon"])
        self.assertTrue(item["blocks_final_completion"])
        self.assertEqual(item["default_if_unanswered"], "leave_as_transcribed")

    def test_packet_items_are_capped_and_report_omitted_count(self) -> None:
        review_state = build_review_state(
            tuple(
                {
                    "id": f"term-{index:03d}",
                    "impact": "high",
                    "candidate": f"candidate {index}",
                }
                for index in range(1, 5)
            ),
            max_items=2,
        )

        packet = review_state["clarification_packet"]
        self.assertEqual(packet["max_items"], 2)
        self.assertEqual([item["id"] for item in packet["items"]], ["term-001", "term-002"])
        self.assertEqual(packet["omitted_item_count"], 2)
        self.assertTrue(review_state["requires_user_response"])

    def test_artifact_paths_are_included_when_available(self) -> None:
        review_state = build_review_state(
            transcript_path=Path("transcripts/run-1/variants/balanced.md"),
            review_path="transcripts/run-1/transcript-review.md",
            manifest_path="transcripts/run-1/manifest.json",
        )

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

    def test_provenance_defaults_are_added(self) -> None:
        review_state = build_review_state(({"impact": "high", "candidate": "term"},))
        provenance = review_state["clarification_packet"]["items"][0]["provenance"]

        self.assertEqual(provenance["candidate_sources"], ["transcript_evidence"])
        self.assertFalse(provenance["used_context"])
        self.assertEqual(provenance["context_sources"], [])
        self.assertEqual(provenance["contamination_risk"], "low")
        self.assertEqual(provenance["risk_note"], "No external or prior context used.")

    def test_provenance_is_preserved_with_missing_defaults_filled(self) -> None:
        review_state = build_review_state(
            (
                {
                    "impact": "high",
                    "candidate": "domain term",
                    "provenance": {
                        "candidate_sources": [
                            "transcript_evidence",
                            "current_workspace_context",
                        ],
                        "used_context": True,
                        "context_sources": [
                            {
                                "type": "current_workspace_context",
                                "description": "Visible repository name.",
                            }
                        ],
                        "contamination_risk": "medium",
                        "risk_note": "Workspace context helped choose casing.",
                    },
                },
            )
        )

        provenance = review_state["clarification_packet"]["items"][0]["provenance"]
        self.assertEqual(
            provenance["candidate_sources"],
            ["transcript_evidence", "current_workspace_context"],
        )
        self.assertTrue(provenance["used_context"])
        self.assertEqual(
            provenance["context_sources"],
            [
                {
                    "type": "current_workspace_context",
                    "description": "Visible repository name.",
                }
            ],
        )
        self.assertEqual(provenance["contamination_risk"], "medium")
        self.assertEqual(provenance["risk_note"], "Workspace context helped choose casing.")


if __name__ == "__main__":
    unittest.main()
