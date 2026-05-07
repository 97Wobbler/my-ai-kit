---
name: phillips-curve
display_name: Phillips Curve
class: model
underlying_class: native
domain: economics
source: A. W. Phillips, "The Relation between Unemployment and the Rate of Change of Money Wages in the United Kingdom, 1861–1957," Economica, 1958
best_for:
  - Predicting short-run inflation-unemployment trade-offs and the cost of disinflation
  - Explaining why policymakers face a choice between higher inflation with lower unemployment or lower inflation with higher unemployment
  - Diagnosing whether observed wage or price movements are driven by slack in the labor market
one_liner: "Short-run trade-off between unemployment and inflation."
---

# Phillips Curve

## Overview

The Phillips Curve claims that there exists a **stable, inverse relationship between the rate of unemployment and the rate of wage (or price) inflation** in the short run. The core insight is that tight labor markets — where unemployment is low — create upward pressure on wages, which flows through to prices. Conversely, slack labor markets suppress wage growth and inflation. The model is primarily **predictive**: given an unemployment rate, it predicts the inflation rate that will result. It is also **diagnostic**: a deviation from the historical Phillips Curve relationship signals either a structural shift (e.g., a change in inflation expectations or labor market institutions) or a temporary supply shock. The model applies to the medium term (quarters to a few years), not the long run, where the original Phillips Curve relationship breaks down.

## Core Variables and Relationships

1. **Unemployment rate (U)** — the primary exogenous variable driving inflation.
   - Lower U (tighter labor market) → higher wage growth → higher inflation.
   - Higher U (slack labor market) → lower wage growth → lower inflation.
   - The relationship is nonlinear: the effect of a 1 percentage-point drop in U is stronger when U is already very low.

2. **Wage inflation (w)** — the transmission mechanism from labor-market slack to price inflation.
   - When U falls, firms compete for scarce workers and raise wages.
   - When U rises, workers compete for scarce jobs and accept lower wage growth.
   - Wage inflation feeds into price inflation with a lag of 1–4 quarters.

3. **Price inflation (π)** — the observed outcome.
   - π = f(U, expected inflation, supply shocks)
   - In the original Phillips Curve, π is a stable function of U alone.
   - In the expectations-augmented Phillips Curve (Friedman, Phelps 1960s), π depends also on expected inflation (π^e) and supply shocks.

4. **Expected inflation (π^e)** — the shift variable that destabilizes the original Phillips Curve.
   - When agents expect higher inflation, nominal wage demands rise even if U is constant.
   - This shifts the Phillips Curve outward (higher inflation at every unemployment level).
   - Expectations can be backward-looking (driven by recent inflation), forward-looking (based on central bank credibility), or adaptive (adjusting gradually to new data).

5. **Supply shocks (s)** — cost-push pressures independent of labor-market slack.
   - Oil price spikes, import tariffs, productivity shocks, or wage-setting anomalies.
   - A positive supply shock (e.g., OPEC embargo) raises inflation even as U rises, breaking the Phillips Curve temporarily.

6. **Natural rate of unemployment (U*)** — the rate consistent with stable inflation in the long run.
   - Below U*, inflation accelerates (excess demand).
   - Above U*, inflation decelerates (excess supply).
   - U* is not directly observable and shifts over time with demographics, labor-market institutions, and structural change.

**The canonical short-run Phillips Curve:**

    π = π^e + α(U* − U) + s

where α > 0 (a unit decrease in unemployment below the natural rate raises inflation) and s captures supply shocks. When U = U*, inflation equals expected inflation.

## Key Predictions

- **Short-run inflation-unemployment trade-off.** A sustained drop in unemployment from 5% to 4% will result in 0.5–1.5 percentage points of additional inflation within 1–2 years, all else equal. This trade-off is available to policymakers in the short run (quarters to a few years).

- **The expectations-augmented trade-off is steeper and shifts.** If central-bank credibility is low and inflation expectations rise, the entire Phillips Curve shifts outward — the same unemployment level now produces higher inflation. Conversely, anchored expectations flatten the curve.

