---
name: osemn
display_name: OSEMN
class: lens
underlying_class: native
domain: data
source: Hilary Mason (2010s); formalized in "Doing Data Science"
best_for:
  - End-to-end data analysis workflows
  - Structuring ad-hoc exploratory work into repeatable phases
  - Identifying which stage of analysis is bottlenecking insight
one_liner: "Five-step analysis workflow from data collection to interpretation."
---

# OSEMN

## Overview
OSEMN breaks down data analysis into five sequential phases: Obtain raw data, Scrub it into a usable form, Explore for patterns, Model for prediction or causality, and iNterpret findings back to domain context. Practitioners use this lens when starting an analysis with vague requirements and need a checkpoint framework to avoid getting lost in tools or technique. The discipline is knowing which phase you are in and what exits that phase before entering the next.

## Analytical Procedure

### Phase 1 — Obtain

1. **Define the data you need.** Write:
   - The business question or hypothesis (one sentence)
   - What entity or event you are measuring (user? transaction? sensor reading?)
   - What time period or population scope
   - What granularity (per-user, per-day, per-pixel?)

2. **List all available data sources.** For each, record:
   - Source name and type (API, database, file dump, sensor)
   - Lag (how fresh is it? real-time? daily batch?)
   - Format (JSON, CSV, Parquet, etc.)
   - Access cost or restrictions

3. **Select sources that cover the question.** If a source is missing, note it as "data debt" and proceed with what you have or flag the work as blocked.

4. **Extract and store raw data unchanged.** Do not filter, transform, or clean yet. If raw data is >1GB, sample strategically (random? time-stratified? stratified by outcome?) but document the sampling method.

### Phase 2 — Scrub

5. **Audit the raw data for completeness and consistency.** For each column or field:
   - What percent of rows are missing? (null/None/NA)
   - What is the range of values? (min, max, cardinality for strings)
   - What is the data type in the source vs. what you loaded?
   - Are there duplicates or logical impossibilities (negative age, future date)?
   - Are there known encoding issues (character sets, special characters)?

