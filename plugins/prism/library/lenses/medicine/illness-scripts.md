---
name: illness-scripts
display_name: Illness Scripts
class: lens
underlying_class: native
domain: medicine
source: Elstein, Shulman, and Sprafka (1978); cognitive psychology of medical diagnosis; refined in medical education (Bordage, Norman)
best_for:
  - Organizing differential diagnoses around temporal and pathophysiological patterns
  - Teaching clinical reasoning by mapping symptoms to disease trajectories
  - Stress-testing a diagnosis by checking symptom-timeline fit
one_liner: "Reconstruct symptom trajectories across time, risk, and pathology to validate diagnostic confidence."
---

# Illness Scripts

## Overview
An illness script is a mental template physicians develop for a disease: the typical *time course* of symptom onset, the *characteristic symptoms* that appear in what sequence, the *risk factors* that make it likely, and the *underlying pathophysiology* that ties them together. Rather than matching isolated symptoms to a checklist, practitioners use scripts to ask whether the patient's actual story fits the disease's natural story. You reach for this lens when a diagnosis fits the symptoms but the timeline doesn't, or when symptoms are present but the usual triggers are absent.

## Analytical Procedure

### Phase 1 — Extract the Patient's Story

1. **Write the chief complaint.** One sentence. Example: "62-year-old with chest pain and shortness of breath."

2. **Build the timeline of onset.** For each symptom reported, record:
   - **When it started** (acute, insidious, specific date/time)
   - **How it started** (sudden, gradual, in relation to event)
   - **Progression** (stable, worsening, improving, episodic)
   - **Associated events** (physical exertion, eating, trauma, stress, new medication, travel)

   Example timeline:
   ```
   Day 1, 2pm: Sudden substernal chest pressure during lawn mowing
   Day 1, 2:30pm: Diaphoresis and shortness of breath onset
   Day 1, 4pm: Pain radiates to left arm
   Day 2: Nausea; pain unchanged
   ```

3. **List active risk factors.** For the patient, record:
   - Age, sex, family history of early cardiac/cerebral disease
   - Smoking, hypertension, diabetes, hyperlipidemia, obesity
   - Recent surgery, immobility, infection, inflammation
   - Medications (estrogen, stimulants, NSAIDs)
   - Psychosocial stressors, sleep deprivation

### Phase 2 — Retrieve and Articulate the Illness Script

4. **For each working diagnosis on your differential, write out its canonical script.** Do not rely on memory; consult a reference (textbook, UpToDate, or internal knowledge base). Record:

   **Pathophysiology summary:** 1-2 sentences on the mechanism. Example: "Acute myocardial infarction: atherosclerotic plaque rupture → thrombosis → myocardial necrosis."

   **Prodrome (if any):** Weeks/months before acute phase. Example: "Angina with exertion, relieved by rest (unstable pattern increasing over days)."

   **Onset pattern:** How acute is acute? Minutes? Hours? Example: "Sudden onset of maximal pain, typically while active."

   **Symptom sequence:** The order and approximate timing. Example:
   - Minutes 0–5: Substernal or left-sided chest pressure, heaviness, squeezing
   - Minutes 5–30: Diaphoresis, nausea, dyspnea if large territory
   - Minutes 30+: Radiation to arm/jaw/back; anxiety; sense of doom

   **Duration:** Minutes, hours, days, weeks? Example: "Hours to days if untreated; persistent if ongoing ischemia."

   **Associated findings:** What else typically co-occurs? Example: "Tachycardia, hypertension (if pain is severe) or hypotension (if cardiogenic shock). No fever."

   **Modifying factors:** What makes it better or worse? Example: "Unrelieved by rest or antacids; may worsen with continued exertion. Improved by nitrates."

   **Risk factor clustering:** Which risk factors typically cluster? Example: "Smoking + hypertension + male + age >45; family history of premature CAD."

### Phase 3 — Compare Patient Story to Script

5. **For each working diagnosis, score the fit.** Use this rubric:

   | Dimension | Poor fit (0 pts) | Partial fit (1 pt) | Good fit (2 pts) |
   |---|---|---|---|
   | **Onset timing** | Timeline contradicts script | Timeline is atypical but not impossible | Timeline matches script |
   | **Symptom sequence** | Symptoms in wrong order or absent | Symptoms present but out of sequence | Symptoms in expected order and timing |
   | **Associated findings** | Major findings contradict script (e.g., fever in MI) | Minor findings absent or unexpected | Associated findings present as predicted |
   | **Risk factor match** | No relevant risk factors present | Some risk factors present; pattern unclear | Risk factors cluster as predicted |
   | **Modifying factors** | Patient response contradicts script (e.g., pain relieved by antacid in MI) | Response atypical but not ruled out | Response matches script (e.g., unrelieved by rest) |

   **Fit score:** Sum the points (0–10). Score ≥7 suggests the diagnosis "fits the script"; score ≤4 suggests the script is a poor match and should be deprioritized.

