---
name: nps-ces-csat
display_name: NPS / CES / CSAT
class: lens
underlying_class: native
domain: marketing
source: Bain & Company (NPS, Reichheld 2003); American Customer Satisfaction Index (ACSI, 1994); Customer Effort Score (Gremler et al., 2015)
best_for:
  - Measuring customer sentiment across lifecycle touchpoints
  - Diagnosing which friction points drive loyalty or churn
  - Tracking sentiment trend and segmenting by driver
one_liner: "Capture customer sentiment through three signals — satisfaction, loyalty, and effort."
---

# NPS / CES / CSAT

## Overview

Net Promoter Score (NPS), Customer Effort Score (CES), and Customer Satisfaction (CSAT) are three widely-adopted metrics that capture different dimensions of customer sentiment. NPS measures loyalty tendency (would you recommend?); CSAT measures satisfaction with a specific experience or product; CES measures the friction or ease of an interaction. Practitioners layer all three to avoid optimizing for one dimension at the expense of another—a customer might rate satisfaction high (CSAT) but require effort so high (CES) that they never return (NPS). The discipline is choosing when to measure each, interpreting their divergence, and acting on root causes rather than the metrics themselves.

## Analytical Procedure

### Phase 1 — Instrument Selection and Administration

1. **Define the measurement context.** For each metric, specify:
   - **Timing**: immediately after purchase, after support interaction, monthly health check, post-renewal, or other.
   - **Scope**: single product, service feature, company relationship, or journey segment.
   - **Population**: all customers, segment (new / at-risk / enterprise), or sample.
   - **Mode**: in-product modal, email survey, SMS, API touchpoint, or embedded in support response.

2. **Administer NPS (0–10 scale).** Ask: "How likely are you to recommend [product/company] to a colleague or friend?" 
   - Respondents scoring 9–10 are Promoters.
   - Respondents scoring 7–8 are Passives.
   - Respondents scoring 0–6 are Detractors.
   - Calculate: NPS = (Promoters − Detractors) / Total Respondents × 100.

3. **Administer CSAT (1–5 or 0–10 scale).** Ask: "How satisfied are you with [specific experience / product / support interaction]?" 
   - If 1–5 scale: "Highly Satisfied" = 5, "Satisfied" = 4, "Neutral" = 3, "Dissatisfied" = 2, "Highly Dissatisfied" = 1.
   - If 0–10 scale: 9–10 is typically considered "satisfied."
   - Report satisfaction rate: % of respondents rating ≥4 (or ≥9 on 0–10 scale).

4. **Administer CES (5–7 point agreement scale).** Ask: "The [company/product] made it easy for me to [complete task / resolve issue / get value]." 
   - Scale: Strongly Agree / Agree / Neutral / Disagree / Strongly Disagree (or extended 7-point).
   - Report ease rate: % of respondents selecting Agree or Strongly Agree.
   - Note: high CES effort (disagreement) is a red flag; low effort (agreement) is desired.

5. **Collect verbatim feedback alongside scores.** Always append an open-ended field: "What is the main reason for your score?" This context is critical for diagnosis.

### Phase 2 — Segmentation and Diagnostic Decomposition

6. **Segment respondents by:**
   - Customer cohort (new, established, at-risk, high-value).
   - Product / feature tier.
   - Geography, industry, or account size if material.
   - Channel (self-serve, support-driven, account-managed).
   - Recent action (made purchase, filed ticket, renewed, churned).

7. **Cross-tabulate metric pairs** for each segment:
   - High NPS + High CSAT + High CES (ease): This is the ideal state. Preserve these workflows.
   - High NPS + High CSAT + Low CES (effort): Customer is loyal despite friction. This segment may churn if friction increases; prioritize effort reduction.
   - High NPS + Low CSAT + High CES (ease): Unlikely combination; investigate whether CSAT question is mismeasuring satisfaction or if question timing is off.
   - Low NPS + High CSAT + High CES: High satisfaction but no loyalty signal. Investigate switching risk and competitive pressure in this segment.
   - Low NPS + Low CSAT + Low CES: Severe problem; immediate action required. Drill into verbatim feedback by pain point.

### Phase 3 — Root Cause Attribution

8. **For each metric that diverged from expectation, extract the verbatim driver.** Group open-ended feedback by theme:
   - Feature gap or limitation.
   - Pricing or value perception.
   - Support responsiveness or quality.
   - Onboarding or learning curve.
   - Integration complexity.
   - Reliability or performance.
   - Competitor comparison.
   - Other.

9. **Assign causality hypothesis to each theme.** Do not assume correlation = causation. For example:
   - If low NPS co-occurs with "poor support response time," verify whether support is actually slow or whether the customer's expectation exceeds SLA.
   - If high CES but low CSAT, check whether the task was easy but solved the wrong problem.

