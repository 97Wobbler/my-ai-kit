---
name: efficient-market-hypothesis
display_name: Efficient Market Hypothesis
class: model
underlying_class: native
domain: economics
source: Eugene F. Fama, "Efficient Capital Markets: A Review of Theory and Empirical Work," Journal of Finance, 1970; refined in "Efficient Markets Revisited," Financial Analysts Journal, 2023
best_for:
  - Predicting whether prices in a market reflect all available information
  - Explaining why active management persistently underperforms passive indices
  - Identifying what type of information asymmetry could support a trading edge
one_liner: "The possibility of excess returns depends on how quickly and fully markets reflect information."
---

# Efficient Market Hypothesis

## Overview

The Efficient Market Hypothesis (EMH) claims that asset prices fully and instantly reflect all available information relevant to valuation, and therefore it is impossible to consistently earn excess returns by trading on that information. The model comes in three forms of increasing informational completeness: weak form (prices reflect historical prices and returns only), semi-strong form (prices reflect all publicly available information), and strong form (prices reflect all information, including insider information). The theory is predictive: it says that if a market is efficient at a given level, certain kinds of trading strategies will and will not work. It does not claim markets are always perfectly efficient — efficiency is a question of degree and varies by market, time, and information type.

## Core Variables and Relationships

The informational efficiency of a market is determined by:

1. **Information arrival rate and distribution**
   - How often new information becomes available
   - How symmetrically distributed is access to that information
   - How quickly information is disseminated (speed of distribution)

2. **Market participant sophistication and capital availability**
   - Number and skill level of traders and analysts competing to exploit mispricings
   - Amount of capital available to arbitrageurs
   - Presence of institutional vs. retail traders
   - Incentive structures (fees, performance pressure) that reward information-hunting

3. **Barriers to arbitrage and trading costs**
   - Transaction costs (commissions, spreads, taxes)
   - Borrowing costs for short selling
   - Liquidity constraints (size of trades relative to market volume)
   - Regulatory or legal restrictions on certain trades
   - Time to execution and information decay

4. **Feedback mechanisms and price discovery**
   - Speed at which traders act on information
   - Mechanism for price corrections (order flow, market makers)
   - Presence of noise traders or irrational actors who resist correction
   - Correlation structure among traders' beliefs (herding vs. independent opinion)

The central relationship: **Price = Expected value conditional on all available information (at the relevant form of efficiency)**. If a piece of information is incorporated into prices, the expected return from trading on it should be zero (adjusted for risk and transaction costs). Conversely, if you observe persistent excess returns from a strategy, either (a) the market is not fully efficient at that information type, or (b) the strategy is capturing a systematic risk premium, not beating the market.

## Key Predictions

- **Under semi-strong efficiency, active management fees will exceed the edge gained from public information.**  Managers compete on the same public data; unless they have superior analysis, the average manager earns less than a passive index fund after fees. This predicts that most actively managed funds underperform their benchmark.

- **Under weak efficiency, technical trading (relying on historical price patterns alone) will not produce excess returns after costs.** Any pattern in prices that can be detected algorithmically will be arbitraged away. Predictable chart patterns should not exist.

- **The existence of a profitable strategy implies the market was not efficient with respect to the information the strategy exploited.** If someone persistently beats a market on a given information set, that information is not yet fully priced. The discovery of such a strategy and its publicity will tend to erode its future profitability (as others copy it).

- **Prices should follow a random walk conditional on information arrival.** The unpredictable component of price changes should be orthogonal to past price data (weak form) or past public information (semi-strong form). Autocorrelation in returns should be zero or insignificant.

- **Anomalies (small-cap effect, value effect, momentum) signal either market inefficiency or missing risk factors.** If returns are predictable from firm characteristics or past returns, either the market has not priced them correctly (inefficiency) or those characteristics proxy for systematic risk that the standard model (CAPM) misses.

- **Insider trading laws and disclosure rules improve semi-strong efficiency by reducing the information advantage available to insiders.** Without such rules, insiders could profit reliably; with them, their edge shrinks toward zero.

## Application Procedure

Instantiate EMH to evaluate whether a given market or trading strategy reflects market efficiency, and at what level.

1. **Define the market and asset class precisely.** Which security or market are you analyzing? (e.g., "US large-cap equities" vs. "penny stocks" vs. "emerging-market bonds"). Different assets may have different efficiency levels.

2. **Choose the form of efficiency you are testing:** weak, semi-strong, or strong. This is your null hypothesis.
   - **Weak:** Does price data alone predict future returns?
   - **Semi-strong:** Can you beat the market using publicly available information?
   - **Strong:** Can you beat the market even with insider information?

3. **Identify the information set at stake.** What specific information or pattern are you claiming the market has missed, or how are you claiming to profit?
   - Historical prices and returns (weak test)?
   - Publicly available financial statements, news, analyst reports (semi-strong)?
   - Insider knowledge (strong)?

