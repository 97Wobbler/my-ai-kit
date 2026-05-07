---
name: double-effect-doctrine
display_name: Double Effect Doctrine
class: lens
underlying_class: native
domain: philosophy
source: Thomas Aquinas (Summa Theologiae, 13th c.); formalized in moral philosophy by Philippa Foot and extended by Judith Thomson
best_for:
  - Evaluating the moral permissibility of actions with foreseen but unintended harmful side effects
  - Distinguishing ethically defensible trade-offs from mere rationalization
  - Stress-testing consequentialist objections to a proposed action
one_liner: "Distinguish the moral weight of intended effects versus foreseen side effects."
---

# Double Effect Doctrine

## Overview
The Double Effect Doctrine holds that an action with both good and bad effects may be morally permissible if: (1) the act itself is good or morally neutral, (2) the good effect is intended while the bad effect is merely foreseen, (3) the good effect outweighs the bad, and (4) there is no better alternative available. The discipline lies in distinguishing genuine intention from motivated reclassification — practitioners reach for this framework when they suspect an argument conflates "we foresee this harm" with "we're okay with this harm." The lens applies to actions with unavoidable trade-offs: surgical decisions, resource allocation under scarcity, military or policing dilemmas, and policy choices where harm is structurally inseparable from benefit.

## Analytical Procedure

### Phase 1 — Extract the action and its effects

1. **State the action under scrutiny in one sentence.** Use the simple present tense and avoid loaded language. Example: "A surgeon removes a cancerous uterus from a pregnant woman" (not "the surgeon kills the fetus").

2. **List all foreseeable effects — good and bad.** Do not filter yet. Include second-order consequences. Order them by immediacy and certainty. Be specific about magnitude where possible.

3. **For each effect, ask: Is this effect intended, or merely foreseen?** Intended means the agent wants this outcome to happen and it is part of their goal. Foreseen means the agent knows it will happen but it is not the aim. Write a one-sentence justification for each classification. Red flag: if you're unsure whether something is intended, re-examine the argument's actual goal — often ambiguity masks equivocation.

### Phase 2 — Apply the four conditions

4. **Condition 1: The act itself (stripped of effects) is good or neutral.**
   - Identify the core action (the verb, abstracted from consequences).
   - Is this action inherently immoral (e.g., breaking a promise, deceiving), morally neutral (e.g., using a scalpel), or good (e.g., alleviating suffering)?
   - If the core action is inherently immoral, the doctrine does not apply — move to red flags.

5. **Condition 2: The good effect is intended; the bad effect is foreseen only.**
   - Review your intention tags from Step 3.
   - Is the bad effect truly unintended, or is it a causal means to the good effect? (Example: if you must harm X to help Y, and harming X is your chosen means, then harm is intended, not foreseen.)
   - Restate what the agent actually aims at. Is the bad effect absent from that aim?

6. **Condition 3: The good effect outweighs the bad.**
   - Assign rough magnitudes to good and bad effects. Use a scale (negligible, minor, moderate, serious, catastrophic) if numbers are unavailable.
   - List any asymmetries: Is the good effect certain and the bad uncertain, or vice versa?
   - Ask: Would a reasonable moral agent in this position, ignorant of which outcome would benefit them, accept this trade-off? (This is a sanity check against self-serving judgment.)

7. **Condition 4: There is no available alternative with better net effect.**
   - Enumerate at least three alternative actions, including inaction.
   - For each, estimate the good and bad effects.
   - Is any alternative clearly superior (more good, less bad)?
   - If an alternative exists that achieves the good without the bad, the doctrine is inapplicable — the harm was avoidable.

### Phase 3 — Test for rationalization

8. **Revisit the intention boundary.** Re-read the original argument. Does it rely on collapsing the distinction between "foreseen" and "intended" to make the trade-off seem acceptable? Common evasions:
   - "We accept the collateral damage because the mission is vital" (acceptance ≠ mere foresight; it suggests intention).
   - "We knew this would happen but we didn't plan for it" (foresight without intent, but is inaction equally foreseen? Why not act to prevent it?).
   - "The bad effect is structurally necessary" (may be true, but do not confuse structural necessity with moral permissibility).

