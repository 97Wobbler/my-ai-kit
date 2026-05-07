---
name: self-efficacy
display_name: Self-Efficacy (Bandura)
class: model
underlying_class: native
domain: psychology
source: Albert Bandura, "Self-Efficacy: Toward a Unifying Theory of Behavioral Change," Psychological Review, 1977; extended in Social Foundations of Thought and Action (1986)
best_for:
  - Predicting whether a person will attempt a task and persist when faced with difficulty
  - Explaining performance gaps that are not explained by ability alone
  - Understanding why prior success or failure has asymmetric effects on future behavior
one_liner: "Belief in one's own capability predicts performance and persistence."
---

# Self-Efficacy (Bandura)

## Overview

Self-Efficacy Theory claims that a person's belief in their capacity to execute a specific behavior — not their objective ability, not personality traits, not motivation in the abstract — is the primary determinant of whether they will attempt that behavior and how long they will persist when faced with difficulty. The theory is predictive: it explains variance in performance, effort, and persistence that ability tests alone do not capture. Efficacy beliefs are task- and context-specific, not global; a person may have high efficacy for public speaking but low efficacy for mathematics, and these beliefs can be shifted through concrete experiences. The model is descriptive and explanatory — applying it requires the procedure below to map specific experiences and feedback onto efficacy beliefs, and then predict downstream behavior.

## Core Variables and Relationships

Self-efficacy is the product of four information sources, each weighted by the perceiver's judgment of its relevance:

1. **Enactive mastery (performance accomplishment)** — the strongest source.
   - Successful past performance on the same or similar task raises efficacy.
   - Failure lowers it, especially early attempts or when failure is seen as diagnostic of low ability.
   - Attributed causality matters: success due to effort/strategy raises efficacy more than success due to external help or luck.
   - Difficulty of past successes moderates the effect: success on an easy task raises efficacy less than success on a hard task.

2. **Vicarious experience (modeling)** — observing similar others succeed or fail.
   - Watching a similar other succeed raises the observer's efficacy ("if they can do it, so can I").
   - The magnitude depends on perceived similarity: watching an expert succeed has smaller effect than watching a peer.
   - Watching a similar other fail lowers efficacy, particularly if the observer attributes the failure to the other's lack of ability.
   - Multiple observations of peers succeeding accumulate more powerfully than a single observation.

3. **Verbal persuasion (social encouragement and feedback)** — the weakest of the four sources.
   - Praise, encouragement, and positive feedback from credible sources raise efficacy.
   - The effect is fleeting unless accompanied by enactive mastery.
   - Negative feedback ("you can't do this") lowers efficacy.
   - Source credibility and specificity matter: generic reassurance ("you'll be fine") has less effect than targeted coaching ("here's how to handle the difficult part").

4. **Physiological and emotional state (affective arousal)** — interpreted through cognition.
   - High anxiety, trembling, or fatigue in the face of the task cues low efficacy ("my body is telling me I can't do this").
   - Calm, energized arousal cues high efficacy ("I feel ready").
   - The same physiological state can be reinterpreted: athlete training-induced muscle soreness can be recoded as "good fatigue" (raising efficacy) rather than "warning signal" (lowering it).
   - Mood also modulates: depressed mood tends to lower efficacy estimates; positive mood tends to raise them.

**Core relationship:**

    Efficacy(task, context) = f(enactive mastery, vicarious experience, verbal persuasion, physiological state)

where enactive mastery is the highest-weight input, vicarious experience is moderate, verbal persuasion is weak, and physiological state is mediated by interpretation.

Once efficacy is formed, it predicts behavior through two mechanisms:

- **Choice to attempt the task.** Low-efficacy people avoid the task entirely; high-efficacy people attempt it.
- **Persistence under difficulty.** High-efficacy people increase effort and strategy; low-efficacy people quickly disengage.

## Key Predictions

- **Past success on the task itself is the strongest predictor of future attempt and persistence, more powerful than encouragement, watching others succeed, or ability test scores alone.** A person who has failed at public speaking in the past will avoid speaking opportunities despite being told they have the skill and watching confident peers succeed, unless they have a new enactive success to build on.

- **Failure early in learning has asymmetric, lasting effects.** Early failures disproportionately lower efficacy and lead to avoidance, even if later attempts would succeed. Early mastery experiences (even small ones) are load-bearing.

- **Similarity of the model (vicarious source) matters more than the model's raw ability.** Watching a "natural" athlete succeed at a difficult task raises efficacy less for an observer than watching a peer of similar background struggle and then succeed.

- **Efficacy predictions behavior better than ability in domains with high task difficulty or uncertainty.** On easy tasks, ability predicts performance; on hard or novel tasks where failure risk is real, efficacy dominates the prediction.

- **Verbal persuasion alone — encouragement without scaffolded success — produces short-lived belief changes.** When the person attempts the task and fails, the belief collapses. Persuasion's role is primarily to prevent avoidance long enough for enactive mastery to occur.