6. **Document every decision rule.** For missing data:
   - If >50% missing, drop the column (unless it's your target). Record why.
   - If 5–50% missing, choose: impute (mean/median/mode/forward-fill?), flag (create a binary missing-indicator?), or drop rows.
   - If <5% missing, usually safe to impute or drop.
   For duplicates, decide: keep first occurrence, aggregate, flag for manual review.

7. **Fix or flag data quality issues.** Examples:
   - Normalize text (case, whitespace, accents)
   - Convert to correct types (string date → datetime)
   - Remove or cap outliers if they are measurement error (not legitimate extremes)
   - Handle categorical variables: code as numeric, one-hot encode, or leave as string?
   
   Keep a log of every transformation. If you changed >10% of values, the dataset is more curated than raw — note this.

8. **Create a "scrubbed" dataset.** This is the input to Explore. It should be clean enough to plot without errors but not yet filtered to the analysis question (that happens in Explore).

### Phase 3 — Explore

9. **Describe each variable univariately.** For each column:
   - Histogram or bar chart (distribution)
   - Summary stats (mean, median, std, quartiles for numeric; counts for categorical)
   - Skew, kurtosis, or dominant categories
   - Visual check for bimodality or heavy tails

10. **Explore relationships between variables.** Generate:
    - Scatterplot matrix (or a subset for high-dimensional data)
    - Correlation matrix (numeric pairs; use Cramér's V or chi-squared for categorical)
    - Segmentation plots (outcome by top categorical variables)
    - Time series plots if your data is temporal

11. **Look for data issues masked by Scrub.** Examples:
    - Are there obvious data quality shifts across time or subgroups?
    - Is one category suspiciously dominant?
    - Do two variables track perfectly (collinearity)?
    - Are distributions wildly different from domain expectation?
    If you find issues, loop back to Scrub.

12. **Generate hypotheses.** Note 3–5 patterns or relationships that are worth modeling. Example: "users in region X churn 40% more; let's test if this is causal or confounded by age."

### Phase 4 — Model

13. **Choose a model class** suited to your question:
    - Supervised regression (numeric outcome): linear, tree-based, neural net?
    - Supervised classification (binary/multiclass): logistic, random forest, SVM?
    - Unsupervised (no outcome): clustering, dimensionality reduction, anomaly detection?
    - Causal inference (isolate treatment effect): randomized trial, matching, IV, DAG?

14. **Train/test split:** Reserve at least 20% of data for held-out evaluation (temporal split if time-series).

15. **Fit the model.** Log:
    - Hyperparameters used
    - Training time and convergence
    - Feature importance or coefficients (which inputs matter most?)
    - In-sample error (train), out-of-sample error (test)
    - Bias–variance diagnosis: is the model underfitting or overfitting?

16. **Validate against the hypothesis.** Does the model confirm or contradict your Explore findings? If contradiction, reconcile it — you may have misread the pattern or the model may have captured confounding.

17. **Document model limits.** What assumptions did you make? What population is this model valid for? When does it fail?

### Phase 5 — iNterpret

18. **Translate model outputs to domain language.** Do not say "coefficient = 0.23". Say "a one-unit increase in X is associated with a 23% increase in Y, holding Z constant" or "this cluster is 60% likely to be high-value users."

19. **Connect findings to the business question.** Restart from step 1. Does your analysis answer it? What is the recommendation?

20. **Quantify uncertainty.** Report confidence intervals, p-values, or prediction intervals where applicable. Avoid point estimates without bounds.

21. **Identify next steps.** What data is missing? What assumption is most fragile? What would change the recommendation?

## Evaluation Criteria

| Check | Pass |
|---|---|
| Each of the five phases has documented outputs | Y/N |
| Obtain: raw data is stored separately and unchanged | Y/N |
| Scrub: every data cleaning decision is logged with justification | Y/N |
| Explore: univariate and bivariate summaries exist for all variables | Y/N |
| Model: train/test split was used; test performance is reported | Y/N |
| iNterpret: findings are stated in domain terms, not model terms | Y/N |
| Uncertainty is quantified (confidence intervals, p-values, ranges) | Y/N |

## Red Flags

- Obtain and Scrub are conflated; data is cleaned during extraction, so raw data is lost.
- Explore is skipped entirely; analysis jumps straight from Scrub to Model, and patterns are discovered *after* fitting.
- Scrub decisions are not logged; six months later, no one knows why 40% of rows were dropped.
- Model choice is unjustified ("I tried five models, this one had the best accuracy on train set").
- iNterpret restates model outputs literally ("the coefficient on feature_12 is 0.089") rather than translating to business logic.
- No test/validation set; model error is reported on training data only.
- Uncertainty is absent; findings are stated as certainties ("users in region X churn") without confidence intervals or caveats.

## Output Format

```
## OSEMN Analysis Report

### 1. Obtain
**Data question:**
<one sentence>

**Selected sources:**
| Source | Type | Lag | Format | Access cost/notes |
|---|---|---|---|---|
| <...> | <...> | <...> | <...> | <...> |

**Missing data (debt):**
<list any required data not available>

**Raw data stored:** <path or reference>

### 2. Scrub
**Completeness audit:**
| Column | Missing % | Data type | Issues | Decision |
|---|---|---|---|---|
| <...> | <...> | <...> | <...> | <...> |

**Transformations applied:**
1. <rule and justification>
2. ...

**Scrubbed dataset:** <path or reference>

### 3. Explore
**Univariate summaries:**
| Variable | Type | Summary | Visual pattern |
|---|---|---|---|
| <...> | <...> | <...> | <...> |

**Key relationships:**
- <relationship 1: description and chart reference>
- <relationship 2>
- ...

**Hypotheses for modeling:**
1. <hypothesis based on patterns>
2. ...

### 4. Model
**Model class:** <type and justification>

**Train/test split:** <% held-out; method (random/temporal/stratified)>

**Results:**
- Train error: <metric and value>
- Test error: <metric and value>
- Top features/coefficients: <list>

**Bias–variance:** <underfitting | balanced | overfitting>

**Validation against hypotheses:** <do findings match Explore?>

### 5. iNterpret
**Domain translation:**
1. <Finding in business terms>
2. ...

**Uncertainty quantification:**
<confidence intervals, p-values, or ranges for each finding>

**Answer to data question:**
<explicit yes/no or recommendation, grounded in findings>

**Next steps:**
- <missing data or assumption to verify>
- ...

### Confidence
<high | medium | low> — <justification>
```
```
