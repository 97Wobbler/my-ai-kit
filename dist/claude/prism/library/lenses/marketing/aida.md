---
name: aida
display_name: AIDA
class: lens
underlying_class: native
domain: marketing
source: Elias St. Elmo Lewis (1898); formalized in advertising theory and modern marketing frameworks
best_for:
  - Diagnosing breakpoints in a marketing or sales message
  - Evaluating whether a campaign or ad moves prospects through the full funnel
  - Sequencing promotional content to match buyer psychology
one_liner: "Check that a marketing message covers Attention → Interest → Desire → Action."
---

# AIDA

## Overview

AIDA is a four-stage model of how a buyer moves from unawareness to purchase: Attention (you notice), Interest (you care), Desire (you want it), Action (you buy). The lens operates on marketing messages, campaigns, sales sequences, or ad copy. Practitioners use it to identify which stage their message is strongest in and which stages are underdeveloped — a message that nails Attention but skips Desire often fails in the real world, even if traffic is high. The discipline is recognizing that each stage has distinct psychological requirements and a message weak in any one stage can break the entire chain.

## Analytical Procedure

### Step 1 — Map the message to the four stages

1. **Identify the artifact.** What is the marketing message, campaign, or sales material? (Ad copy, email sequence, landing page, pitch deck, video, product listing, etc.)

2. **Read/view the artifact in full.** Do not paraphrase yet.

3. **For each of the four AIDA stages, extract the specific text, visuals, or claims that address it.** Mark them up directly on a copy of the artifact or in a table.

| Stage | Definition | Example from artifact |
|---|---|---|
| **Attention** | Something makes the prospect notice this message and pause. Novelty, emotion, relevance, contrast, or problem statement. The goal is to interrupt distraction. | <quote or describe> |
| **Interest** | The prospect now wants to know more. The message explains why this matters to *them* — not why it's impressive, but why it solves a problem or meets a need they have. | <quote or describe> |
| **Desire** | The prospect can now imagine themselves with this product or outcome. The message moves from abstract benefit to concrete, tangible value. It may include social proof, results, specificity, or emotional payoff. | <quote or describe> |
| **Action** | The prospect knows exactly what to do next and is nudged to do it now. Call-to-action, offer, urgency, friction removal. The path to conversion is explicit. | <quote or describe> |

4. **If a stage is absent or minimal, mark it as "Weak" or "Missing."** Do not assume the stage is happening implicitly.

### Step 2 — Evaluate the quality of each stage

5. **For each stage that is present, assess whether it actually accomplishes its psychological goal using these criteria:**

| Stage | Quality Check | Pass | Fail |
|---|---|---|---|
| **Attention** | The opening is distinctive enough to pause a skimming reader/viewer in under 3 seconds. (Not: background noise, generic, or expected.) | Y/N | |
| **Interest** | The message states a problem, need, or benefit *relevant to the target audience specifically*, not just "this is cool." | Y/N | |
| **Desire** | The message makes the value concrete and tangible — results, specificity, proof, or emotional resonance — not aspirational or abstract. | Y/N | |
| **Action** | The CTA is clear, low-friction, and time-bound or urgency-tagged (if appropriate). The next step is unambiguous. | Y/N | |

6. **Note any stage that fails its quality check.** This is a breakdown point.

### Step 3 — Assess sequence and gaps

7. **Check the order.** In the artifact, do the stages progress Attention → Interest → Desire → Action, or is there backtracking or skipping?
   - **Ideal:** Each stage builds on the previous one.
   - **Common failure:** Attention is strong, Interest is weak, so the message loses the prospect before they get curious.
   - **Another failure:** Interest and Desire are inverted; the message shows results before explaining the problem.

8. **Identify any stage that is completely missing or negligible.** Mark its impact: 
   - Missing Attention: Few people see or notice the message.
   - Missing Interest: People notice but don't care.
   - Missing Desire: People understand the benefit but don't emotionally commit.
   - Missing Action: People want it but don't know how to buy.

### Step 4 — Determine the breakpoint and severity

9. **Locate the stage where the chain breaks (highest dropout risk).** If all four are strong, the message likely works. If one is weak, that's your breakpoint.

10. **Classify the severity:**
    - **Critical:** Attention or Action missing. (No one sees it, or no one knows how to respond.)
    - **High:** Interest missing. (People notice but don't engage.) or Desire missing. (People understand but don't commit emotionally.)
    - **Medium:** The stage exists but is low-quality (e.g., a weak CTA, or interest that's generic).

## Evaluation Criteria

| Check | Pass |
|---|---|
| All four AIDA stages were searched for in the artifact | Y/N |
| At least one stage has a direct quote or specific reference from the artifact | Y/N |
| Stages are marked present/weak/missing, not assumed | Y/N |
| Each present stage was evaluated against its quality criteria | Y/N |
| A clear breakpoint (weakest stage) is identified | Y/N |
| Severity of the breakpoint is classified (critical/high/medium) | Y/N |

## Red Flags

- All four stages are marked "Strong" or all are "Present." Either the artifact is unusually excellent (rare) or the evaluation was not critical enough.
- The message has strong Desire but weak Action. (People want it but bounce when faced with a confusing checkout or form.)
- The message is heavy on Attention and Interest (product story) but lacks Desire (no proof, no specificity, no emotional landing).
- Attention is achieved only through manipulation or clickbait; when the prospect reads further, they feel misled. The Interest stage loses them immediately.
- No stage addresses the target audience's actual problem or need. (The message is about the product, not the buyer.)

## Output Format

```
## AIDA Assessment

**Artifact:** <type and title>

### Stage Breakdown

| Stage | Present? | Content excerpt | Quality |
|---|---|---|---|
| Attention | Yes/No/Weak | <quote or description> | Pass / Fail / N/A |
| Interest | Yes/No/Weak | <quote or description> | Pass / Fail / N/A |
| Desire | Yes/No/Weak | <quote or description> | Pass / Fail / N/A |
| Action | Yes/No/Weak | <quote or description> | Pass / Fail / N/A |

### Sequence Assessment
<Does progression follow Attention → Interest → Desire → Action? Any backtracking or skips?>

### Identified Breakpoint
**Weakest stage:** <Attention / Interest / Desire / Action>
**Severity:** Critical / High / Medium
**Reason:** <Why this stage fails or is missing>
**Impact on conversion:** <What happens when the prospect reaches this stage>

### Recommendations
1. <Specific fix for the breakpoint>
2. <Secondary issue if present>

### Confidence
<high/medium/low> — <justification based on artifact clarity and data available>
```
