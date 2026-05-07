---
name: pre-mortem
display_name: Pre-mortem
class: lens
underlying_class: native
domain: general
source: Gary Klein, 1999 (Harvard Business Review)
best_for:
  - Surfacing risks before they materialize
  - Building group consensus on failure modes
  - Moving past optimism bias in planning
one_liner: "Assume failure and work backward through its causes to expose present blind spots."
---

# Pre-mortem

## Overview
A pre-mortem inverts the typical risk conversation. Instead of asking "What could go wrong?" (which triggers defensive reasoning), it asks "We are six months in the future. The project failed spectacularly. Why?" This reframing suspends the constraint that the project *should* succeed and allows people to speak candidly about problems they see but haven't named. Practitioners use it before launching initiatives to capture risks that a forward-looking risk assessment would miss — especially organizational and behavioral risks that don't show up in spreadsheets.

## Analytical Procedure

### Phase 1 — Setup

1. **Define the project or initiative.** State it as a concrete outcome: "We ship the mobile app," "We onboard 50 new customers," "We refactor the core service." Not abstract ("improve efficiency"). Write it one sentence. This is the future success you are killing in imagination.

2. **Establish the temporal frame.** Choose a specific point in the future — "six months from launch," "end of Q3," "when it hits 10k users." Everyone must use the same horizon. Shorter horizons (months) surface implementation risks; longer horizons (year+) surface strategy and adoption risks.

3. **Brief the group.** Read aloud: "It is [DATE]. The initiative [PROJECT] has failed. It didn't deliver the intended outcome. We are here to explain why it failed. Assume this failure is real. You do not need to defend the original decision. The goal is to understand what went wrong." This is the permission structure — it revokes the obligation to be optimistic.

### Phase 2 — Silent Generation

4. **Each person writes independently for 5–10 minutes.** Prompt: "The project failed. Write down the reasons — what went wrong, what didn't happen, what we didn't see coming, who dropped the ball, what changed, what we were naive about." No discussion yet. Writing is private to each person.

5. **Create an inventory.** Go around the table. Each person states one failure reason. Write every reason on a shared surface (whiteboard, document) without evaluation or discussion. If someone repeats a reason, mark it as a duplicate rather than restating. Continue until all reasons are listed.

6. **Do not dismiss, explain, or defend any reason at this stage.** A reason is "We didn't get buy-in from ops" even if ops was not involved. A reason is "The market wasn't ready" even if market research said it was. You are not evaluating truthfulness — you are inventorying perceived risks.

### Phase 3 — Clustering and Interrogation

7. **Group reasons into categories.** Common categories are: organizational (unclear roles, silos, incentive misalignment), technical (architecture debt, integration failures), market/user (adoption didn't happen, use case was wrong), execution (timeline collapsed, resources reallocated), and dependency (external parties didn't deliver). Group reasons by hand. Category names emerge from the reasons, not the other way around.

8. **For each category, ask: "What would have to be true to prevent this failure?"** Write the preventive action as a concrete, testable statement. If the reason is "Ops wouldn't adopt the tool," ask: "What would have to happen during design and rollout for ops to actually use it?" Not "build ops support" (too vague), but "run a pilot with the ops team lead's team, get three sign-offs before launch, allocate ops on-call to the project."

9. **Identify which reasons map to *existing* project plans.** Go through the list. For each reason, ask: "Is there a person, task, or dependency in the current project plan that owns preventing this failure?" Mark it `Covered` or `Gap`. Reasons with no corresponding plan element are gaps.

### Phase 4 — Disposition

10. **For gaps, decide the action.** Each gap is one of:
    - **Add to plan** — Create a task, hire a person, or add a dependency to the project plan.
    - **Accept the risk** — The failure mode is real but the cost to prevent it exceeds the value of the initiative. Document this as an accepted risk.
    - **Reframe the goal** — The reason reveals that the original goal was misstated. Revise what "success" means.
    - **Kill the project** — Rarely, the pre-mortem surfaces a gap so large that continuing is unjustifiable. This is a success of the method.

11. **Assign ownership.** For each action (add, accept, reframe), assign one person to implement, document, or escalate the decision. Vague assignment (e.g., "someone will handle this") is a red flag that the failure mode will return.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Initiative defined as a concrete outcome (not abstract) | Y/N |
| Temporal horizon stated and shared across group | Y/N |
| All participants generated at least one failure reason | Y/N |
| Reasons are stated as concrete failures, not vague concerns | Y/N |
| Each category has a corresponding "what would prevent this" preventive action | Y/N |
| Gaps are identified (reasons with no corresponding plan element) | Y/N |
| Each gap has a disposition: Add/Accept/Reframe/Kill | Y/N |
| Ownership assigned to named person for each disposition | Y/N |

## Red Flags

- The group generates only 3–4 reasons. Either the initiative is trivial (unlikely) or people are holding back. Use the silent writing phase — it increases volume and psychological safety.
- All reasons are technical. Groups often retreat to technical risk because it feels safe and objective. Ask explicitly: "What could go wrong between people, with leadership, or with the market?" Press until non-technical reasons emerge.
- A reason is stated as "It could fail because of X" rather than "It failed because of X." The temporal frame (imagining failure as real, not possible) must be enforced. Re-read the failure as a fact.
- No gaps identified. Either the plan is remarkably comprehensive (check assumption) or people are not looking for missing pieces (more likely). Re-examine reasons: "Is there currently someone responsible for preventing this?"
- Dispositions are vague ("we'll be more careful") or unowned ("someone should think about this"). A disposition without a name and a deadline is not a decision — it is avoidance.
- The group agrees on all reasons and all dispositions. Consensus in a pre-mortem is a smell — it suggests conformity, not truth-seeking. Seek dissent explicitly: "Who sees a failure mode nobody else mentioned?"

## Output Format

```
## Pre-mortem Assessment

**Initiative:**
<Concrete outcome statement>

**Temporal frame:**
<Date and scenario>

### Failure Reasons (raw inventory)
1. <Reason as stated by participant>
2. <Reason as stated by participant>
...

### Clustered Reasons and Preventive Actions
| Category | Reasons | Preventive action ("what would have to be true") |
|---|---|---|
| <Category name> | <Reason 1>, <Reason 2> | <Concrete action> |

### Plan Coverage Analysis
| Reason | Covered in current plan? | Gap? |
|---|---|---|
| <...> | Y/N | Y/N |

### Dispositions and Ownership
| Gap | Disposition | Action | Owner | Deadline |
|---|---|---|---|---|
| <Reason> | Add/Accept/Reframe/Kill | <Specific action or acceptance statement> | <Name> | <Date> |

### Confidence
<high | medium | low> — <Justification. Note: confidence here reflects the group's alignment on failure modes and the clarity of gap ownership, not the likelihood of success.>
```
