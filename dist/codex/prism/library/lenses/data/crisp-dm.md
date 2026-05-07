---
name: crisp-dm
display_name: CRISP-DM
class: lens
underlying_class: native
domain: data
source: Shekel Shmueli, Nitin R. Patel, Peter C. Bruce; IBM, SPSS, 2000
best_for:
  - Structuring end-to-end data science projects with clear handoff points
  - Ensuring stakeholder alignment across business, data, and deployment phases
  - Reducing rework by explicit validation before phase transitions
one_liner: "Six-phase iterative data-science process from business understanding to deployment."
---

# CRISP-DM

## Overview
CRISP-DM (Cross-Industry Standard Process for Data Mining) is a six-phase iterative workflow that moves from business problem to deployed model. Unlike waterfall, it treats feedback loops and rework as expected — after deployment, outcomes inform the next cycle. Practitioners use it to avoid the gap between lab-built models and business value, and to clarify who owns what decision at each stage. The discipline is phase discipline: knowing when one phase ends, what artifact proves it, and what must be true before moving forward.

## Analytical Procedure

### Phase 1 — Business Understanding

1. **State the business goal in plain language, with success metric.** Not "build a model." Examples: "Reduce customer churn within 12 months by identifying at-risk accounts and routing them to retention"; "Cut fraud losses by 20% within 6 months by flagging suspicious transactions in real time." Write the metric as <outcome>, <target%, <timeframe>.

2. **List all stakeholders by role and verify alignment.** Rows: business owner, data owner, compliance/legal, ML engineer, ops team. For each, record: What success looks like to them? What failure costs them? Any conflicting metrics? (Example: Recall = 95% helps the business but ops teams worry about false positive load.)

3. **Document constraints and non-negotiables:**
   - **Latency:** Is prediction needed in real time (< 100ms), batch (daily), or ad-hoc (on request)?
   - **Interpretability:** Does the model need to explain *why* it predicted X? (Regulatory, stakeholder trust, fairness audit.)
   - **Data availability:** What data exists, how often is it refreshed, who controls access?
   - **Resource limits:** Budget, compute, personnel hours, calendar deadline.
   - **Regulatory:** GDPR, HIPAA, fairness constraints, explainability mandates.

4. **Define success and failure modes.** Not just accuracy. Record: What is the cost of a false positive? A false negative? Example: False positive (wrongly flag account as fraud) costs $50 in ops work; false negative costs $5000 in fraud loss. True positive saves $5000. Use this to set precision/recall targets later.

### Phase 2 — Data Understanding

