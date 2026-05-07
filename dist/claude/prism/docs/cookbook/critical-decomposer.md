# Critical Decomposer — Composition Recipe

> **This is NOT an executable agent config.** It is a composition recipe — a
> narrative explaining how a set of Prism instruments can be combined for a
> given task. To actually build an agent, use Claude Code's native agent
> creation mechanism (`/agents` or a hand-written `.claude/agents/*.md`) and
> reference the instruments below manually. Prism is a catalog; the agent
> runtime lives in Claude Code.

## Persona / purpose

A philosophical analyst that takes a single claim, statement, or assertion
and performs a structured critical decomposition: surfacing what the
statement actually says, which alternative readings it sustains, what
concepts carry the argumentative load, what it silently presupposes, how
its argument holds together, and where it is most vulnerable. The recipe
produces an evaluation that is attribution-blind, morally bracketed, and
operationally specific — suitable for argument audits, editorial review of
opinion writing, adversarial preparation in policy or strategy, and
teaching critical reading.

## Instruments used

### Lenses

Applied in sequence in the **analyze** step.

- `library/lenses/philosophy/multi-layer-reading.md` — **usage: always** —
  first pass. Captures the literal surface and enumerates candidate
  readings (semantic, figurative, performative, contextual) with per-reading
  plausibility, so downstream analysis targets the right claim rather than
  the one most convenient to the analyst.
- `library/lenses/philosophy/conceptual-analysis.md` — **usage: always** —
  for each Reading, extracts key concepts and pairs a charitable definition
  with a critical one, maps boundary and edge cases, and flags unfalsifiable
  or slippery terms.
- `library/lenses/philosophy/presupposition-analysis.md` — **usage: always** —
  walks five categories of hidden assumption (definitional, empirical,
  structural, normative, scope), grading plausibility and failure impact.
- `library/lenses/philosophy/toulmin-argument-model.md` — **usage: always** —
  reconstructs the claim's structure into claim, grounds, warrant, backing,
  qualifier, and rebuttal, then stress-tests each link. Covers the argument-
  reconstruction + validity/soundness work that the original Critical
  Decomposition engine handled in its Phase 4.

### Stances

Applied in the **critical-read** step, in parallel with the lens findings.

- `library/stances/philosophy/analytic-critique.md` — **usage: always** —
  holds the decomposer's interpretive commitments: moral evaluation is
  bracketed, analysis starts neutrally (no pre-assumed truth or falsity),
  attribution is recorded but never weighed as evidence, and claims that
  are under-specified trigger a context request rather than an invented
  reconstruction.

### Heuristics

Applied in the **sanity-gate** step.

- `library/heuristics/general.md` — **usage: always** — Occam's Razor,
  Hanlon's Razor, Chesterton's Fence, Hickam's Dictum, and related rules
  of thumb. Used here to catch surface-level reasoning failures in the
  synthesis (single-cause attribution of compound effects, exotic theories
  when plain ones fit, ripping out load-bearing premises without asking
  why they were there).
- `library/heuristics/philosophy/*.md` — **usage: when-relevant** —
  domain-specific checks: `is-ought-problem.md` and
  `naturalistic-fallacy.md` for claims mixing descriptive and normative
  registers, `russells-teapot.md` for unfalsifiable existence claims,
  `ought-implies-can.md` for normative claims whose feasibility is doubted,
  `ship-of-theseus.md` for identity-through-change claims. Only invoke the
  members of this bundle whose conditions the claim actually triggers.

## Why this composition

**The lens ordering is load-bearing, not decorative.** Running the four
lenses in the order multi-layer-reading → conceptual-analysis →
presupposition-analysis → toulmin enforces a specific dependency chain.
Interpretation has to be fixed before concepts can be analyzed, because a
term's meaning shifts across Readings. Concepts have to be pinned before
presuppositions can be surfaced, because many silent assumptions ride on
a particular meaning of a key term. And presuppositions have to be
catalogued before argument reconstruction, because Toulmin's grounds and
warrant frequently are exactly those unstated presuppositions. Running
toulmin first would have the analyst reconstruct a skeleton of a claim
whose body hasn't been made inspectable yet.

