---
name: hoshin-kanri
display_name: Hoshin Kanri
class: lens
underlying_class: native
domain: okr
source: Shoji Shiba (Toyota, 1960s); formalized in Japan as Hoshin Kanri; introduced to the West by Yoji Akao
best_for:
  - Cascading strategic objectives through an organization with feedback loops
  - Aligning annual plans to multi-year vision without siloing departments
  - Identifying and breaking misalignment between strategy and execution
one_liner: "Visualize strategy as an X-matrix and cascade it through the organization."
---

# Hoshin Kanri

## Overview
Hoshin Kanri (policy deployment) translates long-term strategy into annual objectives using an X-Matrix that forces explicit connection between vision, annual goals, initiatives, and responsible owners. Unlike top-down mandates that departments ignore or misinterpret, Hoshin requires bidirectional negotiation: top leadership proposes targets, middle management challenges feasibility, and the organization agrees on a shared plan with built-in review cycles. Practitioners use it when strategy feels disconnected from day-to-day work and when accountability disappears between planning cycles.

## Analytical Procedure

### Phase 1 — Strategy Extraction and Clarification

1. **State the organization's 3-5 year vision in plain language.** Not a mission statement. What does success look like in 3-5 years? Revenue, market position, capability, culture? Write it as concrete outcomes a customer or employee would recognize.

2. **Identify the critical few annual strategic priorities.** Not a list of everything the organization could do. Ask: "If we achieve only 3-5 things this year, which ones unlock the vision?" Narrow ruthlessly. Each should be expressible in one sentence without jargon.

3. **For each annual priority, list the current state and target state.** Use metrics where possible. Bad: "improve customer satisfaction." Good: "NPS from 42 to 55" or "support ticket resolution time from 48 hours to 4 hours."

### Phase 2 — Capability and Initiative Mapping

4. **Identify which organizational capabilities must improve to close each gap.** If the target is "NPS 42→55," what capabilities drive that? Better product quality? Faster support response? More empathetic onboarding? List 2-4 capabilities per priority.

5. **For each capability, identify the specific initiatives (projects, programs, process changes) that will improve it.** These are not vague ("improve quality") but concrete actions with owners: "reduce defects in the payment flow by 60% (Owner: Engineering, Q2-Q3)" or "implement real-time chat support (Owner: Customer Success, Q1)."

6. **Cross-check: can the proposed initiatives actually deliver the target metrics?** This is the moment of truth. If the gap between current state and target requires a 30% improvement but the initiatives only plausibly deliver 10%, flag it and either revise the target, add initiatives, or challenge the capability assumption.

### Phase 3 — X-Matrix Construction

7. **Build the X-Matrix as a 4-quadrant table:**
   - **Top-left:** Annual priorities (rows) vs. long-term vision elements (columns). Cells show which priorities support which vision components.
   - **Top-right:** Annual priorities (rows) vs. key performance indicators (columns). Cells show which metrics measure success on each priority.
   - **Bottom-left:** Key capabilities (rows) vs. annual priorities (columns). Cells show which capabilities enable which priorities.
   - **Bottom-right:** Initiatives (rows) vs. key capabilities (columns). Cells show which initiatives build which capabilities.

8. **Fill each cell with a strength rating: strong (●), medium (◐), weak (○), or null (blank).** Use dots, not words. The purpose is to visually verify that:
   - Every annual priority has at least one path to the vision (top-left filled).
   - Every priority has measurement mechanisms (top-right filled).
   - No priority is orphaned (no row in bottom-left with no dots).
   - No initiative is isolated (every initiative in bottom-right connects to at least one capability).

9. **Walk the matrix horizontally and vertically.** Read each row left-to-right to verify the chain: initiative → capability → priority → vision. Any gap is a broken link. Read each column top-to-bottom to verify no priority lacks capability support.

### Phase 4 — Negotiation and Commitment

10. **Present the matrix to middle management and team leads.** Their job is not to accept it but to challenge feasibility. Ask: "Can you actually deliver this initiative with the resources and constraints you have?" Accept pushback. Good Hoshin requires honest disagreement before agreement.

11. **Revise targets and initiatives based on feedback.** If middle management says "NPS 42→55 is not reachable," either reduce the target to something credible (e.g., NPS 42→50) or add initiatives. The goal is alignment, not compliance.

