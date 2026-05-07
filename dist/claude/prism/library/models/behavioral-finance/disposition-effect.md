---
name: disposition-effect
display_name: Disposition Effect (Shefrin-Statman)
class: model
underlying_class: native
domain: behavioral-finance
source: "Hersh Shefrin & Meir Statman, \"The Disposition to Sell Winners Too Early and Hold Losers Too Long: Theory and Evidence,\" Journal of Finance, 1985"
best_for:
  - Predicting when investors will realize gains or losses in their portfolios
  - Explaining systematic trading patterns and portfolio turnover that deviate from tax-loss harvesting and rebalancing logic
  - Understanding why market rallies may see excess volume (forced selling of winners) and recoveries face resistance (reluctance to realize losses)
one_liner: "Predict portfolio trading patterns via loss aversion and mental accounting: investors overweight recent gains and losses relative to fundamental value."
---

# Disposition Effect (Shefrin-Statman)

## Overview

The Disposition Effect claims that investors have a systematic bias in the **timing and direction of their trades**: they sell securities that have gained in value (winners) too early and hold securities that have lost in value (losers) too long before liquidating. The mechanism is loss aversion, combined with mental accounting that treats each position as a separate decision rather than integrating it into total portfolio risk. The model is both descriptive and predictive — it explains *why* observed trading behavior deviates from rational models (which would optimize to tax harvesting and rebalancing), and it predicts which positions will be sold first and which will be held or added to. Prospect Theory supplies the psychological foundation: gains and losses are evaluated relative to a reference point (purchase price), losses hurt ~2× as much as equivalent gains feel good, and this asymmetry distorts the decision to realize or defer.

## Core Variables and Relationships

1. **Position gain/loss relative to purchase price (reference point).**
   - A security with an unrealized gain is in the **gain domain** (current price > entry price).
   - A security with an unrealized loss is in the **loss domain** (current price < entry price).
   - The reference point r is the purchase price; outcomes are measured as (current price − r).
   - Larger gains or losses (in absolute terms) increase the emotional weight of the decision.

2. **Loss aversion coefficient λ ≈ 2–2.5.** Losses hurt roughly 2–2.5× as much as equivalent gains feel good. Applied here: the pain of realizing a $1,000 loss outweighs the pleasure of realizing a $1,000 gain.

3. **Prospect Theory value function.** The perceived value of selling a position is:
   - **In the gain domain:** diminishing sensitivity (utility gain is concave). Selling a +$500 position feels good, but the marginal appeal of selling a +$5,000 position (vs. holding) is lower.
   - **In the loss domain:** diminishing sensitivity is convex. The investor is motivated to "break even" or defer the loss to avoid realizing the pain.

4. **Mental accounting / position isolation.** Each position is mentally partitioned and evaluated independently of total portfolio return, taxes, and risk diversification. This isolation locks the reference point at the purchase price and prevents investors from asking "should I hold this for portfolio reasons?" Instead, the question becomes "do I want to lock in this gain or loss?"

5. **Regret aversion and "getting even."** Investors in the loss domain experience regret and harbor an implicit goal of riding the losers back to break-even. This creates a reluctance to sell — selling would make the loss "real" and is emotionally coded as giving up on redemption.

6. **Realization utility.** The act of selling a winner in the gain domain triggers immediate satisfaction (realizing the gain), while selling a loser in the loss domain triggers immediate pain (realizing the loss). This asymmetry biases the timing of sales.

The combined effect: **probability of sale = f(gain/loss, magnitude, isolation, λ).** Positions in the gain domain are more likely to be sold; positions in the loss domain are more likely to be held (until either regret fades, forced liquidation occurs, or the position bounces back).

## Key Predictions

- **High turnover in winning positions; low turnover in losing positions.** A portfolio with many winners will show excess realized gains and low realized losses, distorting the realized-gains/realized-losses ratio to above 1 (often 1.5–2.0) — exactly the opposite of what a rational, tax-conscious investor would do.

- **Sell-off clustering in rallies.** During strong market rallies, the number of positions in the gain domain rises sharply. Loss aversion pushes investors to "harvest" gains quickly, creating excess selling volume. This creates a contrarian signal (heavy selling at the top) that efficient-market theory cannot easily explain.

- **Momentum resistance in recoveries.** During rebounds from a drawdown, investors in the loss domain hold firm rather than add to recovering positions, because they have not yet broken even. Only once a position's price crosses the entry price do they regain appetite to hold or buy. This creates a "stickiness" in the price recovery around the entry level.

- **Position concentration in losses.** Portfolios contain a long tail of small, underwater positions held for psychological reasons. These positions are diversification dead weight.

- **Taxes are left on the table.** Investors realize large capital gains and small capital losses, rather than the tax-efficient strategy of realizing losses first (to offset gains). Over a year, this can cost 1–3% in after-tax returns.

- **Volatility of realized gains is correlated with asset price momentum, not fundamental factors.** High realized gains during rallies reflect disposition effect, not changes in fundamentals. This creates a lagged, trend-chasing pattern in which transactions are concentrated at prices that are already extreme.

## Application Procedure

Instantiate the model against a concrete investor portfolio or market segment to predict trading behavior.

