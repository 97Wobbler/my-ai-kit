---
name: a-b-testing-principles
display_name: A/B Testing Principles
class: lens
underlying_class: native
domain: data
source: Ronald Fisher (design of experiments, 1920s); sequential analysis (Wald, 1945); multiple comparisons (Benjamini–Hochberg, 1995); optional stopping (Armitage et al., 1969)
best_for:
  - Validating that observed differences are real, not noise or artifacts
  - Detecting when a test is underpowered or when peeking invalidates results
  - Choosing between fixed-horizon and sequential testing designs
one_liner: "Secure statistical validity: power, MDE, sequential analysis, peeking risks."
---

# A/B Testing Principles

## Overview
A/B testing compares two variants by running them in parallel and measuring whether differences in outcomes are statistically real or due to chance. The discipline is not running the test — it is designing it before seeing data and resisting the temptation to stop early or redefine the metric once results arrive. Practitioners use this lens when planning a test to identify hidden design flaws (underpowered, unbalanced, or vulnerable to peeking) before data collection begins, and again when interpreting results to separate signal from noise.

## Analytical Procedure

### Phase 1 — Design Specification

1. **State the hypothesis in causal form.** Example: "Changing button color from blue to green will increase click-through rate." Not: "Button color affects CTR." Specify which variant is control and which is treatment.

2. **Define the primary metric precisely.**
   - Metric name and calculation method (e.g., "CTR = clicks / impressions").
   - Population (e.g., "users in US, desktop only").
   - Aggregation level (per-user, per-session, per-event).
   - If a ratio metric, define numerator and denominator separately; they may have different distributions.

3. **Set the minimum detectable effect (MDE).**
   - Current baseline: If CTR is 5%, state it.
   - Smallest effect worth detecting: "We care about a 10% relative increase, i.e., 5% → 5.5%." Justify why smaller effects don't matter (e.g., implementation cost, business priority).
   - Beware: Business stakeholders often claim "any improvement" matters. Push back. MDE sizes real assumptions about cost and value.

4. **Choose a significance level (α) and power (1 − β).**
   - Standard: α = 0.05 (5% false positive risk), power = 0.80 (80% chance of detecting the true effect if it exists).
   - Higher power (0.90) or lower α (0.01) require larger sample sizes; justify the choice.
   - Document: "We accept a 5% risk of declaring a false winner and a 20% risk of missing a real effect."

