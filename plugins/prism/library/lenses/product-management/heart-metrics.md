---
name: heart-metrics
display_name: HEART Metrics
class: lens
underlying_class: native
domain: product-management
source: Google (Kerry, Rodden, Peach; 2010)
best_for:
  - Measuring user experience holistically across five dimensions
  - Defining success metrics for product features and user flows
  - Diagnosing why a product change succeeded or failed
one_liner: "Integrated UX measurement — Happiness, Engagement, Adoption, Retention, Task Success."
---

# HEART Metrics

## Overview
HEART is a framework for defining and measuring the health of a product or feature across five user-centric dimensions: Happiness (user satisfaction), Engagement (frequency and intensity of use), Adoption (new user uptake), Retention (repeat usage), and Task Success (completion rates and efficiency). Rather than optimizing a single metric in isolation, practitioners use HEART to ensure that product improvements don't trade off user satisfaction for adoption, or retention for task efficiency. The framework operates on product features or entire user flows and forces teams to articulate success criteria *before* shipping.

## Analytical Procedure

### Phase 1 — Define the Scope

1. **Identify the product element.** What is the target of measurement — a new feature, a user flow, an entire product surface, or a cohort interaction pattern? Write it in one sentence. Example: "The email campaign creation workflow for first-time newsletter senders."

2. **Establish the measurement window.** When will you measure? (e.g., 4 weeks post-launch, 90 days, first 6 months). Some dimensions (Adoption) are front-loaded; others (Retention) reveal later. Commit to a timeline before launching.

3. **Define your user cohort.** Who are you measuring — all users, new users only, power users, a specific segment? Granular cohorts expose patterns that aggregate metrics hide. Document it explicitly.

### Phase 2 — Operationalize Each Dimension

For each of the five HEART dimensions below, define *one primary metric* and *one supporting metric*. The primary metric is what you'll track; the supporting metric is your pressure-test (does the primary metric mask a problem?).

#### Happiness
- **What to measure:** User satisfaction with the feature or experience.
- **Primary metric:** Net Promoter Score (NPS) or user satisfaction survey (Likert scale, 1–5) administered to a representative sample within the measurement window.
- **Supporting metric:** Complaint or support ticket volume related to this feature. A rise in help requests despite high NPS signals a usability mismatch or frustration point.
- **Concrete step:** If using NPS, send a survey to 10–20% of active users in the cohort within 2 weeks of engagement. If using Likert, embed a single rating question in-product post-task. Target 15% response rate minimum.

#### Engagement
- **What to measure:** How actively users interact with the feature (frequency, duration, depth).
- **Primary metric:** DAU/WAU ratio (daily/weekly active users) or daily/weekly interaction frequency among cohort users. Example: "Sessions/user/day" or "feature opens per user per week."
- **Supporting metric:** Time spent in feature per session, or session length distribution (median, p90). High frequency with sub-second sessions signals low engagement depth.
- **Concrete step:** Instrument the feature to log entry, interaction, and exit events. Compute median session length and DAU/WAU for the cohort weekly. Flag if frequency rises but duration drops.

#### Adoption
- **What to measure:** What fraction of eligible users activate the feature and how quickly.
- **Primary metric:** Day-1, Day-7, and Day-30 adoption rates: (new users who used feature at least once / total new users) on each day, computed weekly.
- **Supporting metric:** Time-to-adoption distribution (median days from account creation to first feature use). A high adoption rate paired with long tail adoption (p90 >> median) suggests onboarding friction.
- **Concrete step:** Identify new user cohorts by signup date. For each cohort, track % who used the feature by Day 1, 7, and 30. Plot adoption curves; flag if adoption stalls before Day 7.

#### Retention
- **What to measure:** Repeat usage — whether users come back after initial encounter.
- **Primary metric:** D7/D30/D90 retention: % of users active in the feature in weeks 1 / 4 / 12 after first use. (Cohort retention, not rolling retention.)
- **Supporting metric:** Churn rate by feature usage intensity: % of users who used the feature 1x, 2–5x, and 10+x, who are still active 30 days later. Identify the "stickiness threshold."
- **Concrete step:** Segment users by feature usage intensity (1x, 2–5x, 10+ uses in week 1). Track % of each segment active 30, 90, and 180 days later. A sharp cliff after 2 uses indicates the feature doesn't retain.

#### Task Success
- **What to measure:** Can users complete the primary goal of the feature efficiently?
- **Primary metric:** Task completion rate: % of sessions that reach the goal state (order placed, video watched, file uploaded, etc.). For flows with multiple steps, track step-wise completion drop-off.
- **Supporting metric:** Time-to-completion or interaction efficiency (steps / task / user or clicks to success). A high completion rate paired with high latency signals friction or low confidence.
- **Concrete step:** Define the "success state" for the feature (e.g., "form submitted"). Instrument step-by-step. Compute: (sessions reaching success state / total sessions). Compute median time-to-success and step-wise drop-off. Flag any drop >15% between adjacent steps.

### Phase 3 — Set Thresholds and Baselines

