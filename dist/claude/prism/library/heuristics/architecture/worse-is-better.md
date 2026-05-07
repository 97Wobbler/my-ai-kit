---
name: worse-is-better
display_name: Worse is Better
class: heuristic
underlying_class: native
domain: architecture
source: Richard P. Gabriel, "Lisp: Good News, Bad News, How to Win Big" (1990)
best_for:
  - design trade-offs under time or resource pressure
  - shipping decisions when perfection blocks progress
  - evaluating competing architectural proposals
one_liner: "Simple and shipped beats perfect but delayed."
---

# Worse is Better

## The Rule
A simple solution that ships and solves the immediate problem, even with rough edges, beats a perfect solution that is still incomplete when the deadline arrives.

## When It Applies
- Choosing between a feature-complete but unshipped design and a simpler, shippable one with known limitations.
- Evaluating architectural trade-offs when adding robustness, generality, or elegance will slip the timeline.
- Prioritizing MVP feature lists: including something incomplete but working often beats deferring until all pieces are polished.
- Production incidents where a scrappy fix that restores service is preferable to waiting for the ideal solution.
- Iterating on a deployed system where early users benefit from incomplete features available now rather than perfect features available later.

## When It Misleads
- Safety-critical or security-sensitive domains where "good enough to ship" may mean "dangerously broken." Worse-is-better assumes the rough edges are cosmetic or recoverable, not systemic.
- When the "simple" version creates technical debt so severe that the next iteration is blocked. Worse-is-better is not a license to ship unmaintainable code.
- In platforms or APIs where early adopters build on your shipped roughness, locking in your shortcuts as de facto standards. The cost to fix later explodes.
- When the market or user expectations have already set a quality bar; shipping below it may not gain you any advantage over waiting for the complete version.

## Common Misuse
Conflating "good enough" with "actually works." A solution that ships but is fundamentally broken in silent ways (data loss, security holes, incorrect behavior) is not worse-is-better; it is sabotage. The heuristic applies to *tradeoffs between complete solutions*, not between a working solution and a broken one. Also frequently misapplied by teams that ship incomplete work and then never circle back to finish it, citing worse-is-better as justification for permanent debt.

## How Agents Use It
- **Embedded**: in design-decision or architectural-trade-off lenses, at the step where the agent compares candidate designs against the timeline. Ask: "Which design ships soonest, and does the gap to perfection actually matter before users can benefit?"
- **Sanity-gate**: on each architecture recommendation that defers capability or accepts rough edges, force the agent to state explicitly what the rough edges are and why they are acceptable given the business or user timeline. If the rough edges are unstated or unknown, the recommendation has not yet applied worse-is-better rigorously.
