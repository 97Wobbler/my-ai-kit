---
name: auction-theory
display_name: Auction Theory
class: model
underlying_class: native
domain: game-theory
source: William Vickrey, "Counterspeculation, Auctions, and Competitive Sealed Bids," Journal of Finance, 1961; extended by Klemperer, McAfee, and others
best_for:
  - Predicting equilibrium bidding behavior and revenue across different auction formats
  - Explaining why sealed-bid second-price auctions induce truthful bidding
  - Comparing efficiency and revenue properties of first-price, second-price, and English auctions
one_liner: "Equilibrium strategies and revenue differences across auction formats — truth-telling, revenue equivalence, efficiency."
---

# Auction Theory

## Overview

Auction Theory models how bidders behave when competing for a good of uncertain or heterogeneous value, and predicts the equilibrium outcome (bids, allocation, revenue) under different auction rules. The central claim is that the auction format — the rules governing bidding, information revelation, and payment — fundamentally shapes equilibrium behavior and the resulting allocation and seller revenue, even when the underlying bidders and valuations are identical. The theory is predictive: it derives what rational bidders *will* do under each format, given strategic incentives. It is also normative: it shows which formats maximize seller revenue or allocative efficiency under different conditions. Applying it requires instantiating bidder valuations and the auction format against the procedure below.

## Core Variables and Relationships

**Primitives:**
- **Number of bidders (n):** affects competitiveness and the gap between first and second highest valuation.
- **Valuation distribution:** each bidder i has a private valuation v_i for the item. Valuations may be i.i.d. (symmetric) or asymmetric; may be known only to the bidder (private value) or partly common knowledge (common value). The distribution's support and dispersion matter for the gap between winning and losing bids.
- **Information structure:** do bidders know their own valuation only, or do they also observe (or infer) others' valuations or the seller's reserve price?

**Four canonical auction formats and their equilibrium properties:**

1. **English (ascending-price, open-outcry) auction**
   - Rule: price rises; bidders drop out when price exceeds their willingness to pay. Last remaining bidder wins at the price where the second-to-last bidder dropped.
   - Equilibrium: bidders drop out when the current price equals their own valuation. The winner pays (approximately) the second-highest valuation.
   - Revenue consequence: English ≈ second-price sealed-bid in expected revenue.
   - Efficiency: allocatively efficient (highest-valuation bidder wins).

2. **First-price sealed-bid auction**
   - Rule: bidders submit sealed bids; highest bidder wins and pays their own bid.
   - Equilibrium: bidders shade their bids below their true valuation. The amount of shading increases with n (more competition ⟹ less shading) and with the gap between their own valuation and the next-highest competitor's.
   - Formal: in symmetric equilibrium with i.i.d. valuations, the bid function b(v) is strictly increasing and b(v) < v for all v.
   - Revenue consequence: first-price and English auctions often yield similar (or identical in some models) expected revenue.
   - Efficiency: allocatively efficient (highest-valuation bidder wins, but the amount of overbidding risk is different).

3. **Second-price sealed-bid (Vickrey) auction**
   - Rule: bidders submit sealed bids; highest bidder wins and pays the *second-highest* bid.
   - Equilibrium: bidding your true valuation is a weakly dominant strategy. No shading occurs.
   - Formal: b(v) = v for all v is the unique symmetric equilibrium.
   - Revenue consequence: expected price = expected second-highest valuation, independent of the winner's valuation.
   - Efficiency: allocatively efficient and also truthful-revelation efficient (no one has an incentive to misreport).

4. **Dutch (descending-price) auction**
   - Rule: price falls from high to low; first bidder to call wins at the current price.
   - Equilibrium: strategically equivalent to first-price sealed-bid (a bidder's optimal stopping price is the bid they would submit in first-price, given their beliefs about others' valuations).
   - Revenue consequence: Dutch ≈ first-price.

**Revenue equivalence and bid-shading dynamics:**
- Under symmetric, independent private values and risk-neutral bidders, expected revenue is the same across all four formats: **Revenue Equivalence Theorem** (Myerson, Riley).
- The difference lies in the distribution: second-price concentrates on the second-highest valuation; first-price is more dispersed because the winner shades by varying amounts.
- Bid shading in first-price = (number of competitors − 1) / (number of competitors). As n → ∞, shading → 0; as n → 1, shading → 0 (monopoly). Maximum shading at intermediate n.

## Key Predictions

- **Second-price auctions induce truthful bidding.** Rational bidders will submit their true valuation in a sealed-bid second-price auction, even without communication, reputation, or legal enforcement. Deviation (overbidding or underbidding) strictly reduces expected payoff.

- **First-price auctions produce less revenue at the margin than bidders' willingness to pay.** The gap between the winner's bid and their true valuation is larger when there are few competitors and when valuations are highly dispersed. With many bidders, shading shrinks because the competition is fierce.

- **English auctions reveal information incrementally,** making them vulnerable to winner's curse in common-value settings (oil leases, art with resale uncertainty). Second-price and Dutch auctions do not reveal live price signals, so bidders must form independent assessments.

- **The identity of the winner is the same across all four formats** (highest-valuation bidder wins in equilibrium), but the payment differs, producing different revenue consequences when you account for risk aversion, bidder heterogeneity, or asymmetric information.

- **Reserve prices (minimum acceptable bid) increase expected revenue** in all formats by excluding low-valuation scenarios, even if they sometimes eliminate the winner entirely. The optimal reserve equals the seller's own valuation (if the seller is risk-neutral and can credibly commit).

