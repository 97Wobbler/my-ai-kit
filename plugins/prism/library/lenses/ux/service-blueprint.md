---
name: service-blueprint
display_name: Service Blueprint
class: lens
underlying_class: native
domain: ux
source: Shostack & Kingman-Brundage (1990s service design); formalized in Bitner, Booms & Tetreault (1990)
best_for:
  - Mapping all actors and touchpoints in a service delivery system
  - Identifying failure points where customer and operational realities diverge
  - Aligning front-stage (visible) and back-stage (hidden) operations
one_liner: "Map the service ecosystem across four layers — customer, front-stage, back-stage, support."
---

# Service Blueprint

## Overview
A Service Blueprint visualizes the complete service delivery system by separating customer-facing interactions (front-stage), employee actions that enable those interactions (middle-stage), and organizational support systems (back-stage) into distinct lanes. Practitioners use it to surface misalignments between what the customer expects, what front-line staff can deliver, and what back-office processes actually support—the gaps are where services fail. The discipline is refusing to view the service from the customer perspective alone; operations matter as much as the experience.

## Analytical Procedure

### Phase 1 — Map Customer Journey

1. **Define the service scope.** Write one sentence describing what the service delivers (e.g., "order placement and fulfillment for an e-commerce site"). Include start and end points.

2. **Identify the customer persona.** Name the primary user: their goal, context, and constraints (time, knowledge, emotional state). If multiple personas exist, run this separately for each.

3. **Break the customer journey into discrete phases.** A phase is a cohesive stage with a single goal:
   - Bad: "Customer interacts with website" (too broad)
   - Good: "Customer searches for product," "Customer adds item to cart," "Customer completes checkout," "Customer receives confirmation email"
   Write 4-8 phases in sequence.

4. **For each phase, list the customer touchpoints.** A touchpoint is anything the customer sees, hears, or interacts with:
   - Digital: web page, email, SMS, app notification
   - Physical: retail store, printed receipt, product packaging
   - Human: phone call with agent, in-person conversation
   Write all touchpoints for the phase, in order of encounter.

### Phase 2 — Map Front-Stage Actions

5. **For each customer touchpoint, identify the front-line actor(s).** Who delivers this touchpoint? Examples: checkout page engineer, customer service rep, delivery driver, product picker in warehouse.

