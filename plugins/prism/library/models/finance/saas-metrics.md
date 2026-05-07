---
name: saas-metrics
display_name: SaaS Metrics
class: model
underlying_class: native
domain: finance
source: David Skok, "SaaS Metrics 2.0", for Entrepreneurs (2009); Brad McLeod, "SaaS Unit Economics" (2015); Seth Godin and others, Rule of 40 popularized in venture capital industry ~2015
best_for:
  - Predicting cash burn trajectory and runway from recurring revenue, churn, and growth
  - Identifying which metric is the binding constraint on unit economics
  - Diagnosing why a SaaS company is capital-inefficient despite strong topline growth
one_liner: "Recurring revenue, churn, and net new growth determine long-run profitability and capital efficiency."
---

# SaaS Metrics

## Overview

The SaaS Metrics model claims that the long-run viability and capital efficiency of a subscription business is governed by four interdependent metrics: **Monthly Recurring Revenue (MRR) or Annual Recurring Revenue (ARR)**, **net revenue retention / net dollar retention (NDR)**, **customer churn rate**, and **Rule of 40** (Growth Rate % + Magic Number / CAC Payback Period ≥ 40). The model is diagnostic and predictive: it reveals not only the current state of cash flow and runway but also which lever — growth, retention, unit economics, or sales efficiency — is the binding constraint on profitability and cash endurance. Unlike topline metrics (total bookings, gross revenue), SaaS metrics isolate the recurring, repeatable portion of revenue and expose the hidden drain of churn and expansion dynamics. The model is explanatory when applied to a concrete cohort or company.

## Core Variables and Relationships

The core variables and the relationships that connect them:

1. **Monthly Recurring Revenue (MRR) or Annual Recurring Revenue (ARR)** — the committed, subscription-based revenue recurring each period, net of discounts and prorations.
   - Driven by: New customer acquisition × Average Contract Value (ACV), plus expansion revenue (upsell, cross-sell).
   - Decremented by: Churn rate × Current MRR.
   - Direction: Higher MRR → longer runway, better unit-economics visibility, lower per-unit cost of operations.

2. **Net Revenue Retention (NRR) / Net Dollar Retention (NDR)** — the ratio of MRR retained + expansion revenue from the same cohort of customers in period t to MRR from those customers in period t−1. Formula: (Beginning MRR − Churned MRR + Expansion Revenue) / Beginning MRR.
   - Driven by: Gross churn rate (% of customers lost), expansion rate (% of revenue from upsells), and contraction (downgrades).
   - Interpretation: NRR > 100% means the company grows without new customer acquisition; NRR < 100% means contraction that new sales must offset.
   - Direction: Higher NRR → path to profitability even with slowing new sales; lower NRR → compounding pressure to acquire faster or burn capital.

3. **Customer Churn Rate** (monthly or annual) — the percentage of customers (by count or revenue) that leave the product each period.
   - Driven by: Product-market fit, product quality, customer success execution, economic downturn, price increases.
   - Direction: Higher churn → shorter customer lifetime, lower LTV, faster runway depletion; lower churn → exponential endurance benefit.

4. **Magic Number** (or Sales Efficiency Ratio) — Net New MRR generated in a period ÷ Sales & Marketing spend in the *prior* period. Typical targets: 0.75 or higher.
   - Driven by: Conversion rate, ACV, CAC, and sales productivity.
   - Direction: Higher Magic Number → faster payback of sales investment, lower cash burn per acquired dollar.

5. **CAC Payback Period** — Time (in months) for a customer's gross margin to repay the fully-loaded CAC (fully-loaded CAC / Monthly Gross Margin per customer). Typical targets: 12 months or less.
   - Driven by: CAC, Gross Margin %, and churn rate (a churned customer never repays).
   - Direction: Shorter payback → faster redeployment of capital, lower financing risk; longer payback → capital-intensive model.

6. **Rule of 40** — Growth Rate (%) + (Magic Number or CAC Payback as a percentage metric) ≥ 40. Alternative form: Growth Rate + Magic Number ≥ 40, or Growth Rate + (Net Margin %) ≥ 40 for mature companies.
   - Interpretation: Captures the trade-off between growth and profitability. High-growth companies (50%+ YoY) can sustain Rule of 40 even with Magic Number of −10; low-growth companies (10% YoY) need Magic Number ≥ 30 to qualify.
   - Direction: Rule of 40 ≥ 40 → investor-fundable / long-term viable; Rule of 40 < 30 → unsustainable burn, capital trap.

