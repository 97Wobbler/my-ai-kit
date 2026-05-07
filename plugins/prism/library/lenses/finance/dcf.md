---
name: dcf
display_name: Discounted Cash Flow Valuation
class: lens
underlying_class: native
domain: finance
source: Fisher (1930, The Theory of Interest); modernized by Graham & Dodd (1934, Security Analysis); operationalized in corporate finance (Damodaran, 2012)
best_for:
  - Valuing a business or asset based on expected cash generation
  - Comparing intrinsic value to market price
  - Stress-testing assumptions about growth, margins, and terminal value
one_liner: "Core valuation method — discount future cash flows to present value to compute intrinsic value."
---

# Discounted Cash Flow Valuation

## Overview

DCF values an asset by projecting its future cash flows and discounting them to present value using a risk-adjusted discount rate. The method forces explicit assumption-making about revenue growth, operating margins, capital expenditure, and terminal value — making hidden leverage and fragility visible. Practitioners use DCF when market price seems detached from fundamentals and they need to defend a valuation against skeptics or capital committees. The output is a single intrinsic value estimate and a sensitivity surface showing which assumptions move the needle most.

## Analytical Procedure

### Phase 1 — Cash Flow Projection

1. **Establish the projection period.** Choose 5 to 10 years. Longer periods amplify forecast error; shorter periods overweight terminal value. Document the choice (e.g., "5 years to first product maturity; 10 years to capture full cycle").

2. **Project revenue for each year in the projection period.**
   - Start with historical revenue (last 3–5 years).
   - State the growth rate assumption explicitly (percentage per year).
   - Document the driver: market expansion, volume, pricing, or mix. If you assume 15% growth, explain which component moves.
   - For years 6+, flatten the growth rate gradually toward a terminal rate (typically 2–3%, GDP growth or inflation).
   - Flag any year-on-year decline as a red flag requiring justification.

3. **Project operating cash flow (or EBIT/NOPAT, depending on method) for each year.**
   - Calculate operating margin (EBIT / Revenue) for each historical year.
   - State your assumption for future margin (will it stay flat, improve, or decline?).
   - Justify the assumption: is it based on scale economies, competitive positioning, industry trends, or management guidance?
   - Common error: assuming margins improve without explaining why competitors don't erode them.
   - Apply the margin to projected revenue to get operating profit.

4. **Project Free Cash Flow to the Firm (FCFF) for each year.**
   - FCFF = Operating Profit × (1 − Tax Rate) + Depreciation − Capital Expenditure − Change in Net Working Capital.
   - For each component:
     - **Tax rate**: use the company's effective rate (check tax filings; not the statutory rate).
     - **Depreciation**: as a % of revenue or capital stock. If capex is high, depreciation should track it over time.
     - **Capital Expenditure (capex)**: as a % of revenue. Maintenance capex (to sustain revenue) typically runs 2–5% of revenue; growth capex varies. Document both.
     - **Net working capital change**: as a % of revenue growth. High-growth businesses burn cash here (inventory, receivables); mature businesses may release it.
   - The result is cash available to all claimants (debt and equity).

5. **Project a terminal value.** This typically represents 60–80% of total DCF value, so it deserves scrutiny.
   - Choose one method:
     - **Perpetuity growth**: Terminal Value = FCFF(Year N) × (1 + g) / (Discount Rate − g), where g is perpetual growth (2–3%).
     - **Exit multiple**: Assume the business sells at a market multiple (e.g., 10× EBIT) in year N. Terminal Value = EBIT(Year N) × Exit Multiple.
   - Justify the choice. Perpetuity growth is more conservative; exit multiple is more market-anchored but depends on multiples staying stable.
   - Sanity check: does the terminal value imply the business is growing at GDP rate? Does the exit multiple match current market comparables?

### Phase 2 — Discount Rate Selection

6. **Calculate the Weighted Average Cost of Capital (WACC).**
   - WACC = (E/V × Re) + (D/V × Rd × (1 − Tc))
   - **E/V**: market value of equity as % of total value.
   - **D/V**: market value of debt as % of total value.
   - **Re (cost of equity)**: use CAPM: Re = Risk-free rate + Beta × Market risk premium.
     - Risk-free rate: use long-term government bond yield (e.g., 10-year Treasury).
     - Beta: measure of volatility vs. the market. Use historical beta (5 years) or compare to industry peers if the company is private.
     - Market risk premium: typically 5–7% (historical average); pick one and document it.
   - **Rd (cost of debt)**: company's yield to maturity on outstanding bonds, or estimated based on credit rating.
   - **Tc (tax rate)**: corporate tax rate (debt is tax-deductible).
   - Red flag: If WACC is higher than expected return on projects, the company is destroying value.

### Phase 3 — Valuation Calculation

7. **Discount each year's FCFF to present value.**
   - PV(Year i) = FCFF(Year i) / (1 + WACC)^i
   - Sum the PV of all projection years.

8. **Discount terminal value to present value.**
   - PV(Terminal Value) = Terminal Value / (1 + WACC)^N

9. **Sum to get Enterprise Value.**
   - Enterprise Value = Sum of PV(FCFF) + PV(Terminal Value)

