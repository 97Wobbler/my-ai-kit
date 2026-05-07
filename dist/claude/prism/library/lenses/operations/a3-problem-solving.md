---
name: a3-problem-solving
display_name: A3 Problem Solving
class: lens
underlying_class: native
domain: operations
source: Toyota Production System (1960s); formalized in lean manufacturing and problem-solving curricula
best_for:
  - Structured root-cause analysis and countermeasure planning
  - Cross-functional problem documentation that survives leadership handoff
  - Disciplines teams to distinguish observation from interpretation
one_liner: "One-page problem analysis and improvement plan — observation, root cause, countermeasure, effect check."
---

# A3 Problem Solving

## Overview
The A3 is a one-page structured report (named for the paper size) that forces a team to move through problem analysis and solution design in a disciplined sequence: current state observation, gap definition, root-cause hypothesis, countermeasures, implementation plan, and validation. Practitioners use it to prevent premature solution-jumping and to create an auditable record of reasoning. The discipline is the constraint — one page forces clarity and kills filler.

## Analytical Procedure

### Phase 1 — Current State (Observation, not judgment)

1. **State the problem in observable terms.** Do not interpret. 
   - Bad: "The team is inefficient."
   - Good: "Shipping cycle time increased from 3 days to 7 days between January and March."
   Write the metric, the baseline, the current level, and the time period. Attach one supporting chart or table.

2. **Define the gap.** Compare current state to target state (or historical state if no target exists).
   - Current: 7 days
   - Target: 3 days
   - Gap: 4 days
   Do not propose solutions yet.

3. **Quantify the impact.** How much does this gap cost (time, money, quality, customer satisfaction)? Use a single impact measure.

### Phase 2 — Root Cause Analysis (Structured interrogation)

4. **List 4-6 candidate root causes.** Do NOT filter for plausibility yet. Ask:
   - What changed in the system (people, process, tools, supply) between the baseline and now?
   - What did we stop doing?
   - What did we start doing?
   - What external event coincides with the gap?
   Write each as a factual hypothesis, not a judgment.

5. **For each candidate, gather evidence.** Do not argue for your favorite cause yet.
   - How would I know if this cause is real? (What observable evidence would prove/disprove it?)
   - What data do I have? (Logs, timestamps, interviews, measurements)
   - What data am I missing?
   Record at least one piece of evidence per candidate. If you have zero evidence, mark it as "unverified" and move on.

6. **Identify the strongest candidate.** Choose the one with the most evidence, not the most intuitive. If multiple candidates are equally supported, list both — do not force a single cause if the evidence doesn't warrant it.

7. **Write a root-cause statement.** This is your hypothesis, not a conclusion. Phrase it as: "The root cause is [specific change/failure] which led to [mechanism] resulting in [observed gap]."
   - Example: "The root cause is insufficient code review capacity (3 reviewers became 1) which caused bottleneck in the approval pipeline, resulting in 7-day shipping cycle."

### Phase 3 — Countermeasures (Solution design)

8. **Generate 3-5 countermeasures.** Each must directly address the root cause, not the symptom.
   - Bad: "Ship faster." (This is a restatement of the goal, not a countermeasure.)
   - Good: "Hire and onboard a second code reviewer" or "Implement asynchronous review tool to parallelize approvals."
   For each countermeasure, write: the action, the owner, the start date, and the expected effect size.

9. **Evaluate countermeasures.** For each, estimate:
   - **Effort**: Low / Medium / High
   - **Expected impact on gap**: High / Medium / Low
   - **Risk**: (what could go wrong?)
   - **Dependencies**: (what must happen first?)
   Choose one primary countermeasure (highest impact, acceptable effort). List secondary countermeasures as "follow-up."

### Phase 4 — Implementation (Plan and execute)

10. **Create a 30-60-90 day action plan.** Who does what by when?
    - Week 1-2: <action>
    - Week 3-4: <action>
    - Month 2: <action>
    - Month 3: <action>

