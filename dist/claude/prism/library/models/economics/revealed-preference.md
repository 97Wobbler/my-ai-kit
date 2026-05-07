---
name: revealed-preference
display_name: Revealed Preference (Samuelson)
class: model
underlying_class: native
domain: economics
source: Paul A. Samuelson, "A Note on the Pure Theory of Consumer's Behaviour," Economica, 1938; formalized in Foundations of Economic Analysis (1947)
best_for:
  - Inferring preferences from observed choices without assuming utility functions
  - Testing whether behavior is consistent with rational choice
  - Predicting future choices from historical choice data
one_liner: "Infer preferences from observed choices and check consistency."
---

# Revealed Preference (Samuelson)

## Overview

Revealed Preference Theory claims that **a person's true preferences can be
inferred directly from their observed choices**, without needing to posit
an underlying utility function or assume anything about the decision
maker's mental states. The core insight is behavioral: if a person chooses
bundle A when bundle B is equally affordable, then A is *revealed to be
preferred* to B. The theory is descriptive and testable — it generates
testable consistency conditions (the Weak Axiom and Strong Axiom of
Revealed Preference) that any rational choice sequence must satisfy. When
these conditions are violated, you have evidence that either preferences
are not stable across choices, or the decision maker is not choosing
rationally, or the choice set was misspecified. The model is primarily
used to validate whether empirical choice data is consistent with rational
behavior, and to predict future choices given past choices.

## Core Variables and Relationships

The core relationship is between **choice sets, choices made, and
revealed-preference orderings**:

1. **Budget set B(p, y)** — the set of affordable bundles given prices p
   and income y.
   - Defined by the constraint: Σ(p_i · x_i) ≤ y
   - The choice set available to the decision maker at each decision
     point.

2. **Observed choice x(p, y)** — the specific bundle actually chosen from
   B(p, y).
   - Can be a single bundle (deterministic) or a probability distribution
     over bundles (stochastic).

3. **Direct revealed preference: x ≻^R y** — bundle x is directly
   revealed preferred to bundle y if:
   - x was chosen from a budget set B that included both x and y
   - When x was chosen, y was also affordable
   - Therefore, the chooser could have had y but chose x instead
   - Conclusion: x is revealed preferred to y

4. **Transitive closure (Strong Axiom):** If x is revealed preferred to y
   and y is revealed preferred to z, then x must be revealed preferred to
   z. This is the consistency requirement.

The **Weak Axiom of Revealed Preference (WARP):**
- If x is directly revealed preferred to y, then y cannot be directly
  revealed preferred to x.
- In other words, the revealed preference relation must not cycle.

The **Strong Axiom of Revealed Preference (SARP):**
- The transitive closure of direct revealed preferences must satisfy WARP.
- No cycles can arise from combining multiple direct comparisons.

Key insight: **No utility function is assumed.** The model works purely
from choice data. If choices satisfy WARP/SARP, they are *consistent with
rational behavior* — not because they maximize a utility function (which
may not exist or be unique), but because they obey an irreflexive,
transitive ordering.

## Key Predictions

- **If observed choices violate WARP** (e.g., when prices are p¹ and
  income y¹, bundle A is chosen despite B being affordable; when prices
  are p², bundle B is chosen despite A being affordable), then the
  choices are inconsistent with any stable preference ordering. Either
  preferences have changed between the two decisions, or the choice
  mechanism is not rational, or the choice set was misspecified (e.g.,
  constraints not captured).

- **SARP violations are rarer than WARP violations in real data**, because
  SARP requires consistency across all transitive chains. Small SARP
  violations in large datasets suggest noise in measurement or modest
  preference instability; systematic violations suggest structural
  irrationality.

- **From a sequence of choices consistent with SARP, future choices can be
  partially predicted.** If the revealed-preference ordering covers a
  bundle not yet chosen, you can predict which of two new options will be
  chosen (assuming preferences remain stable and choice sets are the same).

- **Stochastic revealed preference:** When choices are probabilistic
  rather than deterministic, the revealed preference relation becomes a
  partial order (a bundle may be preferred to another with some
  probability < 1). The consistency conditions must be relaxed to allow
  for decision noise, but violations of a **statistical** WARP indicate
  either preference instability or a misspecified choice model.

- **SARP data implies a utility function exists**, but it may not be
  unique and may not be smooth or continuously differentiable. The model
  does not predict *which* utility function, only that one is consistent
  with the choices. This bounds the predictive power: you can rule out
  certain future choices (those that would create a SARP violation) but
  cannot pin down unique future behavior.

## Application Procedure

Instantiate the model against a sequence of observed choices to test
consistency and make predictions.

1. **Define the choice domain and scope.** What is the decision maker?
   What is the set of all possible bundles (goods, time periods, states of
   the world)? What time period does the data cover? Example: "consumer
   household H, annual choice of quarterly consumption bundles (food,
   housing, transport), 2018–2023."

