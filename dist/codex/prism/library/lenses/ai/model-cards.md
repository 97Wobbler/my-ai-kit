---
name: model-cards
display_name: Model Cards
class: lens
underlying_class: native
domain: ai
source: Mitchell et al., Google Research, 2019 ("Model Cards for Model Reporting")
best_for:
  - Documenting model capabilities and limitations systematically
  - Surfacing fairness and performance blindspots before deployment
  - Communicating model behavior to non-technical stakeholders
one_liner: "Document intended use, performance, and limitations of a model for responsible deployment."
---

# Model Cards

## Overview
A Model Card is a one-to-two page documentation artifact that records a model's intended use, performance characteristics across demographic groups and use conditions, and known limitations. Instead of burying model behavior in research papers or leaving it implicit, the Card makes it explicit and queryable. Practitioners use this when releasing models to production, auditing for fairness risk, or onboarding new teams to inherited models. The discipline is exhaustiveness — most teams document the 60% case and omit the 40% of edge cases and failure modes where the model deteriorates.

## Analytical Procedure

### Phase 1 — Model Specification

1. **Write the model's intended use in one sentence.** Specify the task (classification, regression, generation), the user (who operates it), and the decision it informs. Example: "Predicts loan approval probability to assist human loan officers at regional banks in consumer lending decisions."

2. **List the input and output specifications.**
   - Input: data type, shape, range, preprocessing applied. Example: "Credit history vector (12 features, normalized 0-1), income (log-scaled), debt-to-income ratio."
   - Output: format, range, interpretation. Example: "Probability score 0-1; score > 0.7 → recommended approval."

3. **Document the training dataset.** Record: size, source, time period collected, demographic composition (if labeled: gender, race, age bins), and any filtering applied. Be honest about gaps. Example: "10M loan applications from 2018-2020, 72% male applicants, underrepresented in rural regions."

4. **Specify model architecture and training procedure.** Name the model class (linear, tree, neural net, etc.), hyperparameters used, optimization objective, and train/validation/test split. Include the date the model was finalized.

### Phase 2 — Performance Characterization

5. **Measure overall performance on the test set.** Report at least three metrics:
   - One task-specific metric (accuracy, AUC, RMSE, etc.)
   - Precision and recall (for classification)
   - Fairness-relevant metric (false positive rate, false negative rate by demographic group)
   
   Record the threshold or decision rule used if applicable.

6. **Measure performance across demographic groups.** Disaggregate the metrics from step 5 by:
   - Gender, race, age, income level, geography — whichever groups are relevant to the use case and present in the data
   - Any intersections (e.g., "low-income women") if the sample size permits (n > 30 per cell)
   
   Create a table with groups as rows and metrics as columns. Flag any disparity > 5 percentage points.

7. **Measure performance across use conditions.** Test the model on:
   - Data outside the training time period (temporal shift): use the same test metric on data from 6 months after training cutoff
   - Data from sources not represented in training (domain shift): if the model was trained on bank A's loans, test on bank B's loans
   - Underrepresented subsets from the test set (e.g., applicants over 65, applicants in rural areas)
   
   For each condition, report the primary metric and note the % drop from test-set baseline.

8. **Document failure modes.** For each metric or demographic group where performance drops ≥ 10%, write:
   - What examples failed? (Show 3-5 concrete cases if possible)
   - What pattern do the failures share? (Systematic blindspot or random noise?)
   - Why did the model fail? (Training data gap, feature encoding, model capacity, etc.)
   - Can it be fixed? (Answer: "Yes, retrain with X" or "No, fundamental tradeoff" or "Unknown")

### Phase 3 — Limitations and Recommendations

9. **List what the model was NOT designed to do.** Explicit negations: "This model was not trained to detect fraud." "It should not be used for automated (human-out) decisions." "Performance is unknown for applicants with no credit history."

10. **For each known limitation, propose a mitigation.** Format:
    - Limitation: <description>
    - Mitigation: <concrete action (e.g., "flag for manual review", "retrain quarterly", "use only in contexts where...", "combine with another signal")>
    - Owner: <team or role responsible>
    - Cadence: <when to revisit (e.g., "quarterly" or "when deployment context changes")>

11. **Specify monitoring requirements.** If deployed, what metrics will be tracked in production? How often? What is the alert threshold for drift or degradation? Example: "Track approval rate by demographic group monthly; alert if any group deviates > 3 percentage points from Q4 2024 baseline."

12. **Identify stakeholders and conflicts.** List:
    - Who is affected by this model (loan applicants, loan officers, bank, regulators)?
    - Are there conflicting interests? (Speed of decision vs. fairness? Volume vs. accuracy?)
    - How are conflicts resolved? (Specific policy, tradeoff statement, etc.)