- **Physiological misinterpretation is exploitable.** High heart rate before a test can be reframed from "I'm too nervous to succeed" to "I'm aroused and ready" and this reframing raises efficacy and subsequent performance.

## Application Procedure

Instantiate the model against a specific person, task, and context.

1. **Define the task and context precisely.** What specific behavior is the person facing (e.g., "giving a presentation to 50 people in a board meeting," not "public speaking" in the abstract)? When and where? What are the stakes?

2. **Identify the four sources of efficacy information for this person and task.**
   - **Enactive mastery:** Has the person done this exact task or close variants before? When? With what outcome? How is the outcome attributed (ability, effort, external luck, difficulty of the task)?
   - **Vicarious experience:** Has the person observed similar others (peers, not experts) attempt this task? What was the outcome? How similar is the model to the person?
   - **Verbal persuasion:** Has the person received feedback, coaching, or encouragement on this task from credible sources? Generic ("you'll be great") or specific ("here's how to handle the Q&A")?
   - **Physiological state:** How does the person report feeling when facing this task (anxious, calm, energized, depleted)? How is this state being interpreted?

3. **Estimate efficacy level** on a 3-point scale (Low / Moderate / High) by weighting the four sources, with enactive mastery as the highest weight.

4. **Predict downstream behavior** based on the efficacy level.
   - Low efficacy → expect avoidance or minimal attempt; if attempt is forced, expect quick disengagement on difficulty.
   - Moderate efficacy → expect attempt, but effort/persistence will drop sharply if initial difficulty is high.
   - High efficacy → expect sustained attempt and increased effort/strategy under difficulty.

5. **Identify the highest-leverage intervention point.** Which source has the most room to shift? Usually enactive mastery (small early success) or vicarious experience (peer model) are higher leverage than verbal persuasion alone.

6. **Check boundary conditions** (below). If any apply, note that efficacy is incomplete and flag what complementary analysis is needed.

## Boundary Conditions

Self-Efficacy Theory is robust for predicting task-specific behavior, but it breaks down or becomes partial under several conditions:

- **Lack of agency or control.** The theory assumes the person can meaningfully influence the outcome through effort and strategy. In contexts of genuine powerlessness (oppressive systems, severe resource constraints), efficacy beliefs may not correlate with behavior because the person rationally perceives that effort doesn't change outcomes. Supplement with expectancy-value analysis that separates "can I do it?" from "will my effort be rewarded?"

- **Extreme skill gaps.** If the task requires a prerequisite skill the person lacks entirely (e.g., a non-reader attempting written exams), raising efficacy beliefs alone will not improve performance. Efficacy predicts persistence, not magical ability transfer. Prerequisite skill assessment is needed alongside.

- **Extrinsic motivation collapse.** High efficacy for a task combined with perceived meaninglessness or external-only reward structure sometimes leads to procrastination or minimal effort (particularly in adolescents and knowledge workers). Efficacy predicts *whether* effort will occur, not *how much* absent motivation. Combine with motivation/value analysis.

- **Group or organizational dynamics overriding individual efficacy.** In teams, social proof, conformity, and hierarchical dynamics may suppress high-efficacy individuals' behavior or boost low-efficacy individuals artificially. Efficacy is an individual-level variable; group effects require separate modeling.

- **Long time horizons between source and behavior.** Efficacy beliefs decay or shift when the interval between a success experience and the future task is very long (months or years) and no reinforcement occurs. Efficacy is relatively stable short-term but requires periodic updating.

- **Ambiguity in task definition or success criteria.** If the person is unclear what the task actually requires or how success is measured, efficacy beliefs may not map cleanly to behavior because the person cannot anchor efficacy to a concrete standard.

## Output Format

```
## Self-Efficacy Analysis: <task and person>

**Task:** <specific behavior, context, stakes>
**Person / population:** <who is attempting it>
**Task specificity:** <how closely does past experience match this task>

### Sources of efficacy information

| Source | Level | Evidence / reasoning |
|---|---|---|
| Enactive mastery | L/M/H | <past performance on this or similar task, attribution, difficulty> |
| Vicarious experience | L/M/H | <who has been observed, similarity, outcome> |
| Verbal persuasion | L/M/H | <feedback received, credibility, specificity> |
| Physiological / affective | L/M/H | <reported state, how is it being interpreted> |

### Overall efficacy estimate
<Low / Moderate / High, with reasoning on relative weight of sources>

### Predicted behavior
- **Attempt (yes / no / conditional):** <will the person choose to engage>
- **Persistence under difficulty:** <expected effort increase or disengagement>
- **Strategy adjustment:** <will the person try new approaches or give up>

### Highest-leverage intervention
<which source is most movable and what specific action would shift it>

### Boundary-condition check
<which boundary conditions apply; what complementary analysis is needed>

### Confidence: high | medium | low
<reasoning: clarity of enactive mastery history + relevance of vicarious sources + time horizon + whether task prerequisites and motivation are clear>
```
