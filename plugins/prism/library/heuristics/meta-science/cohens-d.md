---
name: cohens-d
display_name: Cohen's d
class: heuristic
underlying_class: native
domain: meta-science
source: Jacob Cohen, 1988
best_for:
  - effect size interpretation
  - meta-analysis synthesis
  - statistical significance traps
one_liner: "A small effect can reach statistical significance in a large sample."
---

# Cohen's d

## The Rule
A statistically significant result does not tell you whether the effect is practically meaningful; check the standardized effect size (d) to separate trivial effects that happen to reach significance from effects that matter in context.

## When It Applies
- Evaluating a study with n > 500 where p < 0.05 but the absolute difference between groups is tiny relative to real-world variability.
- Comparing effect sizes across studies with different sample sizes, measurement scales, or units.
- Meta-analyses where heterogeneous studies report p-values but not effect sizes; computing d lets you weight findings by magnitude, not just statistical significance.
- Deciding whether a statistically significant result justifies a policy change, treatment adoption, or resource allocation.

## When It Misleads
- When the practical threshold for "meaningful" is genuinely set by context, not by Cohen's conventional cutoffs (small ≈ 0.2, medium ≈ 0.5, large ≈ 0.8). In some domains, a d of 0.15 is life-changing; in others, d = 0.9 is negligible. The cutoffs are not laws.
- In small-sample studies (n < 30), d is unstable and has high sampling variability; treating a point estimate as truth misleads more than reporting p-values alone.
- When the effect is directionally reversed or null in a subset of the population. A population-level d = 0.5 can mask that half the sample got worse. Aggregate effect size hides heterogeneity.
- When the outcome is bounded (0–100% compliance, 1–5 rating scale). Cohen's d assumes unbounded normal distributions; on constrained scales, the same d value can mean very different things depending on where the means fall.

## Common Misuse
Citing Cohen's conventional thresholds ("d > 0.8 is large, so this is large") without ever asking whether the threshold applies to the domain. The cutoffs come from social psychology circa 1988 and do not transfer blindly to medicine, engineering, or other fields where cost-of-error and baseline variability differ radically. 

Another pattern: computing d post-hoc on a p-value-driven study to make a weak finding look acceptable, then hiding the unstable estimate behind the appearance of a standardized metric. If the study was powered for p < 0.05 (not for a specific d), the resulting effect size estimate is inflated and should be reported with a wide confidence interval.

## How Agents Use It
- **Embedded**: in meta-analysis or systematic-review lenses, at the "synthesize findings" step, to ensure effect sizes are extracted or computed before pooling across studies. Also in critical-appraisal lenses, as a mandatory check on any claim that a large sample and p < 0.05 together imply a meaningful result.
- **Sanity-gate**: on each top finding from a quantitative study, ask: "Is the reported effect size (d, r, odds ratio, etc.) meaningful in the real-world context of the question, independent of the p-value?" If the effect size is not reported or is trivially small, flag the finding for downweighting or reframing before synthesis.
