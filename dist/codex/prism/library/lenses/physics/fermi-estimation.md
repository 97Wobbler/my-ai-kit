---
name: fermi-estimation
display_name: Fermi Estimation
class: lens
underlying_class: native
domain: physics
source: Enrico Fermi (1930s–1950s); modernized in technology estimation and product estimation
best_for:
  - Quick magnitude estimates when precise data is unavailable
  - Sanity-checking the plausibility of claims or designs
  - Breaking down intractable problems into estimable components
one_liner: "Order-of-magnitude reasoning that derives reasonable approximations from constraints and assumptions."
---

# Fermi Estimation

## Overview
Fermi estimation is the art of breaking a large, seemingly unanswerable question into smaller, estimable pieces, then multiplying or summing them to arrive at an order-of-magnitude answer. It is not a precision tool — the goal is to land within a factor of 2–10 of the true value, not to be exact. Practitioners use it when exact data is inaccessible, time is limited, or they need to pressure-test whether a claim or design is even plausible before committing to deeper analysis.

## Analytical Procedure

### Phase 1 — Decompose the Problem

1. **State the question plainly.** What quantity are you estimating? Write it as a single variable with units (e.g., "How many piano tuners in Chicago?" or "What is the annual water consumption of New York City in gallons?").

2. **Identify the decomposition axis.** Decide whether to break the question by:
   - **Population or geography** (e.g., piano tuners = piano owners × fraction needing tuning annually ÷ tunings per tuner per year)
   - **Time** (e.g., total resource use = daily use × days per year × number of years)
   - **Process steps** (e.g., production output = machines × uptime % × utilization × output per unit)
   - **Market segments** (e.g., revenue = segment A users × price A + segment B users × price B)

3. **Write out the formula as a product or sum of estimable quantities.** For example:
   ```
   Piano tuners in Chicago = 
     (Chicago population) 
     × (fraction owning pianos) 
     × (fraction maintained professionally) 
     × (tunings per piano per year) 
     ÷ (tunings per tuner per year)
   ```
   Each factor should be a quantity you can estimate from first principles, personal experience, or quick research.

4. **Identify which factors are known, guessable, or research-worthy.** Mark each:
   - **Known** — publicly available (e.g., Chicago population)
   - **Guessable** — based on personal experience or reasonable assumption (e.g., fraction owning pianos)
   - **Research-worthy** — you need a 5-minute lookup (e.g., tunings per piano per year, tunings per tuner per day)

### Phase 2 — Estimate Each Factor

5. **For guessable factors, use the bracketing method.** Do not try to hit the exact value. Instead:
   - State a lower bound: "At least ___, because..."
   - State an upper bound: "At most ___, because..."
   - Pick a point estimate between them, usually the geometric mean.
   - Write down your reasoning for each bound.

6. **For research-worthy factors, do a quick lookup (5 minutes max).** Document the source. If you cannot find it, fall back to bracketing.

7. **Check each estimate for absurdity.** Does a piano tuner earning $50/hour tuning 3 pianos/day at $100/piano equate to $15k/month? Is that plausible for that market? If not, revise.

### Phase 3 — Compute and Validate

8. **Multiply (or sum) the factors to get a point estimate.** Write down the full calculation so someone can trace your arithmetic.

9. **Estimate the uncertainty bounds.** For each factor, identify the range you'd accept. Multiply the lower bounds of all factors to get a lower-bound estimate. Multiply the upper bounds to get an upper-bound estimate. Your true estimate sits somewhere between these.

10. **Sanity-check the result against reality or analogy.**
    - Does the answer pass a smell test? (E.g., "Piano tuners in Chicago: 200" feels plausible given the city size and the rarity of pianos.)
    - Can you compare it to a known proxy? (E.g., "If piano tuning is 1/100th the size of guitar repair, and there are 500 guitar repairers, then ~5 piano tuners is in the right ballpark.")
    - Would a 10× error materially change a decision? If yes, do deeper analysis. If no, move on.

11. **Document your assumptions visibly.** Write a bullet list: "I assumed pianos are owned by 2% of households, that they're tuned 2×/year on average, and that a tuner can do 3–4 pianos per day." Future readers (including yourself) must be able to see what you bet on.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Question is stated with units and no ambiguity | Y/N |
| Formula decomposes question into ≥3 factors | Y/N |
| Each factor is marked Known / Guessable / Research-worthy | Y/N |
| Guessable factors have documented lower and upper bounds | Y/N |
| Research-worthy factors have sources or bracketing | Y/N |
| Full arithmetic is shown (not just final answer) | Y/N |
| Uncertainty range (low–high) is calculated | Y/N |
| Assumptions are listed explicitly | Y/N |
| Sanity check references either analogy or order-of-magnitude plausibility | Y/N |

## Red Flags

- A factor is stated without reasoning ("I think it's 50%"). Bracketing is missing.
- The formula is not shown; only a final number appears. You cannot trace the estimate or spot where assumptions went wrong.
- Uncertainty bounds are symmetric (e.g., "50 ± 10"). Fermi estimates live in a multiplicative world; use factors (e.g., "50, with a range of 25–100") or logarithmic scaling.
- The sanity check is self-referential ("The answer feels right to me"). Compare to external data, analogies, or market size.
- Assumptions are implicit. The reader cannot tell whether the estimate would change materially if, say, you assumed 3% ownership instead of 2%.
- All factors are "known" or researched from the same source. No decomposition has occurred; you are just looking up a number.

## Output Format

```
## Fermi Estimation

**Question:**
<what quantity, in units>

**Decomposition formula:**
<quantity> = <factor 1> × <factor 2> × ... ÷ <factor N>

### Factor Estimates

| Factor | Category | Lower Bound | Point Estimate | Upper Bound | Reasoning |
|---|---|---|---|---|---|
| <factor name> | Known / Guessable / Research | <low> | <mid> | <high> | <why> |

### Calculation

<show full arithmetic:>
= <factor 1> × <factor 2> × ...
= <intermediate steps>
= <final number>

### Uncertainty Range

- Low estimate: <product of lower bounds>
- Point estimate: <result>
- High estimate: <product of upper bounds>
- Uncertainty factor: <high / low> (how many times the point estimate does the range span?)

### Key Assumptions

- <assumption 1, specific and falsifiable>
- <assumption 2>
- ...

### Sanity Check

<Comparison to analogy, market size, or known proxy. Does the answer pass?
Why or why not?>

### Confidence

<high | medium | low> — <justification: which factors are most uncertain? Did assumptions hold? How sensitive is the result to the biggest unknowns?>
```
---
