---
name: tort-analysis
display_name: Tort Analysis
class: lens
underlying_class: native
domain: law
source: Common law tradition; systematized in Restatement (Second) of Torts (American Law Institute, 1965)
best_for:
  - Evaluating whether a defendant bears legal liability for harm
  - Breaking down negligence claims into their constituent elements
  - Identifying gaps in a plaintiff's case before trial
one_liner: "Four-element tort liability test — duty, breach, causation, damages."
---

# Tort Analysis

## Overview
Tort liability rests on four irreducible elements: the defendant owed a legal duty to the plaintiff, the defendant breached that duty, the breach caused injury to the plaintiff, and the injury resulted in measurable damages. This lens applies the doctrine to a fact pattern or legal claim by interrogating each element separately. Practitioners use it to evaluate the strength of a negligence claim, to identify which elements are weakest, and to determine where discovery should focus.

## Analytical Procedure

### Phase 1 — Establish the Legal Duty

1. **Identify the relationship between defendant and plaintiff.** Was there a professional relationship (doctor-patient, attorney-client), a contractual relationship, a landlord-tenant relationship, or mere strangers? Write it plainly.

2. **Determine the scope of duty from that relationship.** Ask:
   - What standard of care applies? (reasonable person, professional standard, higher standard due to special relationship, etc.)
   - What foreseeable harms was the defendant under a duty to prevent?
   - Did the defendant voluntarily assume a duty by acting?
   - Did the defendant's prior conduct create a duty to rescue or warn?

3. **Check for duty-negating doctrines:**
   - Assumption of risk (plaintiff knowingly accepted the risk)
   - No duty to rescue strangers (except in special relationships)
   - No liability for non-action absent a duty-creating relationship
   - Statutory or common law immunities (sovereign immunity, charitable immunity)

   Mark each as applies/does not apply/unclear.

### Phase 2 — Examine the Breach

4. **Define the applicable standard of care.** Write it as a concrete behavioral rule, not a principle:
   - Bad: "the defendant should have been reasonable"
   - Good: "a homeowner must inspect the roof every two years and repair known leaks within 30 days"

5. **Determine what the defendant actually did (or failed to do).** Gather facts about the defendant's conduct:
   - What precautions did the defendant take?
   - What did the defendant know or should have known at the time?
   - What industry practice or regulatory requirement applies?

6. **Compare conduct to standard.** Did the defendant's conduct fall below the standard? 
   - If yes, mark as breached.
   - If no, mark as compliant.
   - If unclear (facts disputed or standard ambiguous), mark as disputed and note what additional facts would resolve it.

7. **Consider the Hand Formula (cost-benefit test) if useful:**
   - Probability of harm × Magnitude of harm vs. Cost of precaution
   - If the cost of preventing the harm is less than the expected loss, breach is likely.

### Phase 3 — Trace Causation

8. **Establish actual (but-for) causation.** Ask: But for the defendant's breach, would the harm have occurred?
   - If yes → defendant's conduct was a cause-in-fact.
   - If no → no liability (causation fails).
   - If unclear → note what counterfactual evidence would decide it.

9. **Establish proximate (legal) causation.** Ask: Is the harm a foreseeable result of the breach, or is it too remote?
   - Was the type of harm foreseeable?
   - Was the plaintiff a foreseeable victim?
   - Did an intervening act (act of third party or act of God) break the causal chain?
   - Does public policy limit liability despite foreseeability?

   Mark each as supports/undermines/neutral on proximate causation.

10. **Identify intervening causes.** If a third party's act or an unforeseeable event occurred between the breach and the harm:
    - Was it foreseeable? (If yes, does not break the chain.)
    - Was it independent of the defendant's conduct? (If no, does not break the chain.)
    - Was it extraordinary? (If yes, more likely to break the chain.)

### Phase 4 — Quantify Damages

11. **Identify the type of harm:** personal injury, property damage, economic loss, emotional distress, loss of consortium, or punitive damages.

12. **Calculate special (economic) damages.** These are quantifiable losses:
    - Medical expenses (past and future, reasonably certain)
    - Lost wages (past and future, if employment causally linked to injury)
    - Property repair or replacement cost
    - Note: speculative future damages are not recoverable; must be reasonably certain.

13. **Assess general (non-economic) damages.** These are harder to quantify:
    - Pain and suffering
    - Emotional distress
    - Loss of enjoyment of life
    - Disfigurement or scarring
    - Loss of consortium (spouse, parent, child)

    For each, note whether the jurisdiction allows recovery and whether the claim is supported by evidence (medical records, testimony, comparables).

14. **Determine if punitive damages are available.** Punitive damages (designed to punish, not compensate) are available only if:
    - The defendant acted with intent to harm, or
    - The defendant acted with recklessness or gross negligence
    - AND the jurisdiction allows them in this type of case.

    Mark as available/unavailable/unclear. If available, note the defendant's financial condition (used to set the award).

## Evaluation Criteria