**Net relationships:**
- High NRR (> 110%) + Low Churn (< 2% MRR monthly) reduces dependency on new sales; enables profitable growth.
- Low CAC Payback + High Magic Number + Reasonable growth can achieve Rule of 40 at modest burn.
- High Growth + Low NDR is a velocity trap: the company burns cash faster but never achieves durability.
- MRR growth without attention to churn or NRR masks revenue quality: the numerator goes up but the denominator (customer cohort persistence) weakens.

## Key Predictions

- **A company with MRR growth > 15% monthly but NRR < 95% will eventually decelerate to profitability or failure despite high topline growth**, because the cohort-level unit economics are negative and new-customer acquisition only delays the cliff.

- **A business with high churn (> 5% monthly) cannot be profitable without either a very high gross margin (> 80%) or extreme sales efficiency (Magic Number > 1.5)**, because too much MRR is evaporating to replenish.

- **Rule of 40 < 30 is a hard boundary for VC-fundable SaaS; companies in this zone require either a dramatic inflection in growth, churn, or sales efficiency within 12–18 months, or they face a capital-sufficiency crisis.**

- **Companies with NRR > 115% and CAC Payback < 9 months can achieve Rule of 40 ≥ 40 even at single-digit growth rates**, unlocking profitable scaling without external capital.

- **MRR stagnation with stable churn and NRR signals a sales/marketing productivity crisis, not a product crisis**; the fix is CAC reduction or sales process efficiency, not product changes.

- **A company with ARR < $1M and NRR < 95% faces a mathematical race: burn rate must be < (1 − NRR) × MRR × 12 to reach profitability**, and most startups cannot achieve this without killing growth to uncompetitive levels.

## Application Procedure

Instantiate the model against a specific SaaS company or a specific cohort of customers within a company.

1. **Define the scope precisely: company, time period, and cohort (if applicable).**
   - Entire company (across all customers and segments)?
   - Single customer segment (e.g., SMB vs. enterprise)?
   - Single cohort (e.g., all customers acquired in Q1 2026)?
   - Write the boundary: "Company-wide ARR, cohort-based NRR, 12-month lookback to 2026-04-11."

2. **Collect the four primary inputs:**
   - **ARR or MRR** as of the measurement date. (If monthly, annualize; if cohort-based, use cohort ARR.)
   - **Gross churn rate** (% of customers lost per month, or count-based churn for enterprise).
   - **NRR** (or derive it: (Beginning MRR − Churn × Beginning MRR + Expansion) / Beginning MRR, measured over 12 months).
   - **CAC Payback Period** (CAC ÷ (Monthly Gross Margin per Customer)), derived from:
     - CAC: (Sales & Marketing spend in the cohort acquisition period) / (Number of new customers acquired)
     - Monthly Gross Margin per Customer: (ARPU × Gross Margin %) (typically 70–85% for SaaS)

3. **Derive secondary metrics:**
   - **Magic Number**: Net New MRR (current period MRR − prior period MRR − churn loss) ÷ (Sales & Marketing spend in prior period). If > 0.75, efficiency is acceptable; < 0.50, efficiency is poor.
   - **Monthly Gross Churn Rate** (if only annual is available): Approximate as Annual ÷ 12, or derive from retention curve.
   - **Monthly Burn Rate**: (Operating expenses − Gross profit) / 1 (per month).
   - **Runway**: Current cash balance ÷ Monthly burn rate (in months until depletion).

4. **Assess each metric against benchmarks:**
   - NRR: > 110% is exceptional; 100–110% is healthy; 90–100% is declining but common early-stage; < 90% is a warning sign.
   - Churn: < 2% monthly is excellent; 2–5% is acceptable for SMB; > 7% is unsustainable without extraordinary unit economics.
   - CAC Payback: < 12 months is standard for venture-backed SaaS; < 9 months is strong; > 18 months is unsustainable without positive unit economics elsewhere.
   - Magic Number: > 0.75 is healthy; 0.5–0.75 is acceptable if growth is high; < 0.5 is a red flag.