- **Collusion among bidders destroys revenue.** If bidders can coordinate, they can reduce bids below the competitive equilibrium (cartelize the auction). Second-price and English formats are somewhat more vulnerable because truthful/drop-out bidding is detectable; first-price collusion is harder to police.

## Application Procedure

Instantiate the model against a concrete auction or bidding scenario.

1. **Define the auction context precisely.** What is the object? Who are the bidders? Is valuation private (each bidder knows only their own) or common (the item's true value is the same for all, but knowledge is asymmetric)? What is the time horizon (one-shot or repeated)?

2. **Identify the auction format.** English, first-price sealed-bid, second-price sealed-bid, Dutch, or a hybrid? Write the rules explicitly (e.g., "ascending-price English with a $100 reserve, no overbidding allowed, open book on all bids").

3. **Characterize the bidder population.**
   - How many bidders?
   - Are valuations symmetric (all bidders draw from the same distribution) or asymmetric (e.g., one incumbent, several entrants)?
   - What is the distribution of valuations? (e.g., uniform on [0, 100], log-normal, discrete values known from prior data).

4. **Identify the information structure.**
   - Do bidders know only their own valuation, or do they also observe a public signal (e.g., an independent appraiser's estimate)?
   - Is this private-value (each bidder's value is independent) or common-value (there is an underlying true value, but bidders have noisy signals)?

5. **Derive or estimate the equilibrium bid function for the format.**
   - Second-price: bid your valuation.
   - First-price: apply bid-shading formula; shade by approximately (n−1)/n if using the uniform-distribution shortcut.
   - English: bidders drop out at their valuation.
   - Dutch: bidders stop at the first-price equivalent.

6. **Predict the allocation and expected revenue.**
   - Allocation: highest-valuation bidder wins.
   - Expected revenue: depends on the format (second-price pays second-highest; first-price pays (n−1)/n times average winning valuation, approximately).
   - If you have data on prior valuations, calculate the expected gap between first and second highest.

7. **Check boundary conditions** (below). If any apply, flag that the standard theory may not predict behavior accurately.

8. **Generate the prediction:**
   - Expected winning bid and final payment.
   - Expected seller revenue.
   - Which bidder wins and by what margin.
   - How behavior would change if the format were switched.

## Boundary Conditions

Standard Auction Theory (symmetric, independent private values, risk-neutral bidders) breaks down or becomes partial under several conditions:

- **Common-value auctions (winner's curse).** When the item's true value is the same for all bidders but each has only a noisy signal (e.g., offshore oil lease, a company being acquired), the highest bidder is often the one who was most optimistic, and that optimism is likely to be wrong. Observed bids are systematically below the theoretical prediction, and the winner often regrets the purchase. Second-price does not eliminate this; English is most vulnerable because the live price revelation updates everyone's estimates.

- **Asymmetric bidders.** When bidders have systematically different valuations (e.g., an incumbent with a cost advantage, or a bidder with deep pockets), the equilibrium bid function is no longer a simple function of valuation. The lower-valuation bidder may shade more or exit earlier. Predict using asymmetric equilibrium models (e.g., Maskin & Riley) or numerical methods.

- **Risk-averse bidders.** Risk aversion reduces bid shading in first-price auctions (the bidder wants to increase their win probability) and can flip revenue rankings. Use a utility function u(x) reflecting risk aversion and re-solve for equilibrium.

- **Interdependent or relational valuations.** If one bidder's value depends on whether another bidder also wins (synergies, network effects, or spite), the valuation function is no longer separable. Standard theory does not apply; use models of package bidding or interdependent-value auctions.

- **Collusion or entry deterrence.** If bidders can communicate before the auction or if the seller can screen entrants, collusive equilibria and signaling equilibria exist that are not captured by the competitive baseline. Empirically, sealed-bid formats are somewhat harder to collude in than open English.

- **Behavioral and cognitive limits.** Bidders may not solve the equilibrium bid-shading formula. They may anchor on the ask price, the previous price (if repeated), or other salience cues. In practice, bid functions are often less smooth and more dispersed than theory predicts.

## Output Format

```
## Auction Theory Analysis: <auction name / context>

**Auction format:** <English / first-price sealed / second-price sealed / Dutch / other>
**Number of bidders:** <n>
**Valuation type:** <private-value / common-value>
**Bidder symmetry:** <symmetric / asymmetric — describe if asymmetric>

### Valuation profile
| Bidder | Estimated valuation | Signal / basis | Notes |
|---|---|---|---|
| ... | ... | ... | ... |

### Equilibrium predictions
- **Format:** <name>
- **Bid function:** <"bid true valuation" for second-price; "shade by (n−1)/n" for first-price; etc.>
- **Expected winning bid:** <estimate or range>
- **Expected payment to seller:** <estimate>
- **Winner:** <highest-valuation bidder>

### Revenue and efficiency comparison
| Format | Expected revenue | Truthfulness | Efficiency | Notes |
|---|---|---|---|---|
| English | ... | ... | ... | ... |
| First-price | ... | ... | ... | ... |
| Second-price | ... | ... | ... | ... |

### Behavioral predictions
- How behavior changes if the format switches to <alternative>
- Impact of a reserve price
- Vulnerability to collusion (if applicable)

### Boundary-condition check
<which of the boundary conditions apply: common-value risk, bidder asymmetry, risk aversion, collusion, behavioral anomalies — and how each would shift the prediction>

### Confidence: high | medium | low
<reasoning: clarity of valuation distribution + bidder symmetry + private vs. common value + applicability of boundary conditions>
```
