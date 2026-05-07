---
name: clinical-decision-rules
display_name: Clinical Decision Rules
class: lens
underlying_class: native
domain: medicine
source: Wells (PE risk stratification, 1995); CURB-65 (pneumonia severity, 2003); Ottawa Ankle Rules (fracture risk, 1992); and subsequent structured scoring frameworks in emergency medicine
best_for:
  - Triaging patients to appropriate care level (emergency vs. outpatient)
  - Reducing overtesting and unnecessary admissions
  - Standardizing clinical judgment across providers
one_liner: "Standardized score-based clinical judgment to reduce overtreatment and optimize care pathways."
---

# Clinical Decision Rules

## Overview
A Clinical Decision Rule is a decision-support tool that combines patient history, examination findings, and test results into a scoring algorithm that predicts the probability of a specific outcome (diagnosis, severity, prognosis) and recommends a management pathway. Practitioners use these when they need to reduce subjective variation, lower unnecessary testing or admission, or stratify risk in high-volume settings. The rule is only useful if it is valid (tested on real populations), simple enough to remember or calculate quickly, and actionable (the output changes what you actually do).

## Analytical Procedure

### Phase 1 — Validate the Rule's Derivation

1. **Identify the outcome the rule predicts.** What disease or severity state is it predicting? Be specific: not "pneumonia" but "pneumonia requiring ICU admission" or "30-day mortality." Check that this outcome is clinically meaningful and that the rule was originally derived on a population similar to yours.

2. **Locate the derivation study.** Find the original paper in which the rule was developed. Verify:
   - Sample size (minimum 100 cases; fewer is underpowered)
   - Population (age, setting, inclusion/exclusion criteria — does it match your patient population?)
   - Outcome definition (how was the outcome measured and verified?)
   - Statistical method (logistic regression, decision tree, or expert consensus?)

3. **Check for validation studies.** Has the rule been prospectively validated on *independent* populations (not the same cohort used to derive it)? Rules validated only on their derivation cohort often overestimate performance. Note the number of validation studies and whether they are from your setting.

4. **Identify the variables the rule uses.** List each predictor (clinical finding, lab value, vital sign). For each, confirm:
   - How it is measured (clinical judgment vs. objective test)
   - Whether it is readily available in your setting
   - Whether any special equipment or expertise is needed
   - The inter-observer agreement if it is subjective (kappa ≥0.60 is acceptable)

5. **Examine the scoring system.** Is the rule a points-based score, a decision tree, or a probability calculator? Verify that the scoring is consistent (e.g., Does a 15-point score always map to the same risk category, or does the threshold differ by subgroup?).

### Phase 2 — Evaluate Clinical Performance

6. **Determine the rule's sensitivity and specificity on the target population.** 
   - Sensitivity = proportion of patients with the outcome who are correctly identified by the rule (few false negatives)
   - Specificity = proportion of patients without the outcome who are correctly ruled out (few false positives)
   - If published data are from a different population, note that your local performance may differ

7. **Assess the clinical consequences of misclassification:**
   - If the rule is *overly sensitive* (few false negatives, many false positives): patients without the outcome are over-admitted, over-tested, or over-treated. Cost: unnecessary intervention and anxiety.
   - If the rule is *overly specific* (few false positives, many false negatives): patients with the outcome are undertreated or discharged inappropriately. Cost: morbidity, mortality, liability.
   - Which error is more costly in your clinical context?

8. **Check for subgroup differences.** Do sensitivity and specificity hold across age, sex, comorbidity, and socioeconomic status? Some rules perform differently in subgroups (e.g., elderly patients, pregnant patients). If subgroup performance data are missing, note this as a limitation.

### Phase 3 — Assess Implementation Barriers

9. **Test the rule in practice.** Does it actually reduce inappropriate workup or admission, or does clinician intuition override it? Run a small prospective audit (20–50 patients) to check:
   - Is the rule used? (Or do providers ignore it in favor of judgment?)
   - Is it calculated correctly?
   - Does the recommended action match the outcome (e.g., did low-risk patients actually do well without admission)?
   - What reasons did providers give for overriding the rule?

10. **Identify system barriers:**
    - Are all variables easily accessible in the EMR, or do clinicians have to search or calculate by hand?
    - Does the rule integrate with your triage workflow, or does it require a separate step?
    - Do providers distrust the rule because it conflicts with their experience (even if their experience is biased)?

### Phase 4 — Measure Local Impact

