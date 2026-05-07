---
name: irac-creac-firac
display_name: IRAC / CREAC / FIRAC
class: lens
underlying_class: native
domain: law
source: IRAC origin uncertain; CREAC (Conclusion-Rule-Explanation-Application-Conclusion) popularized in American legal writing pedagogy; FIRAC (Fact-Issue-Rule-Application-Conclusion) variant used in some jurisdictions
best_for:
  - Structuring legal arguments for memoranda, briefs, and opinion letters
  - Ensuring complete coverage of issue analysis before conclusion
  - Training legal writers to separate rule statement from application
one_liner: "Organize legal argument into Issue-Rule-Application-Conclusion form."
---

# IRAC / CREAC / FIRAC

## Overview

IRAC (Issue-Rule-Application-Conclusion) and its variants CREAC and FIRAC are structural frameworks for legal argument that enforce separation of concerns: what question are we answering, what law governs, how does the law apply to these facts, and what follows. Practitioners use these when writing memos, briefs, or opinions because the discipline of compartmentalization exposes gaps in reasoning — a weak rule section reveals poor research; an application that doesn't track the rule reveals confused thinking. The discipline is enforcing that every claim has its antecedent.

## Analytical Procedure

### Phase 1 — Identify the Legal Question

1. **State the issue in one sentence as a legal question, not a factual statement.**
   - Bad: "John assaulted Mary."
   - Good: "Whether John's act of pushing Mary constitutes battery under the jurisdiction's statute."

2. **Bracket sub-issues.** If the issue has logical dependencies (e.g., "Is the contract valid?" depends first on "Was there an offer?"), list them in order. This is your issue roadmap.

3. **Verify the issue is narrow enough to be resolved in one memo section.** If it spans multiple distinct legal theories or multiple statutes with different elements, split it. One issue per section.

### Phase 2 — State the Governing Rule

4. **Identify the applicable jurisdiction and source of law.** Statute, case law, regulation, common law principle — write the citation. Do not omit this.

5. **State the legal rule in full.** This is not a paraphrase or summary; it is the operative language of the statute or the holding of the controlling case, followed by any elements or factors the court applies.
   - Write out the full text if the rule is short (under 100 words).
   - For longer rules, quote the key operative clause and synthesize elements if they come from multiple sources.

6. **Define any ambiguous terms in the rule.** Courts often define what "reasonable," "knowing," "substantial," or other flexible language means in the context of this rule. Include those definitions in the Rule section.

7. **Note any exceptions, safe harbors, or affirmative defenses.** If the rule has carve-outs, list them explicitly. This prevents applying the rule too broadly later.

### Phase 3 — Apply the Rule to the Facts

8. **State the material facts relevant to each element of the rule.** Do not dump all facts; filter to those that bear on the legal question. Organize by element.
   - Element 1: [relevant facts]
   - Element 2: [relevant facts]
   - Exceptions: [relevant facts, if any]

9. **For each element, walk through the legal test against those facts.** This is not conclusory ("he was negligent"). This is: "The rule requires X; the facts show Y; therefore X is/is not satisfied." If a fact is ambiguous or could cut either way, acknowledge both interpretations.

10. **If controlling case law has applied the rule in a similar factual scenario, cite and distinguish or analogize.** Show your work: "This case is like Jones v. Smith (citation) because both involve [similarity], but unlike Jones because [distinction]."

11. **If the case for one party is stronger, say so and quantify uncertainty.** Do not pretend ambiguity where the facts plainly favor one side. Legal writing that hedges everything is evasive.

### Phase 4 — Reach Conclusion

12. **State the answer to the legal question.** Not "it depends" — yes or no, or the condition under which the answer changes.

13. **If the conclusion was in doubt during application, note what would change the outcome.** This trains the reader (and you) to see the pivotal facts.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Issue is stated as a legal question, not a fact | Y/N |
| Governing rule is cited with full statutory or case language, not paraphrased | Y/N |
| Every element of the rule is addressed in Application | Y/N |
| At least one fact is connected explicitly to at least one element | Y/N |
| Application avoids conclusory language ("he was negligent") in favor of element-by-element tracking | Y/N |
| Controlling or analogous case law is cited if available | Y/N |
| Conclusion is a direct answer to the Issue, not a hedge | Y/N |
| If conclusion is uncertain, pivotal facts are identified | Y/N |

## Red Flags

- Rule section consists of paraphrases instead of statutory or case language. The writer did not look up the actual rule.
- Application section has no reference back to the Rule — it reads like facts analysis without legal reasoning.
- Conclusion is hedged ("it probably," "likely," "arguably") when facts point clearly one way. This is evasion, not analysis.
- No cite to governing authority. Whose rule is this? Without citation, it is opinion, not law.
- Issue is factual, not legal ("What happened?") instead of legal ("Does what happened constitute X under the law?").
- Exceptions or elements in the Rule are not applied. The writer stated the rule but did not fully test the facts against it.
- Application references facts never mentioned in the facts paragraph — analysis is disconnected from the record.

## Output Format

```
## Legal Analysis

**Jurisdiction and Issue:**
[Jurisdiction]. [Full legal question in one sentence.]

**Sub-issues (if any):**
1. [Sub-issue]
2. [Sub-issue]

### Rule
**Governing Authority:** [Citation]

**Full Rule Statement:**
[Complete statutory language or case holding, with elements listed if applicable]

**Key Definitions:**
- [Term]: [court's or statute's definition]

**Exceptions/Safe Harbors:**
- [Exception]: [when applicable]

### Application

**Element 1 — [Name]:**
- Material facts: [list]
- Analysis: [rule + facts + reasoning]
- Case law comparison: [If applicable, cite similar case and explain fit]

**Element 2 — [Name]:**
[same structure]

**[Exceptions or affirmative defenses, if raised]:**
[same structure]

### Conclusion
**Answer to legal question:**
[Direct yes/no/conditional answer]

**Pivotal facts (if conclusion was uncertain):**
[What would flip the outcome]

### Confidence
<high | medium | low> — <justification>
```
---

**Note on variants:**
- **IRAC** (Issue-Rule-Application-Conclusion): Standard four-part structure.
- **CREAC** (Conclusion-Rule-Explanation-Application-Conclusion): States the likely outcome upfront, then proves it. Preferred in briefs where the reader wants the bottom line immediately.
- **FIRAC** (Fact-Issue-Rule-Application-Conclusion): Fronts the fact paragraph for jurisdictions that require it. Logically identical to IRAC; purely organizational.

Use the variant your jurisdiction, instructor, or judge prefers. The analytical discipline is the same.