## Evaluation Criteria

| Check | Pass |
|---|---|
| Intended use is specified as a single sentence with task, user, and downstream decision | Y/N |
| Input and output specifications are precise enough to reproduce the model call | Y/N |
| Training dataset documented: size, source, time period, demographic composition | Y/N |
| Performance measured across at least 3 metrics on overall test set | Y/N |
| Performance disaggregated by ≥2 demographic groups | Y/N |
| Performance tested under ≥2 use conditions (temporal or domain shift) | Y/N |
| Every metric or demographic disparity ≥5 percentage points is flagged | Y/N |
| Failure modes include concrete examples (not just summary statistics) | Y/N |
| At least 3 explicit "NOT designed for" statements present | Y/N |
| Every limitation has a proposed mitigation with owner and cadence | Y/N |
| Monitoring specification includes metric, frequency, and alert threshold | Y/N |
| Stakeholder conflicts are named, not hidden | Y/N |

## Red Flags

- "Performance is 92% accurate" reported without demographic disaggregation. Aggregate metrics hide unfairness.
- No failure modes documented. Either the model is worse than claimed, or the analysis wasn't rigorous enough to find them.
- Limitations section says "None identified" or is left blank. Every model has blindspots; missing them is a red flag for insufficient testing.
- Monitoring section is generic or empty. "We'll monitor it" without specifying what, how often, and what triggers action means the model is uncontrolled post-deployment.
- Intended use is vague ("assist decision-making") or omits the human's role. Clarity on whether the model is advisory or autonomous is critical.
- Training data demographics are not reported. If you don't know the composition, you can't explain disparities.
- Stakeholder conflicts are not named. Pretending they don't exist is a governance failure.
- No mitigation for known failures. A limitation with no path to address it is an unmanaged risk.

## Output Format

```
# Model Card: <Model Name>

## Model Details
- **Developed by:** <team/organization>
- **Model date:** <finalization date>
- **Model type:** <architecture>
- **Intended use:** <one sentence: task, user, downstream decision>
- **Input specification:** <data type, shape, range, preprocessing>
- **Output specification:** <format, range, interpretation, decision threshold if any>

## Training Data
- **Dataset size:** <number of examples>
- **Source:** <where data came from>
- **Time period:** <when collected>
- **Demographic composition:** <% by gender, race, age, other relevant groups>
- **Data filtering/exclusions:** <what was removed and why>

## Performance

### Overall Metrics (Test Set)
| Metric | Value |
|---|---|
| <Primary metric (e.g., AUC)> | <value> |
| Precision | <value> |
| Recall | <value> |
| False Positive Rate | <value> |

### Performance by Demographic Group
| Group | Primary Metric | FPR | FNR | Sample Size |
|---|---|---|---|---|
| <group1> | <value> | <value> | <value> | <n> |
| <group2> | <value> | <value> | <value> | <n> |
| <disparity noted> | <value> | <value> | <value> | <n> ⚠️ |

### Performance Under Use Conditions
| Condition | Primary Metric | Change from Test | Notes |
|---|---|---|---|
| Temporal shift (6mo post-training) | <value> | <% change> | <observation> |
| Domain shift (alternate source) | <value> | <% change> | <observation> |
| Underrepresented subgroup | <value> | <% change> | <observation> |

## Known Limitations

### Failure Mode Analysis
**Failure:** <description>
- **Examples:** <3-5 concrete cases>
- **Pattern:** <what the failures have in common>
- **Root cause:** <why the model failed>
- **Mitigation:** <fixable? how?>

### Out-of-Scope Uses
- This model was NOT designed for <use1>.
- It should NOT be used for <use2>.
- Performance is UNKNOWN for <condition>.

## Recommendations

| Limitation | Mitigation | Owner | Cadence |
|---|---|---|---|
| <limitation> | <action> | <team> | <frequency> |

## Monitoring
- **Metrics to track:** <metric1, metric2, ...>
- **Tracking frequency:** <daily/weekly/monthly>
- **Alert threshold:** <drift or degradation threshold>
- **Responsible team:** <team name>

## Stakeholders and Conflicts
- **Affected parties:** <who is impacted>
- **Conflicting interests:** <speed vs. fairness, etc.>
- **Resolution:** <how conflicts are adjudicated>

### Confidence
**<high | medium | low>** — <justification (e.g., "Confidence is high on overall metrics but medium on fairness assessment due to limited racial diversity in training data; temporal validation pending Q2 2026 data")>
```
---