10. **Adjust to get Equity Value.**
    - Equity Value = Enterprise Value − Net Debt
    - Net Debt = Total Debt − Cash and Cash Equivalents.
    - Do not double-count: if FCFF already deducts interest, do not subtract debt again.

11. **Divide by shares outstanding to get Per-Share Value.**
    - Price per Share = Equity Value / Diluted Shares Outstanding
    - Use diluted shares (including in-the-money options, warrants, etc.) to avoid overvaluing on a per-share basis.

### Phase 4 — Sensitivity and Stress Testing

12. **Build a sensitivity table.** Vary two key assumptions (e.g., terminal growth rate and WACC) and observe how the per-share value changes. This shows which assumptions the valuation depends on most.

13. **Stress-test extreme scenarios.** Run the model under pessimistic and optimistic cases:
    - **Base case**: best estimate of all assumptions.
    - **Upside**: revenue growth +2%, margin expansion +200bps, WACC −0.5%.
    - **Downside**: revenue growth −2%, margin compression −200bps, WACC +0.5%.
    - Document the probability-weighted average if you want a single "expected" value.

14. **Compare to market price.** Calculate upside/downside: (Intrinsic Value − Market Price) / Market Price. If significantly positive or negative, investigate why. Possible explanations:
    - Your assumptions are more pessimistic or optimistic than the market.
    - The market is mispricing the stock.
    - You have missed a risk or opportunity (check competitor analysis, regulatory changes, technology disruption).

## Evaluation Criteria

| Check | Pass |
|---|---|
| Revenue growth assumptions tied to explicit drivers (market size, volume, pricing, mix) | Y/N |
| Operating margin assumptions justified by scale, competition, or management track record | Y/N |
| Capex and working capital projections realistic relative to historical and peer benchmarks | Y/N |
| Terminal growth rate ≤ long-term GDP growth (typically 2–3%) | Y/N |
| WACC calculation shows all inputs: risk-free rate, beta, market risk premium, debt cost, capital structure | Y/N |
| Terminal value as % of total value is between 50–85% (wide range is normal; >85% signals over-reliance) | Y/N |
| Sensitivity table covers plausible ranges (not just ±1%) | Y/N |
| Comparison to market price includes hypothesis for any large gap | Y/N |

## Red Flags

- Revenue growth rate is higher than the company's historical long-term growth or industry growth rate, without explaining why competitive position or market will shift.
- Operating margins improve year-on-year with no explanation (scale economies, pricing power, cost reduction). In competitive industries, margins tend to compress over time.
- Terminal growth rate exceeds GDP growth or long-term inflation rate. This implies the business will grow faster than the economy forever, which is unsustainable.
- Terminal value is > 85% of total value. The valuation is hostage to assumptions 5+ years out; short-term execution matters less than it should.
- WACC is lower than expected operating return on projects. The company should be expanding; if it's not, something is wrong with strategy.
- Sensitivity table only varies assumptions by ±1% or uses overlapping ranges (e.g., WACC of 7.5%, 8%, 8.5%). Widen the ranges; the output should show material variation in value.
- Market price is 50%+ above intrinsic value, and the analysis assumes no change in competitive position or market growth. In that case, you may have underestimated the value of intangibles (brand, network effects, switching costs).
- Per-share value is calculated using basic shares outstanding instead of diluted shares. This overstates value to current shareholders by ignoring dilution.

## Output Format

```
## DCF Valuation Summary

### Assumptions
- Projection period: ___ years
- Revenue CAGR (projection): ___%; Driver: ___
- Terminal growth rate: ___%
- Operating margin (steady state): ___%
- Tax rate: ___%
- WACC: ___%
  - Risk-free rate: ___%
  - Beta: ___
  - Market risk premium: ___%
  - Cost of debt: ___%

### Valuation Results
- Sum of PV(FCFF, Years 1–N): $___
- PV(Terminal Value): $___
- Enterprise Value: $___
- Less: Net Debt: $___
- Equity Value: $___
- Diluted shares outstanding: ___
- **Intrinsic value per share: $___**

### Sensitivity Analysis
| WACC ↓ / Terminal Growth → | 2.0% | 2.5% | 3.0% |
|---|---|---|---|
| 8.0% | $___ | $___ | $___ |
| 8.5% | $___ | $___ | $___ |
| 9.0% | $___ | $___ | $___ |

### Scenario Analysis
| Scenario | Revenue CAGR | Op. Margin | WACC | Per-share value | Probability |
|---|---|---|---|---|---|
| Downside | ___% | __% | __% | $___ | ___ |
| Base | ___% | __% | __% | $___ | ___ |
| Upside | ___% | __% | __% | $___ | ___ |

### Market Comparison
- Current market price: $___
- Intrinsic value (base case): $___
- Upside / Downside: ___% / ___%
- Rationale for gap: <brief statement of what explains the difference>

### Key Risks to Value
1. <assumption-dependent risk and mitigation if plausible>
2. <...>

### Confidence
<high/medium/low> — <one sentence justifying the rating based on assumption robustness, visibility, and time horizon>
```
---
