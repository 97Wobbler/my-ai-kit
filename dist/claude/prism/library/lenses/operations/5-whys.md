---
name: 5-whys
display_name: 5 Whys
class: lens
underlying_class: native
domain: operations
source: Taiichi Ohno (Toyota Production System, 1950s); popularized in quality and incident analysis
best_for:
  - Finding root causes of failures or recurring problems
  - Breaking shallow symptom-fixing habits
  - Training teams to think causally rather than blame-fixated
one_liner: "Repeat 'why' until you reach the root cause of a problem."
---

# 5 Whys

## Overview
When a problem surfaces (a system failed, a deadline was missed, a bug shipped), the instinct is to assign blame or apply the first fix that occurs to you. The 5 Whys method disciplines this by insisting you ask "Why?" once you think you have an answer, and keep asking until you reach a cause you can actually fix — not a symptom, not an excuse, but a root cause. Practitioners use it when shallow fixes keep failing and they suspect the team is treating effects, not origins. The method is iterative: each answer becomes the subject of the next "why," creating a causal chain.

## Analytical Procedure

### Phase 1 — Problem Statement

1. **State the failure in concrete, measurable terms.** Not "the system was slow" but "database query time for user_id lookup went from 50ms to 2000ms at 16:35 UTC on 2026-04-10."

2. **Separate the symptom from its context.** The symptom is what you observed. The context is when and where. Write both.
   - Symptom: "Requests returned 503 Service Unavailable."
   - Context: "All requests for 8 minutes, affecting 12% of traffic, during peak hours."

### Phase 2 — Iterative Questioning

3. **Ask "Why did [symptom] happen?" and write a direct, testable answer.** Do not answer with:
   - Blame ("Engineer forgot to update the config")
   - Vagueness ("The system was under load")
   - Another symptom ("The database was overloaded")
   
   Instead answer with a mechanism: "The connection pool was exhausted because idle connections were not being recycled, and a code deploy 40 minutes prior changed the timeout from 5m to 30m."

4. **Take that answer. Ask "Why did [that cause] happen?"** Again, write a mechanism, not a blame or vagueness.
   - Bad: "No one was paying attention."
   - Good: "The deployment process does not run connection pool validation before marking a deploy as healthy."

5. **Repeat step 4 up to four more times (for a total of five "why" questions).** Most problems reach a root cause between the third and fifth why. If you hit a cause that is:
   - **External** (a third-party API went down, the ISP failed) — stop there; this is not actionable by your team.
   - **Physical** (a disk physically failed) — stop; this is root cause.
   - **Repeatable within your control** (a process, a decision, a gap in tooling) — keep asking.

6. **For each why-answer pair, assign a category:**
   - **Process gap** — a step or check is missing from a workflow.
   - **Tooling gap** — no automated check or guard rail exists.
   - **Knowledge gap** — someone did not know or notice a fact that would have prevented the problem.
   - **Decision** — someone made a choice that directly caused the problem (neutral category; decisions can be right or wrong in retrospect).
   - **External** — outside the organization's control.

### Phase 3 — Validation and Action

7. **At the final why, ask: "Is this cause something we can prevent next time?"** If the honest answer is "no," you have not reached root cause — the chain breaks because no action is possible. Go back and re-examine the previous why-answer pair.

8. **Map each why-answer to a preventative action.** Not a fix to the current problem (that may already be done), but a systemic change:
   - For a **Process gap**: add a checklist, approval step, or runbook entry.
   - For a **Tooling gap**: implement monitoring, validation, or automation.
   - For a **Knowledge gap**: add documentation, training, or a decision log.
   - For a **Decision**: post-mortem analysis or a decision review process.

9. **Prioritize actions by likelihood and impact.** You have a causal chain; not every link is equally important to address. Ask: "If we fixed this, would the problem be prevented?" and "How likely is this cause to recur?" Focus on causes that are both likely and preventable.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Problem statement includes time, scope, and measurable symptom | Y/N |
| All five "why" answers describe mechanisms, not blame or vagueness | Y/N |
| Each why-answer is assigned a category (Process/Tooling/Knowledge/Decision/External) | Y/N |
| The final root cause is within the organization's control | Y/N |
| Each why in the chain has a corresponding preventative action | Y/N |
| At least one action is specific enough to assign to a person/team | Y/N |

## Red Flags

- The fifth why is "human error" or "someone wasn't paying attention." This is not root cause; it is abdication. If humans are the cause, the real cause is the absence of a check that would have caught the error before it propagated.
- The causal chain ends with an external cause (cloud provider outage, vendor bug) but the team has no plan to detect or work around it next time. This is learned helplessness, not closure.
- Only two or three whys were asked. Early stops often miss systemic issues. If a why-answer makes you immediately think "yes, that's the root," check by asking why one more time.
- The preventative actions are vague ("improve monitoring," "be more careful"). Vague actions are not actionable. A good action names the tool, person, or process change.
- Different team members arrive at different root causes for the same incident. This means the why-chain was not interrogated rigorously enough or assumptions were not shared. Re-run the method as a group.

## Output Format

```
## 5 Whys Assessment

**Incident/Problem:**
- Symptom: <what broke or went wrong>
- Context: <when, where, scope>
- Time detected: <time>

### Causal Chain

| Why # | Question | Answer | Category |
|---|---|---|---|
| 1 | Why did <symptom> happen? | <mechanism> | Process/Tooling/Knowledge/Decision/External |
| 2 | Why did <answer from #1> happen? | <mechanism> | <category> |
| 3 | Why did <answer from #2> happen? | <mechanism> | <category> |
| 4 | Why did <answer from #3> happen? | <mechanism> | <category> |
| 5 | Why did <answer from #4> happen? | <mechanism> | <category> |

### Root Cause
<Summary of the final why. Is it within your control? Can it be prevented?>

### Preventative Actions
1. **[Category]:** <specific, actionable step> — Owner: <person/team>
2. **[Category]:** <specific, actionable step> — Owner: <person/team>

### Confidence
<high | medium | low> — <justification: e.g., "high — root cause is documented in deploy logs and the preventative action (connection pool validation in CD pipeline) is within the team's control"; or "medium — the fifth why required an assumption about code timing that we cannot fully verify without reproduction">
```
