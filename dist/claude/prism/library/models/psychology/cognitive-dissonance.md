---
name: cognitive-dissonance
display_name: Cognitive Dissonance
class: model
underlying_class: native
domain: psychology
source: Leon Festinger, "A Theory of Cognitive Dissonance," Stanford University Press, 1957
best_for:
  - Predicting attitude change following forced compliance or behavioral commitment
  - Explaining why people rationalize decisions that contradict prior attitudes
  - Identifying conditions under which cognitive conflict drives internal change vs. external excuse-making
one_liner: "Attitude change motivated by the drive to resolve cognitive dissonance."
---

# Cognitive Dissonance

## Overview

Cognitive Dissonance Theory claims that when a person simultaneously holds two cognitions (beliefs, attitudes, or knowledge of behavior) that are psychologically inconsistent, they experience a drive to reduce the discomfort — and that this drive often results in attitude change rather than behavior change. The theory is predictive: given the magnitude of dissonance and the person's available options for resolution, it predicts *which* cognition will shift. The central insight is that people will rationalize their behavior by changing their stated attitudes, especially when the behavior is difficult to undo and when external justifications are weak. This explains attitude reversals that seem irrational from a rational-choice perspective but are predictable from a dissonance-reduction view.

## Core Variables and Relationships

Cognitive dissonance arises when cognitions are inconsistent. The magnitude of dissonance depends on:

1. **Magnitude of inconsistency** — the degree to which two cognitions contradict each other.
   - Cognitions that are opposite or directly contrary produce high dissonance.
   - Cognitions that are merely tangential produce low dissonance.

2. **Importance of the cognitions** — how central each cognition is to the person's self-concept or value system.
   - High importance (e.g., "I am an honest person" vs. "I just lied") produces high dissonance.
   - Low importance produces low dissonance.

3. **Ratio of consonant to dissonant cognitions** — the relative weight of beliefs that support vs. contradict each other.
   - If many cognitions support the dissonant pair, the total dissonance is lower.
   - If few consonant cognitions buffer the inconsistency, dissonance is higher.

Once dissonance is present, the person has **three broad routes to resolution**:

- **Change a cognition** (most common when the inconsistent behavior is already committed or difficult to reverse).
- **Add new cognitions** that bridge or buffer the inconsistency.
- **Decrease the importance** of one of the conflicting cognitions.

The **magnitude of dissonance predicts the magnitude of attitude shift**. High dissonance drives larger changes. However, **the direction of change depends on which cognition is easiest to modify**: behavior is usually harder to undo than attitudes, so attitudes shift to justify behavior.

A critical moderator is **external justification**: if the person can point to an external reason for the behavior ("I was forced"; "I was paid well"), the dissonance is smaller and attitude change is weaker. If external justification is weak or absent, attitude change is larger.

## Key Predictions

- **Insufficient justification effect.** A person induced to perform a behavior that contradicts their stated attitude, with minimal external justification (small reward, weak coercion), will shift their attitude *toward* the behavior more than someone given large external justification. Dissonance drives the shift; excessive external justification makes attitude change unnecessary.

- **Attitude shifts are larger for important cognitions in the person's self-concept.** Inconsistency between "I am a moral person" and "I behaved immorally" produces larger attitude revision than inconsistency between "I prefer coffee" and "I just drank tea."

- **Post-decision dissonance.** After committing to a difficult or irreversible choice (e.g., buying a car, choosing a college), people will increase their evaluation of the chosen option and decrease their evaluation of the rejected alternative — not because new information arrived, but to reduce regret-driven dissonance.

- **Resistance to disconfirming evidence.** When dissonance is present, people will distort, avoid, or dismiss information that would increase dissonance. Conversely, they will seek out consonant information.

- **Forced compliance with weak justification produces larger attitude change than with strong justification.** This predicts a non-monotonic relationship: attitude change increases as external pressure decreases (until the person simply refuses).

- **Cognitive clustering.** Once one attitude shifts to reduce dissonance, related attitudes tend to shift as well, because they were originally consonant with the old attitude and dissonant with the new one.

## Application Procedure

Instantiate the model against a specific person facing or having faced inconsistency between cognitions.

1. **Identify the two (or more) conflicting cognitions.** Write them out explicitly.
   - Cognition A (usually a prior attitude or self-concept): "I believe X."
   - Cognition B (usually a behavior or newly acquired knowledge): "I did Y" or "I learned Z."
   - Are they directly contradictory, or merely tangential?

