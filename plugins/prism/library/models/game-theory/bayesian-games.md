---
name: bayesian-games
display_name: Bayesian Games (Harsanyi)
class: model
underlying_class: native
domain: game-theory
source: John C. Harsanyi, "Games with Incomplete Information Played by 'Bayesian' Players," Management Science, 1967–1968 (three-part series)
best_for:
  - Modeling strategic interaction when players have private information
  - Predicting equilibrium outcomes when uncertainty is asymmetric or mutual
one_liner: "Equilibrium analysis of incomplete-information games that explicitly handle private information and beliefs."
---

# Bayesian Games (Harsanyi)

## Overview

Bayesian Games is the analytical framework for modeling strategic interaction under **incomplete information** — situations where players do not know each other's payoff functions, constraints, or types. Harsanyi's central insight is that incomplete information can be represented as complete-but-imperfect information: introduce a "Nature" move that assigns each player a private type drawn from a known distribution, after which all players know the probability distribution over types but not the realized types of others. This transforms an incomplete-information problem into a standard game with enlarged strategy and belief spaces. The model is both descriptive and predictive: it explains why equilibrium behavior differs from complete-information benchmarks and predicts how uncertainty, asymmetry, and information revelation structure strategic choices. Applying the model requires the procedure below.

## Core Variables and Relationships

A Bayesian game is defined by:

1. **Players and types** — n players, each player i has a type θᵢ drawn from type space Θᵢ.
   - Type encodes all private information about player i's payoffs, constraints, or abilities.
   - Player i knows their own type θᵢ but not the types θ₋ᵢ of others.
   - Types are drawn from a common prior probability distribution p(θ₁, …, θₙ) known to all players.

2. **Beliefs** — each player i, upon observing their own type θᵢ, holds a posterior belief about the types of others: p(θ₋ᵢ | θᵢ).
   - Posterior is derived from the common prior and the player's own type via Bayes' rule.
   - Player i's strategy and equilibrium choice are conditioned on θᵢ and the implied belief.

3. **Strategies and payoffs** — each player i chooses an action aᵢ ∈ Aᵢ possibly depending on θᵢ.
   - Strategy is a mapping σᵢ(θᵢ) = aᵢ from type to action.
   - Payoff function u_i(a₁, …, aₙ; θᵢ) depends on all actions and *player i's own type θᵢ*.
   - Crucially, player i's payoff does not directly depend on others' types, only on their actions.

4. **Bayesian Nash Equilibrium** — a profile of strategies (σ₁*, …, σₙ*) such that for each player i and each type θᵢ:
   - σᵢ*(θᵢ) maximizes player i's expected payoff given their type, their beliefs about others' types, and the equilibrium strategies of others.
   - No player has incentive to deviate, conditional on their own type.

**Key relationships:**

- **Belief revision drives behavior.** When player i observes their own type θᵢ, they update their belief about others. This updated belief, not the common prior, determines the equilibrium action for type θᵢ.
- **Type correlation affects equilibrium.** If types are correlated (e.g., a strong opponent makes others weak), a player's type contains information about others' types, shifting the posterior and the equilibrium.
- **Information asymmetry vs. symmetry.** If players have symmetric information structures (e.g., both draw types from the same distribution and both know this), equilibrium often involves a **separating** or **pooling** pattern. Asymmetric information (e.g., one player has more precise information) breaks symmetry and typically leads to strategic information revelation through actions.

## Key Predictions

- **Private information generates endogenous mixing or type-dependent play.** Even in a game that would have a pure-strategy equilibrium under complete information, incomplete information often induces players to play different actions for different types or to play mixed strategies, because opponents cannot infer types from actions alone.

- **Inefficiency from adverse selection.** A player's action is a noisy signal of their type. Opponents interpret actions conservatively (updating toward the worst type consistent with that action), leading to outcomes where trade or cooperation fails even when it would be mutually beneficial. Example: a seller's refusal to guarantee quality signals that the product is low-quality, which depresses buyers' willingness to pay, deterring even good sellers from the market (Akerlof's used-car market is a special case).

- **Signaling and pooling.** If types differ in the cost of taking an action, an **out-of-equilibrium action** can serve as a credible signal. Types with low cost of signaling (strong players, high-quality sellers) use the action to separate from types with high cost, generating a separating equilibrium. Types that cannot afford to signal pool on a common action, with equilibrium payoffs reflecting the posterior belief about the pool.

- **Information revelation via play.** In repeated or dynamic extensions, players' past actions reveal their types over time. Strategic behavior often includes deliberate information concealment (mimicry) or selective revelation to maintain favorable beliefs.

- **Equilibrium existence and multiplicity.** A Bayesian Nash Equilibrium always exists (in mixed strategies) in finite games, but multiplicity is endemic when information is asymmetric. Small changes to the type distribution or payoff structure can shift which equilibrium is played.

- **Welfare loss vs. complete information.** Under incomplete information with private types, total surplus is typically lower than under complete information with the same realized types revealed. Uncertainty generates both deadweight loss from ex-ante inefficient choices and ex-post inefficiency when actions are not tailored to true types.

## Application Procedure

