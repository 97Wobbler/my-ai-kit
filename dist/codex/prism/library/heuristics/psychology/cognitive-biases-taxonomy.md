---
name: cognitive-biases-taxonomy
display_name: Cognitive Biases Taxonomy
class: heuristic
underlying_class: native
domain: psychology
source: Tversky & Kahneman, 1974; Kahneman, 2011
best_for:
  - Decision analysis under uncertainty
  - Diagnostic reasoning and root-cause investigation
  - Risk assessment and forecasting
one_liner: "Recognize anchoring, availability, and representativeness biases — check the three main routes of judgment error first."
---

# Cognitive Biases Taxonomy

## The Rule

When reasoning under uncertainty, first check whether your judgment is anchored to an initial number, shaped by how easily examples come to mind, or driven by how closely a case matches a stereotype — these three bias channels account for most systematic errors in judgment.

## When It Applies

- Estimating probabilities, costs, or durations when you have limited data.
- Diagnosing the cause of a problem when multiple explanations fit the evidence.
- Evaluating a person, proposal, or system when you must make a judgment with incomplete information.
- Forecasting outcomes in domains where base rates are low but available data is vivid.
- Reviewing a decision that went wrong, to understand which bias channel led the reasoning astray.

## When It Misleads

- The bias taxonomy is descriptive of *how* humans err, not prescriptive of *which* error is occurring in a specific case. Naming a bias does not diagnose the error or correct it.
- Anchoring, availability, and representativeness are not exhaustive. Overconfidence, sunk-cost fallacy, confirmation bias, and status-quo bias operate on different channels and require different checks.
- In domains where humans have strong feedback loops and calibrated experience (e.g., chess, weather forecasting by meteorologists, poker), these biases are substantially suppressed. Applying the taxonomy to experts in their domain of expertise weakens rather than sharpens judgment.
- Knowing about a bias does not immunize you from it. Mentioning "I might be anchored" while remaining anchored to the same number is theater.

## Common Misuse

Treating the taxonomy as a excuse to dismiss a reasoning chain without doing the work to understand it. "That estimate is just availability bias" is not a rebuttal; you must identify the specific vivid example that distorted the estimate and propose a correction based on base rates or broader evidence. Similarly, citing "representativeness" to reject a diagnosis without actually checking whether the case truly matches the stereotype is lazy reasoning dressed up as critical thinking.

## How Agents Use It

- **Embedded**: in forecasting, estimation, and diagnostic lenses, as a preliminary check step after the initial judgment is stated but before it is finalized. For each of the three channels (anchor, availability, representativeness), ask whether the judgment has been visibly shaped by that channel, and if so, propose a correction using base rates, explicit data, or a wider reference class.
- **Sanity-gate**: on each top finding that involves human judgment under uncertainty, ask: "Which of these three bias channels is most likely to have distorted the reasoning, and what evidence would prove the finding robust to that bias?" If the finding rests on a vivid example, weak base-rate reasoning, or an initial number that was arbitrary, require explicit correction before the finding is finalized.