9. **Check proportionality afresh.** Return to the magnitudes in Condition 3. Ask:
   - Would the agent accept this trade-off if the roles were reversed (agent bore the harm, someone else gained)?
   - Is the good effect distributed justly, or does it accrue only to those not bearing the bad effect?
   - How would the moral status change if the bad effect were larger, or the good effect smaller by 10%?

## Evaluation Criteria

| Check | Pass |
|---|---|
| Action stated plainly without moral framing | Y/N |
| All foreseeable effects (good and bad) are listed | Y/N |
| Each effect is classified as intended or foreseen with justification | Y/N |
| The core action (independent of effects) is assessed for inherent morality | Y/N |
| Condition 2 is re-examined for means-end conflation | Y/N |
| Magnitudes in Condition 3 are assigned (even roughly) | Y/N |
| At least three alternative actions are enumerated and compared | Y/N |
| Revisited intention boundary explicitly addresses rationalizations | Y/N |

## Red Flags

- The core action is inherently immoral (deception, betrayal, torture) but the agent argues the doctrine applies because the consequences are good. The doctrine cannot rescue a rotten means.
- The bad effect is a causal *means* to the good effect, not a side effect. Example: "We must harm the innocent to deter others." This is intended harm dressed as foresight.
- All alternatives enumerated are strawmen (absurdly costly or impossible). The doctrine requires genuine comparison; if no real alternative is worse, the doctrine does not apply.
- The magnitudes in Condition 3 are never specified — "the good outweighs the bad" without evidence. This is bare assertion, not argument.
- Condition 4 (no better alternative) is skipped entirely. This is evasion; the burden is on the agent to show they have no better option.
- The intention reclassification shifts mid-argument. Example: early in the argument, the bad effect is "merely foreseen," but later, the agent acts in ways that maximize it. Inconsistency signals motivated reasoning.
- The agent relies on statistical abstraction to obscure harm. "On average, this policy saves lives" while a specific identifiable person bears the entire bad effect (inverse of the person-affecting objection).

## Output Format

```
## Double Effect Assessment

**Action (plain language):**
<one sentence, no loaded terms>

### Foreseeable Effects
| Effect | Category (good/bad) | Intended or foreseen? | Magnitude | Justification |
|---|---|---|---|---|
| <...> | <...> | <...> | <...> | <...> |

### Condition 1: Core Action Morality
- Core action (abstracted): <...>
- Inherent moral status: <good / neutral / immoral>
- Pass: Y/N

### Condition 2: Intention Boundary
- Primary aim of agent: <...>
- Bad effect is truly foreseen only (not a means): Y/N
- Reclassification risk: <low / medium / high>
- Pass: Y/N

### Condition 3: Proportionality
| Outcome | Magnitude | Confidence | Notes |
|---|---|---|---|
| Good effect | <...> | <...> | <...> |
| Bad effect | <...> | <...> | <...> |
- Net assessment (good clearly outweighs bad): Y/N
- Reverse-role test (would agent accept if roles reversed?): Y/N
- Pass: Y/N

### Condition 4: No Better Alternative
| Alternative | Good effect | Bad effect | Verdict |
|---|---|---|---|
| <...> | <...> | <...> | <worse / equal / better> |
- Current action is least harmful (or tied for least harmful): Y/N
- Pass: Y/N

### Rationalization Check
- Intention boundary holds under re-examination: Y/N
- Bad effect is not a causal means: Y/N
- Proportionality is stable when magnitudes shift by ±10%: Y/N
- Risk of self-serving judgment: <low / medium / high>

### Verdict
<The action is permissible under the doctrine / The doctrine does not apply / The action fails the doctrine>

### Confidence
<high/medium/low> — <justification. High confidence requires: all four conditions clearly passed, no rationalization detected, magnitudes assigned with reasonable confidence. Medium if one condition is borderline or magnitudes are speculative. Low if the intention boundary is unclear, alternatives were not adequately enumerated, or the agent's true aim remains opaque.>
```
