---
name: is-lm-ad-as
display_name: IS-LM / AD-AS
class: model
underlying_class: native
domain: economics
source: John Maynard Keynes, *The General Theory of Employment, Interest and Money* (1936); formalized by John Hicks (IS-LM, 1937); later synthesized with classical aggregate supply by economists including James Tobin and others into the AD-AS framework (1960s–1980s)
best_for:
  - Explaining equilibrium output and interest rates given monetary and fiscal policy shocks
  - Predicting how changes in government spending, money supply, or price levels propagate through the economy
  - Identifying whether an economy is demand-constrained or supply-constrained
one_liner: "Aggregate equilibrium where demand meets supply — how policy changes propagate to output and prices."
---

# IS-LM / AD-AS

## Overview

The IS-LM / AD-AS framework claims that **short-to-medium-run macroeconomic equilibrium** is determined by the interaction of goods-market demand (IS), money-market demand and supply (LM), and the aggregate supply of goods (AS). The model is fundamentally explanatory and predictive: it explains why output and prices settle at particular levels given fiscal policy, monetary policy, and supply constraints, and it predicts how shocks propagate. The IS-LM portion (1937) captures demand-side equilibrium; the AD-AS extension (1960s onward) layers in the supply side and price dynamics, allowing prediction of both output and inflation. Unlike classical models that assume full employment, IS-LM / AD-AS treats unemployment and slack demand as equilibrium outcomes when demand is insufficient.

## Core Variables and Relationships

The framework operates across two equilibrium conditions:

**IS (Investment-Savings) equilibrium — goods market:**
- Aggregate demand Y = C + I + G + (X − M), where:
  - C (consumption) = function of disposable income (Y − T), consumer confidence, wealth
  - I (investment) = function of the real interest rate r and expected returns
  - G (government spending) = exogenous policy variable
  - (X − M) = net exports, function of exchange rate and foreign income
- IS slopes downward: higher r → lower I → lower aggregate demand.
- Fiscal expansion (↑G or ↓T) shifts IS rightward → higher Y and r at any given LM position.

**LM (Liquidity-Money) equilibrium — money market:**
- Money supply M (exogenous, set by central bank) = Money demand L(Y, r), where:
  - L depends on transaction demand (proportional to Y) and speculative demand (inversely related to r)
  - Higher Y increases money demand; higher r reduces it (opportunity cost of holding cash)
- LM slopes upward: higher Y → higher money demand → higher r needed to clear the money market.
- Monetary expansion (↑M) shifts LM rightward → lower r, higher Y at any given IS position.

**Macroeconomic equilibrium:**
- Y* and r* are determined where IS and LM intersect.
- If IS ∩ LM lies below full-employment output Y_f, the economy is demand-constrained (Keynesian regime).
- If IS ∩ LM lies at or above Y_f, supply constraints become binding.

**AD (Aggregate Demand) — price-inclusive version:**
- The IS-LM equilibrium traces out a downward-sloping AD curve in (Y, P) space:
  - Higher price level P → lower real money supply M/P → rightward-shifted LM → lower Y.
  - Lower P → higher M/P → leftward-shifted LM → higher Y.

**AS (Aggregate Supply):**
- **Short run (sticky prices):** Aggregate supply is upward-sloping or even horizontal (prices fixed).
  - Production adjusts to meet demand; inflation is muted.
  - Economy moves left/right along a nearly flat AS curve.
- **Long run (flexible prices):** Aggregate supply is vertical at Y_f (full-employment output).
  - Price level adjusts to clear markets; output returns to potential.

**Short-run equilibrium:** Y and P are determined where AD intersects the short-run AS curve.

**Long-run equilibrium:** The economy converges to where AD intersects the vertical long-run AS at Y_f; the price level adjusts to achieve this.

## Key Predictions

- **Keynesian regime (demand-constrained):** A fiscal expansion (↑G) increases Y and r; it "crowds out" some private investment but net effect on output is positive. Monetary expansion lowers r and increases Y. In a liquidity trap (r → 0, LM becomes flat), monetary policy is impotent; only fiscal policy moves Y.

- **Monetary policy is stronger in expanding demand when** the economy is not in a liquidity trap and the LM curve is steep (high interest-rate sensitivity of money demand). Conversely, when LM is flat (low sensitivity), fiscal policy has larger multiplier effects.

- **Stagflation (stagnation + inflation) emerges** when the AS curve shifts leftward (e.g., oil shock, wage shock) while IS-LM equilibrium does not shift. Policymakers then face a trade-off: expanding demand (↑G, ↑M) restores output but worsens inflation; contracting demand fights inflation but deepens recession.

- **Price-wage spirals:** If inflation becomes expected and workers demand higher wages, AS shifts upward (costs rise). If the central bank accommodates by expanding M to prevent output loss, AD shifts right, spiraling prices upward. Non-accommodation trades growth for disinflation.

- **Crowding out:** Large fiscal expansions raise r, reducing private investment (I). If the economy is near full capacity (vertical AS), crowding out is nearly complete — no net output gain. In slack regimes, crowding out is partial.

- **Policy transmission lag:** Monetary policy's effect on Y is lagged (changes in M affect r quickly, but r affects investment and consumption with a lag). Fiscal policy has a shorter lag on demand but longer lags on full multiplier realization through income-consumption feedback.

