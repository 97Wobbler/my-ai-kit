---
name: prisoners-dilemma
display_name: Prisoner's Dilemma
class: model
underlying_class: native
domain: game-theory
source: Merrill Flood & Melvin Dresher, RAND Corporation, 1950; formalized by Albert W. Tucker, 1950
best_for:
  - Explaining why rational individual incentives can produce collectively suboptimal outcomes
  - Predicting defection in repeated or one-shot interactions without binding commitment
  - Identifying conditions under which cooperation emerges despite incentive misalignment
one_liner: "Archetype of non-cooperative games where individual rationality leads to collective irrationality."
---

# Prisoner's Dilemma

## Overview

The Prisoner's Dilemma model claims that when two agents each face a
choice between cooperation and defection, **rational individual incentives
produce mutual defection even though both would be better off cooperating**.
The core mechanism is simple: defection is a strictly dominant strategy
(it is best for me regardless of what you do) for both players, yet when
both exploit this dominance, both end up worse off than if both had
cooperated. The model is both descriptive — it explains actual patterns of
defection in negotiations, arms races, and commons-management — and
predictive, because the structure of incentives determines the outcome
mechanically. The model applies most directly to one-shot interactions or
situations where agents cannot commit to future reciprocity.

## Core Variables and Relationships

The Prisoner's Dilemma is defined by four payoff values:

1. **Mutual cooperation (C, C).** Payoff to each player: R (reward for mutual cooperation).

2. **Mutual defection (D, D).** Payoff to each player: P (punishment for mutual defection).