6. **Write the employee/system action required to fulfill that touchpoint.** This is what the customer sees as the result of:
   - Bad: "Process the order" (what's hidden in this?)
   - Good: "Validate payment, reserve inventory, generate order number, trigger fulfillment system, send confirmation"
   Be granular. Each action is a decision or operation.

7. **Mark each action as visible or invisible to the customer:**
   - Visible: customer sees it happen or sees its result in real time (e.g., "checkout button becomes enabled")
   - Invisible: happens in the background; customer doesn't see the mechanism (e.g., "inventory database is queried")
   Visible actions are front-stage. Invisible actions are the boundary between front and middle.

### Phase 3 — Map Back-Stage Support Systems

8. **For each front-stage action, identify the back-stage processes required.** What systems, teams, or workflows must run to make that action possible?
   - Examples: inventory management system, payment processor, CRM database, warehouse management, compliance check, pricing engine
   List each back-stage dependency.

9. **For each back-stage system, write its job.** What does it do? What data does it consume and produce? How fast must it respond?
   - Bad: "Handles inventory"
   - Good: "Tracks stock by SKU and warehouse; updates in real time on sale; triggers reorder at threshold; must respond within 500ms"

10. **Identify support functions that don't handle customer interactions but enable operations.** Examples: HR (staff training), Finance (budgeting), Compliance (audits), IT (infrastructure). Write one sentence for each: what do they do that affects service quality?

### Phase 4 — Identify Failure Points

11. **For each front-stage action, note the conditions under which it would fail.** Examples:
    - Payment processor is down → customer can't complete checkout
    - Inventory system is out of sync → order confirmation says item is in stock when it isn't
    - Staff training is inadequate → rep gives inconsistent information
    - Back-stage system is slow → customer waits for response
    Write at least one failure mode per action.

12. **Mark the severity of each failure.**
    - **Critical**: Service cannot complete; customer is blocked
    - **Major**: Service degrades noticeably; customer is frustrated but not blocked
    - **Minor**: Inconvenience or poor experience quality; service completes
    Use this to prioritize which failures to address.

### Phase 5 — Assess Alignment

13. **Check alignment between stages.** For each front-stage action, verify:
    - Does the back-stage system have the capacity (speed, accuracy, uptime) the front-stage needs?
    - Does the front-line staff have the authority, information, and tools to execute?
    - Are service standards clear? (e.g., "checkout must complete in under 10 seconds")
    - Are there hidden hand-offs or delays?
    Write alignment findings as aligned/misaligned with reason.

14. **Identify the "line of visibility."** Anything below this line is hidden from the customer. Flag if the customer is told something is "simple" when it's actually complex back-stage, or vice versa.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Service scope is one clear sentence with start/end points | Y/N |
| Customer persona is named with goal and context | Y/N |
| Customer journey has 4-8 distinct phases | Y/N |
| Every customer touchpoint is listed under its phase | Y/N |
| Every front-stage action is marked visible or invisible | Y/N |
| Back-stage systems are listed for each front-stage action | Y/N |
| At least one failure mode is identified per front-stage action | Y/N |
| Failure modes are severity-tagged (critical/major/minor) | Y/N |
| Alignment check was applied: does back-stage support front-stage? | Y/N |
| Line of visibility is explicitly marked | Y/N |

## Red Flags

- All front-stage actions are marked "visible." Either the service is trivial or you're not separating the customer's view from the technical reality.
- No back-stage systems identified. Either the service is a single person's job (rare) or you've missed the operational dependencies.
- Failure modes are absent or generic ("system could go down"). Think through specific failure paths: payment processor offline, inventory lag, staff turnover, network latency.
- Front-stage and back-stage are at different levels of granularity. Front-stage should be atomic (one customer-visible action), back-stage should describe systems/processes, not individual clicks.
- Alignment check only says "aligned" everywhere. Systems are never perfectly aligned; you've either not looked hard or you've assumed everything works.
- The blueprint ignores support functions (HR, Finance, IT). These aren't customer-facing, but they directly affect whether front-stage and back-stage can perform.

## Output Format

```
## Service Blueprint Assessment

**Service Scope:**
<one sentence with start/end points>

**Customer Persona:**
<name, goal, context, constraints>

### Customer Journey

| Phase | Touchpoints | Type |
|---|---|---|
| <phase name> | <touchpoint list> | digital/physical/human |

### Front-Stage Actions & Mapping

| Phase | Customer Sees | Front-Stage Action | Visible? | Back-Stage System Needed |
|---|---|---|---|---|
| <phase> | <what customer encounters> | <what actor does> | yes/no | <system, process, team> |

### Back-Stage Systems

| System | Function | Required Capacity | Response Time |
|---|---|---|---|
| <name> | <job description> | <capacity constraint> | <acceptable latency> |

### Failure Points

| Front-Stage Action | Failure Mode | Severity | Prevention |
|---|---|---|---|
| <action> | <what goes wrong> | critical/major/minor | <what must work> |

### Alignment Assessment

| Front-Stage Requirement | Back-Stage Reality | Aligned? | Gap |
|---|---|---|---|
| <what front needs> | <what back provides> | yes/no | <mismatch description if no> |

### Line of Visibility
<Describe what sits above the line (customer sees) and below (hidden operations). Call out any misalignment between complexity and customer expectation.>

### Support Functions
- <Function>: <impact on service delivery>

### Key Findings
1. <Critical alignment issue or failure mode>
2. <Design opportunity or dependency>
3. ...

### Confidence
<high/medium/low> — <justification: e.g., "high — all phases mapped, back-stage systems verified with ops team" or "medium — customer perspective clear but back-stage coverage incomplete">
```
