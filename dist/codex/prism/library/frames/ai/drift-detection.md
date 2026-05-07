---
name: drift-detection
display_name: Drift Detection
class: frame
underlying_class: native
domain: ai
source: origin uncertain
best_for:
  - Classifying data or concept shift in ML systems by the type of distribution change
  - Deciding which monitoring or retraining strategy is appropriate
one_liner: "Classify covariate, label, and concept drift."
---

# Drift Detection

## Overview

Drift Detection sorts a suspected change in model performance or data distribution into one of three drift types based on *what changed* — the input distribution, the output distribution, or the relationship between them. Its core claim is that different drift types demand **structurally different detection methods and remediation strategies**. Misclassifying the drift type (e.g., treating concept drift as if it were covariate drift) leads to misdirected monitoring investments and ineffective retraining.

## Categories

1. **Covariate Drift** (also: feature drift, input shift)
   - The distribution of input features **P(X) changes**, but the relationship **P(Y|X) remains stable**.
   - The model's decision boundary is still valid; the problem it solves unchanged, but the kinds of instances it sees have shifted.
   - Discriminating criterion: held-out test accuracy (using the original training distribution) remains high, but real-world accuracy drops because the input feature distribution has moved.
   - Example: a loan approval model trained on urban borrowers deployed to rural regions with different income distributions; a recommendation model trained on 2024 user behavior applied to 2025 users with different query patterns.

2. **Label Drift** (also: target shift, class imbalance shift, prior shift)
   - The marginal distribution of labels **P(Y) changes**, but the conditional relationship **P(X|Y) remains stable**.
   - The prevalence of classes shifts, but given a class, the features that produce it are unchanged.
   - Discriminating criterion: retest the model on a held-out set with the *new* label distribution; if accuracy recovers, the shift is in the label prior, not the features.
   - Example: a fraud detection model trained on a 0.1% fraud rate deployed in a region with 2% fraud; a disease classifier trained on hospital data where 5% of patients have the disease, deployed to a screening population where 0.5% have it.

3. **Concept Drift** (also: posterior shift, label shift in the causal sense)
   - The relationship between features and labels **P(Y|X) changes** — the underlying concept or decision boundary shifts, even if input and output distributions remain individually stable.
   - The model is solving a different problem, or the world has changed the rules of the old problem.
   - Discriminating criterion: accuracy degrades *even when the feature and label distributions match their training distributions*. Retraining on new data with the same P(X) and P(Y) but newer timestamps recovers accuracy.
   - Example: a credit risk model trained before 2008 financial crisis deployed after it (risk factors changed); a spam filter trained on spam patterns from 2015 applied to 2026 spam (adversaries evolved tactics); a churn prediction model where customer behavior norms shifted due to market consolidation.

## Classification Procedure

1. **Establish a baseline.** Measure model accuracy on a recent validation set drawn from the deployment distribution. Compare to accuracy on the original held-out test set.
   - If accuracy is stable across time periods, no drift detected; stop.
   - If accuracy has degraded, proceed to step 2.

2. **Check feature distributions.** Compare the marginal distributions **P(X)** of key features in the training set vs. the recent deployment data (using statistical tests: KL divergence, Wasserstein distance, or a simple two-sample test).
   - If feature distributions have shifted significantly, proceed to step 3a (possible Covariate Drift).
   - If feature distributions are stable, proceed to step 3b (possible Label or Concept Drift).

3a. **For suspected Covariate Drift:** Retrain the model on recent data with the same label distribution as the original training set. If accuracy recovers to baseline, the drift is primarily in the input distribution.
   - Conclusion: **Covariate Drift**.
   - Alternative check: use importance weighting or domain adaptation to weight old training data by how similar it is to the new input distribution; if weighted retraining recovers accuracy without changing the decision boundary, this confirms Covariate Drift.

3b. **For suspected Label or Concept Drift:** Check label distribution **P(Y)** in the recent deployment data vs. the training set.
   - If **P(Y) has shifted significantly but P(Y|X) appears stable:** **Label Drift**.
     - Confirm: retrain on recent data but carefully balance classes to match the original training distribution; if accuracy remains degraded, this rules out Label Drift.
   - If **P(Y) is stable but retraining on recent data recovers accuracy:** **Concept Drift**.
     - Confirm: compare feature importance or decision boundaries between old and retrained models; they should differ if the concept shifted.

4. **Name the drift type and the time window** over which it occurred (sudden vs. gradual). Record which features or decision rules changed if available.

## Implications per Category

| Drift Type | Detection method | Remediation | Monitoring priority |
|---|---|---|---|
| **Covariate Drift** | Statistical test on P(X) (KL, Wasserstein, or adversarial binary classifier); feature histograms diverge. | Retrain on recent data *without* architectural changes; adjust feature preprocessing or use domain adaptation; sample re-weighting. | Monitor feature distributions continuously; high-frequency checks acceptable (daily/hourly). |
| **Label Drift** | Check marginal **P(Y)** in recent data; class frequencies diverge from training. | Adjust class weights or decision thresholds; retrain classifier head only if needed; calibrate on recent distribution. | Monitor class prevalence; check that held-out metrics (e.g., precision-recall) remain valid under new prior. |
| **Concept Drift** | Accuracy drop *despite stable* P(X) and P(Y); retraining recovers accuracy; decision boundary changes. | Full retraining on recent data (architecture and weights); consider incremental or online learning; investigate root cause of concept shift (market change, adversary evolution, etc.). | Monitor accuracy on representative recent test set; use **error rate change** as primary signal; lower detection latency needed (risk of stale model is higher). |

## Common Misclassifications

- **Covariate Drift mistaken for Concept Drift.** The tell: you retrain the model on new data (which has shifted feature distribution) and accuracy recovers *without* the decision boundary changing. If retraining without new labels still recovers performance, the shift was in **P(X)**, not the concept. Consequence: over-investing in root-cause investigation when a simple retrain would suffice.

- **Concept Drift mistaken for Covariate Drift.** The tell: feature distributions look stable, but retraining on recent data is necessary. A covariate-drift detector (monitoring **P(X)**) will not fire. Consequence: missing the signal that the model is solving the wrong problem; continuing to use a model with a stale decision boundary.

- **Label Drift mistaken for Covariate Drift.** The tell: **P(X)** is stable, but **P(Y)** has shifted; you adjust only feature processing instead of class weights or thresholds. Consequence: the model's calibration is wrong (it was trained on a 1% positive rate; now 10% of examples are positive), yielding systematically biased predictions.

- **Attributing accuracy drop to drift when the cause is data quality.** The tell: recent data contains measurement errors, missing values, or label noise not present in the training set. This looks like Concept Drift (accuracy drops, retraining helps) but is actually a quality issue. Consequence: retraining models on bad labels, which amplifies the problem. Mitigation: audit data quality and label consistency first before assuming drift.

- **Confusing gradual and sudden drift with drift type.** Gradual vs. sudden is a *temporal* property, not a categorical one. Covariate drift can be sudden (deployment to a new region) or gradual (user behavior shifting season by season). Misclassifying this leads to wrong monitoring cadence (e.g., hourly checks for a gradual drift that moves on a monthly timescale).
