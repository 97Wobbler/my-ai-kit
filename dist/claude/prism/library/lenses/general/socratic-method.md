---
name: Socratic Method
domain: general
source: Socrates (via Plato); modern pedagogical adaptation by Richard Paul (Foundation for Critical Thinking)
underlying_class: native
best_for: Stress-testing a claim, proposal, or conclusion by surfacing hidden assumptions and unexamined implications
one_liner: "Stress-test claims via six question categories — clarification, assumption, evidence, perspective, implication, meta."
---

# Socratic Method

## Overview
Rather than refuting a claim directly, the Socratic Method interrogates it across six categories of questions until either the claim strengthens (because it survived scrutiny) or collapses (because it rested on assumptions that don't hold). Practitioners use it to pressure-test proposals before committing resources and to train themselves out of motivated reasoning. The discipline is asking the questions you'd rather not ask.

## Analytical Procedure

1. **Extract the core claim.** Write it as a single sentence with no hedging. If the original has multiple claims, pick one — run the method separately on each.

2. **Apply the six question categories in order.** For each category, generate at least 2 questions and answer them honestly. Do not skip categories that feel uncomfortable — those are the high-yield ones.

### Category 1 — Clarification
Goal: make the claim precise enough to be evaluated.
- What exactly do you mean by <key term>?
- Could you give a concrete example?
- How does this relate to <related concept>?
- Is this always true or only under certain conditions?

### Category 2 — Assumption probing
Goal: surface what the claim takes for granted.
- What is being assumed here?
- Is this assumption justified by evidence or by convention?
- What would someone who disagrees with this assumption say?
- How did this assumption become accepted?

### Category 3 — Evidence demand
Goal: distinguish belief from evidence.
- What evidence supports this claim?
- How was that evidence collected? By whom? Under what conditions?
- What would count as *disconfirming* evidence?
- Is the evidence causal or merely correlated with the conclusion?

### Category 4 — Perspective shift
Goal: check the claim against alternatives.
- What is the strongest counter-claim? State it in its best form (steelman, not strawman).
- Who benefits if this claim is accepted? Who is harmed?
- What would someone from an adjacent domain (a lawyer, a statistician, an end user) say about this claim?
- Are there contexts where this claim would clearly be wrong?

### Category 5 — Implication and consequence
Goal: trace what follows from the claim.
- If this claim is true, what else must also be true?
- What are the second-order effects of acting on this claim?
- Does the claim imply something that contradicts other things we believe?
- What is the worst plausible outcome if we act on this claim and it turns out to be wrong?

### Category 6 — Meta-question
Goal: examine the examination itself.
- Why is this question being asked right now?
- Are we answering the right question, or have we shifted topics?
- What question is being avoided?

3. **Mark each answer with a confidence tag:** `solid` (backed by evidence), `plausible` (reasonable but unverified), `shaky` (contradicted, hedged, or without support).

4. **Score the claim's resilience.** Count the `shaky` answers. If more than 30% of answers are shaky, the claim has not survived scrutiny — it needs revision or more evidence before being acted on. If 0% are shaky, suspect that the interrogation wasn't adversarial enough and ask harder questions, especially in Categories 2 and 4.

5. **Produce a revised claim.** Take the original and modify it to be honest about what survived. If nothing survived, say so.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Core claim extracted as a single precise sentence | Y/N |
| All 6 categories were applied (none skipped) | Y/N |
| Each category has ≥2 questions with answers | Y/N |
| At least one steelmanned counter-claim is present (Cat 4) | Y/N |
| Each answer is tagged solid/plausible/shaky | Y/N |
| Revised claim reflects the interrogation outcome | Y/N |

## Red Flags

- All answers are `solid`. Either the claim is trivially true (unlikely for anything worth interrogating) or the questioner was lenient.
- Category 4 (Perspective shift) has no genuine counter-claim, only "some might say X, but that's wrong because...". The counter was strawmanned.
- Category 5 (Implications) is empty or generic. The implications of the claim were never traced, so the reviewer doesn't actually know what acting on it commits them to.
- Revised claim is identical to original. Either nothing was learned or nothing changed — both are failures of the method.
- Category 6 was skipped. "Meta" questions feel silly but catch whole-category errors like topic drift.

## Output Format

```
## Socratic Assessment

**Original claim:**
> <verbatim>

**Core claim (extracted):**
<one precise sentence>

### Clarification
Q: <...>
A: <...> [solid | plausible | shaky]

### Assumption Probing
Q: <...>
A: <...> [tag]

### Evidence Demand
...

### Perspective Shift
Counter-claim (steelmanned): <...>
Q: <...>
A: <...> [tag]

### Implication
...

### Meta-question
...

### Resilience Score
- Solid: _  |  Plausible: _  |  Shaky: _
- Shaky ratio: _%
- Verdict: <survived | needs revision | collapsed>

### Revised Claim
<modified claim honest about what survived>

### Confidence
<high/medium/low> — <justification>
```
