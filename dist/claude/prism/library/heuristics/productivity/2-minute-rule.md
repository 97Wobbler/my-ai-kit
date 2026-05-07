---
name: 2-minute-rule
display_name: Two-Minute Rule
class: heuristic
underlying_class: native
domain: productivity
source: David Allen, Getting Things Done (2001)
best_for:
  - task triage and inbox processing
  - reducing decision friction on small items
  - breaking procrastination patterns
one_liner: "If it takes less than two minutes, do it now — delay is cost."
---

# Two-Minute Rule

## The Rule
If a task takes less than two minutes to complete, do it immediately rather than adding it to a list.

## When It Applies
- Processing inbox items (emails, Slack messages, tickets) where a quick reply or action clears the item entirely.
- Breaking procrastination on small, avoidable blockers that are psychologically present but take seconds to remove.
- Triage of bug reports or support requests where a fast assessment or one-step fix prevents later context-switching.
- Reducing list entropy: when the list itself becomes a burden, aggressive clearing of sub-two-minute items buys cognitive relief.

## When It Misleads
- When the "two-minute task" is actually a trap door into a longer job disguised as short work (a quick email reply that triggers a meeting, a "simple" code change that demands review and testing).
- In contexts where immediate action creates context-switching cost higher than the task duration—a developer pulled into a two-minute fix loses fifteen minutes of refocus time on deep work.
- When the task should not be done at all. The rule assumes the task is legitimate; it does not test legitimacy, only urgency.
- In high-interrupt environments, applying the rule to every micro-task can fragment attention worse than batching them later.

## Common Misuse
Treating the rule as "do everything that is short," rather than "do short things now instead of deferring them." The rule is a swap between modes (act vs. defer), not a blanket permission to act on everything. Many teams misapply it by never deferring anything, collapsing into constant interrupt-driven work with no deep work window.

Another failure mode: using the rule to justify context-switching as productive. If the cost of switching context exceeds the task duration, the heuristic misleads; the agent must estimate switching cost, not just task duration.

## How Agents Use It
- **Embedded**: in inbox-processing or triage lenses, after the legitimacy check and before the defer/batch decision, to cull small items that would otherwise stay on a list.
- **Sanity-gate**: on any recommendation to defer or batch a task, ask whether the task is actually under two minutes and whether deferring it has higher cost than completing it now. If yes on both, flag for immediate action.