10. **Validate the top 3 drivers via follow-up.** Either interview a subset of respondents in that theme or measure a proxy metric:
    - For "onboarding complexity," measure time-to-first-value or % activating key features by day 7.
    - For "support response," measure actual ticket-to-response SLA vs. customer expectation.
    - For "competitor comparison," search social media or run competitive win/loss interviews.

### Phase 4 — Trend and Benchmarking

11. **Track month-over-month and cohort-over-cohort change.** Plot NPS, CSAT, CES as time series. Identify inflection points (launch, incident, support change, pricing update) that correlate with metric move.

12. **Benchmark against industry baseline.** NPS varies widely by industry (e.g., SaaS B2B typically 30–60; luxury retail 70+; telecom 10–30). Establish your baseline and target, not vanity metrics.

13. **Monitor correlation between metrics and business outcome.** Link NPS/CSAT/CES cohort to actual retention rate, expansion revenue, churn rate, and support cost. If NPS is high but churn is rising, the metric is lagging reality.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Measurement context (timing, scope, population, mode) is documented | Y/N |
| NPS calculation and Promoter/Passive/Detractor split are correct | Y/N |
| CSAT and CES questions are specific to the experience being measured | Y/N |
| At least one open-ended verbatim field was collected | Y/N |
| Metrics were segmented by customer cohort or product tier | Y/N |
| At least one metric pair divergence was investigated | Y/N |
| Root cause themes were extracted from verbatims and tagged | Y/N |
| Top 3 drivers were validated against a proxy metric or follow-up data | Y/N |
| Trend was tracked over ≥3 time periods | Y/N |
| Results were benchmarked against industry or internal baseline | Y/N |

## Red Flags

- NPS is reported without Promoter/Passive/Detractor breakout. You cannot diagnose without the segments.
- CSAT and CES questions are generic ("How satisfied are you?") and not tied to a specific experience or feature. Vague questions produce vague scores.
- No verbatim feedback collected. Scores without context are noise; context without scores is anecdote.
- All three metrics moved in the same direction uniformly. Either the underlying experience truly changed across all dimensions (rare) or the survey had a single leading question that biased all three.
- Verbatim feedback was collected but not coded or themed. Hundreds of comments dumped without analysis are a liability, not an asset.
- Metric is tracked but never linked to business outcome (retention, revenue, churn). A high NPS that doesn't correlate with lower churn is not actionable.
- Industry benchmark is missing or the target is set to match the current score. Benchmarking against yourself is not benchmarking.
- CES is reported without specifying direction (higher is better for ease; lower effort is desired). If the reporting is inverted, all downstream decisions are backwards.

## Output Format

```
## NPS / CES / CSAT Assessment

**Measurement Context:**
- Timing: <when administered>
- Scope: <which experience>
- Population: <respondent segment>
- Mode: <in-app, email, etc.>
- Sample size: <n>

### Phase 1 — Raw Scores
| Metric | Score | Confidence |
|---|---|---|
| NPS | <value> | High / Medium / Low |
| CSAT (% satisfied) | <value> | High / Medium / Low |
| CES (% agree easy) | <value> | High / Medium / Low |

### Promoter / Passive / Detractor Split (if NPS)
| Segment | Count | % |
|---|---|---|
| Promoters (9–10) | <n> | <%> |
| Passives (7–8) | <n> | <%> |
| Detractors (0–6) | <n> | <%> |

### Phase 2 — Segmentation
| Segment | NPS | CSAT | CES | Pattern |
|---|---|---|---|---|
| <cohort> | <val> | <val> | <val> | <ideal / friction / misalignment / etc.> |

### Phase 3 — Root Cause Themes (from verbatims)
| Theme | Frequency | Example quote | Validation result |
|---|---|---|---|
| <e.g., "onboarding complexity"> | <n=_> | "<...>" | Confirmed / Disconfirmed / Inconclusive |

### Top 3 Drivers and Actions
1. <Driver>: <hypothesis>
   - Validation method: <how verified>
   - Recommended action: <specific change>

2. ...

### Phase 4 — Trend
<Description of trend over last 3+ periods; inflection points noted>

### Industry Benchmark
| Metric | Your score | Industry typical | Your position |
|---|---|---|---|
| NPS | <val> | <range> | Above / At / Below |
| CSAT | <val> | <range> | Above / At / Below |

### Overall Assessment
<Summary of what the metrics reveal about customer health and where the highest-leverage action is. Do not report metrics in isolation.>

### Confidence
<High / Medium / Low> — <justification. High if all checks passed and verbatim validation was done. Medium if sampling was limited or no follow-up validation. Low if only raw scores, no segmentation, no verbatims, or no business outcome linkage.>
```
