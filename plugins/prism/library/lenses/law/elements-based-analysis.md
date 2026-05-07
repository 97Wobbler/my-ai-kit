---
name: elements-based-analysis
display_name: Elements-Based Analysis
class: lens
underlying_class: native
domain: law
source: Common law pleading doctrine; formalized in modern civil procedure (Federal Rules of Civil Procedure, Restatement of Torts)
best_for:
  - Proving or defending a cause of action by isolating and evaluating each required element
  - Identifying gaps in proof before trial
  - Structuring settlement discussions or summary judgment motions
one_liner: "Verify each element of a cause of action independently to judge whether the burden of proof is met."
---

# Elements-Based Analysis

## Overview
A cause of action is not proved or disproved as a whole; it succeeds only when *every* required element is proved. Elements-Based Analysis isolates the discrete legal requirements for a given claim, examines the evidence for each in turn, and flags gaps before they become fatal at trial. Practitioners use this to stress-test pleadings, evaluate discovery adequacy, plan witness examination, and diagnose settlement leverage. The discipline is granularity — vague notions like "the defendant was negligent" collapse into concrete elements (duty, breach, causation, damages), each with its own evidentiary burden.

## Analytical Procedure

### Step 1 — Identify the Cause of Action

1. **Name the specific cause of action.** (e.g., "negligence," "breach of contract," "defamation," "tortious interference"). Do not generalize as "wrongdoing" or "unfair business practices."

2. **Consult the controlling jurisdiction's law.** The required elements vary by jurisdiction and by the specific claim. Use the Restatement of Torts, state statute, or case digest to find the canonical element list.

3. **Write the elements as a numbered list.** Each element should be a single condition or requirement. Bad: "the defendant acted negligently and caused harm." Good: "(1) the defendant owed a duty of care to the plaintiff; (2) the defendant breached that duty; (3) the breach proximately caused injury; (4) the plaintiff suffered damages."

### Step 2 — Collect Evidence Against Each Element

4. **For each element, list all evidence offered to prove it.** Include documents, witness testimony, expert reports, admissions, and circumstantial evidence. Do not evaluate strength yet — capture the whole evidentiary record.

5. **Assign each piece of evidence to ONE element.** If a piece of evidence is probative of multiple elements, note that in parentheses but list it under the element it most directly proves. Avoid double-counting.

6. **Mark each piece as direct or circumstantial.**
   - **Direct:** testimony that the defendant was speeding (proves breach of duty to obey speed limits).
   - **Circumstantial:** skid marks 200 feet long (circumstantial evidence of speed).

### Step 3 — Evaluate Sufficiency for Each Element

7. **For each element, ask: "Is there a triable issue of fact?"** This means: could a reasonable jury find the element proved beyond a preponderance (or beyond a reasonable doubt if criminal)? This is a low bar at the pleading stage but a higher bar at summary judgment.

8. **Score each element as follows:**
   - **Strong (S):** Multiple direct or well-corroborated circumstantial evidence pieces; witness credibility not the crux.
   - **Adequate (A):** Sufficient evidence, but pivots on a single witness or inference; jury could find it either way.
   - **Weak (W):** Single piece of evidence, uncorroborated, or evidence is circumstantial and the inference is not compelling.
   - **Missing (M):** No evidence for this element; element cannot be proved at trial as matters stand.

9. **For each Weak or Missing element, note what evidence would be needed to remedy it.** Be specific: "testimony from a structural engineer on the building code" not "expert testimony."

### Step 4 — Identify Vulnerability and Strategy

10. **List all Weak and Missing elements.** These are the plaintiff's burden; they are the defendant's defense. For a plaintiff, these are litigation risks. For a defendant, these are points to press.

11. **Cross-check element dependencies.** Some elements logically lean on others (e.g., causation depends on breach being proved). If a foundational element is Weak or Missing, mark dependent elements as at-risk even if their direct evidence is Adequate.

12. **For settlement or negotiation, rank elements by:**
    - **Contestability:** How likely is a jury to find it or not find it? Low contestability = leverage.
    - **Cost to prove:** How expensive is it to develop the missing or weak evidence (discovery, experts, trial prep)?

## Evaluation Criteria

| Check | Pass |
|---|---|
| Cause of action is named with precision (not generalized) | Y/N |
| Element list comes from controlling law (citable source) | Y/N |
| Each element is a discrete, testable condition | Y/N |
| All evidence in the record is assigned to at least one element | Y/N |
| Each evidence piece is tagged direct or circumstantial | Y/N |
| Every element has a score (S/A/W/M) with rationale | Y/N |
| Weak and Missing elements have remedies identified | Y/N |
| Element dependencies are noted where they exist | Y/N |

## Red Flags

- Element list comes from the complaint or party's brief instead of case law. Custom element lists are usually incomplete or wrong.
- Every element scores as Strong. Either the case is trivial (unlikely for anything in litigation) or the analysis was lenient. Stress-test the weakest evidence.
- Evidence is assigned to multiple elements without priority. This masks which elements are really vulnerable.
- An element is marked Strong based only on party admissions or interrogatory answers. Admissions are powerful but do not relieve the burden to present evidence at trial.
- Missing elements are acknowledged but not addressed. Silence on remedies means the analysis is incomplete.
- Circumstantial evidence is scored as Strong without discussing the competing inferences available to a skeptical jury.

## Output Format

```
## Elements-Based Analysis

**Cause of action:** <name and jurisdiction>

**Source of elements:** <statute/restatement section/leading case>

### Element List and Evidence
| Element # | Element | Evidence (Direct/Circumstantial) | Type | Score |
|---|---|---|---|---|
| 1 | <element text> | <evidence piece>; <evidence piece> | D/C | S/A/W/M |
| 2 | <...> | <...> | <...> | <...> |

### Element-by-Element Assessment
**Element 1: <text>**
- Score: S/A/W/M
- Evidence: <summary of probative pieces>
- Rationale: <why this score?>
- If Weak or Missing: Remedy needed: <specific evidence or testimony>
- Dependencies: <any other elements this rests on?>

**Element 2: <...>**
...

### Vulnerability Summary
**Strong elements (S):** <list element numbers>
**Adequate elements (A):** <list element numbers>
**Weak elements (W):** <list element numbers>
**Missing elements (M):** <list element numbers>

### Strategic Implications
**For plaintiff/claimant:**
<Which elements create trial risk? What discovery or witnesses are critical?>

**For defendant:**
<Which elements are most defensible? Where should cross-examination focus?>

### Remedies for Weak/Missing Elements
| Element | Current gap | Remedy (evidence needed) | Cost/feasibility | Timeline |
|---|---|---|---|---|
| <...> | <...> | <...> | <...> | <...> |

### Confidence
<high | medium | low> — <justification based on source law authority, completeness of record reviewed, and clarity of element application>
```
