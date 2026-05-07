---
name: stackelberg
display_name: Stackelberg Competition
class: model
underlying_class: native
domain: game-theory
source: Heinrich von Stackelberg, "Marktform und Gleichgewicht," 1934; formalized in modern game theory by Tirole (1988) and others
best_for:
  - Predicting equilibrium output and prices when one firm moves first (leader) and others respond (followers)
  - Explaining why first-mover advantage in quantity-setting competition yields higher profit than Cournot equilibrium
one_liner: "Sequential-game equilibrium where a leader sets quantity first and the follower responds."
---

# Stackelberg Competition

## Overview

The Stackelberg model is a sequential-move game in which one firm (the
leader) chooses its output (or price) first, and one or more other firms
(followers) observe the leader's choice and then optimize their own
response. Unlike simultaneous-move Cournot competition, the leader has a
first-mover advantage: by committing to a quantity, it shapes the
follower's best-response function and thereby captures a larger share of
the market and higher profit. The model is predictive — it specifies the
equilibrium path and the payoffs to both leader and follower under the
assumption that each firm correctly anticipates the other's moves. It
explains why moving first in quantity-setting competition is strategically
valuable, and how that advantage erodes or reverses under different
information or commitment structures.

## Core Variables and Relationships

**Key variables:**

1. **Leader's output q_L** — chosen first, without knowing the follower's
   choice but knowing the follower will respond optimally to q_L.

2. **Follower's output q_F** — chosen after observing q_L. The follower
   maximizes its own profit given q_L; this is the best-response function
   q_F(q_L), which the leader anticipates.

3. **Market price P** — typically a downward-sloping demand curve
   P(Q) = P(q_L + q_F). In the linear case, P = a − b(q_L + q_F).

4. **Profit for leader** — π_L = P(q_L + q_F) · q_L − C_L(q_L), where
   the leader *knows* that q_F will equal the follower's best response to q_L.

5. **Profit for follower** — π_F = P(q_L + q_F) · q_F − C_F(q_F), where
   the follower chooses q_F to maximize this, taking q_L as given.

6. **Cost structures C_L, C_F** — typically constant marginal cost
   (c_L, c_F per unit). Identical costs are common in benchmark models.

**Relationships and solution method:**

The equilibrium is solved by **backward induction**:

- Step 1: Write the follower's profit-maximization problem as a function
  of q_L. Solve for q_F(q_L), the best-response function.
- Step 2: Substitute q_F(q_L) into the leader's profit function. The
  leader now chooses q_L knowing that output will expand by q_F(q_L) in
  response.
- Step 3: The leader maximizes π_L = P(q_L + q_F(q_L)) · q_L − C_L(q_L)
  with respect to q_L.

In the linear-demand, constant-cost benchmark (P = a − b(q_L + q_F),
marginal costs c_L = c_F = c):

- Follower best-response: q_F(q_L) = (a − c − b·q_L) / (2b)
- Leader chooses: q_L = (a − c) / (2b), so q_F = (a − c) / (4b)
- Equilibrium total quantity: Q* = (3/4)·(a − c) / b
- Equilibrium price: P* = a − (3/4)(a − c) = (1/4)a + (3/4)c
- Leader profit: π_L* = [(a − c) / (2b)] · [(a − c) / (4b)]
  = (a − c)² / (8b)
- Follower profit: π_F* = [(a − c) / (4b)]² = (a − c)² / (16b)

The leader earns exactly **twice** the profit of the follower, despite
identical costs and demand structure.

## Key Predictions

- **First-mover advantage in output.** The leader produces twice the
  output of the follower (q_L = 2·q_F in the symmetric-cost linear case)
  and captures twice the profit, not because of technological superiority
  but purely because of timing.

