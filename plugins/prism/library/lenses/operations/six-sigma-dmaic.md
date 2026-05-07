---
name: six-sigma-dmaic
display_name: Six Sigma DMAIC
class: lens
underlying_class: native
domain: operations
source: Motorola (1986); systematized by George et al. in Six Sigma methodologies
best_for:
  - Eliminating defects and variation in repeatable processes
  - Data-driven root cause identification in operations
  - Staged improvement projects with measurable before/after impact
one_liner: "Five-step method (Define/Measure/Analyze/Improve/Control) to stabilize performance by eliminating root-cause variation."
---

# Six Sigma DMAIC

## Overview
DMAIC (Define-Measure-Analyze-Improve-Control) is a five-phase framework for reducing defects and process variation through structured data collection and root cause elimination. Each phase has a specific deliverable: a problem statement, a baseline metric, a causal hypothesis, an intervention, and a control mechanism. Practitioners reach for DMAIC when a process produces known waste (scrap, rework, cycle time) and they can measure both the waste and the process inputs/outputs. The discipline is enforcing the sequence — organizations that skip to Improve without Analyze waste resources on the wrong levers.

## Analytical Procedure

### Phase 1 — Define

1. **Identify the process owner and scope.** Who runs this process day-to-day? What are the start and end points? Write a one-sentence process description (e.g., "Order-to-cash cycle from customer purchase to cash receipt").

2. **Quantify the problem.** What is the defect, waste, or variation? Examples: scrap rate (%), on-time delivery failure (%), customer complaints per month, cycle time (hours). Record the current baseline, the target, and the cost of the gap.
   - Bad: "Our shipping is slow."
   - Good: "Current order fulfillment time is 8 days; target is 3 days. At 500 orders/month, the 5-day gap costs $50k/month in expedited handling and lost sales."

3. **Define the desired outcome.** What metric will you improve? Write it as a SMART goal: Specific, Measurable, Achievable, Relevant, Time-bound. Example: "Reduce on-time delivery failures from 15% to 5% within 6 months."

4. **Map the high-level process.** Draw or describe the major steps (4-8 boxes). This is not a detailed flowchart — it is a boundary map that shows what's in scope and what's not.

5. **Identify constraints and stakeholders.** Who must approve changes? Are there regulatory, budget, or technology constraints? List them explicitly. These will resurface in Improve.

### Phase 2 — Measure

6. **Operationalize the defect or metric.** How will you *recognize* a defect when you see one? Write the operational definition so tightly that two people measuring independently will agree.
   - Vague: "Late delivery."
   - Tight: "Order marked 'shipped' after promised delivery date, or not received by customer by 11:59 PM on promised date."

7. **Collect baseline data.** Sample at least 30-100 instances of the process (more if variation is high). Record both the outcome (defect: yes/no, or metric value) and the process conditions (input variables, operator, time of day, equipment, material batch, etc.). Store raw data in a table or spreadsheet.

8. **Measure process stability.** Plot the metric over time (run chart or control chart). Does it show random variation around a center, or does it drift, spike, or show patterns? If patterns exist, note them — they are clues for Analyze.
   - Random: good baseline for improvement.
   - Drift/pattern: process may be unstable; consider whether you need to stabilize it before you can improve it.

9. **Calculate process capability.** If you have a target and upper/lower specification limits, compute Cp and Cpk (or the equivalent for your metric). This tells you whether the process *can* hit the target, even in theory, or whether variation is too high.

10. **Document data quality.** Who collected the data? Under what conditions? Was measurement consistent? Flag any gaps or suspect records.

### Phase 3 — Analyze

11. **Stratify the defect data.** Break down the baseline by categories to find where the defects cluster. Examples:
    - By shift, operator, machine, material supplier, time of week, order size, customer geography.
    - Create a Pareto chart (defect count by category). The defects are rarely uniform — often 80% of defects come from 20% of causes.

12. **Correlate process variables to the outcome.** For each process input you measured in Phase 2, check whether it correlates with the defect or metric.
    - Use scatterplots for continuous variables (e.g., temperature vs. defect rate).
    - Use box plots or proportions for categorical variables (e.g., supplier A vs. B defect rates).
    - Use statistical tests (t-test, chi-square) to confirm that differences are not due to chance.

13. **Develop causal hypotheses.** Based on stratification and correlation, propose 2-4 root causes. For each, answer:
    - What process step does this cause affect?
    - Why does it cause a defect? (Trace the mechanism.)
    - What evidence supports this hypothesis?
    - What evidence would disprove it?

14. **Design confirmation experiments if needed.** If the root cause is unclear after stratification and correlation, run a focused experiment:
    - Change one process input deliberately (e.g., temperature, supplier, procedure).
    - Hold everything else constant.
    - Measure the outcome. Did the defect rate shift?
    - This is faster than collecting months of passive data.

15. **Rank root causes by impact and controllability.** For each confirmed root cause, estimate:
    - **Impact**: If I fix this, how much will the metric improve?
    - **Controllability**: Can we actually change this in our process? (Cost, feasibility, stakeholder approval.)
    - Prioritize high-impact, high-controllability causes.

### Phase 4 — Improve

16. **Generate solutions for the top 2-3 root causes.** For each, brainstorm 3-5 possible countermeasures. Do not jump to the first solution.

