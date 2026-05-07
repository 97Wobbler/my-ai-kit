---
name: takt-time-cycle-time-lead-time
display_name: Takt Time / Cycle Time / Lead Time
class: lens
underlying_class: native
domain: manufacturing
source: Toyota Production System (Ohno, 1988); formalized in lean manufacturing
best_for:
  - Diagnosing flow bottlenecks in production lines
  - Aligning production rhythm to customer demand
  - Identifying where work queues and delays accumulate
one_liner: "Diagnose flow state by measuring customer demand rhythm, work cycle, and total lead time."
---

# Takt Time / Cycle Time / Lead Time

## Overview

Three metrics that reveal whether a production system matches customer demand or is building inventory. **Takt time** is the heartbeat—how often the customer needs a unit. **Cycle time** is the actual output rate—how often the line produces a unit. **Lead time** is the total elapsed time from order to delivery. When cycle time exceeds takt time, inventory accumulates; when it's faster, the line starves itself by stopping early. Practitioners use this lens to locate flow disruptions and negotiate realistic production rates against demand.

## Analytical Procedure

### Phase 1 — Measure Takt Time

1. **Collect customer demand data.** Obtain actual orders (not forecasts) for the last 1–3 months covering seasonal variation, if any. If demand is erratic, use the 30-day average. If it is project-based, measure per-project delivery frequency.

2. **Calculate available production time.** Subtract scheduled downtime (shift length, breaks, maintenance windows) from calendar time in the measurement period. Record this in minutes.

3. **Compute takt time.** Divide available production time by total units demanded in the same period.
   - **Formula:** Takt time (min/unit) = Available production time ÷ Units demanded
   - **Example:** 480 min/shift ÷ 240 units/shift = 2 min/unit takt time

4. **Validate the scope.** Confirm that the demand number includes all products flowing through this line. If the line produces multiple SKUs, weight them by order frequency or compute takt time separately per product family.

### Phase 2 — Measure Cycle Time

5. **Select a representative work sequence.** Pick a standard product or a weighted average product if the line is mixed-SKU. Do not cherry-pick an easy or hard job.

6. **Time the production of 10 consecutive units.** Use a stopwatch or time-study data. Record: start-to-finish time *per unit*, not total batch time. Exclude the first unit (setup variance).

7. **Calculate the 9-unit average.** This is your cycle time.
   - **Formula:** Cycle time = Sum of 9 unit times ÷ 9
   - Record this to the nearest 0.1 minute.

8. **Repeat the timing at different times of day and on different days.** If cycle time varies by >10%, note the source (fatigue, material variation, tooling wear). Use the median, not the mean.

9. **Cross-check against theoretical minimum.** If the work involves manual steps, break it into sub-tasks (pick, assemble, inspect, pack). Sum theoretical minimum times from work instructions or motion studies. Cycle time should be within 10–15% of this sum; if higher, there is waiting or rework built into the process.

### Phase 3 — Measure Lead Time

10. **Define the start and end points clearly:**
    - **Start:** order placed or work release to the floor (not order creation date)
    - **End:** unit ready to ship (not shipped; ignore post-production delay)

11. **Track 5–10 units from start to finish.** Record timestamps at each major step (release, arrival at station 1, station 2, … quality gate, staging). Include queue time and wait time between stations, not just active work time.

12. **Calculate total lead time.** Sum all elapsed time (active work + queues + waiting).
    - **Formula:** Lead time = (Last timestamp) − (First timestamp)

13. **Decompose lead time into value-added and non-value-added portions:**
    - **Value-added:** time spent on actual transformation (cycle time summed across all stations)
    - **Non-value-added:** queue time, transport time, rework, inspection waiting
    - **Formula:** Lead time = Value-added time + Queue time + Transport time + Rework + Other delays

### Phase 4 — Compare and Diagnose

