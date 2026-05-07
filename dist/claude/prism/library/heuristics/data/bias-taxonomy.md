---
name: bias-taxonomy
display_name: Bias Taxonomy
class: heuristic
underlying_class: native
domain: data
source: origin uncertain
best_for:
  - data quality assessment
  - findings validation
  - research methodology review
one_liner: "Checklist of selection, survivorship, confirmation, recall, and publication biases for data trust."
---

# Bias Taxonomy

## The Rule
Before trusting a finding derived from data, systematically audit which observations made it to your analysis: selection bias (who was sampled), survivorship bias (what was excluded), confirmation bias (which patterns you sought), recall bias (what was remembered), and publication bias (what was reported).

## When It Applies
- Analyzing user behavior or market trends from observational data where the sample is self-selected or filtered by downstream processes.
- Reviewing research findings, especially meta-analyses or literature syntheses where publication decisions shape what is visible.
- Evaluating metrics that depend on user self-report (surveys, logs, feedback) rather than instrumentation.
- Interpreting success stories or case studies where only winning cases are documented.
- Assessing historical datasets where attrition, missing values, or archival practices skewed what survived.

## When It Misleads
- When applied dogmatically, the taxonomy can paralyze: every dataset has *some* bias; the question is whether it is large enough to overturn the finding, not whether it exists.
- In controlled experiments with a properly randomized sample and outcome, selection and survivorship bias are negligible; over-applying the checklist here wastes energy.
- Publication bias is a problem for meta-analysis and literature review, but not for a single well-designed study with pre-registered outcomes.
- When used to dismiss a finding rather than to quantify the bias, it becomes a rhetorical tool rather than a diagnostic.

## Common Misuse
Citing "bias exists" without estimating magnitude. The taxonomy is useful only when you ask: *which* bias is largest, *how much* does it shift the finding, and *does* the finding hold if that bias is reversed? Listing five bias types and stopping is not analysis.

Another common trap: treating bias as a binary (present/absent) rather than directional. Selection bias that over-weights high-engagement users systematically inflates engagement metrics. Publication bias that favors positive results systematically inflates effect sizes. The direction matters for deciding whether the finding is conservative or inflated.

## How Agents Use It
- **Embedded**: in data-quality or research-methodology lenses, as a mandatory checklist step. Before accepting a dataset's findings, apply each bias category and document which are negligible and which require adjustment or caveat.
- **Sanity-gate**: on each quantitative finding, ask for each bias type: "What would this metric look like if [this bias] were removed or reversed?" If the finding survives the largest plausible bias reversal, note it. If not, it is a candidate for downweighting or caveating.