**The stance cannot be folded into the lenses.** The four commitments
carried by `analytic-critique` — bracket morality, start neutral, separate
attribution from evidence, refuse to analyze under-specified claims — are
not procedures. They are dispositions that shape how every lens is run.
Moral bracketing affects how conceptual-analysis handles charged terms;
attribution/evidence separation changes what toulmin accepts as backing;
the vagueness demand determines whether multi-layer-reading proceeds at
all. Writing these commitments into each lens would duplicate them four
times and obscure the single interpretive posture they jointly express.
Keeping them in a stance, run at the critical-read step, makes the
posture a visible object of analysis itself.

**The Toulmin reuse is deliberate.** The original Critical Decomposition
engine's Phase 4 (Argument Reconstruction — premises, conclusion, logical
form, validity, soundness) is functionally the same work that
`toulmin-argument-model` already does: it externalizes the argument's
structure, tests whether grounds connect to claim through a warrant, and
names the backing. Creating a `phase-4-argument-reconstruction.md` lens
would be a duplicate in all but name. Reusing Toulmin lets the recipe
inherit a well-tested procedure and its existing evaluation criteria.

**Why Phase 5 gets no dedicated lens.** The original Phase 5 (Verdict &
Weak Points — strongest version, top vulnerabilities, what would change
your mind) is not an analytical procedure over the claim; it is a
synthesis over the *outputs* of Phases 1–4. It has no independent input
type and no new analytical move — it selects, ranks, and summarizes what
earlier phases produced. That is precisely what the **synthesize** step
of the Prism workflow is for. Phase 5 therefore survives as a
customization of synthesize output, not as a fifth lens (see Step 7 below).

**Heuristics sit downstream of the lenses, not inside them.** The general
bundle is cheap to run and catches common reasoning failures in the
synthesis — exactly the point where surface-level traps (single-cause
framing, removing checks without understanding why they exist) tend to
enter. The philosophy bundle is held at `when-relevant` because its
entries are domain-specific: running `is-ought-problem` against a purely
descriptive empirical claim wastes attention; running it against a claim
that smuggles "ought" inside "is" is exactly the right move. The analyst
picks from the bundle based on what the lenses surfaced, rather than
sweeping all of it over every claim.

## Workflow sketch (7-step pipeline)

| Step | Class(es) used | What happens |
|------|---------------|--------------|
| 1. Triage | — | Confirm the input is a claim, assertion, or short argument (1–3 sentences typical). Confirm it is specified enough to analyze; if not, `analytic-critique`'s vagueness commitment triggers a context request and the pipeline pauses until context is provided. |
| 2. Classify | — | Skipped. `multi-layer-reading` handles interpretive branching internally at the start of analyze, so no separate frame is needed. |
| 3. Analyze | Lenses (multi-layer-reading → conceptual-analysis → presupposition-analysis → toulmin-argument-model) | Run lenses in order. **Orchestration note:** if `multi-layer-reading` returns multiple high-plausibility Readings ("interpretively underdetermined"), each downstream lens must be run **separately per Reading**, and the outputs carried forward in parallel. The current Prism workflow does not execute conditional branching automatically; the analyst is responsible for honoring the branch manually. When Readings converge on one, the other three lenses run once. |
| 4. Model-interpret | — | Not used by this recipe. |
| 5. Critical-read | Stances (analytic-critique) | Apply `analytic-critique` to both the input and the intermediate lens outputs. The stance checks whether moral bracketing held, whether the neutral-start discipline was respected, whether attribution crept into evaluation, and whether the analysis is engaging with what the claim actually says versus a reconstruction. |
| 6. Sanity-gate | Heuristics (general bundle always; philosophy bundle when-relevant) | Walk the general heuristics over the top findings. Then, based on what the lenses surfaced, selectively apply the philosophy bundle: is-ought / naturalistic-fallacy for mixed descriptive-normative claims, russells-teapot for unfalsifiable existence claims, ought-implies-can for feasibility-doubted normative claims, ship-of-theseus for identity-through-change claims. |
| 7. Synthesize | All | **Customized for this recipe.** Standard synthesis cross-checks findings across classes; the Critical Decomposer adds three mandatory output fields absorbed from the original Phase 5: **strongest version** (the most defensible reconstruction of the claim, charitably stated), **critical vulnerabilities** (the two or three points at which the claim is most likely to break down, drawn from weakest presuppositions, slippery concepts, and stress-test failures), and **what would change your mind** (specific evidence or argument that would make the claim more or less convincing). |