2. **Assess the importance of each cognition** to the person's self-concept or value system (high / medium / low).
   - How central is A to how the person sees themselves?
   - How central is B to their identity or values?

3. **Estimate the magnitude of dissonance** (high / medium / low) using:
   - Degree of contradiction (opposite → high).
   - Importance of both cognitions (high + high → high dissonance).
   - Strength of consonant cognitions that buffer the pair (few buffers → high dissonance).

4. **Identify available modes of resolution:**
   - Can the person undo the behavior (Cognition B)? If no, behavior is "stuck."
   - Can the person change the attitude (Cognition A)? If yes, how difficult?
   - Are there external justifications available (reward, coercion, social norm) that reduce dissonance?

5. **Assess the strength of external justification** for the behavior (strong / moderate / weak).
   - Strong: "I was well-paid" or "I was told to do it by authority."
   - Weak: "I did it, and there's no good external reason."

6. **Predict the direction of resolution:**
   - If behavior is irreversible and external justification is weak, predict **attitude shift toward the behavior**.
   - If external justification is strong, predict **minimal attitude shift** (the person relies on the external reason).
   - If both cognitions are mutable, predict shift in the cognition that is easier or less central to identity.

7. **Check boundary conditions** (below). If any apply, note that dissonance may not be the dominant driver.

## Boundary Conditions

Cognitive Dissonance Theory assumes the person has self-awareness, values consistency, and has cognitive freedom. It is less reliable when:

- **The person lacks self-awareness or does not monitor their own cognitions.** If someone does not notice the inconsistency, dissonance does not arise and attitude change will not follow.

- **Cultural or social context devalues consistency.** Some cultures or subgroups place lower weight on internal consistency, especially when external role or situational norms dominate. Dissonance may be weaker or resolved differently (e.g., via compartmentalization rather than attitude change).

- **The behavior is fully determined by external coercion or force.** If a person has no choice (e.g., imprisonment, complete physical constraint), they may not experience dissonance because they do not psychologically "own" the behavior. The cognition "I had no choice" blocks dissonance.

- **The person has strong, pre-existing justifications (ideology, worldview) that integrate the apparent contradiction.** A committed ideologue who believes "the end justifies the means" experiences less dissonance when their behavior contradicts their stated ethics, because a higher-order cognition (the ideology) already resolves it.

- **Immediate external feedback or reward overshadows the cognition.** If a person is rewarded or praised for the behavior immediately after, that external reinforcement may block attitude change even if dissonance was initially present.

- **The time horizon is very short or very long.** Dissonance is strongest in the intermediate term after the behavior. Much later, new attitudes may calcify, and dissonance effects may attenuate or reverse if the person builds a coherent revised identity.

## Output Format

```
## Cognitive Dissonance Analysis: <situation or person>

**Person/context:** <who and what is the situation>

### Conflicting cognitions
| Cognition | Content | Importance (H/M/L) | Mutability (easy/hard to change) |
|---|---|---|---|
| A (prior attitude/self-concept) | <belief> | ... | ... |
| B (behavior/new knowledge) | <behavior or fact> | ... | ... |

### Dissonance magnitude
- Degree of contradiction: <direct opposite / tangential>
- Consonant cognitions (buffers): <list any that reduce overall dissonance>
- Estimated dissonance magnitude: **High | Medium | Low**
- Reasoning: <which factors drive the magnitude>

### External justification assessment
- Strength: **Strong | Moderate | Weak**
- Nature of justification: <reward, coercion, authority, social norm, or none>
- How it affects dissonance: <does it reduce or increase felt dissonance>

### Predicted resolution path
- **Predicted mode:** Attitude change | Behavior reversal | Add consonant cognitions | Decrease importance
- **Predicted direction:** <which cognition shifts, and toward what>
- **Rationale:** <why this mode is available and most likely given mutability and external justification>

### Alternative outcomes
- If the person denies the inconsistency or increases its importance
- If the person adds a strong consonant cognition that integrates both

### Boundary-condition check
<which of the boundary conditions apply and whether dissonance is still the dominant driver>

### Confidence: high | medium | low
<reasoning: clarity of cognition identification + strength of the person's consistency drive + boundary-condition fit>
```