5. **Inventory all raw data sources.** For each, record: what it measures, row count, schema, freshness, ownership, access control. Identify gaps (data you need but don't have).

6. **Exploratory data analysis — structured.** Do NOT skip; this uncovers surprises:
   - **Distribution check.** For each feature: is it normal, bimodal, heavily skewed? Outliers present? (Outliers are either signal or noise; you must decide.) Document with histograms/box plots.
   - **Missingness.** For each column, what % is null? Is it random or systematic (e.g., missing for a cohort)? Is null itself informative?
   - **Correlation structure.** Which features correlate with the target? Which with each other (multicollinearity)? Are relationships linear or nonlinear?
   - **Data quality flags.** Impossible values (age = 999), inconsistencies (same person with two genders across tables), recent schema changes.

7. **Check for target leakage.** Ask: "If I had this feature, would I need a model?" Example: predicting loan default with feature "currently in default" = leakage. Walk through each feature with the data owner: "Would we have this *before* we need to make the decision?"

### Phase 3 — Data Preparation

8. **Clean and transform.** Document every step:
   - Handle nulls: impute (mean, forward-fill, domain rule), drop rows, or keep as a category?
   - Encode categoricals (one-hot, ordinal, embedding).
   - Scale/normalize numerics if your algorithm requires it.
   - Create derived features (ratios, temporal shifts, aggregations). Justify each: why does this feature likely predict the target?
   - For time-series data, ensure no future leakage: if predicting at time T, all features are as-of time T-lag, not T.

9. **Create train/validation/test split.** For time-series: chronological split (train on past, validate on recent past, test on future). For i.i.d. data: stratified random split. Record the split logic; you will need to reproduce it for production.

10. **Baseline sanity check.** Before model building, train a trivial baseline (mean predictor, logistic regression on raw features, random classifier). Record its performance. If your fancy model doesn't beat it by a meaningful margin, the signal may be too weak.

### Phase 4 — Modeling

11. **Build and tune candidate models.** For each model:
    - Algorithm choice (tree, linear, neural net, ensemble): justify based on problem structure (classification vs. regression, linear vs. nonlinear patterns, interpretability need).
    - Hyperparameter tuning: grid search, random search, or Bayesian optimization. Record the parameter space and the best values found.
    - Cross-validation: does performance hold across folds, or does it collapse on certain subsets (sign of overfitting or distribution shift)?

12. **Evaluate on validation set against the metrics you defined in Phase 1.** Not just accuracy — report precision, recall, AUC, or whatever you committed to. Compare to the success threshold (e.g., "model must have 90% recall on at-risk accounts").

13. **Error analysis.** Where does the model fail?
    - False positives: What do these cases have in common? Are they acceptable (low cost) or deal-breakers (high cost)?
    - False negatives: Same question. Example: Model misses 2% of churners. Are they a hard subpopulation (older users, inactive) or random noise?
    - If failures cluster on a subgroup, you may need a separate model or a fairness constraint.

14. **Check for drift.** Does the model perform equally on recent data as on past data? If recent data is systematically different, you need a more robust model or a retraining schedule.

### Phase 5 — Evaluation

15. **Hold-out test set evaluation.** Do NOT touch the test set during tuning. Evaluate the final model once, on unseen data. Record the result. This is your honest estimate of production performance.

16. **Sanity checks for deployment readiness:**
    - Does the model meet the latency requirement? (Can it score 10k requests per day in real time, or does it need batch?)
    - Are predictions interpretable enough for the stakeholder (business owner, regulator)? Can you explain why the model scored account X as high-risk?
    - Does the model degrade gracefully when data is missing or malformed?
    - Have you documented the features, their transformations, and the model weights/coefficients for the ops team?

17. **Compare model to business baseline.** Not the statistical baseline — the current business process. Example: "Today, we manually review all accounts for churn risk. This model flags the top 500 to review instead. Do we save time and money?" Quantify: if model precision is 65%, we review 325 true positives and 175 false positives. Manual review cost is $100/account, so we save 8,500 hours of review. False positive cost is $50/account, so we lose $8,750 to false positives. Net gain: huge.

### Phase 6 — Deployment & Monitoring

18. **Plan the deployment.** Record:
    - Environment (batch job, API, embedded in application).
    - Schedule (real-time, daily, weekly).
    - Rollout strategy (full, canary, shadow).
    - Who monitors? What metrics? What triggers a rollback?

19. **Monitor model performance in production.** Track:
    - **Prediction distribution.** Does the model still output the same class balance, or has it shifted? (Shift = possible data drift.)
    - **Feature distribution.** Have new users, products, or cohorts changed the input data?
    - **Business outcome.** Is churn actually dropping? Are false positives causing harm? Is the model meeting the success metric from Phase 1?

20. **Set a retraining trigger.** When does the model become stale enough to retrain? Options: on a schedule (monthly, quarterly), when a performance metric drops below a threshold, or when input data drifts significantly. Document the trigger so ops doesn't have to guess.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Business goal is stated with outcome, target %, and timeframe | Y/N |
| All stakeholders are identified and their conflicting metrics recorded | Y/N |
| Constraints (latency, interpretability, data, regulatory) are explicit | Y/N |
| Success and failure costs are quantified (Phase 1) | Y/N |
| Data sources are inventoried; gaps identified (Phase 2) | Y/N |
| EDA covers distribution, missingness, leakage, and quality checks (Phase 2) | Y/N |
| Target leakage was explicitly checked and ruled out (Phase 3) | Y/N |
| Train/validation/test split strategy is documented (Phase 3) | Y/N |
| A baseline model was built and recorded (Phase 3) | Y/N |
| Model performance is reported against Phase 1 metrics, not just accuracy (Phase 4) | Y/N |
| Error analysis identifies failure patterns and their cost (Phase 4) | Y/N |
| Test set was held-out and evaluated once (Phase 5) | Y/N |
| Model is compared to current business process, not null (Phase 5) | Y/N |
| Deployment environment, schedule, and rollout strategy are documented (Phase 6) | Y/N |
| Monitoring plan includes prediction drift, feature drift, and business outcome (Phase 6) | Y/N |

## Red Flags

- Phase 1 metric is "high accuracy" with no business outcome. You are optimizing the wrong thing.
- No baseline model built. You have no way to know if the model is actually useful.
- Test set was used during hyperparameter tuning. The performance number is fake.
- Error analysis is missing or generic ("the model made mistakes"). You don't know where it fails or why.
- Model deployment plan says "we'll monitor it" with no specifics on metrics, frequency, or rollback criteria. Ops will not know what to do.
- Fairness analysis is absent, despite the model making decisions about people (credit, hiring, churn risk). Expect regulatory trouble.
- No plan to retrain. Models decay; stale models fail silently.

## Output Format

```
## CRISP-DM Assessment

**Business Goal:**
<outcome, target %, timeframe>

**Success Metric:**
<metric to optimize for>

**Failure Cost:**
False positive: $<cost>  |  False negative: $<cost>

### Phase 1 — Business Understanding
| Stakeholder | Success = | Failure Cost | Conflict with Others? |
|---|---|---|---|
| <role> | <...> | <...> | Y/N |

**Constraints:**
- Latency: <real-time / batch / ad-hoc>
- Interpretability required: <Y/N>
- Regulatory constraints: <list or "none">

### Phase 2 — Data Understanding
**Data sources:**
- <source>: <row count>, <freshness>, <ownership>

**EDA findings:**
- Distribution: <summary of key patterns>
- Missingness: <% null, systematic or random>
- Leakage: <ruled out or flagged>
- Data quality: <issues found or "clean">

### Phase 3 — Data Preparation
**Transformations:**
1. <step>
2. <step>

**Train/validation/test split:** <strategy>

**Baseline model performance:** <metric = value>

### Phase 4 — Modeling
**Models evaluated:**
| Model | Precision | Recall | AUC | Interpretation |
|---|---|---|---|---|
| <name> | <%> | <%> | <value> | <...> |

**Best model:** <name>

**Error analysis:**
- False positives: <pattern>, cost <$>
- False negatives: <pattern>, cost <$>
- Subgroup failures: <if any>

### Phase 5 — Evaluation
**Hold-out test performance:**
<metric = value>

**vs. Business baseline (current process):**
<quantified improvement or "worse than status quo">

**Deployment readiness:**
- Latency requirement met: Y/N
- Interpretability adequate: Y/N
- Graceful degradation: Y/N

### Phase 6 — Deployment & Monitoring
**Deployment plan:**
- Environment: <batch / API / embedded>
- Schedule: <real-time / daily / on-demand>
- Rollout: <full / canary / shadow>

**Monitoring plan:**
- Prediction drift check: <metric and frequency>
- Feature drift check: <metric and frequency>
- Business outcome check: <metric and frequency>

**Retraining trigger:** <schedule or threshold>

### Confidence
<high | medium | low> — <justification: e.g., "high because Phase 1 success metric is quantified, data is clean, test set shows 5% improvement over baseline"; or "low because data leakage was found in feature engineering and error analysis shows model fails on 30% of highest-risk cohort">
```
