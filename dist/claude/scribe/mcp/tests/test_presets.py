from __future__ import annotations

import sys
import unittest
from pathlib import Path

MCP_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MCP_ROOT))

from scribe_mcp.presets import (  # noqa: E402
    DEFAULT_PRESET_ORDER,
    SUPPORTED_PRESET_IDS,
    Preset,
    PresetValidationError,
    all_presets,
    get_preset,
    select_preset_ids,
    select_presets,
)


class PresetTests(unittest.TestCase):
    def test_variant_counts_map_to_stable_ordered_ids(self) -> None:
        self.assertEqual(select_preset_ids(1), ("balanced",))
        self.assertEqual(select_preset_ids(2), ("balanced", "fast"))
        self.assertEqual(select_preset_ids(3), ("balanced", "fast", "strict"))
        self.assertEqual(select_preset_ids(4), ("balanced", "fast", "strict", "no-vad"))

    def test_default_order_matches_expected_reconciliation_priority(self) -> None:
        self.assertEqual(DEFAULT_PRESET_ORDER, ("balanced", "fast", "strict", "no-vad"))
        self.assertEqual(set(DEFAULT_PRESET_ORDER), set(SUPPORTED_PRESET_IDS))

    def test_select_presets_returns_ordered_preset_objects(self) -> None:
        selected = select_presets(3)

        self.assertEqual(tuple(preset.id for preset in selected), ("balanced", "fast", "strict"))
        self.assertTrue(all(isinstance(preset, Preset) for preset in selected))

    def test_requested_ids_override_default_order_when_count_matches(self) -> None:
        self.assertEqual(select_preset_ids(2, ("strict", "fast")), ("strict", "fast"))
        self.assertEqual(
            tuple(preset.id for preset in select_presets(2, ["no-vad", "balanced"])),
            ("no-vad", "balanced"),
        )

    def test_all_presets_uses_supported_id_order(self) -> None:
        self.assertEqual(tuple(preset.id for preset in all_presets()), SUPPORTED_PRESET_IDS)

    def test_get_preset_returns_known_preset(self) -> None:
        preset = get_preset("balanced")

        self.assertEqual(preset.id, "balanced")
        self.assertEqual(preset.temperature, 0.0)
        self.assertTrue(preset.vad_filter)

    def test_transcribe_options_are_fresh_dicts(self) -> None:
        preset = get_preset("balanced")
        options = preset.to_transcribe_options()

        options["beam_size"] = 999
        options["vad_parameters"]["speech_pad_ms"] = 999

        fresh_options = preset.to_transcribe_options()
        self.assertEqual(fresh_options["beam_size"], preset.beam_size)
        self.assertEqual(fresh_options["vad_parameters"]["speech_pad_ms"], 200)

    def test_no_vad_preset_disables_vad_without_vad_parameters(self) -> None:
        options = get_preset("no-vad").to_transcribe_options()

        self.assertFalse(options["vad_filter"])
        self.assertNotIn("vad_parameters", options)

    def test_unknown_preset_raises_validation_error(self) -> None:
        with self.assertRaisesRegex(PresetValidationError, "Unknown preset id: unknown"):
            get_preset("unknown")

    def test_empty_preset_id_raises_validation_error(self) -> None:
        with self.assertRaisesRegex(PresetValidationError, "Preset id cannot be empty"):
            get_preset("")

    def test_variant_count_rejects_out_of_range_values(self) -> None:
        for variant_count in (0, 5):
            with self.subTest(variant_count=variant_count):
                with self.assertRaisesRegex(PresetValidationError, "variant_count must be between 1 and 4"):
                    select_preset_ids(variant_count)

    def test_variant_count_rejects_non_integer_values(self) -> None:
        for variant_count in (True, 1.5, "2"):
            with self.subTest(variant_count=variant_count):
                with self.assertRaisesRegex(PresetValidationError, "variant_count must be an integer"):
                    select_preset_ids(variant_count)

    def test_requested_ids_rejects_single_string(self) -> None:
        with self.assertRaisesRegex(PresetValidationError, "not a single string"):
            select_preset_ids(1, "balanced")

    def test_requested_ids_rejects_empty_sequence(self) -> None:
        with self.assertRaisesRegex(PresetValidationError, "requested_ids cannot be empty"):
            select_preset_ids(1, ())

    def test_requested_ids_rejects_unknown_values(self) -> None:
        with self.assertRaisesRegex(PresetValidationError, "Unknown preset id: custom"):
            select_preset_ids(1, ("custom",))

    def test_requested_ids_rejects_duplicate_values(self) -> None:
        with self.assertRaisesRegex(PresetValidationError, "Duplicate preset id requested: fast"):
            select_preset_ids(2, ("fast", "fast"))

    def test_requested_ids_length_must_match_variant_count(self) -> None:
        with self.assertRaisesRegex(
            PresetValidationError,
            "requested_ids length must match variant_count: expected 2, got 1",
        ):
            select_preset_ids(2, ("fast",))


if __name__ == "__main__":
    unittest.main()