6. **Identify mismatches explicitly.** For each diagnosis that scored ≤4, write:
   - Which dimensions scored 0 and why?
   - Is the mismatch explainable (atypical presentation, comorbidity, medication effect) or is the diagnosis unlikely?

### Phase 4 — Refine the Differential

7. **Reorder your differential by script fit.** High-fit diagnoses move to the top. Low-fit diagnoses do not disappear — they move down but remain on the list until the patient's course clarifies or testing rules them out.

8. **For the top diagnosis, articulate the "story you're predicting."** If this diagnosis is correct, what should happen next?
   - "Over the next 2–4 hours, troponin should rise, EKG should show STEMI pattern."
   - "Over the next 24–48 hours, fever should develop and WBC should rise."

   This predicted story becomes your test of the hypothesis.

9. **Design the next test or observation to confirm or refute the top diagnosis.** The test should check a high-impact feature of the script (a symptom that *should* be there but isn't, or shouldn't be there but is).

## Evaluation Criteria

| Check | Pass |
|---|---|
| Patient timeline includes onset time, progression, and triggers for each symptom | Y/N |
| All risk factors (demographic, behavioral, medical) are listed | Y/N |
| At least 3 diagnoses have full scripts retrieved and articulated | Y/N |
| Each diagnosis has a Fit score calculated with all 5 dimensions assessed | Y/N |
| Mismatches between patient story and low-fit scripts are explicitly identified | Y/N |
| Top diagnosis has a predicted story (what should happen next) | Y/N |
| A test or observation is specified to confirm or refute the top diagnosis | Y/N |

## Red Flags

- Script is vague or generic ("chest pain can be anything"). Vague scripts are useless — use a reference, not intuition.
- Patient timeline is sparse (no times, no sequence, only chief complaint). Without timeline, script-matching collapses.
- All diagnoses score 7–10 (all fit). Either the differential is too broad or the scoring is lenient. Tighten by checking modifying factors and risk factor clustering.
- No diagnosis scores <4 (all fit equally). The differential hasn't been narrowed — time to gather more history or data.
- Predicted story is generic ("we'll see what the labs show"). Predict specific values, timings, or findings. Vague predictions can't be tested.
- A diagnosis is discarded without checking the script for atypical presentation. Rare or atypical variants stay on the list unless the script explicitly rules them out.

## Output Format

```
## Illness Script Assessment

**Chief complaint:**
<one sentence>

### Patient Timeline
| Symptom | Onset | Progression | Associated Event |
|---|---|---|---|
| <...> | <...> | <...> | <...> |

### Active Risk Factors
- <demographic/behavioral/medical>
- ...

### Script Fit Analysis

#### Diagnosis 1: <name>
**Pathophysiology:** <1–2 sentences>

**Script summary:**
- Onset: <timing and pattern>
- Symptom sequence: <expected order and timing>
- Associated findings: <expected exam/lab findings>
- Duration: <typical course>
- Modifying factors: <what makes better/worse>
- Risk factor clustering: <typical risk profile>

**Fit score:** <0–10>
| Dimension | Score | Reasoning |
|---|---|---|
| Onset timing | 0/1/2 | <...> |
| Symptom sequence | 0/1/2 | <...> |
| Associated findings | 0/1/2 | <...> |
| Risk factor match | 0/1/2 | <...> |
| Modifying factors | 0/1/2 | <...> |

**Mismatches:** <if score ≤4, what doesn't fit>

#### Diagnosis 2: <name>
[Same structure as Diagnosis 1]

#### Diagnosis 3: <name>
[Same structure as Diagnosis 1]

### Refined Differential (by script fit)
1. <Diagnosis 1 — Fit score, brief rationale>
2. <Diagnosis 2 — Fit score, brief rationale>
3. <Diagnosis 3 — Fit score, brief rationale>

### Predicted Story for Top Diagnosis
If <top diagnosis> is correct, the following should occur:
- <Expected finding 1> within <timeframe>
- <Expected finding 2> within <timeframe>
- <Expected progression or resolution>

### Test to Confirm or Refute Top Diagnosis
<Test name and what a positive/negative result means for the diagnosis>

### Confidence
<high/medium/low> — <justification based on script fit, timeline coherence, and risk factor clustering>
```
