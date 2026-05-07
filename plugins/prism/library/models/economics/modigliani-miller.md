---
name: modigliani-miller
display_name: Modigliani-Miller
class: model
underlying_class: native
domain: economics
source: Franco Modigliani & Merton H. Miller, "The Cost of Capital, Corporation Finance and the Theory of Investment," American Economic Review, 1958; extended Miller & Modigliani 1961, 1963
best_for: Predicting firm value and cost of capital under different capital structures, and identifying when leverage creates or destroys value
one_liner: "Capital structure does not affect firm value — cash flows are the sole determinant."
---

# Modigliani-Miller

## Overview

The Modigliani-Miller (MM) Theorem claims that **under a set of idealized
market conditions, the total value of a firm is independent of its capital
structure** — that is, how much debt versus equity it issues. The theorem
explains why capital structure is irrelevant to firm value: the firm's
operating cash flows are determined by its assets and business model, not
by how those cash flows are divided between debt holders and equity holders.
The theorem is both descriptive (explaining when and why capital structure
does not matter) and predictive (identifying which deviations from the
idealized conditions *make* capital structure matter). Without the theorem,
many corporate finance decisions appear ad hoc; with it, capital structure
becomes a derived question: *where* do taxes, costs of financial distress,
or agency costs create value?

## Core Variables and Relationships

The core identity under Modigliani-Miller (Proposition I, no taxes):

    V_firm = V_unlevered = (Operating Cash Flows) / (Weighted Average Cost of Capital)

The value of a firm is the present value of its free cash flows, discounted
at a rate that reflects the risk of those cash flows. This rate does *not*
depend on whether the cash flows are promised to debt or equity; it depends
on the *business risk* of the assets generating them.

**Proposition I (no taxes):** The total value of the firm is invariant to
leverage.

- V_leveraged = V_unlevered (regardless of D/E ratio)
- The cost of equity rises with leverage (equity becomes riskier as debt
  claims are senior)
- The cost of debt is approximately fixed (or rises slightly)
- The WACC remains constant even though individual component costs shift

**Proposition II (no taxes):** The cost of equity rises linearly with
leverage.

    r_equity = r_unlevered + (r_unlevered − r_debt) × (D/E)

As the firm borrows more, equity holders face greater financial risk
(larger probability of insolvency, greater volatility of their residual
claim). They demand higher returns to compensate. The increase in required
return on equity exactly offsets the cheaper cost of debt, leaving WACC flat.

**With corporate taxes** (Modigliani & Miller 1963):

    V_leveraged = V_unlevered + (Tax Rate × Debt)

The tax deductibility of interest creates a corporate tax shield: each dollar
of debt interest reduces taxable income, saving (Tax Rate × Interest) in
taxes. This tax shield has present value (Tax Rate × Debt), so leverage
*does* increase firm value — but only because of taxes, not because of any
operating or financial synergy.

**Key drivers of whether MM applies:**

1. **Perfect capital markets:** No transaction costs, no information
   asymmetry, no taxes, no bankruptcy costs.
2. **Perfect substitutability:** Individuals can borrow at the same rate as
   corporations (otherwise MM fails).
3. **Rational expectations:** Investors understand the riskiness of cash
   flows correctly.
4. **No agency costs:** Managers act in the interests of shareholders and
   creditors.

## Key Predictions

- **Leverage is value-neutral if and only if perfect capital-market
  conditions hold.** In any real firm, at least one condition fails
  (taxes, bankruptcy costs, information asymmetry, agency conflicts), so
  leverage does affect value. But the MM model tells you *which* force is
  at work.

- **A firm cannot increase its total value merely by issuing debt and
  distributing the proceeds to shareholders.** The firm's assets and cash
  flows are unchanged; the distribution of those flows to debt and equity
  holders is a zero-sum game (before taxes and distress costs). This
  prediction directly contradicts naive "financial engineering."

- **The cost of equity must rise with leverage.** If a firm increases D/E
  from 0.5 to 1.0, and if the cost of debt is 5% and unlevered cost of
  equity is 10%, then the new cost of equity will rise from 10% to 15% —
  investors will not accept the same return for greater financial risk.

- **If two firms have identical operating cash flows but different capital
  structures, an investor can "undo" the firm's leverage by borrowing on
  personal account.** This arbitrage mechanism enforces the MM prediction:
  leverage cannot create value if you can replicate it yourself.

