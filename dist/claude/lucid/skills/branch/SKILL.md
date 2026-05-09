---
name: "branch"
description: "Split ambiguous user requests into selectable interpretations and minimal confirmation questions. Use when a request has multiple plausible meanings, unclear goals, scope, constraints, or outputs, or when the user asks to branch, clarify options, identify ambiguity, or run a requirements interview."
---

# Branch

This skill was compiled from a Skill Forge runtime-neutral spec for the
Claude Code runtime.

Source spec: private Skill Forge source (not included in distribution): `branch.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- Use Claude Code's native blocking question flow when clarification is required.

## Purpose

Use this skill to turn ambiguity into a small set of choices the user can
actually make. The goal is not exhaustive analysis. The goal is a better next
decision.

`branch` combines two jobs:

- surface the main plausible interpretations of a request;
- convert those interpretations into minimal questions with selectable options.

Use `branch` before expensive implementation, public documentation, planning,
policy work, prompt design, or skill/plugin design when a mistaken
interpretation would be costly.

## Relationship To Restate

Use `restate` when one representative understanding is enough and the user only
needs confirmation. Use `branch` when the request can reasonably lead to
different execution paths.

Do not add an echo-style single restatement flow here. That belongs to
`restate`.

## Mode Selection

`branch` has three modes. The mode is natural-language input, not a separate
parser.

- `light`: default mode. Use for low or medium ambiguity. Cover 1-3 ambiguity
  points, with 2-3 options per point.
- `deep`: use for high ambiguity, high-cost work, conflicting goals, public
  outputs, implementation plans, policy decisions, prompt design, or skill and
  plugin design. Cover the important branches only, up to 5 major branches.
- `interview`: use when facts, preferences, or constraints are missing and
  options alone would be guesswork. Ask 1-3 questions at a time and carry
  forward the user's answers.

If the user names a mode, follow it. If the user mixes incompatible modes, ask
one concise question to choose the mode before continuing.

If no mode is named, start with `light`. Propose or use `deep` when the risk of
misinterpretation is high. Switch to `interview` when a reasonable default would
depend on missing information from the user.

## Output Language

Respond in the user's language unless they ask otherwise.

## Standard Output

For `light` and `deep`, use this structure:

```markdown
## Branch

### Judgment
This request should be handled in <light/deep> mode because <brief reason>.

### Core Ambiguities
1. <ambiguity>
2. <ambiguity>

### Options

#### 1. <ambiguity name>
| Option | Interpretation | If We Proceed This Way | Risk |
|---|---|---|---|
| A | <interpretation> | <execution direction> | <risk> |
| B | <interpretation> | <execution direction> | <risk> |

### Recommended Default
<reasonable default and why. Clearly mark points the user still must choose.>

### Confirmation Questions
<1-3 questions that can be answered by choosing A/B/C or a short mixed answer.>
```

## Interview Output

For `interview`, use this structure:

```markdown
## Branch Interview

### Confirmed So Far
- <decision>

### Remaining Decisions
- <decision needed>

### Questions
1. <question>
   - A. <option>
   - B. <option>
   - C. <option>
```

Ask only 1-3 questions in each interview turn.

## Quality Rules

- Do not invent weak possibilities just to fill a table.
- Options must be choices the user can actually make.
- Keep questions to 1-3 at a time.
- In `light`, avoid long philosophical analysis.
- In `deep`, limit output to the branches that would materially change the
  work.
- If evidence for an interpretation is weak, label it as low confidence.
- Clearly separate blocking ambiguities from non-blocking ones.
- When the user's choices are sufficient for execution, suggest `lucid:brief`
  as the next step.

## Completion Criteria

The request is ready to move to `lucid:brief` when:

- the user chose one option, or a compatible mix of options, for the major
  ambiguities;
- unresolved items can be classified as blocking or non-blocking;
- the selected choices do not conflict with each other.

If the user gives a partial or mixed answer and a blocking ambiguity remains,
ask 1-3 follow-up questions. If only non-blocking ambiguity remains, pass it to
`brief` as non-blocking open questions.

## Runtime Overrides

Plugin skill invocation is namespaced. Users may call this skill as `/lucid:branch light`, `/lucid:branch deep`, or `/lucid:branch interview`.
