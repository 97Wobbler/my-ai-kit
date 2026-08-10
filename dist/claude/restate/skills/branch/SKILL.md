---
name: "branch"
description: "Split a request, statement, policy, or design into materially different interpretations. Use when ambiguity could change the action, scope, or conclusion, or when the user asks to branch, clarify meanings, compare readings, or identify ambiguity."
---

# Branch

This skill was compiled from a Skill Forge runtime-neutral spec for the
Claude Code runtime.

Source spec: private Skill Forge source (not included in distribution): `branch.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- Ask clarification questions only when they materially change the result.

# Branch

Expose only ambiguity that would materially change what happens next.

1. Infer the strongest reading from the nearby context.
2. Test whether another reading remains meaningfully plausible, including when the statement may travel outside its original context.
3. Surface only alternatives that would change action, scope, or conclusion. Do not manufacture branches to fill a format.
4. Recommend the strongest default when evidence supports one.
5. Ask the minimum question needed to distinguish remaining blocking readings. If the ambiguity is non-blocking, state the assumption and continue when the surrounding task permits execution.

Use prose, a short list, or a compact comparison according to the number of real branches. Do not require mode labels or tables. Keep low-confidence readings visibly tentative.

Use `restate` when one representative understanding only needs confirmation. Use `xy` when the wording is clear but the proposed solution may rest on a wrong premise.

## Feedback

If this plugin behaves unexpectedly, open an issue at `97Wobbler/my-ai-kit` with the plugin name, runtime, expected behavior, and observed behavior.

## Runtime Overrides

Users may invoke this skill as `/restate:branch`.
