---
name: differential-diagnosis
display_name: Differential Diagnosis
class: lens
underlying_class: native
domain: medicine
source: William Osler (bedside method, early 1900s); formalized in modern diagnostic algorithms
best_for:
  - Systematic narrowing of multiple candidate diagnoses to identify the most likely and most dangerous
  - Structuring diagnostic reasoning when presentation is ambiguous or overlapping
one_liner: "Enumerate, then narrow by likelihood × severity to prioritize testing."
---

# Differential Diagnosis

## Overview
Differential diagnosis is the systematic process of enumerating plausible diagnoses that match a patient's presentation, then narrowing the list by weighing likelihood (how common is this diagnosis; how well does it fit the data) and severity (what happens if we miss it). Practitioners use this to avoid anchoring on one early hypothesis and to ensure they have considered the dangerous diagnoses — the ones that are rare but fatal if missed. The discipline is the enumeration and the weighing; most errors occur when a clinician skips the enumeration phase or weights likelihood so heavily that severity gets ignored.

## Analytical Procedure

### Phase 1 — Enumerate

1. **State the chief complaint and presenting data clearly.** Write the patient's age, sex, chief complaint (one phrase), duration, and the 3–5 most significant clinical findings (vital signs, physical exam, imaging, labs if available at this stage). Do not pre-interpret. Record data, not conclusions.

2. **Generate the initial differential.** List every diagnosis that could explain the presenting data. Include:
   - Common diagnoses that match the presentation
   - Rare but serious diagnoses that present similarly
   - Diagnoses that match 80% of the data (even if one finding seems odd)
   Do not self-censor. An initially long list is normal; it will be narrowed. Target 6–12 diagnoses.

3. **For each diagnosis, write one sentence describing the mechanism.** Example: "Acute myocardial infarction: coronary thrombosis causing acute transmural ischemia and necrosis." This step clarifies whether you understand the diagnosis or are including it by reflex.

### Phase 2 — Narrow by Likelihood

4. **For each diagnosis, assign a pre-test probability.** Use these anchors:
   - **Very common** (>10% of presentations like this): e.g., viral URI for sore throat
   - **Common** (1–10%): e.g., strep pharyngitis for sore throat
   - **Uncommon** (<1% but recognized): e.g., epiglottitis for sore throat
   - **Rare** (<0.1%, but you know it exists): e.g., retropharyngeal abscess
   
   If you cannot place a diagnosis on this scale in context, drop it — you don't know it well enough to trust your judgment about it.

5. **Check fit to the data.** For each diagnosis, ask:
   - Does it explain the chief complaint? (Y/N)
   - Does it explain the key positive findings? (Y/N for each)
   - Does it explain the key negative findings — the things *not* present that you'd expect if this diagnosis were true? (Y/N)
   
   A diagnosis that explains the positive findings but contradicts the negative findings should be demoted or dropped. Example: Pneumonia would explain fever and cough, but if the chest X-ray is completely clear, pneumonia is unlikely.

6. **Reorder the list by likelihood.** Put the common, good-fit diagnoses at the top. Demote but do not yet delete the rare or poor-fit diagnoses — they will be revisited in Phase 3.

### Phase 3 — Narrow by Severity

7. **For each diagnosis on your list, assign a severity tier:**
   - **Immediately life-threatening** (can kill in minutes to hours without treatment): e.g., tension pneumothorax, septic shock, acute MI
   - **Serious but not immediately fatal** (will cause significant harm if untreated over days/weeks): e.g., bacterial meningitis, PE, acute leukemia
   - **Moderate or self-limited** (causes discomfort or dysfunction but low mortality): e.g., viral URI, muscle strain
   
8. **Apply the "high-sensitivity, low-regret" rule.** Even if a diagnosis is rare (low likelihood), if it is immediately life-threatening or serious, it should remain high on your workup list and be ruled out with targeted testing. This diagnosis should NOT be dropped just because it's uncommon.

   Example: Subarachnoid hemorrhage is rare (<1%) in patients with sudden headache, but it is immediately life-threatening. Do not drop it; rule it out with a specific test (CT, LP if CT negative).

