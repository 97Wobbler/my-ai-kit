---
name: expected-value
display_name: Expected Value
class: model
underlying_class: native
domain: decision
source: John von Neumann & Oskar Morgenstern, Theory of Games and Economic Behavior, 1944; foundational to decision theory and risk analysis
best_for:
  - Computing the long-run average payoff of a risky choice
  - Comparing alternatives when outcomes and probabilities are known
  - Identifying when emotional or reference-dependent reasoning diverges from expected value
one_liner: "Compare options by summing probability-weighted outcomes."
---

# Expected Value

## Overview

Expected Value is the foundational model for rational choice under risk. It
claims that the "worth" of an uncertain outcome is the probability-weighted
sum of its payoffs: if an event yields outcome x with probability p and
outcome y with probability (1−p), its expected value is E[·] = p·x + (1−p)·y.
The model is normative — it prescribes which choice maximizes long-run
payoff — and descriptive in the sense that it reveals what people *should*
choose if they are indifferent to risk, framing, and reference points. The
model is predictive when applied to repeated decisions with known
probabilities; it is diagnostic when applied to a one-shot decision to
expose the gap between a person's actual choice and the EV-optimal one. To
use it, apply the procedure below to a concrete decision.

## Core Variables and Relationships

Expected Value reduces a risky prospect to a single number via:

1. **Outcomes (payoffs)** — the consequences attached to each branch of the
   decision tree.
   - Outcomes must be measured in a common unit (dollars, time, utility
     units, etc.).
   - Outcomes can be positive, negative, or zero.
   - Multiple outcomes are possible (binary gamble, or n-way contingency).

2. **Probabilities** — the likelihood assigned to each outcome.
   - Each probability p ∈ [0, 1].
   - Probabilities sum to 1 across all outcomes for a given decision node.
   - Probabilities must be specified explicitly (frequentist, subjective,
     or model-derived).

3. **Expected Value (linear aggregate)**:

        E[X] = Σ (p_i · x_i)

   where p_i is the probability of outcome i, and x_i is the payoff for
   outcome i. This is a *linear* combination — each outcome is weighted by
   its probability, then summed. There is no asymmetry, no curvature, no
   distortion of probabilities.

4. **Decision rule** — choose the option with the highest expected value.
   For two prospects A and B, if E[A] > E[B], choose A. If E[A] = E[B],
   indifference.

The model assumes outcomes are measured in a fungible, integrable unit
(usually money) and that the decision maker cares only about the
probability-weighted average, not the variance, skew, or tail risk.

## Key Predictions

- **Bet acceptance.** A prospect with E[·] > your current payoff (or
  reference point) will be accepted if you are an expected-value
  maximizer. A bet with E[·] = 0 (fair coin flip, no edge) is taken as
  indifferent.

- **Portfolio convergence.** Over many repeated independent bets, the
  long-run average payoff per bet approaches E[·] by the law of large
  numbers. A strategy with E[·] = +$10 per bet accumulates, on average,
  +$10,000 over 1,000 bets, regardless of sequence.

- **Indifference to framing.** A $100 gain followed by a $50 loss has the
  same expected value as a $50 net gain stated directly — the order and
  framing do not change the EV calculation.

- **Risk-neutral equivalence.** An EV maximizer is indifferent between a
  certain payoff of $1,000 and a 50/50 gamble of $0 vs. $2,000 (both have
  E[·] = $1,000), provided outcomes are fungible and measured in the same
  unit.

- **Dominance detection.** If one option has a higher payoff in every
  possible state of the world, EV ranks it strictly higher. Dominant
  strategies are always preferred under EV.

## Application Procedure

Instantiate Expected Value against a concrete decision or a class of
decisions.

1. **Define the decision and enumerate the possible outcomes.**
   - What is the decision maker choosing between?
   - What are the terminal payoffs for each outcome? (money, lives saved,
     time, reputation points — what is the unit?)
   - Write out the decision tree: which node is the decision, which are
     chance nodes, what are the branches?

