---
name: unit-economics
display_name: Unit Economics (LTV/CAC)
class: model
underlying_class: native
domain: finance
source: David Skok, "SaaS Metrics 2.0," For Entrepreneurs, 2009; foundational framework in venture capital and subscription business evaluation
best_for:
  - Predicting whether a business can achieve profitability and at what scale
  - Comparing unit economics across products or customer segments
  - Diagnosing whether a unit-level economics problem is rate-of-acquisition or rate-of-retention
one_liner: "Diagnose business profitability via the LTV-to-CAC ratio."
---

# Unit Economics (LTV/CAC)

## Overview

Unit Economics claims that the long-run profitability of any subscription or repeat-revenue business is governed by a single structural ratio: the lifetime value of a customer (LTV) divided by the cost to acquire that customer (CAC). The model is predictive and diagnostic: it predicts whether unit-level operations can ever be profitable, and if not, *why* — whether the problem is acquisition cost, retention, pricing, or expansion. Unlike Porter's Five Forces (which explains industry structure), Unit Economics explains the embedded unit-level viability of a single business model. The model is descriptive in its core claim (LTV/CAC determines profitability) but is best used operationally: to identify which lever (acquisition, retention, price, churn) to pull when unit economics deteriorates.

## Core Variables and Relationships

The LTV/CAC ratio is composed of several components that drive profitability:

1. **Lifetime Value (LTV)** — the total profit a customer generates over their lifetime.
   - **Average Revenue Per User (ARPU)** per period (month, year)
   - **Gross Margin (%)** on revenue (cost of goods sold and direct delivery costs)
   - **Customer Lifetime (years / periods)** — inverse of annual churn rate
   - Direction: Higher ARPU → higher LTV; higher gross margin → higher LTV; lower churn → higher LTV
   - Common formula: LTV = ARPU × Gross Margin × (1 / Annual Churn Rate)

2. **Customer Acquisition Cost (CAC)** — the fully-loaded cost to win one customer.
   - **Sales & Marketing Spend** in a period
   - **Number of Customers Acquired** in that period
   - **Blended unit CAC** = Total S&M Spend / Customers Acquired
   - Include salaries, tools, travel, creative, media spend, channel partner payouts — anything required to put a customer on the books
   - Direction: Higher CAC → harder to justify acquisition; must be offset by efficiency gains or pricing increases

3. **The Core Ratio** — LTV / CAC determines payback and cumulative profitability.
   - **LTV / CAC < 1.0**: Unit economics are broken; the company loses money on every customer it acquires.
   - **LTV / CAC = 1.0–2.0**: Marginally viable, but leaves no room for operational overhead, R&D, or G&A; growth is unsustainable.
   - **LTV / CAC = 2.5–3.0**: Healthy for venture-backed software (rule of thumb: 3:1 is the bar for profitability and reinvestment).
   - **LTV / CAC > 4.0**: Unusually efficient; may indicate network effects, viral loops, or a highly differentiated product.

4. **Payback Period** — how long it takes for gross margin dollars from a customer to repay CAC.
   - Payback (months) = CAC / (ARPU × Gross Margin)
   - Shorter payback → faster capital recycling → ability to reinvest sooner
   - Direction: Shorter payback → more sustainable growth; longer payback → requires more upfront capital

5. **Churn Rate** — the rate at which customers leave, in percentage per period.
   - **Monthly Churn %** = (Customers at period start − Customers at period end + Customers acquired) / Customers at period start
   - Alternative: Net Retention Rate (how much revenue is retained / expanded after churn and expansion)
   - Direction: Higher churn → lower LTV → lower LTV/CAC ratio; even small churn increases accumulate exponentially

The relationships are multiplicative and nonlinear:
- A 10% increase in churn (e.g., 5% → 5.5%) can cut LTV by 10%, collapsing a 3:1 ratio to below 2:1.
- A 20% reduction in CAC while holding churn constant increases the ratio by 25%.
- Expansion revenue (upsell, cross-sell) enters as an uplift to ARPU, compounding over lifetime.

## Key Predictions

- **A business with LTV/CAC < 1.5 cannot profitably scale regardless of market size.** No amount of top-line growth can overcome a unit-level loss. It will eventually run out of capital or be forced to cut acquisition spending, causing growth to stall. The fix requires either reducing CAC, increasing ARPU, or reducing churn — not more capital.

