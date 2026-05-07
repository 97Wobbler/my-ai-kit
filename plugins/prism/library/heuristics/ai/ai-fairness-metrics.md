---
name: ai-fairness-metrics-tradeoff
display_name: Fairness Metric Tradeoff
class: heuristic
underlying_class: native
domain: ai
source: Barocas, Hardt, Narayanan (2019); Corbett-Davies et al. (2017)
best_for:
  - Choosing between competing fairness definitions
  - Evaluating fairness claims in ML systems
  - Identifying hidden value judgments in fairness audits
one_liner: "Fairness metrics trade off — you cannot satisfy three or more simultaneously."
---

# Fairness Metric Tradeoff

## The Rule
No ML system can simultaneously satisfy demographic parity, equalized odds, and calibration across all groups; choosing any two forces a tradeoff on the third.

## When It Applies
- Evaluating a fairness audit that claims a model meets multiple fairness criteria without discussing which were prioritized.
- Designing a fairness constraint for a classifier when stakeholders have named competing goals (e.g., "equal FPR across groups *and* equal acceptance rates").
- Interpreting vendor claims that a system is "fair" without specifying which definition of fairness was optimized.
- Regulatory contexts where the law names one fairness principle (e.g., disparate impact) but the system's design may serve another (e.g., individual calibration).

## When It Misleads
- When the system is not a classifier or scoring model — fairness tradeoffs apply most sharply to binary/multiclass decisions; they weaken for regression, ranking, or causal attribution.
- When the groups are small or the base rates differ wildly, the mathematical tension may relax enough that approximate satisfaction of multiple criteria becomes feasible; the heuristic describes the hard case, not all cases.
- When optimizing for a *single* metric across all groups without the cross-group comparison — demographic parity and equalized odds are tradeoffs *between* groups, not universal constraints, and a system can trivially satisfy both if accuracy is allowed to vary without limit.

## Common Misuse
Citing the tradeoff as a reason to abandon fairness work altogether ("all definitions conflict, so nothing can be fair"). The heuristic identifies a hard choice, not an excuse to avoid choosing. Conversely, claiming a metric is "model-agnostic" or "definition-independent" without naming which fairness criterion was actually optimized — that is rhetorical rather than technical.

A related misuse: treating the three criteria as equally important without understanding the stakeholder harm each one guards against. Demographic parity protects against group-wide undertreatment; equalized odds protects individuals in both groups from disparate error rates; calibration protects against misrepresenting confidence to individuals. Choosing one is not morally equivalent to choosing another.

## How Agents Use It
- **Embedded**: in a fairness audit lens, at the "metric selection" step, as a forcing function to name which fairness criterion is being optimized and why the others were not.
- **Sanity-gate**: on each fairness claim, ask: "Which two of the three (demographic parity, equalized odds, calibration) is this system satisfying, and which one was traded off?" If the answer is "all three equally," flag that the claim has not been operationalized.
