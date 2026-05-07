---
name: aarrr-pirate-metrics
display_name: AARRR Pirate Metrics
class: lens
underlying_class: native
domain: product-management
source: Dave McClure, 2007
best_for:
  - Diagnosing which stage of the user lifecycle is underperforming
  - Allocating optimization effort across acquisition, activation, retention, referral, and revenue
  - Communicating product health to non-technical stakeholders
one_liner: "Measure conversion and churn across the five-stage user lifecycle — Acquisition, Activation, Retention, Referral, Revenue."
---

# AARRR Pirate Metrics

## Overview
AARRR Pirate Metrics breaks down the user lifecycle into five sequential funnels—Acquisition, Activation, Retention, Referral, and Revenue—each with a conversion rate and behavioral threshold. Rather than treating "users" as a single blob, the lens forces you to measure where you leak: do people arrive but never come back? Do they activate but never pay? Do they pay but never refer? Practitioners use this when they suspect a product bottleneck exists somewhere but don't know where, or when they need a common diagnostic language across engineering, marketing, and finance teams.

## Analytical Procedure

### Phase 1 — Define the Five Stages

1. **Acquisition.** A prospect completes whatever action brings them into your product's orbit: they visit your landing page, install the app, sign up for the waitlist, or click through a paid ad. Define the specific event that counts as "acquired." Write it down.
   - Bad: "We acquire users."
   - Good: "A user is acquired the moment they complete the signup form and verify their email."

2. **Activation.** A user takes the core action that demonstrates they "get" the product. Activation is *not* signup — it's the first meaningful use. Examples: uploading a document, creating their first project, configuring a profile, running a query, or watching a tutorial.
   - Define the event. Be specific about which action signals "this user understands what they bought."

3. **Retention.** A user returns to the product after their first session and engages with it again. Choose a time window (daily, weekly, or monthly depending on your product cadence) and define what counts as "active" in that window (e.g., "logged in and performed an action").
   - Specify: "We measure retention as % of Day 1 activators who return and engage at least once in Week 1."

4. **Referral.** A user invites, shares with, or recommends the product to someone outside your current user base, resulting in that person attempting to use the product.
   - Define the referral event: Does a share count? An invite? A link click? Or only if the referred person signs up?

5. **Revenue.** A user generates direct economic value. This may be a subscription purchase, a one-time payment, an ad impression, or a transaction fee.
   - Define what counts as a revenue event in your business model.

### Phase 2 — Instrument the Funnel

6. **For each stage, identify the source-of-truth metric.** You need:
   - Total count of users reaching this stage in a time window (e.g., a calendar month)
   - Count of users moving to the next stage in the same window
   - Conversion rate = (next stage count) / (current stage count)

7. **Map these metrics to your analytics system.** If you use Amplitude, Mixpanel, Google Analytics, or custom instrumentation, write down which event(s) feed each stage. If events are missing, add them now — do not estimate or guess.

8. **Choose a measurement window.** Monthly cohorts are standard (all users acquired in April, all in May, etc.). Running weekly cohorts can expose faster feedback but are noisier. Pick one and hold it constant across all five stages.

### Phase 3 — Compute Conversion Rates and Identify the Leak

9. **For each stage, calculate the conversion rate to the next stage.** Use the formula:
   ```
   Conversion(X→Y) = (Users reaching Y in window) / (Users reaching X in window)
   ```
   Record this as a percentage.

10. **Rank the five conversion rates from highest to lowest.** The lowest rate is your biggest leak — the stage where you lose the most users proportionally.

11. **Benchmark each rate against your own history and against industry peers.** Examples (rough, product-dependent):
    - Acquisition→Activation: 20–60% (landing page visitors who sign up)
    - Activation→Retention (week 1): 30–70% (new users who return)
    - Retention→Referral: 1–10% (active users who refer)
    - Retention→Revenue (if applicable): 5–20% (free users who convert to paid)
    
    If your rate is far below peer data, investigate why.

12. **Identify the "critical bottleneck."** This is the stage transition with the lowest conversion rate. This is where optimization effort pays the highest ROI.

### Phase 4 — Diagnostic Drill-Down

