---
name: anchoring-bias
display_name: Anchoring Bias (Tversky-Kahneman)
class: heuristic
underlying_class: native
domain: general
source: Tversky & Kahneman, 1974
best_for:
  - estimation and forecasting
  - negotiation and pricing
  - judgment under uncertainty
one_liner: "Initial numbers disproportionately influence final judgments, even when explicitly irrelevant."
---

# Anchoring Bias (Tversky-Kahneman)

## The Rule

Judgments of quantity, value, or probability systematically shift toward an initially presented number, even when that number is known to be arbitrary or irrelevant to the estimate.

## When It Applies

- Making numerical estimates (revenue forecast, defect count, performance latency) after seeing an earlier figure, even one acknowledged as a placeholder or worst-case assumption.
- Pricing negotiations where the first offer becomes a reference point that shapes all counteroffers.
- Adjusting past estimates or forecasts when asked to revise upward or downward — the original anchor constrains the adjustment.
- Evaluating whether a value is "high" or "low" when the scale or comparable data is not provided independently.

## When It Misleads

- When the anchor is actually informative — a prior estimate, a historical baseline, or a domain-standard assumption. In such cases anchoring is not bias; it is rational updating.
- In domains with strong external feedback loops where the anchor is quickly overridden by data (e.g., repeated auction outcomes, live market prices). The anchor effect decays with real-time correction.
- When the estimator is sufficiently expert and has deliberately ignored or mentally discounted the anchor. Anchoring is most potent for novices; domain specialists show smaller shifts.
- When the anchor is far outside the plausible range — extremely high or low anchors often fail to move judgments because they are implicitly rejected as absurd.

## Common Misuse

Treating anchoring as a universal bias that derails all judgment. The heuristic's real finding is that the *direction and magnitude of adjustment from an anchor* is often insufficient, not that the anchor itself is always wrong. The mistake is confusing "anchor influenced the estimate" with "anchor was unwarranted." Many anchors *are* warrant­ed, and ignoring them would be worse.

Another misuse: deploying anchoring as an excuse for poor estimates. "The number was anchored" is not the same as "the number is wrong." The heuristic is a diagnosis of how the estimate was formed, not a verdict on whether the estimate should be believed.

## How Agents Use It

- **Embedded**: in estimation and forecasting lenses, at the "identify inputs" step, explicitly flag any prior estimate, historical figure, or initial proposal that precedes the judgment task. Document whether the anchor was used and whether it was appropriate.
- **Sanity-gate**: when a finding includes a numerical estimate (forecast, budget, duration, scope), ask whether the estimate was anchored to an earlier figure and whether the estimation process included a deliberate de-anchoring step (e.g., ask for an independent estimate first, then compare). If the anchor was present and unexamined, flag the finding as potentially shifted.
