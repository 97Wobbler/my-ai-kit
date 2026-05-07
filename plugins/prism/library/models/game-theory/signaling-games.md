---
name: signaling-games
display_name: Signaling Games (Spence)
class: model
underlying_class: native
domain: game-theory
source: Michael Spence, "Job Market Signaling," Quarterly Journal of Economics, 1973; extended in Market Signaling (1974)
best_for:
  - Explaining why agents with private information incur costly actions to separate themselves from lower-quality types
  - Predicting which equilibria emerge when signaling costs differ by type
  - Analyzing credential inflation, warranty commitments, and disclosure patterns in markets with asymmetric information
one_liner: "Type separation via costly signaling equilibria."
---

# Signaling Games (Spence)

## Overview

Signaling Games models a market where **one party privately knows their
type** (quality, ability, honesty) and the other party does not. The model
claims that in equilibrium, the informed party will incur costly actions —
signals — to **credibly reveal their type** and command a price or outcome
that reflects their true quality. The theory is explanatory and predictive:
it explains why separating equilibria exist (high types signal, low types do
not) and predicts the conditions under which such equilibria are stable. The
central intuition is that a signal is only credible if it is **cheaper for
the true type to send than for a false type to mimic** — otherwise
imitation destroys the signal's informativeness.

## Core Variables and Relationships

1. **Type space and prior beliefs.** The informed agent has type θ ∈
   {θ_L, θ_H} (or a continuum); the uninformed agent (or market) begins
   with a common prior belief μ about the distribution of types.
   - If μ favors low types, the equilibrium price is low and separating is
     valuable.
   - If μ is already optimistic, signaling becomes less necessary.

2. **Signal s and cost of signaling c(s, θ).** The informed agent chooses
   a signal s (e.g., education level, warranty duration, advertising
   spend). The cost of sending signal s depends on the agent's true type
   θ.
   - **Single-crossing property (critical):** c(s, θ_H) / ∂s <
     c(s, θ_L) / ∂s for all s. High types find signaling cheaper than low
     types — the cost schedule is steeper for low types. Without this,
     mimicry is indistinguishable and separation fails.
   - Low types face an incentive to mimic high types if mimicry is cheap;
     high types face an incentive to deviate to cheaper signals if the
     market does not read them as separating.

3. **Market inference and payoffs.** The uninformed agent (market, employer,
   buyer) observes the signal s and updates beliefs μ(θ | s) via Bayes'
   rule. It then offers a price or contract that depends on inferred type.
   - If the agent observes signal s_H from a type θ_H and signal s_L from
     a type θ_L, Bayes' rule pins down beliefs.
   - Each type gets a payoff u(θ, s, price(s)) = value(θ) − c(s, θ).

4. **Separating equilibrium.** An allocation (s_L, s_H) is a separating
   equilibrium if:
   - The market correctly infers: μ(θ_H | s_H) = 1, μ(θ_H | s_L) = 0.
   - No type wants to deviate: θ_H prefers (s_H, price_H) to
     (s_L, price_L), and θ_L prefers (s_L, price_L) to (s_H, price_H).
   - The incentive-compatibility (IC) constraint binds most tightly for
     the high type: the low type must be kept at zero excess rent by
     choosing s_L just high enough that θ_L indifferent between
     (s_L, price_L) and (s_H, price_H).

5. **Pooling equilibrium.** Both types send the same signal s*. The market
   cannot distinguish; beliefs are proportional to the prior μ. Pooling is
   stable only if both types prefer the average price to any deviation
   signal.

## Key Predictions

- **Separating equilibrium exists (and is stable) only if the single-crossing
  property holds.** If high types are more efficient at signaling than low
  types, they will separate by choosing a costly signal the low type will
  not mimic. The separating signal is **wasteful from a social efficiency
  standpoint** — it is pure rent-extraction, not productive — but it is
  the unique outcome consistent with incentive compatibility and rational
  expectations.

- **The separating signal must be "just binding" for the low type.** In
  equilibrium, s_L is chosen so that the low type is indifferent between
  separating (accepting s_L and the low price) and mimicking (copying
  s_H and hoping the market buys it). This means the high type is
  earning the full premium for type, while the low type earns only its
  true value. The signal is not randomly wasteful; it is precisely
  calibrated.

- **Multiple equilibria can coexist.** Depending on out-of-equilibrium
  beliefs, there can be separating equilibria at many different signal
  levels (s_L, s_H), all consistent with rational expectations. The model
  does not uniquely pin down the level of signaling; it only pins down
  the condition for stability.

- **Pooling equilibrium unravels if any signal reliably separates.** If the
  market observes that all type-θ_H agents send signal s* but type-θ_L
  agents send s* + ε (because signaling is cheaper for high types), the
  market updates and infers type from the signal, unraveling the pooling
  outcome.

- **A lower fraction of high types → higher equilibrium signaling cost.** If
  the population becomes more dominated by low types, the separating
  high-type signal must become more expensive to avoid imitation. The
  informativeness of the signal depends critically on the mix of types.

