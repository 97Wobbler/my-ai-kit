---
name: population-viability-analysis
display_name: Population Viability Analysis
class: lens
underlying_class: native
domain: ecology
source: Shaffer, 1981; developed further by Boyce (1992) and the Conservation Breeding Specialist Group
best_for:
  - Assessing extinction risk for threatened or endangered populations
  - Designing minimum viable population sizes for conservation plans
  - Evaluating management strategies before implementation
one_liner: "Simulate extinction probability to assess long-term viability of a population."
---

# Population Viability Analysis

## Overview

Population Viability Analysis (PVA) is a quantitative framework that estimates the probability a population will persist for a specified time horizon (typically 100–1000 years) given current demographic rates, environmental variability, and management constraints. It operates on demographic data (birth rates, death rates, sex ratios, age structure) and environmental parameters (drought frequency, disease outbreaks, catastrophic events) to produce extinction probability curves. Practitioners use it when designing recovery goals, allocating reintroduction effort, or deciding whether a population can sustain itself without intervention.

## Analytical Procedure

### Phase 1 — Data Collection and Population Modeling

1. **Define the focal population and time horizon.**
   - Specify the species, geographic population, and the time window for persistence (e.g., "California condors over 100 years").
   - Justify the time horizon: conservation targets often use 100 years as a default; longer horizons (500+ years) are more conservative.

2. **Gather baseline demographic data.**
   - Age or stage-specific survival rates (from field studies, captive records, or adjacent populations if data are sparse).
   - Fecundity rates (offspring per female per year, separated by age class).
   - Sex ratio at birth and adult sex ratio.
   - Density dependence (if present): how reproduction or survival decline as population grows.
   - Record the data source and uncertainty range (confidence interval or SD) for each rate.

3. **Document environmental and catastrophic parameters.**
   - Frequency and severity of stochastic events: droughts, epidemics, wildfires, human-caused mortality.
   - Year-to-year variation in vital rates (standard deviation of survival and fecundity around the mean).
   - Environmental correlation: are multiple vital rates affected by the same event (e.g., drought reduces both breeding and survival)?
   - Establish these from historical records, expert elicitation, or analogous populations.

4. **Build a matrix population model (Leslie or stage-structured matrix).**
   - Organize survival and fecundity rates into a projection matrix where entry M[i,j] is the number of offspring (or survivors) produced by an individual in age/stage j that transition to age/stage i.
   - Validate the matrix: does the deterministic (non-random) version produce a stable or growing population consistent with observed trends?
   - If not, iterate on data sources and reconcile discrepancies.

5. **Set initial population size and structure.**
   - Record the current population size from census or survey.
   - Specify age/stage structure (stable age distribution, or actual counts if known).
   - If data are lacking, use the stable age distribution derived from the matrix.

### Phase 2 — Simulation and Extinction Risk Calculation

6. **Run stochastic simulations with environmental randomness.**
   - For each simulation run (typically 1000–10,000 replicates):
     - Begin with the initial population.
     - Each year, draw vital rates from distributions (normal, lognormal, or empirical) centered on observed means with documented variation.
     - Apply catastrophic events at their specified frequencies.
     - Project the population one year forward using the random vital rates.
     - Continue for the full time horizon (e.g., 100 years).
   - Extinction is defined as population size reaching zero; record the year it occurred for each replicate.

7. **Calculate extinction probability and confidence bounds.**
   - Count the number of replicates in which the population reached zero.
   - Extinction probability (PE) = (replicates extinct / total replicates) × 100%.
   - Compute 95% confidence interval on PE using binomial methods.
   - Repeat Step 6 with different initial population sizes to generate an extinction probability curve: PE as a function of starting size.

8. **Quantify population growth rate (λ) under uncertainty.**
   - From the stochastic simulations, calculate the mean and variance of log population size over time.
   - Derive the stochastic growth rate (λs) as the geometric mean of annual growth rates. Populations with λs < 1 are expected to decline; λs > 1 implies growth.
   - λs incorporates environmental variation and is typically lower than the deterministic λ from the matrix.

### Phase 3 — Sensitivity and Scenario Analysis

9. **Run sensitivity analyses to identify demographic bottlenecks.**
   - Increase one vital rate (e.g., juvenile survival) by a fixed percentage (e.g., +10%) while holding others constant.
   - Rerun the simulations and recalculate extinction probability.
   - Compare: "With juvenile survival +10%, PE drops from 0.45 to 0.30."
   - Repeat for each vital rate and for catastrophe frequency. Rank them by their impact on PE.
   - These identify which management interventions (e.g., reduce poaching of juveniles) would be most cost-effective.

10. **Evaluate management scenarios.**
    - Model alternative interventions: increasing survival via predator control, boosting fecundity via assisted breeding, reducing catastrophe frequency via habitat hardening.
    - For each scenario, run full simulations and compare extinction curves to the baseline.
    - Cost each intervention if data exist, and compute the "cost per 1% reduction in extinction probability."

11. **Test robustness to data uncertainty.**
    - Rerun the full analysis using vital rates from the upper and lower bounds of their confidence intervals.
    - If PE changes dramatically (e.g., from 0.3 to 0.7), data uncertainty is a major driver and more field work is justified before committing to a management decision.

### Phase 4 — Interpretation and Reporting

