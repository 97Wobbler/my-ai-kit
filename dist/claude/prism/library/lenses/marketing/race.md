---
name: race
display_name: RACE (Smart Insights)
class: lens
underlying_class: native
domain: marketing
source: origin uncertain
best_for:
  - Diagnosing underperformance in marketing funnel conversions
  - Aligning campaign metrics to business outcomes
  - Identifying which stage of the customer journey is the bottleneck
one_liner: "Diagnose each funnel stage (Reach / Act / Convert / Engage) to find bottlenecks and set improvement priorities."
---

# RACE (Smart Insights)

## Overview

RACE is a diagnostic lens for marketing funnels that examines four sequential stages — Reach, Act, Convert, and Engage — to isolate which stage is constraining business growth. Rather than treating the funnel as a black box, RACE forces explicit measurement and comparison at each gate, revealing whether a campaign's weakness is in audience acquisition, user activation, transaction closure, or retention. Practitioners reach for it when campaign ROI is lower than expected and the root cause is unclear, or when scaling one lever (e.g., more spend on ads) yields diminishing returns despite tactical execution looking correct.

## Analytical Procedure

### Phase 1 — Establish baseline metrics for each stage

1. **Define the full customer journey for the campaign.** Map the path from initial exposure to desired business outcome (purchase, subscription, repeat engagement). Write it as a sequence of 4–7 milestones.

2. **For each stage of RACE, identify the key metric:**
   - **Reach:** How many people encountered the message? (impressions, email opens, video starts, landing page views)
   - **Act:** How many took a deliberate action toward conversion? (clicks, form starts, video watch-through %, download, sign-up)
   - **Convert:** How many completed the primary transaction? (purchases, trial signups, demo bookings, committed leads)
   - **Engage:** How many returned or deepened involvement post-conversion? (repeat purchase, subscription renewal, NPS score, referral, 30-day active users)

3. **Gather historical data for each metric.** Use at least the last 3 comparable periods (weeks, months, or campaign cycles). If data is missing, note it as a red flag — you cannot diagnose what you do not measure.

4. **Calculate conversion rates between stages:**
   - Reach → Act rate: `Act / Reach × 100`
   - Act → Convert rate: `Convert / Act × 100`
   - Convert → Engage rate: `Engage / Convert × 100`
   - Overall funnel conversion: `Engage / Reach × 100`

### Phase 2 — Compare against benchmarks

5. **Establish what "healthy" looks like for your industry and channel.** Gather:
   - Industry median or published benchmarks (SaaS, e-commerce, media, etc.)
   - Your own historical performance (best quarter, average, worst)
   - Competitor proxies if available (publicly reported metrics, case studies)
   - Internal targets (what was forecasted in the campaign brief?)

6. **Plot each stage's conversion rate against the benchmark.** For each stage, mark it as:
   - **Underperforming:** Conversion rate more than 20% below benchmark (or your best historical)
   - **On-track:** Within 20% of benchmark
   - **Outperforming:** Above benchmark

7. **Identify the first underperforming stage in the sequence.** This is the bottleneck — the earliest point where the funnel diverges from expected performance.

### Phase 3 — Diagnose the bottleneck

8. **For the underperforming stage, examine input and output separately.**
   - **Input quality:** Is the traffic/audience entering this stage right? (correct target audience, right message-to-audience fit, expected volume?)
   - **Stage execution:** Is the experience of this stage itself broken? (slow page load, unclear call-to-action, confusing form, low message resonance?)
   - **Output friction:** Is the stage creating unnecessary friction? (too many steps, unexpected cost, trust barriers, technical errors?)

9. **Apply sub-diagnostics by stage type:**

   **If bottleneck is Reach:**
   - Budget allocation: Is spend appropriate for channel and audience size?
   - Targeting: Is the audience definition too narrow or off-brand?
   - Creative: Is the message generating interest (CTR, engagement rate underperforming)?
   - Channel saturation: Has the channel's cost per impression risen recently?

   **If bottleneck is Act:**
   - Message-to-landing fit: Does the landing experience match the ad promise?
   - Call-to-action clarity: Is the next step obvious and low-friction?
   - Trust signals: Is the page/email missing credibility markers (logo, testimonial, security badge)?
   - Form friction: If form abandonment data exists, at which field do users drop off?

   **If bottleneck is Convert:**
   - Pricing or barrier: Is the cost/commitment higher than expected? Compare to competitor or category norms.
   - Payment friction: Are checkout errors happening? (Check logs, failed transactions.)
   - Final objection: Do support tickets, refund requests, or live chat reveal a sticking point?
   - Segmentation: Does conversion rate vary sharply by audience segment? (Indicates message-fit problem, not funnel problem.)

   **If bottleneck is Engage:**
   - Onboarding: Do new customers understand the product value immediately after purchase?
   - In-product experience: Is there friction or complexity after conversion?
   - Expectation setting: Did the campaign oversell or misdirect (e.g., promising one feature, delivering another)?
   - Retention model: Is this a category where repeat behavior is realistic? (High-consideration purchases may not re-engage often.)

