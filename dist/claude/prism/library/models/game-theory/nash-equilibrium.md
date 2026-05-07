---
name: nash-equilibrium
display_name: Nash Equilibrium
class: model
underlying_class: native
domain: game-theory
source: John Nash, "Equilibrium Points in N-Person Games," Proceedings of the National Academy of Sciences, 1950
best_for:
  - Predicting stable outcomes in strategic interactions where each player's best response depends on others' choices
  - Identifying when no player has incentive to unilaterally deviate from a proposed strategy profile
  - Analyzing competitive or cooperative situations with interdependent payoffs
one_liner: "Strategy profile where no player can gain by unilateral deviation given others' strategies."
---

# Nash Equilibrium

## Overview

Nash Equilibrium is the foundational solution concept in game theory that identifies **strategy profiles from which no player can improve their payoff by unilaterally changing their own strategy, holding others' strategies fixed**. It is predictive — it describes a state toward which strategic interaction tends to settle if players are rational, have correct beliefs about each other's play, and have no ability to commit or communicate before choosing. The model does not explain *how* players reach equilibrium, nor does it predict which equilibrium will occur in games with multiple solutions; it only identifies the set of stable outcomes and why they are stable. Applied to a concrete game, the procedure below identifies all pure-strategy Nash Equilibria and, when relevant, mixed-strategy equilibria.

## Core Variables and Relationships

A Nash Equilibrium is defined over a **strategy profile** — an assignment of a strategy to each player:

- **Players:** i = 1, 2, ..., N. Each player i has a set of available strategies S_i.
- **Strategy profile:** (s₁*, s₂*, ..., s_N*), where s_i* ∈ S_i is the strategy chosen by player i.
- **Payoff function:** u_i(s₁, s₂, ..., s_N) — the utility player i receives when the full strategy profile is (s₁, s₂, ..., s_N).

**Definition of Nash Equilibrium:**
A strategy profile (s₁*, s₂*, ..., s_N*) is a Nash Equilibrium if, for every player i:

    u_i(s₁*, ..., s_{i-1}*, s_i*, s_{i+1}*, ..., s_N*) ≥ u_i(s₁*, ..., s_{i-1}*, s_i, s_{i+1}*, ..., s_N*)

for all alternative strategies s_i ∈ S_i. In words: given that all other players are playing their equilibrium strategies, player i cannot improve their payoff by deviating to any other strategy.

**Best response:**
- Player i's **best response** to others' strategies (s₁, ..., s_{i-1}, s_{i+1}, ..., s_N) is a strategy s_i* that maximizes u_i given those others' choices.
- A Nash Equilibrium is a strategy profile where **each player's strategy is a best response to the others' equilibrium strategies simultaneously**.

**Pure vs. mixed strategies:**
- A **pure strategy** is a single deterministic action (e.g., "play Left" in a 2×2 game).
- A **mixed strategy** assigns a probability distribution over pure strategies (e.g., "play Left with probability 0.6, Right with probability 0.4").
- Games may have zero, one, or many Nash Equilibria in pure strategies; Nash's theorem guarantees at least one Nash Equilibrium exists in mixed strategies for any finite game.

## Key Predictions

- **Existence (finite games).** Every finite game has at least one Nash Equilibrium, though it may require mixed strategies. Most economic and social interaction stabilizes in equilibrium because deviating is individually irrational.

- **Multiplicity.** Many games have multiple Nash Equilibria. When they do, the model does not predict *which* will occur — only that if play settles on one, no player will unilaterally defect. This indeterminacy is a major limitation in coordination games and battle-of-the-sexes scenarios.

