---
name: Prospect Theory
domain: economics
source: Daniel Kahneman & Amos Tversky, "Prospect Theory: An Analysis of Decision Under Risk," Econometrica, 1979; extended by Tversky & Kahneman 1992 (Cumulative Prospect Theory)
best_for: Explaining and predicting how people actually evaluate risky choices — especially loss aversion, framing effects, and distortions of small and large probabilities — when expected-utility theory predicts differently
one_liner: "Explain and predict loss-aversion and risk-attitude biases via reference point, value function, and probability weighting."
---

# Prospect Theory

## Overview

Prospect Theory is the empirical replacement for classical expected-utility
theory in describing how people actually evaluate risky options. Its
central claim is that people do not evaluate outcomes in terms of final
wealth (as expected utility assumes) but in terms of **gains and losses
relative to a reference point**, and that losses and gains are weighted
asymmetrically. The theory explains a large class of behavioral anomalies
that expected-utility theory treats as irrational: loss aversion, the
fourfold pattern of risk attitudes, certainty effect, framing effects, and
the endowment effect. Like any model, it is descriptive — applying it to a
concrete decision requires the Application Procedure below.

## Core Variables and Relationships

Prospect Theory evaluates a risky prospect via two transformations:

1. **Value function v(x)**, applied to outcomes measured as **gains or
   losses relative to a reference point r**. Shape:
   - **Reference-dependent.** x is *not* final wealth; it is (outcome − r).
   - **Concave in gains.** Diminishing sensitivity — a gain from +$100 to
     +$200 feels bigger than from +$1,100 to +$1,200.
   - **Convex in losses.** Diminishing sensitivity is symmetric in loss
     space.
   - **Steeper in losses than in gains** — the loss-aversion coefficient
     λ ≈ 2.0–2.5 in typical estimates. Losing $100 hurts ~2× as much as
     winning $100 feels good.

2. **Probability weighting function π(p)**, applied to stated
   probabilities. Shape:
   - **Overweights small probabilities** (e.g., a 1% chance is treated
     as if it were ~5%).
   - **Underweights moderate-to-large probabilities** (e.g., a 70%
     chance is treated as if it were ~55%).
   - **Certainty effect**: the jump from 99% → 100% carries
     disproportionate weight; same for 0% → 1%.

The decision-weighted value of a prospect (outcome x with probability p,
outcome y with probability 1−p) is:

    V = π(p) · v(x − r) + π(1−p) · v(y − r)

where v and π are the nonlinear functions above. The agent chooses the
prospect with the highest V — which is *not* the one with the highest
expected value.

## Key Predictions

- **Loss aversion.** People refuse a 50/50 gamble of winning $200 vs.
  losing $100, even though expected value is strongly positive. Below
  roughly 2× the loss, the gamble is rejected.

- **The fourfold pattern of risk attitudes:**

  |  | Low-probability event | Moderate-to-high probability event |
  |---|---|---|
  | **Gain domain** | **Risk-seeking** (lottery tickets) | **Risk-averse** (bird in hand) |
  | **Loss domain** | **Risk-averse** (buying insurance against rare disasters) | **Risk-seeking** (gambling to avoid a sure loss) |

- **Reference-point dependence.** The *same* final state can be framed as
  a gain or a loss depending on the implicit reference point, and
  preferences flip accordingly. This drives the framing effect and the
  status-quo bias.

- **Certainty effect.** A sure $3,000 is preferred to an 80% chance of
  $4,000 (expected value $3,200). But a 25% chance of $3,000 is rejected
  in favor of a 20% chance of $4,000. The pattern reverses because
  certainty carries disproportionate weight.

- **Endowment effect.** Willingness to accept for an item already owned is
  systematically higher than willingness to pay for the same item, because
  parting with it is coded as a loss.

- **Isolation effect / narrow framing.** People evaluate each decision in
  isolation rather than integrating with their portfolio, so the reference
  point is local to each decision.

## Application Procedure

Instantiate the theory against a concrete decision or behavior you are
trying to explain or predict.

1. **Identify the decision maker and the decision.** Who is choosing?
   What is the prospect, or set of prospects, on the table?

2. **Locate the reference point r.**
   - Is it current wealth? Recently experienced outcomes? A mental
     "target" or quota? The status quo? A salient comparison peer?
   - The reference point is often implicit and context-dependent — this
     step is frequently the load-bearing one. Write it down explicitly.

3. **Re-express all outcomes as gains or losses relative to r.** Do not
   reason in final-wealth terms.

4. **Apply the value function.**
   - Tag each outcome as gain domain or loss domain.
   - Note diminishing sensitivity (larger absolute outcomes have smaller
     marginal impact in *their* domain).
   - Note loss aversion (losses count ~2× in the agent's weighting).

5. **Apply the probability weighting function.**
   - Are any outcomes tied to small probabilities (<10%)? Expect
     overweighting.
   - Are any tied to near-certain probabilities? Expect the certainty
     effect.
   - Moderate probabilities are underweighted.

6. **Compute the weighted value of each prospect** (qualitatively is
   fine — the point is direction, not a precise number).

7. **Check boundary conditions** (below). If any apply, flag that
   Prospect Theory may not give the full picture.

8. **Generate the prediction.**
   - Which prospect will actually be chosen (per Prospect Theory)?
   - Which would be chosen under expected utility?
   - Explain the delta in terms of which mechanism (loss aversion,
     certainty effect, framing, probability weighting) drove the
     divergence.

## Boundary Conditions

Prospect Theory applies well to one-shot or isolated risky decisions by
an individual human. It is less reliable when:

- **Choices are repeated many times** and the agent can learn the true
  probability distribution (behavior converges partway toward EV over
  time).
- **The decision is made by a trained professional using an explicit
  model** (insurance underwriters, quants) — expertise partially
  overrides the biases.
- **Outcomes are not purely monetary** and social / reputational /
  emotional outcomes dominate — those need explicit modeling, not
  a v(x) on $ alone.
- **Ambiguity (unknown probabilities) rather than risk (known
  probabilities)** dominates. Prospect Theory assumes probabilities are
  stated; for true ambiguity, use Ellsberg-style models or
  ambiguity-aversion extensions.
- **Group decisions** — Prospect Theory is an individual model. Group
  dynamics, deliberation, and accountability shift the observed pattern.
- **Extreme outcomes** (catastrophic loss, life-changing gain) where the
  value function may not extrapolate cleanly.

## Output Format

```
## Prospect Theory Analysis: <decision name>

**Decision maker:** <who>
**Decision:** <prospects on the table>
**Reference point r:** <explicit, with reasoning>

### Outcomes in gain/loss space
| Outcome | Probability | Gain/Loss vs r | Notes |
|---|---|---|---|
| ... | ... | ... | ... |

### Mechanisms in play
- Loss aversion: <applies / not applicable, why>
- Diminishing sensitivity: <applies / not>
- Probability weighting: <which range, effect>
- Certainty effect: <applies / not>
- Framing / reference-point dependence: <key framing that locks r>

### Prediction
- Predicted choice (Prospect Theory): <which prospect>
- Choice under expected utility: <which prospect>
- Divergence driver: <which mechanism(s)>

### Boundary-condition check
<which of the boundary conditions apply and whether the prediction is
still load-bearing>

### Confidence: high | medium | low
<reasoning: reference-point clarity + fit to boundary conditions +
whether the person is trained to override biases>
```
