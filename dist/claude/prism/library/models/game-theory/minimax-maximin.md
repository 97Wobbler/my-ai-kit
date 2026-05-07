---
name: minimax-maximin
display_name: Minimax / Maximin
class: model
underlying_class: native
domain: game-theory
source: John von Neumann, "Zur Theorie der Gesellschaftsspiele," Mathematische Annalen, 1928; formalized in von Neumann & Morgenstern, Theory of Games and Economic Behavior, 1944
best_for:
  - Choosing strategy under worst-case adversarial conditions
  - Equilibrium analysis in zero-sum and near-zero-sum games
  - Risk-averse decision-making with incomplete information
one_liner: "Optimize for the worst case in adversarial settings."
---

# Minimax / Maximin

## Overview

Minimax / Maximin is a prescriptive decision principle for choosing a strategy when an agent faces an intelligent adversary (or an unknown environment that behaves like one). The core claim is: **choose the strategy that maximizes your minimum payoff, where the minimum is taken over all possible opponent responses**. Equivalently, the opponent reasons by minimax — they minimize your maximum payoff — and the agent must account for this. The model is both descriptive (explaining play in zero-sum games where players are rational) and prescriptive (recommending a choice when facing adversarial uncertainty). Unlike probability-weighted decision theories, minimax does not assume the agent knows the opponent's strategy or can assign probabilities to outcomes; it only assumes the opponent will play optimally against you. The theory is foundational to game theory and has direct application to strategy, negotiation, security, and algorithmic design.

## Core Variables and Relationships

Minimax strategy selects an action by the following logic:

1. **Strategy set S** — the set of available actions (pure or mixed).
   - Pure strategy: a single action choice.
   - Mixed strategy: a probability distribution over actions.

2. **Payoff function u(s, s*)** — the outcome I receive when I play strategy s and the opponent plays strategy s*.
   - u(s, s*) is defined for each pair of strategies.
   - A payoff is my utility; it may be money, time, goals achieved, or any comparable metric.

3. **Minimax value for a pure strategy s**:
   ```
   MM(s) = min_{s* ∈ S*} u(s, s*)
   ```
   - This is the worst-case payoff I can guarantee if I play s, assuming the opponent responds optimally against me.
   - The opponent knows my strategy and exploits it.

4. **Maximin strategy**:
   ```
   s_maximin = argmax_s [ min_{s*} u(s, s*) ]
   ```
   - The strategy that maximizes my minimum payoff.
   - This is the agent's choice.

5. **Minimax strategy (opponent's perspective)**:
   ```
   s*_minimax = argmin_{s*} [ max_s u(s, s*) ]
   ```
   - The opponent chooses the strategy that minimizes my maximum payoff.
   - By symmetry, in a zero-sum game, both players solve their maximin / minimax problem simultaneously.

6. **Nash equilibrium in zero-sum games**:
   ```
   value_of_game = max_s min_{s*} u(s, s*) = min_{s*} max_s u(s, s*)
   ```
   - At equilibrium (if mixed strategies are used), both the maximin and minimax values coincide. This is the value of the game.
   - Neither player can improve by unilateral deviation from the equilibrium strategy.

## Key Predictions

- **In a zero-sum game, playing the maximin strategy guarantees you at least the game value, no matter what the opponent does.** Conversely, the opponent cannot force you below the value if you play it. This is the fundamental security property.

- **If both players use maximin / minimax strategies, the outcome is a Nash equilibrium.** Neither player would want to deviate unilaterally because the opponent will continue to play optimally against any deviation.

- **Mixed strategies often outperform pure strategies in symmetric games.** A player who plays pure strategies is predictable and exploitable; introducing randomness (mixing) raises the guaranteed minimum payoff. Example: in Matching Pennies, both players' maximin strategy is to play each action with 50% probability, guaranteeing a payoff of 0.

- **The value of the game is the agent's security level.** In a finite, zero-sum game, the maximin value equals the minimax value (von Neumann's minimax theorem for finite games). An agent who commits to the maximin strategy is guaranteed at least this value; an agent who deviates may do worse.

