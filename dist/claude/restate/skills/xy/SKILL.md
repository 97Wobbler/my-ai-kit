---
name: "xy"
description: "Check whether a requested or relayed solution addresses the actual problem. Use for possible XY problems, solution-led directives, inferred causes, or feedback where the observation is reliable but the proposed diagnosis or fix may not be."
---

# Xy

This skill was compiled from a Skill Forge runtime-neutral spec for the
Claude Code runtime.

Source spec: private Skill Forge source (not included in distribution): `xy.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- Ask clarification questions only when they materially change the result.

# XY Check

Separate the observed symptom or goal from the proposed cause or solution. Treat the observation as evidence and the diagnosis or fix as a hypothesis.

1. Recover the underlying goal or failure from the conversation and available evidence.
2. Test multiple plausible explanations for whether the proposed solution follows from a wrong premise.
3. Intervene only when that premise is meaningfully questionable. Present the inferred problem and a better route as hypotheses, preserving the user's final choice.
4. For relayed feedback, keep the reporter's observation distinct from their inference about internal behavior.
5. If the premise looks sound, do not manufacture doubt; proceed with the request when the surrounding task permits execution.

Do not turn the check into a lecture or discard the surface request. Use `branch` when the problem is competing meanings rather than a questionable problem-to-solution inference.

## Feedback

If this plugin behaves unexpectedly, open an issue at `97Wobbler/my-ai-kit` with the plugin name, runtime, expected behavior, and observed behavior.

## Runtime Overrides

Users may invoke this skill as `/restate:xy`.
