# Lucid

Lucid clarifies ambiguous requests before execution. It is separate from
`restate`: Restate checks one representative understanding, while Lucid turns
high-ambiguity requests into selectable interpretations and then captures the
chosen direction as an execution brief.

## Skills

- `branch`: Split an ambiguous request into 1-3 key ambiguity points, selectable
  options, a recommended default, and concise confirmation questions.
- `brief`: Convert selected decisions into a short execution brief with
  objective, scope, decisions, requirements, success criteria, and open
  questions.

## Invocation

Claude Code:

```text
/lucid:branch light
/lucid:branch deep
/lucid:branch interview
/lucid:brief
```

Codex CLI:

```text
$branch light
$branch deep
$branch interview
$brief
use lucid:branch
use lucid:brief
```

## Use Restate Or Lucid

| Situation | Use |
|---|---|
| You only need to confirm one understanding. | `restate` |
| The request can reasonably mean multiple things. | `lucid:branch` |
| You have made choices and need an execution handoff. | `lucid:brief` |
| You need a requirements interview. | `lucid:branch interview` |
