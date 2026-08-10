---
name: "handoff"
description: "Create a copy-ready handoff of current work for another session, parent agent, or recipient. Use when the user asks to hand off, transfer, resume elsewhere, report side-session work, or package decisions and next actions."
---

# Handoff

This skill was compiled from a Skill Forge runtime-neutral spec for the
Claude Code runtime.

Source spec: private Skill Forge source (not included in distribution): `handoff.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- Run the relevant validation checks before reporting completion.

# Handoff

Choose the depth from the receiving context:

- **Relay** transfers only this session's delta when a parent or recipient already knows the larger context.
- **Resume** supplies enough background for a new session or person to continue independently.

Recover the goal, changes, reasons, current state, evidence, risks, and next actions. Preserve concrete paths, symbols, commands, errors, commits, URLs, and validation results only when they help continuation. Keep facts, decisions, hypotheses, unresolved questions, and recommendations distinct. Preserve observations separately from inferred causes or proposed solutions.

For Relay, use a compact paragraph or 3-5 bullets. For Resume, use only the headings needed for independent entry. Include a reliable session identifier only when useful.

Return the handoff itself without preamble. Do not put drafting exclusions, omission instructions, inaccessible internal references, or unexplained private taxonomy into the artifact. Keep negative constraints only when they materially affect the recipient's interpretation, behavior, safety, or scope.

## Feedback

If this plugin behaves unexpectedly, open an issue at `97Wobbler/my-ai-kit` with the plugin name, runtime, expected behavior, and observed behavior.

## Runtime Overrides

Use reliable native session or conversation identifiers only when available and useful; never guess them.