14. **Compare cycle time to takt time.**
    - If **Cycle ≤ Takt:** production is faster than demand. Check for line starvation (operators waiting, premature stops) or inventory buildup before the next constraint.
    - If **Cycle > Takt:** production is slower than demand. Work is backlogged. Identify which station(s) are running above takt.

15. **Calculate the non-value-added ratio.**
    - **Formula:** NVA ratio = (Queue + Transport + Rework + Other) ÷ Lead time
    - If >70%, the system is heavily loaded by delays, not work. Look for long queues between stations, batch delays, or frequent rework.

16. **Identify constraint(s).**
    - If one station's cycle time is significantly higher than others, it is the bottleneck. All other stations' capacity is wasted in queuing behind it.
    - If cycle time is acceptable but lead time is long, the constraint is queuing or batch processing, not the work itself.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Takt time is calculated from actual (not forecast) demand | Y/N |
| Available production time accounts for all scheduled downtime | Y/N |
| Cycle time is measured on ≥9 consecutive units, excluding setup | Y/N |
| Cycle time measurements vary by <10% across different conditions, or variance source is identified | Y/N |
| Lead time is decomposed into value-added and non-value-added portions | Y/N |
| At least one constraint (bottleneck station or queue) is explicitly named | Y/N |

## Red Flags

- Cycle time is estimated or based on work instructions alone, not observed on running production. Work instructions are typically optimistic; actual cycle includes hesitation, rework, and waiting.
- Takt time includes forecast demand. Forecasts mask true rhythm. Use actual orders or (if demand is seasonal) a rolling 30-day actual average.
- Lead time measurement includes post-production delays (staging, shipping prep). These inflate the total and hide the actual production duration.
- Cycle time is measured on only 2–3 units. You cannot detect variance with n<5. Variance is diagnostic.
- NVA ratio is never calculated. You can't prioritize improvements without knowing whether the bottleneck is work speed or queuing.
- Takt time and cycle time are "about" or "roughly" equal. Precision to 0.1 min matters—off-by-one rounding hides small but cumulative overruns that cause backlog.

## Output Format

```
## Takt / Cycle / Lead Time Assessment

### Takt Time
- Measurement period: <dates>
- Total units demanded: <number>
- Available production time: <minutes>
- **Takt time: <min/unit>**
- Frequency: one unit every <time interval>

### Cycle Time
- Product measured: <SKU or representative product>
- Sample size: 9 consecutive units (excluding setup)
- Measurement conditions: <time of day, operator experience level>
- Individual unit times: <list or histogram>
- **Cycle time: <min/unit>**
- Variance range: ±<percentage>

### Lead Time (sampled units)
- Sample size: <number of units tracked>
- Average lead time: <total time, days:hours:minutes>

#### Decomposition
| Component | Time | % of Total | Note |
|---|---|---|---|
| Value-added (total cycle) | <> | <>% | Work on all stations summed |
| Queue time | <> | <>% | Waiting between stations |
| Transport time | <> | <>% | Movement between stations |
| Rework | <> | <>% | Scrap/repair/reinspection |
| Other delays | <> | <>% | Changeovers, material shortage, waiting |
| **Total Lead Time** | <> | 100% | |

**Non-value-added ratio: <>%**

### Flow Diagnosis

**Cycle vs. Takt:**
- Cycle time is <faster / equal to / slower than> takt time by <margin>
- Implication: <inventory accumulating / on-time delivery at risk / line is constrained>

**Constraint identification:**
- Primary bottleneck: <station name or queue location>
- Evidence: <cycle time or queue observation>
- Secondary bottlenecks (if any): <...>

**Lead time drivers:**
- The largest non-value-added component is <queue / transport / rework / other> at <>%
- Recommended focus for improvement: <bottleneck station or queue elimination>

### Confidence
<high | medium | low> — <justification: e.g., "high — measurements taken on n=9 units across 3 shifts with <5% variance and takt computed from 30 days of actual orders", or "medium — cycle time measured on mixed-SKU line with 15% variance; single product takt would be more precise">
```
---
