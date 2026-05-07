---
name: spc
display_name: Statistical Process Control
class: lens
underlying_class: native
domain: manufacturing
source: Walter Shewhart (Bell Labs, 1924); formalized by W. Edwards Deming post-WWII
best_for:
  - Distinguishing common-cause variation from assignable-cause signals in production
  - Detecting process drift before defects occur
  - Building operator confidence in when to adjust vs. when to leave a process alone
one_liner: "Statistical Process Control — monitor process variation in real time and detect intervention signals."
---

# Statistical Process Control

## Overview
SPC uses control charts to track whether a manufacturing process is behaving as expected or has drifted into a state requiring intervention. The core discipline is **distinguishing noise from signal**: every process has variation, but not all variation demands action. A control chart sets statistical boundaries (control limits) around expected variation so operators know when a point (or a pattern) indicates a real shift versus random fluctuation. Practitioners use SPC to reduce both overcontrol (adjusting a stable process, which adds variation) and undercontrol (ignoring a real drift until scrap piles up).

## Analytical Procedure

### Phase 1 — Establish the Baseline

1. **Collect at least 20–25 consecutive subgroups of measurements.** A subgroup is typically 4–5 samples taken close together (e.g., every hour, every batch). Use the process under its current, "normal" conditions with no deliberate changes.
   - Record each individual measurement.
   - Note the date, time, operator, and any unusual conditions (material batch change, temperature spike, etc.).

2. **Calculate subgroup statistics.** For each subgroup, compute:
   - **Subgroup average** (X̄): mean of the measurements in that subgroup.
   - **Subgroup range** (R): max value minus min value in that subgroup.
   - (Alternative: if measuring individuals, use moving range of consecutive points.)

3. **Compute overall process mean and variation.** From the 20–25 subgroups:
   - **Grand average** (X̿): average of all subgroup averages.
   - **Average range** (R̄): average of all subgroup ranges.

4. **Calculate control limits using standard formulas.** These define the boundaries of "normal" variation:
   - **For X̄ chart:**
     - Upper Control Limit (UCL) = X̿ + A₂ × R̄
     - Lower Control Limit (LCL) = X̿ − A₂ × R̄
     - (A₂ is a constant based on subgroup size: n=4 → A₂=0.729; n=5 → A₂=0.577; etc.)
   - **For R chart:**
     - UCL = D₄ × R̄
     - LCL = D₃ × R̄
     - (D₃, D₄ are also size-dependent constants: for n=4, D₃=0, D₄=2.282; for n=5, D₃=0, D₄=2.114.)
   - Plot these limits on the chart as horizontal lines.

### Phase 2 — Assess Baseline Stability

5. **Check whether the baseline subgroups themselves are in statistical control.** Plot each X̄ and R value on the respective chart. A point is out of control if:
   - Any point falls outside the control limits (beyond UCL or below LCL).
   - Any run of 8+ consecutive points falls on the same side of the centerline.
   - Any pattern of 6 points steadily increasing or decreasing (trend).
   - Any 2 out of 3 consecutive points fall beyond 2σ (two standard deviations from the mean).
   
   If the baseline has out-of-control points, investigate and remove them (with documented cause) or recalculate limits from a stable subset.

### Phase 3 — Monitor Ongoing Production

6. **Collect new subgroups at regular intervals** (same frequency as baseline). Calculate X̄ and R for each new subgroup.

7. **Plot new points on the control chart.** Use the control limits established in Phase 1. Do not recalculate limits for every new point — that erases the baseline signal.

8. **Apply detection rules.** A point or pattern signals a real change (assignable cause) if:
   - **Rule 1:** Any point outside ±3σ (beyond control limits).
   - **Rule 2:** 8+ consecutive points on one side of the centerline.
   - **Rule 3:** 6 points in a row steadily increasing or decreasing.
   - **Rule 4:** 2 out of 3 points beyond 2σ on the same side.
   - **Rule 5:** 4 out of 5 points beyond 1σ on the same side.
   - **Rule 6:** 15 points in a row within 1σ of the centerline (indicates process improvement or measurement problem).
   
   When any rule fires, stop and investigate.

