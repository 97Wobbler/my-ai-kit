---
name: ml-test-score
display_name: ML Test Score
class: lens
underlying_class: native
domain: ai
source: D. Breck, S. Polyzotis, S. Roy, S. E. Whang, M. Zinkevich (Google); "The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction" (2017)
best_for:
  - Assessing production readiness of ML systems
  - Identifying technical debt in deployed models
  - Establishing a shared quality baseline across ML teams
one_liner: "Quantify tech debt in production ML using the 28-item ML Test Score checklist."
---

# ML Test Score

## Overview
The ML Test Score is a 28-item rubric that evaluates whether an ML system is production-ready and maintainable. Rather than binary pass/fail, each test is scored on a 3-point scale (0: not satisfied, 1: partially satisfied, 2: fully satisfied), producing a composite score out of 56 points. Practitioners use this when deploying models to production, when assessing inherited systems for technical debt, or when establishing baseline quality expectations across teams. The discipline is the systematic coverage — most teams audit only the obvious tests (does the model work?) and miss the operational ones (can we detect when it breaks?).

## Analytical Procedure

### Phase 1 — Model Tests (8 tests)

1. **Does the model have a versioning system?** Verify that every model artifact (weights, hyperparameters, training data version) can be uniquely identified and recalled. Score 0 if no versioning exists, 1 if partial (e.g., only model weights versioned), 2 if complete versioning across all artifacts.

2. **Are there automated tests for the training pipeline?** Check whether the pipeline (data ingestion → preprocessing → training → evaluation) has unit tests and integration tests. Score 0 if none, 1 if only a few components tested, 2 if all stages have automated tests with failure detection.

3. **Is the model's performance benchmarked against simple baselines?** Verify the model is compared to: a null model (e.g., mean prediction), a simple heuristic, and a standard off-the-shelf baseline. Score 0 if no baselines exist, 1 if one baseline is tested, 2 if all three are present and documented.

4. **Does the model validation avoid overlapping training/test data?** Confirm that train/validation/test splits are non-overlapping and temporally ordered (for time-series). Score 0 if contamination is possible, 1 if splits exist but temporal order is unclear, 2 if splits are documented and validated to be non-overlapping.

5. **Is the model tested on examples from the production distribution?** Collect examples from the live environment and run inference on them. Score 0 if only historical/offline data tested, 1 if some live examples tested, 2 if a systematic sample of production data is tested regularly.

6. **Does the model handle edge cases and outliers explicitly?** Document how the model handles: missing values, extreme feature values, inputs outside training distribution. Score 0 if no handling exists, 1 if some cases handled, 2 if all edge cases have defined behavior with tests.

7. **Are inference-time dependencies documented?** List every external service, data source, or resource the model needs at prediction time (feature stores, databases, APIs). Score 0 if not documented, 1 if partially documented, 2 if complete with fallback strategies.

8. **Is the model interpretable or explainable for its use case?** For high-stakes decisions, verify that model predictions can be explained to users. Use SHAP, LIME, or domain-specific methods. Score 0 if unexplainable, 1 if post-hoc explanations exist, 2 if model is inherently interpretable or explanations are validated for reliability.

### Phase 2 — Data Tests (7 tests)

9. **Is the data collection process documented?** Write a data specification: schema, sources, collection method, sample rate, time window. Score 0 if no documentation, 1 if partial (missing some details), 2 if complete with provenance.

10. **Are there schema and type checks on input data?** Implement automated validation: required fields present, types correct, value ranges valid. Score 0 if no checks, 1 if some fields checked, 2 if all fields validated at ingestion.

11. **Is the data validated for statistical properties?** Test: label distribution (balanced?), feature distributions (skew, outliers?), correlations (multicollinearity?). Score 0 if no statistical validation, 1 if some properties checked, 2 if comprehensive statistical profiling with alert thresholds.

12. **Are missing values handled and documented?** For each field, document the missing data rate and the strategy (drop, impute, default). Score 0 if no documentation, 1 if some fields documented, 2 if all fields have explicit handling with recorded rates.

13. **Is data versioning in place?** Tie every trained model to a specific dataset version. Score 0 if data is not versioned, 1 if data snapshots exist but not linked to models, 2 if model-data pairs are immutable and retrievable.

