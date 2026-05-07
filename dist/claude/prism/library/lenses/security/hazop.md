---
name: hazop
display_name: HAZOP (Hazard and Operability Study)
class: lens
underlying_class: native
domain: security
source: Kletz, T. A. (1974); IEC 61882 standard; chemical and process safety engineering
best_for:
  - Systematic hazard identification in process systems
  - Uncovering deviations from intended design and operation
  - Breaking free from "it's never happened" assumptions
one_liner: "Systematically expose deviations and hazards via parameter × guideword combinations."
---

# HAZOP (Hazard and Operability Study)

## Overview

HAZOP is a structured brainstorm that systematically identifies deviations from design intent by crossing process parameters (flow, pressure, temperature, level, composition) with guidewords (more, less, none, reverse, other). The result is not a list of known hazards but a catalogue of *plausible* deviations and their consequences. Practitioners use HAZOP when the default risk assessment ("we've engineered for known failure modes") misses the tail risks — the 10,000-to-1 scenarios that never happened because they never happened, not because they can't.

## Analytical Procedure

### Phase 1 — System Decomposition

1. **Define the system boundary.** What process, subsystem, or artifact are you studying? Examples: a chemical reactor, a database transaction pipeline, an API endpoint, a manufacturing assembly line. Write it in one sentence with no ambiguity.

2. **List the process parameters that matter.** These are the measurable or controllable aspects of the system:
   - Flow (rate, direction, continuity)
   - Pressure (absolute, gauge, gradient)
   - Temperature (hot, cold, gradient)
   - Level (height, fullness, contents)
   - Composition (purity, concentration, species present)
   - Time (duration, sequence, dwell)
   - Viscosity, pH, density, or domain-specific properties
   Write 5–12 parameters. If you have fewer than 3, your system boundary is too broad. If you have more than 15, subdivide the system.

3. **Break the system into logical study nodes.** Each node is a section, component, or phase where parameters can be examined. A chemical plant might have: feed tank, reactor, condenser, separator, product tank. A software pipeline might have: request parsing, authentication, database query, response serialization. List each node explicitly.

### Phase 2 — Guideword Application

4. **Apply the six standard guidewords to each parameter in each study node:**
   - **NO / NONE** — The parameter is absent or zero. (No flow, no pressure, no temperature control.)
   - **MORE** — The parameter is greater than design intent. (Higher flow, higher pressure, higher temperature.)
   - **LESS** — The parameter is lower than design intent. (Lower flow, lower pressure, lower temperature.)
   - **REVERSE** — The parameter moves or points backward. (Backflow, back-pressure, backward sequence, reverse polarity.)
   - **OTHER / DIFFERENT** — The parameter is off-spec in an unintended way. (Wrong composition, wrong catalyst, wrong user role, wrong input type.)
   - **AS WELL AS** — An additional parameter or input appears alongside the intended one. (Water in addition to organic solvent, extra request headers, second actor modifying state simultaneously.)

5. **For each (parameter, guideword, node) triplet, ask:** "What causes this deviation, and what are its consequences?" Write at least one plausible cause and at least one consequence. Do not filter for likelihood — probability comes later.

   Example for a reactor system:
   | Node | Parameter | Guideword | Cause | Consequence |
   |---|---|---|---|---|
   | Reactor | Pressure | MORE | Cooler inlet temperature, gas generation in exotherm | Vessel rupture, personnel injury, chemical release |
   | Reactor | Temperature | LESS | Cooling loop blockage, pump failure, ambient cold | Reaction stalls, incomplete conversion, product contamination |

6. **Do not skip combinations.** Mark each (parameter, guideword) pair as examined, even if the answer is "impossible under normal operation" — that annotation is data. Skipping because something "shouldn't happen" is the failure mode HAZOP is designed to catch.

### Phase 3 — Consequence and Safeguard Assessment

7. **For each deviation, identify the consequences** (safety, operability, product quality, or business impact). Be specific: "injury to operator" → "operator exposure to 80°C fluid, estimated second-degree burn on contact."

8. **List existing safeguards or controls** that prevent the deviation or mitigate the consequence. Examples: pressure relief valve, automated shutdown, alarm threshold, redundant pump, input validation, rate limiting.

