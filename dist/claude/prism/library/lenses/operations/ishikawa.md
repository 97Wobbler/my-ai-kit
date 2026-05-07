---
name: ishikawa
display_name: Ishikawa (Fishbone)
class: lens
underlying_class: native
domain: operations
source: Kaoru Ishikawa, 1968
best_for:
  - Root cause analysis of quality problems
  - Structured problem decomposition in manufacturing and processes
  - Team-based defect investigation
one_liner: "Fishbone diagram that decomposes root causes via 6M categories."
---

# Ishikawa (Fishbone)

## Overview
The Ishikawa diagram organizes potential causes of a problem into six categories—Materials, Methods, Machines, Manpower, Measurement, and Environment—and forces systematic interrogation of each. Practitioners use it when a quality defect, process failure, or operational problem resists obvious explanation and needs to be examined from multiple angles simultaneously. The discipline is exhaustion: you do not leave a category until you have genuinely exhausted the likely causes within it.

## Analytical Procedure

### Step 1 — Problem Definition
1. **State the problem (effect) in clear, measurable terms.** Do not state a solution or a guess at the cause. Bad: "Fastener quality is bad." Good: "15% of fasteners exceed the 0.5mm diameter tolerance; failure mode is oversize, not undersize."
2. **Measure the problem's severity and frequency.** Quantify it: defect rate, affected units, cost impact, detection method. This prevents chasing rare edge cases.
3. **Set a time boundary.** When did the problem start or when was it detected? This narrows the search space and helps rule out ancient causes.

### Step 2 — Populate Each of Six Categories

For each category below, brainstorm and list all plausible causes. Do not filter during brainstorming. Involve the people closest to the process—operators, technicians, engineers who have hands-on experience.

#### 2.1 Materials
- Material composition or batch variability (supplier, lot number, storage)
- Incoming inspection failures (was material accepted despite spec deviation?)
- Contamination or degradation during storage or handling
- Substitute materials or off-spec inputs
- Shelf life or expiration status

#### 2.2 Methods
- Process steps missing, out of order, or poorly documented
- Setup or calibration procedures not followed
- Parameter settings (temperature, pressure, speed, duration) drift from spec
- Operator discretion or workarounds replacing standard procedure
- Handoff or communication failures between process stages

#### 2.3 Machines
- Equipment calibration drift or maintenance lag
- Worn tooling, dies, or fixtures
- Machine settings inconsistent across units or shifts
- Downtime forcing substitution with alternate equipment
- Preventive maintenance schedule failures or gaps

#### 2.4 Manpower
- Skill gaps or inadequate training
- Fatigue or distraction during critical steps
- Turnover (new operator not yet proficient)
- Unclear role definitions or accountability
- Insufficient staffing causing rushed work

#### 2.5 Measurement
- Measurement instrument out of calibration
- Measurement procedure not standardized or understood
- Sampling strategy (when/where/how often measured) misses the problem
- Measurement resolution too coarse to detect the defect
- Human error in reading or recording the measurement

#### 2.6 Environment
- Temperature, humidity, or atmospheric condition swings
- Vibration or shock during process or transport
- Contamination from adjacent processes
- Lighting, noise, or other ergonomic stressors affecting work quality
- Seasonal or time-of-day variation

### Step 3 — Prioritize and Investigate

3. **For each potential cause, ask: "Is this plausible given the problem definition and timeline?"** Eliminate causes that contradict known facts (e.g., if the problem began two weeks ago, a supplier that has been the same for two years is less likely).

4. **Assign investigation priority using impact × likelihood.** High impact + high likelihood = investigate first. Low impact or very low likelihood = defer or drop.

5. **For the top 3–5 candidates, collect evidence.**
   - Check maintenance logs, calibration records, supplier certificates.
   - Interview the operators or technicians who were running the process when the problem started.
   - If possible, observe the process in action or review production data (SPC charts, defect logs, batch records).
   - Run a small test or reproduce the problem under controlled conditions.

### Step 4 — Validate Root Cause(s)

6. **Does the evidence support the suspected cause as necessary and sufficient?** Necessary: the problem does not occur without it. Sufficient: the problem occurs whenever it is present (or nearly always).

7. **Rule out competing causes.** If two causes are equally plausible, test them against each other (e.g., "If it's a measurement issue, the defect should be random and unrelated to batch; if it's a material issue, the defect should cluster by supplier lot").

8. **Document the final root cause assessment.** State it clearly: "Fastener diameter exceeds spec because Die A has experienced 50 microns of wear since last replacement, occurring uniformly across all parts in a batch."

## Evaluation Criteria

| Check | Pass |
|---|---|
| Problem stated as measurable effect, not suspected cause | Y/N |
| All six categories were populated with at least 3 candidates each | Y/N |
| At least one cause per category was investigated (not all assumed) | Y/N |
| Top candidates were prioritized by impact and likelihood | Y/N |
| Root cause(s) tested for necessity and sufficiency | Y/N |
| Competing causes were explicitly ruled out or ranked | Y/N |

## Red Flags

- The problem statement is already a solution ("Calibration is wrong" instead of "Output is ±0.5mm off nominal"). This prematurely narrows the analysis.
- Only one or two categories were populated. Saying "This is obviously a machine problem" and ignoring Methods, Manpower, and Measurement is confirmation bias.
- Causes were listed but never investigated. A brainstorm list is not root cause analysis.
- The root cause has no quantitative evidence. "Operator error" without observation data or defect clustering is not validated.
- Multiple root causes were identified but not ranked by impact. This muddies corrective action priority.
- Investigation stopped at the first plausible cause. Competing explanations were not tested.

## Output Format

```
## Ishikawa Analysis

**Problem (effect):**
[Measurable description. Quantify: defect rate, units affected, cost, detection method.]

**Timeline:**
[When detected / started.]

### Brainstorm by Category

#### Materials
- [Cause]
- [Cause]
...

#### Methods
- [Cause]
...

#### Machines
...

#### Manpower
...

#### Measurement
...

#### Environment
...

### Prioritized Investigation

| Candidate Cause | Category | Impact | Likelihood | Priority | Evidence | Validated? |
|---|---|---|---|---|---|---|
| [Cause A] | [Category] | H/M/L | H/M/L | [Rank] | [Brief finding] | Y/N |

### Root Cause(s)

**Primary cause:**
[Stated as necessary and sufficient condition with supporting evidence.]

**Competing causes ruled out:**
- [Cause]: [Why ruled out.]
- [Cause]: [Why ruled out.]

### Corrective Action Targets
1. [Specific action to prevent recurrence.]
2. ...

### Confidence
<high | medium | low> — <Justification: How much evidence collected? Were competing causes tested? Is the cause reproducible or only circumstantial?>
```
