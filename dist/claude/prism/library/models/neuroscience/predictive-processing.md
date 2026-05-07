---
name: predictive-processing
display_name: Predictive Processing
class: model
underlying_class: native
domain: neuroscience
source: "Karl Friston, \"The Free-Energy Principle: A Unified Brain Theory,\" Nature Reviews Neuroscience, 2010; Andy Clark, \"Whatever Next? Predictive Minds in Engaging World,\" Behavioral and Brain Sciences, 2013"
best_for:
  - Explaining perception, action, and learning as error minimization
  - Predicting how uncertainty, precision, and attention allocate neural resources
  - Analyzing failures in perception and action under model mismatch
one_liner: "Brain minimizes prediction error via generative models: top-down predictions suppress bottom-up error signals; precision-weighted errors drive learning and attention."
---

# Predictive Processing

## Overview

Predictive Processing claims that the brain's fundamental operation is to construct and refine an internal generative model of the world, using that model to generate predictions about incoming sensory data, and updating the model whenever predictions fail. The brain does not passively receive sensory input; instead, it actively predicts what it expects to sense, compares prediction to observation, and encodes the difference — the prediction error — as the sole signal that drives learning, attention, and action. The theory is both descriptive (explaining how brains work) and generative (predicting when and how perception, learning, and action succeed or fail). It unifies perception and action under a single principle: minimize prediction error either by adjusting the model (learning) or by adjusting the world to match predictions (action).

## Core Variables and Relationships

The model operates on the following variables and their interactions:

1. **Generative model m** — the agent's internal probabilistic model of how the world generates sensory observations.
   - Depth of the model (how many hierarchical levels of latent causes)
   - Scope of the model (which variables does it include)
   - Accuracy of m relative to true world generative process

2. **Prediction ŷ** — the model's expected sensory input given current beliefs about latent state.
   - Derives from m via forward inference
   - ŷ = E[sensory data | m, current beliefs]

3. **Sensory input y** — the actual observation.

4. **Prediction error δ** — the residual: δ = y − ŷ.
   - Drives all learning and attentional reweighting
   - Must be weighted by precision (inverse variance) to determine impact
   - Scales with model mismatch and uncertainty

5. **Precision (inverse variance) π** — the brain's implicit estimate of the reliability of a given prediction error signal.
   - High precision → the error signal is trusted and weighted heavily in updates
   - Low precision → the error is discounted (treated as noise, not model failure)
   - Precision itself is learned: the brain learns which sensory channels and which hierarchical levels are trustworthy
   - Attention is precision-weighting: paying attention to a signal means raising its precision

6. **Hierarchical message passing** — the brain is organized in layers (sensory cortex → association → frontal), and errors flow bottom-up while predictions flow top-down.
   - Each level generates a prediction for the level below and receives bottom-up error signals
   - High-level (abstract) error signals propagate down to update low-level (concrete) predictions
   - Low-level prediction errors that cannot be explained by high-level models cascade upward, forcing revision of abstract models

7. **Action (motor output) a** — minimizes prediction error by changing the world to match predictions.
   - Active inference: rather than always updating m to fit y, the agent can act to make y match ŷ
   - Moves are chosen to reduce predicted future prediction error (expected free energy)
   - Closes a feedback loop: perception → action → new sensory consequence → perception

**Core relationship:**
    
    Learning: m ← m + η · π(δ)  [model shifts in direction of weighted error]
    Attention: π ← π + Δ · δ²   [precision rises where errors cluster]
    Action: a ← argmin E[δ(future)]  [choose acts that predict low future error]

## Key Predictions

- **Prediction-error suppression under uncertainty.** When the brain is uncertain about a prediction (low precision for that channel), the same raw sensory signal produces weaker error signals and slower learning. Conversely, high-precision signals (trusted sensory modalities) drive rapid learning and strong percepts even from weak physical stimulation.

- **Hierarchical error propagation.** Low-level sensory errors (e.g., a brief unexpected flash) that are explainable by high-level models (e.g., "the light flickered") generate small cascading errors and do not revise high-level beliefs. The same sensory signal, if it violates a high-level prediction (e.g., an unexplained human face in a familiar context), generates large errors that propagate upward and force restructuring of abstract representations.

- **Attention as precision-weighting.** Allocating attention to a task or stimulus is equivalent to the brain raising the precision weight on that signal's errors, making the signal more influential in learning and decision-making. This predicts that attended stimuli produce larger error responses and faster learning, and that attention can amplify weak signals by increasing their precision weight, not by amplifying the signal itself.

- **Action under uncertainty.** When predictive uncertainty is high (the model is ambiguous about what will happen next), the brain preferentially chooses actions that **reduce uncertainty** (exploratory actions) over actions that locally minimize expected error. Under low uncertainty, exploitation dominates.

- **Mismatch-driven learning.** The rate and direction of learning is set entirely by prediction error and precision. Correct predictions generate no error, no learning, and no attention — even if the agent is extracting information efficiently. Learning is therefore invisible when the model is good.

- **Perceptual illusions under conflicting predictions.** When top-down predictions conflict sharply with bottom-up sensory signals, the brain does not average them; instead, it weights them by relative precision. If the top-down prediction is high-precision (strongly expected from context), the percept is pulled toward the prediction even against sensory evidence. If the bottom-up signal is high-precision (clear, reliable), the percept follows the signal. Neither dominates *per se*; precision does.

## Application Procedure

Instantiate the model against a concrete perceptual, learning, or motor phenomenon you are trying to explain or predict.

1. **Define the system boundary.** What is the agent? What is the timescale (milliseconds, seconds, minutes)? What sensory modality or behavioral task are you analyzing?

