---
name: shap-lime
display_name: SHAP/LIME Local Interpretability
class: lens
underlying_class: native
domain: ai
source: Lundberg & Lee (SHAP, 2017); Ribeiro et al. (LIME, 2016)
best_for:
  - Understanding why a black-box model made a specific prediction
  - Debugging unexpected model outputs on individual instances
  - Building trust in model decisions for stakeholders
one_liner: "Local attribution methods that decompose a model's contribution to individual predictions."
---

# SHAP/LIME Local Interpretability

## Overview
SHAP (SHapley Additive exPlanations) and LIME (Local Interpretable Model-agnostic Explanations) are techniques for decomposing a model's prediction on a single instance into contributions from each input feature. Instead of explaining the model globally, they ask: "Why did the model output 0.87 for *this* specific example?" Practitioners reach for them when a model's decision feels wrong, when they need to justify a prediction to a non-technical stakeholder, or when they're debugging systematic failures on a subset of cases.

## Analytical Procedure

### Phase 1 — Prepare the artifact

1. **Identify the model and the prediction to explain.** Select one instance (a single row, image, text snippet, etc.) and its corresponding model output. Record the output value and the ground truth if available. This is your explanation target.

2. **Define the feature space.** List all input features your model accepts. For tabular data, these are columns. For images, these might be pixel regions or semantic regions. For text, these might be word tokens or phrase chunks. Ensure the feature space is comprehensive and mutually exclusive.

3. **Collect baseline data.** Gather a representative sample of instances from your training or validation set (typically 100–1000 examples). This will be used to estimate how the model behaves in the absence of each feature. Record the feature values and model outputs for the baseline set.

### Phase 2 — Apply the explanation technique

#### If using LIME:

4. **Generate perturbed variants of the target instance.** Create a set of synthetic instances by randomly masking or removing individual features from the target instance. For tabular data, replace feature values with random draws from the baseline. For images, occlude regions. For text, remove word tokens. Generate 1000–5000 variants.

5. **Predict on all variants.** For each perturbed instance, obtain the model's output. Record the perturbation mask (which features were present) and the output side-by-side.

6. **Fit a local linear model.** Train a simple linear regression (or logistic regression for classification) where:
   - X = the perturbation masks (binary: feature present=1, absent=0)
   - y = the model outputs from step 5
   
   The regularization parameter λ (or `regularization_strength` in LIME implementations) controls how much you penalize large coefficients. Set it to encourage sparsity — typically you want 3–10 features in the final explanation.

7. **Extract coefficients.** The regression coefficients are the feature importances. Positive coefficients mean the feature pushes the prediction higher; negative means it pushes lower. The intercept represents the baseline (the prediction if no features were present).

#### If using SHAP:

4. **Select a SHAP variant** based on your model type:
   - **TreeExplainer** for tree-based models (XGBoost, LightGBM, CatBoost, scikit-learn forests)
   - **DeepExplainer** for neural networks
   - **KernelExplainer** for any black-box model (slowest, model-agnostic)
   - **LinearExplainer** for linear models

5. **Compute Shapley values.** For the target instance, calculate the contribution of each feature by:
   - (Tree/Deep/KernelExplainer) Computing the change in model output when each feature is included vs. excluded, averaged over all possible orderings of features in the feature set.
   - Recording the Shapley value for each feature: a single number representing its marginal contribution to moving the prediction from the baseline to the actual output.

6. **Verify the Shapley property.** Check that the sum of all Shapley values plus the baseline equals the actual model output. This is a sanity check — if it doesn't hold, the computation is wrong.
   ```
   baseline_output + sum(shap_values) = model_output
   ```

### Phase 3 — Evaluate and interpret

8. **Rank features by magnitude.** Sort features by the absolute value of their contribution (LIME coefficient magnitude or SHAP value magnitude). The top 3–5 features should account for most of the explanation.

