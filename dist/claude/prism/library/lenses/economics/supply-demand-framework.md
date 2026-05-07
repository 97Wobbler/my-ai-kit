---
name: supply-demand-framework
display_name: Supply-Demand Framework
class: lens
underlying_class: native
domain: economics
source: Adam Smith (The Wealth of Nations, 1776); formalized by Alfred Marshall (Principles of Economics, 1890)
best_for:
  - Diagnosing price instability and allocation inefficiency in markets
  - Identifying whether a shortage or surplus is demand-driven or supply-driven
  - Predicting the direction and magnitude of price movement when conditions shift
one_liner: "Diagnose imbalances via price signals and analyze rebalancing mechanisms."
---

# Supply-Demand Framework

## Overview
The Supply-Demand Framework maps the relationship between the quantity of a good available (supply), the quantity buyers want at each price (demand), and the equilibrium price where the two match. When supply or demand shifts, price moves to clear the market — a signal that something in the system has changed. Practitioners use this to diagnose why prices are rising or falling, to predict where they're headed, and to identify whether a shortage or glut is temporary (price will correct it) or structural (requires policy or supply-side intervention). The framework is mechanical, not predictive of human behavior; it is most reliable when applied to standardized goods with many buyers and sellers, and least reliable when applied to unique assets or thin markets.

## Analytical Procedure

### Phase 1 — Establish the market boundary

1. **Define the good or service precisely.** What is being traded? Write a one-sentence definition that distinguishes this good from close substitutes (e.g., "whole milk in the US grocery market" not "dairy products globally").

2. **Define the time frame.** Are you analyzing the current quarter, next 12 months, or a specific event (e.g., the 2022 fertilizer shortage)? Supply and demand operate on different cycles; wheat equilibrium resolves in weeks, real estate in months or years.

3. **Identify the relevant buyer segment.** Who is the primary demander? End consumers, businesses, government, or a mix? If heterogeneous (e.g., wealthy and poor), note it — they respond differently to price changes.

4. **Identify the relevant supplier segment.** Who supplies this good? One dominant producer, many small producers, imports? Are suppliers price-takers or price-setters? Is entry/exit easy or slow?

### Phase 2 — Map current supply and demand

5. **Estimate current supply.** How much of this good is currently available at the current price? Look for:
   - Production data (units per year, or revenue divided by price)
   - Inventory levels (finished goods, work in progress)
   - Import/export data if relevant
   - Capacity utilization (are suppliers running flat out, or is there slack?)
   Do not assume current supply equals current production — inventory and trade matter.

6. **Estimate current demand.** How much is currently being purchased at the current price? Look for:
   - Sales data (units sold, or revenue divided by price)
   - Market research or usage surveys
   - Comparable markets (if direct data is unavailable)
   - Leading indicators of demand (e.g., housing starts precede lumber demand)
   Be explicit about whether demand is growing, stable, or shrinking.

7. **Assess price elasticity of demand.** How sensitive are buyers to price changes? Ask:
   - If price rises 10%, does quantity demanded fall 5% (inelastic), 10% (unit elastic), or 20% (elastic)?
   - Are there close substitutes? (substitutes → elastic demand)
   - Is this a necessity or a luxury? (necessity → inelastic)
   - What share of buyer budgets does this good consume? (small share → inelastic)
   Quantify if possible; if not, rank as "high, medium, or low" elasticity.

8. **Assess price elasticity of supply.** How quickly can suppliers increase or decrease output?
   - If price rises 10%, can suppliers increase output 5%, 10%, or 20%?
   - Are inputs (raw materials, labor, capital) readily available at current prices?
   - Are there production bottlenecks or capacity constraints?
   - How long does it take to add capacity (weeks, months, years)?
   Supply is more elastic in the long run (more time to adjust) than the short run (capacity fixed).

### Phase 3 — Detect imbalance

9. **Compare supply to demand at the current price.** Is quantity supplied approximately equal to quantity demanded?
   - If Supply > Demand: there is excess inventory, buyers have choice, prices face downward pressure.
   - If Supply < Demand: there is a shortage, buyers compete, prices face upward pressure.
   - If Supply ≈ Demand: the market is approximately in equilibrium.
   This step is diagnostic; do not yet explain why the imbalance exists.

10. **Rule out measurement error.** Could the apparent imbalance be an artifact of bad data? Check:
    - Are supply and demand measured in the same units? (e.g., both in kilograms, not kilograms vs. pounds)
    - Do the time periods match? (e.g., both measured in the last 30 days, not one in Q1 and one projected for Q2)
    - Are you comparing retail demand to wholesale supply, or similar mismatches?
    If measurement error is likely, re-estimate with better data before proceeding.

### Phase 4 — Diagnose the source of imbalance

11. **Identify recent shifts in supply or demand.** What has changed in the last 3–12 months?
    - Demand shifts: income changes, preference shifts, population growth, new use cases, substitute goods becoming cheaper/unavailable.
    - Supply shifts: input costs (labor, materials, energy), technology changes, weather (agricultural goods), policy/tariffs, producer entry/exit, capacity changes.
    List each shift and mark it as D (demand-side) or S (supply-side).

