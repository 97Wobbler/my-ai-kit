---
name: cohort-analysis
display_name: Cohort Analysis
class: lens
underlying_class: native
domain: data
source: Frederick F. Reichheld (Bain & Company, 1996); operationalized in SaaS retention metrics
best_for:
  - Tracking user/customer behavior over time buckets
  - Isolating cohort-specific trends from aggregate noise
  - Diagnosing product changes and their retention/engagement impact
one_liner: "Track user groups by time or attribute to diagnose trends and churn patterns."
---

# Cohort Analysis

## Overview

Cohort Analysis segments users or entities into groups (cohorts) based on a shared characteristic or entry time, then tracks their behavior over subsequent periods to isolate trends and measure the impact of product changes. Instead of looking at aggregate metrics that mask important variation, you observe how each cohort progresses independently. Practitioners use this when they need to distinguish natural decay from feature-driven changes, or when they suspect that different user segments behave fundamentally differently and therefore deserve separate measurement.

## Analytical Procedure

### Phase 1 — Define Cohort and Time Dimension

1. **Choose the cohort definition.** Decide whether you're grouping by:
   - **Temporal entry**: Users acquired in week 1, week 2, etc., or month-of-signup, or first-engagement-date.
   - **Trait**: Country, plan tier, referral source, feature enabled/disabled, or user segment.
   - **Event trigger**: Users who completed onboarding, users who made a purchase, users who saw a specific experiment variant.
   Write down the exact rule: *"Cohort = all users whose [attribute or event] occurred in [time bucket]."*

2. **Fix the time buckets.** Decide the granularity of the input dimension:
   - Weekly, monthly, or daily cohorts? (Weekly and monthly are most common.)
   - Is this cohort definition retroactive (apply it to historical data) or prospective (define it now and track forward)?

3. **Choose the observation metric and time scale.** Decide what you'll measure for each cohort over time:
   - Retention: % of cohort still active in week 1, week 2, week N.
   - Engagement: DAU, sessions, feature usage, or revenue per user.
   - Conversion: % of cohort who completed a target action.
   - Churn: % of cohort who disengaged.
   - Decide the observation window: days 0–7, days 8–14, days 15–30, etc., or cumulative.

4. **Establish the observation periods.** Write out your time grid:
   - Rows: each cohort (e.g., "Acquired week of Jan 1", "Acquired week of Jan 8").
   - Columns: each observation window (e.g., "Days 0–7", "Days 8–14", "Days 15–30").
   - The cell [cohort, window] contains the metric value (e.g., % retained, revenue).

### Phase 2 — Construct and Populate the Cohort Table

5. **Backfill or prospectively capture data.** Extract from your event log or user database:
   - For each cohort, count or sum the metric in each observation window.
   - Include only users who meet the cohort definition.
   - Exclude users who fall into multiple cohorts (enforce mutual exclusion).
   - Document any filtering rules (e.g., "exclude test accounts", "exclude users with zero activity").

6. **Organize the table.** Create a table with cohorts in rows and observation periods in columns. Each cell is the metric for that cohort in that period:

   | Cohort | Week 1 | Week 2 | Week 3 | Week 4 | Week 5 |
   |---|---|---|---|---|---|
   | Jan 1–7 | 95% | 82% | 71% | 61% | 52% |
   | Jan 8–14 | 93% | 79% | 68% | 58% | ... |
   | Jan 15–21 | 94% | 81% | 70% | ... | ... |

7. **Flag incomplete rows.** If a cohort is too recent to have full observation history, mark those cells as "not yet observed" rather than zero. Do not backfill or interpolate missing future values.

### Phase 3 — Analyze for Patterns and Shifts

8. **Read cohort curves.** For each row (cohort), observe the pattern over time:
   - Is the trend smooth and predictable (e.g., retention drops 10–15% per week)?
   - Are there cliffs or inflection points (sudden drop or flattening)?
   - Do older cohorts show different curves than newer cohorts?

9. **Diagnose cohort-to-cohort variation.** Compare the same observation window across different cohorts:
   - Do all cohorts start at roughly the same level (Week 1 retention), or does entry timing/trait produce persistent differences?
   - If Week 1 retention for Jan cohorts is 94% but Feb cohorts is 92%, that's a signal. Investigate: did onboarding change? Did traffic source change?

10. **Identify inflection points and correlate to events.** For each cohort, mark drops or flattening in the curve. Then cross-reference with your event log:
    - Product launch: did retention curves shift for cohorts entering after the launch?
    - Breaking bug: do cohorts overlap with the bug window show worse retention?
    - Feature removal: do cohorts before and after show different engagement trajectories?
    - Price change: do purchasing cohorts shift?
    Write the event, the cohort(s) affected, and the metric change (e.g., "Bug introduced Jan 15; cohorts entering Jan 15+ show 8% lower Week 2 retention").

