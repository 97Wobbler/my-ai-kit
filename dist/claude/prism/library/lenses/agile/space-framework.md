---
name: space-framework
display_name: SPACE Framework
class: lens
underlying_class: native
domain: agile
source: Will Larson, Stripe (2019); refined in "An Elegant Puzzle"
best_for:
  - Diagnosing developer productivity bottlenecks across multiple dimensions
  - Aligning team structure and process to remove friction
  - Measuring and tracking organizational health signals
one_liner: "Diagnose developer productivity along five axes to find root causes of organizational friction."
---

# SPACE Framework

## Overview

SPACE is a five-axis diagnostic for measuring and improving developer productivity. Rather than conflating productivity with output volume (lines of code, tickets closed), SPACE separates the sources of friction into distinct, independently measurable dimensions: **Satisfaction**, **Performance**, **Activity**, **Collaboration**, and **Efficiency**. Practitioners use this lens when productivity is declining but the cause is opaque—e.g., "we're shipping less despite hiring more"—or when a specific bottleneck (e.g., slow tests) is masking broader systemic issues.

## Analytical Procedure

### Phase 1 — Baseline Measurement

1. **Define the team or system boundary.** Who are you measuring? (e.g., a single product team, backend infrastructure, the entire engineering org). Write it down with scope and any nested sub-teams.

2. **For each of the five SPACE dimensions, select a metric or proxy:**
   - **Satisfaction**: developer survey (eNPS, role satisfaction), retention rate, voluntary attrition rate, or quarterly pulse responses.
   - **Performance**: time-to-code-review (median and p95), deployment frequency, incident response time, or customer-reported time-to-value for features.
   - **Activity**: commits per developer per week, PRs merged, or hours spent in meetings (as a counter-metric—higher is bad).
   - **Collaboration**: code review turn-around time, cross-team dependency time-to-resolve, or incident post-mortems completed.
   - **Efficiency**: build/test cycle time (local and CI), time spent on rework vs. new work, or deployment success rate (inverse of rollback rate).

3. **Collect baseline data for each metric over a 2–4 week window.** Use existing telemetry (Git logs, CI/CD dashboards, surveys, time-tracking). Do not guess. If data is unavailable, note this as a gap.

4. **Plot each metric on a simple scale (poor/fair/good/excellent).** Use historical data or peer benchmarks if available. The goal is a 5-cell grid, one cell per dimension, showing relative health.

### Phase 2 — Identify Decline or Misalignment

5. **Compare the baseline to a previous window (3–6 months ago, or last sprint).** Which dimensions have degraded? Which are stable or improving? Rank by magnitude of change.

6. **For each degraded dimension, list the hypothesized root causes.** Examples:
   - Satisfaction down → recent reorg, increased on-call burden, unclear roadmap, salary/comp concerns.
   - Performance down → new architecture causing deployment friction, reviewer availability, flaky tests.
   - Activity up (if paired with satisfaction down) → scope creep, poor prioritization, thrashing.
   - Collaboration delays → time zone fragmentation, missing decision-making forums, unclear ownership.
   - Efficiency down → slow CI, legacy code, technical debt accumulation, frequent context switches.

7. **Cross-reference degradation patterns.** Multiple dimensions declining usually points to a structural issue (e.g., understaffing, unfinished migration, unclear process). Single-dimension decline often points to a specific bottleneck (e.g., a reviewer, a tool, a person).

### Phase 3 — Depth Interview (Optional but Recommended)

8. **For the top 2–3 degraded dimensions, conduct 30-minute 1:1 interviews with 3–5 team members.** Ask open-ended questions:
   - "What's making it harder to [ship quickly / feel good about the work / collaborate] right now?"
   - "What takes the most time that feels like friction vs. useful work?"
   - "What would unblock you most in the next month?"
   
   Do not lead. Write verbatim quotes, not summaries.

9. **Cluster the verbatim responses by theme.** Do 3+ people independently mention the same bottleneck? That's a signal. Single mentions are flavor, not signal.

### Phase 4 — Isolate Actionable Deltas

10. **For each degraded dimension, rank potential interventions by (impact × effort^-1).** High impact, low effort first. Example interventions:
    - Satisfaction: rotate on-call, publish roadmap, conduct skip-level 1:1s.
    - Performance: parallelize CI jobs, reduce PR review queue via async review norms, fix top 3 flaky tests.
    - Activity: cancel recurring meetings, tighten sprint scope, reduce Slack interrupt frequency.
    - Collaboration: establish decision templates, clarify ownership, add cross-team sync.
    - Efficiency: profile CI/test suite, batch rework, migrate off legacy tooling.