### Phase 4 — Prioritize and recommend

10. **For the bottleneck stage, list 3–5 hypotheses for why performance is weak.** Order by likelihood and impact:
    - Impact = estimated uplift in conversion rate if fixed
    - Likelihood = confidence that this is the actual cause (based on data seen above)

11. **Score each hypothesis on effort and expected ROI:**
    - **High effort, low ROI:** Deprioritize.
    - **Low effort, high ROI:** Immediate action.
    - **Medium effort, high ROI:** Sequence after quick wins.

12. **Write a diagnostic summary.** State the bottleneck, the leading hypothesis, the evidence supporting it, and the recommended test or fix. Include what you would need to measure to confirm the hypothesis (leading indicator).

## Evaluation Criteria

| Check | Pass |
|---|---|
| All 4 RACE stage metrics are defined with specific KPIs | Y/N |
| Conversion rates calculated for each gate (Reach→Act, Act→Convert, Convert→Engage) | Y/N |
| Baseline metrics compared to at least one external or internal benchmark | Y/N |
| First underperforming stage clearly identified | Y/N |
| Bottleneck stage examined for input quality, execution, and output friction | Y/N |
| Hypotheses for bottleneck are ranked by likelihood and impact | Y/N |
| Recommended action includes leading indicator to test or confirm | Y/N |

## Red Flags

- **All stages report "on-track" but overall funnel performance is weak.** This means either the benchmarks are too loose, the metrics are indirect proxies rather than true funnel gates, or the data is incomplete.
- **Bottleneck is diagnosed as "low awareness" or "weak creative" without comparing Reach metrics to channel benchmarks.** These are vague theories. Quantify impression volume, CTR, and cost-per-reach against historical and competitor norms first.
- **Recommendation is to "improve conversion" or "increase engagement" without specifying which lever or test.** That is not actionable. Name the specific experience change, the metric to move, and the expected uplift percentage.
- **No comparison stage data (benchmark absent, historical data thin, or competitor baseline missing).** Without external reference, "underperforming" is opinion.
- **Convert→Engage rate is ignored because "engagement metrics are hard to measure."** If they matter to your business model (SaaS, subscriptions, marketplace), measure them or state explicitly that this campaign is not optimized for retention.
- **Cause and symptom are confused.** ("Act stage is weak because conversion is low" — conversion is downstream; low Act affects conversion, not the reverse.)

## Output Format

```
## RACE Diagnostic Report

**Campaign:** <name and period>

### Stage 1 — Baseline Metrics

| Stage | Metric | Value | Source | Period |
|---|---|---|---|---|
| Reach | <KPI> | <count> | <system> | <date range> |
| Act | <KPI> | <count> | <system> | <date range> |
| Convert | <KPI> | <count> | <system> | <date range> |
| Engage | <KPI> | <count> | <system> | <date range> |

### Stage 2 — Conversion Rates & Benchmark

| Gate | Rate | Benchmark | Status |
|---|---|---|---|
| Reach → Act | _%  | _% | On-track / Underperforming / Outperforming |
| Act → Convert | _%  | _% | <...> |
| Convert → Engage | _%  | _% | <...> |
| Overall (Reach → Engage) | _%  | _% | <...> |

**Benchmark source:** <industry report, your 90th percentile, competitor proxy, etc.>

### Stage 3 — Bottleneck Identified

**First underperforming stage:** <Reach / Act / Convert / Engage>

**Evidence:** <quantified gap from benchmark, trend over time, or comparative data>

### Stage 4 — Diagnosis

**Input quality:** <Is the audience/traffic entering this stage correct?>

**Stage execution:** <Is the experience of this stage itself broken?>

**Output friction:** <Is the stage creating unnecessary barriers?>

### Sub-diagnostics

<Apply relevant checks from Phase 3 for the bottleneck stage>

### Hypotheses (ranked by likelihood × impact)

1. **Hypothesis:** <specific claim>
   - Likelihood: <high/medium/low — evidence>
   - Impact: <estimated % uplift if fixed>
   - Effort: <low/medium/high>
   - Leading indicator to test: <metric to watch>

2. **Hypothesis:** <...>

### Recommendation

**Action:** <Specific change to test or implement>

**Expected outcome:** <Quantified uplift; e.g., "Increase Act→Convert rate from 8% to 10%">

**Measure to confirm:** <Metric and threshold that validates the hypothesis>

### Confidence

<high | medium | low> — <justification; e.g., "high — data is recent and complete for all stages; benchmark is from peer set; hypothesis is supported by two independent signals (form drop-off data + chat sentiment)">
```
---