9. **Check sign consistency.** For the top features, verify that the direction of the contribution makes intuitive sense. If a feature with value 0.95 (high) has a strong negative coefficient, ask: does the model really penalize high values of this feature? Check this against the baseline data — is high values of this feature typically associated with lower outputs?

10. **Test perturbation robustness (LIME only).** Re-run the LIME explanation with a different random seed and different perturbation strategy (e.g., different λ). Do the top features remain stable? If they change dramatically, the explanation is unstable and the conclusions are unreliable.

11. **Validate against human intuition.** Show the explanation to someone familiar with the domain. Does the ranking and direction match domain knowledge? Disagreement is a red flag — it may indicate the model has learned a spurious pattern.

### Phase 4 — Document findings

12. **Produce the explanation artifact.** Record the baseline output, the actual output, the top contributing features, their directions, and their magnitudes. Include a plain-language summary: "The prediction was high because feature X (value=0.8) increased it by +0.15, and feature Y (value=0.2) decreased it by -0.08."

## Evaluation Criteria

| Check | Pass |
|---|---|
| Target instance and its prediction are clearly identified | Y/N |
| Feature space is complete and features are mutually exclusive | Y/N |
| Baseline data was collected and is representative | Y/N |
| Explanation includes ≥3 features with direction and magnitude | Y/N |
| Shapley property holds (if SHAP) or regularization term is reasonable (if LIME) | Y/N |
| Top features align with domain intuition or misalignment is flagged | Y/N |
| Perturbation robustness was tested (LIME) or multiple instances were sampled (SHAP) | Y/N |

## Red Flags

- The explanation names only 1–2 features. Either the model relies on very few features (possible but rare) or the technique hasn't converged. Increase the number of perturbed samples or adjust regularization.
- All features have similar magnitude. This suggests the explanation is flat and uninformative — the model may be averaging inputs uniformly, or the feature scaling is wrong, or the baseline data is biased.
- Top features contradict domain knowledge (e.g., "high credit score decreased loan approval probability") and you proceed without investigating. This is often the first sign of data leakage, encoding errors, or concept drift.
- LIME explanation is unstable across random seeds. The local linear approximation may be poor. Try KernelExplainer or TreeExplainer instead, or check that the perturbation strategy isn't too aggressive.
- Shapley values sum to a value very different from (baseline + output change). The computation is broken — check that the baseline is set correctly and the feature coalitions are exhaustive.
- No comparison to baseline. If you don't show the baseline output alongside the actual output, readers won't know if the explanation is explaining signal or noise.

## Output Format

```
## SHAP/LIME Explanation

**Target instance:**
[Feature values: e.g., age=45, income=75000, credit_score=720, ...]

**Baseline output:** [e.g., 0.32]
**Actual output:** [e.g., 0.87]
**Change to explain:** +0.55

### Top Contributing Features

| Rank | Feature | Value | Contribution | Direction |
|---|---|---|---|---|
| 1 | <feature_name> | <value> | <+/- magnitude> | Increases/Decreases prediction |
| 2 | <feature_name> | <value> | <+/- magnitude> | Increases/Decreases prediction |
| ... | ... | ... | ... | ... |

**Method:** [LIME with λ=0.01, 2000 perturbations] or [SHAP TreeExplainer]

### Plain-Language Summary
The prediction was [high/low] primarily because <feature1> <direction> it by <amount>, followed by <feature2> and <feature3>. These three features account for [X]% of the change from baseline.

### Domain Alignment
[Do the top features and their directions align with domain knowledge? If not, flag the misalignment and possible causes.]

### Robustness Check
[For LIME: Were the top features stable across different random seeds? For SHAP: Were the feature orderings consistent across multiple instances?]

### Confidence
<high/medium/low> — <justification, e.g., "High: top features stable across seeds, align with domain intuition, and Shapley property holds. Medium: explanation is stable but contradicts one domain assumption. Low: top features shifted when regularization changed; explanation may be unreliable.">
```