| Check | Pass |
|---|---|
| Duty: relationship between parties is clearly identified | Y/N |
| Duty: applicable standard of care is stated in concrete behavioral terms | Y/N |
| Breach: defendant's actual conduct is factually described | Y/N |
| Breach: conduct is compared against the standard and marked as breached/compliant/disputed | Y/N |
| Causation: but-for causation is tested with a clear counterfactual | Y/N |
| Causation: proximate causation is assessed across foreseeability and intervening cause | Y/N |
| Damages: special damages are itemized with supporting evidence | Y/N |
| Damages: general damages are identified and jurisdictional availability is noted | Y/N |
| Each element is marked as satisfied/not satisfied/disputed | Y/N |

## Red Flags

- Duty is stated in abstract language ("the defendant owed a duty of care") without identifying the specific relationship or standard. Without concreteness, breach cannot be evaluated.
- The standard of care is never defined. The analysis jumps from "was there a duty?" to "did the defendant breach it?" without ever specifying what conduct the duty requires.
- Breach is assessed without reference to the facts. Statements like "the defendant clearly breached" without describing what the defendant did or failed to do are conclusory.
- Causation analysis stops at "but-for" without addressing proximate causation. Many harms are caused-in-fact by the defendant but too remote to impose liability.
- Intervening causes are ignored. If a third party's act or an unexpected event occurred between the breach and harm, that must be interrogated — it may break the causal chain.
- Damages are stated as a lump sum with no itemization. "The plaintiff suffered $500,000 in damages" without breaking it into medical, lost wages, pain and suffering, etc., is incomplete.
- Speculative future damages are included as if certain. "The plaintiff will suffer lifelong pain worth $2 million" without medical foundation is not recoverable.
- All four elements are marked as "satisfied" without qualification. Tort claims almost always have disputed elements. If none are marked as disputed, the analysis was likely not adversarial.

## Output Format

```
## Tort Analysis

**Case/Claim Summary:**
<one sentence identifying parties and alleged harm>

### Element 1: Duty

**Relationship:** <type of relationship or status>

**Applicable Standard:** <concrete behavioral rule, not abstract principle>

**Duty-Negating Doctrines:** 
| Doctrine | Applies | Notes |
|---|---|---|
| Assumption of risk | Y/N | ... |
| No duty to rescue | Y/N | ... |
| Immunity | Y/N | ... |

**Verdict:** Duty exists / No duty / Unclear

---

### Element 2: Breach

**Defendant's Actual Conduct:** <factual description of what defendant did/failed to do>

**Comparison to Standard:**
| Standard Requires | Defendant's Conduct | Result |
|---|---|---|
| <requirement> | <actual conduct> | Compliant / Breached / Disputed |

**Hand Formula (if applicable):** 
P × H vs. C: <analysis>

**Verdict:** Breached / Compliant / Disputed

---

### Element 3: Causation

**But-For (Actual) Causation:**
Counterfactual: If the defendant had not [breach], would [harm] have occurred?
Answer: <yes/no/unclear> — <justification>

**Proximate (Legal) Causation:**
| Factor | Assessment | Supporting/Undermining |
|---|---|---|
| Type of harm foreseeable? | Y/N | ... |
| Plaintiff a foreseeable victim? | Y/N | ... |
| Intervening cause present? | Y/N/N/A | ... |
| Public policy limit? | Y/N | ... |

**Intervening Cause Analysis (if applicable):**
<description of third party act or force of nature>
Foreseeable? <Y/N> | Independent? <Y/N> | Extraordinary? <Y/N>
Breaks chain? <Yes / No / Unclear>

**Verdict:** Causation established / Causation fails / Disputed

---

### Element 4: Damages

**Type of Harm:** <category>

**Special (Economic) Damages:**
| Item | Amount | Evidence | Reasonably Certain? |
|---|---|---|---|
| Medical expenses | $X | <medical records, invoices> | Y/N |
| Lost wages | $X | <pay stubs, employment records> | Y/N |
| Property damage | $X | <repair estimate, appraisal> | Y/N |
| **Subtotal** | $X | | |

**General (Non-Economic) Damages:**
| Item | Jurisdiction Allows? | Supported by Evidence? | Estimate |
|---|---|---|---|
| Pain and suffering | Y/N | Y/N | $X or not quantified |
| Emotional distress | Y/N | Y/N | ... |
| Loss of consortium | Y/N | Y/N | ... |

**Punitive Damages:**
Available? <Y/N/Unclear> — <justification>
If yes: Defendant's financial condition: <relevant facts>

**Total Recoverable Damages:** $X (special) + $X (general) = $X

**Verdict:** Damages established / No recoverable damages / Partially disputed

---

### Synthesis

**Elements Satisfied:** <Duty, Breach, Causation, Damages — which are firm, which disputed>

**Weakest Element:** <which element is most vulnerable to challenge>

**Liability Verdict:** <Defendant is liable / Defendant is not liable / Liability depends on disputed facts>

### Confidence
<high | medium | low> — <justification based on completeness of fact development, clarity of law, and number of disputed elements>
```
---