9. **Investigate the assignable cause.** When a signal appears:
   - Note the time, material batch, operator, temperature, setup, or other process variable that changed.
   - Confirm the signal is real (not measurement error or recording mistake).
   - Document the root cause and the corrective action taken.

10. **Decide: adjust or update limits.** If the cause was temporary (e.g., wrong operator input), correct it and continue. If the cause represents a permanent improvement (e.g., new tooling, better material), recalculate control limits from the new baseline. If the cause was a persistent drift (e.g., tool wear), establish a preventive maintenance trigger.

### Phase 4 — Continuous Improvement

11. **Review control charts monthly or quarterly.** Look for:
    - Trends in where points cluster (even if in control, a shift toward one side may warn of gradual drift).
    - Recurring assignable causes (same problem every Tuesday = operator training issue, or every batch 5 = supplier lot contamination).
    - Reduction in overall variation (R̄ decreasing) = stable process, opportunity to tighten specification limits or reduce inspection.

12. **Adjust process parameters only when out of control.** Overcontrol (adjusting a stable process) introduces unnecessary variation and is a common failure mode. Use SPC as the objective signal to act or not act.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Baseline sample size is ≥20 subgroups | Y/N |
| Each subgroup has consistent n (same number of measurements) | Y/N |
| Control limits are calculated using the correct constants (A₂, D₃, D₄) for the subgroup size | Y/N |
| Baseline is verified to be in statistical control before limits are used for monitoring | Y/N |
| Detection rules are explicit and applied consistently (not by eye) | Y/N |
| Each out-of-control signal has a documented investigation and root cause | Y/N |
| Charts are updated at regular, documented intervals | Y/N |

## Red Flags

- **Limits recalculated every week or month from recent data.** This defeats the purpose — the baseline is the reference. Frequent recalculation masks real signals.
- **All points fall within control limits, but the process is visibly drifting toward one side.** Control limits are wide; use Rule 2 (8 in a row on same side) to catch creep.
- **Out-of-control points are deleted without investigation.** If a point is real, it signals something; ignoring it is blindness. If it's a measurement error, document that.
- **X̄ chart shows a point out of control but the R chart is normal.** A single point shift in average is a real signal (e.g., material change, tool shift). Don't dismiss it because spread is stable.
- **R chart goes to zero or near-zero.** Either the measurement system is insensitive or the process is not being sampled correctly (all subgroup items are identical, which is suspicious).
- **No record of what changed between baseline and the current month.** Without linking signals to causes, SPC becomes a chart-drawing exercise, not a tool for action.

## Output Format

```
## SPC Assessment

**Process:**
<name and description>

**Specification limits (if known):**
Upper spec: <value> | Target: <value> | Lower spec: <value>

### Baseline Stability (Phase 2)
| Subgroup | X̄ | R | Status | Notes |
|---|---|---|---|---|
| 1 | <value> | <value> | In/Out | <if out, why> |
| 2 | <...> | <...> | | |

**Grand average (X̿):** <value>
**Average range (R̄):** <value>

### Control Limits
**X̄ Chart:**
- UCL: <calculated value>
- Center: <X̿>
- LCL: <calculated value>

**R Chart:**
- UCL: <calculated value>
- Center: <R̄>
- LCL: <calculated value>

### Recent Monitoring (last 10 subgroups or most recent period)
| Subgroup | X̄ | R | Signal? | Rule fired | Action |
|---|---|---|---|---|---|
| n-9 | <...> | <...> | No | — | Continue |
| n-8 | <...> | <...> | Yes | Rule 1 (out of limit) | Investigate: <cause> |

### Assignable Causes (last 3 months)
| Date | Signal | Root cause | Action taken | Limit recalculated? |
|---|---|---|---|---|
| <date> | <X̄ or R out of control> | <documented cause> | <corrective action> | Y/N |

### Process Capability (if spec limits known)
- Cpk: <calculated or N/A>
- Sigma level: <calculated or N/A>
- Status: <capable | marginally capable | not capable>

### Confidence
<high/medium/low> — <justification: e.g., "high — baseline of 25 subgroups in control, 3 months of monitoring data, all signals investigated and linked to documented causes" or "medium — baseline only 18 subgroups, R chart shows unusual pattern suggesting inconsistent sampling" or "low — insufficient baseline history or recent signals unexplained">
```
---
