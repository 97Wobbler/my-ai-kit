---
name: pyramid-principle
display_name: Pyramid Principle
class: lens
underlying_class: native
domain: communication
source: Barbara Minto, "The Pyramid Principle," 1996
best_for:
  - Structuring arguments and recommendations for maximum clarity and persuasion
  - Diagnosing why a document or presentation fails to land with its audience
  - Building top-down narratives that respect reader attention
one_liner: "Conclusion first, hierarchical support — structure arguments for persuasion (Minto)."
---

# Pyramid Principle

## Overview
A communication framework that enforces top-down reasoning: state the conclusion or main idea first, then organize supporting arguments in a pyramid where each level answers a specific question raised by the level above. The reader (or listener) gets the point immediately and can choose to engage with details or stop. Practitioners use this when standard documents get rejected despite being "comprehensive," when presentations lose audience attention midway, or when stakeholders ask "what do you want from me?" before you've finished the preamble.

## Analytical Procedure

### Phase 1 — Extract and Validate the Main Idea

1. **Identify the single answer to the reader's key question.** Ask: "What is the reader asking?" (e.g., "Should we acquire this company?" "Why did sales miss target?" "How do we reduce churn?"). Write the answer in one sentence. This is your Pyramid Point — the apex.

2. **State it as a claim, not a topic.** Bad: "Acquisition strategy." Good: "We should acquire Company X because it closes our product gap in enterprise analytics." If you've written a topic, you don't have a conclusion yet — keep digging.

3. **Check for fit.** Does this claim actually answer the reader's question? If you're not certain the reader was asking this, pause and ask. A pyramid built on a misread question collapses regardless of structure.

### Phase 2 — Build the First Level (Supporting Arguments)

4. **Generate 3-5 supporting arguments that explain WHY your main idea is true.** Each must be at the same logical level — they should not overlap and together should feel complete (not "well, here are some reasons" but "here's the full case"). Write each as a complete sentence.
   - Do NOT write: "Cost savings, timeline, risk." (These are topics.)
   - DO write: "Acquiring Company X eliminates 18 months of R&D, costs 30% less than building in-house, and comes with 200+ enterprise customers we can cross-sell to."

5. **Test the logic between levels.** Does the reader naturally ask "Why?" after your main idea? Do your supporting arguments answer that "Why?" If the reader would ask "What do you mean?" instead, you have a clarification problem, not a support problem — restructure or add definition at the apex.

### Phase 3 — Build the Second Level (Evidence and Detail)

6. **For each first-level argument, write the supporting details that prove it.** Again, each set must be at the same level. If Argument A is "eliminates 18 months of R&D," the supporting details might be:
   - Their platform already handles multi-tenant analytics (3 years of development we'd replicate).
   - Their team has shipped 8 major releases in the past 2 years (proven velocity).
   - Our current roadmap requires 18 months to feature parity (documented in Q3 planning).

7. **Only go as deep as the reader needs.** If the reader stops engaging ("OK, I'm convinced"), stop. Unnecessary depth buries the signal.

### Phase 4 — Validate Structure Against Reader Questions

8. **Walk through the pyramid as if you were the skeptical reader.** At each level, ask: "Does this prove the claim above it?" and "Would I ask for evidence at this point, or move on?" If you'd ask a different question, the structure is wrong — restructure or cut.

9. **Check for hidden assumptions.** Look at your first-level arguments. Does the reader accept all of them, or will at least one need defending *before* they accept your main idea? If so, that argument doesn't belong in the "support" section — it belongs in a separate "pre-requisite" section earlier. (Examples: "We have the integration capacity" or "We can negotiate a reasonable price." Establish these first.)

### Phase 5 — Test Horizontal Logic (Mutual Support)

10. **Verify that your supporting arguments are collectively exhaustive and mutually exclusive.** Do they cover the full case without overlap? Could you drop one and still have a complete argument, or does it fill a gap? If you could drop one, it's redundant — cut it. If you could drop any two, your case is incomplete — find the missing piece.

11. **Reorder by logic flow, not by importance.** Many people put the strongest point first; Pyramid puts the most foundational point first — the one the reader must accept before the others make sense. (Often: necessity → feasibility → impact, or: problem → diagnosis → solution.)

## Evaluation Criteria

| Check | Pass |
|---|---|
| Main idea is stated as a claim, not a topic | Y/N |
| Main idea answers the reader's actual question | Y/N |
| First-level arguments are 3-5 items, all at same logical level | Y/N |
| Each argument is a complete sentence, not a label | Y/N |
| No argument is redundant; collectively they're exhaustive | Y/N |
| Second-level support directly proves each first-level argument | Y/N |
| All hidden assumptions are surfaced and addressed | Y/N |
| Structure passes the "Would I ask for this next?" test | Y/N |

## Red Flags

- Main idea is hedged ("might," "could," "possibly"). A pyramid collapses without a firm apex. Either you don't have a conclusion or you're not confident enough to present it — address the uncertainty separately, then restate the main idea cleanly.
- First-level arguments feel like a checklist ("marketing, sales, operations"). They're not at the same logical level. Group them by a shared principle or restructure the whole argument.
- Supporting details contradict the argument they're supposed to prove, or don't quite reach proof. This is usually a sign the argument itself is wrong — revise the argument, don't force-fit the evidence.
- The pyramid is longer than three levels. Each level adds complexity; if the reader needs a fourth level, either the third-level claims are weak or you're including unnecessary detail.
- You can drop the main idea and the supporting arguments still make sense on their own. The pyramid should be interdependent — each level justifies the one below.

## Output Format

```
## Pyramid Principle Assessment

**Reader's question:**
<What is the reader actually asking for?>

**Main idea (Pyramid Point):**
<One claim sentence>

### First Level — Supporting Arguments
1. <Complete sentence explaining why the main idea is true>
2. <...>
3. <...>
[etc., 3-5 total]

### Second Level — Evidence and Supporting Details

**For Argument 1:**
- <Specific fact or reasoning>
- <...>

**For Argument 2:**
- <...>

### Hidden Assumptions (and how they're addressed)
- <Assumption>: <How it's proven or accepted>
- <...>

### Structural Validation
- Exhaustive and mutually exclusive? <Y/N — if N, what's missing or overlapping?>
- Reader would naturally ask for this detail at this point? <Y/N>
- All claims are at the same level? <Y/N>

### Confidence
<high | medium | low> — <justification. Consider: Does the main idea truly answer the reader's question? Are all arguments defensible? Is the reader likely to follow this flow, or will they object earlier than you expect?>
```