4. **Define targets for each metric.** What does "good" look like? Consult historical data (comparable features, competitor benchmarks, industry standards if available). Write down explicit targets:
   - Happiness: NPS ≥ 30 or 75% at 4–5 on Likert scale
   - Engagement: DAU/WAU ≥ 0.15 (or specify sessions/user/week)
   - Adoption: 30% by Day 7, 50% by Day 30
   - Retention: 60% D7, 40% D30
   - Task Success: 85% completion rate, <5 steps median

5. **Collect baseline data (if feature exists) or establish launch-day snapshots.** For new features, measure the 48 hours post-launch to establish a baseline; then measure 1, 4, and 12 weeks out.

### Phase 4 — Analyze and Diagnose

6. **Run the measurement.** Collect all five primary + five supporting metrics at the end of the measurement window.

7. **Plot each dimension against target.** Create a simple table or radar chart:
   - Metric name | Target | Observed | Gap | Status (green/yellow/red)

8. **Diagnose misses.** If one dimension falls short, cross-reference the supporting metric:
   - Happiness low, but complaints stable? → UX debt, not feature fault. Consider incremental refinement.
   - Engagement low and supporting metric (time/session) also low? → Low perceived value or onboarding gap.
   - Adoption high, Retention low? → Curiosity-driven first use, but no repeat value. Feature scope is too narrow or users hit an unmet need and left.
   - Task Success low? → Check step-wise drop-off. High drop at step N reveals the problem. Redesign that step.

9. **Cross-dimension patterns.** Look for tension:
   - High Happiness + low Engagement → Users like the feature but don't use it (nice-to-have, not must-have).
   - High Adoption + high Task Success + low Retention → Feature is easy but not useful for repeat work.
   - All high except Task Success → Friction somewhere in the flow. Users see value but can't execute reliably.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Scope (product element, window, cohort) is stated explicitly in one sentence each | Y/N |
| All five HEART dimensions have a primary metric and a supporting metric | Y/N |
| Primary metrics are operationalized (event names, SQL queries, or sample frames are specified) | Y/N |
| Measurement window and cohort definition prevent conflation (new users ≠ all users) | Y/N |
| Targets are set *before* measurement begins, with external justification | Y/N |
| Supporting metrics reveal what primary metrics hide (e.g., frequency vs. depth) | Y/N |
| Step-by-step drop-off (Task Success) or intensity cohorts (Retention) are tracked, not just aggregates | Y/N |

## Red Flags

- Only one HEART dimension is measured; the rest are ignored. This is not HEART — it's optimizing a single metric.
- Targets are vague or absent ("engagement should be high"). Without targets, you cannot distinguish signal from noise.
- The measurement window is too short for Retention or too long for Adoption to show meaningful variance (measure Adoption in week 1–2, Retention starting week 3).
- Supporting metrics are not used. If Happiness is high but complaints are rising, you've missed a signal that a single aggregate hides.
- Task Success completion rate is measured as an aggregate, not step-by-step. You cannot diagnose where friction lives.
- Adoption and Retention are measured from "first signup" instead of "first feature use" — conflating product-wide onboarding with feature adoption.
- No cross-dimension analysis. Numbers are reported in isolation; the story of tension (high X, low Y) is never told.

## Output Format

```
## HEART Metrics Report

**Scope:**
- Feature/flow: <...>
- Measurement window: <date start> to <date end>
- Cohort: <user segment and size>

### Targets and Baselines
| Dimension | Metric | Target | Baseline (if applicable) |
|---|---|---|---|
| Happiness | <primary> | <target> | <...> |
| Engagement | <primary> | <target> | <...> |
| Adoption | <primary> | <target> | <...> |
| Retention | <primary> | <target> | <...> |
| Task Success | <primary> | <target> | <...> |

### Measurement Results
| Dimension | Primary Metric | Observed | Supporting Metric | Observed | Status |
|---|---|---|---|---|---|
| Happiness | NPS / Likert | <value> | Complaint volume | <count> | 🟢/🟡/🔴 |
| Engagement | DAU/WAU or freq. | <value> | Median session time | <value> | 🟢/🟡/🔴 |
| Adoption | D7 / D30 adoption % | <value>% | Median time-to-adoption | <days> | 🟢/🟡/🔴 |
| Retention | D7 / D30 retention % | <value>% | Churn by intensity cohort | <distribution> | 🟢/🟡/🔴 |
| Task Success | Completion rate | <value>% | Median time-to-completion | <time> | 🟢/🟡/🔴 |

### Step-by-Step Drop-Off (Task Success only)
| Step | Session %→Next | Observations |
|---|---|---|
| Entry | — | <...> |
| Step 1 | <drop%> | <friction point if >15%> |
| Step 2 | <drop%> | <...> |
| Success | <final%> | <...> |

### Cross-Dimension Diagnosis
<Identify patterns of tension or alignment. Example: "High Adoption + Low Retention = users are curious but not returning; feature scope may be too narrow." OR "High Happiness + Low Engagement = nice-to-have, not must-have; consider repositioning or additional use cases.">

### Recommendations
1. <Priority recommendation with dimension and metric justification>
2. ...

### Confidence
<high | medium | low> — <justification: which dimensions have solid data, which are underpowered or conflated, external factors affecting results>
```