- **Correlated equilibria and communication can improve outcomes.** If the game is not zero-sum (e.g., coordination games, Prisoners' Dilemma), both players might benefit from a cooperative agreement. Minimax is conservative and does not assume cooperation; it is suitable for adversarial settings.

- **In games with imperfect information, maximin strategy selection is harder but still in principle applicable.** The agent must reason about the opponent's beliefs and responses at information sets the agent cannot observe. Computational complexity grows rapidly.

## Application Procedure

Instantiate minimax / maximin against a concrete strategic decision.

1. **Define the game.** Identify the players, actions, and payoffs. Is it zero-sum or general-sum? What information is available to each player?

2. **Enumerate your strategy set S** and the opponent's strategy set S*.
   - For finite games, enumerate all pure strategies (actions).
   - For continuous games, parameterize the strategy space.

3. **Construct the payoff matrix** u(s, s*) for all pairs of strategies. Include:
   - Your payoff from each (s, s*) pair.
   - The opponent's payoff (if general-sum; for zero-sum, it is −u(s, s*)).

4. **Compute the minimax value for each of your pure strategies:**
   - For each s, find the minimum payoff: min_{s*} u(s, s*).
   - This is the worst case if you play s.

5. **Identify the maximin (safest) pure strategy:**
   - Argmax over the minimum values from step 4.
   - If a unique pure strategy has the highest minimum, play it.

6. **Check for a pure-strategy Nash equilibrium:**
   - If u(s, s*) is a Nash equilibrium (neither player wants to deviate), it is stable and often a natural focal point.
   - If no pure-strategy equilibrium exists or you are unsure of the opponent's strategy, proceed to mixed strategies.

7. **Solve for the maximin mixed strategy (if needed):**
   - Use linear programming (for 2×n or m×2 games) or support enumeration.
   - The goal is to find the probability distribution over your actions that maximizes your guaranteed minimum payoff.
   - This is computationally intensive for large games but necessary if pure strategies are exploitable.

8. **Determine the value of the game:**
   - The payoff you can guarantee by playing your maximin strategy, assuming the opponent plays optimally.

9. **Check boundary conditions** (below). If any apply, note that minimax may be too conservative or not applicable.

10. **Output the recommendation:**
    - State your maximin strategy (pure or mixed).
    - State the guaranteed value of the game.
    - Explain why this strategy is robust to opponent deviation.

## Boundary Conditions

Minimax / Maximin is a worst-case principle and breaks down or becomes misleading under several conditions:

- **The opponent is not rational or not adversarial.** Minimax assumes the opponent is intelligent and plays to minimize your payoff. If the opponent is irrational, confused, or cooperative, playing maximin may forego substantial gains. In such settings, you might want to assume a probabilistic model of opponent behavior (e.g., Bayesian game theory or behavioral models) instead.

- **You have information about the opponent's strategy or beliefs.** Minimax is a strategy that does not assume you know the opponent's move. If you do observe the opponent's action (or have beliefs about it), you should condition on that information and update your strategy, rather than play a pre-committed maximin strategy.

- **The game is not fully specified.** If payoffs are uncertain, the opponent's action set is unclear, or the rules can change, the payoff matrix is not well-defined. Minimax requires a well-defined game; in ambiguous settings, you may need to combine minimax with robustness or scenario analysis.

- **Repeated or long-horizon games with reputation.** Minimax is a single-shot principle. In repeated games, both players may cooperate (e.g., tit-for-tat) and achieve payoffs far better than the single-shot minimax value. Using minimax myopically in a repeated game can destroy mutual gains and is usually suboptimal.

- **Non-zero-sum games with potential for Pareto improvement.** In Prisoners' Dilemma or coordination games, both players' minimax strategies often lead to mutual loss. A cooperative agreement would be better for both. Minimax does not account for the possibility of communication or binding agreements; use cooperative game theory (core, Shapley value) if such agreements are possible.

- **Continuous or infinite strategy spaces with no solution.** Not all games have a well-defined minimax value (e.g., some games with no pure or mixed strategy equilibrium). In such cases, the application requires refinement (e.g., epsilon-equilibrium) or a different solution concept.

## Output Format

```
## Minimax/Maximin Analysis: <game name>

**Game:** <players, actions, payoff structure>
**Zero-sum:** yes / no
**Information structure:** <perfect / imperfect; complete / incomplete>

### Payoff matrix
| Your action | Opponent's response | Your payoff | Opponent's payoff |
|---|---|---|---|
| ... | ... | ... | ... |

### Minimax values (pure strategies)
| Your strategy | Minimum payoff | Reasoning |
|---|---|---|
| ... | ... | ... |

### Maximin strategy
- **Pure strategy:** <if applicable, which action; otherwise "none">
- **Mixed strategy:** <probability distribution over actions, if needed>
- **Value of the game:** <guaranteed payoff>

### Nash equilibrium check
- **Pure-strategy equilibrium:** <exists / does not exist; if exists, which>
- **Justification:** <why neither player deviates>

### Strategic implications
- **Why this strategy is robust:** <worst-case guarantee>
- **Vulnerabilities:** <if opponent is irrational or you have more information>

### Boundary-condition notes
<which boundary conditions apply and whether minimax is appropriate for this decision>

### Confidence: high | medium | low
<reasoning: clarity of payoff matrix + game structure + whether the opponent is truly adversarial + whether single-shot minimax is appropriate for the decision horizon>
```
