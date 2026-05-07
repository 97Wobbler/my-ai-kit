---
name: shapley-value
display_name: Shapley Value
class: model
underlying_class: native
domain: game-theory
source: Lloyd S. Shapley, "A Value for n-Person Games," Contributions to the Theory of Games II, 1953
best_for:
  - Computing fair contribution shares in cooperative settings
  - Allocating joint value among players with overlapping contributions
  - Predicting who claims credit or demands compensation in coalitions
one_liner: "Unique fair allocation of contribution in cooperative games."
---

# Shapley Value

## Overview

The Shapley Value is a solution concept in cooperative game theory that assigns each player a unique, mathematically fair share of the total value created by a coalition. Its central claim is that there exists exactly one allocation rule that satisfies four rational axioms (symmetry, dummy player, additivity, efficiency), and that rule is the Shapley Value — the average marginal contribution of each player across all possible orderings in which the coalition could form. The model is predictive: it predicts *how* value will (or should) be divided when rational agents cooperate and care about fairness. Unlike expected-utility or strategic-form models, Shapley Value is normative in spirit — it says what *ought* to happen — but it also describes what actually happens in real teams, partnerships, and open-source projects when informal haggling settles on something that *feels* fair.

## Core Variables and Relationships

The Shapley Value decomposes the allocation problem into player contributions measured against all possible coalition paths:

1. **The characteristic function v(S).** For any subset S of players, v(S) is the total value that coalition S can create *without* the others. Key drivers:
   - Value of the grand coalition: v(N), the total pie.
   - Marginal products: v(S ∪ {i}) − v(S), the incremental value player i adds to coalition S.
   - Subadditivity: whether v(S) + v(T) ≥ v(S ∪ T) (i.e., do players create more value together or apart?).

2. **Marginal contributions over orderings.** Player i's contribution depends on the *order* in which players join. If player i joins an existing coalition S (not containing i), the marginal contribution is v(S ∪ {i}) − v(S). Different orderings yield different marginal values for i.

3. **The Shapley Value for player i is:**

       Φᵢ = (1/n!) × Σ [v(S ∪ {i}) − v(S)]
       
   summed over all (n!) orderings. Equivalently, it is the *average* marginal contribution of player i across all permutations of player entry.

4. **The Efficiency axiom:** Σᵢ Φᵢ = v(N). The full pie is always exhausted; there is no surplus or deficit.

5. **Symmetry axiom:** If two players have identical marginal-contribution profiles across all coalitions, they receive identical Shapley Values.

6. **Dummy player axiom:** If player i adds zero marginal value to every coalition (v(S ∪ {i}) = v(S) for all S), then Φᵢ = 0.

7. **Additivity (linearity):** If two games are combined (summed), the Shapley Values of players in the combined game are the sums of their individual Shapley Values.

## Key Predictions

- **In a subadditive game,** each player receives their average marginal contribution, which is always ≥ their solo contribution v({i}) and ≤ the full grand coalition value v(N). Egalitarian-seeming teams often cluster around the center of this range.

- **A player with zero marginal contribution to every coalition receives exactly zero** — no "free riding" on average. This explains why a genuinely redundant team member cannot negotiate a positive share if rationality holds.

- **The Shapley Value is the unique allocation** satisfying the four axioms. Any other "fair" rule (equal split, proportional to some exogenous factor) violates at least one axiom. This uniqueness prediction explains why, when people reason carefully about fairness, they often converge on something close to marginal-contribution logic.

- **In a unanimous-win coalition (e.g., all N players must participate for any value),** all players receive v(N)/N regardless of their individual contribution profiles. The model predicts equal splits when everyone is equally indispensable.

- **In a "core" game where some coalitions are more valuable than the grand coalition,** the Shapley Value can lie *outside* the core (i.e., some players receive less than they could guarantee by leaving). The model predicts instability or dissatisfaction even though the allocation is "fair" by the axioms.

- **Computational complexity.** For large n, computing the exact Shapley Value requires exponential time (2ⁿ coalitions). The model predicts that real groups resort to approximation, sampling, or heuristics that feel like marginal contributions but are not exact.

## Application Procedure

Instantiate the model against a concrete value-sharing problem in a cooperative setting.

1. **Define the cooperation problem precisely.** Who are the players? What is the total value created? Is there a deadline, a natural dissolution point, or ongoing renewal? Write the boundary in one sentence.

