---
name: kanban
display_name: Kanban (WIP, CFD, Little's Law)
class: lens
underlying_class: native
domain: agile
source: David Anderson (Kanban: Successful Change Management for Your Technology Business, 2010); Cumulative Flow Diagram and Little's Law formalized by operations research (Kingman, 1961)
best_for:
  - Diagnosing bottlenecks and queue buildup in workflow
  - Validating that work-in-progress limits are set correctly
  - Predicting delivery time from current queue state
one_liner: "Flow-based work management that makes the mathematical relationship between WIP limits and cycle time visible."
---

# Kanban (WIP, CFD, Little's Law)

## Overview

Kanban makes flow visible and measurable by tracking three things: the number of items in work at any moment (WIP), how long each item takes from start to finish (cycle time), and how many items finish per unit time (throughput). The Cumulative Flow Diagram (CFD) plots these over time, revealing where work stalls. Little's Law connects them mathematically: *cycle time = WIP / throughput*. Practitioners use this lens when they suspect queues are forming, WIP limits are too loose, or delivery predictability is eroding.

## Analytical Procedure

### Step 1 — Instrument the Workflow

1. **Define the workflow stages.** List every stage from "ready" to "shipped" (e.g., Backlog → Designed → In Progress → Code Review → Testing → Deployed). Each stage must be distinct enough that "started" and "completed" are unambiguous.

2. **Set the observation window.** Choose a historical period (e.g., last 8 weeks). All measurements will span this window.

3. **Collect entry and exit data for each item.** For every work item, record:
   - Item ID or name
   - Entry date into each stage
   - Exit date from each stage
   - Actual WIP count at end of each day (count of items "in progress" but not yet completed)

   Do not estimate. If the data is not recorded, use git history, pull request timestamps, or ticket status logs to reconstruct it.

### Step 2 — Calculate Cycle Time and Throughput

4. **For each completed item, calculate cycle time (CT).** Cycle time = exit date of final stage minus entry date of first stage. Record in days.

5. **Calculate average cycle time (ACT).** Sum all cycle times and divide by the count of completed items.

6. **Calculate throughput (T).** Count the number of items completed in the observation window. Divide by the length of the window in days to get items per day (or per week if the window is short).

7. **Validate with Little's Law.** Calculate predicted average WIP:
   - Predicted WIP = ACT × T
   - Count the actual average WIP during the window (sum of daily WIP counts divided by number of days).
   - Compare predicted to actual. If they differ by more than 20%, recheck the data — stage definitions may be inconsistent or items may be getting stalled outside the main workflow.

### Step 3 — Build the Cumulative Flow Diagram

8. **Plot cumulative items by stage.** On a graph with time on the x-axis (days of the observation window):
   - For each stage, draw a line showing the cumulative count of items that have *entered* that stage by each day.
   - Stack the lines or use color bands so that the vertical distance between lines represents the WIP in each stage.

9. **Identify stalls and bunches.** Look for:
   - **Vertical jumps** (many items entered at once) — indicates batch arrivals or release events.
   - **Flat sections** (a line stays horizontal while others climb) — indicates a stage where items are queued and not flowing. This is a bottleneck.
   - **Converging bands** (distance between two lines shrinks) — throughput downstream exceeded upstream, pulling items through. This is healthy.
   - **Diverging bands** (distance widens) — upstream is outpacing downstream, forming a queue.

10. **Calculate the slope of the final (shipped) line.** This is throughput. Steeper slope = higher throughput. If it's flat or declining, throughput is falling.

### Step 4 — Diagnose Constraints

11. **For each stage showing WIP buildup (diverging bands in the CFD):**
    - Retrieve 3–5 items currently in that stage.
    - Interview the assignee: "What is blocking progress on this item right now?" Record the answer verbatim.
    - Look for patterns: missing information, waiting for external review, technical debt, unclear acceptance criteria, dependency on another stage.

12. **Measure stage-specific cycle time.** For items completed in the window, calculate:
    - Stage CT = time spent in that stage only.
    - Compare across stages. The stage with the longest average CT is the constraint.

13. **Calculate the theoretical WIP limit for each stage.** For a stage where:
    - Average stage CT = S days
    - Desired throughput = T items per day
    - Then: max WIP for that stage = S × T (rounded up)

    If actual WIP in that stage is higher, the stage is overstaffed for its throughput, or items are waiting idly.

### Step 5 — Compute Predictability

14. **Calculate the 85th percentile cycle time.** Sort all completed cycle times from shortest to longest. The 85th percentile is the cycle time that 85% of items beat (and 15% exceed). This is the cycle time to quote to stakeholders.

15. **Calculate the standard deviation of cycle time.** This measures variability. High SD means cycle time is unpredictable. Low SD means it's consistent. Compare to the mean: if SD > 0.5 × mean, cycle time is highly variable.

16. **Estimate delivery date for items currently in the workflow.** For an item with entry date E and current date C:
    - Days elapsed so far = C − E.
    - Remaining days (from current stage) ≈ 85th percentile CT − (C − E).
    - Predicted delivery = C + remaining days.

    This is a median estimate; communicate the 85th percentile as a "safe" estimate.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Workflow stages are defined such that entry/exit are unambiguous | Y/N |
| Historical data (timestamps per stage) exists or can be reconstructed | Y/N |
| Cycle time calculated for ≥20 completed items | Y/N |
| Little's Law check: predicted WIP within 20% of actual average WIP | Y/N |
| CFD produced with ≥5 data points (daily readings over 5+ days) | Y/N |
| Bottleneck stage identified by stage CT or CFD divergence | Y/N |
| At least one root cause interview conducted for the bottleneck stage | Y/N |
| 85th percentile CT and standard deviation calculated | Y/N |

## Red Flags

- **Little's Law prediction is off by >20%.** Stage definitions are likely inconsistent (items entering/exiting at different boundaries). Redefine stages or check for "dark" WIP (work happening outside the tracked stages).
- **CFD shows no clear slope for the "shipped" line.** Throughput is unstable or too low to measure. The window may be too short, or work is being released in large batches rather than continuously.
- **All stages show equal WIP buildup.** The entire system is queue-bound, not bottlenecked at one stage. This suggests work is arriving faster than the system can process. Reduce input or increase capacity across all stages.
- **Diverging band matches WIP limit exactly.** Items hit the limit and stop, creating artificial constraint. Raise the limit or fix the underlying stage constraint.
- **No flat sections in the CFD, but cycle time is very high.** Items are flowing but slowly — likely due to excessive rework, unclear acceptance criteria, or dependencies outside the main workflow.
- **85th percentile >> mean cycle time.** Outliers are common. Investigate the slowest 15% of items separately — they may have a different root cause (e.g., blocked on external review, involves rework).

## Output Format

```
## Kanban Flow Assessment

**Observation window:**
[start date] to [end date] (_X_ days)

**Workflow stages:**
- <Stage 1>
- <Stage 2>
- ...

### Throughput & Cycle Time
- Average cycle time: _X_ days
- Throughput: _X_ items/day
- Items completed: _X_
- Average WIP (actual): _X_
- Predicted WIP (Little's Law): _X_
- Variance: ±_X_% [within tolerance | OUT OF TOLERANCE]

### 85th Percentile (Safe Estimate)
- Cycle time (p85): _X_ days
- Std deviation: _X_ days
- Predictability: [high | medium | low]

### Bottleneck Analysis
| Stage | Avg stage CT (days) | Current WIP | Max WIP (calc.) | Status |
|---|---|---|---|---|
| <...> | <...> | <...> | <...> | bottleneck / flowing |

**Root cause (if bottleneck identified):**
- [From interviews or CFD analysis]

### Cumulative Flow Diagram Summary
- [Brief description of visual patterns observed]
- Diverging bands (queuing): [stages affected]
- Converging bands (pulling): [stages affected]

### Recommendations
1. <Action based on identified constraint>
2. <WIP limit adjustment>
3. <Cycle time target>

### Confidence
<high/medium/low> — <justification based on data completeness and convergence of Little's Law check>
```
