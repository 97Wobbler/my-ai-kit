---
name: nnt
display_name: Number Needed to Treat
class: model
underlying_class: native
domain: medicine
source: Laupacis et al., "How should we measure the success of joint replacement surgery?," The Journal of Rheumatology, 1991; popularized in evidence-based medicine via Sackett et al., Evidence-Based Medicine, 1997
best_for:
  - Quantifying the clinical benefit of a treatment in absolute terms
  - Comparing the practical impact of competing interventions
  - Making treatment decisions when baseline risk varies across patients
one_liner: "Number Needed to Treat — express treatment effect as absolute risk reduction for concrete clinical decisions."
---

# Number Needed to Treat

## Overview

Number Needed to Treat (NNT) is a metric that translates the relative risk reduction (RRR) of a treatment into the absolute number of patients who must be treated to prevent one adverse outcome. Its core claim is that relative risk reduction alone obscures the actual clinical burden and benefit: a drug that reduces risk by 50% is worthless if baseline risk is 0.2%, but life-changing if baseline risk is 40%. NNT makes the absolute impact transparent and actionable. The model is descriptive and practical — it reframes trial efficacy data into a quantity clinicians and patients can reason about directly. Unlike relative measures, NNT changes with baseline risk, forcing an honest conversation about whom the treatment actually helps.

## Core Variables and Relationships

NNT is calculated from two key inputs:

1. **Absolute Risk Reduction (ARR)** — the difference in event rates between intervention and control groups:
   - ARR = (event rate in control) − (event rate in intervention)
   - ARR is measured in percentage points or proportions (e.g., 0.15 means 15 percentage points).

2. **Baseline (control) event rate** — the probability that the bad outcome occurs without treatment:
   - Higher baseline risk → lower NNT (same RRR has bigger absolute effect).
   - Lower baseline risk → higher NNT (same RRR matters less).

The core identity is:

    NNT = 1 / ARR

If a trial shows event rate of 20% in control and 10% in treatment, ARR = 0.10 (10 percentage points), so NNT = 10. Conversely, if control is 2% and treatment is 1%, ARR = 0.01, so NNT = 100 — the same 50% relative reduction, but vastly different clinical impact.

## Key Predictions

- **The same RRR produces wildly different NNTs depending on baseline risk.** A 50% RRR for a condition with 40% baseline risk yields NNT ≈ 5; for a condition with 2% baseline risk, NNT ≈ 100. Clinical meaning is not in the RRR; it is in the NNT.

- **Treatment decisions should pivot on baseline risk stratification.** A drug with NNT = 10 for high-risk patients may have NNT = 200 for low-risk patients, making it standard-of-care for one group and wasteful for the other. Relative efficacy hides this.

- **Comparisons between interventions become concrete only when baseline risk is held constant.** Drug A (NNT = 8) appears superior to Drug B (NNT = 12), but only if both are tested in identical baseline-risk populations. A cross-trial comparison without baseline risk adjustment is meaningless.

- **NNT inverts the economics of screening.** A screening test with high sensitivity but low disease prevalence can yield NNT in the thousands for treatment of screen-detected disease, because baseline risk post-screening is still low. Conversely, a test for high-risk enrichment collapses NNT.

- **The inverse, Number Needed to Harm (NNH), becomes comparable to NNT.** If a treatment prevents 1 outcome in 10 treated (NNT = 10) but causes a serious adverse event in 1 in 20 treated (NNH = 20), the benefit-to-harm ratio is 1:0.5 — a modest margin that a patient's preferences should drive.

## Application Procedure

Instantiate NNT to evaluate whether a treatment is worth doing for a specific patient or population.

1. **Identify the patient population and baseline risk.** What is the probability of the bad outcome (hospitalization, stroke, death, relapse) in the absence of treatment, over a specified time horizon (e.g., 5 years)? Baseline risk may come from the control arm of the trial, but better: use the patient's own risk (age, comorbidities, biomarkers). Write it as a percentage or proportion.

2. **Locate the trial or meta-analysis that tested the intervention in this (or a similar) population.** Extract the event rate in the intervention arm and the control arm over the same time horizon. Both must be from the same trial or pooled data — mixing is a common error.

3. **Calculate ARR** = (control event rate) − (intervention event rate). If control is 20% and intervention is 12%, ARR = 0.08.

