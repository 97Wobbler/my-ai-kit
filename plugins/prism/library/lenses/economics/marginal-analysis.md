---
name: marginal-analysis
display_name: Marginal Analysis (MR=MC)
class: lens
underlying_class: native
domain: economics
source: Alfred Marshall (Principles of Economics, 1890); formalized in microeconomic theory
best_for:
  - Finding the profit-maximizing or cost-minimizing quantity in production, pricing, or resource allocation
  - Identifying whether a decision is efficient at the margin
  - Debugging overspending or underinvestment in a specific activity
one_liner: "Find the optimum where marginal revenue equals marginal cost."
---

# Marginal Analysis (MR=MC)

## Overview
Marginal analysis compares the cost of one additional unit against the benefit (revenue or value) of that unit. The optimal point—where Marginal Revenue equals Marginal Cost (MR=MC)—is where profit is maximized or where value per unit spent is optimized. Practitioners use this to audit whether they are producing too much, too little, or the right amount of something; it is especially useful when unit economics matter more than total sums, and when small changes in quantity can have outsized effects on profitability or efficiency.

## Analytical Procedure

### Phase 1 — Define the Decision Variable

1. **Identify the activity being optimized.** This can be:
   - Units of product manufactured and sold
   - Hours spent on a task or project
   - Dollars allocated to marketing, R&D, or headcount
   - Incremental features added to a product
   - Write down what changes (quantity) and what you are measuring (profit, revenue, cost, or user value).

2. **Identify the time horizon and scope.** Is this a single quarter, annual decision, long-term investment, or per-transaction choice? Is the scope a single product line, a customer segment, or the whole business?

3. **Confirm the cost and revenue structures are continuous or can be approximated as continuous.** If output is lumpy (e.g., hiring comes in discrete people, not fractional employees), note this and adjust step calculations accordingly. For lumpy cases, calculate MR and MC for each discrete jump.

### Phase 2 — Gather and Calculate Marginal Values

4. **List Total Revenue (TR) or Total Benefit (TB) at multiple quantity levels.** Collect actual data or estimates for at least 5 points:
   - Quantity: 0, Q1, Q2, Q3, ..., Qmax
   - Corresponding TR or TB at each level
   - Example: if selling widgets, TR = Price × Quantity at each volume (accounting for volume discounts if they apply)

5. **Calculate Marginal Revenue (MR) for each step.** 
   - MR = ΔTR / ΔQ (change in total revenue divided by change in quantity)
   - Record MR between each pair of quantity levels
   - Example: if TR goes from $100 to $150 when quantity rises from 10 to 11 units, MR = $50 for the 11th unit

6. **List Total Cost (TC) at the same quantity levels.**
   - Include all relevant costs: fixed costs (if variable by decision), direct variable costs (materials, labor, energy), and allocated overhead (if it changes with quantity)
   - Do not include sunk costs (already spent, unchangeable by this decision)

7. **Calculate Marginal Cost (MC) for each step.**
   - MC = ΔTC / ΔQ (change in total cost divided by change in quantity)
   - Record MC between each pair of quantity levels
   - Example: if TC goes from $60 to $75 when quantity rises from 10 to 11 units, MC = $15 for the 11th unit

### Phase 3 — Find the Optimum

8. **Locate the quantity where MR ≈ MC.**
   - Plot MR and MC against quantity (or make a table)
   - Find the point where they are closest or where MR first becomes less than MC
   - If no exact intersection exists in your data, use linear interpolation between the nearest two points to estimate the optimal Q

9. **If MR and MC curves are smooth or you have a formula, solve MR = MC algebraically.**
   - Example: if TR = 100Q − 2Q² and TC = 10Q + 0.5Q², then MR = 100 − 4Q and MC = 10 + Q. Setting 100 − 4Q = 10 + Q gives Q = 18.

10. **Record the optimal quantity, the MR and MC values at that point, and the resulting profit or margin.**

### Phase 4 — Stress-Test the Optimum

