---
name: tinbergen-rule
display_name: Tinbergen Rule
class: heuristic
underlying_class: native
domain: economics
source: Jan Tinbergen, 1956
best_for:
  - policy design
  - constraint satisfaction in systems
  - feasibility assessment
one_liner: "To hit N independent targets you need at least N independent instruments."
---

# Tinbergen Rule

## The Rule
To achieve N independent policy goals, you must have at least N independent policy instruments.

## When It Applies
- Designing a monetary and fiscal policy mix: you cannot hit both an inflation target and a growth target with only interest rates; you need both fiscal and monetary levers.
- System design with multiple constraints: achieving latency, throughput, and cost simultaneously requires at least three independent knobs to tune.
- Resource allocation: hitting targets for retention, conversion, and engagement requires separate budgets, not a single marketing spend that must somehow serve all three.
- Troubleshooting a complex failure: if you have four independent failure modes and only two independent corrective actions, you will be forced to trade off at least two modes.

## When It Misleads
- When instruments are not actually independent. If you control both tax rate and spending from a single authority with a unified objective function, they are a single instrument, not two, regardless of their formal labels.
- When goals are not actually independent. If goals are correlated or one is a proxy for another, the effective dimensionality is lower and you may need fewer instruments.
- When you have continuous levers, not discrete choices. Tinbergen's rule assumes you are assigning instruments to goals in a one-to-one way; continuous adjustment of a single instrument can sometimes approximate the behavior of multiple instruments.
- In adaptive or feedback systems where a single instrument, if well-tuned, can achieve multiple goals via causal coupling (e.g., improving code quality reduces both bugs and maintenance time).

## Common Misuse
Citing Tinbergen to shut down a policy proposal without actually counting the goals and instruments. A careless invocation sounds like "you can't optimize for both, so this is impossible" when the real question is whether you have enough levers. If you do, the problem is tractable; if you don't, you must either drop a goal, find a new instrument, or accept a trade-off. Tinbergen does not say what to do in any of those cases — it only flags that you need to do one of them.

## How Agents Use It
- **Embedded**: in policy-design or constraint-satisfaction lenses, use Tinbergen as a mandatory audit step: list all independent goals, list all independent instruments, verify the count, and flag any mismatch before recommending a solution.
- **Sanity-gate**: on each top finding that proposes to hit multiple targets with a single lever, ask: "Are these goals truly independent, and is this lever truly independent of other constraints? If yes, is this design under-resourced?"
