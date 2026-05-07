---
name: adaptive-management
display_name: Adaptive Management
class: lens
underlying_class: native
domain: ecology
source: C.S. Holling (1978); formalized in natural resource management by Walters & Hilborn (1976) and extended to ecosystem stewardship
best_for:
  - Managing systems with high uncertainty and irreversible outcomes
  - Designing interventions where consequences reveal themselves only over years
  - Escaping lock-in from policies that proved wrong but cannot be reversed
one_liner: "Decision framework that treats policies as experiments and improves them via monitoring data."
---

# Adaptive Management

## Overview
Adaptive management treats a management decision as a controlled experiment: implement a policy intervention, monitor its effects against pre-specified indicators, and adjust course based on what the data reveals. The discipline is the pre-commitment to adjust — most policies are defended long after evidence turns against them. Practitioners use this when the system's response to an intervention is uncertain, when mistakes are costly (or irreversible), and when waiting for perfect information costs more than learning by doing.

## Analytical Procedure

### Phase 1 — Specify the Decision and Uncertainty

1. **Name the resource or ecosystem being managed.** Be specific: "salmon population in the Deschutes River basin" not "fish management."

2. **State the management objective in measurable terms.** Examples: "increase chinook spawning escapement to 5,000 fish by 2035" or "reduce wildfire extent to <5% of landscape per decade." Vague objectives (e.g., "improve habitat quality") cannot be monitored.

3. **List the key uncertainties.** What does the manager not know about how the system will respond to intervention? Examples:
   - Does dam removal increase fish passage enough to boost populations?
   - Will suppressing fire for 50 years increase fuel loads enough to trigger uncontrollable burns?
   - How sensitive is this population to climate change vs. harvest?
   
   Do not list uncertainties you can resolve with existing research — only those that learning-by-doing can clarify.

4. **For each uncertainty, write the two or three competing hypotheses.** Example:
   - **H1:** Removing the dam allows spawning migration; population increases 30% within 5 years.
   - **H2:** Removing the dam destabilizes the riverbed; spawning habitat degrades despite passage; population stays flat.
   - **H3:** Population is limited by ocean conditions, not river access; dam removal has minimal effect.
   
   Each hypothesis should predict observable outcomes.

### Phase 2 — Design the Monitoring System

5. **Select monitoring indicators.** An indicator is a measurable proxy for your objective. It must be:
   - **Observable within the decision timeline.** (Population genetics may take 20 years; juvenile survival can be tracked within 2 years.)
   - **Causally connected to the objective,** not just correlated. (Spawning escapement counts are direct; water temperature is a partial proxy.)
   - **Sensitive enough to detect the effect you're trying to measure.** If the true effect size is 10% but your monitoring noise is ±15%, you will not detect it.
   
   Examples: spawning adult counts, juvenile survival rates, species diversity indices, fire size distribution, vegetation cover in burned areas, stream temperature time series.

6. **Specify baseline and threshold values.** Before intervening, record the system's current state (baseline). Define the decision threshold — the monitoring result that would trigger a change in policy. Example:
   - Baseline: 2,000 spawning adults per year (2010–2015 average)
   - Threshold: If spawning counts remain below 2,500 for three consecutive years post-intervention, consider adding hatchery support or revoking dam removal.

7. **Design a sampling protocol.** How will you observe the indicator? How often? At what cost? Examples:
   - Weekly snorkel surveys during spawning season at 20 index sites (cost: $10k/year, precision: ±200 fish)
   - Annual aerial count of all visible nests (cost: $50k, precision: ±500 fish, but weather-dependent)
   - Write down the protocol explicitly — it must be repeatable by others.

8. **Assign responsibility and a review schedule.** Who collects the data? When is it analyzed? When is a management decision made based on the results? Specify the interval: quarterly, annually, every three years. Longer intervals allow more signal to accumulate but delay correction of course.

### Phase 3 — Design the Intervention and Decision Rules

9. **Describe the intervention(s) in operational terms.** Not "improve habitat" but "remove the Milo Dam by July 2028, breach the spillway first to avoid scouring, stabilize the banks with bioengineering, and plant 50,000 native trees within the new riparian zone."

10. **Write if-then decision rules.** These are conditional: if monitoring shows X, then do Y.
    - If spawning escapement exceeds 4,000 for two consecutive years, reduce hatchery supplementation by 50%.
    - If wildfire frequency increases above historical mean after 10 years of fire suppression, shift to prescribed burns on 2% of landscape per year.
    - If juvenile survival drops below 5%, revisit the dam removal decision and consider re-engineering the spillway.
    
    Rules should reference the thresholds you set in Step 6. Do not leave the response vague ("managers will reassess").

