---
name: qsar
display_name: Quantitative Structure-Activity Relationship (QSAR)
class: lens
underlying_class: native
domain: chemistry
source: Hansch & Fujita, 1964; modernized in computational chemistry and cheminformatics
best_for:
  - Predicting biological activity from molecular structure
  - Identifying key structural features that drive potency
  - Screening large chemical libraries before synthesis
one_liner: "Quantitative structure-activity relationship — regression modeling of bioactivity from molecular descriptors."
---

# Quantitative Structure-Activity Relationship (QSAR)

## Overview

QSAR models the relationship between the structural properties of molecules (descriptors) and their observed biological activity (potency, toxicity, binding affinity, etc.) as a mathematical equation. The discipline is rigorous descriptor selection and validation — most QSAR failures occur because descriptors were chosen on intuition rather than correlation, or the model was not stress-tested on held-out data. Practitioners use QSAR when they need to predict activity for untested compounds or understand which molecular features control a biological response.

## Analytical Procedure

### Phase 1 — Problem Definition

1. **Define the biological endpoint.** Write the exact measurement being predicted: binding affinity (Kd in nM), inhibition (IC50 in µM), cytotoxicity (LC50), clearance (ml/min/kg), etc. Include units and the assay platform (cell-free, cellular, in vivo). This is non-negotiable — conflating different assay formats invalidates the model.

2. **Establish the dataset.** Collect or curate a set of compounds with measured activity values. Minimum useful size is 20 compounds; 50+ is preferred. Document:
   - Chemical structure (SMILES, SDF, or InChI)
   - Measured activity value
   - Standard deviation or confidence interval (if available)
   - Source (literature, internal assay, database)
   - Assay conditions (pH, temperature, cell line, incubation time)

3. **Audit for quality.** Screen for:
   - Duplicate structures (same compound measured multiple times — use mean or remove outliers)
   - Inactive compounds (activity below detection limit — mark as censored, do not discard)
   - Outliers (activity value inconsistent with chemical structure — flag for review, do not auto-remove)
   - Activity range (tightly clustered activities limit model power; 2+ orders of magnitude is typical)

### Phase 2 — Descriptor Calculation and Selection

4. **Calculate molecular descriptors.** Use a cheminformatics tool (RDKit, MOE, Pipeline Pilot) to generate a pool of descriptors. Standard categories include:
   - **Lipophilicity:** LogP (partition coefficient)
   - **Molecular weight & size:** MW, TPSA (topological polar surface area), number of rotatable bonds
   - **Aromaticity & rings:** number of aromatic rings, fraction of sp3 carbons
   - **H-bonding:** donor/acceptor counts
   - **Shape:** molecular surface area, shape coefficient
   - **Electronic:** molar refractivity, electronegativity
   Start with 50–200 descriptors. Do not cherry-pick based on chemical intuition alone.

5. **Screen for redundancy.** Compute pairwise Pearson or Spearman correlations between all descriptors. Remove or merge descriptors with |r| > 0.95 to avoid multicollinearity. Keep the descriptor with the higher univariate correlation to activity.

6. **Univariate correlation scan.** Plot each descriptor against activity (scatter plot or binned bar chart). Note which descriptors show monotonic or U-shaped trends. Descriptors with no visual correlation to activity are candidates for removal. Document correlation coefficient and p-value for each.

7. **Select descriptors via stepwise or regularized regression.**
   - **Stepwise forward selection:** Start with zero descriptors. At each step, add the descriptor that minimizes prediction error (use cross-validation; see Phase 3). Stop when cross-validated error plateaus or when adding a descriptor increases error.
   - **Regularized regression (LASSO or Ridge):** Fit a regression model with automatic feature shrinking. LASSO will zero out weak descriptors; Ridge will shrink their coefficients. Extract descriptors with non-zero coefficients.
   - Do not hand-select more than 6–8 descriptors for a dataset of 50 compounds; overfitting risk rises with descriptor count.

### Phase 3 — Model Building and Validation

8. **Partition the data.** Randomly split compounds into training (60–70%), validation (10–15%), and test (15–30%) sets. Stratify by activity if possible (ensure all activity ranges are represented in each set). Record the partition for reproducibility.

9. **Fit the regression model.** Common choices:
   - **Linear regression:** y = b₀ + b₁·D₁ + b₂·D₂ + ... (most interpretable)
   - **Nonlinear (polynomial, spline, kernel):** If training R² > 0.95 but test R² < 0.80, nonlinearity may help — but validate carefully (see step 10).
   - Fit only on the training set. Do NOT touch validation or test data.

10. **Cross-validate on training data.** Perform k-fold cross-validation (k=5 or 10). For each fold:
    - Withhold 1/k of training data
    - Fit model on remaining (k-1)/k
    - Predict withheld fold
    - Calculate RMSE, MAE, or R²
    Average metrics across folds. This estimates how the model will generalize. If cross-validated R² < 0.60, the model is weak — consider more/better data or different descriptors.