4. **Calculate NNT** = 1 / ARR. In the example above, NNT = 12.5, round to 13. This is the number of patients you must treat to prevent one event.

5. **Adjust NNT for the actual baseline risk if it differs from the trial population.** If the trial enrolled average-risk patients but your patient is higher-risk, you can estimate a patient-specific NNT using:
   - Patient-specific NNT ≈ (trial NNT) / (patient's baseline risk / trial's baseline risk).
   - This is a rough adjustment; use with caution in extreme cases.

6. **Identify and calculate NNH** for the most common serious adverse effects. Does the trial report this? If not, estimate from safety data in the literature.

7. **Compare NNT to NNH** and to the patient's preferences. Is preventing 1 outcome in 13 patients worth the side effect risk in 1 in 20? This is not a statistical question — it is a values question.

8. **Check boundary conditions** (below). If any apply, flag that NNT may be misleading.

## Boundary Conditions

NNT is a powerful absolute-risk metric but becomes misleading or unhelpful under several conditions:

- **Heterogeneous baseline risk within the trial population.** If the trial enrolls a broad range of risks (say, 5%–40%), the overall NNT is an average that fits no one. Demand subgroup analyses; apply patient-specific baseline risk adjustment, not the trial average.

- **Different time horizons in the trial vs. the clinical scenario.** NNT is time-dependent: preventing 1 event per 10 treated in 1 year is not the same as in 5 years. Always specify the horizon. Extrapolating beyond the trial period is risky.

- **Surrogate outcomes instead of clinical outcomes.** If the trial measured cholesterol reduction (surrogate) rather than myocardial infarction (clinical), the NNT for the surrogate may not translate to NNT for the outcome patients care about. Demand trials of hard endpoints.

- **Rare but catastrophic harms not captured in trial data.** Safety monitoring in trials is often too short or underpowered to detect rare serious events (e.g., 1 in 10,000 risk). NNT from the trial will be too optimistic. Cross-reference with pharmacovigilance and post-marketing data.

- **Multiple outcomes with competing NNTs.** A drug may have NNT = 15 for preventing cardiovascular death but NNT = 200 for preventing quality-of-life decline. The model says nothing about how to trade these off — that is a values call, not a statistical one.

- **Trials in populations that do not match your patient.** A trial of a 65-year-old white male cohort has little predictive power for a 45-year-old woman of different ethnicity, different comorbidities. The extrapolation is a clinical judgment, not a model output.

## Output Format

```
## NNT Analysis: <intervention, outcome, population>

**Intervention:** <drug, dose, duration>
**Outcome:** <clinical event being prevented>
**Patient/Population baseline risk:** <% or proportion over time horizon>
**Time horizon:** <e.g., 5 years>
**Source trial(s):** <citation, or trial name>

### Absolute Risk Reduction
| Group | Event rate | Duration |
|---|---|---|
| Control | <e.g., 20%> | <e.g., 5 years> |
| Intervention | <e.g., 12%> | <same> |
| ARR | <8 percentage points> | |

### Number Needed to Treat
- **NNT:** <13> (one event prevented per 13 treated over 5 years)
- **Patient-adjusted NNT** (if baseline risk differs from trial): <estimate, with caveat>

### Number Needed to Harm
| Adverse Effect | Frequency | NNH |
|---|---|---|
| <e.g., GI bleed> | <1 in 50> | 50 |
| <e.g., rash> | <1 in 10> | 10 |

### Benefit-to-Harm assessment
- NNT vs. NNH: <e.g., 13 vs. 50 for the most serious harm; favorable or not>
- Magnitude of outcome prevented: <e.g., cardiovascular death vs. symptom relief; patient values matter>

### Boundary-condition check
- Trial population match: <good / fair / poor match to your patient>
- Baseline risk heterogeneity in trial: <is subgroup data available?>
- Time horizon fit: <does the trial duration match your clinical horizon?>
- Surrogate vs. clinical outcomes: <hard endpoints or surrogates?>

### Recommendation
<Does the NNT justify treatment given the NNH and the patient's values? This is a clinical judgment, not a model output.>

### Confidence: high | medium | low
<Reasoning: baseline risk stratification in trial + match to patient population + completeness of safety data + stability of effect across subgroups.>
```
