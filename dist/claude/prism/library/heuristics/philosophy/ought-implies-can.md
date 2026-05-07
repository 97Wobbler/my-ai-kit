---
name: ought-implies-can
display_name: Ought Implies Can
class: heuristic
underlying_class: native
domain: philosophy
source: Immanuel Kant, Critique of Practical Reason (1788)
best_for:
  - evaluating moral or practical demands on agents or systems
  - detecting impossible mandates disguised as obligations
  - sanity-checking requirement specifications against capability
one_liner: "Obligation presupposes ability."
---

# Ought Implies Can

## The Rule

No moral agent can be bound by a duty to perform an action it lacks the capacity to perform.

## When It Applies

- Evaluating ethical or legal demands on individuals or teams where the claimed obligation exceeds demonstrable capability (e.g., "be on-call 24/7 and maintain perfect work-life balance").
- Designing system requirements or SLAs where the specification demands outcomes the system architecture cannot deliver.
- Assessing responsibility in contexts where an agent was required to do something impossible before failure occurred.
- Reviewing organizational mandates ("ship with zero downtime," "never miss a deadline") that are logically impossible under real constraints.

## When It Misleads

- When "capacity" is read too narrowly. An agent may lack the capacity *right now* but have the capacity to acquire it (learn, hire, refactor). The heuristic applies to permanent incapacity, not temporary gaps.
- As an excuse for inaction. "I can't do it" may mean "it's hard" or "I haven't tried yet." The heuristic does not license passivity.
- In domains where the obligation is to *try*, not to *succeed*. A physician has a duty to attempt resuscitation even if success is unlikely; the duty is not nullified by incapacity to guarantee outcome.
- When applied to collective action. A team may have the distributed capacity to do X even if no individual has it alone; the heuristic must account for coordination.

## Common Misuse

The heuristic is often invoked to shut down conversation without examining what capacity actually means in context. Someone citing "ought implies can" to dismiss a demand may be using it to avoid either (a) acquiring the needed capacity, or (b) renegotiating the obligation. The heuristic is a diagnostic tool, not a permission slip.

It is also misapplied when the agent conflates "I am unwilling" with "I am unable." Kant's principle addresses incapacity in principle, not reluctance or inconvenience.

## How Agents Use It

- **Embedded**: in requirements-validation or design-review lenses, as a check step after capability assessment. For each stated obligation (SLA, mandate, acceptance criterion), force the agent to name the mechanism by which it will be satisfied, or flag the obligation as incoherent.
- **Sanity-gate**: on each top recommendation that includes a new obligation (deadline, quality bar, availability guarantee), ask: "Does the target have or can acquire the capacity to deliver this? If not, is the obligation itself wrongly stated?"