1. **Define the investor or cohort.** Who is the decision maker? Is this a retail investor, a mutual fund, a hedge fund? (The Disposition Effect is strongest in retail; weaker in institutional investors with explicit rebalancing rules.)

2. **Segment the portfolio into positions.**
   - For each position, compute the unrealized gain/loss: current price − entry price (or average cost basis).
   - Classify as **gain domain** or **loss domain**.
   - Note the magnitude (as % of entry price or absolute $).

3. **Estimate the reference point for each position.** In standard cases, this is the purchase price. If the investor has had multiple tranches, use the blended entry price (or most recent if mental accounting is narrow).

4. **Apply loss aversion and realization utility.** For each position:
   - **Gain domain:** Estimate the probability it will be sold in the next period. Larger gains → higher sale probability (concave utility, so gains feel "cashed in").
   - **Loss domain:** Estimate the probability it will be sold. Expected to be low unless forced (margin call, liquidity need, or the position bounces back to break-even, triggering a mental transition).

5. **Predict realized gain/loss flows.**
   - Sum up the gains likely to be realized (from positions in gain domain, high-magnitude winners).
   - Sum up the losses likely to be realized (from positions in loss domain that are forced to sell or have waited too long).
   - Compute the realized-gain-to-realized-loss ratio.
   - Compare to the underlying buy-and-hold portfolio: is the ratio distorted toward excess gains?

6. **Check temporal context.** 
   - Is the market in a rally or a drawdown? Rallies increase the number of positions in gain domain, boosting realized gains.
   - Is year-end approaching? Tax-loss harvesting may artificially increase realized losses in a narrow window.
   - Are there forced redemptions or liquidity events? These override disposition bias.

7. **Assess tax impact.**
   - Compute the tax drag from realizing gains before losses.
   - Is the investor in a high tax bracket (amplifying the cost of selling winners early)?

## Boundary Conditions

The Disposition Effect is strongest in individual retail investors and weakens or disappears under several conditions:

- **Institutional or professional investors with explicit rebalancing algorithms.** Funds with rules-based selling discipline (e.g., "sell when position exceeds 5% of AUM") override the psychological bias. The effect is much weaker in mutual funds and hedge funds than in retail portfolios.

- **High-frequency or algorithmic trading.** Systematic traders evaluate positions on statistical or technical grounds, not reference prices. The reference point is not the entry price; it is the model's signal.

- **Positions with embedded derivatives or complex tax structures.** If a position is hedged or tax-loss-harvesting is automated, mental accounting may not lock onto the entry price.

- **Extreme losses approaching zero or total wipeout.** Once a loss is so large (>80%) that the probability of "getting even" is negligible, investors may sell earlier than the model predicts. The reference point shifts from "break-even" to "minimizing further damage."

- **Distributed holding periods across a cohort.** If entry prices vary widely across the same security (common in index funds or dividend reinvestment plans), aggregated behavior averages out the reference-point effect. The model is strongest when cohort entry prices are clustered.

- **Markets with continuous feedback (mark-to-market, daily rebalancing).** In stable portfolios reviewed infrequently, mental accounting is stronger; in actively managed or marked-to-market portfolios, the disposition effect is smaller (positions are re-evaluated more often and the reference point may drift).

- **Behavioral-finance literacy or prior experience with tax optimization.** Investors who have learned the cost of the disposition effect can partially override it; this is rare in retail but increasingly common in wealthy cohorts.

## Output Format

```
## Disposition Effect Analysis: <investor / portfolio / market segment>

**Subject:** <retail investor, mutual fund, hedge fund, market cohort>
**Portfolio size:** <if relevant>
**Observation period:** <date range>
**Reference point:** <typically purchase/entry price; note any exceptions>

### Position inventory (gain/loss domain)
| Position / Ticker | Entry price | Current price | Gain/Loss $ | Gain/Loss % | Domain | Magnitude |
|---|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | Gain / Loss | H/M/L |

### Disposition Effect predictions
- **Probability of sale (next period), by position:**
  | Position | Domain | Loss-aversion weight | Predicted sale probability |
  |---|---|---|---|
  | ... | Gain/Loss | High / Low | % |

- **Aggregate realized gain/loss forecast:**
  - Expected realized gains: $X
  - Expected realized losses: $Y
  - Ratio of realized gains to realized losses: X/Y (compare to 1.0 as baseline)

- **Tax drag (if applicable):**
  - Estimated after-tax underperformance vs. optimal harvesting: X% annually

### Drivers of the effect in this portfolio
- **Largest winners (high sale probability):** <list top 3 positions by magnitude, explain why they are at risk of early sale>
- **Longest-held losers (low sale probability):** <list bottom 3 positions, explain why they are sticky>
- **Market context:** <rally / drawdown / stagnation — does this amplify or dampen the effect?>

### Boundary-condition check
- **Investor type:** Does this investor have rules or algorithms that override the bias? (high/low override risk)
- **Forced liquidations or liquidity events on horizon?** (yes/no — if yes, may override disposition bias)
- **Tax constraints or harvesting rules already in place?** (yes/no)

### Confidence: high | medium | low
<reasoning: clarity of entry prices + investor type (retail stronger signal than institutional) + data freshness + whether forced sales are imminent + tax situation complexity>
```