- **Under corporate taxation, optimal capital structure is at or near 100%
  debt** (from MM's perspective) — the tax shield is maximized. Real firms
  do not lever this heavily because bankruptcy costs and agency costs
  outweigh the tax shield at high leverage. This discontinuity between the
  MM prediction and observed behavior is the key signal that real-world
  frictions matter.

## Application Procedure

Instantiate the model against a concrete capital-structure decision: a firm
considering a change in leverage, a comparison of two firms with different
debt levels, or a valuation problem.

1. **Define the firm's operating cash flows (or EBIT).** Calculate or
   estimate the free cash flow to the firm independent of its capital
   structure. This is the anchor — it does not change with leverage.

2. **Identify the current (or proposed) capital structure.** What is the
   current D/E ratio, debt level, and cost of debt? What is the proposed
   change?

3. **Calculate the unlevered cost of equity** (the WACC if the firm were
   all-equity financed). This reflects the business risk of the assets.
   - Use CAPM with an unlevered beta (asset beta), or
   - Use the WACC formula with the *current* cost of debt and cost of
     equity, then solve for the cost of equity assuming D = 0.

4. **Apply Proposition II to calculate the levered cost of equity.**
   - If taxes are zero: r_e,levered = r_u + (r_u − r_d) × (D/E)
   - If corporate taxes apply: use the levered-beta formula:
     β_levered = β_unlevered × [1 + (1 − Tax Rate) × (D/E)]

5. **Calculate the new WACC** under the proposed capital structure.
   - WACC = (E / (D + E)) × r_e + (D / (D + E)) × r_d × (1 − Tax Rate)
   - Under MM without taxes, WACC should be unchanged.
   - Under MM with taxes, WACC falls (because of the tax shield).

6. **Calculate the effect on firm value.**
   - V_firm = Operating Cash Flows / WACC
   - If WACC is constant (MM I, no taxes), firm value is unchanged.
   - If WACC falls (MM with taxes), firm value rises by the present value
     of the tax shield.

7. **Check boundary conditions** (below). If any apply substantially,
   adjust predictions to account for real-world frictions.

8. **Generate the prediction.**
   - What is the change in firm value (if any)?
   - What is the change in cost of equity?
   - Why does MM predict what it does, and where does reality deviate?

## Boundary Conditions

Modigliani-Miller operates under a set of idealized conditions that never
fully hold in practice. The model breaks down or becomes incomplete when:

- **Bankruptcy and financial distress costs are material.** At high leverage,
  the probability of insolvency rises, and the expected costs of
  restructuring, liquidation, and lost operational efficiency offset the
  tax shield. MM does not endogenize these costs, so it predicts 100% debt
  when taxes matter; real optimal leverage is much lower.

- **Agency costs are present.** Debt holders impose covenants and monitoring
  on management; equity holders face different incentives (risk-shifting,
  underinvestment in safe projects). MM assumes perfect alignment; any
  divergence creates value or destroys it depending on the direction. A
  firm with high agency costs benefits from leverage (debt disciplines
  management); a firm with low agency costs is harmed by it.

- **Information asymmetry between management and investors.** If insiders
  know more about the firm's prospects than outsiders, leverage conveys a
  signal (debt is riskier, so management only issues it if confident). MM
  assumes perfect information.

- **The firm's cost of debt depends on leverage.** MM assumes r_d is
  constant; in reality, higher leverage raises the risk premium on debt,
  and eventually debt holders demand much higher rates. This raises WACC
  at high leverage.

- **Market imperfections: taxes are asymmetric, personal income taxes
  matter, or transaction costs are large.** MM's tax result assumes
  corporate tax shields are valuable. If personal income taxes on debt are
  high, the net tax benefit can be small or negative. If transaction costs
  of issuing debt are large, the friction can exceed the tax benefit.

- **Individuals cannot borrow at the firm's borrowing rate.** If this
  assumption fails, the arbitrage mechanism that enforces MM breaks down,
  and leverage can create value through a form of financial intermediation.

## Output Format

```
## Modigliani-Miller Analysis: <firm or decision name>

**Firm / Decision:** <name and context>
**Operating cash flows (EBIT or FCF):** <$ amount or range>
**Current capital structure:** D = $X, E = $Y, D/E = Z%
**Proposed change:** <new D/E ratio or leverage action>

### Unlevered cost of capital
- Business risk (asset beta, or unlevered cost of equity): <X%>
- Unlevered WACC: <Y%>

### Current cost of capital (if leveraged)
- Cost of debt (pre-tax): <X%>
- Cost of equity (levered): <Y%>
- Current WACC: <Z%>

### Proposed capital structure
- New D/E ratio: <X%>
- New cost of equity (Prop II): <Y%>
- New WACC (with/without tax shield): <Z%>

### MM prediction (no taxes)
- Change in firm value: $<amount> or <percent> (should be ~zero)
- Reasoning: <operating cash flows unchanged, WACC unchanged>

### MM prediction (with corporate taxes at X%)
- Present value of tax shield: $<amount>
- Change in firm value: +$<amount>
- New WACC: <Y%>

### Boundary-condition check
- Bankruptcy / distress costs material? <yes/no>
- Agency costs present? <yes/no; if yes, direction of effect>
- Information asymmetry? <yes/no>
- Cost of debt assumed constant? <realistic / unrealistic given leverage>
- Which boundary conditions most constrain the MM prediction?

### Confidence: high | medium | low
<reasoning: stability of operating cash flows + visibility of tax rates +
magnitude of financial distress risk + whether the firm has agency or
information problems that contradict MM assumptions>
```
