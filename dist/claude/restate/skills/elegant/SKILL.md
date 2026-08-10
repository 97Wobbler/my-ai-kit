---
name: "elegant"
description: "Re-weigh a proposed plan or design for the best balance between change cost and effect. Use when the user asks whether a path is optimal, elegant, too complex, too defensive, or worth reconsidering before commitment."
---

# Elegant

This skill was compiled from a Skill Forge runtime-neutral spec for the
Claude Code runtime.

Source spec: private Skill Forge source (not included in distribution): `elegant.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- No special runtime capabilities are required.

# Elegant Check

Treat a request to reconsider as a signal to re-weigh, not as a command either to reverse course or defend the existing plan.

Assess whether the proposal reaches the best balance between minimal change and maximal effect. Check for a simpler path, unnecessary machinery, insufficient coverage, and structures that reflect the first idea rather than a real constraint such as performance, scale, safety, or consistency.

- If a genuinely better path emerges, change the recommendation substantively.
- If the existing path remains best, keep it and give concrete reasons.
- State the conclusion plainly; neither agreement nor resistance is the goal.

Review the whole plan without replaying interpretation or diagnosis unless those gaps materially affect the judgment.

## Feedback

If this plugin behaves unexpectedly, open an issue at `97Wobbler/my-ai-kit` with the plugin name, runtime, expected behavior, and observed behavior.

## Runtime Overrides

Users may invoke this skill as `/restate:elegant`.
