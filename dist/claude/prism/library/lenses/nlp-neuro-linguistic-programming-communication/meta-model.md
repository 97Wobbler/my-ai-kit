---
name: meta-model
display_name: Meta Model
class: lens
underlying_class: native
domain: nlp-neuro-linguistic-programming-communication
source: Bandler & Grinder (NLP, 1970s); formalized in therapeutic and communication contexts
best_for:
  - Recovering missing information in vague statements
  - Uncovering hidden assumptions in claims or proposals
  - Deepening shallow explanations to actionable specifics
one_liner: "Recover hidden information and assumptions through generalization, deletion, and distortion questions."
---

# Meta Model

## Overview
The Meta Model is a set of linguistic patterns that identify where speakers have compressed, omitted, or distorted information. By asking targeted questions that reverse these compressions, you recover the specifics underneath vague language — what was deleted, what was generalized, and what was distorted. Practitioners use this to move from abstract claims ("That won't work") to concrete, actionable details ("What specifically won't work about it, and under what conditions?"). The discipline is systematic questioning, not assumption-filling.

## Analytical Procedure

### Phase 1 — Identify the Distortions

1. **Record the original statement verbatim.** Write it exactly as spoken or written, including hedges, nominalizations, and vague pronouns.

2. **Mark instances of these three distortion types:**

   **Generalization** — A statement that applies a rule without exception:
   - Markers: "always," "never," "everyone," "no one," "all X," "nobody understands"
   - Example: "Engineers never listen to feedback."
   - Recovery question: "Never? Has there been an engineer who listened?"

   **Deletion** — Information has been left out. The statement is incomplete:
   - Missing subject: "It won't work" (what is "it"?)
   - Missing object: "I'm worried" (worried about what?)
   - Missing comparison: "This is better" (better than what?)
   - Missing comparison basis: "That's expensive" (compared to what standard?)
   - Nominalization (verb turned into noun, losing detail): "The implementation was a failure" (who did what, and how did it fail?)
   - Missing process: "People just don't care" (don't care about what, and why not?)
   - Example: "The proposal failed." (Who proposed what, why did it fail, what counted as failure?)
   - Recovery question: "What specifically failed, and how did you measure failure?"

   **Distortion** — Relationships between ideas are stated unclearly or causality is implied without evidence:
   - Mind reading: "She thinks I'm incompetent" (how do you know what she thinks?)
   - Cause-effect: "His criticism made me angry" (did it make you angry, or did you choose to be angry in response?)
   - Equivalence: "If I can't do it perfectly, it's worthless" (are those two things actually equivalent?)
   - Presupposition: "When will you stop failing?" (presupposes you've been failing)
   - Example: "Their delay caused the project to fail" (was delay the only cause? did it definitely cause failure?)
   - Recovery question: "How specifically did their delay cause the failure? What else was required for it to fail?"

3. **For each distortion, write it in the "Distortion Type" column of the evaluation table.**

### Phase 2 — Generate Recovery Questions

4. **For each distortion, ask a targeted question to recover the missing or compressed information.** Use the category-specific patterns below:

   **For Generalizations:**
   - "Always? Have you ever seen an exception?"
   - "Never? Can you think of even one time when [opposite]?"
   - "Everyone? Is there anyone for whom this isn't true?"

   **For Deletions:**
   - Who? What? When? Where? How? (Basic who/what/when/where/how on the missing piece)
   - "Worried about what specifically?"
   - "What exactly do you mean by [vague noun]?"
   - "Compared to what?" (for comparisons without basis)
   - "How did they measure that?" (for outcomes)
   - "What process did you use to reach that conclusion?"

   **For Distortions:**
   - "How do you know that?" (for mind reading)
   - "Is that the only thing that caused [outcome]?" (for cause-effect)
   - "Are you saying [restate the equivalence as a question]. Is that always true?" (for equivalence)
   - "What would it take for [opposite claim] to be true?" (to test the claim's elasticity)

5. **Do not fill in the blanks yourself.** Ask the question and record the answer verbatim. Your job is to surface what the speaker knows but left unsaid, not to invent details.

### Phase 3 — Document the Recovery

6. **For each answer, record:**
   - The recovery question asked
   - The answer given (verbatim if possible)
   - Whether the answer was specific (actionable details) or remained vague
   - What information was recovered (the deleted piece, the exception to the generalization, the cause mechanism)

7. **Assess the depth.** If the first answer is still vague ("It just won't work"), ask a second-level recovery question on the same distortion. Continue until either the speaker provides specifics or it becomes clear the speaker doesn't know.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Original statement was recorded verbatim | Y/N |
| Each distortion (generalization, deletion, distortion) was identified and labeled | Y/N |
| At least one recovery question was asked for each distortion found | Y/N |
| Answers were recorded verbatim, not paraphrased | Y/N |
| At least 50% of answers contained specific, actionable details (not vague) | Y/N |
| No recovery question was leading or suggested the answer | Y/N |

## Red Flags

- No distortions were found. Either the original statement was unusually precise (rare) or the analysis missed obvious generalizations and deletions. Re-read looking for "always/never," missing nouns/verbs, and causal claims.
- All answers remained vague after the first question. Either you accepted vagueness (re-ask more concretely) or the speaker is uncertain. If the latter, note it explicitly.
- Recovery questions were leading ("So you admit it's always this way?"). The question should open up the space for specifics, not guide toward a predetermined answer.
- No deletions were found. Nearly every statement omits information. Look for pronouns with unclear referents, nominalizations (failure, resistance, communication), and missing comparison bases.
- You filled in the blanks yourself instead of asking ("So you mean X, right?"). The whole point is to recover what the speaker knows. If you're inventing, you've lost the method.

## Output Format

```
## Meta Model Recovery

**Original statement (verbatim):**
> <statement>

### Distortions Identified

| Distortion Type | Instance | Recovery Question | Answer Given | Specificity | Information Recovered |
|---|---|---|---|---|---|
| Generalization / Deletion / Distortion | <...> | <...> | <...> | Specific / Vague | <...> |

### Depth Assessment
- Total distortions found: _
- Total recovery questions asked: _
- Vague answers after first question: _ (these may require second-level probing)
- Statements with actionable specifics recovered: _

### Key Recoveries
1. <Information that was deleted/generalized/distorted>
2. <Information that was deleted/generalized/distorted>
3. ...

### Unanswered Distortions
<Distortions for which no specific answer was provided, even after follow-up>

### Confidence
<high/medium/low> — <justification. High: specific answers throughout. Medium: mix of specific and vague, or incomplete coverage. Low: answers remained vague, or distortions were difficult to identify.>
```
