---
name: mise-en-place
display_name: Mise en Place
class: heuristic
underlying_class: native
domain: cooking
source: French culinary practice, 19th century
best_for:
  - time-critical execution
  - high-stakes deployments
  - incident response
one_liner: "Organize and verify every ingredient and tool before execution."
---

# Mise en Place

## The Rule
Before starting the active work, stage all the ingredients, tools, and state you will need and verify they are ready.

## When It Applies
- Deployments, migrations, and cutover operations where a missing tool or incorrect state mid-execution is expensive.
- Incident response and debugging sessions: have logs, dashboards, reproduction steps, and rollback procedures open before touching the system.
- Hotfixes and time-pressured problem-solving where context-switching mid-task carries high cost.
- High-stakes presentations, interviews, or demonstrations where you cannot pause to fetch missing information.
- Surgical procedures, safety-critical operations, and any task where recovery from an incomplete setup is slow or dangerous.

## When It Misleads
- When the setup ritual becomes procrastination — spending hours preparing for work that could start with 60% of the pieces in place. Mise en place serves execution, not the reverse.
- In genuinely exploratory work where the output shape is unknown and advance preparation locks in assumptions the exploration should question.
- When the cost of a mid-task discovery is actually low. In a low-pressure, reversible setting, "prepare as you go" is faster than "prepare perfectly upfront."
- In domains with frequent pivots or requirement changes, where pre-staging becomes waste when the goal shifts.

## Common Misuse
Treating mise en place as a universal productivity principle divorced from its time-critical setting. The heuristic's power is specifically about tasks where a discovered gap under time pressure is expensive; it is much weaker in leisurely, exploratory, or highly reversible settings.

Another common failure: confusing "prepared" with "overexplained." A checklist of 40 items is not mise en place if it delays the start by hours; the rule is about *necessary* readiness, not perfection.

## How Agents Use It
- **Embedded**: in deployment, incident-response, and cutover lenses, as a mandatory pre-execution checklist step. The procedure should name the ingredients (data, configs, rollback steps, dashboards), verify each exists and is accessible, and report blockers before the active phase starts.
- **Sanity-gate**: on any recommendation involving time-critical execution (go-live, hotfix deployment, rollback, incident drill), ask: "Are the prerequisites explicitly listed, accessible without searching, and verified to work in advance—or assumed?"