- **Inefficiency (Prisoner's Dilemma archetype).** A Nash Equilibrium need not be Pareto-efficient. Both players may be strictly better off if they could commit to cooperate, yet the equilibrium outcome is mutual defection because unilateral cooperation is punished. The model predicts inefficiency whenever individual incentives diverge from collective payoffs.

- **Symmetry.** In symmetric games (all players have the same strategy sets and payoffs are symmetric in the players), there often exists a **symmetric Nash Equilibrium** where all players play identical strategies. This is the most focal solution in symmetric contexts.

- **Uniqueness with dominance.** If a player has a **dominant strategy** (a strategy that is a best response no matter what others do), then any Nash Equilibrium must involve that player playing the dominant strategy. If all players have dominant strategies, there is a unique Nash Equilibrium.

- **Entry and exit dynamics.** In games with free entry (e.g., competitive industries modeled as one-shot contests), the Nash Equilibrium often predicts that entry continues until expected payoff equals zero, even though each firm incurs sunk costs. The model explains why industries with low barriers to entry have persistently low profits.

## Application Procedure

Instantiate the model against a concrete strategic situation.

1. **Define the game precisely.**
   - Who are the players? (Individuals, firms, countries, etc.)
   - What are the strategy sets for each player? (List all available pure strategies per player.)
   - What is the payoff structure? (Construct a payoff matrix if 2 players, or describe payoff functions if N > 2.)
   - Write the game in normal form (simultaneous-move) or transform an extensive-form game (sequential-move) into its reduced normal form via backward induction.

2. **Check for dominant strategies.**
   - For each player i, is there a strategy that yields a higher payoff than all others, regardless of what the other players do?
   - If yes, mark it. Any Nash Equilibrium must include dominant strategies.

3. **Identify pure-strategy Nash Equilibria.**
   - For each strategy profile in the payoff matrix:
     - Check whether each player's strategy is a best response to the others' strategies in that profile.
     - If yes for all players, it is a pure Nash Equilibrium. Mark it.
   - If no pure-strategy equilibrium exists, mixed-strategy analysis is needed (see step 4).

4. **Compute mixed-strategy Nash Equilibria (if needed).**
   - If the game has no pure-strategy NE, or if you want to identify all NE including mixed:
   - In a 2×2 game with no pure NE, each player will be indifferent between their two pure strategies at equilibrium. Set up the indifference condition and solve for the probability mixing weights.
   - For larger games, mixed-strategy computation is more involved; use a game-theory solver or linear complementarity conditions.

5. **Check for multiple equilibria and assess their stability/salience.**
   - If multiple NE exist, note which are Pareto-dominant (all players prefer it to others).
   - Note which are symmetric (all players play the same strategy), as symmetry is often focal.
   - Identify whether the game has coordination-game structure (both players benefit from matching) or conflict structure (payoffs are opposed).

6. **Predict play and outcomes.**
   - Which Nash Equilibrium is most likely to be played? (Use salience, symmetry, Pareto-dominance, or history as a tiebreaker; the model itself does not determine this.)
   - What is the equilibrium payoff for each player?
   - Is the equilibrium efficient? (Compare to the Pareto frontier.)

7. **Check boundary conditions** (below). If any apply, note that the Nash Equilibrium prediction may not hold and flag what additional analysis is needed.

## Boundary Conditions

Nash Equilibrium assumes rational, fully informed players in a one-shot or repeated game where they know the payoff structure and each other's rationality. It breaks down or becomes incomplete when:

- **Incomplete or asymmetric information.** Players do not know the true payoff structure, others' types, or their own payoffs with certainty. Use Bayesian games and Bayesian Nash Equilibrium instead. Standard NE assumes common knowledge.

- **Sequential moves (commitment and threat).** In extensive-form games, subgame-perfect equilibrium is the refinement; backward induction may eliminate off-path NE that are sustained by non-credible threats. A pure Nash Equilibrium of the normal form may not survive the sequential move structure.

- **Communication or collusion.** If players can communicate, form binding agreements, or observe and punish past play in a repeated game, they may coordinate on Pareto-dominant outcomes that are not Nash in the one-shot game. The model predicts the one-shot outcome, not the repeated-game outcome with observed history.

- **Learning and adaptation (out-of-equilibrium dynamics).** The model is static; it does not describe the path toward equilibrium. Players may cycle, fail to converge, or converge slowly if they use simple learning rules (fictitious play, gradient ascent) rather than rational expectations. In some games, equilibrium is never reached.

- **Very large N or continuous strategy spaces.** Computation becomes intractable; existence may fail if strategy sets are not compact or payoffs are not continuous. Existence theorems assume finite or nice topological structure.

- **Behavioral violations.** Players may have biases (overconfidence, framing effects, inequality aversion) or may not be purely self-interested. This requires behavioral game theory or extensions with social preferences.

## Output Format

```
## Nash Equilibrium Analysis: <game name>

**Players:** <list of players>
**Strategy sets:** <list of available strategies per player>

### Payoff matrix
| Strategy | Player 2: Left | Player 2: Right |
|---|---|---|
| Player 1: Up | (u₁, u₂) | (u₁, u₂) |
| Player 1: Down | (u₁, u₂) | (u₁, u₂) |
[Extend as needed; for N > 2 players, describe payoff functions instead]

### Dominant strategies
- Player 1: <none / strategy X>
- Player 2: <none / strategy Y>
[repeat for all players]

### Pure-strategy Nash Equilibria
1. Strategy profile: (s₁*, s₂*, ...)
   - Payoffs: (u₁*, u₂*, ...)
   - Is Pareto-efficient? <yes / no>
   - Is symmetric? <yes / no>
   
[List all pure NE; if none, state "None in pure strategies."]

### Mixed-strategy Nash Equilibrium (if applicable)
- Player 1 plays strategy X with probability p*, strategy Y with probability 1−p*
- Player 2 plays strategy A with probability q*, strategy B with probability 1−q*
- Expected payoffs: (u₁*, u₂*)

### Prediction
- Most focal equilibrium: <which, and why — salience, efficiency, symmetry, historical play>
- Equilibrium outcome: <describe)>
- Efficiency assessment: <is the NE Pareto-optimal? If not, what is the loss?>

### Boundary-condition check
<which boundary conditions apply (incomplete information, sequential moves, learning dynamics, etc.)
and whether the NE prediction remains robust>

### Confidence: high | medium | low
<reasoning: information structure (complete common knowledge vs. not), game structure
(one-shot vs. repeated), multiplicity of equilibria and whether focal equilibrium is clear>
```