12. **State explicit extinction thresholds.**
    - Decide: what extinction probability is acceptable for this species? Typical conservation thresholds are PE < 0.05 (5%) over 100 years, but this depends on species ecology, legal status, and resource constraints.
    - Identify the minimum viable population (MVP) — the smallest starting size that keeps PE at or below the threshold.

13. **Document assumptions and limitations.**
    - List key assumptions: stable vital rates, no evolution or adaptation, no immigration from other populations, no change in habitat or climate (unless explicitly modeled).
    - Identify data gaps (e.g., "juvenile survival estimated from n=3 animals") and their likely direction of bias.
    - If the analysis ignores density dependence but the population has a history of boom-bust, note this as a limitation that could underestimate extinction risk at low densities.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Baseline vital rates (survival, fecundity) are sourced and uncertainty ranges documented | Y/N |
| Environmental stochasticity (variation and catastrophes) are specified with frequency and magnitude | Y/N |
| Population matrix is validated against historical population growth | Y/N |
| Simulations run ≥1000 replicates over the stated time horizon | Y/N |
| Extinction probability is reported with 95% confidence interval | Y/N |
| Sensitivity analysis identifies ≥3 vital rates ranked by impact on extinction risk | Y/N |
| ≥2 alternative management scenarios were modeled and compared | Y/N |
| Robustness to data uncertainty tested (upper/lower bounds on vital rates) | Y/N |
| Explicit extinction threshold stated and MVP identified | Y/N |
| Key assumptions and limitations are listed with direction of bias | Y/N |

## Red Flags

- Vital rates are point estimates with no uncertainty ranges. Stochastic simulations without input variation are meaningless.
- Simulations run for only 10–50 years. Extinction is a low-probability tail event; insufficient time window will underestimate PE.
- Sensitivity analysis is missing or only qualitative ("survival is important"). Practitioners need ranked, quantified impacts to prioritize action.
- No validation: the deterministic model was never checked against observed population trajectory. The model may be internally consistent but wrong.
- Catastrophe frequencies are invented rather than grounded in historical data or expert consensus. A "one-in-ten-year drought" claimed without evidence is speculation.
- Management scenarios are modeled without cost data. The "best" intervention may be prohibitively expensive, and cost-per-unit-risk-reduction is invisible.
- Data uncertainty was not tested. If PE is sensitive to one poorly-known parameter, that dominates the decision and demands a field study, not a model run.
- Assumptions include "climate is stable" in a region with documented climate change. The analysis may be technically sound but obsolete.

## Output Format

```
## Population Viability Analysis Report

**Species and Population:**
<species name, geographic population, current census size>

**Time Horizon:**
<e.g., 100 years> | Extinction Threshold: <e.g., 5% probability>

### Demographic Parameters
| Life Stage | Survival Rate | Fecundity (f/year) | Data Source | Uncertainty (SD or CI) |
|---|---|---|---|---|
| <e.g., Juvenile> | <e.g., 0.75> | <e.g., 0.0> | <...> | <...> |
| <Adult female> | <...> | <...> | <...> | <...> |

### Environmental Stochasticity
- **Vital rate variation (year-to-year SD):** Survival ±<SD>, Fecundity ±<SD>
- **Catastrophic events:** <Event type> (frequency <per N years>, reduces <rate> by <magnitude>)
- Example: "Drought (1 in 7 years), reduces fecundity to 0 in drought year; reduces survival by 30%."

### Stochastic Simulation Results
- **Number of replicates:** <N>
- **Initial population size:** <size>
- **Stochastic growth rate (λs):** <value> [95% CI: <lower>–<upper>]
  - Interpretation: Population expected to <grow/decline> at <%/year>
- **Extinction probability (100-year):** <PE%> [95% CI: <lower%>–<upper%>]
- **Minimum viable population (MVP):** <size at which PE ≤ threshold>

### Sensitivity Analysis (Ranked by Impact on Extinction Probability)
| Vital Rate | Baseline PE | +10% Scenario PE | Impact (ΔPE) | Rank |
|---|---|---|---|---|
| <e.g., Juvenile survival> | <PE%> | <PE%> | <ΔPE%> | 1 |
| <Adult survival> | <...> | <...> | <...> | 2 |

### Management Scenarios
**Scenario A:** <e.g., Predator control — increases juvenile survival from 0.75 to 0.85>
- Extinction probability: <PE%>
- Cost: <$X>
- Cost per 1% reduction in PE: <$Y>

**Scenario B:** <e.g., Assisted breeding — fecundity +20%>
- Extinction probability: <PE%>
- Cost: <$X>
- Cost per 1% reduction in PE: <$Y>

### Robustness to Data Uncertainty
- **Using lower-bound vital rates:** Extinction probability <PE%>
- **Using upper-bound vital rates:** Extinction probability <PE%>
- **Data uncertainty assessment:** <High/Medium/Low impact on conclusion>

### Key Assumptions and Limitations
- <e.g., Vital rates assumed stable; no evolutionary response to selection>
- <e.g., No gene flow from other populations modeled>
- <e.g., Juvenile survival estimated from n=3 animals; likely <high/low>-biased>
- <e.g., Climate held constant; warming could reduce fecundity by X%>

### Confidence
<high/medium/low> — <justification: e.g., "Medium — vital rates well-documented from 20-year field study, but juvenile survival has high variance; robustness test shows PE could range ±0.15 with plausible parameter sets. Recommend 5-year data update before committing to reintroduction.">
```