11. **Check sensitivity to assumptions.**
    - How does the optimal Q change if price drops 10%? (This shifts MR down; optimal Q may rise or fall depending on elasticity)
    - How does it change if variable costs rise 10%? (This shifts MC up; optimal Q falls)
    - How does it change if fixed costs rise? (Should not affect optimal Q, only the profit level; if your answer changes, you included a fixed cost as variable)

12. **Verify that total profit is indeed higher at the MR=MC quantity than at neighboring quantities.**
    - Calculate Profit = TR − TC at Q_optimal, Q_optimal − 1, and Q_optimal + 1
    - Profit should be highest (or tied) at Q_optimal

13. **Check for other constraints.** Does capacity, demand ceiling, or regulatory limit prevent you from producing at the MR=MC quantity? If yes, the constrained quantity is optimal for the real world, even if it's not where MR=MC.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Decision variable (what quantity?) is defined in concrete terms | Y/N |
| TR (or TB) and TC data cover at least 5 quantity levels | Y/N |
| MR and MC are calculated for each step; values are not just stated | Y/N |
| MR=MC point is identified and the optimal quantity is explicitly stated | Y/N |
| Profit (or benefit) is verified to be highest at the MR=MC quantity | Y/N |
| Sensitivity check shows how optimal Q responds to a 10% price or cost change | Y/N |
| External constraints (capacity, demand, regulation) are listed and acknowledged | Y/N |

## Red Flags

- MR and MC are never equal or close. This suggests either the decision boundary has not been reached (you are only exploring a narrow range) or the cost/benefit structure is fundamentally non-standard (e.g., network effects, monopolistic pricing). Widen your quantity range or reconsider whether MR=MC applies.
- The optimal quantity is at the boundary of your data (the maximum or minimum quantity you examined). This is usually a sign you need to expand your range.
- Profit at Q_optimal is lower than at a neighboring quantity. This indicates a calculation error; recompute TR, TC, MR, and MC.
- No sensitivity analysis. The MR=MC point is mathematically elegant but fragile; claiming it without testing how it moves under realistic cost or price changes is premature.
- Fixed costs are included in the marginal cost calculation. Marginal cost should reflect only the incremental cost of one additional unit; fixed costs do not change with quantity and should not affect the MR=MC optimum.
- The optimal Q is stated as a number but there is no statement of what MR and MC are at that point. Without these values, there is no proof that MR=MC.

## Output Format

```
## Marginal Analysis Assessment

**Decision variable:**
<What quantity is being optimized? (e.g., units produced, hours allocated, dollars spent)>

**Cost and revenue structure:**
<Brief description of how price/value and cost per unit change with quantity.>

### Phase 2 — MR and MC Calculation

| Quantity | Total Revenue (or Benefit) | Marginal Revenue | Total Cost | Marginal Cost |
|---|---|---|---|---|
| 0 | <...> | — | <...> | — |
| <Q1> | <...> | <...> | <...> | <...> |
| <Q2> | <...> | <...> | <...> | <...> |
| ... | ... | ... | ... | ... |

### Phase 3 — Optimal Quantity

**MR=MC intersection:**
- Optimal quantity: <number> units (or at value <constraint if binding>)
- MR at optimal Q: <value>
- MC at optimal Q: <value>
- Total Revenue at optimal Q: <value>
- Total Cost at optimal Q: <value>
- **Profit (or net benefit) at optimal Q: <value>**

**Verification:**
Profit at Q−1: <value> | Profit at Q: <value> | Profit at Q+1: <value>
→ Confirms maximum at Q_optimal: Y/N

### Phase 4 — Sensitivity

| Scenario | New Optimal Q | New Profit | Notes |
|---|---|---|---|
| Price down 10% | <...> | <...> | <...> |
| Variable cost up 10% | <...> | <...> | <...> |
| <other scenario> | <...> | <...> | <...> |

### Constraints & Real-World Conditions

<List any capacity, demand, regulatory, or organizational limits that might prevent production/allocation at the MR=MC quantity. If the true optimal is constrained, state the constraint and the resulting quantity.>

### Confidence
<high | medium | low> — <Justification: data quality, assumption stability, proximity of MR to MC, sensitivity results>
```
