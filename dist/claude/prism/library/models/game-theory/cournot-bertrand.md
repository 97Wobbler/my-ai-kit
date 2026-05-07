---
name: cournot-bertrand
display_name: Cournot vs. Bertrand Competition
class: model
underlying_class: native
domain: game-theory
source: Antoine Augustin Cournot, Researches into the Mathematical Principles of the Theory of Wealth, 1838; Joseph Bertrand, review in Journal des Savants, 1883
best_for:
  - Predicting equilibrium price and quantity in duopoly when firms choose different strategic variables
  - Explaining why the same market structure can yield vastly different outcomes depending on whether competition is quantity-based or price-based
  - Identifying which competitive mode (Cournot or Bertrand) better describes an industry
one_liner: "Market outcomes differ depending on whether firms compete on quantity or price."
---

# Cournot vs. Bertrand Competition

## Overview

The Cournot-Bertrand framework explains how the *choice of strategic variable* — whether firms compete on quantity or price — determines the equilibrium price, quantity, and profit in oligopolistic markets. Both models assume rational, simultaneous-move competition with full information, but they yield dramatically different predictions: Cournot equilibrium produces positive profits and outcomes between monopoly and perfect competition; Bertrand equilibrium (with homogeneous products) collapses to marginal-cost pricing and zero economic profit, approaching the competitive extreme. The framework is predictive: it does not explain *why* firms choose one variable over another, but rather predicts what equilibrium will obtain once the choice is locked in. Applying the model requires identifying which assumption (quantity or price setting) better matches the industry's institutional structure.

## Core Variables and Relationships

**Two competing assumptions about firm behavior:**

1. **Cournot competition (quantity-setting).**
   - Each firm chooses a quantity q_i to maximize profit given the (fixed) quantities of competitors.
   - Inverse market demand is P = a − b(Q), where Q = Σq_i.
   - Each firm solves: max π_i = [a − b(Q)] · q_i − c · q_i, taking Q_−i as given.
   - Equilibrium condition: firms set quantity such that marginal revenue equals marginal cost.
   - **Key outcome:** equilibrium price P* > marginal cost c (positive markup).
   - **Profit per firm:** π_i = [(P* − c) / b] · (a − c) / (n + 1)², where n is the number of firms.

2. **Bertrand competition (price-setting).**
   - Each firm chooses a price p_i to maximize profit given the (fixed) prices of competitors.
   - Demand faced by firm i is perfectly elastic at prices below competitors' prices; zero if its price exceeds theirs.
   - Each firm solves: max π_i = [p_i − c] · D(p_i), taking p_−i as given.
   - Equilibrium condition: firms undercut each other until price equals marginal cost.
   - **Key outcome:** equilibrium price P* = c (zero markup).
   - **Profit per firm:** π_i ≈ 0 (in the limit of identical products and no capacity constraints).

**The Bertrand Paradox:** With only two firms, homogeneous products, and no capacity or product-differentiation constraints, Bertrand competition converges instantly to P = c. Cournot with the same parameters yields P > c. This is the core tension: identical market structure, different strategic variables, vastly different outcomes.

**Key relationship:**
- As the number of firms n → ∞ in Cournot, price → c and Cournot converges to Bertrand.
- With differentiated products, Bertrand equilibrium supports P > c and positive profits (firms no longer have incentive to undercut on identical goods).
- With capacity constraints or strategic commitments, Bertrand outcomes shift toward Cournot (a firm cannot undercut below its capacity).

## Key Predictions

- **Duopoly with homogeneous products under Bertrand:** Price immediately drops to marginal cost, rendering the firm unable to cover fixed costs. The market becomes unstable or a firm exits. In Cournot duopoly with the same cost, price remains well above c and both firms earn positive profit.

- **Quantity commitments (e.g., via capacity investment or production lead time) favor Cournot outcomes.** When firms must set quantity first (e.g., manufacturing capacity booked in advance), or when production cannot be instantly scaled, Cournot is the operative model and price remains above marginal cost.

- **Price-setting with differentiated products softens the Bertrand collapse.** If products are substitutable but not perfect substitutes (differentiation via brand, location, features, or switching costs), Bertrand yields P > c. The degree of differentiation determines the markup; the more differentiated, the higher the price and profit.

- **Markets that appear "Cournot" (P > c with limited firms) may be Bertrand with high product differentiation, switching costs, or capacity constraints, not because firms are "cooperating" but because the strategic environment naturally selects for those constraints.

- **In Bertrand with limited capacity, a firm with 60% of total capacity can exercise Cournot-like power.** Capacity constraints convert the equilibrium toward quantity-setting, preventing full undercutting.

- **Industries with short production cycles and frequent price revision (e.g., e-commerce, commodities with daily auctions) exhibit Bertrand-like dynamics. Industries with long lead times, upfront capacity investment, or infrequent repricing (e.g., utilities, contract manufacturing) exhibit Cournot-like outcomes.**

## Application Procedure

Instantiate the framework against a specific oligopolistic industry or market.

1. **Define the industry boundary precisely.** What is the product or service? What is the geographic scope? Who are the main competitors, and how many? Write the boundary in one sentence.

