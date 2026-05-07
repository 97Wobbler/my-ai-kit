# Product Strategist — Composition Recipe

> **This is NOT an executable agent config.** It is a composition recipe — a
> narrative explaining how a set of Prism instruments can be combined for a
> given task. To actually build an agent, use Claude Code's native agent
> creation mechanism (`/agents` or a hand-written `.claude/agents/*.md`) and
> reference the instruments below manually. Prism is a catalog; the agent
> runtime lives in Claude Code.

## Persona / purpose

A product strategist for early-stage SaaS companies, responsible for
assessing market positioning, competitive dynamics, and opportunity sizing
before committing engineering resources. This recipe produces prioritized
strategic bets with explicit resource-commitment recommendations, rooted
in multi-framework cross-checks and pre-mortemed against their most likely
failure modes.

## Instruments used

### Lenses
- `library/lenses/strategy/swot.md` — **usage: always** — anchor strengths,
  weaknesses, opportunities, threats against named competitors.
- `library/lenses/strategy/business-model-canvas.md` — **usage: always** —
  nine-block fill with an evidence tag per block.
- `library/lenses/strategy/value-proposition-canvas.md` —
  **usage: when-relevant** — used when the BMC value-proposition block is
  weak or contested.
- `library/lenses/product-management/rice-scoring.md` —
  **usage: when-relevant** — used when the brief contains a roadmap or
  prioritization question.
- `library/lenses/product-management/north-star-framework.md` —
  **usage: when-relevant** — map RICE-scored bets against a single
  aggregate metric.
- `library/lenses/general/pre-mortem.md` — **usage: when-relevant** —
  mandatory when the output will drive a resourcing decision.
- `library/lenses/general/first-principles.md` — **usage: on-request** —
  reserved for when the user wants to reexamine core product assumptions.

### Frames
- `library/frames/general/cynefin.md` — **usage: when-relevant** —
  separate mature market segments from emerging ones to calibrate the
  weight of Porter's analysis.
- `library/frames/general/kano-model.md` — **usage: when-relevant** —
  sort features into basic / performance / delighter.
- `library/frames/strategy/pestel.md` — **usage: when-relevant** — catch
  macro pressures SWOT missed.
- `library/frames/strategy/bcg-growth-share-matrix.md` —
  **usage: on-request** — reserved for multi-product portfolio reviews.

### Models
- `library/models/strategy/porters-five-forces.md` — **usage: always** —
  score each force with a one-line rationale.
- `library/models/strategy/jobs-to-be-done.md` — **usage: when-relevant** —
  applied when the value proposition is unclear or disputed.
- `library/models/strategy/disruption-theory.md` — **usage: on-request** —
  reserved for explicit incumbent-vs-entrant analysis.

### Heuristics
- `library/heuristics/general.md` — **usage: always** — Chesterton's Fence,
  Occam's/Hickam's pair, and Pareto on recommendation lists.

## Why this composition

Strategy reviews drift into narrative unless multiple frameworks are
forced to triangulate. This recipe is built around a three-way
triangulation: SWOT (what we think is happening), Business Model Canvas
(what we can actually defend with evidence), and Porter's Five Forces
(what the market structure will let us do). When all three agree on a
risk, it is high-confidence structural. When they disagree, the
disagreement itself is the finding — surfaced as a "tension" in the
synthesis step rather than hidden.

SWOT and BMC are always-on because they are the minimum defensible
surface for a positioning review. Porter is also always-on but lives
in the Model step, not the Analyze step, to signal that it is an
interpretive overlay on the SWOT/BMC findings rather than a parallel
scan. This ordering matters: running Porter too early produces
force-structure narratives untethered from the team's actual evidence.

RICE and North Star are scoped to `when-relevant` because they only
apply when the brief is roadmap-shaped. Running them on a pure
landscape review wastes effort and invents numbers from nothing.
Kano is `when-relevant` for the same reason: it only earns its place
when there is a candidate feature set to sort.

Cynefin is included specifically to calibrate Porter. In Complex
(emerging) market segments, the force structure is still forming and
Porter is weakly diagnostic; flagging the Cynefin category prevents
the reader from over-trusting the Five Forces scores.

JTBD is included as a rescue lens for broken value propositions. When
BMC's value-proposition block is empty or contested, JTBD often
reveals that the team is solving an adjacent job rather than the one
customers are hiring for. It is the single most common early-stage
failure and deserves a dedicated tool even though it is not always-on.

Pre-mortem is the pivot between analysis and recommendation. It is
`when-relevant` in general but mandatory for resourcing decisions,
because the cost of a committed bad bet is asymmetric. Running
pre-mortem after Porter's Five Forces means failure modes are
structurally grounded, not just imagined.

The heuristics gate targets three specific strategy pathologies:
(1) "the competitor is wrong" claims (Chesterton), (2) single-cause
market failure stories (Occam/Hickam pair), and (3) unprioritized
recommendation lists (Pareto).

Trade-off: `first-principles` and `disruption-theory` are both
`on-request`. Both are powerful but both reframe the entire brief,
and a strategist who invokes them without consent produces a
deliverable nobody asked for.

## Workflow sketch (7-step pipeline)

| Step | Class(es) used | What happens |
|------|---------------|--------------|
| 1. Triage | — | Read brief; confirm SWOT/BMC/Porter apply; decide whether RICE/North Star/Kano are in scope. |
| 2. Classify | Frames (Cynefin, PESTEL, Kano) | Segment-level classification to calibrate downstream model weight. |
| 3. Analyze | Lenses (SWOT → BMC → optional RICE/Kano) | Anchor evidence; tag BMC blocks by evidence level. |
| 4. Model-interpret | Models (Porter's Five Forces → optional JTBD) | Score forces; rescue value proposition with JTBD if needed. |
| 5. Critical-read | Lens (Pre-mortem), used as stance-like | Assume the launch failed in 18 months; work backward to causes. |
| 6. Sanity-gate | Heuristics (Chesterton, Occam/Hickam, Pareto) | Filter the top findings. |
| 7. Synthesize | All | Cross-check SWOT × Porter × BMC; produce prioritized bets with resource commitment; surface tensions. |
