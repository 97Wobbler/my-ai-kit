---
name: soap-notes
display_name: SOAP Notes
class: lens
underlying_class: native
domain: medicine
source: Lawrence Weed (Problem-Oriented Medical Record, 1960s); standard in clinical practice
best_for:
  - Organizing patient encounters into a structured, reproducible format
  - Ensuring clinical decision-making is traceable from observation to plan
one_liner: "Structure patient records into Subjective / Objective / Assessment / Plan to make clinical reasoning auditable."
---

# SOAP Notes

## Overview

SOAP is a four-part structure for documenting patient encounters: Subjective (what the patient reports), Objective (what the clinician measures or observes), Assessment (the clinician's clinical reasoning and diagnosis), and Plan (the intended interventions). The discipline is the separation — Subjective and Objective stay distinct so that bias and inference do not contaminate observation. Practitioners use this to produce records that another clinician can audit, hand off reliably, and defend in court if necessary.

## Analytical Procedure

### Part 1 — Subjective (S)

1. **Record only what the patient or caregiver reported.** Include chief complaint, history of present illness, relevant past medical history, medications, allergies, family history, and social history. Use the patient's own words for symptoms when possible.

2. **Do not interpret or diagnose.** Write "patient reports sharp chest pain for 2 hours" not "patient has angina." Record symptom onset, duration, character, severity (0–10 scale), radiation, aggravating/alleviating factors, and associated symptoms (the "Old Carts" mnemonic: Onset, Location, Duration, Character, Aggravating/Alleviating, Radiation, Timing, Severity).

3. **Flag missing information.** If a standard history element was not obtained, note it: "Denies fever, chills, or night sweats. Alcohol use not assessed."

### Part 2 — Objective (O)

4. **Record vital signs first.** Blood pressure, heart rate, respiratory rate, temperature, oxygen saturation, and weight. Include the date/time and which arm/site if relevant.

5. **Document physical examination findings in system-by-system order.** General appearance, HEENT (head, eyes, ears, nose, throat), neck, lungs, heart, abdomen, extremities, neurological. Write what you observed, not an interpretation: "lung fields clear to auscultation bilaterally" not "lungs normal."

6. **Include relevant diagnostic test results and imaging.** Lab values, ECG, imaging, cultures — include the value, unit, reference range, and date obtained. Do not omit abnormal values and do not suppress normal ones that were specifically checked.

7. **Use standardized terms and abbreviations.** This aids consistency and allows other clinicians to scan quickly.

### Part 3 — Assessment (A)

8. **List the active problem list.** Each item is a diagnosis, symptom, or syndrome that will drive the plan. Order by acuity and relevance. For each problem, write a one-sentence summary of the clinical reasoning that connects Objective findings to this diagnosis.

9. **Justify each diagnosis against the Subjective and Objective data.** For example: "Acute myocardial infarction — 65-year-old with 2 hours of substernal chest pressure, diaphoresis, and ECG showing ST elevation in leads II, III, aVF."

10. **Note differential diagnoses for the chief complaint.** If the working diagnosis is "chest pain, likely ACS," list and briefly rule out: "Differential includes pulmonary embolism (no leg swelling, no D-dimer ordered yet), pneumonia (clear lungs), and GERD (pain not relieved by antacid)."

11. **Separate the assessment from the plan.** Do not say "will start antibiotics" here; that belongs in the Plan.

### Part 4 — Plan (P)

12. **For each problem in the Assessment, write the intended action.** Break this into diagnostic (tests to order), therapeutic (medications, procedures, lifestyle counseling), and monitoring (follow-up, when to return, warning signs).

13. **Be specific about dose, frequency, duration, and indication.** Bad: "Start antibiotics." Good: "Start amoxicillin 500 mg PO TID for 10 days for streptococcal pharyngitis."

14. **State the follow-up interval.** "Patient to return in 1 week for recheck of blood pressure" or "Follow lab results; call patient with results within 2 business days."

15. **Document patient education and agreement.** "Discussed risks/benefits of watchful waiting vs. imaging; patient opted to defer imaging pending symptom resolution. Advised to return or call 911 if chest pain worsens, shortness of breath develops, or symptoms persist >3 days."

## Evaluation Criteria

| Check | Pass |
|---|---|
| Subjective contains only patient-reported information; no clinician interpretation | Y/N |
| Objective includes vitals, exam findings, and test results with dates and values | Y/N |
| Each Assessment problem is linked to at least one Objective finding | Y/N |
| Differential diagnosis is documented for the chief complaint | Y/N |
| Plan includes diagnostic, therapeutic, and monitoring actions with specifics (dose, frequency, duration) | Y/N |
| Follow-up interval is stated clearly | Y/N |
| Patient education or shared decision-making is noted | Y/N |
| No diagnostic conclusions appear in the Subjective section | Y/N |
| No raw observations appear *only* in the Assessment; all supporting data are in Objective | Y/N |

## Red Flags

- Subjective section contains clinician interpretations ("suggestive of CHF," "likely pneumonia"). These belong in Assessment.
- Objective section is missing vital signs or contains only "exam unremarkable" with no detail. Another clinician cannot reproduce the assessment from this.
- Assessment lists problems without connecting them to Objective findings. The logic is opaque.
- Differential diagnosis is absent or contains only the working diagnosis, not genuine alternatives.
- Plan lacks specificity: "Follow up," "Monitor," "Consider antibiotics." Vague plans breed medication errors and missed follow-up.
- SOAP is squeezed into a single paragraph. Separation of the four parts is the whole point.
- No mention of patient education, refusal of care, or shared decision-making. This is legally and ethically risky.

## Output Format

```
## SOAP Note Assessment

**Patient:** [Name, MRN, Age, Date of Note]

### Subjective
[Chief complaint and history of present illness in patient's words and timeline. Past medical history, medications, allergies, family history, social history. Note any items not assessed.]

### Objective
**Vital Signs:** [BP, HR, RR, Temp, O2 sat, Weight]
**Exam:** [Findings by system, using standard terminology]
**Labs/Imaging:** [Values with units, reference ranges, dates]

### Assessment
**Active Problems:**
1. [Diagnosis/Problem] — [one-sentence clinical reasoning linking Objective data]
2. [Diagnosis/Problem] — [reasoning]
...

**Differential Diagnosis:**
- [Alternative 1] — [why ruled out or why still considered]
- [Alternative 2] — [why ruled out or why still considered]

### Plan
1. **[Problem 1]**
   - Diagnostic: [Test, indication, timing]
   - Therapeutic: [Medication/procedure with dose/frequency/duration]
   - Monitoring: [What to watch, follow-up interval, return precautions]

2. **[Problem 2]**
   - [same structure]

**Patient Education:** [What was discussed and patient's understanding/agreement]

### Confidence
<high/medium/low> — <justification>
- Confidence is HIGH if: Subjective and Objective are complete, Assessment differential is documented, Plan is specific and actionable
- Confidence is MEDIUM if: One section lacks detail but core logic is sound
- Confidence is LOW if: Subjective/Objective are sparse, Assessment lacks differential, or Plan is vague
```