2. **Identify the primary strategic variable.** Do firms compete by announcing a price and letting quantity adjust to demand? Or do they commit to a quantity (capacity, production run, inventory) and let price adjust to clear the market?
   - Price-setting cues: prices are posted, advertised, or negotiated frequently; production can scale rapidly in response to demand; customers can easily switch based on price.
   - Quantity-setting cues: capacity or production runs are decided in advance (e.g., seasonal, contractual, or investment-heavy); short-run supply is inelastic; price fluctuates with demand.

3. **Assess product homogeneity.** Are products perfect substitutes or differentiated (via brand, location, features, quality, switching costs)?
   - Perfect substitutes → expect Bertrand collapse (P → c) unless capacity or other constraints intervene.
   - Differentiated → Bertrand yields P > c; degree of differentiation sets the markup.

4. **Check for capacity or commitment constraints.** 
   - Do firms have inelastic short-run capacity?
   - Is there a time lag between the competitive move (price or quantity) and the response?
   - If yes, the effective model shifts toward Cournot even if firms nominally post prices.

5. **Identify the cost structure.**
   - If marginal cost c is near zero and fixed costs are high, even Cournot equilibrium may not cover fixed costs; a firm may need to exit.
   - If c is high relative to demand, P > c slack is more pronounced.

6. **Compute or bound the equilibrium.**
   - If quantity-setting (Cournot): equilibrium price P* = a − b · (n+1)(a−c) / [(n+1)² · b], where n is the number of firms. Profit per firm declines as n grows.
   - If price-setting with homogeneous products (Bertrand): P* = c (approximately), π ≈ 0.
   - If price-setting with differentiation: P* lies between c and the monopoly price; use elasticity of substitution or discrete-choice models to refine.

7. **Check boundary conditions** (below). Note any that apply.

8. **Generate the prediction.**
   - What is the expected equilibrium price, quantity, and profit per firm?
   - How would profit change if the strategic variable shifted (quantity → price, or vice versa)?
   - What market structure would emerge if firms could endogenously choose their strategic variable?

## Boundary Conditions

The Cournot-Bertrand framework assumes rational, simultaneous-move competition with symmetric information and homogeneous (or exogenously differentiated) products. It breaks down or becomes incomplete when:

- **Products are endogenously differentiated through R&D or advertising.** If firms invest in product differentiation as part of the game, the model no longer predicts equilibrium — you need a three-stage game (invest in differentiation, then compete in price or quantity). Differentiation itself becomes endogenous.

- **Firms move sequentially, not simultaneously (Stackelberg leadership).** If one firm commits to quantity first and others respond, the equilibrium is not Cournot or Bertrand but Stackelberg. The leader earns a first-mover advantage.

- **Entry and exit are free and rapid.** Cournot and Bertrand assume n is fixed. In a contestable market, free entry drives profit to zero regardless of the strategic variable (approaching Bertrand outcomes in price, Cournot quantity levels but zero economic profit). Use a contestable-markets framework instead.

- **Collusion or repeated interaction (infinitely repeated game).** The model predicts one-shot equilibrium. If firms meet repeatedly, they can sustain cooperative outcomes (higher price, lower quantity) via trigger strategies. Use a repeated-games or cartel-stability framework.

- **Demand is stochastic or firms have private information about costs or demand.** The model assumes perfect information. Under uncertainty, Cournot and Bertrand may give different average outcomes, and behavior shifts toward Bayesian equilibrium. The impact of information asymmetry can be large.

- **Capacity constraints are asymmetric or so tight that they bind at very different quantities across firms.** The model assumes capacity is either non-binding (Cournot or Bertrand apply cleanly) or homogeneous. Extreme asymmetry in capacity may require case-by-case analysis.

## Output Format

```
## Cournot vs. Bertrand Analysis: <industry name>

**Boundary:** <one-sentence scope: product, geography, main competitors>
**Time snapshot:** <date>
**Strategic variable:** Cournot (quantity) | Bertrand (price) | [Mixed or uncertain]

### Market structure
| Firm | Market share | Capacity / Commitment |
|---|---|---|
| ... | ... | ... |

### Product differentiation
- Homogeneity / substitutability: <high / moderate / low>
- Switching costs: <high / low>
- Key differentiation levers: <brand, location, features, other>

### Equilibrium prediction

**Assumed model:** Cournot | Bertrand | [Hybrid]

- Equilibrium price P*: <point estimate or range, vs. marginal cost c>
- Equilibrium quantity Q*: <point estimate or range per firm>
- Economic profit per firm: <positive / zero / negative, with magnitude if possible>
- Consumer surplus / allocative efficiency: <relative to monopoly and perfect competition>

### Sensitivity analysis
- If product differentiation increases: <price, profit, quantity direction>
- If the number of firms increases: <price, profit, quantity direction>
- If strategic variable shifts (Cournot ↔ Bertrand): <magnitude of change in P, Q, π>

### Endogenous variable that would move equilibrium
<which single factor (capacity, differentiation, entry barriers) would most shift P or π if relaxed>

### Boundary-condition notes
<which of the six boundary conditions apply; whether the prediction is still robust; what complementary analysis is needed>

### Confidence: high | medium | low
<reasoning: clarity of strategic variable + product homogeneity + stability of market structure + boundary-condition fit>
```
