---
name: sunk-cost-fallacy
display_name: Sunk Cost Fallacy
class: heuristic
underlying_class: native
domain: general
source: Arkes & Blumer, 1985
best_for:
  - resource allocation decisions
  - project continuation vs. pivot judgment
  - investment and sundown calls
one_liner: "Discard past unrecoverable costs from forward-looking decisions; they are irrelevant to whether to continue or stop."
---

# Sunk Cost Fallacy

## The Rule
Once a cost is sunk — unrecoverable and past — it has no bearing on whether to continue, pivot, or abandon the path forward; only future costs and benefits matter.

## When It Applies
- Deciding whether to shut down a project, feature, or product line that is consuming resources and underperforming, when the sunk development cost is substantial.
- Evaluating whether to abandon an investment strategy or portfolio position that has already lost money.
- Assigning additional engineering to "rescue" a codebase or system where heavy investment has already yielded poor returns.
- Choosing to continue a course of action primarily because "we've already spent so much on it."

## When It Misleads
- When sunk costs are *correlated with* (but not identical to) the quality or fitness of future output. A codebase that cost $1M to build may indeed be more robust than a $100K equivalent, not because money is relevant but because the correlation is real.
- In organizational or political contexts where abandoning a high-investment project signals poor judgment or wastes capital. The sunk cost is genuinely sunk, but the *perception* of waste creates real downstream costs (reputation, credibility, future funding).
- When the sunk cost represents infrastructure or capability that has value beyond the original project. Dismissing it as "sunk" ignores its option value.
- In path-dependent domains where the sunk cost has created a lock-in that makes reversal genuinely expensive (switching costs, vendor agreements, learned expertise tied to one platform).

## Common Misuse
Citing the fallacy as a rubber stamp to kill projects without actually comparing forward costs and benefits. "That's a sunk cost fallacy" does not replace the hard work of estimating whether future revenue, risk reduction, or strategic value justifies continued investment. The heuristic eliminates one *irrelevant* factor; it does not render the decision obvious.

Also: confusing "ignore the sunk cost" with "ignore the reason the cost was sunk." If a project overran budget because of technical complexity, that complexity is *not* sunk and *does* matter to the forward decision.

## How Agents Use It
- **Sanity-gate**: on any recommendation to continue a struggling project, feature, or investment, check whether the justification relies on "we've already spent X" or on forward-looking fundamentals (revenue, impact, risk). If the sunk cost is doing the work, flag it.
- **Embedded**: in go/no-go decision lenses, as a mandatory filter step that explicitly removes sunk costs from the evaluation before comparing forward alternatives.
