---
name: heijunka
display_name: Heijunka
class: heuristic
underlying_class: native
domain: manufacturing
source: Toyota Production System, origin uncertain
best_for:
  - production scheduling
  - demand variability
  - capacity planning
one_liner: "Level production by spreading demand fluctuations across time to balance equipment and labor load."
---

# Heijunka

## The Rule
Distribute variable demand evenly across time intervals rather than batching orders, so that capacity, inventory, and staffing remain stable and predictable.

## When It Applies
- A production line receives large orders in irregular clusters, leaving long idle periods punctuated by overtime spikes.
- Demand forecasts show wide seasonal swings, and you're choosing between pre-building inventory or tolerating late delivery.
- Multiple product variants share the same equipment, and changeover costs or setup times are significant.
- Workforce staffing is inflexible (hiring/firing is slow), but the workload fluctuates month-to-month by 30%+ of capacity.

## When It Misleads
- The products are genuinely made to order with customer deadlines that won't tolerate delay. Leveling demand across time directly conflicts with promised delivery windows.
- Setup and changeover costs are so high that batching large runs is cheaper than the inventory carrying cost of intermediate stock. Heijunka assumes the marginal cost of switching is low relative to the cost of idle capacity and working-capital tie-up.
- Demand is already stable and evenly distributed — the heuristic adds process overhead with no benefit.
- A single customer accounts for 80%+ of volume and their orders are non-negotiable. Heijunka works best with many small customers whose demands can be aggregated and smoothed.

## Common Misuse
Confusing "level the demand" with "ignore the demand." Heijunka is not about denying customer requests; it is about negotiating pull-based scheduling with customers so that small orders arrive steadily rather than a few massive lumpy batches. Without customer buy-in or a market where you control the schedule (e.g., retail replenishment), the heuristic becomes a justification for poor responsiveness.

Applying heijunka without first eliminating large fixed changeover costs is expensive — you level demand but end up holding more inventory than you save in capacity smoothing. The heuristic assumes that switching between products is cheap (quick, automated, or both).

## How Agents Use It
- **Embedded**: in production-design or capacity-planning lenses, as a check step after demand forecasts are built. Ask: "Is the demand pattern already roughly level across our time intervals, or would distributing it improve utilization?"
- **Sanity-gate**: when a plan proposes large inventory build or overtime to handle demand peaks, ask whether the underlying demand distribution could be leveled through schedule negotiation or pull-based replenishment, reducing the need for both.