3. **Unilateral defection.** One player defects, one cooperates.
   - Payoff to the defector: T (temptation — the sucker's best outcome).
   - Payoff to the cooperator: S (sucker's payoff — the worst outcome).

The defining constraint that creates the dilemma:

    T > R > P > S

This ordering ensures:
- **Defection is strictly dominant.** For any choice by the other player, I do better by defecting: T > R (if they cooperate) and P > S (if they defect).
- **Mutual cooperation dominates mutual defection in total welfare.** R > P, so both prefer (C,C) to (D,D).
- **The gap between individual and collective rationality is real.** Individually rational play (each choosing D) produces a Pareto-inferior outcome (both get P when they could both get R, an improvement of 2(R − P)).

The magnitude of the gap is driven by how far T exceeds R and how far P exceeds S. A larger spread (T − R or R − P) makes defection more tempting and mutual cooperation harder to sustain.

## Key Predictions

- **In a one-shot interaction with no side-effects, both players defect.** The structure of the payoff matrix is self-enforcing; no external enforcement is required to produce defection.

- **Mutual defection is a Nash equilibrium.** Neither player can unilaterally improve by switching to cooperation given the other is defecting.

- **Mutual cooperation is not a Nash equilibrium in the one-shot case.** If you expect the other to cooperate, your best response is to defect and claim the temptation payoff T.

- **In repeated play with indefinite time horizon and sufficiently high discount factor, cooperation can emerge via tit-for-tat or similar trigger strategies.** The threat of permanent retaliation shifts the incentive structure: defection today costs more (in lost future cooperation) than it gains.

- **Introducing commitment devices, monitoring, or reputational consequences can shift the outcome from (D,D) toward (C,C).** These mechanisms change the effective payoff matrix by adding costs to defection or enforcement benefits to cooperation.

- **Increasing the number of players (n-player public goods variant) does not change the fundamental logic but does reduce the individual incentive to cooperate.** In a public goods game, one free-rider's defection is subsidized by all cooperators; the larger the group, the more attractive free-riding becomes.

## Application Procedure

Instantiate the model against a concrete two-player (or n-player) interaction to predict the equilibrium outcome.

1. **Define the scope and horizon.** Identify the two agents (or group). Is this a one-shot interaction, or repeated? Can agents commit to future behavior, or can they only condition on observed history? Write this down explicitly.

2. **Map the decision alternatives onto cooperation and defection.** Define what "cooperating" and "defecting" mean in this context. Cooperation is the choice that benefits both if mutual; defection is the choice that benefits one at the cost of the other if it exploits mutual cooperation.

3. **Assign payoff values** for each outcome:
   - (C,C): mutual cooperation payoff R
   - (D,D): mutual defection payoff P
   - (D,C) from your perspective: temptation T (if you defect and they cooperate)
   - (C,D) from your perspective: sucker's payoff S (if you cooperate and they defect)

4. **Verify the ordering T > R > P > S.** If this does not hold, the model does not apply — the game is not a Prisoner's Dilemma.

5. **Check the interaction structure.** Is this truly one-shot, or is there shadow of the future (repeated play)? Are there reputational costs to defection? Can players communicate or commit?

6. **Predict the outcome:**
   - One-shot, no commitment: predict mutual defection (D,D).
   - Repeated indefinitely, players can observe and condition on history: predict possible cooperation via trigger strategies (e.g., tit-for-tat), conditional on discount factor being sufficiently high. The critical condition is δ ≥ (T − R) / (T − P), where δ is the discount factor.
   - Repeated with finite horizon: predict defection in the final round and backward induction into defection in all earlier rounds unless players use other commitment or reputation mechanisms.

7. **Identify mechanisms that shift the outcome:**
   - Legal enforcement or third-party punishment
   - Monitoring (detection of defection)
   - Reputational costs (defection becomes observable to future partners)
   - Communication and binding agreements
   - Repeated play with shadow of the future

8. **Check boundary conditions** (below).

## Boundary Conditions

The Prisoner's Dilemma model assumes a symmetric, isolated dyad (or n-player group) and breaks down or becomes incomplete under:

- **Asymmetric information or beliefs about the other player's type.** If you are uncertain whether the other will cooperate or defect, or whether they face the same payoff matrix, the simple dominant-strategy logic no longer applies. Use a Bayesian game model instead.

- **Repeated play with finite (known) horizon.** The model predicts cooperation, but backward induction produces defection in the final round and unravels all cooperation. In practice, observed behavior often sustains cooperation near the end, suggesting agents use other models (e.g., reputation, implicit tit-for-tat) or have uncertainty about the true horizon.

- **Correlated play or communication.** If players can correlate their strategies (e.g., by publicly committing or coordinating before play), the model's one-shot prediction fails. The dilemma is fundamentally about non-binding play; binding contracts resolve it.

- **Preference heterogeneity or non-monetary motives.** The model assumes payoffs are comparable across players and outcomes are defined purely in material terms. If cooperation is intrinsically valued (altruism, fairness, identity), or if defection carries reputational or moral cost, the effective payoff matrix changes and defection may no longer be dominant.

- **More than two players with free-rider dynamics.** In n-player settings (public goods, common-pool resources), the incentive to free-ride can dominate even more strongly than in two-player games because one defector's gain is spread across the cost to all cooperators. The model remains valid but the prediction of defection is even stronger.

- **Nested or multi-level dilemmas.** Real-world systems often involve overlapping Prisoner's Dilemmas (e.g., firm-level defection vs. industry-level cooperation, or individual incentives vs. organizational norms). The model applies locally but may miss emergent coordination at higher levels.

## Output Format

```
## Prisoner's Dilemma Analysis: <interaction name>

**Agents:** <who, number of players>
**Interaction horizon:** <one-shot / repeated / indefinite horizon>
**Binding commitment possible:** <yes / no>

### Payoff matrix
| Outcome | Agent 1 | Agent 2 | Notes |
|---|---|---|---|
| Both cooperate (C,C) | R | R | <define cooperation in context> |
| Both defect (D,D) | P | P | <define defection in context> |
| Agent 1 defects, Agent 2 cooperates | T | S | <temptation; sucker payoff> |
| Agent 1 cooperates, Agent 2 defects | S | T | |

### Dominance check
- T > R > P > S: <yes / no — if no, Prisoner's Dilemma does not apply>
- Magnitude of temptation (T − R): <value>
- Magnitude of punishment gain (R − P): <value>

### Predicted outcome
- One-shot or finite horizon: <mutual defection (D,D)>
- Repeated indefinitely: <depends on discount factor δ; cooperation possible if δ ≥ (T−R)/(T−P); critical threshold: [value]>
- Actual discount factor: <if known, compare to threshold>

### Mechanisms in play
- Reputational cost to defection: <yes / no; if yes, effective payoff matrix shifts>
- Monitoring: <yes / no; can defection be detected>
- Binding agreement: <yes / no; if yes, (C,C) is enforceable>
- Shadow of the future: <strong / weak / absent>

### Prediction
- Expected outcome under Prisoner's Dilemma: <(C,C) / (D,D) / mixed with reasoning>
- Confidence in prediction: <high if one-shot or highly repeated; lower if finite horizon or reputational effects are uncertain>

### Boundary-condition notes
<which of the above conditions apply and whether the model's prediction
is still load-bearing, or what complementary analysis is needed>

### Confidence: high | medium | low
<reasoning: clarity of payoff structure + interaction horizon certainty + strength of mechanisms shifting the outcome>
```