### Step 7 example output block

```
## Synthesis

### Strongest version
<The claim charitably reconstructed in neutral language: the best defensible
form of what it is asserting, under the winning Reading from step 3.>

### Critical vulnerabilities (top 2–3)
1. <vulnerability 1 — drawn from a weak load-bearing presupposition, a
   slippery concept, or a missing/assumed link in the Toulmin chain; name
   the source lens>
2. <vulnerability 2 — as above>
3. <vulnerability 3 — optional; only if genuinely distinct from 1 and 2>

### What would change your mind
- Evidence that would strengthen the claim: <specific, observable>
- Evidence that would weaken or refute the claim: <specific, observable>

### Confidence
<Weighted from the four lens confidences and the stance's specification
judgment. High only when Readings converged, key concepts were pinned,
load-bearing presuppositions were at most contested, and the Toulmin chain
held without missing links.>
```

## Reconstruction note — why this is a recipe, not a skill

The source for this recipe is `temp/decomposer.md`, a five-phase Critical
Decomposition system prompt that, read at face value, looks like a
candidate for a standalone Prism skill: a single, self-contained
analytical pipeline that could be dropped into an agent as one unit.

On closer inspection, it is not. Phases 1 through 4 are already
recognizable as reusable analytical procedures that the Prism library
either contains or can cleanly express: Phase 1 is the hermeneutic move
of generating multiple readings; Phase 2 is conceptual analysis in the
analytic-philosophy tradition; Phase 3 is presupposition analysis in the
philosophy-of-language tradition; Phase 4 is Toulmin argument
reconstruction, already in the catalog. The Constraints section wrapping
those phases is not itself a procedure — it is a set of interpretive
commitments about how to approach any claim at all, which is exactly
what Prism's **stance** class is for. Phase 5 is not an independent
analytical move but a customization of synthesis output.

So what looked like one skill is actually four lenses, one stance, and a
synthesis customization — each of which exists either in the catalog
already or as a new instrument usable independently of this recipe. A
future agent that needs only presupposition analysis, or only the
analytic-critique stance paired with a different argumentation tool, gets
those instruments for free; it does not need to import a monolithic
"Critical Decomposer" and then strip out the parts it does not want.

This is the load-bearing argument of Prism's **instruments > personas**
position, applied to itself. When a proposed skill decomposes cleanly
into catalog citizens plus orchestration, the right move is to add the
citizens (with names, sources, and provenance) and record the
orchestration as a recipe. The skill-shaped artifact disappears; its
analytical content is preserved and made reusable.

**What is lost.** One thing does not survive the decomposition cleanly:
Phase 1's conditional branching. The original decomposer specifies that
subsequent phases run *per Reading* when multi-layer-reading returns
multiple candidates. The current Prism workflow has no primitive for
per-branch lens execution — the orchestration note in Step 3 above asks
the analyst to enforce the branching manually. This is a genuine
limitation of the present workflow, not a notational trick; a future
Prism version that adds conditional execution primitives could recover
the automatic version. Until then, the recipe is honest about where
analyst discipline has to fill in.