2. **Specify the generative model m.**
   - What latent causes (hidden states, features, objects, categories) does the brain's model assume generate observations?
   - What is the hierarchical structure (if any)? Are there abstract top-level causes that gate lower-level causes?
   - Is the model accurate, or are there systematic gaps or false assumptions?

3. **Identify the relevant prediction ŷ.**
   - Given the agent's beliefs and m, what does the brain predict to sense or experience next?
   - At what hierarchical level is the prediction being made (sensory pixels, features, categories, abstract meanings)?

4. **Observe or measure the actual sensory input y and compute the prediction error δ = y − ŷ.**
   - Is δ zero (prediction correct) or non-zero (mismatch)?
   - What is the magnitude and direction of δ?

5. **Estimate or infer the precision π of the error signal.**
   - Is this a reliable, high-signal sensory channel (e.g., proprioception) or a noisy one (e.g., vision in poor light)?
   - Is the prediction from a high-confidence model or a tentative one?
   - Look for neural signals of confidence (e.g., pupil dilation, activity in anterior insula or prefrontal cortex that correlates with uncertainty).
   - Context matters: the same sensory signal may carry higher precision in one context (expert musician hearing a slightly off note) than another (casual listener).

6. **Apply the core mechanism.**
   - **If learning:** the model should shift in proportion to π·δ. Prediction errors with high precision drive fast learning; low-precision errors are discounted.
   - **If attention:** precision should rise in regions where errors cluster. Over time, attentional resources should concentrate on high-error, high-precision signals.
   - **If action:** the agent should preferentially choose actions that reduce expected future prediction error (or expected free energy if uncertainty dominates).

7. **Trace hierarchical propagation** (if applicable). If the error δ cannot be explained by the current level of m, does it propagate upward, forcing revision of higher-level beliefs?

8. **Check boundary conditions** (below). Does the situation fit the core assumptions of the model?

9. **Generate the prediction.**
   - What should the agent's behavior, learning trajectory, or percept be, given the prediction error and precision structure?
   - Where does the model predict success vs. failure?

## Boundary Conditions

Predictive Processing is a powerful unifying framework but breaks down or requires extension under several conditions:

- **Model structure is unknown or ambiguous.** The model's predictions depend critically on what generative model m the brain actually uses. If m is not well-characterized (e.g., is it a simple linear model or a deep hierarchy? does it include temporal dynamics?), the predictions are vague and unfalsifiable. You must have independent evidence for m's structure — not just assume it.

- **Precision is unobserved or unmeasured.** The model's explanatory power rests on precision-weighting, but precision is a hidden variable. If you cannot measure or independently infer π (e.g., via confidence judgments, neural signals of uncertainty, or behavioral tracking), the model becomes post-hoc: any failure can be blamed on "low precision."

- **Learning has already saturated or there is no error.** Under a perfect or nearly perfect model, δ ≈ 0 everywhere, and the model makes no predictions about behavior, attention, or learning. In stable, familiar domains where the brain's model is accurate, Predictive Processing offers little leverage; you need domain-specific models instead.

- **The system is not hierarchical or feedforward error propagation doesn't apply.** Predictive Processing assumes a roughly hierarchical architecture with bottom-up error signals and top-down predictions. In highly recurrent, massively parallel networks (true of much of the brain), the message-passing picture may be too simplified. Similarly, if lateral connections dominate, the hierarchical view breaks down.

- **Payoffs, reward, or goals are not derivable from prediction error.** In situations where the agent has explicit rewards or goals independent of prediction error (e.g., an agent with an explicit objective function in reinforcement learning), Predictive Processing alone may not capture the full decision rule. Supplement with a goal-based or reward-based model.

- **Social or high-level reasoning is primary.** When decisions are driven by social norms, abstract reasoning, or rule-based thought rather than sensory prediction, Predictive Processing is a coarse-grained view. The model assumes the brain is fundamentally sensorimotor, which breaks down for abstract cognition.

## Output Format

```
## Predictive Processing Analysis: <phenomenon>

**System:** <agent and timescale>
**Task or context:** <what the agent is perceiving or doing>

### Generative model m
- Latent causes (hidden variables the brain assumes generate observations): <list>
- Hierarchical structure: <levels, if any>
- Model accuracy: <accurate / partially misspecified / severely misspecified, with evidence>

### Prediction and error
| Level | Predicted ŷ | Actual y | Error δ = y − ŷ | Notes |
|---|---|---|---|---|
| (e.g., sensory) | ... | ... | ... | ... |
| (e.g., feature) | ... | ... | ... | ... |

### Precision π
- Signal reliability: <sensory channel or modality, confidence in that channel>
- Contextual precision estimate: <high / medium / low, with reasoning>
- Observed neural/behavioral markers of confidence: <if available>

### Mechanisms activated
- Learning (model adjustment): <expected direction and rate, given π · δ>
- Attention (precision-weighting): <which signals should be amplified or suppressed>
- Action (error minimization): <if applicable, what actions would reduce prediction error>
- Hierarchical propagation: <does δ stay local or cascade upward>

### Prediction
- Expected behavior / perception / learning outcome: <per Predictive Processing>
- Confidence in this prediction: <high / medium / low, with reasoning>

### Boundary-condition check
- Model structure clarity: <is m well-characterized>
- Precision observability: <can π be independently verified>
- Applicability to domain: <does the task fit the PP assumptions>
- Additional mechanisms needed: <reward, social, abstract reasoning, etc.>

### Confidence: high | medium | low
<reasoning: clarity of generative model + observability of precision + domain fit + whether alternative frameworks (reinforcement learning, social reasoning, etc.) might better explain the phenomenon>
```
```