Instantiate the model against a concrete strategic interaction with private information.

1. **Define the game structure and the source of incomplete information.** What are the players? What actions are available? What is the nature of the private information (payoff uncertainty, constraint uncertainty, ability/signal uncertainty)? Write one sentence per player describing what they do not know about others.

2. **Specify the type space and prior distribution.** For each player i, define Θᵢ (what values can θᵢ take?) and p(θ₁, …, θₙ). Note whether types are independent or correlated; whether the information structure is symmetric (all players draw from the same type distribution and know this) or asymmetric.

3. **Write the payoff function u_i(a₁, …, aₙ; θᵢ) for each player.** Explicitly show how player i's payoff depends on θᵢ. If player i's payoff depends on others' types, the game is not a standard Bayesian game — flag this and note that a different framework (e.g., common-value auctions, interdependent-value games) may be needed.

4. **For each player type, compute the posterior belief p(θ₋ᵢ | θᵢ).** If types are independent, the posterior equals the marginal prior for others. If correlated, use Bayes' rule.

5. **Solve for Bayesian Nash Equilibrium.** For each player i and each type θᵢ, find the strategy σᵢ*(θᵢ) that maximizes:
   - E[u_i(σ₁*(θ₁), …, σₙ*(θₙ), θᵢ) | θᵢ]
   - expectation over θ₋ᵢ using the posterior belief p(θ₋ᵢ | θᵢ).
   - In low-dimensional games, this can be done by hand; in larger games, numerical methods or qualitative reasoning (separation vs. pooling) is standard.

6. **Compare to complete-information benchmark.** Solve the game assuming all types were commonly known. Highlight which predictions differ and attribute the difference to information asymmetry.

7. **Identify welfare loss or inefficiency.** Check whether the equilibrium outcome is Pareto efficient given the realized types, or whether players could have coordinated ex-post to improve both. Ex-ante efficiency (before types are drawn) and ex-post efficiency (after types are realized but before play) often diverge under incomplete information.

8. **Check boundary conditions** (below). Note whether any apply and what complementary analysis is needed.

## Boundary Conditions

Bayesian Games assumes a well-defined type space, a common prior, and rational Bayesian belief updating. The framework breaks down or requires modification when:

- **Types are multidimensional and continuous.** The framework handles any type space, but equilibrium existence and uniqueness proofs rely on compactness and convexity assumptions that may fail in high-dimensional spaces. Screening and signaling equilibria become much harder to characterize.

- **The common-prior assumption fails.** If players have different priors over the type distribution (or do not agree on the prior), the Harsanyi approach collapses — use non-Bayesian models or models of heterogeneous beliefs (e.g., interactive epistemology, self-confirming equilibrium).

- **A player's payoff depends on others' types, not just others' actions.** Example: in a common-value auction, all players care about the true value of the object, which depends on others' private signals. This requires a richer model (e.g., interim-efficient mechanisms, mechanism design with common values).

- **Information is endogenously revealed through play** and players are learning the type distribution on the fly. If the type distribution p is unknown and updated as the game is played repeatedly, Bayesian Games gives the equilibrium for a fixed prior, but the equilibrium itself changes as beliefs are updated. Use learning models (e.g., no-regret learning, belief learning) to capture this dynamic.

- **There is uncertainty about the game structure itself** — e.g., players are unsure about whether others are rational, or unsure about others' action sets. Standard Bayesian Games fixes the game structure; extending it to higher-order uncertainty requires models like Harsanyi's own type spaces or epistemic game theory.

- **Commitment, cheap talk, or costless communication** before play. The framework assumes no communication; if players can send verifiable signals (commitment) or unverifiable signals (cheap talk), a signaling subgame must be added, and the equilibrium is often different from the no-communication Bayesian game.

## Output Format

```
## Bayesian Game Analysis: <game name>

**Game structure:** <players, actions, source of private information>
**Type spaces:** θᵢ ∈ Θᵢ for each player i
**Common prior:** p(θ₁, …, θₙ) — note independence or correlation

### Payoff structure
| Player | Payoff u_i(a₁, …, aₙ; θᵢ) | θᵢ-dependence |
|---|---|---|
| ... | ... | ... |

### Type-conditional beliefs
| Player i, type θᵢ | Posterior p(θ₋ᵢ \| θᵢ) | Key implications |
|---|---|---|
| ... | ... | ... |

### Bayesian Nash Equilibrium
- Strategy profile: σ₁*(θ₁), …, σₙ*(θₙ) [write qualitatively or list outcomes for discrete types]
- Separating / pooling / hybrid: <characterization>
- Equilibrium payoffs (ex-ante, interim, ex-post): <comparison to complete-information outcome>

### Inefficiency
- Pareto-improvable ex-post: <yes / no, with specific example if yes>
- Deadweight loss vs. complete information: <estimate or direction>
- Information revelation / signaling: <who learns what about whom, through which actions>

### Boundary-condition check
<which boundary conditions apply and whether the Bayesian-game prediction is load-bearing>

### Confidence: high | medium | low
<reasoning: type-space tractability + prior-agreement fit + payoff structure transparency + empirical support>
```