13. **For the critical bottleneck, apply cohort analysis.** Split the input cohort by:
    - Acquisition channel (organic vs. paid vs. partnership)
    - User segment (geography, device type, user persona)
    - Time period (week-over-week or month-over-month)
    
    Calculate conversion rates for each slice. If one channel or segment has a much lower rate, you've narrowed the problem.

14. **Examine the behavioral path of non-converters.** For users who reached stage X but not stage X+1:
    - Did they abandon mid-flow (i.e., incomplete action)?
    - Did they try and fail (error logs)?
    - Did they succeed but never return (churn after stage X)?
    - Did they disengage gradually (declining session frequency)?
    
    This distinguishes "hard friction" (they tried and hit a blocker) from "soft friction" (they lost interest).

15. **Generate a hypothesis.** Based on steps 13–14, propose one root cause and a single, testable intervention. Examples:
    - "Activation bottleneck is driven by organic users from SEO; they are less intent-driven and need in-product onboarding. Test: add a 3-step interactive tutorial."
    - "Referral rate is 0% because we've never built a refer button. Test: add a share modal to the dashboard."

### Phase 5 — Iteration and Re-Measurement

16. **Run the intervention.** Ship the fix and let it run for one full measurement window (usually a month) so the cohort reaches a steady state.

17. **Re-measure the conversion rate for that stage.** Compare new rate to baseline. If the rate improved, the hypothesis was directionally correct. Quantify the lift.

18. **Update all five rates and re-rank them.** The bottleneck may shift. Repeat from step 12.

## Evaluation Criteria

| Check | Pass |
|---|---|
| All five stages are defined with concrete, event-based criteria | Y/N |
| Each stage has a source-of-truth metric mapped to your analytics system | Y/N |
| Measurement window is consistent (e.g., monthly cohorts) across all five stages | Y/N |
| All five conversion rates are calculated | Y/N |
| Conversion rates are ranked and the critical bottleneck is identified | Y/N |
| Critical bottleneck has been analyzed by cohort or segment | Y/N |
| Root cause hypothesis for the bottleneck is stated and testable | Y/N |
| Hypothesis has been (or will be) tested with a concrete intervention | Y/N |

## Red Flags

- One or more stages lack a clear metric or source of truth. You will measure gut feelings, not data.
- Conversion rates are missing or inconsistent across time windows. If you measure Acquisition one way in month 1 and another way in month 2, the trend is meaningless.
- All five conversion rates are above 50%. Either the product is genuinely exceptional (rare) or stages are defined too loosely (likely). "User engagement" is not a stage; "user ran a saved query for the second time in week 2" is.
- The bottleneck was identified but no cohort drill-down was performed. You know *where* you leak but not *why*. Recommendations will be generic.
- The hypothesis is vague ("improve onboarding") or unfalsifiable ("increase user intent"). It will not yield actionable results when tested.
- No re-measurement after intervention. The full cycle requires evidence that the fix actually moved the needle.

## Output Format

```
## AARRR Assessment

### Stage Definitions
| Stage | Event | Metric |
|---|---|---|
| Acquisition | <event> | <metric definition> |
| Activation | <event> | <metric definition> |
| Retention | <event> | <metric definition> |
| Referral | <event> | <metric definition> |
| Revenue | <event> | <metric definition> |

### Conversion Rates (Measurement Window: <date range>)
| Transition | Cohort Size (n) | Converters | Rate |
|---|---|---|---|
| Acquisition → Activation | <n> | <n> | <x>% |
| Activation → Retention | <n> | <n> | <x>% |
| Retention → Referral | <n> | <n> | <x>% |
| Retention → Revenue | <n> | <n> | <x>% |

### Critical Bottleneck
**Stage transition:** <X → Y>
**Current rate:** <x>%
**Peer benchmark:** <y>% (if available)
**Gap:** <z>% below peer average

### Cohort Analysis of Bottleneck
| Segment | Conversion Rate | Sample Size | Notes |
|---|---|---|---|
| <slice> | <x>% | <n> | <difference from overall> |

### Root Cause Hypothesis
**Hypothesis:** <testable statement>
**Evidence:** <from behavioral path analysis>
**Intervention:** <specific change to measure>

### Confidence
<high/medium/low> — <justification: Is the data reliable? Is the bottleneck clearly defined? Is the hypothesis grounded in observed user behavior or speculation?>
```
