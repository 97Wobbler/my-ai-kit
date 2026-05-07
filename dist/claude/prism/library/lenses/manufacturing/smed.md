---
name: smed
display_name: SMED (Single-Minute Exchange of Die)
class: lens
underlying_class: native
domain: manufacturing
source: Shigeo Shingo, Toyota Production System; formalized in "A Revolution in Manufacturing" (1985)
best_for:
  - Diagnosing where setup time is hidden in changeover operations
  - Separating internal setup (must stop production) from external setup (can happen while running)
  - Identifying quick wins in changeover reduction
one_liner: "Single-Minute Exchange of Die — convert internal setup to external setup to cut changeover time to minutes."
---

# SMED (Single-Minute Exchange of Die)

## Overview
SMED is a structured method for reducing equipment setup and changeover time from hours to minutes (ideally under 10 minutes — hence "single-digit minute exchange"). The core insight is separating internal setup (tasks that require the machine to be stopped) from external setup (tasks that can be done while the machine is running), then converting as much internal work as possible to external. Practitioners use this when changeover frequency is a bottleneck to responsiveness, batch size, or equipment utilization.

## Analytical Procedure

### Stage 1 — Capture Current State

1. **Choose a representative changeover.** Pick a setup that occurs regularly on the target equipment (not the worst case, not the easiest — median). Record the equipment type and current changeover time in minutes.

2. **Film or observe the full changeover from stop to first good part.** Capture every task, every person, every movement. Timestamp the start of each task and mark when production resumes. Include waiting, searching, testing, and adjustment time — don't omit "waiting for supervisor."

3. **List every task in sequence.** For each task, record:
   - Task name
   - Duration (seconds)
   - Tools or materials used
   - Why the machine must be stopped for this task (or confirm it does not require a stop)
   - Who does it
   - Whether it happens every changeover or occasionally

### Stage 2 — Classify Internal vs. External

4. **Mark each task as Internal or External:**
   - **Internal (I):** Machine must be stopped; production cannot resume until this task is done.
   - **External (E):** Machine is running or stopped but not for this task; this work can happen before the machine stops or after it restarts.
   - **Borderline:** If unclear, ask: "Could a second person do this while the machine runs the previous batch?" If yes, it's a candidate for conversion to external.

5. **Sum the Internal time and External time separately.** Current changeover time = (time spent on internal tasks, from machine stop to restart).

### Stage 3 — Convert Internal to External

6. **For each Internal task, ask: "Can this move to External?"** The answer is usually one of:
   - **Already external** — mark it and move on.
   - **Can be pre-staged** — parts, tools, or dies positioned before stopping the machine (e.g., moving dies to the machine while current run is finishing).
   - **Can be parallel-tasked** — assign a second person to do it while another completes remaining internal work.
   - **Requires a setup jig or fixture** — a small investment (often $100–$1k) can move the task external (e.g., pre-positioning a die on an external fixture instead of positioning it on the machine).
   - **Cannot be converted** — rare, but document it.

7. **For each task slated for conversion, design the change.** Specify:
   - What physical or procedural change is needed
   - What new tools, fixtures, or layouts are required
   - Who will do the task and when (e.g., "operator preps die on external station while machine completes current run")
   - One-time cost (if any) and implementation risk

### Stage 4 — Streamline Remaining Internal Work

8. **Eliminate search and adjustment time** in internal tasks:
   - Can tools be pre-positioned or standardized so the operator doesn't search for them?
   - Can measurements or settings be pre-dialed (e.g., die offset pre-set on a calibration block outside the machine)?
   - Can multiple small adjustments be replaced by a single jig or gauge?

9. **Parallelize internal tasks** where safe and physically possible:
   - Can two people work simultaneously on different aspects of the changeover?
   - Can tasks be reordered so that while one person adjusts the die, another person preps the next batch?

### Stage 5 — Measure and Iterate

10. **Conduct a pilot changeover** with the new setup. Measure actual time from machine stop to first good part. Record which conversions worked and which revealed unexpected dependencies.

11. **Calculate the delta.** Original internal time − new internal time = time saved. Also note any external time that now overlaps with production (a win) vs. external time that remains sequential (partial win).

12. **Document the new standard.** Photograph or video the new sequence, update the work instruction, and train operators. Test consistency across 3–5 changeovers to catch variance.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Current state observation includes at least 8 distinct tasks | Y/N |
| Every task is classified as Internal or External (no unclassified tasks) | Y/N |
| Internal time and External time are separately summed | Y/N |
| At least 3 Internal tasks have a documented conversion strategy | Y/N |
| Conversions specify physical change, cost, risk, and new procedure | Y/N |
| Pilot changeover time is measured and compared to baseline | Y/N |
| New standard is documented and tested for consistency | Y/N |

## Red Flags

- All tasks are classified as Internal. The machine must be stopped for changeover, but this is rare. Re-examine tasks like "fetch next batch," "move current batch to staging," or "clean spill" — most can be external.
- Conversions are proposed but no cost or risk is documented. "We could build a jig" without estimation suggests the analysis hasn't engaged with reality.
- Pilot measurement shows little to no improvement. Either the conversions weren't actually implemented or the tasks were mis-classified in Stage 2. Re-observe the pilot.
- New internal time is within 5% of old internal time. Meaningful SMED results are typically 30–70% reduction. Smaller gains suggest partial implementation or that most internal work is already non-convertible (physics or safety constraints).
- No second operator was used in Stage 4 even though the current changeover has idle time. Parallelization is often the easiest win and was skipped.

## Output Format

```
## SMED Analysis

**Equipment:** <name and type>
**Current changeover time:** <minutes:seconds>

### Stage 1–2: Current State Capture & Classification

| Task # | Task Name | Duration (sec) | Internal/External | Dependency / Reason |
|---|---|---|---|---|
| 1 | <task> | <seconds> | I/E | <if I, why machine must stop> |

**Total Internal Time:** <minutes:seconds>
**Total External Time:** <minutes:seconds>

### Stage 3: Conversion Strategy

| Internal Task | Conversion | Method | Cost | Risk | New Owner/Timing |
|---|---|---|---|---|---|
| <task> | Pre-stage / Parallel / Jig / Cannot convert | <description> | $<amount> | <low/medium/high> | <operator, when> |

### Stage 4: Streamlined Internal Procedure

<Describe the reordered or optimized sequence of remaining internal tasks. Include parallelization plan if applicable.>

### Stage 5: Pilot Results

**Pilot changeover time:** <minutes:seconds>
**Improvement:** <old − new>, <% reduction>
**Consistency check (3–5 subsequent changeovers):** <min:sec to min:sec, variance>

### New Standard Documented

- [ ] Work instruction updated
- [ ] Photographs / video recorded
- [ ] Operators trained
- [ ] First-piece quality confirmed

### High-Confidence Conversions

1. <task> → <new method>: <% of internal time saved>
2. ...

### Confidence
<high/medium/low> — <justification: e.g., "high — five pilot runs consistent within 10 seconds; no external dependencies unresolved; cost under budget">
```