5. **Calculate required sample size.**
   - Use a power calculator (e.g., G*Power, Evan Miller's tools, or statsmodels). Record the output.
   - Sample size depends on: baseline rate, MDE, α, power, and test type (two-tailed vs. one-tailed).
   - Note: "20 days per variant" is not a sample size. Confirm you have 20 days worth of traffic; don't assume.

6. **Set run duration and stopping rule in advance.**
   - Fixed-horizon: "Run for exactly 14 days or until N = 100,000 users, whichever comes first."
   - Sequential (if using a sequential method): "Stop if the likelihood ratio exceeds X, or after 21 days, whichever comes first." (Requires a pre-specified stopping boundary; optional stopping without one is invalid.)
   - Record the calendar dates. This is your contract — do not change it after observing data.

7. **Specify the analysis plan.**
   - Intent-to-treat (ITT) or per-protocol?
   - If users see both variants during the test window, how do you assign them?
   - What statistical test (t-test, chi-square, Mann-Whitney)?
   - Multiple comparisons: If you run multiple primary metrics, do you adjust α (e.g., Bonferroni) or are these hypothesis confirmation, not discovery?
   - Confidence interval or p-value? Both is better.

### Phase 2 — Pre-test Audit

8. **Check for power bias.** Is the MDE so small that you'd need 1M+ users to detect it? If yes, either the effect doesn't matter or the metric is too noisy. Pick a cleaner metric or increase MDE.

9. **Check for metric quality.**
   - Is the metric biased? (e.g., measuring clicks, not conversions — users might click but not buy.)
   - Is it stable? Pull historical data on the baseline; check variance. High-variance metrics need larger sample sizes.
   - Is it local or global? "Time to first click" is user-local. "Site-wide revenue" is global and may be noisy due to spikes.

10. **Check for segment imbalance.** If the treatment variant or control is routed to systematically different users (e.g., all treatment goes to night traffic, all control to day), the test is biased. Confirm randomization is uniform across time, geography, and user type.

11. **Check for interference.** Do treated users affect untreated users? Example: A change that affects recommendation algorithm could make untreated users' feeds worse (negative interference) or better (spillover). If you suspect it, run the test on isolated user cohorts (geographic regions, app versions) and compare.

12. **Check for peeking risk.** Is anyone looking at results before the stopping date? If yes, the test is invalid. Recommend: lock the test from manual inspection; log only aggregate dashboards; announce the stopping date publicly.

### Phase 3 — Post-test Interpretation

13. **Check the result against the stopping rule.** Did you stop at the pre-specified boundary (calendar date, sample size, or sequential boundary)? If you stopped early because "results look good," you have optional stopping bias — the p-value is inflated and the confidence interval is too narrow.

14. **Compute effect size and confidence interval, not just p-value.**
   - P-value = 0.049 and p-value = 0.051 are not meaningfully different, but "effect = 5.2% ± [2%, 8%]" vs. "effect = 3.1% ± [−1%, 7%]" are.
   - If the CI crosses zero (or the zero-effect line), the test is inconclusive. Do not claim a winner.

15. **Account for multiple comparisons if needed.**
   - If you ran 5 secondary metrics without pre-specifying one as primary, adjust α (Bonferroni: divide α by 5) or use false discovery rate control (Benjamini-Hochberg).
   - If you did not pre-register which metric is primary and it emerges as significant post-hoc, treat it as exploratory, not confirmatory.

16. **Check for external validity.** Did the test run during an unusual period (holiday, outage, competitor launch)? Does the winner generalize to the broader population or just to test cohort?

## Evaluation Criteria

| Check | Pass |
|---|---|
| Hypothesis is stated causally with control and treatment identified | Y/N |
| Primary metric is defined with population and aggregation level | Y/N |
| MDE is set and justified (not "any improvement") | Y/N |
| α and power (1 − β) are documented | Y/N |
| Sample size was calculated before running the test | Y/N |
| Stopping rule is fixed in advance (no peeking) | Y/N |
| Analysis plan specifies test type and multiple-comparison handling | Y/N |
| Metric quality checked for bias, variance, and localness | Y/N |
| User randomization confirmed as uniform across time and segments | Y/N |
| Interference checked (or explicitly ruled out) | Y/N |

## Red Flags

- MDE is tiny relative to historical variance. This usually means the test will run for months or the metric is a proxy for the real outcome.
- "We'll stop when results are significant" instead of a calendar or sample-size boundary. This is optional stopping and invalidates the p-value.
- Sample size calculated post-hoc ("we ran for 2 weeks, so N = 50k"). Running time ≠ sample size; you need N before the test.
- Metric is a proxy but primary interest is something else. Example: measuring clicks, claiming it predicts lifetime value, but never validating the link.
- Multiple metrics tested, one is significant, declared as the "winner." If not pre-specified, this is p-hacking.
- Result is p = 0.04 and confidence interval crosses zero. Statistical significance without practical significance.
- Treatment group has different composition (age, geography, device type) than control group. Confound, not a valid comparison.
- Stopping rule violated: "Results looked good on day 10, so we stopped." Optional stopping inflates false positive risk.
- No confidence interval reported, only p-value. P-value alone does not convey effect size or uncertainty range.

## Output Format

```
## A/B Test Design & Validation

**Hypothesis:**
<causal statement with control and treatment>

### Phase 1 — Design Specification
| Element | Value | Justification |
|---|---|---|
| Primary metric | <name and definition> | <why this metric> |
| Baseline rate | <value> | <source> |
| Minimum detectable effect | <value + relative %> | <why this magnitude matters> |
| Significance level (α) | <0.05, 0.01, etc.> | <justification> |
| Power (1 − β) | <0.80, 0.90, etc.> | <justification> |
| Required sample size | <N> | <per-group or total> |
| Stopping rule | <fixed date, sample size, or sequential boundary> | <calendar or event> |
| Analysis plan | <ITT/per-protocol, test type, multi-comparison handling> | <method> |

### Phase 2 — Pre-test Audit
- **Power bias:** <acceptable | at risk>. <reason if at risk>
- **Metric quality:** <stable/noisy/biased>. Historical variance: <coefficient of variation>.
- **Randomization:** <confirmed uniform> or <confounds identified>. <details>
- **Interference:** <none suspected | controlled for | present — mitigated by>
- **Peeking:** <access locked> or <at risk of early stopping>

### Phase 3 — Results & Interpretation
- **Effect observed:** <value with 95% CI>
- **P-value:** <value>
- **Stopped as planned:** <yes / no>. <detail if no>
- **Multiple comparisons:** <not applicable | Bonferroni adjustment applied | false discovery rate controlled>
- **Generalizability:** <population covered by test> vs. <target population>

### Key Finding
<brief summary: does the treatment win, lose, or is the result inconclusive?>

### Confidence
<high/medium/low> — <justification: all pre-specified rules followed? Any violations to optional stopping, metric definition, or analysis plan? Is effect size practically meaningful given the MDE?>
```
