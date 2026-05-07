---
name: ach
display_name: Analysis of Competing Hypotheses
class: lens
underlying_class: native
domain: information-analysis
source: Richards J. Heuer Jr., "Psychology of Intelligence Analysis" (1999)
best_for:
  - Evaluating competing theories against evidence systematically
  - Avoiding confirmation bias in complex investigations
  - Identifying which hypotheses are truly ruled out by data
one_liner: "Analysis of Competing Hypotheses — evidence-consistency matrix that removes bias when evaluating rival theories."
---

# Analysis of Competing Hypotheses

## Overview
ACH systematically tests multiple hypotheses against evidence by measuring inconsistency rather than consistency. Most analysts naturally search for evidence that confirms their favored hypothesis; ACH reverses this by asking "Which hypotheses does this evidence *disconfirm*?" and scoring how well each hypothesis survives disconfirming evidence. The discipline is the asymmetry — disconfirmation is stronger than confirmation. Practitioners use ACH when the stakes are high, the hypotheses are mutually exclusive, evidence is mixed, and they suspect their own analytical bias is steering the conclusion.

## Analytical Procedure

### Step 1 — Generate Hypotheses
1. **List all plausible hypotheses.** Include the leading hypothesis, at least two credible alternatives, and one "null" or baseline hypothesis (the simplest assumption, or "nothing special is happening"). Do not pre-rank them.
2. **Write each hypothesis as a single declarative statement.** No hedging, no modality ("might," "could"). Examples:
   - "The system failure was caused by a hardware defect."
   - "The system failure was caused by a software bug introduced in the last deployment."
   - "The system failure was a transient network event with no permanent cause."
3. **If more than 7 hypotheses exist, group related ones or combine weak variants into one.** ACH becomes unwieldy with more than 5–7 live hypotheses.

### Step 2 — Assemble Evidence
4. **List all significant evidence and arguments, not just confirming ones.** Include:
   - Direct observations (logs, measurements, witness statements).
   - Absence of expected evidence (e.g., "no error messages in the log" is evidence).
   - Contextual facts (timing, prior incidents, system state).
   - Arguments or analyses that point in different directions.
5. **Write each piece of evidence as a single fact or claim, free of interpretation.** Bad: "The system is unreliable." Good: "Three crashes in two weeks vs. zero crashes in the prior six months."
6. **Do not filter out "soft" evidence** (circumstantial, subjective, or incomplete). ACH scores it differently, but it stays.

### Step 3 — Build the Inconsistency Matrix
7. **Create a matrix with hypotheses as columns and evidence as rows.** For each cell, ask: "If this hypothesis is true, would I expect to see this evidence?"
8. **Score each cell one of three ways:**
   - **C (Consistent):** The evidence is expected if the hypothesis is true, OR the evidence is consistent with the hypothesis.
   - **I (Inconsistent):** The evidence is *not* expected if the hypothesis is true. The evidence would be surprising or contradictory if this hypothesis held.
   - **N (Neutral):** The evidence has no bearing on the hypothesis — it would be present or absent regardless.
9. **Be conservative with "Inconsistent" scores.** Do not score "I" just because the evidence is not perfectly explained by the hypothesis. Score "I" only when the evidence actively argues *against* the hypothesis.

### Step 4 — Measure Hypothesis Strength
10. **Count, for each hypothesis, the number of "I" (Inconsistent) scores.** This is the key metric: a hypothesis with many inconsistencies is weaker than one with few.
11. **Do not count consistent evidence as supporting.** In ACH, a hypothesis is strong because it has *fewer disconfirmations*, not because it has more confirmations. This flips the usual reasoning.
12. **Calculate a disconfirmation ratio for each hypothesis:**
    - Disconfirmation Ratio = (Number of I scores) / (Total evidence items)
    - Lower ratio = stronger hypothesis.

### Step 5 — Identify Assumptions and Sensitivity
13. **For each "Inconsistent" score, ask: "On what assumption does this inconsistency rest?"** Write the assumption next to the score. Examples:
    - "I scored H2 as inconsistent with 'no error log' because I assume the system logs all errors to this file."
    - "I scored H1 as inconsistent with 'witness saw X at 2pm' because I assume the witness is reliable and the time is accurate."
