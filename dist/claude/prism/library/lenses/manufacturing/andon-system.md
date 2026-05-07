---
name: andon-system
display_name: Andon System
class: lens
underlying_class: native
domain: manufacturing
source: Toyota Production System (1950s–present); formalized in lean manufacturing
best_for:
  - Detecting and escalating production problems before they cascade
  - Building operator accountability and rapid response culture
  - Identifying systemic bottlenecks through anomaly visibility
one_liner: "Stop-the-line signals that surface problems immediately and trigger collective response."
---

# Andon System

## Overview

An andon system is a visual and/or auditory signaling mechanism that allows any operator on a production line to halt work and call attention when a problem is detected. Rather than continuing to produce defects or allow equipment to fail silently, the operator pulls a cord, presses a button, or activates a light that signals the problem to supervisors and team members. The system treats visibility of abnormality as more valuable than uninterrupted output. Practitioners use it to shift accountability downstream (to the person closest to the problem) and to create feedback loops so recurring issues surface and get addressed systematically.

## Analytical Procedure

### Phase 1 — Establish the Baseline

1. **Document the current line operations.** Record the standard cycle time, the number of stations, staffing levels, and the types of problems that occur most frequently (quality defects, equipment jams, component shortages, setup delays). Interview operators about what problems they see but currently work around or hide.

2. **Map the current escalation path.** When an operator notices a problem today, who do they tell? How long does notification take? What authority do they have to stop the line? Write out the actual chain (not the official one). Note delays, gatekeeping, or reasons operators hesitate to report.

3. **Identify what problems are being masked.** Collect data on defects found downstream (in QC, in customer returns) that originated in this line. Ask: which of these would have been caught earlier if the operator had immediately signaled a stop?

### Phase 2 — Design the Andon Signal

4. **Choose the signal medium.** Decide whether the andon is:
   - **Visual** (colored light, status board, flag)
   - **Auditory** (buzzer, chime, horn)
   - **Hybrid** (light + sound)
   - **Digital** (dashboard alert, SMS, Slack message)
   
   Consider visibility from all stations, audibility over ambient noise, and false-alarm tolerance. A signal that triggers 10 times per shift will be ignored; one that triggers twice per week will be taken seriously.

