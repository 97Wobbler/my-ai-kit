---
name: process-capability
display_name: Process Capability (Cp, Cpk)
class: model
underlying_class: native
domain: manufacturing
source: Walter Shewhart, Statistical Method from the Viewpoint of Quality Control (1939); formalized as capability indices by Ford Motor Company in the 1980s; ISO 21747:2005
best_for:
  - Quantifying how much margin a process has relative to specification limits
  - Predicting the rate of out-of-spec defects under stable conditions
  - Diagnosing whether process centering or variation reduction is the binding constraint
one_liner: "Indicator quantifying how comfortably a process meets specification limits."
---

# Process Capability (Cp, Cpk)

## Overview

Process Capability indices (Cp and Cpk) quantify whether a stable manufacturing process has enough margin relative to its specification limits to produce conforming parts at an acceptable defect rate. The model is predictive: given a process's mean, standard deviation, and specification bounds, it predicts the percentage of parts that will fall outside the spec window. Cp measures potential capability (assuming perfect centering); Cpk measures actual capability (accounting for centering drift). The model assumes the process is statistically stable (in control) and that the output follows a normal distribution. It is used diagnostically to identify whether a process improvement should target centering (mean shift) or variation reduction (reducing σ), and as a quantitative gate for accepting or rejecting a process for production.

## Core Variables and Relationships

1. **Upper Specification Limit (USL)** — the maximum acceptable value for the part characteristic.

2. **Lower Specification Limit (LSL)** — the minimum acceptable value.

3. **Specification window (SW)** — the interval [LSL, USL]; width = USL − LSL.

4. **Process mean (μ)** — the central tendency of the process output. Can be anywhere within or outside the spec window.

5. **Process standard deviation (σ)** — the measure of process spread or variation. Smaller σ is better; σ is estimated from a rational subgroup sample (e.g., within-subgroup standard deviation from an X-bar/R control chart).

6. **Potential capability (Cp)** — assumes the process is perfectly centered at the midpoint of the spec window:
   ```
   Cp = (USL − LSL) / (6σ)
   ```
   The denominator 6σ represents ±3 standard deviations, which under normality captures 99.73% of the distribution. Cp ignores where the mean actually is.

7. **Actual capability (Cpk)** — accounts for the actual process mean being off-center:
   ```
   Cpk = min[ (USL − μ) / (3σ), (μ − LSL) / (3σ) ]
   ```
   It is the smaller of the two one-sided margins (in units of 3σ). Cpk ≤ Cp always; equality only when μ is exactly centered.

8. **Relationship:** Cpk is the binding constraint on defect rate. If Cpk = 1.0, the process mean is exactly 3σ away from the nearest spec limit, which (under normality) corresponds to ~0.135% defect rate (1.35 parts per thousand, or ~3.4 parts per million). If Cpk = 1.33, the margin is 4σ, corresponding to ~0.003% defect rate.

9. **Industry convention:** Cpk ≥ 1.33 is the minimum acceptable for most manufacturing; Cpk ≥ 1.67 is preferred for critical characteristics; Cpk ≥ 2.0 signals very high confidence.

## Key Predictions

- **Cpk directly predicts defect rate.** A Cpk of 1.0 maps to ~0.135% defects; Cpk of 1.33 maps to ~0.003% (~30 ppm); Cpk of 1.67 maps to ~<0.0001% (sub-ppm). These assume normality and stability. Under these conditions, the prediction is quantitative, not directional.

- **If Cp >> Cpk (e.g., Cp = 1.5 but Cpk = 0.8), the process has sufficient variation headroom but is off-center.** The improvement lever is to re-center the mean, not to reduce variation. Reducing variation will help but will not directly address the constraint.

- **If Cp ≈ Cpk (both ~1.2), the process is centered but has inadequate variation margin.** The binding constraint is σ reduction. Centering adjustments alone will not move the needle.

- **A process with Cpk < 1.0 will produce non-conforming parts at a rate exceeding ~0.135%, even if stable.** This is the Cpk = 1.0 threshold: below it, the process is incapable of meeting the specification with acceptable defect rates under standard acceptance rules.

- **Cpk is invariant to the absolute magnitude of the specification.** A process with ±0.01mm tolerance on a 50mm part (tight, relative) and a process with ±1mm tolerance on a 5m part (loose, relative) can have identical Cpk values if their σ, μ, and margin ratios are the same. Cpk is a dimensionless efficiency ratio.

## Application Procedure

Instantiate the model against a specific manufacturing process and product characteristic you are evaluating.

1. **Define the process and the characteristic precisely.**
   - What is the part? What is the characteristic being measured (dimension, hardness, surface finish, etc.)?
   - What is the production rate and time horizon of interest?
   - Is the process currently in control (statistically stable), or are there known assignable causes?

2. **Obtain or specify the specification limits.**
   - Write USL and LSL explicitly. If the spec is one-sided (e.g., "hardness ≥ 55 HRC"), treat the other as ±∞ for Cp/Cpk purposes (or use one-sided capability indices Cpu / Cpl).
   - Document the engineering rationale for these limits and whether they are truly required or are defensive.

3. **Collect process data and estimate μ and σ.**
   - Sample at least 25–30 consecutive parts (or 5–10 rational subgroups of 4–5 parts each) under stable conditions.
   - Compute the sample mean and standard deviation. For more precision, use within-subgroup standard deviation (e.g., from an X-bar/R chart) rather than overall standard deviation; this isolates short-term variation and removes noise from long-term drift.
   - Verify the data are approximately normal (plot a histogram, run a normality test). If non-normal (e.g., bimodal, skewed), flag this in boundary conditions and consider a transformation or non-parametric method.