2. **Establish the characteristic function v(S).** For every non-empty subset of players, estimate the value that subset could create *in isolation* (without the others). This is the critical and often contentious step:
   - If players are fungible (replaceable), v(S) is often proportional to |S|.
   - If players have complementary skills, v(S) may spike discontinuously when a critical member is added.
   - If the good is non-rival (software, knowledge), v(S) may be close to v(N) even for small S.
   - Document your v(S) estimates and their sources (contract, historical data, expert estimate).

3. **Compute or approximate the Shapley Value for each player.** For small n (≤4–5), enumerate all permutations and compute marginal contributions. For larger n, use a sampling algorithm (e.g., Monte Carlo over random orderings) or a closed-form approximation if the game has structure.

4. **Validate the allocation.** Check:
   - Does Σ Φᵢ = v(N)?
   - Are Φᵢ ≥ v({i}) for all i? (Otherwise a player has an incentive to exit.)
   - Does the ranking of Φ values match your intuition about contribution? If not, your v(S) estimates may need revision.

5. **Interpret the allocation as a claim on the actual payoff.** The Shapley Value is a recommendation, not a mechanism. Real actors may negotiate away from it, but it provides a focal point for bargaining.

6. **Check boundary conditions** (below). If any apply, note what the Shapley Value is *not* telling you and what additional analysis is needed.

## Boundary Conditions

The Shapley Value assumes full rationality, perfectly specified coalitional values, and no external constraints. It breaks down or misleads in several situations:

- **The characteristic function is unknown or contested.** The Shapley Value is only as good as the v(S) estimates. If players disagree on what value a coalition of {A, B} could create without C, the computation is garbage-in-garbage-out. In such cases, use it as a negotiation framework, not a verdict.

- **The game is not superadditive or is poorly structured.** If v(S ∪ T) < v(S) + v(T), the grand coalition is not stable and breaking apart may be Pareto-improving. The Shapley Value still divides v(N), but the prediction that players will cooperate is weakened.

- **Power, outside options, or disagreement payoffs matter.** The Shapley Value assumes coalitions form symmetrically and can enforce side payments. If one player has an outside option (walk away and get a guaranteed value), the Shapley Value may be a poor predictor of the actual agreement. Use a bargaining model (e.g., generalized Nash) alongside.

- **Asymmetric information.** If players cannot observe each other's marginal contributions and must estimate v(S), the Shapley Value becomes a target that may be systematically gamed or biased.

- **The game is dynamic or players enter/exit over time.** The Shapley Value is a snapshot for a fixed set of players. In a growing or shrinking coalition, use a dynamic variant (e.g., the "sequential Shapley Value").

- **Non-monetary outcomes or multi-dimensional value.** The Shapley Value is agnostic to the units of v(S), but if the problem involves both money, credit, autonomy, and risk, a single scalar allocation may disguise unequal treatment on the dimensions that matter most.

## Output Format

```
## Shapley Value Analysis: <cooperation problem>

**Boundary:** <players, value metric, time horizon>

### Characteristic function estimates
| Coalition S | v(S) | Reasoning |
|---|---|---|
| {1} | ... | <solo value> |
| {2} | ... | ... |
| {1,2} | ... | <joint value, assumptions> |
| ... | ... | ... |
| {1,2,...,n} | ... | <grand coalition total> |

### Marginal contributions (sample orderings)
| Ordering | Player 1 marginal | Player 2 marginal | ... |
|---|---|---|---|
| (1,2,...,n) | v({1}) | v({1,2})−v({1}) | ... |
| (2,1,...,n) | v({2,1})−v({2}) | v({2}) | ... |
| ... | ... | ... | ... |

### Shapley Value allocation
| Player | Φᵢ | % of v(N) | Validation |
|---|---|---|---|
| 1 | ... | ... | Φ₁ ≥ v({1})? |
| 2 | ... | ... | ... |
| ... | ... | ... | ... |
| Total | v(N) | 100% | ✓ |

### Interpretation
- Highest contributor: <player, reasoning>
- Lowest contributor: <player, reasoning>
- Unexpected gaps or rankings: <note any surprises and whether v(S) needs revision>

### Boundary-condition check
<which boundary conditions apply and what they imply for reliance on this allocation>

### Confidence: high | medium | low
<reasoning: certainty of characteristic function estimates + stability of v(N) + whether power/outside options threaten the allocation>
```