14. **Are there automated tests for data quality?** Run validation queries or checks on every new batch: expected schema, no unexpected nulls, distribution shift detection. Score 0 if no automation, 1 if manual checks exist, 2 if continuous automated validation with alerting.

15. **Is the training data representative of production?** Sample data from the live environment and compare its distribution to training data using statistical tests (e.g., Kolmogorov-Smirnov). Score 0 if no check, 1 if ad-hoc comparison, 2 if systematic distribution monitoring with defined thresholds.

### Phase 3 — Feature Tests (4 tests)

16. **Are features documented with definitions and code?** For each feature, write: business definition, type, source, expected range, update frequency. Link to code that computes it. Score 0 if no documentation, 1 if partial (missing some features), 2 if all features fully documented with links to source.

17. **Are features tested for staleness or missing values in production?** Automated checks: Do features arrive on time? What % are null? When was the last update? Score 0 if no checks, 1 if manual monitoring, 2 if automated alerts for staleness and nullness thresholds.

18. **Are features validated for consistency across training and serving?** Run the exact same feature code in training and at prediction time. Periodically compare: do the same inputs produce the same features in both paths? Score 0 if not validated, 1 if occasional spot-checks, 2 if continuous validation with alerts on divergence.

19. **Is there a feature store or registry tracking which features are used by which models?** Maintain a map of: model → [feature1, feature2, ...]. Score 0 if no registry, 1 if manual list, 2 if automated registry with dependency tracking.

### Phase 4 — Monitoring and Maintenance Tests (5 tests)

20. **Is model performance monitored in production?** Measure: accuracy, precision, recall, or task-specific metrics on live data. If ground truth is delayed, use proxy metrics. Score 0 if no monitoring, 1 if monitored manually or with long latency, 2 if real-time monitoring with defined SLOs and alerts.

21. **Is data distribution shift detected?** Use statistical tests or ML-based detectors to identify when live data differs significantly from training data. Score 0 if no detection, 1 if ad-hoc detection, 2 if continuous monitoring with automated alerts and defined thresholds.

22. **Is the model's prediction latency tracked?** Monitor p50, p95, p99 inference time. Set targets and alerts. Score 0 if not tracked, 1 if tracked without alerts, 2 if SLOs defined and violations trigger alerts.

23. **Is there a rollback or retraining plan?** Document: When is retraining triggered? How quickly can the model be reverted? Is the previous model version always available? Score 0 if no plan, 1 if plan exists but untested, 2 if plan is tested and documented with runbooks.

24. **Are there automated tests on model retraining?** When a new model is trained, automatically check: Does it outperform the current production model? Is performance degradation acceptable? Score 0 if no tests, 1 if tests exist but are manual, 2 if fully automated with automatic promotion/blocking.

### Phase 5 — Infrastructure Tests (4 tests)

25. **Is the model serving infrastructure logged and monitored?** Log every prediction request (or a statistical sample) with: input, output, latency, timestamp. Monitor logs for errors and anomalies. Score 0 if no logging, 1 if partial logging, 2 if comprehensive logging with anomaly detection.

26. **Can the model serving system gracefully handle prediction failures?** Define fallback behavior: return cached prediction, serve a default, reject the request with clear error. Score 0 if no fallback, 1 if partial fallback, 2 if all failure modes have documented fallbacks.

27. **Is the model serving infrastructure load-tested?** Verify capacity at 2× expected peak load. Score 0 if not tested, 1 if tested but results not documented, 2 if tested, documented, and alerts set before saturation.

28. **Are there tests for dependency failures?** Inject failures in external dependencies (feature store, database, APIs) and verify the model gracefully degrades or fails safely. Score 0 if no failure testing, 1 if tested manually, 2 if chaos tests automated and run regularly.

## Evaluation Criteria

| Check | Pass |
|---|---|
| All 28 tests were scored (none skipped) | Y/N |
| Each test received a 0, 1, or 2 score (no partial credit within a test) | Y/N |
| Scores are defensible with evidence (code, documentation, test results) | Y/N |
| At least one test from each phase was scored 2 (production-ready) | Y/N |
| Total score is calculated correctly (sum out of 56) | Y/N |
| Major gaps identified (any section with average < 1.0) | Y/N |

## Red Flags