14. **Highlight assumptions that are not firmly established.** These are sensitivity points — if the assumption is wrong, the disconfirmation disappears.

### Step 6 — Derive Conclusion
15. **Rank hypotheses by disconfirmation ratio (lowest = strongest).** Do not declare the lowest as "true" — declare it as "the hypothesis least disconfirmed by evidence."
16. **Examine the top 2–3 ranked hypotheses.** If the gaps are small (e.g., H1 has 3 inconsistencies and H2 has 4), the evidence does not clearly distinguish them. Say so.
17. **Assess what evidence would be needed to disconfirm the leading hypothesis further.** What would you need to observe, measure, or find to definitively rule it out? This is your follow-up investigative plan.

## Evaluation Criteria

| Check | Pass |
|---|---|
| At least 3 distinct hypotheses generated, including a baseline | Y/N |
| All evidence items written as facts, not interpretations | Y/N |
| Every cell in the matrix is scored C, I, or N (none blank) | Y/N |
| At least one "Inconsistent" score exists (otherwise, no discrimination) | Y/N |
| Every "I" score is paired with an explicit assumption | Y/N |
| Disconfirmation ratios are calculated for all hypotheses | Y/N |
| Top-ranked hypothesis is presented as "least disconfirmed," not "true" | Y/N |
| Follow-up evidence list is concrete (observable, measurable) | Y/N |

## Red Flags

- No "I" (Inconsistent) scores in the matrix. Either all hypotheses fit perfectly (implausible) or the analyst is treating all evidence as confirmation (failure of the method).
- The leading hypothesis has a much lower disconfirmation ratio than alternatives, but the evidence is circumstantial or relies on single assumptions. Sensitivity to those assumptions was not examined.
- Assumptions underlying the "I" scores are vague ("the system should work that way"). Assumptions must be testable or clearly grounded in prior data.
- The analyst switches to a different hypothesis late in the analysis without re-scoring the matrix. The ranking becomes incoherent.
- Follow-up evidence list is empty or generic ("get more data"). The analysis should specify what to look for, not just "investigate further."
- More than half the evidence is marked "N" (Neutral). Either the evidence is irrelevant and should be removed, or the hypotheses are too similar and should be consolidated.

## Output Format

```
## ACH Assessment

**Hypotheses:**
1. H1: <hypothesis>
2. H2: <hypothesis>
3. H3: <hypothesis>
...

### Evidence & Inconsistency Matrix

| Evidence | H1 | H2 | H3 | ... |
|---|---|---|---|---|
| <fact 1> | C/I/N | C/I/N | C/I/N | |
| <fact 2> | C/I/N | C/I/N | C/I/N | |
| ... | | | | |

### Assumptions for Inconsistent Scores
- H1 + Evidence 3 (I): Assumption — <...>
- H2 + Evidence 5 (I): Assumption — <...>
- ...

### Disconfirmation Scores
| Hypothesis | Inconsistent Count | Total Evidence | Ratio |
|---|---|---|---|
| H1 | _ | _ | _% |
| H2 | _ | _ | _% |
| H3 | _ | _ | _% |

### Ranking (by disconfirmation ratio, lowest first)
1. <hypothesis> — _% disconfirmed
2. <hypothesis> — _% disconfirmed
3. ...

### Discrimination Assessment
<If top hypotheses are close in score, explain why the evidence does not clearly distinguish them.>

### Critical Assumptions & Sensitivities
- Assumption: <...> — If false, H1's inconsistency with Evidence X disappears.
- ...

### Follow-up Evidence Needed
To further disconfirm the leading hypothesis, seek:
1. <Specific observable or measurable fact>
2. <Specific observable or measurable fact>
...

### Confidence
<high | medium | low> — <justification. High: leading hypothesis is much more consistent with evidence and key assumptions are solid. Medium: leading hypothesis is only slightly ahead, or key assumptions are unverified. Low: multiple hypotheses have similar disconfirmation ratios, or evidence is sparse.>
```