9. **Consolidate into a working differential.** Rank diagnoses by the product of likelihood and severity:
   - Top tier: High likelihood + High severity (rule in or rule out urgently)
   - Second tier: High likelihood + Moderate severity, OR Low likelihood + Very high severity (rule out quickly; if ruled out, move to next tier)
   - Third tier: Low likelihood + Moderate severity (rule out with remaining time/resources)
   - Drop tier: Diagnoses that are both very unlikely AND low severity (acknowledge you thought of them, then explicitly dismiss them)

### Phase 4 — Design the Workup

10. **For each diagnosis in the top two tiers, choose a discriminating test or finding.** The goal is not to confirm the diagnosis but to rule it out efficiently. Prefer:
    - Tests with high sensitivity if the diagnosis is high-severity (you don't want to miss it)
    - Tests with high specificity if the diagnosis is high-likelihood and ruling it in would commit you to major treatment (you don't want false positives driving unnecessary intervention)
    - Tests that are fast, safe, or low-cost when multiple tests compete

11. **Anticipate results and branch.** Write out: "If test A is positive, I will conclude X. If negative, I will conclude Y and move to test B." This prevents reactive, aimless testing.

12. **Document the diagnoses you are ruling out.** Explicitly note the serious diagnoses you have decided do NOT fit the data and briefly state why (e.g., "Meningitis: low risk — patient alert, no neck stiffness, normal WBC"). This creates a record that you considered them.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Initial differential contains 6–12 diagnoses | Y/N |
| Each diagnosis has a mechanism statement (one sentence) | Y/N |
| Each diagnosis is assigned pre-test probability (Very common / Common / Uncommon / Rare) | Y/N |
| Each diagnosis is scored against positive and negative findings | Y/N |
| High-severity diagnoses are retained even if uncommon | Y/N |
| At least 2 serious diagnoses appear in the ruled-out list with justification | Y/N |
| Workup plan branches on anticipated test results (not just lists tests) | Y/N |

## Red Flags

- Differential list contains only 2–3 diagnoses. You are likely anchored on a single hypothesis and are missing systematic enumeration.
- All diagnoses on the list are common. You are weighting likelihood so heavily that rare-but-serious diagnoses are being dropped without explicit consideration.
- Negative findings are not discussed. A diagnosis that contradicts the data (e.g., "no fever" rules out infection) should be demoted or dropped; if it isn't, the narrowing step was skipped.
- High-severity diagnoses appear only in the drop list or are not tested for. This is a safety failure — the method is being used as a speed tool, not a safety tool.
- Workup plan is a list of tests with no logic connecting them (e.g., "Order CBC, CMP, troponin, CT chest"). Tests should be sequential and conditional: "If troponin is normal, I do not order CT. If troponin is elevated, I do."
- Patient age, sex, or key risk factors are not mentioned in the presentation. Without these, pre-test probabilities are guesses.

## Output Format

```
## Differential Diagnosis Assessment

**Presentation:**
Age/Sex: <...>
Chief Complaint: <...>
Duration: <...>
Key Findings: <positive>; <negative>

### Phase 1 — Initial Differential
| Diagnosis | Mechanism | Pre-test Probability |
|---|---|---|
| <...> | <...> | Very common / Common / Uncommon / Rare |

### Phase 2 — Data Fit
| Diagnosis | Explains CC? | Explains +Findings? | Explains −Findings? | Keep? |
|---|---|---|---|---|
| <...> | Y/N | Y/N | Y/N | Y/N |

### Phase 3 — Likelihood × Severity
| Diagnosis | Likelihood | Severity | Tier | Rule Out With |
|---|---|---|---|---|
| <...> | <...> | Immediately life-threatening / Serious / Moderate | Top / Second / Third / Drop | <test or finding> |

### Phase 4 — Workup Plan
1. <Diagnosis 1>: If <test> is <result>, conclude <outcome>. If <opposite result>, proceed to test 2.
2. <Diagnosis 2>: ...

### Ruled-Out Diagnoses
- <Diagnosis>: <brief rationale>
- <Diagnosis>: <brief rationale>

### Confidence
<high | medium | low> — <justification. E.g., "High — presentation is classic for the top diagnosis, serious mimics have been tested, and negative findings support exclusion of the runner-up.">
```
