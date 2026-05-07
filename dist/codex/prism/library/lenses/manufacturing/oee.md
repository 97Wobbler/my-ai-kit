---
name: oee
display_name: Overall Equipment Effectiveness
class: lens
underlying_class: native
domain: manufacturing
source: Nakajima, Seiichi (Japan Institute of Plant Maintenance, 1988); foundational to Total Productive Maintenance (TPM)
best_for:
  - Diagnosing the true source of production shortfall (is it availability, speed, or quality?)
  - Prioritizing improvement investments across maintenance, process, and quality initiatives
  - Tracking operational health without conflating different failure modes
one_liner: "Overall Equipment Effectiveness = availability × performance × quality — pinpoint the root cause of production loss."
---

# Overall Equipment Effectiveness

## Overview
OEE breaks total production loss into three independent multiplicative dimensions: Availability (is the equipment running?), Performance (at what speed?), and Quality (how many good parts?). The insight is that a facility running at 100% availability but 50% speed and 90% quality is fundamentally different from one at 70% availability, 100% speed, and 100% quality — yet both yield 45% OEE. Practitioners use OEE to isolate which lever to pull, and to detect when an "improvement" in one dimension masks deterioration in another. The discipline is measuring each dimension separately and resisting the temptation to conflate them.

## Analytical Procedure

### Phase 1 — Data Collection

1. **Define the unit of analysis.** Pick a single production line, machine, or process step. Document its name, shift schedule, and standard cycle time (parts per minute or similar). Establish the time period under review (shift, day, week — typically 1-2 weeks for initial assessment).

2. **Collect operational events for the period.** For each stoppage or interruption, record:
   - Start time and end time (duration in minutes)
   - Category: planned maintenance, unplanned maintenance, changeover, setup, material shortage, quality stop, or other
   - Root cause (be specific; "line stopped" is not a cause)
   
   Use existing logs (maintenance ticketing, line monitoring sensors) where available. If no formal log exists, interview the operator and maintenance team for the major events.

3. **Collect production output.** Record:
   - Total pieces produced (attempted)
   - Total pieces that passed first-quality inspection (no rework required)
   - For a first pass, assume rework defects are scrapped; do not double-count pieces that cycle back through the line
   
   Use production reports, quality records, or line counters.

4. **Establish the baseline.** Calculate:
   - Total scheduled time (shift hours × 60 minutes/hour, accounting for unpaid breaks)
   - Standard cycle time (seconds or minutes per piece, from engineering or historical average under good conditions)
   - Theoretical maximum pieces (scheduled time ÷ cycle time)

### Phase 2 — Calculate OEE Components

5. **Calculate Availability.**
   - Operating time = Scheduled time − Total unplanned downtime (maintenance, material shortage, quality stops, etc.)
   - Planned downtime (changeovers, scheduled maintenance) is *not* subtracted from operating time; it is excluded from scheduled time entirely if tracking intra-shift. (See red flags: clarity on this distinction is critical.)
   - **Availability = Operating time ÷ Scheduled time**
   - Example: 480 min scheduled, 60 min unplanned stops → 420 min operating → 87.5% availability

6. **Calculate Performance (Speed).**
   - Ideal cycle time = Standard cycle time (from engineering or best observed performance)
   - Actual run rate = Total pieces attempted ÷ Operating time
   - **Performance = Actual run rate ÷ Ideal run rate** (or equivalently, Ideal cycle time ÷ Actual cycle time)
   - Example: Standard is 30 sec/piece (2 pieces/min). Line produced 750 pieces in 420 min = 1.79 pieces/min. Performance = 1.79 ÷ 2 = 89.5%
   - *Include* minor slowdowns, operator hesitations, and brief micro-stops in the actual run rate — these degrade performance even if the line didn't formally "stop."

7. **Calculate Quality.**
   - First-pass pieces = Pieces that passed inspection without rework
   - **Quality = First-pass pieces ÷ Total pieces attempted**
   - Example: 750 pieces attempted, 705 passed first-pass inspection → 705 ÷ 750 = 94%
   - Do *not* count reworked pieces as good for this metric. Rework is a performance loss, not a quality success.

8. **Calculate OEE.**
   - **OEE = Availability × Performance × Quality**
   - Example: 87.5% × 89.5% × 94% = 73.8%

### Phase 3 — Decompose and Diagnose

9. **Identify the limiting factor.** Rank the three components. Whichever is lowest is the biggest loss driver and the primary improvement target. (A line that is 95% available but 75% quality is quality-constrained, not availability-constrained.)