- **Churn is the hidden leverage point.** A 1-percentage-point reduction in monthly churn (e.g., 5% → 4%) increases LTV by 25% (all else constant), often with minimal incremental cost. Retention investments yield far higher ROI than acquisition investment once churn is high.

- **Payback period determines growth velocity and required capital.** A business with 6-month payback can reinvest gross margin profits within the same fiscal year; a 24-month payback requires 2 years of external capital to fuel growth at the same customer-acquisition rate. Payback > 24 months is a capital crunch waiting to happen.

- **Unit economics compress at scale when CAC becomes dominated by fixed overhead.** Early-stage (pre-PMF) companies often show inflated CAC because they allocate all S&M spend across a small cohort. Once acquisition scales and marketing efficiency kicks in, CAC per customer often drops 30–50%, improving LTV/CAC materially.

- **Expansion revenue (net retention > 100%) can rescue a marginal LTV/CAC.** If ARPU grows 20–30% per year via upsell, a 2:1 ratio on base ARPU can become 3.5:1 on blended ARPU, turning a break-even business into one that compounds profitably.

- **Geographic or segment arbitrage reveals hidden LTV/CAC variance.** Enterprise customers often have higher LTV (longer lifetime, larger ARPU, lower churn) but higher CAC (longer sales cycle). SMB / self-serve segments may have lower LTV but *much* lower CAC. The segment-level LTV/CAC can differ by 10× even within the same product.

## Application Procedure

Instantiate the model against a specific business, segment, or customer cohort.

1. **Define the business unit and cohort precisely.** Are you analyzing a single product line, a customer segment (enterprise vs. SMB), a geographic market, or the entire company? Specify the time period (usually annual or trailing-twelve-month) and the cohort (e.g., customers acquired in Q1 2026).

2. **Calculate Lifetime Value (LTV).**
   - Measure ARPU for the cohort: total revenue / customer count, annualized.
   - Measure Gross Margin %: subtract direct costs (COGS, payment processing, hosting, support) from revenue and divide by revenue. Do *not* include overhead.
   - Measure Customer Lifetime by calculating the inverse of churn. For a monthly-churn rate c, lifetime = 1 / (c / 12) months. Alternatively, analyze actual retention curves for the cohort and integrate under the curve.
   - Compute LTV = ARPU × Gross Margin % × (1 / Annual Churn Rate). Sanity-check against actual per-customer profit over a 3–5 year window if you have historical data.

3. **Calculate Customer Acquisition Cost (CAC).**
   - Tally all S&M spend (salaries, commissions, tools, advertising, events, channel payouts) for the period.
   - Divide by the number of new customers acquired in that period.
   - If acquisition channels differ (e.g., direct sales vs. self-serve), compute CAC per channel and flag the mix.

4. **Calculate the LTV/CAC ratio and payback period.**
   - Ratio = LTV / CAC.
   - Payback (months) = CAC / (ARPU × Gross Margin % / 12).
   - Compare against the benchmarks: healthy SaaS typically targets 3:1 or better.

5. **Identify which variable is the constraint.**
   - Plot LTV and CAC separately over the last 3–5 cohorts. Is LTV declining (churn worsening, ARPU falling)? Is CAC rising (market saturation, higher customer acquisition cost)? Both?
   - If LTV is falling, churn and retention are the levers.
   - If CAC is rising, product-market fit is being questioned or acquisition channels are saturating; revisit positioning or channel mix.

6. **Model the sensitivity of LTV/CAC to changes in each driver.**
   - E.g., "If we reduce churn from 5% to 4% monthly, LTV increases from $X to $Y, and LTV/CAC moves from 2.2:1 to 2.8:1."
   - E.g., "If we reduce CAC from $500 to $400 via product-led growth, payback shrinks from 18 months to 14 months."
   - This identifies which levers move the needle most.

7. **Check boundary conditions** (below). If any apply, note that the model gives a partial view and flag what additional analysis is needed.

8. **Generate the diagnosis.**
   - Is unit economics healthy or broken? By how much?
   - Which variable is the primary constraint (churn, ARPU, CAC, gross margin)?
   - What is the minimum improvement required to reach 3:1? (This gives a concrete target.)