- **The natural rate is not fixed.** A sustained period of high unemployment (e.g., 2009–2013 in the US) can raise U* through hysteresis — scarring of the labor force, skill depreciation, network loss — so that the Phillips Curve itself shifts inward (lower inflation at every unemployment level).

- **Stagflation (high inflation + high unemployment) occurs when supply shocks dominate.** A negative supply shock (oil shock, wage-price spiral from unanchored expectations) can simultaneously raise inflation and unemployment, breaking the observed Phillips Curve temporarily. The model predicts stagflation will be accompanied by visible supply-side pressures, not demand-side slack.

- **Disinflation is costly in the short run.** Bringing inflation down from 6% to 3% requires unemployment to rise above U* for an extended period. The cost in forgone output is cumulative and nonlinear: if U* is 4.5% but inflation is high, the disinflation requires U to be at, say, 6–7% for 2–3 years. The ratio of cumulative output loss to achieved disinflation is the sacrifice ratio (typically 2–5 in historical data).

- **When the Phillips Curve flattens, the cost of reducing inflation rises, and labor-market tightness matters less for inflation.** A flat Phillips Curve (low α) means disinflation requires much larger increases in unemployment, and small changes in U produce minimal inflation response. This has been the empirical pattern post-2010 in many developed economies.

- **Inflation expectations are a load-bearing variable.** If the central bank is credible and expected inflation is anchored at 2%, the Phillips Curve is more predictable and disinflation costs are lower. If expected inflation is unanchored or drifting, the Phillips Curve is unstable and harder to exploit for policy.

## Application Procedure

Instantiate the Phillips Curve against a concrete labor market and inflation environment.

1. **Define the scope and time horizon.** Which country or region? Over what sample period? (The Phillips Curve relationship has shifted over time, so historical estimates are period-dependent.) Are you forecasting inflation over the next 1–2 years (where the trade-off is most reliable) or the long run?

2. **Estimate or locate the natural rate of unemployment U* for the region and period.** This is the crux: U* is unobservable. Approaches include:
   - NAIRU estimates from central banks (often 4–5% in developed economies, but varies).
   - Backward inference: the unemployment level consistent with stable inflation in recent years.
   - Search for survey evidence on worker inflation expectations; rising expectations suggest U < U*.

3. **Estimate the slope α** — the sensitivity of inflation to unemployment deviations. This requires historical data on π, U, and π^e over the relevant sample period. Typical post-1990 estimates in the US are 0.3–0.8 (a 1 percentage-point drop in U raises inflation by 0.3–0.8 pp).

4. **Assess inflation expectations π^e.** Consult:
   - Central-bank forward guidance and credibility (high credibility anchors expectations).
   - Survey of professional forecasters and household expectations.
   - Market-implied inflation breakevens (5yr-5yr forward inflation swaps, where available).
   - Recent inflation trajectory (backward-looking expectations); if inflation has been rising, π^e may be rising.

5. **Identify supply shocks s.** Are there current or imminent cost-push pressures? Energy prices, supply-chain disruptions, wage-price spirals, import tariffs. Estimate their magnitude if possible (percentage-point impact on inflation).

6. **Compute or read off the predicted inflation:**

    π^forecast = π^e + α(U* − U) + s

   Example: if π^e = 2.0%, U* = 4.5%, U = 3.5%, α = 0.5, and s = 0.3% (supply shock), then π ≈ 2.0 + 0.5(1.0) + 0.3 = 2.8%.

7. **Check boundary conditions** (see below). If any apply strongly, note that the Phillips Curve forecast is incomplete and flag what additional analysis is needed.

8. **Generate the prediction and confidence assessment.** State the predicted inflation rate, the lead time (1 year, 2 years), and the primary driver(s) — demand-side (unemployment gap), expectations, or supply shocks. Include explicit confidence.

## Boundary Conditions

