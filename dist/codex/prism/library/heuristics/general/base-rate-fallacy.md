---
name: base-rate-fallacy
display_name: Base Rate Fallacy
class: heuristic
underlying_class: native
domain: general
source: Kahneman & Tversky, 1973
best_for:
  - probability estimation under vivid case information
  - diagnosis and forecasting with case-specific details
  - risk assessment in medicine, security, and fraud detection
one_liner: "When given vivid case-specific information, people systematically underweight the base rate (population frequency) of the outcome."
---

# Base Rate Fallacy

## The Rule

When specific, concrete information about an individual case is available, people tend to ignore or dramatically underweight the base rate (the frequency of the outcome in the general population), leading to miscalibrated probability estimates.

## When It Applies

- Medical diagnosis: a positive test result is presented in vivid detail while the disease prevalence in the population is stated as a number.
- Security incidents: a suspicious login pattern triggers vivid alerts while the actual frequency of such patterns among legitimate users is backgrounded.
- Hiring: a candidate's interview performance or resume detail is highly memorable while the true success rate for candidates of similar background is abstracted.
- Forecasting: a recent, emotionally salient event (a market crash, a competitor's move) dominates prediction while historical frequency of such events is downweighted.
- Fraud detection: a transaction pattern "looks wrong" based on narrative detail while the actual prevalence of similar benign transactions is ignored.

## When It Misleads

- Base rates themselves can be stale or irrelevant. If the population has changed, the historical base rate may not apply to the current cohort. A rise in disease incidence should shift the base rate upward, not be ignored.
- In genuinely low-base-rate scenarios, the specific case information may be the only reliable signal. Base rates near zero can make case-by-case assessment necessary even if it feels like you are ignoring the rate.
- When the "case-specific information" is actually predictive and uncorrelated with the base rate — e.g., a specific risk factor that stratifies risk differently than the population average — attending to the case detail is correct, not a fallacy.

## Common Misuse

Treating base-rate correction as a blanket reason to discount vivid case information entirely. The fallacy is not "vivid information is bad"; it is the *asymmetric weighting* — people often swing from ignoring base rates to ignoring case detail when corrected. A well-calibrated judgment requires both.

Confusing "the base rate is low" with "therefore the finding is false." A finding can be correct and still surprise us because it is rare. The fallacy is probability miscalibration, not the detection itself.

## How Agents Use It

- **Embedded**: in diagnosis, forecasting, and risk-assessment lenses, at the "estimate probability" step, as a mandatory check: state the base rate explicitly before the case detail, then recalibrate the case probability against it using Bayesian reasoning or explicit calculation.
- **Sanity-gate**: on each probability estimate or binary verdict (positive/negative, likely/unlikely, approve/reject), ask: "What is the base rate for this outcome in the relevant population, and did I consciously weight it, or did the case detail crowd it out?"
