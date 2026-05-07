---
name: difference-in-differences
display_name: Difference-in-Differences
class: lens
underlying_class: native
domain: data
source: Ashenfelter and Card, 1985; formalized econometric treatment in Angrist & Pischke (2009)
best_for:
  - Isolating causal effects when randomization is impossible
  - Leveraging natural experiments or policy changes
  - Removing confounding from time-invariant group differences
one_liner: "Causal estimation leveraging policy changes or natural experiments."
---

# Difference-in-Differences

## Overview
Difference-in-Differences (DiD) estimates causal effects by comparing how two groups changed relative to each other across two time periods—before and after an intervention. One group is exposed to a treatment (the "treated" group); the other is not (the "control" group). The method works by removing the effect of time-invariant confounders and trends that affect both groups equally. Practitioners use DiD when a randomized experiment is infeasible but a natural experiment or policy shock exists that affects one group but not another.

## Analytical Procedure

### Phase 1 — Validate the Setup

1. **Identify the treatment event and groups.** Write down:
   - Exactly what changed (policy, program, external shock)?
   - When did it happen (month, year)?
   - Which units (individuals, firms, regions) were exposed?
   - Which units were not exposed?
   
   Do not proceed if the treatment is ambiguous or if treated and control groups are self-selected.

2. **Verify the parallel trends assumption.** This is non-negotiable:
   - Graph the outcome for treated and control groups across all pre-treatment periods.
   - Do the two lines run roughly parallel? (Same slope, not the same level.)
   - If they diverge or converge before treatment, the assumption is violated—DiD is not valid.
   - Document this visually. A single crossing trend line is a red flag.

3. **Confirm data coverage.** Ensure you have:
   - At least two periods before treatment (to check pre-trends)
   - At least one period after treatment (to measure the effect)
   - The same units observed in both pre and post periods (balanced panel strongly preferred)
   - No major differential attrition between groups

### Phase 2 — Specify the Estimating Equation

4. **Write the regression model explicitly:**
   ```
   Y_it = α + β₁(Treated_i) + β₂(Post_t) + β₃(Treated_i × Post_t) + ε_it
   ```
   where:
   - `Y_it` = outcome for unit i at time t
   - `Treated_i` = 1 if unit i is in treated group, 0 otherwise (group fixed effect)
   - `Post_t` = 1 if time t is after treatment, 0 otherwise (time fixed effect)
   - `Treated_i × Post_t` = the interaction (the DiD estimand)
   - `β₃` = the causal effect of interest

5. **Choose covariates carefully.** Include only:
   - Baseline characteristics measured *before* treatment (not post-treatment controls, which can be bad colliders)
   - Variables that do not change over time (redundant with fixed effects but useful for transparency)
   - Do NOT include post-treatment variables unless they are mediators and you are explicitly studying mediation

6. **Add fixed effects.** Use unit-level and time-level fixed effects to absorb all time-invariant and unit-invariant confounders:
   - Unit fixed effects remove any permanent differences between treated and control groups
   - Time fixed effects remove any aggregate time trends affecting all units equally

### Phase 3 — Estimate and Validate

7. **Estimate the model.** Run OLS regression with the specification from Phase 2. Report:
   - The point estimate for β₃ (the DiD coefficient)
   - Standard errors (or use robust/clustered standard errors if there is within-unit or within-group correlation)
   - The full regression table (all coefficients, R², N)

8. **Test the parallel trends assumption formally:**
   - Include separate time dummies for each pre-treatment period, interacted with `Treated_i`
   - These pre-treatment interactions should be small and not jointly significant (p > 0.10)
   - If any pre-treatment interaction is large and significant, the identifying assumption fails

9. **Run placebo tests:**
   - Fake a treatment at an earlier date (before the real treatment)
   - Estimate the "effect" of this fake treatment
   - It should be close to zero and not significant
   - If the fake treatment shows a large effect, the method is picking up pre-existing differences or other bias

10. **Check for common support.** Ensure treated and control groups have overlapping distributions on all baseline covariates. If the groups are very different ex-ante, no amount of regression adjustment fully solves it.

### Phase 4 — Examine Robustness

11. **Vary the specification:**
    - Run with and without covariates (coefficients should be similar if selection is not a problem)
    - Use alternative time periods (drop early or late periods; check if the effect is stable)
    - Test alternative functional forms (linear vs. log, levels vs. changes)

