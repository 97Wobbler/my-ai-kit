# Curriculum Reviewer — Composition Recipe

> **This is NOT an executable agent config.** It is a composition recipe — a
> narrative explaining how a set of Prism instruments can be combined for a
> given task. To actually build an agent, use Claude Code's native agent
> creation mechanism (`/agents` or a hand-written `.claude/agents/*.md`) and
> reference the instruments below manually. Prism is a catalog; the agent
> runtime lives in Claude Code.

## Persona / purpose

A curriculum reviewer for Korean K-12 educational materials and AI-generated
problems, responsible for verifying alignment with national achievement
standards (성취기준) and appropriate cognitive demand. This recipe produces
per-item verdicts grounded in the standard's text, with cognitive-level
distributions and a distinction between item-level fixes and systemic
curriculum issues.

## Instruments used

### Lenses
- `library/lenses/education/achievement-standard-alignment.md` —
  **usage: always** — the spine of the review; the standard defines what
  "correct" means.
- `library/lenses/education/blooms-taxonomy.md` — **usage: always** — scan
  objectives, content, and assessment for cognitive-level distribution and
  misalignment.
- `library/lenses/education/cognitive-load-theory.md` —
  **usage: when-relevant** — applied to material a student learns from
  directly (lessons, worked examples, UI), not to isolated assessment items.
- `library/lenses/general/socratic-method.md` — **usage: on-request** —
  reserved for deep stress-testing of a specific claim in the material.

### Frames
- `library/frames/general/cynefin.md` — **usage: when-relevant** — separate
  well-defined procedural content (Clear / Complicated) from open-ended
  inquiry or project-based content (Complex), so cognitive-load findings
  are read correctly.

### Heuristics
- `library/heuristics/general.md` — **usage: always** — Chesterton's Fence
  and Pareto applied as a sanity gate on recommendations.

## Why this composition

Achievement-standard-alignment is not negotiable: without the standard,
there is no ground truth for "aligned." It runs first and anchors every
subsequent finding. Putting it anywhere else in the pipeline allows the
reviewer to drift into aesthetic preferences dressed up as rigor.

Bloom's taxonomy is paired with alignment because the two catch
different failure modes. Alignment catches "wrong content" (the item
doesn't exercise the 기능 요소 the standard asks for). Bloom catches
"right content, wrong level" (the item technically covers the topic
but asks for recall when the standard asks for application). A single
lens cannot do both jobs; the cross-check between them is what makes
the review diagnostic rather than descriptive.

Cognitive Load Theory is `when-relevant` on purpose. For an isolated
assessment item it produces noise — intrinsic load is whatever the
standard requires. For a lesson or worked example it is the only lens
that distinguishes good difficulty from bad difficulty. The recipe
scopes it correctly rather than running it everywhere.

Cynefin's role here is subtle: it prevents a common reviewer mistake
where high intrinsic load in project-based (Complex) material is
flagged as a defect when it is in fact the pedagogical intent.
Classifying first gives the cognitive-load pass the right calibration.

The heuristic gate is narrowed to two tools. Chesterton's Fence is
aimed at the specific temptation to recommend removing scaffolding
(sentence frames, partial solutions, hints) — scaffolding often exists
for reasons invisible on the page. Pareto forces recommendation lists
to prioritize rather than sprawl; for K-12 materials, five "fix this"
items are worthless if one item is actually load-bearing.

Trade-off: `socratic-method` stays `on-request`. Running it on every
review would be exhausting and would produce suspicion-first critiques
that miss the material's actual goals.

## Workflow sketch (7-step pipeline)

| Step | Class(es) used | What happens |
|------|---------------|--------------|
| 1. Triage | — | Identify the target 성취기준; confirm alignment + Bloom apply; decide whether Cognitive Load Theory is in scope. |
| 2. Classify | Frames (Cynefin) | Sort materials into Clear/Complicated/Complex; Complex material may have high intrinsic load by design. |
| 3. Analyze | Lenses (Alignment → Bloom → optional CLT) | Per-item verdicts; cite 성취기준 해설 on borderline alignment calls. |
| 4. Model-interpret | — | Not used by this recipe. |
| 5. Critical-read | — | Not used by this recipe. |
| 6. Sanity-gate | Heuristics (Chesterton's Fence, Pareto) | Filter "remove the scaffolding" recommendations; compress the recommendation list to the load-bearing 1–3. |
| 7. Synthesize | All | Cross-check alignment failures against Bloom mismatches; cluster by root cause; separate item-level fixes from systemic curriculum issues. |