## Boundary Conditions

Unit Economics assumes a stable, repeating business model and breaks down or becomes partial under these conditions:

- **Two-sided or multi-sided marketplaces where unit economics differ radically by side.** A ride-share calculates LTV/CAC for riders and drivers separately; they often have opposite slopes. The company is profitable only if the sum of both sides' unit economics is positive. The simple LTV/CAC framework cannot capture this without explicit modeling of both sides.

- **Highly seasonal or multi-year contract cycles.** SaaS with annual upfront contracts has zero churn in year 1 (LTV is inflated) and sharp cliff churn at year-end. Monthly churn-based LTV is misleading; must model cohort retention curves explicitly.

- **High expansion revenue and logo churn divergence.** Enterprise software often has high annual churn by count (companies close) but negative net churn (survivors expand 20–40% in spend). A simple "5% monthly churn" LTV calculation misses this; must separate logo churn, expansion revenue, and contraction.

- **Freemium or land-and-expand models with late monetization.** If acquisition to free users is near-zero CAC, LTV/CAC for free users is not meaningful; the real CAC is the cost to convert a free user to paying, which occurs months after acquisition. The model needs cohort-level conversion rates baked in.

- **Negative unit economics by design during growth phase.** Venture-backed companies often run LTV/CAC < 1 deliberately (e.g., burning capital to acquire market share or achieve critical mass / network effects). The model predicts that growth will stop when capital runs out; it does not account for the option value of market dominance or second-order monetization shifts. Complement with a strategic / option-value view.

- **High customer concentration or winner-take-most dynamics.** If 50% of revenue comes from 5 customers, average LTV/CAC is misleading; cohort averages hide extreme variance. Analyze top-N separately from long-tail; the model works well for the tail but not the head.

- **Significant network effects or viral loops not captured by CAC.** If a customer brings 2–3 free-riding additional customers (virality), the traditional CAC is double-counted. Adjust CAC downward by the multiplier or model viral coefficients separately.

## Output Format

```
## Unit Economics Analysis: <business / segment name>

**Business unit:** <product, geography, segment>
**Cohort:** <time period: e.g., customers acquired Q1 2026>
**Analysis date:** <date>

### Financial metrics
| Metric | Value | Notes |
|---|---|---|
| ARPU (annual) | $<value> | <revenue per customer / count> |
| Gross Margin | <value>% | <(Revenue − direct costs) / Revenue> |
| Monthly Churn | <value>% | <(Churned customers / starting base)> |
| Annual Churn | <value>% | <derived> |
| Customer Lifetime (years) | <value> | <1 / annual churn> |
| LTV | $<value> | <ARPU × GM% × lifetime> |
| CAC | $<value> | <total S&M spend / customers acquired> |
| Payback (months) | <value> | <CAC / (ARPU × GM% / 12)> |

### Ratio & Health
| Ratio | Value | Benchmark | Assessment |
|---|---|---|---|
| LTV / CAC | <value>:1 | 3.0:1 | <healthy / marginal / broken> |
| Implied status | ... | ... | <growing sustainably / shrinking / at scale> |

### Constraint analysis
- **Primary constraint** (LTV or CAC): <which is moving most, in what direction>
- **Sub-constraint**: <churn, ARPU, CAC channel mix, or gross margin>
- **Evidence**: <3-month or 3-cohort trend>

### Scenario: paths to 3.0:1 ratio
| Scenario | Target metric | Required change | Feasibility |
|---|---|---|---|
| Retention focus | Churn | <from X% to Y%> | <high / medium / low> |
| Pricing / ARPU | ARPU | <from $X to $Y> | ... |
| Acquisition efficiency | CAC | <from $X to $Y> | ... |

### Boundary-condition notes
<which conditions apply and whether the LTV/CAC analysis is the binding constraint or whether complementary analysis is needed (e.g., cohort curve, two-sided marketplace, network effects)>

### Confidence: high | medium | low
<reasoning: data completeness (revenue, churn, CAC accuracy) + cohort stability (is churn stable or changing?) + boundary-condition fit (single-sided, mature SaaS vs. freemium / multi-sided) + whether LTV/CAC is the actual bottleneck>
```
---