9. **Assign a severity grade to each consequence:**
   - **Critical** — Uncontrolled release, loss of life, catastrophic business impact
   - **Major** — Serious injury or illness, significant environmental release, major business disruption
   - **Moderate** — Minor injury, containable release, operational issue
   - **Minor** — Nuisance, small loss, easily recovered

10. **Assess safeguard effectiveness.** For each safeguard, rate its robustness:
    - **High** — Fully independent, regularly tested, diverse from root cause
    - **Medium** — Adequate coverage but depends on operator intervention or maintenance
    - **Low** — No redundancy, susceptible to common-cause failure with the deviation root cause, untested

### Phase 4 — Recommendation and Closure

11. **For deviations with Critical or Major severity and Low safeguard effectiveness, generate recommendations.** Do not filter for "feasibility" at this stage — capture what would help.

12. **Classify each recommendation:**
    - **Design change** — Modify the system to eliminate the deviation
    - **Add safeguard** — Introduce a new control (sensor, valve, software check, procedure)
    - **Procedure or training** — Establish a process or operator practice to detect or respond
    - **Monitor** — Accept the risk and establish monitoring until further action

## Evaluation Criteria

| Check | Pass |
|---|---|
| System boundary is defined in one sentence with no ambiguity | Y/N |
| 5–12 process parameters identified for the system | Y/N |
| Study nodes defined and listed explicitly | Y/N |
| All six guidewords applied to each parameter in each node | Y/N |
| Each (parameter, guideword, node) triplet has ≥1 cause and ≥1 consequence recorded | Y/N |
| No combinations skipped; skipped items explicitly marked as examined | Y/N |
| Severity grades assigned to all consequences | Y/N |
| Safeguard effectiveness rated (High/Medium/Low) for each control | Y/N |
| Recommendations classified by type (Design/Safeguard/Procedure/Monitor) | Y/N |
| At least one Critical or Major finding identified (if not, check that guidewords were applied adversarially) | Y/N |

## Red Flags

- All combinations come out "impossible" or "already prevented." The guideword application was insufficiently adversarial. Push harder: "What if the operator made a mistake?" "What if a sensor failed?" "What if two rare events coincided?"
- No deviations with Critical or Major severity. Either the system is genuinely very safe (rare) or consequences were underestimated. Revisit the consequence step.
- Safeguards are listed but their effectiveness is never rated. You have identified controls but not validated that they actually prevent the deviations you're worried about.
- Study nodes are too large (e.g., "the whole plant"). Break into smaller pieces. Large nodes hide interactions and make the matrix unwieldy.
- Recommendations are vague ("improve monitoring," "review procedure"). Be specific: "install a pressure transducer on the outlet line with a setpoint of 50 psi and an audible alarm at >45 psi."
- The study was completed in one session with one facilitator. HAZOP is a team sport. If only one perspective was present, blind spots are likely.

## Output Format

```
## HAZOP Study Report

**System Boundary:**
<one sentence description of the system being studied>

**Study Nodes:**
1. <node name>
2. <node name>
...

**Process Parameters:**
- <parameter>
- <parameter>
...

### Deviation Analysis Matrix

| Node | Parameter | Guideword | Cause | Consequence | Severity | Existing Safeguard | Safeguard Effectiveness | Recommendation | Rec Type |
|---|---|---|---|---|---|---|---|---|---|
| <node> | <param> | <guideword> | <cause> | <consequence> | Critical/Major/Moderate/Minor | <safeguard or "none"> | High/Medium/Low | <recommendation or "accept risk"> | Design/Safeguard/Procedure/Monitor |

### Critical and Major Findings

1. **<Deviation description>**
   - Root cause: <cause>
   - Consequence: <consequence> (Severity: Critical/Major)
   - Current safeguard: <safeguard> (Effectiveness: <rating>)
   - Recommended action: <recommendation>

### Summary of Recommendations

| Type | Count | Examples |
|---|---|---|
| Design change | <n> | <...> |
| Add safeguard | <n> | <...> |
| Procedure/Training | <n> | <...> |
| Monitor | <n> | <...> |

### Confidence

<high | medium | low> — <justification: e.g., "high — full cross-functional team participated, all guideword combinations applied systematically, safeguards independently verified" or "medium — single facilitator, time-limited session, did not re-examine recommendations with operations team">
```