The Phillips Curve is a reliable short-run forecasting device under specific conditions and breaks down or becomes partial under others:

- **Low and stable inflation environment (< 5% baseline).** The Phillips Curve relationship is most reliable when inflation is low and inflation expectations are anchored. In high-inflation or hyperinflationary regimes (>10% inflation), behavioral and institutional shifts (dollarization, frequent price indexation, wage spirals) dominate and the Phillips Curve becomes uninformative.

- **The flattening Phillips Curve (post-2010 in many developed economies).** Since the global financial crisis, the empirical Phillips Curve relationship has weakened in the US, euro area, and UK: unemployment has fallen dramatically, but inflation has remained subdued or risen less than the historical relationship would predict. Causes include anchored expectations, globalization, changes in labor bargaining power, or measurement issues (gig economy, quality adjustment). If α is near zero, the model loses predictive power.

- **Structural breaks and regime shifts.** A change in central-bank credibility, monetary-policy framework, or labor-market institutions (e.g., unionization decline, shift to gig work, immigration policy) can shift U* or α. Historical estimates become invalid. The model predicts based on a stable α; if α is changing, forecasts fail.

- **Hysteresis and duration of slack.** Persistent unemployment can raise U* through worker scarring and skill loss. In that case, the Phillips Curve itself shifts inward, and the forecaster must estimate the shift — the model does not do that automatically.

- **Supply-side dominance.** When supply shocks are large and volatile (e.g., oil embargoes, pandemic supply-chain collapses, major tariff changes), the Phillips Curve becomes noisy. The model assumes s is small or predictable; if s is large and variable, inflation is driven more by supply than demand, and the unemployment-inflation trade-off is broken.

- **Long-run analysis.** The Phillips Curve applies to the short and medium run (quarters to 2–3 years). In the long run, the relationship disappears: inflation is determined by monetary policy and inflation expectations, not the unemployment rate. The long-run Phillips Curve is vertical at U*.

## Output Format

```
## Phillips Curve Analysis: <country/region, time horizon>

**Scope:** <country, time period, forecast horizon (e.g., 12 months ahead)>
**Date of analysis:** <date>

### Key parameters
| Parameter | Value | Source / Note |
|---|---|---|
| Natural rate U* | <X%> | <NAIRU estimate or derived from recent stable inflation> |
| Current unemployment U | <Y%> | <latest data> |
| Unemployment gap (U* − U) | <Z pp> | <positive = tight, negative = slack> |
| Phillips Curve slope α | <coefficient> | <historical regression or range> |
| Expected inflation π^e | <X%> | <survey forecasts, central bank target, recent trajectory> |
| Supply shock s | <±X pp> | <visible pressures: energy, supply chain, wage dynamics> |

### Components of predicted inflation
| Component | Value | Driver |
|---|---|---|
| Expected inflation | <π^e%> | <anchored / unanchored / rising> |
| Demand-side (demand shock) | <α(U*−U) pp> | <unemployment gap × slope> |
| Supply shock | <s pp> | <observed or estimated cost pressures> |
| **Total predicted inflation** | **<π%>** | **<sum>** |

### Prediction
- **Predicted inflation (12 months / 24 months ahead):** <X% ± confidence band>
- **Primary driver:** <demand slack / tight labor market / supply shock / expectations drift>
- **Key assumption:** <most load-bearing assumption in the forecast>

### Risks and shifts
- **Upside risk:** <what could raise inflation more than predicted; e.g., further unemployment decline, upward shift in U*, unanchoring of expectations>
- **Downside risk:** <what could keep inflation lower; e.g., structural flattening of the curve, hysteresis, deflationary supply shock>

### Boundary-condition check
<which of the boundary conditions apply (if any) and whether the forecast is still valid under them>

### Confidence: high | medium | low
<reasoning: stability of α over the sample period + anchoring of expectations + visibility and magnitude of supply shocks + fit to historical Phillips Curve relationship in the current regime>
```
---
