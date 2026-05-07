---
name: chevron-two-step
display_name: Chevron Two-Step
class: lens
underlying_class: native
domain: law
source: Chevron U.S.A., Inc. v. Natural Resources Defense Council, Inc., 467 U.S. 837 (1984)
best_for:
  - Evaluating statutory ambiguity and agency interpretation deference
  - Judicial review of regulatory action
  - Predicting likelihood of agency action surviving challenge
one_liner: "Two-step reasonableness review of agency interpretations of ambiguous statutes."
---

# Chevron Two-Step

## Overview
When a statute is ambiguous and an agency has adopted an interpretation, courts apply a two-step test to determine if that interpretation deserves deference. Step One asks whether Congress has directly spoken to the precise question at issue. Step Two asks whether the agency's interpretation is reasonable, even if not the only permissible one. Practitioners use this lens to evaluate whether a regulatory interpretation will survive judicial challenge and to structure arguments in administrative law disputes. The discipline is distinguishing genuine statutory silence from silence that has been filled by statutory structure or legislative history.

## Analytical Procedure

### Step One — Determine if Congress Spoke Directly to the Question

1. **State the precise question at issue.** This is not "What does this statute do?" but rather "What does this statute require or permit in this specific circumstance?" Write it as a conditional: "Does the statute permit/require [X] when [Y condition]?"

2. **Consult the statutory text.** Read the relevant provision(s) in their full context, including section headings, provisos, and definitions. Look for language that directly answers the question. Do not infer from silence yet.
   - If the text directly answers the question (either yes or no), note the precise clause(s).
   - If the text uses clear language but is susceptible to more than one reading, note both readings and flag this as potential ambiguity.
   - If the text uses conditional language, cross-references, or delegation clauses ("the agency may," "as the Secretary determines"), note these as signals of permissible agency discretion.

3. **Consult legislative history (if available and relevant).** Review committee reports, floor statements, and legislative debates specifically addressing the question. Legislative history can narrow an apparent ambiguity or confirm that Congress intended to leave the question to agency discretion.
   - If the legislative history is clear and directly addresses the question, note the intent.
   - If the legislative history is sparse, silent, or contradictory, flag this as non-dispositive.
   - Do not treat legislative history as superior to text; use it only to clarify ambiguity in the text.

4. **Assess prior agency interpretation and acquiescence.** If Congress has enacted amendments or reauthorizations since the agency adopted its interpretation, and those amendments did not reject the interpretation, this can suggest Congress acquiesced to it (narrowing the range of permissible interpretations).
   - Note any legislative events (amendments, hearings, failed bills) that bear on the question.
   - Acquiescence is weak evidence but can shift the ambiguity analysis.

5. **Render a Step One verdict:**
   - **Congress spoke directly (ambiguity resolved):** The statute, read in context with legislative history and structural signals, yields a clear answer. The question is not one of agency discretion.
   - **Congress was silent or ambiguous:** The statute does not directly answer the question. Agency discretion is permissible. Proceed to Step Two.

### Step Two — Determine if the Agency's Interpretation is Reasonable

(Only apply if Step One yields ambiguity.)

6. **Extract the agency's interpretation.** Identify the specific rule, guidance, or enforcement position the agency has adopted. Write it plainly: "The agency interprets the statute to mean [X]."

7. **Check the agency's procedure.** Did the agency follow required notice-and-comment rulemaking, formal adjudication, or other statutory procedure?
   - If the procedure was adequate, the interpretation is entitled to Chevron deference (full Step Two review).
   - If the procedure was inadequate or the agency acted without authority, the interpretation may fail on procedural grounds without reaching Step Two substance.
   - If the agency relied on informal guidance, a court may give less deference (Skidmore respect rather than Chevron deference), but the reasonableness test still applies.

8. **Assess whether the interpretation is rational and internally consistent.**
   - Does the agency's interpretation rest on a logical chain of reasoning?
   - Does the agency address the statutory text, structure, and purpose?
   - Does the agency acknowledge and respond to counter-arguments or alternative readings?
   - Has the agency flip-flopped without explanation, or does any change in interpretation rest on a reasoned basis?