10. **Categorize the root causes within each dimension.**
    
    **For Availability losses, classify stops by type:**
    - Planned: scheduled maintenance, changeovers, setup (separate from unplanned; these are usually acceptable)
    - Unplanned: equipment failure, material shortage, operator error, quality stops, tooling issues
    - Tally the top 3-5 causes by frequency and total minutes lost
    
    **For Performance losses, identify the source:**
    - Is the standard cycle time unachievable? (Investigate process bottleneck, operator skill, tool condition)
    - Are there micro-stops or hesitations recorded by sensors but not in manual logs? (Investigate jams, sensor noise, material variability)
    - Is the line intentionally running slower due to quality concerns or demand? (Document constraint)
    
    **For Quality losses, classify defects:**
    - By defect type (dimension, surface, assembly, etc.) — tally the top 3-5
    - By defect origin (material, setup, tool wear, operator) — assign each major defect type to a source
    - Separate first-pass failures from rework failures to understand whether the problem is controllability or process capability

11. **Check for masking interactions.** A line that keeps stopping to fix quality is showing high unplanned availability loss, but the underlying problem is quality. Re-examine Availability stops: do any mention "quality stop" or "rework"? If yes, the Quality component is the root; fixing Availability alone (e.g., faster maintenance) will not solve the problem.

### Phase 4 — Validation

12. **Spot-check the data.** Verify one day's manual logs against sensor records (if available) or repeat observations on a sample day. Calibration errors are common; discovery here is cheap.

13. **State the confidence level** (see Output Format, below).

## Evaluation Criteria

| Check | Pass |
|---|---|
| Scheduled time, operating time, and planned downtime are clearly defined and consistent | Y/N |
| First-pass quality and rework/scrap are clearly separated; no double-counting | Y/N |
| Standard cycle time is justified (engineering spec, best observed, or measured baseline) | Y/N |
| All three components sum to a meaningful OEE value (0–100%) | Y/N |
| Top 3 root causes by dimension are identified and quantified | Y/N |
| No single component is suspiciously close to 100% (suggests measurement gaps) | Y/N |

## Red Flags

- **OEE is reported as a single number with no breakdown.** "Our OEE is 72%" is useless without knowing whether that's due to availability (60%), performance (90%), or quality (80%). Always report the triplet.
- **Availability includes planned downtime.** If changeovers and scheduled maintenance are subtracted from available time, the metric becomes incoherent; performance against the theoretical peak is conflated with execution against the schedule. Clarify before proceeding.
- **Standard cycle time is outdated or never validated.** If the "ideal" is actually unachievable, Performance will appear artificially low. Validate the standard against best-observed performance in the past 3 months.
- **Reworked pieces are counted as good in Quality.** This masks process instability. Rework is a hidden cost; do not hide it.
- **One component is 95%+ and the others are sub-80%.** The high component may be a measurement artifact or a misleading target. Question whether the measurements are independent or whether one is hiding another (e.g., quality stops masked as availability loss).
- **No root causes identified.** Reporting OEE without decomposing the loss is a scorecard, not an analysis. Drill into the top 3 causes in each dimension or the exercise is incomplete.

## Output Format

```
## OEE Assessment

**Equipment/Process:** <name>
**Period:** <dates and shift>
**Standard Cycle Time:** <time per unit> (source)

### Raw Measurements
- Scheduled time: <minutes>
- Operating time (after unplanned stops): <minutes>
- Total pieces attempted: <count>
- First-pass good pieces: <count>
- Ideal run rate: <pieces/minute or units/hour>
- Actual run rate: <pieces/minute or units/hour>

### OEE Components
| Metric | Calculation | Result |
|---|---|---|
| **Availability** | Operating time ÷ Scheduled time | <XX.X%> |
| **Performance** | Actual run rate ÷ Ideal run rate | <XX.X%> |
| **Quality** | First-pass good ÷ Total attempted | <XX.X%> |
| **OEE** | Availability × Performance × Quality | <XX.X%> |

### Root Cause Summary
**Limiting Factor:** <Availability / Performance / Quality>

**Top Unplanned Availability Losses** (if applicable):
1. <cause> — <duration> min, <frequency> events
2. <cause> — <duration> min, <frequency> events
3. <cause> — <duration> min, <frequency> events

**Top Performance Deviations** (if applicable):
1. <cause/constraint> — <efficiency loss in %> — evidence
2. ...

**Top Quality Failures** (if applicable):
1. <defect type> — <% of total defects> — suspected origin
2. ...

### Masking Check
<Any available stops that are actually rooted in quality or performance issues? Describe here, or state "None detected.">

### Confidence
<high | medium | low> — <brief justification. Examples: "Sensor logs match manual records; data spans 2 weeks and captures typical operations." or "Cycle time is estimated from operator interview, not verified; data collection is incomplete for the weekend shift.">
```
---

**Acknowledgment:** The OEE framework originates in Japanese Total Productive Maintenance (TPM) methodology. The Nakajima definition (three independent multiplicative factors) has become the manufacturing standard and is widely used in automotive, food & beverage, pharmaceuticals, and heavy equipment. This lens operationalizes the measurement and root-cause decomposition process.
