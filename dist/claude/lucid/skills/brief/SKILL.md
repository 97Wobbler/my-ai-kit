---
name: "brief"
description: "Create an execution-ready brief from selected intent and decisions. Use after lucid:branch choices are made, after a long clarification thread, or when the user asks to create a brief, freeze decisions, summarize agreement, or prepare implementation, documentation, PRD, or task planning input."
---

# Brief

This skill was compiled from a Skill Forge runtime-neutral spec for the
Claude Code runtime.

Source spec: private Skill Forge source (not included in distribution): `brief.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- Ask clarification questions only when they materially change the result.

## Purpose

Use this skill to turn selected intent and decisions into a short execution
brief. The brief should be useful to a later implementer, writer, planner, or
reviewer without requiring them to re-read the whole conversation.

`brief` closes clarification work. It does not continue broad exploration. If
major choices are still unresolved, use `lucid:branch` first or mark the brief
as blocked.

## Relationship To Branch And Restate

Use `branch` when the user still needs to choose between meanings or execution
paths. Use `brief` when enough choices have been made to capture the work as an
execution handoff.

Use `restate` only when the user wants a one-understanding confirmation rather
than a decision record.

## Stop Condition

Create the brief when all of these are true:

- the objective can be written in one sentence;
- included and excluded scope can be separated at a minimal level;
- blocking open questions can be distinguished from non-blocking open questions;
- at least one success criterion is known.

The brief does not need to remove all uncertainty. It must classify uncertainty.

## Output Language

Respond in the user's language unless they ask otherwise.

## Output Format

Use this structure:

```markdown
## Brief

### Execution Status
- Status: <ready | ready_with_open_questions | blocked>
- Reason: <why execution can start or why it is blocked>

### Objective
<what this work is trying to accomplish>

### Scope
- Included: <included scope>
- Excluded: <excluded scope>

### Decisions
| Decision | Choice | Reason |
|---|---|---|
| <decision item> | <choice> | <reason> |

### Requirements
| Priority | Requirement | Acceptance Standard |
|---|---|---|
| P0 | <must-have> | <how to judge it> |
| P1 | <nice-to-have> | <how to judge it> |

### Success Criteria
- <completion criterion>

### Open Questions
| Type | Question | Execution Impact |
|---|---|---|
| blocking | <question that must be answered first> | <why it blocks> |
| non-blocking | <question that can be answered during execution> | <impact or default> |

### Recommended Next Step
<next action>
```

## Status Rules

- Use `ready` when the work can proceed without meaningful unresolved decisions.
- Use `ready_with_open_questions` when execution can start but some
  non-blocking choices remain.
- Use `blocked` when a missing decision prevents a responsible next action.

## Quality Rules

- Do not create new decisions and present them as agreed facts.
- When recommending a default, label it as a recommendation.
- Do not hide uncertainty. Classify it.
- Keep the brief shorter than a PRD.
- Include both inclusion and exclusion scope.
- Include blocking and non-blocking open questions as separate rows when both
  exist.
- If there are no open questions of a type, write `None` for that row rather
  than deleting the section.

## Runtime Overrides

Plugin skill invocation is namespaced. Users may call this skill as `/lucid:brief`.