4. **Map the market's arbitrage capacity.** Can the misprice actually be exploited?
   - What are trading costs (bid-ask spread, commissions, taxes)?
   - How much capital can you deploy without moving the price?
   - How long do you need to hold to realize the edge?
   - Can you short the overpriced or borrow the underpriced at reasonable cost?

5. **Look for evidence of the information's incorporation into prices.**
   - Is the information already priced in? (Quick price reaction upon public announcement)
   - Is there a measurable lag in price adjustment?
   - Do informed traders (insiders, sophisticated investors) act before the information is public?

6. **Test the strategy's alpha after costs.** Does the strategy beat the benchmark after transaction costs, taxes, and fees? 
   - Backtesting on historical data often overestimates due to survivorship bias and data snooping.
   - Forward testing (walk-forward, paper trading) is more reliable.

7. **Check whether returns are explained by risk, not inefficiency.** Use a multi-factor model (CAPM, Fama-French) to see if the "excess" return is actually a risk premium for factors you have not controlled.

8. **Check boundary conditions** (below). If any strongly apply, EMH predictions weaken.

## Boundary Conditions

EMH assumes rational traders with sufficient capital competing away mispricings, and it breaks down or becomes partial under these conditions:

- **Limits to arbitrage are severe.** If the mispriced asset is illiquid (small float, low volume, high transaction costs), or if short selling is restricted, arbitrageurs may not have enough capital or access to correct the price, allowing the misprice to persist. (Example: microcap or emerging-market equities.)

- **Irrational traders have deep pockets and stable beliefs.** If noise traders or trend-followers have enough capital and their irrationality is not quickly stamped out, they can move prices away from fundamentals. This is especially true if they systematically bet in the same direction (herding, momentum chasing). EMH prediction weakens; pricing may not be determined by fundamentals.

- **The information is ambiguous or not easily quantifiable.** If no clear model links information to valuation (e.g., implications of a regulatory change, or the value of a novel technology), traders disagree on priors, and prices may be slow to adjust. Semi-strong efficiency is weaker for soft or novel information.

- **Disclosure or dissemination of information is slow or patchy.** If information diffuses to some traders before others, the semi-strong form is violated. Insider trading, dark pools, and fast-access networks can create delays in semi-strong efficiency.

- **Correlated beliefs or systematic bias among market participants.** If traders have systematic biases (overconfidence in growth, undervaluation of risk, behavioral momentum), and those biases are persistent, they can lock in prices away from the efficient level. This is especially true in sentiment-driven markets (cryptocurrencies, SPACs, meme stocks).

- **Structural breaks or regime changes.** EMH assumes the relationship between information and valuation is stable. In periods of structural change (technological disruption, regulatory overhaul, financial crisis), the model's past calibration breaks, and observed "anomalies" may reflect a shifted regime rather than persistent inefficiency.

## Output Format

```
## EMH Analysis: <market/asset and strategy under test>

**Market scope:** <asset class, geography, time period>
**Form of efficiency tested:** weak | semi-strong | strong
**Null hypothesis:** Market is efficient at the [form] level

### Information set and trading mechanism
| Information type | Public? | Arrival lag | Arbitrage cost | Notes |
|---|---|---|---|---|
| <e.g., earnings announcement> | Yes/No | <days/hours/seconds> | <% of expected return> | ... |

### Alpha calculation
- Strategy return (gross): <% annualized>
- Benchmark return: <% annualized>
- Transaction costs: <% per year>
- Risk-adjusted return (Fama-French alpha or CAPM alpha): <% annualized>
- Statistical significance: <t-stat, p-value, or "not significant">

### Information incorporation check
- Speed of price reaction post-announcement: <immediate / <1 min / >1 day / no clear lag>
- Evidence of informed trading before public dissemination: <yes / no / unclear>
- Degree of misprice correction over test period: <full / partial / persistent>

### Arbitrage capacity
- Market liquidity (average daily volume): <$Xmm>
- Bid-ask spread or trading cost as % of expected return: <%>
- Short-sale or financing cost: <% annualized>
- Binding constraint on arbitrage: <none / liquidity / costs / leverage / regulatory>

### Prediction
- EMH prediction: <strategy should / should not beat the benchmark after costs>
- Observed result: <does / does not beat>
- Interpretation: <supports efficiency / contradicts efficiency / inconclusive>
- If inefficient: most likely driver (irrational traders / slow information dissemination / limits to arbitrage / risk factor?)

### Boundary-condition check
<which of the above conditions apply, and how do they impact confidence in the EMH prediction>

### Confidence: high | medium | low
<reasoning: data quality and time-span of test + severity of boundary-condition violations + alternative explanations (e.g., missing risk factor) not yet ruled out>
```