9. **Check for statutory constraints.** Even if an interpretation is reasonable, it must not violate other parts of the statute, administrative law principles, or constitutional limits.
   - Does the interpretation conflict with definitions, standards, or prohibitions elsewhere in the statute?
   - Does it impose unreasonable burdens (major questions doctrine, where ambiguous statutes will not be read to authorize major regulatory action without clear direction)?
   - Does it implicate constitutional concerns (speech, due process, equal protection)?

10. **Render a Step Two verdict:**
    - **Interpretation is reasonable:** The agency's reading is plausible, grounded in the text and statutory purpose, internally coherent, and not in conflict with other law.
    - **Interpretation is unreasonable:** The agency's reading is implausible, contradicted by text or structure, incoherent, or inconsistent with statutory limits. The agency has exceeded its delegated authority or acted arbitrarily.

## Evaluation Criteria

| Check | Pass |
|---|---|
| The precise question (as a conditional) is stated clearly | Y/N |
| All relevant statutory text was consulted, not just one clause | Y/N |
| Legislative history was reviewed (even if found unhelpful) | Y/N |
| Step One verdict is explicit and justified | Y/N |
| Agency interpretation is stated plainly without hedging | Y/N |
| Procedural posture (notice-and-comment, etc.) was verified | Y/N |
| Reasonableness check includes text, structure, and consistency | Y/N |
| At least one counter-argument or alternative reading was acknowledged | Y/N |
| Step Two verdict follows logically from the analysis | Y/N |

## Red Flags

- Step One verdict is hedged or vague ("the statute seems to be ambiguous"). Ambiguity is binary — either Congress spoke directly or it didn't. If you cannot commit, the ambiguity was not adequately analyzed.
- The precise question was never stated. If you cannot write the question as a conditional ("Does the statute permit X when Y?"), the analysis has not been grounded.
- Legislative history was ignored entirely. Even if unhelpful, its absence should be noted.
- Step Two analysis treats the agency's interpretation as the only plausible reading. Reasonableness review must consider whether alternatives are also permissible — the bar is not uniqueness.
- The analysis conflates Step One and Step Two. A clear statutory directive ends the inquiry at Step One; if Step One fails, do not second-guess the agency's choice among permissible readings.
- No mention of procedure (notice-and-comment, adjudication, informal guidance). Deference level turns partly on whether the agency followed its statutory procedures.
- Constitutional or major questions doctrine concerns are wholly absent. Even if a reading is "reasonable," it may fail because the statute does not clearly authorize it.
- The verdict is stated as confidence in an outcome ("the court will uphold this") rather than as a Chevron analysis. The lens assesses deference and reasonableness, not prediction.

## Output Format

```
## Chevron Two-Step Analysis

**Statute(s):**
<citation(s)>

**Precise Question:**
Does the statute [permit/require] [X] when [Y condition]?

### Step One — Did Congress Speak Directly?

#### Statutory Text
<Relevant provision(s) in context. Note any ambiguity.>

#### Legislative History
<Summary. If sparse or contradictory, note.>

#### Prior Agency Interpretation and Congressional Acquiescence
<Any relevant amendments, reauthorizations, or legislative events.>

**Step One Verdict:** 
[Congress spoke directly / Congress was ambiguous / Congress was silent]
<Justification in 2–3 sentences.>

---

### Step Two — Is the Agency's Interpretation Reasonable?

(Only if Step One found ambiguity.)

#### Agency's Interpretation
<Statement of the rule or position.>

#### Procedural Posture
<Notice-and-comment, adjudication, guidance, etc. Is Chevron deference applicable?>

#### Rationality and Consistency
<Does the agency's reasoning follow logically? Does it address text, structure, and counter-arguments?>

#### Statutory Constraints
<Does the interpretation conflict with other statutory provisions, the major questions doctrine, or constitutional limits?>

**Step Two Verdict:** 
[Interpretation is reasonable / Interpretation is unreasonable]
<Justification in 2–3 sentences.>

---

### Confidence
<high | medium | low> — <justification>
```