11. **Segment for confounds.** If you see variation, test whether it's driven by the variable you think:
    - If trait-based cohorts (e.g., country), construct sub-cohorts: country=US + temporal, country=UK + temporal, etc., to separate geography from onboarding time.
    - If temporal cohorts, check: did traffic source or plan tier distribution change in that week? Create sub-cohorts by traffic source to isolate it.

### Phase 4 — Confidence and Next Steps

12. **Quantify the shift.** For any observed change in a cohort curve:
    - Calculate the effect size: **(new curve value – old curve value) / old curve value** as a percentage.
    - Note the sample size (# of users in each cohort).
    - If the sample is small (<100 users per cohort per window), flag low confidence.

13. **State the finding.** Write it as: *"Cohorts entering [after/before date/event] show [metric] X% [lower/higher] than prior cohorts in [observation window]."* Do not claim causation; causation requires experimentation or natural experiment validation (see Red Flags).

14. **Design a follow-up experiment if causation is in question.** If you suspect a feature or change caused the shift, plan an A/B test with a fresh cohort, hold all else equal, and measure the same metric. Document this as a separate investigation.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Cohort definition is explicit and unambiguous (rule written out) | Y/N |
| Cohort definition is mutually exclusive (no user in two cohorts) | Y/N |
| Metric choice is justified for the question being asked | Y/N |
| Time buckets are consistent across all cohorts | Y/N |
| Table is complete for observed periods; incomplete rows flagged clearly | Y/N |
| At least one product event/change is cross-referenced with cohort shifts | Y/N |
| Sample sizes are reported for each cohort | Y/N |
| No causation is claimed without justification or follow-up experiment | Y/N |

## Red Flags

- **Missing baseline.** You compare two cohorts but never establish whether the difference is large enough to matter. A 2% retention drop might be noise. Report absolute numbers and sample size so the reader can judge significance.
- **Shifting definitions.** Cohorts are redefined mid-analysis (e.g., "Week 1 = first 7 days, but Week 2 = days 8–14 for some cohorts and days 7–14 for others"). This invalidates comparison. Lock the definition upfront.
- **Causation claimed from observation.** "Cohorts after the feature launch show higher retention, therefore the feature works." Without A/B testing, this conflates the feature with other changes (seasonal demand, traffic source, pricing). Observation can only generate hypotheses, not proof.
- **Incomplete cohorts treated as zeros.** A cohort with fewer than N days of history should not be plotted as "0% retained in Week 4"; it should be marked "not yet observed." Mixing complete and incomplete cohorts distorts the visual story.
- **No event log cross-reference.** You plot cohort curves but never ask "what happened to the product on this date?" Purely visual cohort analysis misses the narrative — good analysis connects curves to events.
- **Sample size collapse.** Early observation windows have thousands of users per cohort, but later windows have hundreds (churn) or tens (observation period ends). Comparing Week 1 and Week 8 retention without noting the sample shrinkage overstates confidence in the later metric.

## Output Format

```
## Cohort Analysis Report

**Cohort Definition:**
<Explicit rule: "Cohort = all [users/entities] whose [attribute or entry event] occurred in [time bucket]">

**Metric:**
<What is being measured (retention, engagement, churn, revenue, etc.) and how it is calculated.>

**Time Grid:**
| Cohort | Observation Window 1 | Observation Window 2 | ... |
|---|---|---|---|
| <Cohort 1> | <metric> (n=X) | <metric> (n=Y) | ... |
| <Cohort 2> | <metric> (n=X) | <metric> (n=Y) | ... |

### Key Patterns
- **Within-cohort trend:** <Description of how the metric changes over time for a typical cohort. E.g., "Retention decays ~12% week-over-week until week 4, then stabilizes.">
- **Cohort-to-cohort variation:** <Does the starting level or trajectory differ across cohorts? E.g., "Cohorts entering in January start at 95% Week-1 retention; February cohorts start at 91%.">

### Inflection Points & Events
| Event | Date | Affected Cohorts | Metric Change | Magnitude |
|---|---|---|---|---|
| <Event name (e.g., "Feature X launch")> | <Date> | <Cohorts overlapping or entering after this date> | <Metric and direction (e.g., "Week 2 retention decreased")> | <% or absolute change> |

### Confound Analysis (if applicable)
<If multiple variables are at play, describe how you isolated the primary driver.>
Example: "Controlled for traffic source by creating sub-cohorts (Organic, Paid) within each temporal cohort. Paid cohorts show consistent 5% lower retention; temporal effects persist independently."

### Findings
1. <Observation from the cohort curve, tied to a metric change and a time window.>
2. <...>

### Limitations & Next Steps
- <Sample size or observation period constraint, if applicable.>
- <Hypothesis requiring follow-up experimentation, if causation is in question.>

**Confidence: <high | medium | low>** — <Justification. Include sample size, observation window completeness, number of cohorts, and clarity of the event/change being measured.>
```
---
