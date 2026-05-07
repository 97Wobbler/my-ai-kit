---
name: confusion-matrix-p-r-f1
display_name: Confusion Matrix + P/R/F1
class: lens
underlying_class: native
domain: ai
source: Confusion matrix (Kohavi & Provost, 1998); Precision/Recall/F1 (van Rijsbergen, 1979; Powers, 2011)
best_for:
  - Evaluating binary or multiclass classifiers beyond accuracy
  - Diagnosing class imbalance and type I/II error trade-offs
  - Selecting thresholds when cost of false positives differs from false negatives
one_liner: "Diagnose real classifier performance beyond accuracy using precision, recall, and F1."
---

# Confusion Matrix + P/R/F1

## Overview
A confusion matrix is a cross-tabulation of true labels against predicted labels, exposing not just overall accuracy but the distribution of error types: false positives (FP), false negatives (FN), true positives (TP), true negatives (TN). From this matrix, precision, recall, and F1 quantify different failure modes — precision penalizes false alarms, recall penalizes missed cases, F1 balances both. Practitioners reach for this lens when accuracy alone hides poor performance on the minority class or when the cost of one error type dwarfs the other.

## Analytical Procedure

### Phase 1 — Build the Confusion Matrix

1. **Collect predictions and ground truth labels.** Use a held-out test set (not training data). Record both the predicted class and the true class for every sample.

2. **For binary classification, construct a 2×2 table:**
   ```
            Predicted Positive    Predicted Negative
   Actual Positive       TP                 FN
   Actual Negative       FP                 TN
   ```
   - **TP (True Positive):** Predicted positive, actually positive.
   - **FP (False Positive):** Predicted positive, actually negative (type I error).
   - **FN (False Negative):** Predicted negative, actually positive (type II error).
   - **TN (True Negative):** Predicted negative, actually negative.

3. **For multiclass (N classes), construct an N×N table** where rows are true labels and columns are predicted labels. Fill cell (i, j) with the count of samples with true label i predicted as label j.

4. **Verify the matrix sums to the total test set size.** Check: TP + FP + FN + TN = |test set|.

### Phase 2 — Compute Precision, Recall, F1

5. **Calculate Precision (P):**
   ```
   P = TP / (TP + FP)
   ```
   Answers: "Of all cases the model predicted as positive, what fraction were actually positive?" High precision means few false alarms.

6. **Calculate Recall (R):**
   ```
   R = TP / (TP + FN)
   ```
   Answers: "Of all actual positive cases, what fraction did the model catch?" High recall means few missed positives.

7. **Calculate F1 Score:**
   ```
   F1 = 2 * (P * R) / (P + R)
   ```
   The harmonic mean of P and R; treats both equally. F1 = 1 is perfect; F1 = 0 means at least one of P or R is zero.

8. **For multiclass, choose an aggregation strategy:**
   - **Macro:** Average P, R, F1 across all classes equally (each class weighted 1/N).
   - **Weighted:** Average P, R, F1 across all classes, weighted by class frequency in the test set.
   - **Micro:** Pool all TP, FP, FN across classes, then compute P, R, F1 globally.

### Phase 3 — Interpret for Asymmetric Costs

9. **Identify which error matters more.** For each use case, determine:
   - Cost of false positive (e.g., sending a spam filter alert to a legitimate message).
   - Cost of false negative (e.g., missing a spam message).

10. **Prioritize metric based on cost asymmetry:**
    - If FP >> FN (e.g., medical screening): prioritize **Precision** — you'd rather miss some positives than generate false alarms that consume resources.
    - If FN >> FP (e.g., disease detection, fraud): prioritize **Recall** — you'd rather flag some false positives and investigate than miss true cases.
    - If FP ≈ FN: use **F1** as a single summary.

11. **Check for class imbalance.** Compare the ratio of positive to negative cases in the test set. If > 9:1 or < 1:9, accuracy alone will mislead; the confusion matrix and P/R/F1 reveal the imbalance's impact.

### Phase 4 — Document Per-Class Behavior (Multiclass Only)

12. **For each class, extract its row and column from the confusion matrix.**
    - The row (true label) shows where this class's instances ended up; off-diagonal counts are misclassifications.
    - The column (predicted label) shows what the model mistook for this class.

13. **Identify confusion pairs:** Which classes are most frequently confused with each other? This guides feature engineering or retraining focus.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Confusion matrix dimensions match the number of classes | Y/N |
| Matrix sums to total test set size | Y/N |
| Precision, Recall, F1 computed for all classes or globally | Y/N |
| Aggregation method (macro/weighted/micro) is stated for multiclass | Y/N |
| Cost asymmetry between FP and FN is identified | Y/N |
| At least one metric (P, R, or F1) is prioritized based on the use case | Y/N |

## Red Flags

- Accuracy is the only reported metric and the test set has class imbalance. The matrix and P/R/F1 have not been examined.
- Precision and Recall are both reported as "good" but neither matches the stated use case. (e.g., Recall = 95% for a system where missed positives are catastrophic, but Precision = 60%.)
- F1 is reported without specifying macro vs. weighted aggregation in multiclass. The single number masks per-class variation.
- The confusion matrix is not actually shown, only P/R/F1 numbers. The matrix is the diagnostic tool; the numbers are summaries of it.
- FN count is zero or negligible in a recall-critical application (e.g., fraud detection). Either the threshold is too lenient or the metric is being gamed.
- No test set / matrix built on training data. Overfitting hides the true behavior.

## Output Format

```
## Confusion Matrix + P/R/F1 Assessment

**Test Set Size:** <N>
**Class Distribution:** <e.g., "Positive: 150 (15%), Negative: 850 (85%)">

### Confusion Matrix
<2x2 or NxN table with TP, FP, FN, TN labeled>

### Metrics (Binary)
| Metric | Value | Interpretation |
|---|---|---|
| Precision | <P> | <proportion of predicted positives that were correct> |
| Recall | <R> | <proportion of actual positives that were caught> |
| F1 Score | <F1> | <harmonic mean> |
| Accuracy | <(TP+TN)/(TP+FP+FN+TN)> | <baseline; may be inflated if imbalanced> |

### Metrics (Multiclass — aggregation: macro/weighted/micro)
| Class | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| <class_1> | <P> | <R> | <F1> | <count> |
| <class_2> | <P> | <R> | <F1> | <count> |

### Cost Analysis
**Use Case:** <e.g., "fraud detection">
**Cost of False Positive:** <description and relative weight>
**Cost of False Negative:** <description and relative weight>
**Prioritized Metric:** <Precision / Recall / F1> — <justification>

### Confusion Pairs (Multiclass)
<List most frequent off-diagonal confusions, e.g., "Class A predicted as Class B: 23 times">

### Diagnosis
<Summary of what the matrix and metrics reveal about model behavior, including:
- Which error type dominates (FP vs. FN)?
- Is any class systematically misclassified?
- Does the prioritized metric meet the use case threshold?
- Recommended next steps (retrain, adjust threshold, gather more data for minority class, etc.)>

### Confidence
<high | medium | low> — <justification, e.g., "high — test set is held-out, N=1000, stratified sampling; imbalance is moderate (8:2)">
```
---
