---
name: First Principles Thinking
domain: general
source: Aristotle (Posterior Analytics); modernized in physics (Feynman) and engineering (Musk)
underlying_class: native
best_for: Breaking free of analogies and received wisdom when a problem resists conventional solutions
one_liner: "Decompose to basics, separate physics from convention, discard convention, and rebuild to find delta versus incumbent solutions."
---

# First Principles Thinking

## Overview
Instead of reasoning by analogy ("X is similar to Y, so do what works for Y"), decompose the problem to its irreducible truths and rebuild the solution from scratch. The discipline is the decomposition — most people stop one or two levels shallow and declare the residue a "first principle." Practitioners use this when the default solution feels expensive or incoherent and they suspect it inherited assumptions from a different context.

## Analytical Procedure

### Phase 1 — Decompose

1. **State the problem in one sentence.** No jargon. A 12-year-old should parse it.

2. **List the current/default approach to the problem.** Write the 3-6 steps or components of how it's usually solved.

3. **For each component, ask "Why is this here?" three times.** The first "why" usually gives a tradition answer. The second gives a historical answer. The third usually gives the actual constraint. Write all three down. This is the "5 Whys" technique applied at component granularity.

4. **Mark each resulting reason as one of:**
   - **Physical** — dictated by physics, chemistry, information theory, etc.
   - **Economic** — dictated by current costs or markets (which can change)
   - **Regulatory** — dictated by law or policy (which can change)
   - **Conventional** — dictated by habit or tradition (no actual constraint)
   - **Historical** — made sense once but the original reason no longer applies
   Conventional and Historical reasons are candidates for elimination. Physical reasons stay.

### Phase 2 — Identify First Principles

5. **Extract the irreducible requirements.** What does the problem *actually* demand, stripped of how it's currently solved? Write each as a constraint:
   - Bad: "We need a faster database."
   - Good: "We need to answer queries about user state within 100ms at 10k QPS, and we must not lose writes."

6. **Stress-test each principle.** Try to state it more basely. If you can keep going, you haven't hit a principle yet. Stop only when you reach a constraint grounded in physics, math, user need, or a hard external requirement you can't negotiate.

### Phase 3 — Reconstruct

7. **Starting from ONLY the first principles, design a fresh solution.** Do not reference the default solution. Do not use the word "like" or "similar to." If you catch yourself importing structure from the default, note it and back up.

8. **Compare the reconstruction to the default.** The interesting output is NOT "my reconstruction is better." It's the delta — the parts of the default that exist only for Conventional or Historical reasons. These are the real findings.

9. **Cost the delta.** For each piece of the default that the reconstruction drops or replaces, estimate the cost of actually removing it from the current system. High-value, low-cost deltas are your recommendations.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Problem statement is jargon-free and under 20 words | Y/N |
| Every component of the default was interrogated with 3 "why"s | Y/N |
| Each "why" answer is tagged Physical/Economic/Regulatory/Conventional/Historical | Y/N |
| At least 2 components were found to be Conventional or Historical | Y/N |
| The reconstruction does NOT reference the default by analogy | Y/N |
| Deltas between reconstruction and default are cost-tagged | Y/N |

## Red Flags

- Every reason in Phase 1 comes out as "Physical" or "Economic." This is decomposition failure — you stopped at the first plausible answer.
- The reconstruction in Phase 3 looks nearly identical to the default. Either the default really is near-optimal (rare) or you imported assumptions without noticing (common).
- The "first principle" is itself a solution ("we need caching"). That's not a principle, it's a technique. Go deeper.
- No Conventional/Historical reasons anywhere. Every system has crust. Missing it means the interrogation wasn't adversarial enough.
- Reconstruction is presented with high confidence but never costed. Without costing, the analysis is academic.

## Output Format

```
## First Principles Assessment

**Problem (plain language):**
<one sentence>

### Phase 1 — Decomposition of Default
| Component | Why1 | Why2 | Why3 | Tag |
|---|---|---|---|---|
| <...> | <...> | <...> | <...> | Physical/Economic/Regulatory/Conventional/Historical |

### Phase 2 — First Principles (irreducible requirements)
1. <constraint>
2. <constraint>
3. ...

### Phase 3 — Reconstruction
<Description of a solution derived only from the principles above.
Do not reference the default solution here.>

### Delta Analysis
| Part of default | Keep / Drop / Replace | Why | Removal cost |
|---|---|---|---|
| <...> | <...> | <...> | <...> |

### High-Value Deltas
1. <delta with cost justification>
2. ...

### Confidence
<high/medium/low> — <justification>
```