12. **For each shift, estimate its magnitude.** Did it move supply or demand by 1%, 5%, 10%, or more?
    - Small shifts (< 3%) often go unnoticed and prices adjust slowly.
    - Large shifts (> 10%) trigger rapid price movement and market attention.
    - Use comparable historical events or sensitivity analysis if direct data is unavailable.

13. **Determine whether the imbalance is acute or chronic.** 
    - Acute: caused by a recent, time-limited shock (weather, port closure, policy change) that will likely reverse in weeks to months.
    - Chronic: rooted in structural factors (population growth, resource depletion, sustained cost inflation) that will persist or worsen.
    Acute imbalances resolve via price movement. Chronic imbalances may trigger supply-side or policy intervention.

### Phase 5 — Project the rebalancing mechanism

14. **Project how price will move.** Given the current imbalance and elasticities:
    - If demand > supply and demand is inelastic, expect large price increases.
    - If demand > supply and demand is elastic, expect moderate price increases (because higher prices will suppress demand).
    - If supply > demand and supply is elastic, expect price to fall steeply (suppliers quickly cut output).
    - If supply > demand and supply is inelastic, expect prices to fall gradually (suppliers absorb losses, maintain output).

15. **Identify non-price adjustment mechanisms.** Not all rebalancing happens through price. Look for:
    - Rationing or allocation (e.g., semiconductors allocated to key customers instead of auctioned)
    - Long-term contracts that lock in price (insulating the market from short-term swings)
    - Waiting lists or backlogs (price signals delayed because inventory is zero).
    - Regulatory caps or floors on price (preventing price discovery).
    If these are present, price may not move even if imbalance exists — the imbalance persists in non-price form (shortages, surpluses of inventory).

16. **Estimate the time to rebalance.** How long until supply and demand re-equilibrate?
    - Agricultural goods: weeks to months (supply adjusts slowly; demand elastic).
    - Manufactured goods: months to 2 years (capacity takes time to add).
    - Real estate: 2–5 years (supply very inelastic short-term; demand cyclical).
    - Commodities with storage: varies; storage costs create a ceiling on price appreciation.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Market boundary (good, time frame, buyer/seller segments) explicitly defined | Y/N |
| Current supply and demand both estimated (not assumed equal) | Y/N |
| Price elasticity of demand assessed and justified | Y/N |
| Price elasticity of supply assessed and justified | Y/N |
| Imbalance (supply vs. demand at current price) clearly stated | Y/N |
| At least one recent shift in supply or demand identified | Y/N |
| Shift magnitude estimated (% change, not vague) | Y/N |
| Rebalancing mechanism described (price move, rationing, or persistence) | Y/N |
| Rebalancing timeline estimated | Y/N |

## Red Flags

- Supply and demand are assumed equal without checking. If current prices haven't changed, supply may equal demand, but if they have, you must verify the imbalance yourself.
- Elasticity is assessed as "high" or "low" with no supporting reasoning. Cite substitutes, budget share, or historical price-quantity data.
- The imbalance is diagnosed but no shift is identified. If quantity supplied ≠ quantity demanded, *something* must have changed. If you cannot name it, re-examine your supply and demand estimates.
- Rebalancing time is guessed. Anchor to comparable past events or supply/demand cycle times for the industry.
- The analysis assumes prices are free to move. If there are price controls, rationing, or long-term contracts, state this explicitly — the framework still applies, but the imbalance will manifest in non-price form (shortages, inventory, waiting lists).
- Substitutes or close alternatives are ignored. If price rises enough, buyers switch to alternatives; this limits how high price can go and makes demand more elastic than it appears at current prices.

## Output Format

```
## Supply-Demand Analysis

**Market Definition:**
- Good: <...>
- Time frame: <...>
- Primary buyers: <...>
- Primary suppliers: <...>

### Current State
- Current supply (units/period): <...>
- Current demand (units/period): <...>
- Current price: <...>
- Imbalance: Supply [ > | < | ≈ ] Demand by <...%>

### Elasticity Assessment
- Price elasticity of demand: <high/medium/low> — <justification>
- Price elasticity of supply: <high/medium/low> — <justification>

### Recent Shifts
| Shift | Type (D/S) | Magnitude | Evidence |
|---|---|---|---|
| <e.g., labor costs rose 15%> | S | ~10% | <...> |

### Imbalance Diagnosis
- Acute or chronic? <...>
- Primary cause (demand or supply-driven): <...>
- Secondary factors: <...>

### Rebalancing Projection
- Projected price direction: <up/down/stable>
- Magnitude of price move: <expected % change>
- Non-price adjustments (rationing, contracts, etc.): <...>
- Estimated time to rebalance: <...>

### Confidence
<high/medium/low> — <justification (e.g., "high: sales data available, elasticity estimates backed by industry comps; low: future supply contingent on policy not yet decided")>
```