11. **Establish a baseline.** Before implementing, measure the current admission/testing rate for the target condition. Document the current outcome (e.g., How many admitted patients actually had the disease? How many discharged patients had adverse events?).

12. **Implement and monitor.** Track:
    - Proportion of eligible patients for whom the rule was applied
    - Changes in admission/testing rates
    - Patient outcomes (diagnosis rate, adverse events, readmission, mortality)
    - Clinician compliance and barriers to use
    
13. **Recalibrate if necessary.** If local sensitivity or specificity differ significantly from published data, recalculate thresholds on your own population (if sample size permits) or adjust your confidence in the rule.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Outcome predicted by the rule is specific and clinically meaningful | Y/N |
| Rule was derived on ≥100 patients in a relevant population | Y/N |
| At least one independent prospective validation study exists | Y/N |
| All variables in the rule are clearly defined and easily measured | Y/N |
| Sensitivity and specificity are documented for your population | Y/N |
| Clinical consequences of misclassification are explicitly discussed | Y/N |
| Rule has been tested in your clinical setting (prospective audit completed) | Y/N |
| Baseline admission/outcome rates are measured before implementation | Y/N |

## Red Flags

- The rule was derived on a tiny sample (n < 50) or only validated on the derivation cohort — external validity is unknown.
- Sensitivity and specificity are not reported, or only the positive predictive value (PPV) is given — you cannot assess how many patients are missed or over-treated.
- The rule uses subjective variables (e.g., "clinician judgment of severity") with no reported inter-observer agreement — different clinicians will score differently.
- Published performance comes from a specialty center (academic ICU, tertiary referral), but your setting is primary care or the emergency department — rule performance may be worse.
- Providers consistently override the rule because it conflicts with their intuition — either the rule is truly inappropriate for your population or clinicians need better education and feedback on outcomes.
- Baseline and post-implementation metrics are not compared — you cannot tell if the rule actually changed practice or outcomes.
- The rule recommends an action (e.g., "admit if score ≥ 2") but no outcome data are provided to justify that threshold.

## Output Format

```
## Clinical Decision Rule Assessment

**Condition and outcome:**
<specific diagnosis or severity outcome the rule predicts>

**Rule name and source:**
<e.g., Wells Scoring for PE, CURB-65 for CAP>

### Phase 1 — Rule Derivation and Validation

**Derivation sample:**
- N = <...>
- Population: <age, setting, inclusion/exclusion>
- Outcome: <definition and verification method>

**Validation:**
- <N independent validation studies; cite key study>
- Performance in your population: <sensitivity and specificity, if known>

**Variables included:**
| Variable | Measurement | Inter-observer agreement (if subjective) |
|---|---|---|
| <...> | <...> | <...> |

**Scoring system:**
<points-based, decision tree, or calculator; describe how to apply>

### Phase 2 — Clinical Performance

**Sensitivity (rule's ability to identify patients with outcome):**
<% from derivation and validation studies; note if lower in your population>

**Specificity (rule's ability to rule out patients without outcome):**
<% from derivation and validation studies>

**Clinical consequence of false positives (over-testing/admission):**
<cost and burden>

**Clinical consequence of false negatives (missed diagnosis):**
<morbidity/mortality risk>

**Subgroup performance:**
<any variation by age, sex, comorbidity, or setting? note if unknown>

### Phase 3 — Implementation in Your Setting

**Prospective audit (20–50 patients):**
- Rule used in <N/%> of eligible patients
- Correctly calculated: <Y/N; note any errors>
- Outcome match: <% of low-risk correctly discharged, % of high-risk correctly admitted>
- Clinician override reasons: <list top 3>

**System barriers:**
- Variable availability in EMR: <accessible/difficult>
- Workflow integration: <seamless/requires separate step>
- Clinician trust: <high/moderate/low — why?>

### Phase 4 — Local Outcomes

**Baseline (pre-implementation):**
- Admission rate for target condition: <...%>
- Diagnostic yield (% of admitted with confirmed outcome): <...%>
- Adverse events in discharged patients: <...>

**Post-implementation (after 3+ months):**
- Admission rate: <...%> (change: +/- <...%>)
- Diagnostic yield: <...%>
- Adverse events in discharged patients: <...>
- Rule applied to <...%> of eligible patients

**Recalibration (if applicable):**
- Local sensitivity: <...%>
- Local specificity: <...%>
- Thresholds adjusted: <Y/N; describe>

### Confidence
<high | medium | low> — <justification: derivation and validation quality, local performance data, applicability to your population, implementation barriers>
```
---
