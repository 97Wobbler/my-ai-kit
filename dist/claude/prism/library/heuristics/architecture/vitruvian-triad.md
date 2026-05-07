---
name: vitruvian-triad
display_name: Vitruvian Triad
class: heuristic
underlying_class: native
domain: architecture
source: Vitruvius, De architectura, 1st century BCE
best_for:
  - evaluating design proposals for balance across multiple criteria
  - resolving trade-offs between structural, functional, and aesthetic demands
  - auditing existing solutions for hidden weaknesses in one dimension
one_liner: "Judge firmness, commodity, and delight equally — ignoring any one of the three is design failure."
---

# Vitruvian Triad

## The Rule
A design that neglects any one of firmness (structural integrity), utility (fitness for purpose), or beauty (coherent form) will fail, regardless of excellence in the other two.

## When It Applies
- Evaluating architectural or design proposals where stakeholders disagree on which criterion matters most.
- Resolving conflicts between structural constraints, functional requirements, and aesthetic intent — common in buildings, software systems, and products.
- Auditing completed work that appears successful on one axis (e.g., "it works beautifully") but weak on another (e.g., "it will not scale").
- Prioritizing among competing design revisions when some improve function at the cost of form, or strengthen structure at the cost of usability.

## When It Misleads
- When one criterion is genuinely non-negotiable due to safety, legal, or existential constraints. A structure that collapses is not salvaged by beauty; utility and aesthetics become secondary priorities.
- In contexts where the audience or user base explicitly deprioritizes one dimension. A utilitarian industrial tool may be rightly ugly; a temporary pavilion may rightly sacrifice durability for vision. The Triad is a *balance principle*, not an absolute weighting.
- When applied as a blocker against iteration. A prototype may be intentionally weak in one dimension to test the others; the Triad is a reminder to address all three *eventually*, not simultaneously.
- In domains where one dimension is genuinely not applicable (e.g., a purely virtual system has no physical firmness; a temporary installation has no durability requirement).

## Common Misuse
Treating the Triad as three equal votes, each with the same weight in every context. This flattens the distinct roles each plays: firmness is a floor (non-negotiable minimum), utility is the primary purpose, and beauty is the multiplier that makes a solution preferred over a merely adequate one. Misuse often manifests as architects or designers dismissing functional feedback as "not part of their brief" or dismissing structural warnings as "conservative engineering."

## How Agents Use It
- **Embedded**: in design-review lenses, as a mandatory three-part audit step. For each proposed design, explicitly assess it on firmness (Will it hold? Does it scale?), utility (Does it do the job? For whom?), and beauty (Is it coherent? Does it feel right?). Flag any axis where the proposal is silent or weak.
- **Sanity-gate**: when a design recommendation is finalized, ask: "Which of the three dimensions is this solution strongest in, which is it weakest in, and have we explicitly accepted the weakness or should we iterate?" A design that excels in one dimension only is not ready for recommendation without acknowledged trade-offs.
