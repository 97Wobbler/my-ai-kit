---
name: margin-of-safety
display_name: Margin of Safety
class: heuristic
underlying_class: native
domain: finance
source: Benjamin Graham, The Intelligent Investor, 1949
best_for:
  - valuation and buy/sell decisions
  - risk management in equity analysis
  - portfolio construction
one_liner: "Do not buy without sufficient discount to intrinsic value."
---

# Margin of Safety

## The Rule
Never buy a security unless it is trading at a material discount to your estimate of its intrinsic value, and the size of that discount should reflect the uncertainty in your valuation.

## When It Applies
- Evaluating whether a stock is cheap enough to buy given estimation error in the valuation model.
- Deciding between two stocks with similar fundamentals but different trading prices relative to estimated intrinsic value.
- Assessing downside protection if your valuation assumption turns out to be wrong by 20%, 30%, or 50%.
- Setting portfolio allocation: larger positions warrant larger margins of safety because conviction compounds risk.

## When It Misleads
- In growth or momentum markets where the highest-returning stocks trade at no discount to intrinsic value, or at a premium, for years. Waiting for a margin of safety can mean sitting out the entire move.
- When intrinsic value itself is unknowable (early-stage companies, platforms, or network-effect businesses with no clear cash flow pattern). A large margin of safety on a number you guessed is false comfort.
- In mean-reversion situations where valuation is sticky: a stock trading at 2× book value may be fairly valued if the business has structurally shifted. A margin of safety only protects against *estimation error*, not against misidentified structural change.
- When applied mechanically without assessing the *source* of the discount — a stock may be cheap for good reason (deteriorating moat, lost competitive position).

## Common Misuse
Using margin of safety as a substitute for conviction analysis. "It's trading at 50% of intrinsic value so it's safe" mistakes a discount for a thesis. The heuristic assumes your intrinsic value estimate is sound; if it is not, a large margin does not save you.

Treating margin of safety as a fixed percentage (e.g., "always require 30% discount") rather than scaling with uncertainty. High-certainty businesses (utilities, mature consumer staples) can justify smaller margins; nascent or cyclical businesses need larger ones.

## How Agents Use It
- **Embedded**: in a valuation lens, after the intrinsic value estimate is complete, as a check step before a buy/sell recommendation. The agent should state the estimated intrinsic value, the current price, the resulting margin or premium, and whether that margin matches the confidence level of the valuation.
- **Sanity-gate**: on each investment recommendation, ask: "What is the margin of safety, and does it scale appropriately with the estimation uncertainty in this valuation?" If margin is thin or negative, or if the valuation confidence is low but margin is also low, flag the finding for further review before synthesis.