11. **Define what "reversal" or "course correction" means.** Some interventions are hard to undo. For each, note:
    - **Reversible:** removing the spillway net; can re-engineer it in 2 years at 2× cost.
    - **Hard to reverse:** dam removal; sediment regime change is permanent; restoring habitat takes decades.
    - **Partially reversible:** prescribed burns; can rebuild fuel stocks if you pause burns, but it takes 30 years.
    
    Irreversible interventions require higher confidence in the hypothesis before implementation.

### Phase 4 — Implement and Monitor

12. **Begin with a pilot or small-scale trial if possible.** If you can test the intervention on a 10% slice of the system first, do it. Monitor for 1–3 years. Use the results to refine the full-scale design.

13. **Implement the intervention as specified and record the date.** Do not drift from the design without deliberate revision. Drift makes it impossible to attribute observed changes to the intervention.

14. **Collect monitoring data on schedule.** Flag and investigate any anomalies in real time (e.g., equipment failure, unusual weather, changed sampling methods). Document everything — departures from protocol matter.

15. **At each review interval, compare observed outcomes to the hypotheses.** Which hypothesis is the data supporting? Are you moving toward the objective? Is the intervention creating unexpected side effects (e.g., invasive species colonizing the newly opened habitat)?

16. **Apply the decision rules.** If the rule triggers, implement the corrective action. If it doesn't, continue. If the data is equivocal (close to the threshold), err on the side of caution in irreversible interventions.

17. **Iterate.** After each decision, refine the monitoring design, revise hypotheses if necessary, and continue. Adaptive management is a loop, not a one-time intervention.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Objective is stated in measurable, time-bound terms | Y/N |
| At least 2 competing hypotheses are written (with predicted outcomes) | Y/N |
| Monitoring indicators are observable within the decision timeline | Y/N |
| Baseline and decision thresholds are quantified (not vague ranges) | Y/N |
| Sampling protocol is written in enough detail to be replicated | Y/N |
| At least 3 if-then decision rules are specified | Y/N |
| Reversibility of the intervention is documented | Y/N |
| Review interval and responsible party are named | Y/N |

## Red Flags

- Objective is stated qualitatively ("improve the ecosystem"). This cannot be monitored, and the intervention will never be deemed successful or unsuccessful.
- Only one hypothesis is present. Adaptive management requires genuine uncertainty; a single expected outcome is not uncertainty, it's overconfidence.
- Monitoring indicators are indirect proxies (e.g., "habitat quality index") without clear linkage to the objective. Indices obscure what you're actually measuring and make it hard to refine hypotheses.
- Decision thresholds are missing or vague ("we'll know it's working when we see improvement"). Vague thresholds are ignored in practice.
- No pilot. The full intervention is deployed at landscape scale on day one. If the hypothesis is wrong, the cost is catastrophic and reversal is impossible.
- Decision rules are absent or generic ("managers will reassess the results"). Without explicit rules, monitoring data goes unheeded and the intervention persists regardless of outcome.
- The review interval is so long (e.g., 10 years) that course correction is delayed until the objective is already missed and reversal is infeasible.
- Reversibility is not addressed. Irreversible interventions (habitat conversion, species introductions, dam removal) should require higher prior confidence and more conservative thresholds.

## Output Format

```
## Adaptive Management Assessment

**Resource / System:**
<name and geographic scope>

**Objective (measurable, time-bound):**
<e.g., "increase chinook spawning escapement to 5,000 fish by 2035">

### Phase 1 — Competing Hypotheses
| Hypothesis | Predicted Outcome | Evidence (how to test) | Plausibility |
|---|---|---|---|
| H1: <...> | <...> | <...> | High/Medium/Low |
| H2: <...> | <...> | <...> | <...> |
| H3: <...> | <...> | <...> | <...> |

### Phase 2 — Monitoring Design
**Primary indicator:** <name and units>
**Baseline:** <current state, with dates>
**Decision threshold:** <trigger value>
**Sampling protocol:** <method, frequency, cost, precision>
**Review schedule:** <interval and responsible party>

### Phase 3 — Intervention & Decision Rules
**Intervention:** <operational description>
**Reversibility:** <reversible / hard to reverse / irreversible + cost/timeline>

**Decision Rules:**
1. If <monitoring outcome>, then <action>
2. If <...>, then <...>
3. ...

### Adaptive Loop Status
- Pilot conducted? <yes / no / in progress>
- Current iteration: <Gen 1 / Gen 2 / ...>
- Data collected to date: <summary of results>
- Hypothesis supported: <H1 / H2 / H3 / unclear>
- Course corrections applied: <yes / no / pending decision>

### Confidence
<high/medium/low> — <justification: Are the hypotheses genuinely distinguishable by the monitoring data? Are the decision rules likely to trigger before irreversible harm occurs? How much uncertainty remains?>
```
---
