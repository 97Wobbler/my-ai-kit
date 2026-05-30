<!-- Rendering rule: Do not narrate routing or file-loading decisions to the user — render the content below directly, without meta commentary about which intent was classified or which file was opened. -->

# Prism quick reference

## Claude Code

- `/prism:prism` — show what Prism is and how to use it (loads `about.md`).
- `/prism:prism {framework name}` — create a new instrument via a short
  interview. Example: `/prism:prism CVSS`, `/prism:prism 칸반 방식`, `/prism:prism PASTA
  threat modeling`. If the request is specific, generation starts
  immediately; if it's ambiguous, expect up to 3 clarifying questions.
- `/prism:prism help` — this page.
- `/prism:search security lens` — browse matching catalog entries.
- `/prism:fetch stride owasp-top10` — prepare selected instruments for a
  subagent prompt.
- `/prism:debate --review path/to/doc.md` — run instrumented multi-agent review.

## Codex

- `$prism` or `use prism:prism` — show what Prism is and how to use it.
- `$prism CVSS` or `use prism:prism CVSS` — create a new instrument via a
  short interview.
- `$prism help` or `use prism:prism help` — this page.
- `$search security lens` or `use prism:search security lens` — browse
  matching catalog entries.
- `$fetch stride owasp-top10` or `use prism:fetch stride owasp-top10` —
  prepare selected instruments for a subagent prompt.
- `$debate --review path/to/doc.md` or `use prism:debate --review
  path/to/doc.md` — run instrumented multi-agent review.

## For catalog browsing

Use the `search` skill for queries like "what lenses exist for security?"
or "show me frames for product strategy".

## For loading instruments into subagents

Use the `fetch` skill with one or more instrument names to get a ready-made
instruction block for subagent prompts.

## For multi-agent debate

Use the `debate` skill to have multiple agent personas analyze a document,
brainstorm ideas, or converge on a solution through structured rounds.

Three modes:
- `--review` — multi-perspective analysis with consensus judgment
- `--ideate` — divergent brainstorming (no convergence pressure)
- `--solve` — solution proposals with convergence toward a best answer

Omit the flag and the skill infers the mode from context.
Prism instruments (stances, lenses) can serve as expertise sources for
debate participants.

## For batch generation

That's outside this skill: `python3 scripts/prism_batch.py` handles
bulk generation from a prompt template.

## 5 classes at a glance

- **Lens (렌즈)** — executable procedure with input, output template, and
  confidence signal. All four criteria required.
- **Frame (분류 프레임)** — taxonomy or classification matrix: categories
  plus discriminating criteria, no "next step" procedure.
- **Model (이론 모델)** — theoretical or predictive model with variables,
  relationships, and predictions, but no built-in application steps.
- **Stance (비판적 관점)** — interpretive commitment expressed as guiding
  questions about what is worth looking for.
- **Heuristic (원리 / 격언)** — single-rule aphorism used as a check
  inside a lens or as a sanity gate before synthesis.

## Storage layers

Instruments live in 3 layers: bundle (read-only), global, project.
Precedence: project > global > bundle.