12. **Assign explicit owners to each annual priority and each initiative.** One name per priority. One name per initiative. Owners are responsible for reporting progress and escalating blockers.

### Phase 5 — Review and Feedback Cycles

13. **Schedule monthly priority reviews.** Owners report: (1) progress on initiatives, (2) progress on capability-building, (3) progress toward priority targets, (4) blockers. Review is not judgment; it's early warning.

14. **Conduct quarterly strategy check-ins.** Ask: are the assumptions in the matrix holding? Is the market still the same? Is the initiative actually building the capability we thought? If not, revise the matrix and initiatives — not the annual goals (those stay stable unless the market fundamentally shifts).

15. **At year-end, assess outcome.** Did we hit the targets? Which initiatives worked? Which capabilities still need work for next year's vision step? Use this assessment to draft next year's Hoshin.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Vision statement is specific and outcome-focused (not aspirational vagueness) | Y/N |
| 3-5 annual priorities stated with current→target metrics | Y/N |
| Every priority has 2-4 named capabilities that close the gap | Y/N |
| Every capability has 2-3 concrete named initiatives with owners | Y/N |
| X-Matrix is fully connected (no orphaned rows/columns) | Y/N |
| Every annual priority has at least one owner name | Y/N |
| Middle management has reviewed and challenged (evidence of revision) | Y/N |
| Monthly and quarterly review cycles are scheduled | Y/N |

## Red Flags

- Vision is a tagline ("be the leading provider"). It's not falsifiable. Go deeper.
- Annual priorities number more than 5 or fewer than 2. The "critical few" discipline was abandoned.
- Initiatives are vague ("improve process," "invest in quality"). They need names, owners, and expected metrics.
- X-Matrix has blank rows or columns (isolated priorities, orphaned capabilities). The matrix is not actually connected.
- No evidence that middle management pushed back or revised. Either the strategy was already obvious (unlikely) or the organization is not actually negotiating (common failure mode).
- Targets are unquantified ("improve," "accelerate," "enhance"). You cannot measure success.
- No monthly review cycle scheduled. Without rhythm, alignment degrades within weeks.
- Owners are departments, not people. "Engineering will deliver it" is not accountability. Name the person.

## Output Format

```
## Hoshin Kanri Deployment

**Vision (3-5 year outcome):**
<concrete description of success state>

### Phase 1 — Annual Strategic Priorities
| Priority | Current State | Target State | Gap Magnitude |
|---|---|---|---|
| <priority 1> | <metric> | <metric> | <direction, % or absolute> |
| <priority 2> | <metric> | <metric> | <direction, % or absolute> |

### Phase 2 — Capability and Initiative Map
| Priority | Required Capability | Initiative (Owner, Timeline) | Expected Contribution to Gap |
|---|---|---|---|
| <priority 1> | <capability A> | <initiative X (Name, Q1-Q2)> | High/Medium/Low |
| | <capability B> | <initiative Y (Name, Q2-Q3)> | High/Medium/Low |

### Phase 3 — X-Matrix Summary
```
[Visual or text representation of the 4-quadrant matrix with strength ratings]

Vision components: [listed]
Annual priorities: [listed]
Key capabilities: [listed]
Initiatives: [listed]

Connectivity check: [All rows/columns filled? Y/N. Any orphans? List them.]
```

### Phase 4 — Ownership and Review Cadence
| Annual Priority | Owner Name | Monthly Review | Quarterly Review |
|---|---|---|---|
| <priority 1> | <name> | Scheduled | Scheduled |

Revision history: [Evidence that middle management challenged and matrix was revised]

### Phase 5 — Confidence Assessment

**Confidence: <high | medium | low>**

Reasoning:
- Vision clarity: <articulate, vague, or untestable>
- Strategy-to-execution linkage: <fully mapped, partially mapped, or unclear>
- Owner commitment: <explicit alignment, lip service, or absent>
- Review discipline: <scheduled and tracked, informal, or missing>
- Evidence of negotiation: <pushback documented, assumed consensus, or top-down imposed>

**Key risks to plan execution:**
1. <risk and mitigation>
2. <risk and mitigation>
```
