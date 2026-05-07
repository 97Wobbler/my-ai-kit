---
name: cognitive-forcing-strategies
display_name: Cognitive Forcing Strategies
class: lens
underlying_class: native
domain: medicine
source: Pat Croskerry, emergency medicine and cognitive error research, 2003–present
best_for:
  - Breaking anchoring bias in diagnostic reasoning
  - Reducing premature closure in clinical decision-making
  - Forcing re-examination of working diagnoses before committing to treatment
one_liner: "Forced cognitive reappraisal procedures that break diagnostic bias."
---

# Cognitive Forcing Strategies

## Overview

Cognitive Forcing Strategies are deliberate checkpoints that interrupt the natural flow of diagnostic reasoning to prevent anchoring on an initial hypothesis and missing alternative diagnoses. They are most useful in high-stakes, time-constrained environments like emergency medicine where the cost of diagnostic error is patient harm. The practitioner applies them when the initial working diagnosis feels "complete" but hasn't been genuinely stress-tested against competing alternatives or hasn't been examined for inconsistency with the full clinical picture.

## Analytical Procedure

### Phase 1 — Establish the Current Working Diagnosis

1. **Write the leading diagnosis in plain language.** State it as a specific pathophysiologic entity, not a symptom (not "chest pain" but "acute myocardial infarction" or "spontaneous coronary artery dissection").

2. **List the clinical findings that support it.** Include vital signs, physical exam, imaging, labs, and history elements. Be specific: not "tachycardia" but "heart rate 112, BP 145/88, JVD present."

3. **Note the pathway to this diagnosis.** What was the clinical sequence? Did the patient present with classic features or atypical ones? Was this diagnosis considered first or did it emerge after ruling others out? This reveals anchoring tendency.

### Phase 2 — Force Reconsideration (Croskerry's Core Strategies)

Choose and apply at least **two** of the following forcing functions:

#### Strategy A: The Competing Diagnosis Requirement
4a. **Generate the three most plausible alternative diagnoses** that fit at least 70% of the presenting signs and could cause the same chief complaint. Do not generate strawmen. Use differential diagnosis templates if available (e.g., VINDICATE for abdominal pain: Vascular, Infection, Neoplasm, Drugs, Inflammatory, Congenital, Allergic, Trauma, Endocrine).

4b. **For each alternative, explicitly state which clinical findings it explains and which it does NOT explain.** Complete mismatch with one or two findings is acceptable; unexplained findings should be flagged.

#### Strategy B: The Red Flag Interrogation
4c. **Ask: "If I am wrong about this diagnosis, what would change my mind?"** List 3–5 findings that, if present or absent, would falsify the working diagnosis. This is deliberate vulnerability-seeking.

4d. **Search the chart, physical exam, and available imaging for those exact findings.** Document what you found. If any red flags are present, re-weight the working diagnosis downward.

#### Strategy C: The Atypical Presentation Check
4e. **Confirm whether the presentation is classic or atypical for the leading diagnosis.** If atypical (e.g., infarction without chest pain, appendicitis without RLQ tenderness), apply heightened skepticism and require stronger evidence for the diagnosis.

#### Strategy D: The Risk Stratification Anchor
4f. **Identify the worst plausible outcome** if the diagnosis is wrong. For example, if working diagnosis is anxiety but the worst outcome is missed acute coronary syndrome, pause and apply a rule-out strategy (e.g., troponin, ECG) even if the diagnosis feels likely.

4g. **Apply a standardized risk tool** for that worst outcome if one exists (e.g., HEART score for ACS, Ottawa ankle rules for fracture). Document whether the patient meets high-risk criteria.

### Phase 3 — Synthesis and Decision

5. **Revisit the working diagnosis.** Given the alternatives, red flags, and risk stratification, is the working diagnosis still the most likely? Is the confidence the same? Has it shifted?

6. **If confidence has **not** shifted materially, document why the alternatives were rejected.** Be explicit: "STEMI ruled out because troponin negative, no ECG changes, and symptom onset was 36 hours ago." Vague reasoning is a sign the forcing strategy failed.

7. **If confidence **has** shifted, revise the working diagnosis and the plan accordingly.**

8. **If uncertainty remains unresolved, choose a rule-out strategy** (additional test, observation, escalation) rather than committing to the working diagnosis. Document the explicit trigger for escalating or changing course.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Working diagnosis stated as a specific entity, not a symptom | Y/N |
| Clinical findings listed with specificity (values, locations, timing) | Y/N |
| At least 2 cognitive forcing strategies were applied | Y/N |
| Each competing alternative was examined against the full clinical picture | Y/N |
| Red flags or falsifying conditions were explicitly sought | Y/N |
| Risk stratification tool applied if worst-case outcome was high-stakes | Y/N |
| Final reasoning includes explicit rejection or revision of working diagnosis | Y/N |

## Red Flags

- Working diagnosis is defended by listing *only* supporting findings. Any omission of alternative explanations is a sign the interrogation was incomplete.
- The competing diagnoses in Strategy A are implausible strawmen (e.g., "could be a brain tumor") rather than genuine alternatives that fit the presentation.
- Red flags in Strategy B are vague ("something unexpected") or do not actually conflict with the working diagnosis.
- Risk stratification in Strategy D is skipped because "the diagnosis is clear." Clarity and safety are different; high-stakes scenarios demand both.
- The final diagnosis is identical to the initial working diagnosis with no revision. Either the forcing strategies found nothing (unlikely) or they were performative (more likely).
- No documentation of why alternatives were rejected. Silent elimination of competing diagnoses is the definition of premature closure.

## Output Format

```
## Cognitive Forcing Assessment

**Working Diagnosis (specific entity):**
<diagnosis>

**Clinical Presentation:**
- Findings supporting diagnosis: <list>
- Pathway to diagnosis: <description>

### Phase 2 — Forcing Strategies Applied

#### Strategy A: Competing Diagnoses
1. <Alternative 1>
   - Explains: <findings>
   - Does NOT explain: <findings>
2. <Alternative 2>
   - Explains: <findings>
   - Does NOT explain: <findings>
3. <Alternative 3>
   - Explains: <findings>
   - Does NOT explain: <findings>

#### Strategy B: Red Flags
Findings that would falsify working diagnosis:
1. <specific finding or absence>
2. <specific finding or absence>
3. <specific finding or absence>

Sought in chart: <yes/no, findings documented>

#### Strategy C: Typicality Check
Presentation is [classic | atypical] for this diagnosis because: <reason>

#### Strategy D: Risk Stratification
Worst plausible outcome if wrong: <outcome>
Risk tool applied: <tool name and score>
High-risk category: <yes/no>

### Phase 3 — Synthesis

**Revised working diagnosis:**
<same as initial | modified | escalated for rule-out>

**Confidence shift:** <increased | same | decreased | uncertain>

**Rationale for alternative rejection or revision:**
<explicit reasoning; do not omit>

**Next action:**
<commit to plan | apply rule-out strategy | escalate>

### Confidence
<high/medium/low> — <justification grounded in whether alternatives were genuinely addressed and risk was managed>
```
