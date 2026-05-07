---
name: underdetermination
display_name: Underdetermination
class: heuristic
underlying_class: native
domain: meta-science
source: Duhem–Quine problem, early 20th century
best_for:
  - theory selection
  - hypothesis testing
  - model evaluation
one_liner: "Among competing theories that explain the data equally well, none may be uniquely correct."
---

# Underdetermination

## The Rule
When multiple theories, models, or explanations fit the same data equally well, no amount of additional data from the same experimental or observational regime will distinguish between them; you need a different kind of evidence or a principled reason to choose.

## When It Applies
- Evaluating competing machine-learning models that achieve identical held-out accuracy on the same test set.
- Choosing between scientific theories that both account for existing experimental results but make no different predictions under current testable conditions.
- Architectural decisions where two designs satisfy all stated requirements and constraints equally well.
- Debugging when multiple root causes would produce the same observed failure signature.
- Model selection in econometrics, epidemiology, or climate science where identifiability is structurally limited by available data.

## When It Misleads
- When "equally well" is judged by a single metric that is blind to important aspects of performance (accuracy alone ignores latency, fairness, interpretability, or robustness to distribution shift).
- In domains where future data or novel conditions *will* discriminate between the theories, and the marginal cost of waiting or gathering new evidence is small relative to the cost of being wrong.
- When one theory is simpler, more elegant, or more aligned with known mechanisms in adjacent domains — underdetermination applies to the data, but not to the full epistemic context. Do not confuse "the data does not choose" with "all choices are equally justified."
- When the theories differ in their assumptions about unobserved variables or boundary conditions that, while empirically equivalent now, carry different risks if those assumptions are violated later.

## Common Misuse
Treating underdetermination as license to choose arbitrarily or to claim all theories are equally good. The heuristic says the data does not settle the question; it does not say the question is unsettleable. Common misuses include: citing underdetermination to avoid making a choice, using it to defend a preferred theory without acknowledging the indistinguishability, or ignoring side constraints (computational cost, interpretability, maintainability, alignment with domain knowledge) that break the tie even when the data does not.

## How Agents Use It
- **Embedded**: in model-selection or theory-evaluation lenses, after the fit-to-data step, as a mandatory check: "Are there alternative theories, models, or architectures that explain the same evidence?" If yes, do not declare one the winner without stating why.
- **Sanity-gate**: on each top finding that rests on choosing between equivalent explanations, ask: "What experiment, data source, or external constraint would discriminate between these?" If the answer is "nothing we can reasonably test," flag the choice as underdetermined and state the justification for the pick explicitly (elegance, precedent, risk profile, etc.) rather than claiming the evidence settled it.
