---
name: elasticity-analysis
display_name: Elasticity Analysis
class: lens
underlying_class: native
domain: economics
source: Marshall (Principles of Economics, 1890); formalized in neoclassical economics
best_for:
  - Quantifying demand response to price, income, or competitor-price changes
  - Identifying which product or service lever will move quantity most efficiently
  - Setting pricing strategy when you have historical sales and price data
one_liner: "Quantify how quantity responds to price, income, or cross-price changes."
---

# Elasticity Analysis

## Overview
Elasticity measures how much a quantity demanded changes when one economic variable (price, income, competitor price) shifts by one percent. Instead of saying "lower price increases sales," elasticity says "a 10% price drop increases quantity by 8%" — a ratio that lets you compare the strength of different levers and predict revenue impact. Practitioners use this when deciding which pricing move, promotion, or market segment to prioritize and when historical sales data exists to measure actual behavior.

## Analytical Procedure

### Phase 1 — Define the elasticity type and gather data

1. **Identify which elasticity you need to measure.** Choose one:
   - **Own-price elasticity:** How quantity changes when *this product's* price changes.
   - **Income elasticity:** How quantity changes when customer income (or purchasing power) changes.
   - **Cross-price elasticity:** How quantity of *this product* changes when a *competitor's* or *related product's* price changes.

2. **Collect historical data.** You need:
   - At least 10 observations (weeks, months, quarters — your choice, but be consistent).
   - For own-price: quantity sold and price per unit in each period.
   - For income: quantity sold and a measure of aggregate income or customer wealth (GDP per capita, median household income, credit card spending, etc.).
   - For cross-price: quantity of your product and the price of the competing or complementary product.
   - Control for obvious confounds (seasonality, promotions, stockouts). If a price change and a major ad campaign happened the same week, note it — you may need to isolate the price effect separately.

3. **Plot quantity vs. your chosen variable.** Use a scatter plot with the economic variable on the x-axis (price, income, or competitor price) and quantity on the y-axis. Visually check:
   - Is the relationship roughly linear, or does it curve sharply?
   - Are there obvious outliers or breaks (e.g., a price war that distorted normal behavior)?
   - If the relationship is non-linear, note it — you may need logarithmic transformation or segment the data.

### Phase 2 — Calculate elasticity

4. **Convert to percentage changes.** Elasticity is always a ratio of *percent* changes, not absolute changes. For each consecutive pair of observations, calculate:
   - % change in quantity = (Q₂ − Q₁) / Q₁ × 100
   - % change in driver = (Driver₂ − Driver₁) / Driver₁ × 100
   Where Driver is Price, Income, or Competitor Price depending on your elasticity type.

5. **Fit a regression or calculate the point elasticity.** Choose one method:

   **Method A — Regression (recommended for 10+ data points):**
   - Use log-log regression: log(Quantity) = a + b × log(Driver Variable)
   - The coefficient `b` is your elasticity estimate. This is the percent change in quantity per 1% change in the driver.
   - Report the R² to show how much of the variation in quantity is explained by this driver alone. R² > 0.5 is meaningful.

   **Method B — Midpoint formula (quick, for small datasets):**
   - Elasticity = [(Q₂ − Q₁) / ((Q₁ + Q₂) / 2)] / [(Driver₂ − Driver₁) / ((Driver₁ + Driver₂) / 2)]
   - This dampens the effect of extreme observations. Use it for one-off calculations or sensitivity checks.

6. **Interpret the coefficient.** The sign and magnitude tell the story:
   - **Own-price elasticity:** Negative values are normal (lower price → higher quantity). Magnitude > 1 means elastic (customers are price-sensitive; a 1% price drop increases quantity by >1%). Magnitude < 1 means inelastic (price cuts drive small quantity gains).
   - **Income elasticity:** Positive values mean the good is normal (income up → quantity up). Negative means inferior (income up → quantity down, e.g., cheap beans). Magnitude tells the strength.
   - **Cross-price elasticity:** Positive means substitutes (competitor price up → your quantity up). Negative means complements (competitor price up → your quantity down). Magnitude shows strength of the relationship.

