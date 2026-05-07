---
name: pareto-80-20
display_name: Pareto 80/20
class: heuristic
underlying_class: native
domain: general
source: Vilfredo Pareto, 1896; generalized by Joseph Juran
best_for:
  - prioritization under resource constraints
  - root-cause and impact analysis
  - identifying where to focus effort
one_liner: "80% of outcomes come from 20% of causes — nothing is uniform."
---

# Pareto 80/20

## The Rule

In many real-world distributions, roughly 80% of the effects come from roughly 20% of the causes; the exact ratio varies, but the usable insight is that most systems exhibit heavy-tailed distributions, not uniform ones.

## When It Applies

- **Prioritizing fixes or effort**: a handful of bugs, support tickets, or performance bottlenecks account for the bulk of user impact or operational cost.
- **Deciding what to cut**: when time or budget is limited, identifying the 20% of work that drives 80% of value lets you protect it and shed the rest.
- **Root-cause analysis**: beginning the investigation at the top of the actual distribution rather than guessing where the leverage is.
- **Roadmap triage**: separating the few features that will move the needle from the many that will not, by measuring real usage or revenue contribution.

## When It Misleads

- **Assuming the distribution without measuring it**: the real pattern may be uniform, bimodal, or even inverted. Always plot the data before citing Pareto.
- **Confusing frequency with severity**: 80% of incidents by count may come from 20% of failure modes, but the remaining 20% of incidents may carry 80% of the risk (security, safety, correctness). Pareto by volume does not imply Pareto by consequence.
- **In exploratory or compounding domains**: breakthrough work often lives in the long tail. Cutting the tail in R&D, research, or creative work can kill the high-leverage ideas that are rare precisely because they haven't been found yet.
- **When the "20%" is hard to address but cheap to protect**: sometimes the high-impact causes are harder to fix than they look, and cutting them may create new problems faster than the Pareto gain accrues.

## Common Misuse

Citing 80/20 as a law of nature without ever looking at the actual distribution. The heuristic is an empirical observation to check against data, not a prior to assume. Agents often treat Pareto as permission to ignore the tail entirely, when the real output is: "prioritize the top 20% and reassess the tail's contribution to secondary goals before deleting it."

## How Agents Use It

- **Embedded**: in prioritization or impact-analysis lenses, use Pareto to structure the ranking step. Measure or estimate the distribution explicitly, sort by contribution, and mark the cutoff point where diminishing returns begin.
- **Sanity-gate**: on each prioritization or scope-cut recommendation, force the agent to state what the actual distribution is (not the assumed one) and name the top 3–5 items by measured impact. If a recommended item falls outside that top bucket, justify why it survives the cut.