2. **Assign probabilities to each outcome.**
   - Use historical frequency data if available (e.g., "20% of startups in
     this sector fail within 5 years").
   - Use a model or calibrated expert judgment if data is sparse.
   - If probabilities are genuinely unknown (ambiguity), note this as a
     boundary condition — EV requires stated probabilities.
   - Check that probabilities sum to 1.

3. **Compute the expected value of each option.**
   - Multiply each outcome by its probability.
   - Sum across all outcomes for that option.
   - Write the number down: E[Option A] = $X.

4. **Rank the options by expected value.** Highest EV is the rational
   choice (or co-optimal if tied).

5. **Note the variance or range.**
   - EV ignores spread: a 50/50 bet of $0/$2,000 (E[·] = $1,000) is ranked
     identically to a 99/1 bet of $999/$10,010 (E[·] ≈ $1,000).
   - If the decision maker cares about risk (downside), note that EV is
     incomplete.

6. **Compare the EV-optimal choice to the actual choice (if observed).**
   - Does the person choose the highest-EV option?
   - If not, identify which bias or boundary condition is in play: loss
     aversion (see Prospect Theory), ambiguity aversion, concern for
     variance / downside, or a misestimate of probabilities.

7. **Check boundary conditions** (below). Flag any that apply.

## Boundary Conditions

Expected Value is a powerful, simple model but breaks down or misleads
under several conditions:

- **Unknown or ambiguous probabilities.** If the decision maker must
  decide under Knightian uncertainty (true unknowns, not just
  unobserved randomness), EV assumes away the problem. Supplement with
  ambiguity-aversion models (e.g., Ellsberg) or robust decision analysis.

- **Finite time horizon or single play.** EV is exact for repeated,
  independent decisions (law of large numbers kicks in). For a one-shot,
  high-stakes decision, variance and tail risk matter; an EV maximizer can
  go bankrupt on a single bad draw. Kelly Criterion or safety-first
  models handle this.

- **Non-monetary or non-integrable outcomes.** If payoffs are lives,
  environmental damage, reputational harm, or other non-fungible goods,
  the assumption that outcomes can be summed in a single unit breaks down.
  Use multi-attribute utility or capabilities approaches.

- **Reference-dependent or loss-averse decision makers.** People do not
  evaluate outcomes in absolute terms (final wealth) but relative to a
  reference point (see Prospect Theory). They weight losses ~2× as heavily
  as gains. EV predicts choice; Prospect Theory predicts behavior.

- **Strategic or game-theoretic settings.** EV assumes the probabilities
  and payoffs are exogenous. In games, they are endogenous to others'
  strategies. Use game theory or strategic interaction models.

- **Information asymmetry or costly observation.** If the true probabilities
  are private to one party or costly to learn, naive EV calculation can be
  manipulated or wrong. Supplement with signaling or mechanism-design
  models.

## Output Format

```
## Expected Value Analysis: <decision name>

**Decision:** <who is choosing between what>
**Unit of payoff:** <dollars / lives / time / other>
**Probability source:** <historical data / expert judgment / model / stated>

### Outcomes and probabilities
| Option | Outcome 1 | Probability | Outcome 2 | Probability | ... |
|---|---|---|---|---|---|
| A | $x | p | $y | (1−p) | ... |
| B | $x' | p' | $y' | (1−p') | ... |

### Expected value calculation
- E[Option A] = (p · outcome₁) + ((1−p) · outcome₂) = $X
- E[Option B] = ... = $Y

### EV ranking
Optimal choice (EV maximizer): **Option [A/B]** with E[·] = $X
Dominance: [Yes / No / Partial] — <if applicable, which option dominates>

### Variance and risk
- Spread in Option A: [range, std dev, or worst-case]
- Spread in Option B: ...
- Note: EV ignores variance. If downside risk or tail exposure matters, this
  model is incomplete.

### Actual vs. EV-optimal choice
- Observed choice: <if known>
- EV-optimal choice: <from above>
- Gap / explanation: <loss aversion, ambiguity, risk preference, or
  probability miscalibration?>

### Boundary-condition check
<which of the above apply and whether the EV recommendation is still
reliable>

### Confidence: high | medium | low
<reasoning: probability clarity + single-shot vs. repeated + outcome
fungibility + reference-dependence fit>
```