11. **Evaluate on test set.** Apply the fitted model to compounds never seen during training or cross-validation. Calculate:
    - **R²:** fraction of variance explained
    - **RMSE (root mean squared error):** typical prediction error
    - **MAE (mean absolute error):** mean |predicted − observed|
    - **Slope and intercept of predicted vs. observed plot:** slope near 1 and intercept near 0 indicate unbiased predictions
    Do not optimize the model based on test set performance. Test results should match cross-validation estimates; large gaps indicate overfitting.

12. **Generate prediction intervals.** For each test prediction, report ± confidence interval (e.g., ±1 standard error). This quantifies uncertainty. Narrow intervals on the test set are a good sign; wide intervals on new compounds are a red flag.

### Phase 4 — Interpretation and Applicability

13. **Analyze descriptor contributions.** For a linear model, the fitted coefficients (b₁, b₂, ...) show direction and magnitude of each descriptor's effect:
    - Positive coefficient: higher descriptor value → higher activity
    - Negative coefficient: higher descriptor value → lower activity
    - Large coefficient: large impact on activity
    Create a bar chart of standardized coefficients to visualize relative importance. Do not interpret magnitudes as chemical causation without additional evidence (correlation ≠ causation).

14. **Define applicability domain (AD).** The model is only reliable for compounds similar to the training set. Define AD as:
    - Descriptor ranges: min and max of each training descriptor. Flag test compounds outside these ranges.
    - Leverage: For each test compound, compute its Mahalanobis distance to training set centroid (or use simpler distance metrics). High leverage = high prediction uncertainty.
    Report how many test compounds fall outside AD. Predictions for AD-violating compounds should be flagged as extrapolations.

15. **Document mechanistic assumptions.** Write 2–3 sentences on what the model *does* assume about mechanism (e.g., "This model assumes activity is driven by cell permeability and target binding, not off-target effects"). This is not a proof of mechanism, only a check that the inferred relationship is chemically plausible.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Biological endpoint is defined with units and assay platform | Y/N |
| Dataset has ≥20 compounds (≥50 preferred) with documented sources | Y/N |
| No duplicate structures; outliers reviewed and justified (kept or removed) | Y/N |
| Descriptor redundancy screened; |r| > 0.95 pairs removed | Y/N |
| Training/validation/test partition is random and documented | Y/N |
| Cross-validated R² on training data ≥ 0.60 | Y/N |
| Test set R² ≥ 0.60 and agrees with cross-validated estimate (gap < 0.15) | Y/N |
| Test set predictions show unbiased slope (0.9–1.1) and near-zero intercept | Y/N |
| Applicability domain is defined and applied to all predictions | Y/N |
| Each descriptor and its coefficient is interpretable (linear model) or justified (nonlinear) | Y/N |

## Red Flags

- Test set R² is much lower than cross-validated R² (gap > 0.20). The model overfit the training data. Reduce descriptor count, increase training set size, or use regularization.
- All descriptors have similar coefficient magnitudes. Either the descriptors are collinear (despite the redundancy screen) or the model is degenerate. Investigate pairwise correlations again.
- Prediction intervals are uniform across the test set (no variation). The model is not accounting for local uncertainty. Use heteroscedastic methods (e.g., quantile regression) or residual analysis.
- Applicability domain is never invoked. The model will be applied to compounds far outside training chemistry, leading to unreliable predictions. AD definition and enforcement is mandatory.
- The fitted coefficients contradict known medicinal chemistry (e.g., positive coefficient for a known toxicity driver). This suggests the descriptor is a proxy for a true cause, not the cause itself. Tighten the mechanism interpretation.
- Dataset contains only active compounds or only inactive compounds (no range). The model cannot learn the relationship; it will predict a constant. Ensure activity spread.

## Output Format

```
## QSAR Model Report

**Biological Endpoint:**
<assay name, measurement, units, platform>

**Dataset Summary:**
- Training compounds: _
- Test compounds: _
- Activity range: _ to _ <units>
- Outliers flagged and handled: <Y/N>

**Selected Descriptors:**
| Descriptor | Type | Univariate r | Coefficient | Interpretation |
|---|---|---|---|---|
| <name> | <lipophilicity/size/HBond/etc> | <value> | <value> | <increases/decreases activity> |

**Model Performance (Test Set):**
- R²: _
- RMSE: _ <units>
- MAE: _ <units>
- Slope (predicted vs. observed): _
- Intercept: _
- N compounds: _

**Cross-Validation (Training):**
- k-fold CV (k=_): R² = _, RMSE = _

**Applicability Domain:**
- Descriptor ranges: <min–max for each descriptor>
- Test compounds outside AD: _ of _ (flagged)
- Leverage analysis: <summary of high-leverage outliers>

**Mechanistic Interpretation:**
<2-3 sentences on what structural features drive activity and any known limitations of the model>

**Sample Predictions:**
| Compound | Predicted Activity | 95% CI | In AD? |
|---|---|---|---|
| <SMILES or ID> | _ <units> | ±_ | Y/N |

**Confidence:**
<high/medium/low> — <justification, e.g., "high: R² = 0.82, test agreement with CV, 60 compounds, validated mechanism"> or <"low: R² = 0.55, high prediction error, small dataset">
```