- All tests are scored 0 or 1, with no 2s anywhere. The system is not yet production-ready; do not deploy until at least 20 tests are scored 2.
- Model tests (Phase 1) average < 1.0 but Data tests (Phase 2) average > 1.5. The model itself is under-validated while data pipelines are mature — invert this priority.
- Phases 3 and 4 (Features and Monitoring) are neglected. Features will silently decay and production failures will be invisible.
- Scores are not tied to evidence. "Fully satisfied" (2) claimed without documentation, code, or test results is a red flag for assessment integrity.
- Total score > 40 but Monitoring tests (Phase 4) average < 1.0. The system is mature but blind in production — this is a common failure mode.
- No test in Phase 5 (Infrastructure) is scored 2, but the model is in heavy traffic. Failure modes are untested; incidents are likely.

## Output Format

```
## ML Test Score Assessment

**System being evaluated:** <name/version>
**Evaluation date:** <YYYY-MM-DD>
**Evaluator:** <name>

### Phase 1 — Model Tests (max 16 points)
| Test | Score | Evidence | Notes |
|---|---|---|---|
| 1. Versioning | 0/1/2 | <documentation, registry, or code link> | |
| 2. Pipeline tests | 0/1/2 | | |
| 3. Baseline comparison | 0/1/2 | | |
| 4. Train/test isolation | 0/1/2 | | |
| 5. Production data testing | 0/1/2 | | |
| 6. Edge case handling | 0/1/2 | | |
| 7. Dependency documentation | 0/1/2 | | |
| 8. Interpretability | 0/1/2 | | |
| **Phase 1 Subtotal** | **/16** | | |

### Phase 2 — Data Tests (max 14 points)
| Test | Score | Evidence | Notes |
|---|---|---|---|
| 9. Data collection documented | 0/1/2 | | |
| 10. Schema validation | 0/1/2 | | |
| 11. Statistical validation | 0/1/2 | | |
| 12. Missing value handling | 0/1/2 | | |
| 13. Data versioning | 0/1/2 | | |
| 14. Data quality tests | 0/1/2 | | |
| 15. Production distribution check | 0/1/2 | | |
| **Phase 2 Subtotal** | **/14** | | |

### Phase 3 — Feature Tests (max 8 points)
| Test | Score | Evidence | Notes |
|---|---|---|---|
| 16. Feature documentation | 0/1/2 | | |
| 17. Staleness/null monitoring | 0/1/2 | | |
| 18. Train/serve consistency | 0/1/2 | | |
| 19. Feature registry | 0/1/2 | | |
| **Phase 3 Subtotal** | **/8** | | |

### Phase 4 — Monitoring Tests (max 10 points)
| Test | Score | Evidence | Notes |
|---|---|---|---|
| 20. Performance monitoring | 0/1/2 | | |
| 21. Distribution shift detection | 0/1/2 | | |
| 22. Latency tracking | 0/1/2 | | |
| 23. Rollback/retraining plan | 0/1/2 | | |
| 24. Retraining tests | 0/1/2 | | |
| **Phase 4 Subtotal** | **/10** | | |

### Phase 5 — Infrastructure Tests (max 8 points)
| Test | Score | Evidence | Notes |
|---|---|---|---|
| 25. Serving infrastructure logging | 0/1/2 | | |
| 26. Failure fallback | 0/1/2 | | |
| 27. Load testing | 0/1/2 | | |
| 28. Dependency failure testing | 0/1/2 | | |
| **Phase 5 Subtotal** | **/8** | | |

### Summary
| Phase | Score | % of Max |
|---|---|---|
| Model | **/16** | **%** |
| Data | **/14** | **%** |
| Features | **/8** | **%** |
| Monitoring | **/10** | **%** |
| Infrastructure | **/8** | **%** |
| **TOTAL** | **/56** | **%** |

### Critical Gaps
<List any phase averaging < 1.0 or any test scored 0 in a production system>

### Recommendations
1. <Highest-priority test to bring from 0→1 or 1→2, with effort estimate>
2. ...

### Confidence
<high/medium/low> — <justification: e.g., "high — all 28 tests scored by system owners with documented evidence"; or "medium — some tests self-reported without external audit"; or "low — evaluator unfamiliar with the system's infrastructure">
```
