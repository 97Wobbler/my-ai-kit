---
name: dora-metrics
display_name: DORA Metrics
class: lens
underlying_class: native
domain: agile
source: Nicole Forsgren, Jez Humble, Gene Kim; "Accelerate" (2018)
best_for:
  - Measuring delivery performance across teams and pipelines
  - Identifying bottlenecks in deployment velocity and stability
  - Tracking operational resilience and incident response capability
one_liner: "Measure software delivery capability via deployment frequency, lead time, MTTR, and change failure rate."
---

# DORA Metrics

## Overview

DORA (DevOps Research and Assessment) Metrics quantify software delivery performance along four dimensions: how often you deploy, how long from commit to production, how quickly you recover from failures, and what fraction of changes break in production. Teams use this lens to move beyond vanity metrics (lines of code, velocity points) to signals that correlate with business outcomes. The discipline is rigorous measurement — most teams measure deployment frequency accurately but conflate MTTR with incident detection time, or include only major incidents in failure rate, introducing systematic bias.

## Analytical Procedure

### Phase 1 — Define the Four Metrics

For each metric below, establish a clear measurement definition before collecting data. Ambiguity here propagates through all downstream analysis.

1. **Deployment Frequency (DF)**
   - Count the number of production deployments per calendar unit (day, week, month).
   - Include only deployments that reach end users or production systems.
   - Exclude rollbacks, hotfixes to staging, and internal-only releases.
   - Decision point: Are blue-green deployments counted once (at cutover) or twice (one per environment)?
   - Record definition in writing before measurement begins.

2. **Lead Time for Changes (LTC)**
   - Measure the span from first commit to production readiness (merged to main, or equivalent deployment trigger).
   - Start: timestamp of the earliest commit in the change.
   - End: timestamp of deployment to production (or to a production-ready stage if staged rollouts are standard).
   - Exclude: time in manual approval queues, time waiting for a deployment window, or time code sits in a staging environment after readiness.
   - Decision point: Do you measure median LTC, or separately track fast changes (e.g., hotfixes) and slow changes?
   - Document the decision and stick to it across measurement periods.

3. **Mean Time to Recovery (MTTR)**
   - Measure the average duration from incident start (detected) to incident end (resolved in production).
   - Start: timestamp when incident is first detected or reported (not when root cause is found).
   - End: timestamp when the system is fully operational for end users (not when "fix deployed" but when users are unblocked).
   - Include: all incidents that caused user-facing degradation, not just major outages.
   - Decision point: Do you include degradation (slow API responses) or only complete unavailability?
   - Clarify the threshold in writing.

4. **Change Failure Rate (CFR)**
   - Calculate: (number of deployments causing user-facing incidents or rollbacks) / (total deployments) × 100%.
   - Incident definition: Any unplanned outage, data corruption, security breach, or missing feature flag caused by a specific deployment.
   - Rollback definition: Automated or manual revert to a prior version within 24 hours of deployment.
   - Decision point: Do you count only P1 incidents, or all user-facing issues?
   - Document and audit weekly to catch silent failures.

### Phase 2 — Establish Data Collection

5. **Identify data sources.**
   - Deployment Frequency: CI/CD pipeline logs, deployment tool (e.g., Spinnaker, ArgoCD, GitHub Actions). Source of truth: git tags or CD tool events.
   - Lead Time: VCS commit timestamps and CD deployment logs. Correlate by commit SHA.
   - MTTR: Incident tracking system (PagerDuty, Opsgenie, Jira Service Desk) or post-mortems. Manual post-incident review if logs are sparse.
   - Change Failure Rate: Deployment logs + incident tracking system. Cross-reference by date window and changed services.

6. **Automate collection where possible.**
   - Query CI/CD API (GitHub, GitLab, Jenkins) for deployment events.
   - Poll incident management API for resolved incidents.
   - Export weekly or daily aggregates to a single source (spreadsheet, time-series DB, observability platform).
   - Alert if any metric becomes stale (e.g., no DF data for 7 days indicates tooling failure).

7. **Validate the data pipeline.**
   - Spot-check 10% of deployments manually against the data set.
   - Audit MTTR calculations for 3 recent incidents: verify start/end timestamps match incident notes.
   - Test the pipeline once with known test data (e.g., deploy a canary change, confirm it appears in DF count within 1 hour).

### Phase 3 — Measure and Trend

8. **Collect baseline metrics for 4 weeks minimum.** Do not take action on a single week; weekly variance is normal.

9. **Calculate rolling averages.**
   - DF: count deployments per week, then average the last 4 weeks.
   - LTC: median of all commits deployed in the last 4 weeks.
   - MTTR: mean of all resolved incidents in the last 4 weeks. If <5 incidents, extend the window.
   - CFR: (count of bad deployments in last 4 weeks) / (total deployments in last 4 weeks).

