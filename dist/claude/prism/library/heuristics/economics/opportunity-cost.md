---
name: opportunity-cost
display_name: Opportunity Cost
class: heuristic
underlying_class: native
domain: economics
source: origin uncertain
best_for:
  - resource allocation decisions
  - trade-off evaluation
  - investment justification
one_liner: "The value of a choice is measured by the next-best alternative foregone."
---

# Opportunity Cost

## The Rule
The true cost of choosing option A is not the price you pay, but the value of the best alternative option B you gave up.

## When It Applies
- Comparing two investments where only one will be funded; the cost of choosing project X includes the return you lose from project Y.
- Evaluating whether to keep an employee on a task when they could work on a higher-impact project; the cost includes the forgone output.
- Deciding whether to use an existing asset (server, inventory, person-hour) for a new purpose; the cost is what that asset would have earned in its current use.
- Justifying a strategy that consumes resources; the case is weak if you haven't named what gets displaced.

## When It Misleads
- When opportunity cost is used to second-guess every decision in hindsight: "you could have invested in Bitcoin" is not a useful cost analysis unless Bitcoin was a genuine live alternative at the time.
- In situations with genuine surplus capacity, where the alternative is idle (not a productive use). Forcing a phantom opportunity cost into the analysis adds no information.
- When the "forgone alternative" is hypothetical or unmeasurable (e.g., "the cost of this feature is the product we might have built instead, which we never defined"). A real alternative must be concrete enough to have an actual value.
- In sunk-cost reasoning, where the rule is used to justify continuing a failing project ("we can't stop now, think of what we've invested"). Sunk costs are not opportunities; opportunity cost only applies to forward-looking choices.

## Common Misuse
Treating opportunity cost as a justification for paralysis. "Everything has an opportunity cost" is true; it does not mean all choices are equivalent or that you should optimize for the unmeasured alternative over the concrete one in front of you. The heuristic is most useful when you have at least two named, concrete alternatives with estimated values — without that comparison, citing "opportunity cost" is a rhetorical gesture, not analysis.

## How Agents Use It
- **Embedded**: in resource-allocation or portfolio-choice lenses, as a mandatory step: before recommending option A, the agent must explicitly identify the best alternative B that will be displaced, estimate its value, and confirm that A's benefit exceeds B's.
- **Sanity-gate**: on each resource-allocation recommendation, ask: "What is the second-best use of this resource, and does the recommended choice beat it by a margin that justifies the displacement?"