4. **Calculate Cp and Cpk.**
   - Cp = (USL − LSL) / (6σ)
   - Cpk = min[(USL − μ) / (3σ), (μ − LSL) / (3σ)]
   - Note which limit is binding (which term is smaller).

5. **Compare Cpk against the acceptance threshold.**
   - Cpk ≥ 1.33: process is capable; acceptable for ongoing production.
   - 1.0 ≤ Cpk < 1.33: process is marginally capable; defect rates ~30–135 ppm; action required.
   - Cpk < 1.0: process is incapable; expect regular out-of-spec parts; stop production and investigate.

6. **Diagnose the improvement lever.**
   - If Cp >> Cpk: re-center the process (adjust μ).
   - If Cp ≈ Cpk: reduce variation (improve tool stability, reduce material scatter, tighten environmental control).
   - If both Cp and Cpk are low: both levers needed; prioritize based on cost and ease.

7. **Check boundary conditions** (below). If any apply, adjust the interpretation or supplement with additional methods.

8. **Generate the prediction and action.**
   - State the predicted defect rate under the observed Cpk (use the defect rate table or normal probability tables).
   - Specify which process adjustment (centering or variation reduction) will move Cpk to the target (e.g., 1.33 or 1.67).
   - Estimate the effort and timeline required.

## Boundary Conditions

The Process Capability model applies well to stable, single-mode, continuous manufacturing characteristics with two-sided specs. It becomes unreliable or incomplete under:

- **Non-normal distributions.** If the process output is skewed, bimodal, or has heavy tails, the normal-based Cpk formula overestimates or underestimates defect rate. Solution: transform the data (log, Box-Cox) or use non-parametric capability indices (quantile-based Cpk).

- **Process instability (special causes present).** If the process mean is drifting, the variation is non-constant, or there are assignable causes (tool wear, material batch effects), the σ estimate is inflated or the μ is not a stable target. Cpk becomes a noise metric, not a prediction. Solution: control-chart the process first to remove assignable causes; then measure Cpk on the stable remainder.

- **Short production runs or small samples.** Estimating σ from fewer than 20–25 parts introduces high uncertainty in Cpk; the 95% confidence interval on Cpk itself can be ±0.2 or wider. Solution: pool data across similar runs or use Bayesian estimation with a prior.

- **One-sided specifications.** When only USL or only LSL applies (e.g., "tensile strength ≥ 400 MPa, no upper limit"), the standard two-sided Cp/Cpk formula does not apply. Solution: use one-sided indices Cpu or Cpl, or recalculate using the one-sided formula Cpk = (USL − μ) / (3σ) or (μ − LSL) / (3σ).

- **Tight tolerances relative to material or measurement error.** If the measurement system variation (gage repeatability and reproducibility, GR&R) is more than ~10% of the tolerance, the Cpk estimate is dominated by measurement noise, not process variation. Solution: perform a GR&R study first and improve the gage or reduce the tolerance.

- **Characteristics with cost or physics asymmetries.** Cpk treats deviations equally in both directions, but in reality, exceeding USL (e.g., over-torquing a bolt) may cost more or be more critical than falling below LSL. Solution: weight the defect rate by risk or rework cost; use loss functions.

## Output Format

```
## Process Capability Analysis: <process name / characteristic>

**Characteristic:** <dimension, material property, etc.>
**Unit:** <measurement unit>
**Specification window:** [LSL, USL] = [<value>, <value>] <unit>
**Sample size:** <n parts or subgroups>
**Data collection date:** <date>

### Process parameters (estimated from sample)
| Parameter | Value | Notes |
|---|---|---|
| Process mean (μ) | <value> <unit> | <method: overall or subgroup average> |
| Process std dev (σ) | <value> <unit> | <method: sample or within-subgroup σ> |
| Specification width | <value> <unit> | USL − LSL |

### Capability indices
| Index | Value | Interpretation |
|---|---|---|
| Cp (potential) | <number, 2 decimals> | <capable / marginal / incapable> |
| Cpk (actual) | <number, 2 decimals> | <capable / marginal / incapable> |
| Binding limit | <USL or LSL> | <3σ margin: <value> σ> |

### Predicted defect rate
- **At current Cpk:** <0.135% / 30 ppm / <value>% — based on normal distribution>
- **Reject rate:** <count per million or per thousand> expected out-of-spec parts

### Improvement diagnosis
- **Centering gap:** <μ − midpoint> <unit> — magnitude of off-center shift
- **Cp vs Cpk delta:** Cp − Cpk = <value> — indicates margin for centering vs. variation reduction
- **Recommended lever:** <re-center / reduce variation / both> with estimated cost/timeline

### Boundary-condition check
- **Normality:** <visual / Anderson-Darling test> — <normal / suspect / non-normal>
- **Stability:** <X-bar/R control chart or run test> — <stable / assignable causes detected>
- **Sample adequacy:** <n = <count>> — <adequate / borderline / insufficient>
- **Measurement system:** GR&R <% of tolerance> — <acceptable / marginal / inadequate>

### Confidence: high | medium | low
<reasoning: sufficient stable sample data under normal conditions at acceptable Cpk / limited by non-normality or process instability / small sample or high measurement error masking true process performance>
```