5. **Set the activation threshold.** Define exactly what triggers the signal:
   - All defects, or only critical ones? (If all, operators will signal constantly; if only critical, you'll miss early warnings.)
   - Equipment hesitation/stall, or only hard failure?
   - Missing component, or only wrong component?
   - Out-of-spec measurement, or only measurement below/above limits?
   
   Write the threshold as a checklist the operator can execute in 10 seconds or less. If the threshold takes 2 minutes of deliberation, operators will skip it.

6. **Define the response protocol.** When the andon signal fires:
   - Who is notified? (Supervisor, line lead, maintenance, quality, all of the above?)
   - What is their arrival time target? (Under 2 minutes? Under 10?)
   - What is the operator's task while waiting? (Continue, hold line, isolate defects, prepare root-cause notes?)
   - What is the resolution requirement? (Problem must be fixed before restart, or temporary containment is acceptable?)
   
   Write these as if-then statements so anyone stepping into the role can execute without interpretation.

### Phase 3 — Pilot and Measure

7. **Run a controlled pilot.** Select one line, one shift, or one product family. Activate the andon. Track for at least 1 week:
   - How many times per hour does the signal fire?
   - Average time from signal to first responder arrival
   - Average time from signal to line restart
   - How many signals result in a fix vs. a temporary reset vs. no action
   - What are the top 3 reasons for signals?

8. **Assess operator hesitation.** Conduct exit interviews or brief stand-downs with operators:
   - Did you hesitate to pull the cord? Why?
   - Did you pull the cord and then decide it was a false alarm? When?
   - How did your supervisor react to the signal?
   - Did you feel blamed for stopping the line?
   
   Hesitation indicates signal threshold is miscalibrated or the response culture is punitive. Fix before expanding.

9. **Measure the impact on downstream problems.** Compare the defect rate in QC or the first-week customer return rate for material made under the andon pilot vs. the baseline. Expect 5–30% reduction, depending on how many defects originated in operator-detectable conditions.

### Phase 4 — Institutionalize

10. **Expand the andon to other lines,** calibrating the threshold and response protocol for each. Do not copy settings from one line to another without pilot data — different product families and staffing patterns will have different optimal thresholds.

11. **Track andon metrics as leading indicators.** Plot weekly signal frequency, average response time, and primary reason categories. A sudden spike in signals often precedes an outbreak of field failures; investigate why visibility increased (threshold miscalibrated?) or why problems increased (equipment drift?).

12. **Link andon data to root-cause action.** Monthly or weekly, review the top reason categories. If "component shortage" accounts for 40% of signals, the andon has done its job — now it's the production planning team's job to fix it. If "operator training" accounts for 30%, the training program needs updating. The andon reveals what to fix; it is not itself the fix.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Baseline defect and escalation data are documented | Y/N |
| Signal threshold is written as an operator checklist (≤10 seconds to execute) | Y/N |
| Response protocol specifies who, arrival target, operator task, restart criteria | Y/N |
| Pilot baseline (before andon) and with-andon metrics are measured for ≥1 week | Y/N |
| Operator hesitation was assessed via interview (not inferred) | Y/N |
| Signal frequency is tracked and does not exceed saturation (>10/hour suggests over-sensitivity) | Y/N |
| Top reason categories are reviewed and assigned to owners (not left as andon "findings") | Y/N |

## Red Flags

- **Signal fires >15 times per shift.** Threshold is too sensitive; operators will ignore it. Raise the threshold or fix the upstream cause (equipment drift, design flaw, training gap) and re-calibrate.
- **Signal fires 0–1 times per week.** Threshold is too high or operators are hesitant. Lower the threshold, run interviews to identify hesitation, or both.
- **Average response time exceeds 15 minutes.** Responders are not prioritizing or not assigned. Clarify protocol and accountability; andon is useless if no one comes.
- **Operator interviews reveal fear or blame.** The supervisor is reacting punitively to signals. Culture is broken; no amount of signal tuning will help until management behavior changes.
- **Signals spike but are never investigated.** The andon is generating visibility but no action. Data is accumulating in a dashboard no one reads. Either assign clear owners to reason categories or deactivate the andon — false visibility is worse than none.
- **No differentiation between signal types.** If "minor quality drift" and "equipment fire" trigger the same signal, important alarms will be lost in noise. Use layered signals (yellow for advisory, red for critical stop).

## Output Format

```
## Andon System Assessment

**Line / Process:**
<name and location>

**Baseline Condition**
- Cycle time: __ seconds
- Defects found downstream: __ per 1000 units
- Current escalation delay: __ minutes median
- Top 3 hidden problems: 1. <...>  2. <...>  3. <...>

**Andon Design**
- Signal type: <visual/auditory/hybrid/digital>
- Activation threshold: <operator checklist>
- Response protocol:
  - Notified: <roles>
  - Target arrival: __ minutes
  - Operator task while waiting: <...>
  - Restart criteria: <...>

**Pilot Results** (1 week minimum)
- Signal frequency: __ per hour
- Median response time: __ minutes
- % resolved (fixed before restart): __%
- % temporary reset: __%
- % no action: __%
- Top 3 reason categories: 1. <...> 2. <...> 3. <...>

**Operator Hesitation Assessment**
- Did operators hesitate to signal? <Yes/No>
- Primary reasons for hesitation: <...>
- Supervisor reaction tone (punitive / supportive / neutral): <...>
- Recommended culture changes: <...>

**Impact on Downstream Quality**
- Baseline defect rate: __%
- With-andon defect rate: __%
- Improvement: __% or <no significant change>

**Current Status**
- <Pilot active / Approved for expansion / Expanded to N lines / Paused>
- Outstanding issues: <...>

### Owner Actions
| Reason Category | Owner | Action | Target Date |
|---|---|---|---|
| <e.g., Component shortage> | <name> | <action> | <date> |

### Confidence
<high/medium/low> — <justification based on data collection completeness and operator feedback consistency>
```