12. **Check for violations of homogeneity:**
    - Plot heterogeneous effects by subgroup (age, income, baseline outcome level, etc.)
    - If the effect is very different across subgroups, the average effect may mask important variation
    - Report the range of effects, not just the mean

13. **Examine the timing of the effect.** If the treatment has a lead time or phased rollout:
    - Estimate separate effects for each period post-treatment
    - Plot the event study (coefficients against time relative to treatment)
    - The effect should remain flat and zero before treatment, then jump at treatment (not gradually grow or decay for no reason)

## Evaluation Criteria

| Check | Pass |
|---|---|
| Treated and control groups are clearly defined and mutually exclusive | Y/N |
| Treatment timing is precise (no ambiguity about when it happened) | Y/N |
| Parallel trends assumption is tested graphically and formally | Y/N |
| Data are balanced (same units pre and post, or attrition is explained) | Y/N |
| Regression model includes unit and time fixed effects | Y/N |
| Pre-treatment interactions are small and jointly insignificant (p > 0.10) | Y/N |
| Placebo test shows zero or near-zero fake effect | Y/N |
| Robustness checks (with/without covariates, alternative specs) are reported | Y/N |
| Standard errors are reported and justified (robust/clustered if needed) | Y/N |

## Red Flags

- Parallel trends assumption is never visually checked or formally tested. This is the single most important assumption — its violation invalidates the entire analysis.
- Treated and control groups differ substantially on baseline covariates that are themselves affected by the treatment (e.g., using post-treatment employment status as a covariate when the treatment affects employment). This introduces bias.
- Post-treatment covariates are included in the regression. These can be colliders and induce bias even if the parallel trends assumption holds.
- The DiD coefficient is large and highly significant, but pre-treatment interactions are not formally tested. Overconfidence in the absence of evidence.
- Event study plot shows effects growing or decaying smoothly over time, rather than a sharp jump at treatment. This suggests the treatment was gradual or confounded by other time-varying factors.
- Specification changes dramatically with the addition of covariates. This suggests the treated and control groups are not comparable and selection bias is present.
- The sample size is very small (especially for the control group), or treated and control groups are very unequal in size. Standard errors will be inflated and power low.
- No heterogeneity analysis. The average effect may mask that the treatment helped some groups and hurt others.

## Output Format

```
## Difference-in-Differences Analysis

**Treatment:**
- Policy/event: <description>
- Timing: <date or period>
- Treated group: <definition and N>
- Control group: <definition and N>

### Phase 1 — Design Validity

**Parallel trends assumption:**
- Visual check: <pass/fail — describe the pre-treatment trend graph>
- Formal test (pre-treatment interactions): <F-stat, p-value, verdict>
- Conclusion: <assumption holds / violated>

**Data coverage:**
- Observations per group: <N treated, N control>
- Time periods: <list>
- Balance: <balanced / unbalanced — if unbalanced, describe attrition>

### Phase 2 — Specification

**Model:**
```
Y_it = α + β₁(Treated_i) + β₂(Post_t) + β₃(Treated_i × Post_t) + ε_it
[+ covariates and any interactions if used]
```

**Fixed effects:** Unit and time fixed effects included.
**Covariates:** <list, or "none">
**Standard errors:** <robust / clustered at [level] / other>

### Phase 3 — Estimates

| Coefficient | Estimate | Std. Error | t-stat | p-value |
|---|---|---|---|---|
| Treated (β₁) | <...> | <...> | <...> | <...> |
| Post (β₂) | <...> | <...> | <...> | <...> |
| DiD (β₃) | <...> | <...> | <...> | <...> |
| <covariates> | <...> | <...> | <...> | <...> |

**Interpretation:** The causal effect of the treatment is β₃ = <value> [95% CI: <lower>, <upper>].

### Phase 4 — Robustness

**Placebo test:** Fake treatment at <period>. Effect = <estimate> (p = <...>). Verdict: <pass/fail>

**Specification checks:**
- With covariates: β₃ = <estimate> (compare to main estimate)
- Without covariates: β₃ = <estimate>
- Alternative time periods: <brief summary of stability>

**Heterogeneous effects:**
- <Subgroup 1>: β₃ = <...>
- <Subgroup 2>: β₃ = <...>
- <...>

**Event study plot:** <Describe the pattern — sharp jump, gradual effect, etc.>

### Confidence

<high | medium | low> — <justification based on parallel trends validity, effect size, sample size, robustness checks, and pre-treatment balance>
```
---
