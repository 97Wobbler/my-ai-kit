---
name: gini-coefficient-lorenz-curve
display_name: Gini Coefficient & Lorenz Curve
class: lens
underlying_class: native
domain: economics
source: Corrado Gini (1912); Max Otto Lorenz (1905)
best_for:
  - Quantifying income or wealth inequality in a population
  - Comparing inequality across regions, time periods, or datasets
  - Identifying whether redistribution efforts are working
one_liner: "Standard measure for quantifying income or wealth inequality and tracking distributional change."
---

# Gini Coefficient & Lorenz Curve

## Overview
The Gini Coefficient is a single number (0–1 or 0–100%) that measures inequality: 0 means perfect equality (everyone has the same), 1 means perfect inequality (one person has everything). The Lorenz Curve is the graph it rests on — a cumulative distribution plot that shows how much of total income is held by each percentile of the population. Practitioners use this lens when they need to track whether inequality is widening or shrinking, compare inequality across countries or time periods, or audit whether a policy intervention actually redistributed wealth as claimed.

## Analytical Procedure

### Phase 1 — Data Preparation

1. **Obtain the raw dataset.** You need either:
   - Individual-level data: a list of incomes (or net worth, or any scarce good you're measuring) for N people, one row per person.
   - Binned data: groups labeled by percentile or income bracket with the total income in each bracket.
   
   Document the data source, collection date, and any known biases (e.g., survey data misses the very rich; tax data misses unreported income).

2. **Sort incomes in ascending order.** From lowest to highest. Discard any negative values or zero incomes — document how many rows you dropped and why.

3. **Calculate cumulative shares.** For each person (or percentile):
   - Cumulative population %: `(person's rank / total people) × 100`
   - Cumulative income %: `(sum of all incomes up to this person / total income) × 100`
   
   Build a two-column table: Population % on the x-axis, Income % on the y-axis. Include the point (0, 0) at the start and (100, 100) at the end.

### Phase 2 — Construct the Lorenz Curve

4. **Plot the cumulative shares.** x-axis is cumulative population percentage (0–100), y-axis is cumulative income percentage (0–100). Mark each percentile as a point. Connect the points with straight lines. The result is the Lorenz Curve.

5. **Compare to the line of perfect equality.** This is a diagonal from (0, 0) to (100, 100). The larger the gap between the Lorenz Curve and this diagonal, the greater the inequality.

### Phase 3 — Calculate the Gini Coefficient

6. **Measure the area between the curves.** The Gini Coefficient is defined as:
   ```
   Gini = (Area between Lorenz Curve and diagonal) / (Total area below the diagonal)
   ```
   
   The total area below the diagonal is always 0.5 (a right triangle with base 100 and height 100). So:
   
   ```
   Gini = 2 × (Area between the curves)
   ```
   
   Use the trapezoid rule to approximate area under the Lorenz Curve, then subtract from 0.5.

7. **Express the Gini as a percentage.** Multiply by 100. A Gini of 0 means perfect equality; a Gini of 100 means perfect inequality (one person has all income).

### Phase 4 — Interpret and Compare

8. **Benchmark against known values.** Common reference points:
   - Nordic countries (Sweden, Denmark): Gini ~25–28
   - Western Europe (Germany, France): Gini ~30–35
   - United States: Gini ~38–42
   - Brazil: Gini ~50+
   - South Africa: Gini ~63+
   
   Interpret your result in context. A Gini of 35 in a high-income country suggests moderate inequality; the same Gini in a low-income country may indicate relative equality given regional norms.

9. **Track changes over time.** If you have data from multiple years, plot Gini values chronologically. A rising Gini suggests inequality is worsening; falling suggests it's improving. Note policy changes, economic shocks, or demographic shifts that coincide.

10. **Test robustness.** Re-calculate the Gini on:
    - Data excluding the top 1% (to see if extreme wealth is driving the result)
    - Data excluding the bottom 10% (to see if extreme poverty is driving the result)
    - Alternative income definitions (gross vs. net, pre-tax vs. post-tax, including/excluding transfers)
    
    If the Gini is stable across these variants, the result is robust. If it swings wildly, the conclusion depends on boundary choices.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Data source is documented and bias/coverage gaps are noted | Y/N |
| Cumulative population and income percentages are correctly calculated | Y/N |
| Lorenz Curve is plotted and visually compared to the diagonal | Y/N |
| Area under the curve is calculated (trapezoid or integral method) | Y/N |
| Gini Coefficient is expressed as a number between 0–100 | Y/N |
| Result is benchmarked against known reference values | Y/N |
| Robustness checks (excluding extremes, alternative definitions) are done | Y/N |

## Red Flags

- Gini is calculated but the Lorenz Curve is not plotted or shown. The curve is the visual evidence; without it, the number is unanchored.
- Data includes negative incomes, zero incomes, or missing values without justification for inclusion or exclusion. Gini is sensitive to boundary cases.
- The Gini Coefficient is compared across datasets collected in different years, regions, or using different methodologies (tax data vs. survey data) without acknowledging these are not directly comparable.
- The Lorenz Curve shows a clear "kink" or discontinuity (e.g., a jump from 50th percentile to 95th percentile). This suggests binned data with unequal bin widths or a genuine clustering in the population. Either way, it must be explained.
- Robustness checks are not performed. A Gini of 35 is meaningless if excluding the top 10% drops it to 20 — the conclusion depends on what you exclude, and that choice must be defended.
- The result is reported without context. "Gini = 38" in isolation tells the reader nothing. Always state: the country/population, the time period, the income definition (gross/net, pre-tax/post-tax), and the nearest comparable benchmark.

## Output Format

```
## Gini Coefficient & Lorenz Curve Assessment

**Population and income definition:**
<e.g., "United States, household income, pre-tax, 2023 survey data, N=50,000 households">

**Data summary:**
- Total records: _
- Records dropped (negative/zero/missing): _ (<reason>)
- Minimum income: $_ | Maximum income: $_
- Mean income: $_ | Median income: $_

**Lorenz Curve:**
[Table with cumulative population % and cumulative income %]

**Area under Lorenz Curve (0–0.5 scale):**
<calculated value using trapezoid rule or integration>

**Gini Coefficient:**
- Raw (0–1 scale): _._
- Percentage (0–100 scale): __

**Benchmark comparison:**
- This population: Gini = __
- Reference: <country/region at comparable time>: Gini = __
- Interpretation: <more/less equal than benchmark>

**Robustness checks:**
| Variant | Gini |
|---|---|
| Full dataset | __ |
| Excluding top 1% | __ |
| Excluding bottom 10% | __ |
| Post-tax income (if applicable) | __ |
| Alternative definition | __ |

**Stability:** <stable across variants / sensitive to exclusions / highly dependent on definition>

**Trend (if multi-year data available):**
| Year | Gini |
|---|---|
| ... | ... |
Change: <direction and magnitude>

**Confidence**
<high/medium/low> — <justification: e.g., "high — large sample size, verified data source, robust across sensitivity checks" OR "medium — survey data, possible undercount of extreme wealth" OR "low — small sample, significant missing data, high sensitivity to exclusion choices">
```