## Application Procedure

Instantiate the model against a macroeconomic shock or policy question.

1. **Define the initial equilibrium state.** Specify:
   - Current output Y and unemployment rate
   - Current interest rate r and inflation π
   - Is the economy demand-constrained (slack) or supply-constrained (tight)?
   - Estimate the output gap: Y − Y_f (in % of potential)

2. **Identify the shock or policy change.**
   - Monetary: change in M, or shift in money demand (e.g., flight to liquidity)
   - Fiscal: change in G or T
   - Supply: shift in AS (e.g., commodity price shock, productivity change)
   - External: change in exchange rate, foreign demand, or commodity prices

3. **Trace the shock through IS-LM.**
   - Does it shift IS, LM, or both?
   - Direction and magnitude: qualitative (small / medium / large) or quantitative if data exist
   - New IS-LM intersection: higher or lower Y and r?

4. **Layer in AS to predict prices and full output dynamics.**
   - If AS is flat (Keynesian regime with slack), output adjusts; prices change little.
   - If AS is steep (tight labor market, near capacity), price pressure is high; output adjustment is muted.
   - If AS shifts, separate the direct effect on Y from the feedback through AD.

5. **Check for second-order effects:**
   - Does higher Y increase inflation expectations, shifting AS or shifting money demand?
   - Does higher r crowd out investment, reducing future productive capacity and shifting long-run AS?
   - Do external constraints (e.g., balance-of-payments) impose limits on sustainable Y?

6. **Project the medium-run outcome.** If the initial shock creates a positive output gap, inflation will rise, eroding real money supply (M/P), and shifting LM back leftward. The economy will gradually return toward Y_f unless policy adjusts.

7. **Assess policy options.** Which combination of monetary and fiscal policy moves the economy toward the desired outcome (e.g., closing a negative output gap while controlling inflation)?

8. **Check boundary conditions** (below). Note which apply and whether the model's prediction is still reliable.

## Boundary Conditions

IS-LM / AD-AS was designed for **closed or relatively closed economies with sticky prices in the short run** and breaks down or becomes partial when:

- **Open economy with flexible exchange rates:** Capital flows respond to interest-rate differentials, shifting money demand and complicating IS-LM dynamics. A Mundell-Fleming extension is needed to model the interaction of IS-LM with the external balance and exchange rate.

- **Expectations are forward-looking and policy-aware:** If agents anticipate future inflation or policy reversals, the AD-AS curves shift in real time, not passively. New Keynesian / rational expectations models (Lucas critique) are required to avoid systematic policy prediction errors.

- **Supply shocks are large or persistent:** Oil shocks, pandemics, or productivity collapses shift AS dramatically. The model predicts stagflation correctly but offers limited guidance on *resolving* it without the supply-side healing independently. Long-term growth models (Solow, endogenous growth) are needed.

- **Zero lower bound (ZLB) on nominal interest rates:** Below r = 0, conventional IS-LM breaks down. Monetary policy operates through forward guidance, QE (balance-sheet composition), or negative rates (if technically feasible). The model's assumption that r can fall indefinitely is violated.

- **Financial instability or credit crunches:** IS-LM assumes investment demand I responds smoothly to r. When credit markets seize, investment collapses even at low r, or lending itself contracts. Financial accelerator models (Bernanke-Blinder) are needed.

- **Long-run hysteresis:** Extended unemployment or slack can permanently damage productive capacity (skill atrophy, discouraged workers, capital depreciation). The model assumes Y_f is exogenous and stable; hysteresis violates that.

- **Distributional effects:** IS-LM aggregates across households. Changes in the composition of income (wages vs. profits), wealth inequality, or redistribution can shift the consumption function C(Y) in ways the model does not capture.

## Output Format

```
## IS-LM / AD-AS Analysis: <scenario name>

**Initial state:**
- Output Y: <level or % of potential>
- Interest rate r: <level>
- Inflation π: <level>
- Output gap: <Y − Y_f, in %>
- Regime: demand-constrained / supply-constrained

**Shock or policy change:**
- Type: <monetary / fiscal / supply / external>
- Magnitude: <qualitative or quantitative>
- Mechanism: <which curve shifts, direction>

### IS-LM equilibrium path
| Variable | Initial | After shock | Medium-run |
|---|---|---|---|
| Output Y | ... | ... | ... |
| Interest rate r | ... | ... | ... |
| Inflation π | ... | ... | ... |

### Demand and supply dynamics
- AD shift: <direction, mechanism (IS or LM or both)>
- AS position: <flat, upward, or vertical; expectations-adjusted>
- Initial intersection: <output and price outcome>
- Convergence dynamics: <does economy move back toward Y_f; if so, on what timescale>

### Mechanism breakdown
- Crowding out (if fiscal): <magnitude>
- Price-wage spiral risk: <present / absent>
- Liquidity trap / ZLB risk: <present / absent>
- Open-economy spillovers: <present / absent>

### Policy implications
- Monetary response: <appropriate action, if any>
- Fiscal response: <appropriate action, if any>
- Trade-offs: <what is sacrificed to achieve a goal>

### Boundary-condition check
<which boundary conditions apply and whether predictions remain load-bearing>

### Confidence: high | medium | low
<reasoning: stability of initial-state estimates + shock clarity + relevance of boundary conditions>
```