11. **Define success metrics.** How will you know the countermeasure worked?
    - Primary: (the metric from Phase 1 — shipping cycle time back to 3 days)
    - Secondary: (proxy metrics — e.g., average review turnaround time, number of blockers)
    - Measurement frequency: (weekly / biweekly / monthly)

### Phase 5 — Verification (Reflection and learning)

12. **Track progress on the action plan.** Mark each milestone complete/incomplete/blocked.

13. **Re-measure the primary metric** at 30, 60, and 90 days. Compare to gap target.

14. **Document learnings.** Did the countermeasure close the gap? If yes, what enabled it? If no, what was the gap between plan and reality? Did you discover a different root cause?

15. **Update the A3 with results.** The bottom half of the page now shows actual vs. planned progress and next steps (if gap persists, cycle back to root-cause analysis with new data).

## Evaluation Criteria

| Check | Pass |
|---|---|
| Current state is stated as a measurable observation (not interpretation) | Y/N |
| Gap is quantified with baseline, current, and target | Y/N |
| At least 4 root-cause candidates are listed | Y/N |
| Each candidate has supporting evidence (not just plausibility) | Y/N |
| Root-cause statement is specific: names what changed, why it matters | Y/N |
| Countermeasures directly address root cause, not the symptom | Y/N |
| Implementation plan has owners and dates for each action | Y/N |
| Success metrics are measurable and tied to the original gap | Y/N |
| A3 fits on one page (forces discipline, kills filler) | Y/N |

## Red Flags

- Current state is vague or interpretive ("morale is low," "process is inefficient"). This ruins the entire analysis — you cannot do root cause on a judgment.
- Root cause is a solution ("we need better communication") not a cause ("communication channels were eliminated when the team moved").
- Countermeasures are generic ("improve quality," "work harder"). They don't tie to the specific root cause.
- No evidence gathered in Phase 2 — all candidates listed but none investigated. This is a guess disguised as analysis.
- A3 exceeds one page. Length inflation means unclear thinking or scope creep.
- Implementation plan has no owners or dates, only intentions ("we should consider," "we will try to").
- Success metrics are not tied to the original gap metric. You cannot claim success if you're measuring something different from what you said was broken.
- Verification never happens — A3 is filed, not revisited. The point is learning, not paperwork.

## Output Format

```
# A3 Problem Solving Report

## Current State
**Problem (observable):** [Metric has shifted from X to Y between Date1 and Date2]
**Impact:** [Cost / benefit loss]

### Gap Analysis
| Baseline | Current | Target | Gap |
|----------|---------|--------|-----|
| 3 days   | 7 days  | 3 days | 4 days |

## Root Cause Analysis

### Candidate Causes
1. [Cause] — Evidence: [data/observation]
2. [Cause] — Evidence: [data/observation]
3. [Cause] — Evidence: [data/observation]

### Root Cause (Selected)
[Specific change/failure that led to observed gap]

## Countermeasures
| Countermeasure | Owner | Timeline | Expected Impact | Effort | Risk |
|---|---|---|---|---|---|
| [Action] | [Name] | Week 1-2 | [Effect size] | Low/Med/High | [Risk] |

**Primary Countermeasure:** [Selected action with justification]

## Implementation Plan
- **Week 1-2:** [Action] — Owner: [Name]
- **Week 3-4:** [Action] — Owner: [Name]
- **Month 2:** [Action] — Owner: [Name]
- **Month 3:** [Action] — Owner: [Name]

## Success Metrics
- **Primary:** [Metric back to baseline/target by Day 90]
- **Secondary:** [Proxy metrics and frequency]

## Verification (30-60-90 day review)
| Milestone | Target | Actual | Status |
|-----------|--------|--------|--------|
| Day 30    | [metric] | [measured] | ✓ / ✗ |
| Day 60    | [metric] | [measured] | ✓ / ✗ |
| Day 90    | [metric] | [measured] | ✓ / ✗ |

### Learning
[Did countermeasure close the gap? Gap between plan and reality? Next steps if incomplete?]

### Confidence
<high/medium/low> — <Justification: Did metrics move as predicted? Was root cause verified or hypothetical? Were countermeasures executed as planned?>
```
