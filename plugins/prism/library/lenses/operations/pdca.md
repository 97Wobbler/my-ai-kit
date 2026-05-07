---
name: pdca
display_name: PDCA Cycle
class: lens
underlying_class: native
domain: operations
source: W. Edwards Deming (Statistical Process Control); formalized in Toyota Production System (1950s–present)
best_for:
  - Closing the loop between intention and outcome in repeated processes
  - Surfacing whether failures are execution gaps or design flaws
  - Building organizational muscle for continuous incremental improvement
one_liner: "Plan-Do-Check-Act — structure process improvement and institutionalize learning."
---

# PDCA Cycle

## Overview

PDCA (Plan-Do-Check-Act) is a disciplined four-step loop for improving any repeatable process. Each cycle tests a hypothesis about how to improve, measures whether the test worked, and feeds the result back into the next plan. Practitioners use it when the gap between current state and desired state is unknown—not to execute a known-good process, but to learn what works through structured experimentation. The discipline is treating every cycle as a data point, not a failure.

## Analytical Procedure

### Step 1: Plan

1. **Define the process boundary.** What activity or workflow are you improving? Write it in one sentence. Include input, output, and who performs it.

2. **Identify the current problem or opportunity.** Describe the gap between current state and desired state. Quantify if possible (time, cost, error rate, customer impact). If you cannot quantify it, the opportunity is too vague—return to step 1.

3. **State a hypothesis in the form "If we [change X], then [measurable outcome Y] will improve by [Z%/amount] within [timeframe]."** Example: "If we add a peer review step before deployment, then production defects will decrease by 40% within 2 sprints."

4. **Plan the change.** Specify exactly what will be done differently:
   - Who will do it?
   - When will the test start and end?
   - What resources are needed?
   - What is the scope (are we testing on all units or a sample)?
   - What could go wrong, and how will you mitigate it?

5. **Establish the measurement baseline.** Collect data on the current process for at least one full cycle (one day, week, sprint, or production run—whatever "normal" looks like). Record:
   - The metric you care about (latency, defect rate, cost, etc.)
   - How you will measure it (tool, method, frequency)
   - Who will collect it
   - Any confounding factors that might affect the result

### Step 2: Do

6. **Execute the planned change on a limited scope.** Run the process exactly as planned, for exactly the duration planned. Record:
   - What actually happened (vs. what was planned)
   - Any obstacles or unexpected behavior
   - Deviations from the plan and why they occurred
   - Any qualitative observations (mood, ease of use, unintended consequences)

7. **Maintain a log of the execution.** Capture each instance of the process with timestamps, who performed it, and any notes. Do not wait until the end to record data—this introduces memory bias and makes troubleshooting impossible.

### Step 3: Check

8. **Collect the post-change measurement.** Using the same method as the baseline, measure the process during the test period. Ensure consistency: same metric, same measurement method, same observer if possible.

9. **Compare baseline to post-change.** Create a simple table:
   - Baseline average / median / range
   - Post-change average / median / range
   - Difference (absolute and %)
   - Statistical significance (if you have >30 data points, calculate a confidence interval or p-value; otherwise note "small sample, directional only")

10. **Examine execution logs for root causes of the outcome.** Did the metric improve because the change was good, or because of some other factor? Look for:
    - Changes that were unplanned but happened anyway (confounds)
    - Steps that were skipped or done differently
    - External events during the test period (a holiday, a system outage, unusual demand)
    - Evidence that the change was actually applied consistently

11. **Interview the people who performed the process.** Ask:
    - Did the change make the process easier or harder?
    - Did you forget to do any step?
    - Did you do anything differently than instructed?
    - Would you want to keep using this change?
    - What would need to happen for you to believe this is an improvement?

### Step 4: Act

12. **Classify the outcome:**
    - **Adopt:** The metric improved significantly, the change was executed as planned, and people report it's workable or better. Implement the change permanently.
    - **Adapt:** The metric moved in the right direction but the change was hard to execute or unintended consequences appeared. Plan a refinement (loop back to Step 1 with the new insight) and run another cycle.
    - **Abandon:** The metric did not improve or got worse. Understand why (Was the hypothesis wrong? Was it executed poorly? Was it confounded?). Propose a different hypothesis and loop back to Step 1.

13. **Standardize the learning.** If adopting:
    - Update the process documentation, training, and checklists.
    - Communicate the change and the evidence to all stakeholders.
    - Set a date to revisit (e.g., "check defect rate again in 3 months").

14. **Schedule the next cycle.** Identify the next most-pressing problem or opportunity in the same process (or an adjacent one). Return to Step 1.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Process boundary is stated in one sentence (who, what, input, output) | Y/N |
| Gap quantified with a baseline metric | Y/N |
| Hypothesis is in the form "If X, then Y will change by Z% in [time]" | Y/N |
| Baseline data collected before change was made | Y/N |
| Post-change data collected using identical method as baseline | Y/N |
| Execution log kept during the "Do" phase | Y/N |
| At least one confounding factor was considered | Y/N |
| Post-change metric is compared to baseline with difference stated | Y/N |
| Outcome classified as Adopt / Adapt / Abandon with justification | Y/N |
| Next cycle is planned (if Adopt) or refinement is planned (if Adapt) | Y/N |

## Red Flags

- Baseline was collected after the change had already started. Data is contaminated; restart the cycle with a clean baseline.
- "Check" phase relies on memory or anecdote instead of logged data. Measurement is invalid; the cycle learned nothing.
- Hypothesis was vague ("improve efficiency") or unmeasurable ("make people happier"). Return to Step 1 and restate.
- Post-change metric improved but execution logs show the change was never consistently applied. The improvement is a confound, not validation.
- Same cycle repeated three times with no learning or adjustment between cycles. The team is executing rote process, not running PDCA.
- No interview of process performers. You know the metric changed but not whether the change is sustainable or acceptable to the people who must do the work.
- Outcome classification has no supporting evidence. An "Adopt" decision with a 5% improvement on a 10-sample test is premature.

## Output Format

```
## PDCA Assessment

**Process:** <boundary statement>

**Baseline Problem/Opportunity:** <gap description with quantification>

**Hypothesis:** If we [change], then [outcome] will improve by [amount] within [timeframe].

### Plan Phase Summary
| Element | Specification |
|---|---|
| Change description | <...> |
| Scope (full process or sample) | <...> |
| Test duration | <...> |
| Resources required | <...> |
| Baseline metric method | <...> |
| Baseline collected | <date range> |

### Do Phase Summary
| Item | Observation |
|---|---|
| Change executed as planned | Y/N; <deviations> |
| Execution logs kept | Y/N; <sample entries> |
| Obstacles encountered | <...> |
| Stakeholder feedback (qualitative) | <...> |

### Check Phase Results
| Metric | Baseline | Post-Change | Difference | Confidence |
|---|---|---|---|---|
| <metric name> | <avg/median> | <avg/median> | <±% or ±amount> | High/Medium/Low |

**Confounds or external factors during test:**
<...>

**Performer interviews:**
- <question + answer>
- <question + answer>

### Act Phase
**Outcome:** Adopt / Adapt / Abandon

**Justification:** <why this classification given the data and feedback>

**If Adopt:** Changes to process documentation / training / checklists:
- <...>

**If Adapt:** Refinement hypothesis for next cycle:
- <...>

**Next cycle topic:** <...>

### Confidence
<high | medium | low> — <If high: baseline and post-change data are large and clean, confounds ruled out, performers buy in. If medium: sample size small, one confound not fully ruled out, or mixed performer feedback. If low: execution was inconsistent, baseline or post-change data incomplete, or outcome unclear.>
```
