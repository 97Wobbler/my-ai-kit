---
name: roc-pr-curves
display_name: ROC/PR Curves
class: lens
underlying_class: native
domain: ai
source: Tom Fawcett (ROC analysis, 2006); Jesse Davis and Mark Goadrich (PR curves, 2006)
best_for:
  - Evaluating binary classifiers across thresholds without choosing one upfront
  - Comparing models when class imbalance makes accuracy misleading
  - Understanding precision-recall trade-offs in high-stakes prediction tasks
one_liner: "Threshold-independent classifier evaluation and comparison."
---

# ROC/PR Curves

## Overview
ROC (Receiver Operating Characteristic) and PR (Precision-Recall) curves measure classifier performance across all decision thresholds simultaneously, rather than at a single threshold. ROC plots true positive rate against false positive rate; PR plots precision against recall. Practitioners reach for these when a single accuracy metric would hide poor performance on the minority class, when the cost of false positives differs from false negatives, or when comparing classifiers fairly without committing to a threshold before deployment. PR curves are especially useful for imbalanced datasets; ROC curves show the full trade-off space.

## Analytical Procedure

### Step 1 — Gather predictions and ground truth
1. Obtain a held-out test set with binary labels (positive/negative, 1/0).
2. Run the classifier on the test set and collect soft predictions — the probability or score assigned to the positive class (not binary predictions, but continuous values in [0,1]).
3. Verify that soft predictions are calibrated to [0,1] or monotonic; if the model outputs logits or log-odds, apply sigmoid/softmax first.
4. Confirm that ground truth labels are balanced or note their class distribution for later interpretation.

### Step 2 — Compute threshold-performance pairs
1. **Sort predictions in descending order** by score. Retain the true label paired with each prediction.
2. **For each unique threshold value** (set thresholds to each unique score in the test set, plus 0 and 1):
   - Classify all instances with score ≥ threshold as positive; others as negative.
   - Count true positives (TP), false positives (FP), true negatives (TN), false negatives (FN).
   - Compute metrics:
     - **For ROC:** TPR = TP / (TP + FN), FPR = FP / (FP + TN)
     - **For PR:** Precision = TP / (TP + FP), Recall = TP / (TP + FN)
   - Record the (FPR, TPR) pair for ROC and (Recall, Precision) pair for PR.
3. Handle the edge case where TP + FP = 0 (no positive predictions at high thresholds): precision is undefined; use 1.0 by convention or omit the point.

### Step 3 — Plot and compute area under curve (AUC)
1. **Plot ROC curve:** FPR on x-axis (0 to 1), TPR on y-axis (0 to 1). Connect the threshold-pairs in order of decreasing threshold (upper-left corner = high threshold, all negatives; lower-right corner = low threshold, all positives).
2. **Plot PR curve:** Recall on x-axis (0 to 1), Precision on y-axis (0 to 1). Same threshold ordering applies.
3. **Compute AUC (Area Under Curve)** for each:
   - Use the trapezoidal rule: AUC = Σ[(x_{i+1} - x_i) × (y_{i+1} + y_i) / 2] over consecutive points.
   - ROC-AUC ranges [0, 1]; 0.5 = random classifier, 1.0 = perfect.
   - PR-AUC ranges [0, 1]; for imbalanced data, the baseline (always predicting positive) is not 0.5 but the positive class fraction. Use this baseline as a sanity check.
4. **Record both AUC values.**

### Step 4 — Identify operating points and trade-offs
1. **On the ROC curve,** mark the points corresponding to standard thresholds (e.g., 0.5, 0.7) and note the TPR and FPR at each.
2. **On the PR curve,** do the same.
3. **Compare the curves visually:** If one curve is consistently above the other, that model dominates. If curves cross, models are optimal at different thresholds.
4. **Estimate the threshold for your task:**
   - Identify the cost of FP and FN in your application (e.g., "false alarm costs 10× false negative").
   - On the ROC curve, find the threshold where cost(FP) × FPR + cost(FN) × FNR is minimized.
   - Alternatively, on the PR curve, choose the threshold that balances acceptable precision and recall for your use case.

### Step 5 — Validate and interpret
1. **Sanity checks:**
   - At threshold 0, TPR and Recall = 1.0 (all positives correctly labeled as positive); FPR, Precision = positive class fraction.
   - At threshold 1.0, TPR = 0, Recall = 0, FPR = 0, Precision = undefined.
   - For imbalanced data, PR-AUC should be compared to the baseline (positive fraction); PR-AUC > baseline means the model is better than "always positive."
2. **Compare models:** If two models have ROC-AUCs that differ by < 0.02, the difference may not be statistically significant; bootstrap or cross-validate to confirm.
3. **Document the chosen threshold** and its corresponding precision, recall, and FPR in the final model card or deployment spec.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Soft predictions (not hard class labels) are provided | Y/N |
| Threshold-pairs computed for ≥10 distinct score values | Y/N |
| Both ROC and PR curves plotted or AUCs computed | Y/N |
| AUC values reported with ≥3 decimal places | Y/N |
| Baseline (random / always-positive) noted for comparison | Y/N |
| Operating point (chosen threshold) mapped to precision/recall/FPR | Y/N |

## Red Flags

- Thresholds generated by binning predictions (e.g., [0–0.1], [0.1–0.2]) instead of using unique score values. This discards information and produces jagged curves.
- PR curve rises sharply at low recall then crashes at high recall. This usually signals extreme class imbalance or a broken precision calculation (numerator/denominator flipped).
- ROC-AUC = 0.5 and PR-AUC = 0.5. Likely causes: (a) predictions are random, (b) labels and predictions are inverted, (c) the classifier ignores features.
- Precision reported as 1.0 at all thresholds. This happens when TP + FP is always ≤ 1 (test set too small) or precision was clamped incorrectly.
- Curves cross drastically or show non-monotonic behavior. Indicates misaligned score/label order or a threshold-setting bug. Recompute and verify threshold direction.
- No baseline cited for comparison. For imbalanced data, reporting PR-AUC = 0.75 without baseline (which might be 0.9) is misleading.

## Output Format

```
## ROC/PR Curve Assessment

**Dataset summary:**
- Test set size: N
- Positive class fraction: P%
- Baseline precision (always positive): P%

### ROC Curve
- Points computed: <number>
- ROC-AUC: <value, 3 decimals>
- Interpretation: <classifier vs. random>

### PR Curve
- Points computed: <number>
- PR-AUC: <value, 3 decimals>
- Baseline (always positive): <baseline AUC>
- Interpretation: <model outperforms baseline / underperforms baseline>

### Operating Point Analysis
| Threshold | TPR | FPR | Precision | Recall |
|---|---|---|---|---|
| <chosen> | <...> | <...> | <...> | <...> |

**Threshold rationale:** <business case or cost justification>

### Model Comparison (if applicable)
| Model | ROC-AUC | PR-AUC | Dominant region | Notes |
|---|---|---|---|---|
| <...> | <...> | <...> | <...> | <...> |

### Red Flags
- <any observed>
- <any observed>

### Confidence
<high/medium/low> — <justification: e.g., "high — curves computed from 1000+ test samples with ≥50 positive instances; baseline established; no data anomalies detected">
```