- **When signaling costs are type-independent, separation is impossible.**
  If both types face the same cost schedule c(s) independent of θ, no
  signal can credibly separate; the market cannot distinguish. The outcome
  reverts to pooling at the average price, low types are over-valued, and
  high types exit (Akerlof's adverse selection).

## Application Procedure

Instantiate the model against a market where information asymmetry and
signaling incentives are at play.

1. **Identify the informed and uninformed parties, and the type space.**
   Who has private information? What is the type θ (ability, quality,
   honesty)? What is the prior belief μ about the distribution of types
   in the population?

2. **Identify candidate signals.** What actions or credentials can the
   informed party send to reveal type? (education, warranty, advertising,
   price premium, contract terms). List at least two distinct signals
   under consideration.

3. **Establish the cost schedule c(s, θ) for each signal.**
   - For each signal, what does it cost (time, money, reputation risk) for
     a high-type agent to send it? For a low-type agent?
   - Is the single-crossing property satisfied? (Is ∂c / ∂s steeper for
     low types?) If not, note that separation is likely impossible.
   - If costs are nearly equal across types, flag that signaling fails.

4. **Identify the separating-equilibrium signals.**
   - Given IC constraints, which signal level s_L keeps the low type
     indifferent?
   - What signal s_H would the high type choose to separate?
   - Verify that neither type has an incentive to deviate.

5. **Check for pooling stability.** Would both types prefer a pooling
   outcome at the average price? If so, check whether the pooling is
   stable to small deviations by high types.

6. **Identify which equilibrium the market is likely in.**
   - Do you observe low types attempting to mimic high-type signals? If so,
     separation is breaking down or pooling dominates.
   - Do you observe credential inflation (signals becoming more costly over
     time)? If so, the separating equilibrium is present but informativeness
     is eroding.

7. **Generate the prediction.**
   - What signal(s) will the high type send, and what price will they
     command?
   - What will the low type do, and at what price?
   - Will the equilibrium be separating, pooling, or mixed (some high types
     separate, others pool)?

8. **Check boundary conditions** (below). If any apply, note limitations
   on the model's applicability.

## Boundary Conditions

Signaling Games relies on strong assumptions that may not hold in practice:

- **Exogenous type space and no type change.** The model treats type θ as
  fixed and exogenous (e.g., innate ability). In reality, signals often
  *create* ability (education is both signal and investment). If signaling
  changes type, the model's IC constraints no longer apply and outcomes
  can be vastly different (separation may be privately and socially
  beneficial). Distinguish between pure signaling and signaling-plus-investment.

- **Single-crossing property may be violated.** If low types are actually
  more efficient at sending a signal than high types (or costs are
  identical), the separating equilibrium collapses. Check empirically
  whether high and low types face meaningfully different costs; if
  marginal costs are similar, treat signaling as ineffective.

- **Observable signals only.** The model assumes signals are observable to
  the market and verified (education attained, credentials issued). If
  signals are claimed but unverifiable (claimed expertise, internal
  ratings), the equilibrium may not hold; introduce verification costs or
  reputational mechanisms.

- **Homogeneous market beliefs.** The model assumes all agents in the
  market share the same prior and update identically. If beliefs are
  heterogeneous (different evaluators weight signals differently), or if
  some agents use heuristics rather than Bayes' rule, the separating
  equilibrium is much less stable.

- **Static, one-shot interaction.** The model is a one-shot game. In
  repeated markets (labor markets, product reputation), agents learn true
  type over time and the signaling equilibrium may collapse as signal
  informativeness erodes. Use repeated-game or learning models for
  long-run behavior.

- **No signaling technology change.** The model treats the set of available
  signals as fixed. If new, cheaper signals emerge (e.g., skills tests
  replacing education), the equilibrium unravels and re-equilibrates at
  lower signaling cost.

## Output Format

```
## Signaling Game Analysis: <market / context>

**Informed party:** <who holds private information>
**Type space:** <θ_L, θ_H, or continuous; prior μ>
**Uninformed party:** <who makes the decision based on signal>

### Signal and cost structure
| Signal | c(s, θ_L) | c(s, θ_H) | Single-crossing? |
|---|---|---|---|
| <signal name> | <cost for low type> | <cost for high type> | Yes / No |

### Separating equilibrium (if it exists)
- **s_L:** <signal sent by low type>
- **s_H:** <signal sent by high type>
- **Incentive compatibility:** <verify low type indifferent, high type indifferent>
- **Price/payoff:** <price_L, price_H>
- **Stability:** <can either type profitably deviate?>

### Pooling equilibrium (if credible)
- **Pooled signal:** <both types send s*>
- **Market inference:** <beliefs are μ>
- **Stability:** <do either type want to separate?>

### Equilibrium prediction
- **Which equilibrium is played:** separating / pooling / mixed
- **Observed signal(s):** <what agents actually send>
- **Outcome:** <allocation and payoffs>

### Boundary-condition check
- **Single-crossing property:** Verified / Violated (detail)
- **Type exogeneity:** Type is fixed / Type is affected by signal
- **Signal observability:** Observable and verifiable / Unverifiable claims
- **Market homogeneity:** Homogeneous beliefs / Heterogeneous interpretation
- **Signaling technology:** Fixed / Evolving (note implications)

### Confidence: high | medium | low
<reasoning: cost-schedule clarity + stability of IC constraints + fit to
boundary conditions + observability of signals>
```
---