11. **Run a small experiment on one intervention.** One dimension, one change, two weeks. Measure the same metrics again. Did the degraded dimension improve? By how much? Did another dimension worsen as a side effect?

## Evaluation Criteria

| Check | Pass |
|---|---|
| All five SPACE dimensions have at least one concrete metric | Y/N |
| Baseline data is collected, not estimated | Y/N |
| At least one prior window (3–6 months) is available for comparison | Y/N |
| Degraded dimensions are ranked by magnitude of change | Y/N |
| Interview feedback is clustered by theme, not summarized | Y/N |
| Interventions for top deltas are ranked by (impact / effort) | Y/N |
| A test intervention was run and re-measured | Y/N |

## Red Flags

- All five dimensions show equal degradation. This usually means the team is understaffed, not that five separate problems emerged. Reframe the investigation as "are we running out of capacity?" before treating each dimension separately.
- Satisfaction is high while performance and efficiency are low. The team may not be aware of the magnitude of the problem (data lag) or may be prioritizing other work. Investigate disconnect before intervening.
- Interviews reveal a single root cause (e.g., one person is a bottleneck) but the framework implicates three dimensions. Solve the root cause. SPACE is a diagnostic, not a solution.
- No data was collected for a dimension; intervals are used instead. Confidence in that dimension's findings is low. Collect data before acting.
- Intervention was run, but re-measurement used different definitions or time windows than the baseline. You cannot compare; run again with consistent definitions.

## Output Format

```
## SPACE Framework Assessment

**Team/scope:**
<definition>

### Baseline Metrics (Window: <date range>)
| Dimension | Metric | Value | Scale (poor–excellent) |
|---|---|---|---|
| Satisfaction | <metric> | <value> | fair |
| Performance | <metric> | <value> | good |
| Activity | <metric> | <value> | good |
| Collaboration | <metric> | <value> | poor |
| Efficiency | <metric> | <value> | fair |

### Comparison to Prior Window (<prior date range>)
| Dimension | Prior | Current | Change |
|---|---|---|---|
| Satisfaction | good | fair | ↓ -1 |
| Performance | excellent | good | ↓ -1 |
| Activity | fair | fair | — |
| Collaboration | fair | poor | ↓ -1 |
| Efficiency | good | fair | ↓ -1 |

**Rank of degraded dimensions (by magnitude):**
1. Collaboration (dropped 1 level, tied for most)
2. Efficiency (dropped 1 level, tied for most)
3. Performance (dropped 1 level, tied for most)

### Root Cause Hypotheses
**Performance:** slow CI (median 12m, p95 25m) | new review queue backlog (2+ days) | flaky integration tests (8% failure rate)
**Collaboration:** async review norms not established | time zone fragmentation (4 zones) | no decision log maintained
**Efficiency:** legacy codebase (30% of time in rework) | build times (15m local, 20m CI)

### Interview Findings (5 respondents, 2-week window)
**Collaboration theme:** "Hard to get review feedback across zones" (3/5) | "Unclear who owns which service" (2/5)
**Efficiency theme:** "Local build is slow and flaky" (4/5) | "Spend too much time debugging old code" (3/5)
**Satisfaction theme:** "Blocked by infra review queue" (2/5) | "Too many meetings" (2/5)

### High-Impact, Low-Effort Interventions
1. **Async review norms:** post-review SLA (24h), reduced blocking approval rules → impact: reduce Collaboration delay 2–3 days, lift Performance 1 level. Effort: 1 week.
2. **Parallelize CI jobs:** split test suites by domain → impact: reduce Efficiency bottleneck by 5–7m, lift Performance 1 level. Effort: 2 weeks.
3. **Cancel 3 low-value meetings:** audit recurring syncs → impact: recover 2–3 hours/week per developer, lift Activity and Satisfaction. Effort: <1 week.

### Test Intervention
**Intervention:** Implement async review norms (24h SLA, auto-approval for docs/config).
**Duration:** 2 weeks.
**Re-measurement:**
- Performance (PR review time): median 4h → 2h, p95 18h → 8h. ✓ Improved.
- Collaboration: anecdotal reports of "less blocked by reviews." Pending next survey.
- Side effects: No regressions detected.

### Confidence
<high | medium | low> — <justification. E.g., "high — baseline data collected from logs, interviews clustered themes, test intervention was measured with same definitions.">
```
---