### Phase 3 — Validate and apply

7. **Check for reverse causality and confounds.** Did price change *cause* the quantity shift, or did quantity pressure *cause* the price change? If your product was in shortage and you raised price, the quantity drop isn't demand elasticity — it's a supply shift. Look for:
   - Exogenous price moves (announced sales, industry-wide rate changes, tax changes) that moved price but not because of quantity pressure.
   - A gap between when price changed and when quantity responded (elasticity usually shows within 1-2 periods).
   - If reverse causality is present, note it and flag the elasticity estimate as unreliable.

8. **Test robustness.** Rerun the calculation with:
   - Different time windows (exclude known outliers like holiday spikes or stockouts).
   - Different product segments if data permits (luxury vs. budget, online vs. offline).
   - If elasticity stays similar, you have confidence. If it swings wildly, the number is probably unstable.

9. **Calculate revenue impact.** Use elasticity to predict the effect of a price move:
   - % change in revenue ≈ % change in price × (1 + elasticity)
   - Example: Own-price elasticity = −0.8. A 10% price cut: % change in revenue ≈ −10% × (1 − 0.8) = −10% × 0.2 = −2%. Revenue falls, so the price cut is not profitable.
   - If elasticity = −1.5, a 10% price cut: % change in revenue ≈ −10% × (1 − 1.5) = −10% × −0.5 = +5%. Revenue rises.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Elasticity type (own-price, income, or cross-price) is stated | Y/N |
| Data spans at least 10 observations and includes the driver variable | Y/N |
| Percentage changes were computed (not absolute changes) | Y/N |
| Coefficient was estimated via regression (R² reported) or midpoint formula | Y/N |
| Sign and magnitude of elasticity align with economic theory or prior knowledge | Y/N |
| Reverse causality and major confounds were checked | Y/N |
| Revenue impact was estimated from the elasticity coefficient | Y/N |

## Red Flags

- Elasticity near zero but with high R². This suggests the driver variable explains very little variation; other factors dominate quantity. The number is theoretically clean but practically useless.
- Elasticity has the opposite sign from what theory predicts (e.g., own-price elasticity is positive). Reverse causality or a major confound (promotion, stockout, competitor entry) is almost certainly at play. Do not use the coefficient without investigation.
- R² < 0.2 in regression. The driver explains less than 20% of quantity variation. Elasticity may be estimated, but it is noisy and unstable.
- Data includes a major exogenous shock (pandemic, competitor exit, supply disruption) that breaks the historical pattern. Elasticity estimated from pre-shock data may not hold going forward. Segment the data and report both.
- Revenue impact calculation was skipped or unclear. Elasticity is useful only if it changes what you decide. If you don't trace it to a revenue or margin decision, the analysis is incomplete.

## Output Format

```
## Elasticity Analysis

**Elasticity type:** [own-price | income | cross-price]

**Data summary:**
- Period: <start date> to <end date>, <N> observations
- Quantity range: <min> to <max> units
- Driver variable range: <min> to <max>

**Scatter plot visual check:**
- Relationship shape: [linear | curved | broken]
- Outliers or breaks: [none | <description>]

**Regression results (log-log):**
- Elasticity coefficient (b): <value>
- R²: <value>
- Interpretation: <one sentence; e.g., "A 1% price increase reduces quantity by 0.85%">

**Robustness checks:**
- Rerun with segment A: elasticity = <value> [similar | divergent]
- Rerun with segment B: elasticity = <value> [similar | divergent]
- Sensitivity: [robust | unstable]

**Reverse causality check:**
- Exogenous price drivers present: [yes | no]
- Lag structure observed: [yes | no, describe]
- Verdict: [causal link supported | reverse causality likely | unclear]

**Revenue impact (example: 10% price change):**
- % change in revenue = <calculation>
- Decision: [price move is profitable | price move erodes margin | neutral]

**Confidence: [high | medium | low]** — <justification, e.g., "High: R²=0.72, exogenous price variation, consistent across segments. Low: R²=0.15, no exogenous driver, elasticity unstable across periods.">
```