5. **Compute Rule of 40** (or your variant):
   - Growth Rate (YoY % change in ARR) + Magic Number ≥ 40?
   - Or: Growth Rate + (Contribution Margin % if near profitability)?
   - If Rule of 40 ≥ 40, the company is on a sustainable path (or close). If < 30, the company has a capital-efficiency problem.

6. **Identify the binding constraint:**
   - Is NRR the issue (high churn, low expansion)?
   - Is growth the issue (slow new sales despite good retention)?
   - Is unit economics the issue (high CAC, low Magic Number)?
   - The binding constraint is the one with the largest gap to a healthy benchmark; fixing it will move Rule of 40 the most.

7. **Project forward:**
   - If NRR < 100%, project the MRR cliff: when will churn exceed growth?
   - If Magic Number < 0.75, project the burn cliff: when will runway deplete?
   - Identify the most likely crisis point (usually 12–24 months out).

8. **Check boundary conditions** (below). If any apply, note that the SaaS metrics view is incomplete.

## Boundary Conditions

The SaaS Metrics model assumes a mature, subscription-based recurring-revenue business with clear customer identity and predictable churn. It breaks down or becomes partial under:

- **Very early stage (ARR < $100K, or < 20 paying customers).** Customer cohorts are too small to produce statistically meaningful churn or NRR; the model's predictions are noise. Supplement with cohort analysis once n ≥ 50 per cohort.

- **Highly seasonal or lumpy revenue (e.g., annual contracts, educational software with fiscal-year cycles).** The monthly MRR view is misleading; use quarterly or annual cohorts instead. Churn and NRR should be measured over the same period as the contract.

- **Mixed business model (SaaS + services, SaaS + perpetual licenses, SaaS + marketplace commissions).** The recurring-revenue base does not capture the full cash equation. Separate services or transaction-based revenue, and model them independently.

- **High-touch enterprise sales with multi-year contracts and long sales cycles.** CAC and payback are distorted by the lag between spend and recognition; use a bookings-based model (TCV, ACV) alongside MRR to avoid overestimating current health.

- **Usage-based or consumption-based pricing (no fixed MRR).** The model assumes predictable recurring contracts; usage-based revenue is volatile and requires a separate probabilistic model.

- **Strong macro or market-specific headwinds (recession, regulatory change, technology disruption).** Churn and NRR may be unstable and non-predictive of future cohort performance. Use forward-looking cohort analysis and scenario modeling.

## Output Format

```
## SaaS Metrics Analysis: <company or cohort name>

**Scope:** <company, cohort, time period>
**Measurement date:** <date>
**Time horizon for churn / NRR:** <e.g., 12 months>

### Core metrics
| Metric | Value | Benchmark | Status |
|---|---|---|---|
| ARR / MRR | $X | — | — |
| Monthly Churn Rate | Y% | < 2% | 🟢 / 🟡 / 🔴 |
| NRR (12-month) | Z% | > 110% | 🟢 / 🟡 / 🔴 |
| CAC Payback Period | M months | < 12 months | 🟢 / 🟡 / 🔴 |
| Magic Number | N | > 0.75 | 🟢 / 🟡 / 🔴 |
| YoY Growth Rate | P% | Context-dependent | — |

### Rule of 40
- **Calculation:** Growth Rate (P%) + Magic Number (N) = **R** (target ≥ 40)
- **Interpretation:** <sustainable / acceptable / at-risk / critical>

### Binding constraint
<Which metric is furthest from healthy benchmarks and why it matters most for the company's next 12–24 months.>

### Forward projection
- **MRR in 12 months (if current trends hold):** $X → $Y (based on growth − churn)
- **Monthly burn runway:** Z months at current burn rate
- **Critical inflection point:** <When does the company hit a wall without intervention? What metric must change?>

### Primary levers to move Rule of 40
1. <Fix X (e.g., reduce CAC, improve NRR)>
2. <Fix Y>
3. <Fix Z>

### Boundary-condition notes
<Which of the boundary conditions apply, and what complementary analysis is needed (e.g., cohort-level detail, bookings model, usage forecast)?>

### Confidence: high | medium | low
<Reasoning: data maturity (number of cohorts, months of history), fit to boundary conditions, stability of churn / NRR estimates, macro environment stability.>
```