- **Stackelberg outcome lies between Monopoly and Cournot.** Total output
  is higher than monopoly (which would maximize joint profit) but lower
  than simultaneous-move Cournot (in which neither firm accounts for the
  other's quantity change). Price is higher than Cournot, lower than
  monopoly.

- **The follower's output is a decreasing function of the leader's
  output.** If the leader expands q_L, the follower shrinks q_F because
  the follower's best response to a larger market supply is to produce
  less. This is the **demand-reduction effect**.

- **Capacity commitment and credibility determine advantage.** The leader's
  profit advantage exists *only if* the follower believes the leader's
  output is fixed (i.e., will not be reduced if the follower produces
  more). If the follower believes the leader will match the follower's
  output or respond aggressively, the advantage disappears.

- **Asymmetric costs flip advantage conditionally.** If the follower has
  lower cost (c_F < c_L), the follower's best response is to produce
  more despite being second-mover. In the limit, the low-cost follower
  can produce more than the high-cost leader, though the leader still
  earns higher profit because it moves first. **However**, if the
  cost gap is large enough, the advantage reverses and the follower
  earns more. The relative cost and the demand curve determine the
  outcome.

- **Welfare and surplus allocation.** Consumer surplus is lower in
  Stackelberg than in Cournot (price is higher). The leader captures
  more of the economic surplus because it moves first.

## Application Procedure

Apply the Stackelberg model to a duopoly (or oligopoly with one dominant
leader) in which one firm commits to a quantity and the other firm(s)
respond.

1. **Identify the leader and follower.** Who moves first? Who has observed
   the leader's choice and can respond? For this to apply, the first mover
   must be visibly committed to its output (e.g., capacity is fixed, or
   the firm has announced production publicly and reversing is costly).

2. **Write the demand curve.** P = P(Q) = P(q_L + q_F). In linear form,
   P = a − b(q_L + q_F), or equivalently Q = (a − P) / b. Specify a and b.

3. **Write the cost structure.** Specify marginal costs c_L and c_F
   (or total cost functions if nonlinear). Assume constant marginal cost
   if no information is given.

4. **Derive the follower's best-response function** q_F(q_L).
   - Set ∂π_F / ∂q_F = 0: P'(Q)·q_F + P(Q) − c_F = 0, where
     Q = q_L + q_F.
   - Solve for q_F as a function of q_L.

5. **Solve for the leader's optimal output.** Substitute q_F(q_L) into
   π_L and maximize:
   - π_L = P(q_L + q_F(q_L))·q_L − C_L(q_L)
   - Set ∂π_L / ∂q_L = 0 and solve for q_L*.

6. **Compute equilibrium quantities, price, and profits.**
   - q_L*, q_F* = q_F(q_L*), Q* = q_L* + q_F*, P* = P(Q*).
   - π_L* = P*·q_L* − C_L(q_L*), π_F* = P*·q_F* − C_F(q_F*).

7. **Compare to alternatives** (monopoly, Cournot, perfect competition) to
   contextualize the result.

8. **Check boundary conditions** below. If any apply, note that the
   Stackelberg prediction may not hold.

## Boundary Conditions

The Stackelberg model assumes commitment and perfect observability. It
breaks down or becomes partial under:

- **No commitment / reversibility.** If the leader can easily change its
  output after observing the follower's response, the model collapses into
  a **simultaneous-move Cournot game**. The first-mover advantage vanishes
  because the follower knows the leader can retaliate or accommodate. This
  is empirically common: firms often adjust production mid-period.

- **Price competition instead of quantity competition.** Under Bertrand
  pricing (firms set price, not quantity), the leader's first-mover
  advantage is small or reversed — the follower can often undercut the
  leader's price and capture market share. Stackelberg's logic applies to
  quantity-setting; price-setting requires Bertrand or price-leadership
  models instead.

- **More than two firms (complex follower best-response).** With n > 2
  firms, the follower's optimization is more complex. If all followers
  move simultaneously after the leader, the follower's best response is to
  the leader's choice, but followers may also compete with each other.
  Multiple-follower Stackelberg (leader-follower(s) with followers also
  competing) requires explicit modeling of the follower equilibrium.

- **Incomplete or asymmetric information about costs or demand.** If the
  follower does not know the leader's cost or the true demand curve, the
  follower cannot compute the correct best response. The equilibrium shifts
  to a signaling or inference game, and Stackelberg's closed-form solution
  no longer applies.

- **Repeated interaction or dynamic settings.** If firms compete multiple
  times, trigger strategies and reputation effects can sustain collusive
  or alternative equilibria. Stackelberg applies to a static, one-shot
  game; dynamic games require multi-period analysis.

- **Capacity constraints or decreasing returns at scale.** If the leader
  hits a capacity ceiling or faces sharply increasing marginal cost, the
  best-response function changes shape, and the solution can flip. The
  model assumes smooth, continuous optimization.

## Output Format

```
## Stackelberg Equilibrium Analysis: <industry or firms>

**Market structure:** Duopoly (leader + follower) | Oligopoly with leader
**Leader:** <firm name / description>
**Follower(s):** <firm name / description>
**Commitment assumption:** <how is the leader's output locked in? capacity? public announcement? other>

### Demand and cost parameters
| Parameter | Value | Source / notes |
|---|---|---|
| Demand intercept (a) | ... | ... |
| Demand slope (b) | ... | ... |
| Leader marginal cost (c_L) | ... | ... |
| Follower marginal cost (c_F) | ... | ... |

### Best-response function
Follower: q_F(q_L) = <formula or qualitative description>

### Equilibrium outcome
| Variable | Value | Notes |
|---|---|---|
| Leader output (q_L*) | ... | ... |
| Follower output (q_F*) | ... | ... |
| Total output (Q*) | ... | ... |
| Equilibrium price (P*) | ... | ... |
| Leader profit (π_L*) | ... | ... |
| Follower profit (π_F*) | ... | ... |

### Comparison to alternatives
| Benchmark | Total Q | Price | Leader Π | Follower Π |
|---|---|---|---|---|
| Stackelberg | ... | ... | ... | ... |
| Cournot (simultaneous) | ... | ... | ... | ... |
| Monopoly | ... | ... | ... | ... |

### First-mover advantage assessment
- Profit ratio (π_L* / π_F*): <X:1>
- Plausible? <is the commitment credible; are assumptions met>

### Boundary-condition check
<which conditions apply and whether they undermine the Stackelberg prediction>

### Confidence: high | medium | low
<reasoning: commitment credibility + cost/demand data quality + whether
competition is quantity-based (not price-based) + whether the market is
static (not dynamic)>
```
