---
name: reverse-brainstorming
display_name: Reverse Brainstorming
class: lens
underlying_class: native
domain: brainstorming
source: Edward de Bono (Lateral Thinking, 1970); popularized in innovation workshops and root-cause analysis
best_for:
  - Uncovering hidden assumptions in a problem
  - Finding root causes by inverting the question
  - Breaking through cognitive fixation on existing solutions
one_liner: "Look for ways to make the problem worse, then invert to surface causes."
---

# Reverse Brainstorming

## Overview
Instead of asking "How do we solve this problem?", ask "How could we make this problem worse?" Generate ideas on the inverse, then flip them back to yield solutions that target root causes rather than symptoms. Practitioners reach for this when conventional brainstorming produces surface-level fixes, or when the real causes of a problem remain hidden beneath multiple layers of attempted workarounds.

## Analytical Procedure

### Phase 1 — Invert the Problem

1. **State the problem as a clear, outcome-focused sentence.** Write what currently goes wrong in concrete terms, not the desired state.
   - Bad: "We need better customer retention."
   - Good: "Customers cancel subscriptions within 3 months at a 40% rate."

2. **Invert the problem statement to ask how to maximize the bad outcome.** Rewrite to target the opposite direction explicitly.
   - Inverted: "How could we get customers to cancel within 3 months at an even higher rate?"

3. **List every action or condition that would worsen the problem.** Brainstorm freely. This is divergent — aim for 15-25 ideas before filtering. Be specific; "make the product worse" is too vague.
   - Example ideas: Hide the onboarding steps. Send confusing billing emails every week. Ignore support tickets. Make the interface unintuitive. Never follow up after purchase. Increase prices without warning. Ship broken features.

### Phase 2 — Analyze Root Causes

4. **For each "how to make it worse" idea, ask: "Is this already happening in some form?"** Mark each as:
   - **Active** — we are deliberately or inadvertently doing this.
   - **Latent** — we are not doing this, but nothing stops it from happening.
   - **Protected** — we have safeguards against this.

5. **Cluster the Active and Latent ideas by root cause.** Group ideas that stem from the same underlying failure. Write the inferred cause for each cluster.
   - Example cluster: "Hide onboarding," "Don't send tutorials," "No in-app guidance" → Root cause: *No onboarding investment or ownership.*
   - Another cluster: "Ignore support tickets," "No response SLA," "Hidden support contact" → Root cause: *Support is treated as a cost center, not a revenue protector.*

6. **Prioritize clusters by impact.** Which clusters, if left unfixed, would most likely cause the problem? Rank them 1–N.

### Phase 3 — Reverse to Solutions

7. **For each cluster, invert the root cause back to an affirmative action.** Do not just negate; propose a positive change grounded in the inverse of the root cause.
   - Inverted cause: "No onboarding investment" → Solution: "Design and staff a structured onboarding program with milestones and metrics."
   - Inverted cause: "Support treated as cost center" → Solution: "Tie support team incentives to retention metrics; empower first-line support to resolve issues immediately."

8. **For each solution, estimate effort and expected impact on the problem metric.** Use a simple scale (High/Medium/Low) for both.
   - Example: Onboarding program — Effort: High. Impact on 40% cancellation rate: Medium (estimated move to 32–35%).
   - Example: Support incentive change — Effort: Low. Impact: Medium–High (estimated move to 28–30%).

### Phase 4 — Validate Against Symptoms vs. Root Causes

9. **Compare your solutions against the original problem statement.** Ask: "If we implemented this, would we be fixing a symptom or addressing a root cause?"
   - Symptom fix: "Send customers a special discount email if they haven't logged in for 2 weeks."
   - Root cause fix: "Invest in customer success onboarding so they reach value in week 1."

10. **Discard or deprioritize symptom fixes unless they are extremely low-cost quick wins.** Root-cause solutions should dominate your action list.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Problem statement is specific, measurable, and outcome-focused (not a desired state) | Y/N |
| Inverted problem statement is clearly opposite and actionable | Y/N |
| At least 15 "how to make worse" ideas were generated | Y/N |
| Each idea was marked Active/Latent/Protected | Y/N |
| Ideas were clustered into 3 or more root-cause groups | Y/N |
| Each cluster has an inferred root cause written explicitly | Y/N |
| Solutions are stated as affirmative actions, not negations | Y/N |
| At least one solution is a root-cause fix, not a symptom fix | Y/N |
| Effort and impact were estimated for each solution | Y/N |

## Red Flags

- The inversion is shallow: "How do we make it worse?" produces only obvious answers like "do nothing" or "ignore it." Push for specificity; the power of the method lies in discovering what you are *already* doing wrong.
- All ideas are marked "Protected" or "Latent." Either your brainstorm was too cautious or your organization genuinely has no exposure — confirm before moving on.
- Solutions are restated symptoms: "Cancel less often" instead of "Fix the root cause of why customers want to cancel." The inversion was not actually reversed.
- No clustering step was performed. Without grouping by root cause, the solutions remain scattered and tactical.
- Effort and impact estimates were omitted. Without them, you cannot prioritize and may invest in high-effort, low-impact changes.
- The problem statement was a goal ("increase retention") not an outcome ("customers cancel at 40%"). Goals hide the actual failure mode.

## Output Format

```
## Reverse Brainstorming Assessment

**Problem (specific, measurable outcome):**
<statement of what currently goes wrong>

**Inverted problem:**
<how to maximize the bad outcome>

### Phase 1 — How to Make It Worse
| Idea | Active / Latent / Protected |
|---|---|
| <...> | <...> |

### Phase 2 — Root Cause Clusters
| Cluster | Ideas | Inferred Root Cause | Priority |
|---|---|---|---|
| <...> | <...> | <...> | 1/2/3/... |

### Phase 3 — Solutions
| Root Cause | Inverted to Solution | Effort | Estimated Impact | Root Cause Fix? |
|---|---|---|---|---|
| <...> | <...> | H/M/L | H/M/L | Y/N |

### High-Priority Actions
1. <solution> — <justification for priority>
2. ...

### Confidence
<high/medium/low> — <justification>
```
