---
name: Porter's Five Forces
domain: strategy
source: Michael E. Porter, "How Competitive Forces Shape Strategy," Harvard Business Review, 1979; expanded in Competitive Strategy (1980)
best_for: Explaining and predicting the long-run profitability of an industry by mapping the structural forces that determine where value accrues
one_liner: "Read industry profitability and competitive dynamics via rivalry, entry, substitutes, buyers, and suppliers."
---

# Porter's Five Forces

## Overview

Porter's Five Forces model claims that the long-run profitability of any
industry is governed not by individual firm behavior but by **five
structural forces** that together determine how much of the value created
in the industry is captured by producers versus siphoned off by customers,
suppliers, substitutes, or new entrants. The model is diagnostic, not
prescriptive: its purpose is to reveal *why* a given industry looks the
way it does, so that a firm's strategy can position against the forces
rather than wishing them away. The model is explanatory — to act on it
you apply the procedure below to a concrete industry.

## Core Variables and Relationships

The five forces and the variables that drive each one:

1. **Rivalry among existing competitors** — higher rivalry → lower
   industry profits.
   - Number and relative size of competitors
   - Industry growth rate (slow growth intensifies rivalry)
   - Fixed / storage costs relative to value added
   - Degree of differentiation vs. commodity character
   - Exit barriers (specialized assets, labor commitments)

2. **Threat of new entrants** — higher threat → lower profits (incumbents
   must deter entry with lower prices).
   - Economies of scale
   - Capital requirements
   - Switching costs for customers
   - Access to distribution channels
   - Incumbency advantages (learning curves, network effects, brand)
   - Expected retaliation by incumbents
   - Government / regulatory barriers

3. **Threat of substitutes** — higher threat → lower profits (cap on
   price).
   - Relative price-performance of the substitute
   - Switching cost to the substitute
   - Buyer propensity to substitute
   - Substitute's trajectory (improving vs. plateaued)

4. **Bargaining power of buyers** — higher power → buyers extract value.
   - Buyer concentration vs. producer concentration
   - Volume per buyer relative to producer sales
   - Undifferentiated product (easy to switch)
   - Buyer switching costs
   - Buyer information (can the buyer see the true cost stack?)
   - Threat of backward integration by buyers

5. **Bargaining power of suppliers** — higher power → suppliers extract
   value.
   - Supplier concentration vs. producer concentration
   - Absence of substitute inputs
   - Producer's importance to the supplier
   - Differentiation of the supplier's input
   - Supplier switching costs
   - Threat of forward integration by suppliers

The net structural profitability of the industry is the combined
intensity of the five forces. Firms compete *within* the resulting
envelope; changing the envelope itself is a very high-bar move.

## Key Predictions

- An industry with **high rivalry + low entry barriers + powerful buyers**
  will exhibit chronically low returns on invested capital regardless of
  individual firm effort (commodity-like: airlines, most retail
  grocery).
- An industry with **low rivalry + high entry barriers + fragmented
  buyers + fragmented suppliers** will support sustained above-average
  returns unless a force shifts (e.g., historical pharma, enterprise
  software with lock-in).
- Structural shifts in any single force propagate: new entrants that
  commoditize a previously differentiated input force suppliers into
  weaker positions; a concentrating buyer base flips margins rapidly.
- Most "competitive strategy" failures are firms attacking the wrong
  force — e.g., trying to out-rivalry competitors when the binding
  constraint is buyer power.

## Application Procedure

Instantiate the model against a specific industry or a specific firm's
competitive situation.

1. **Define the industry boundary precisely.** What is the product or
   service? What is the geographic scope? What time horizon? An
   over-broad definition ("transportation") produces a uselessly average
   view; an over-narrow one ("electric scooters in Seoul, 2026") produces
   noise. Write the boundary in one sentence.

2. **Enumerate participants for each force.**
   - Existing competitors: list the top 5–10 and note relative share.
   - Potential entrants: who could credibly enter within the horizon?
   - Substitutes: what non-industry alternatives serve the same
     underlying buyer need?
   - Buyers: who pays, and at what concentration?
   - Suppliers: what key inputs, and from whom?

3. **Score each force** on a 3-level scale (Low / Medium / High intensity)
   by walking through its driver variables above. Cite at least one
   observable fact per variable — not opinion.

4. **Identify the dominant force(s).** Usually one or two forces drive
   the profitability ceiling. State which and why.

5. **Read off structural predictions.**
   - What is the approximate profitability envelope of the industry?
   - Where is value leaking out (which force is extracting most)?
   - Which strategic moves would shift a dominant force in the firm's
     favor (and which would not, regardless of effort)?

6. **Check boundary conditions** (see below). If any apply, note that the
   Five Forces view is incomplete and flag what complementary analysis is
   needed (e.g., a dynamic / innovation view, or a network-effects view).

## Boundary Conditions

Porter's Five Forces was designed for **relatively stable, physical-good
industries** and breaks down or becomes partial under several conditions:

- **High-rate technological disruption.** The model is static; it
  assumes forces change slowly relative to strategy cycles. In
  fast-moving markets (early-stage platforms, generative AI tooling),
  the model gives a snapshot that is already obsolete.
- **Network effects and multi-sided markets.** The five forces don't
  naturally capture cross-side externalities that are the dominant
  dynamic in platform businesses. Supplement with a platform / network
  effects view.
- **Complementors / ecosystems (the "sixth force").** Brandenburger &
  Nalebuff's Value Net adds complementors. Pure Five Forces can miss
  ecosystem leverage (e.g., operating systems and app developers).
- **Regulated or state-dominated industries.** Political economy often
  dominates the force structure; modeling it as a buyer or entrant is
  an oversimplification.
- **Firm-level heterogeneity.** The model predicts industry-average
  profitability, not why one firm in the industry earns 3× the average —
  for that, use a resource-based view (VRIO) or capability analysis
  alongside.

## Output Format

```
## Industry Five Forces Analysis: <industry name / boundary>

**Boundary:** <one-sentence scope: product, geography, time horizon>
**Time snapshot:** <date>

### Force intensity
| Force | Intensity | Key drivers |
|---|---|---|
| Rivalry | H/M/L | <2-3 observed drivers with evidence> |
| New entrants | H/M/L | ... |
| Substitutes | H/M/L | ... |
| Buyer power | H/M/L | ... |
| Supplier power | H/M/L | ... |

### Dominant force(s)
<which 1–2 forces set the profitability ceiling and why>

### Structural prediction
- Profitability envelope: <above avg / avg / below avg>
- Primary value leakage: <which force, how much>
- Structural shifts to watch: <what would move a force and on what timescale>

### Strategic implications
- Moves that plausibly shift a dominant force in our favor
- Moves that will not work because they attack the wrong force

### Boundary-condition notes
<which boundary conditions apply and what complementary analysis is needed>

### Confidence: high | medium | low
<reasoning: data quality + industry stability + boundary-condition fit>
```