2. **Collect choice data: (p^t, y^t, x^t) for each time period t.**
   - p^t: prices (or attributes, if not monetary)
   - y^t: income or budget constraint
   - x^t: the bundle actually chosen
   - Ensure y^t is observable and that x^t was indeed in B(p^t, y^t)

3. **For each pair of periods (t, s), check if x^t ≻^R x^s.**
   - Does B(p^t, y^t) contain both x^t and x^s?
   - If yes, and x^t was chosen, then x^t ≻^R x^s is observed.

4. **Check WARP:** For all pairs (t, s) where x^t ≻^R x^s, verify that
   x^s ≻^R x^t does not hold.
   - If WARP is violated, stop and flag the inconsistency.
   - Document which pair(s) of choices violate it.

5. **If WARP holds, compute the transitive closure** of revealed
   preferences:
   - If x^t ≻^R x^s and x^s ≻^R x^u, then x^t ≻^R x^u.
   - Check SARP: does any cycle emerge?

6. **If SARP holds**, the choice sequence is consistent with a rational
   preference ordering (though not necessarily unique or continuous).

7. **For prediction:** given a new choice set B(p^new, y^new), apply the
   revealed-preference ordering to rule out certain outcomes.
   - If x^old ≻^R y^old is in the transitive closure, and both x^old and
     y^old are in B(p^new, y^new), predict that x^new will not be
     incomparable to y^old in a way that reverses the revealed ranking.
   - More concretely: if the revealed ordering is transitive, new choices
     should respect it.

8. **Check boundary conditions** (below). If any apply, note limitations
   on the consistency test or prediction.

## Boundary Conditions

Revealed Preference Theory assumes stable, rational choice from well-defined
budget sets. It breaks down or requires modification when:

- **Preferences are not stable over time.** If the decision maker's true
  preferences shift between observations (e.g., due to changed taste,
  learning, or external shocks), WARP violations can be observed without
  irrationality. You must either model preference change explicitly or
  segment the data into periods with stable preferences.

- **Choice sets are not accurately observed or captured.** If the chooser
  faces constraints (social, legal, informational) not visible to the
  observer, B(p, y) is mismeasured, and apparent WARP violations may be
  artifacts. Always verify that the budget set is correct.

- **Choices are probabilistic or subject to measurement noise.** Pure
  Revealed Preference is deterministic; observed bundles have no noise. If
  data is noisy (e.g., stated choices vs. actual, or small random
  perturbations), WARP violations will accumulate. Use stochastic revealed
  preference models (generalized axiom of revealed preference, GARP) to
  allow for error.

- **Multidimensional or non-monetary goods with quality uncertainty.**
  Real-world consumption often involves attributes that are not fully
  known at purchase (durability, fit, experience goods) or cannot be
  priced atomically. If the "bundle" is not precisely defined, revealed
  preference is ill-posed.

- **Strategic or social interdependence.** Revealed Preference assumes
  isolable choice: the decision maker's preference does not depend on
  others' choices or on signaling. In status-conscious consumption,
  network effects, or strategic games, this fails. Extend the model to
  include interdependence explicitly.

- **Extreme or rare events.** The model works best on repeated,
  stable-environment choices. For one-off catastrophic or life-changing
  decisions, the assumption of stable, rational preferences is harder to
  verify.

## Output Format

```
## Revealed Preference Analysis: <domain>

**Decision maker:** <entity>
**Scope:** <time period, bundle space, constraints>
**Data:** <number of choice observations, time range>

### Choice data summary
| Period | Prices p^t | Budget y^t | Bundle chosen x^t | Feasible set size |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

### Direct revealed preferences
| t | s | x^t ≻^R x^s | Notes |
|---|---|---|---|
| ... | ... | Yes/No | x^t was chosen when x^s was affordable / ... |

### WARP check
- **Result:** Satisfied / Violated
- **If violated:** [List specific pairs (t, s) where x^t ≻^R x^s but x^s ≻^R x^t, or where a preference reversal is observed]
- **Interpretation:** [Preference instability / constraint mismeasurement / irrationality]

### SARP (transitive closure)
- **Result:** Satisfied / Violated
- **If violated:** [Describe the cycle in transitive chain]

### Consistency verdict
- **Rational consistency:** Yes / Partial / No
- **Implications:** [What does consistency or violation imply about preferences or measurement?]

### Prediction for new choice set
**New budget B(p^new, y^new):** [describe prices and budget]
- **Bundles ruled out:** [which choices would violate the revealed-preference ordering]
- **Bundles consistent with revealed preferences:** [which choices respect the ordering]

### Boundary-condition notes
<which boundary conditions apply: preference stability, choice-set observability, measurement noise, interdependence>

### Confidence: high | medium | low
<reasoning: data completeness + budget-set accuracy + whether WARP/SARP holds + whether preferences appear stable + whether new predictions can be tested>
```
---