10. **Plot trends over 8–12 weeks.** Look for direction:
    - Improving DF but worsening CFR? Suggests lower quality gates or skipped testing.
    - Stable DF but rising MTTR? Suggests system complexity or observability gaps.
    - LTC rising? Bottleneck is likely in review, testing, or approval processes.

### Phase 4 — Interpret and Act

11. **Classify the team by DORA tier** (High, Medium, Low) using the published thresholds as a reference:
    - **Deployment Frequency:** High ≥ daily, Medium = weekly–monthly, Low < monthly.
    - **Lead Time:** High < 1 day, Medium = 1–7 days, Low = 1–6 months.
    - **MTTR:** High < 1 hour, Medium = 1–24 hours, Low > 24 hours.
    - **Change Failure Rate:** High < 15%, Medium = 15–45%, Low > 45%.

12. **Identify mismatches.** Teams rarely align on all four. Document what's imbalanced:
    - High DF + high CFR = "fast but broken" (speed without safety gates).
    - Low DF + low MTTR = "rare deployments but they're reliable" (low risk, low opportunity).
    - High DF + low MTTR but high LTC = "deployment capacity exists but changes are stuck in review."

13. **Trace each metric to root causes with a 5-Whys session:**
    - Why is LTC 10 days? → code reviews take 4 days. Why? → averaging 15 PRs/day, 3 reviewers. Why? → no bot-driven lint/test, so reviews check basics. Why? → no CI linting configured. → Action: add CI linting.
    - Why is CFR 35%? → 7 of 20 deployments broke in last month. What broke? → 3 database migrations, 2 config pushes, 2 feature flags. → Action: audit migration process and feature-flag rollout strategy separately.

14. **Set a target for the next quarter** and assign ownership. Example:
    - Target: LTC < 5 days (from 10), by reducing review latency via async reviews + bot checks.
    - Owner: Platform team. Measurement: weekly LTC percentile, track top-5 slowest PRs.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Definitions for all four metrics are written and unambiguous | Y/N |
| Data sources for each metric are identified and automated | Y/N |
| Baseline data covers ≥4 weeks | Y/N |
| Rolling 4-week averages calculated for all metrics | Y/N |
| Team is classified into DORA tier (H/M/L) on all four dimensions | Y/N |
| At least one metric imbalance is identified with a 5-Whys root cause | Y/N |
| Next-quarter target and owner assigned to at least one metric | Y/N |

## Red Flags

- Definitions are vague or include contradictions (e.g., "DF includes hotfixes but excludes emergency patches"). Measurements will be inconsistent.
- Data comes from manual spreadsheets or memory. Manual collection fails at scale; failures go unreported; trends are invisible.
- Only one or two metrics are measured well; others are estimated or missing. Imbalance analysis is impossible.
- Metrics improve across the board every quarter with no plateaus. Either measurement is gaming (e.g., deployments are being split to inflate DF) or targets are too low.
- MTTR includes time spent in war rooms after incident resolution. The metric becomes a proxy for incident severity, not recovery speed.
- Change Failure Rate is calculated only from P1 incidents. All other failures are invisible, inflating confidence.
- Team achieved "High" tier on DF but LTC is unmeasured, and CFR is unknown. Speed without safety is a red flag.

## Output Format

```
## DORA Assessment

**Team / Pipeline:** <name>
**Measurement period:** <start date> to <end date> (≥4 weeks)

### Metric Definitions
- Deployment Frequency: <definition; how splits/rollbacks are handled>
- Lead Time for Changes: <definition; inclusion/exclusion of queue time>
- MTTR: <definition; incident threshold>
- Change Failure Rate: <definition; incident severity threshold>

### Baseline Data (4-week rolling average)
| Metric | Value | DORA Tier | Trend (past 8 weeks) |
|---|---|---|---|
| Deployment Frequency | <e.g., 4.2 per day> | High | ↑ improving |
| Lead Time for Changes | <e.g., 3.1 days, median> | High | → stable |
| MTTR | <e.g., 42 min, mean> | Medium | ↓ worsening |
| Change Failure Rate | <e.g., 8.5%> | High | ↑ worsening |

### Tier Classification
- High / Medium / Low on each dimension.
- Imbalance observed: <e.g., "High DF, Medium CFR — suggests speed bias">

### Root Cause Analysis (5-Whys)
**Metric:** <name of metric causing concern>
| Why Level | Answer |
|---|---|
| Why1 | <...> |
| Why2 | <...> |
| Why3 | <...> |
| Why4 | <...> |
| Why5 | <...> |

**Action:** <specific, ownable intervention>

### Next Quarter Target
| Metric | Current | Target | Owner | Key Action |
|---|---|---|---|---|
| <...> | <...> | <...> | <...> | <...> |

### Confidence
<high | medium | low> — <justification, e.g., "high: definitions are locked, data sources automated, baseline is 8 weeks, no manual steps"; or "low: MTTR data is sparse (3 incidents total), LTC includes queue time which may bias upward">
```