17. **Pilot the countermeasures.** Run each solution on a small scale (one shift, one operator, one machine, 50 orders) for 1-4 weeks. Measure the outcome using the same operational definition from Phase 2. Did the metric improve? By how much?

18. **Cost the improvement.** For each successful pilot:
    - What is the cost to implement permanently? (Training, equipment, procedure change, labor.)
    - What is the ongoing cost to sustain? (Labor, materials, maintenance.)
    - What is the benefit (reduced scrap, faster cycle, reduced complaints, higher revenue)? Annualize it.
    - Is the ROI positive? Timeline to payback?

19. **Get stakeholder buy-in.** Present the pilot results to the process owner, finance, operations, and any other approvers. Address concerns about cost, implementation risk, and workflow disruption. Do not move to implementation without approval.

20. **Implement the solution.** Roll out the countermeasure to the full process. Update procedures, train staff, communicate the change, and adjust equipment if needed.

### Phase 5 — Control

21. **Establish a control plan.** Define the ongoing process: Who will monitor the metric? How often? What are the control limits (upper and lower)?
    - Typical: run chart or control chart updated weekly or monthly.
    - Alert condition: if metric drifts above the upper limit or below the target for 3 consecutive periods.

22. **Audit compliance.** For the first 2-3 months post-implementation, verify that the new procedure is being followed. Sample work, observe operators, check records. Compliance often drifts without reinforcement.

23. **Lock in the standard.** Document the new procedure as the standard operating procedure (SOP). Update training materials, checklists, and work instructions. Make it the default, not a special request.

24. **Measure post-improvement baseline.** After 2-3 months of stable operation under the new procedure, calculate the new capability (Cp, Cpk) and compare it to the baseline from Phase 2. This is your proof of improvement.

25. **Assign ownership and frequency.** Assign someone (the process owner, a quality engineer, a shift supervisor) to monitor the control chart. Set a review cadence (weekly, monthly). If the metric drifts, trigger a root cause investigation — you may be entering a new Improve cycle.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Problem is quantified with baseline, target, and cost of gap | Y/N |
| Baseline data includes ≥30 samples with process conditions recorded | Y/N |
| Operational definition of defect/metric is tight enough for two independent raters to agree | Y/N |
| Stratification analysis (Pareto or equivalent) was performed | Y/N |
| Correlation between inputs and outcome was tested (not assumed) | Y/N |
| Root causes were ranked by impact and controllability | Y/N |
| Improvement was piloted at small scale before full rollout | Y/N |
| Control plan includes alert conditions and assigned owner | Y/N |
| Post-improvement metric is compared quantitatively to baseline | Y/N |

## Red Flags

- The "problem" is stated in terms of a solution ("We need to use Six Sigma" or "We need better training"). DMAIC requires a quantified defect or metric, not a solution.
- No baseline data was collected before Improvement. You have no proof the improvement actually worked — the metric might have changed for other reasons.
- Stratification shows the defect is random across all categories. This suggests either your categorization is wrong, or the root cause is systemic and not easy to isolate. Do not force a Pareto chart where none exists.
- Root causes were identified by opinion, not by correlation or experimentation. "I think it's operator error" is not analysis — test it.
- The pilot was never run. Moving directly from Analyze to full-scale implementation is a classic failure mode. Pilots save money.
- Post-improvement, the metric is not monitored. Without control, the improvement drifts away within weeks. Control is not optional.
- The Improve phase delivered a solution without costing it. You do not know if the ROI justifies the implementation effort.

## Output Format

```
## Six Sigma DMAIC Assessment

**Process:** <name and scope>

**Problem (quantified):**
- Current baseline: <metric value>
- Target: <metric value>
- Cost of gap: <annualized cost or impact>

### Phase 1 — Define
- Process owner: <name>
- High-level steps: <4-8 step summary>
- Constraints: <regulatory, budget, technology>

### Phase 2 — Measure
- Operational definition: <tight, unambiguous description>
- Baseline sample size: <n>
- Process stability: <random | drift | pattern | (describe)>
- Process capability (Cp/Cpk): <values or N/A if not applicable>

### Phase 3 — Analyze
- Stratification result: <Pareto: 80% of defects from X category> or <Random across categories>
- Correlation findings:
  | Input variable | Correlation to defect | Strength | Test used |
  |---|---|---|---|
  | <...> | <...> | <weak/moderate/strong> | <...> |

- Root causes (ranked by impact × controllability):
  1. <cause> — Impact: <est. % improvement>. Controllability: <high/medium/low>. Evidence: <...>
  2. <cause> — ...

### Phase 4 — Improve
- Pilots run: <list countermeasures and pilot results>
- Pilot improvement: <metric change from baseline to post-pilot>
- Implementation cost: <one-time and annual>
- Estimated ROI: <annual benefit / cost, payback period>
- Stakeholder approval: <yes/no, conditions if any>

### Phase 5 — Control
- Control plan: <metric, frequency, alert limits>
- Owner assigned: <name>
- Post-improvement baseline: <metric value after 2-3 months stable operation>
- Improvement confirmed: <% change from Define baseline to Control baseline>

### Confidence
<high | medium | low> — <justification: e.g., "High — improvement validated over 3-month period with n=200 samples; stakeholder compliance audited; control chart shows stability within target range.">
```
