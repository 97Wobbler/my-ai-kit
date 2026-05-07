---
name: task-batching
display_name: Task Batching
class: heuristic
underlying_class: native
domain: productivity
source: origin uncertain
best_for:
  - time-block scheduling
  - interrupt-heavy environments
  - deep work protection
one_liner: "Group similar tasks to cut context-switching cost."
---

# Task Batching

## The Rule
Group similar tasks together and execute them in a contiguous block rather than interleaving them with dissimilar work; each context switch carries a switching cost that accumulates faster than the time saved by task-ordering flexibility.

## When It Applies
- Writing or code review, where mental models of a codebase take 10–15 minutes to load and switching breaks the model.
- Meetings or communication that require sustained presence in a different "mode" (async writing vs. real-time discussion).
- Administrative tasks (email triage, expense reports, ticket labeling) that have a uniform cognitive footprint and low interdependency.
- Support or customer-facing work where context is domain-specific and repetition reduces per-task latency.

## When It Misleads
- When the tasks have hard sequential dependencies and the first task is blocked; batching forces waiting instead of switching to unblocked work.
- In genuinely reactive work (on-call, emergency response), where the point of the role is to interrupt whatever else you're doing; batching is the opposite of what's needed.
- When context-switching cost is low or invisible (e.g., simple rote tasks, fully internalized mental models) but batching is mandated anyway, turning flexibility into false discipline.
- When the "batch" grows so large that fatigue sets in and quality degrades faster than context-switch savings accumulate (diminishing returns).

## Common Misuse
Treating task batching as a universal law rather than a trade-off. The heuristic assumes that the switching cost is real and larger than the cost of holding a task in queue; this is true for cognitively heavy work and false for light work or work with short deadlines. Teams often over-batch (e.g., a single "email batch" that swallows two hours) in the name of discipline, when smaller, more frequent batches would be more efficient.

Another misuse: conflating batching with procrastination. Batching defers tasks to a scheduled block; procrastination defers them indefinitely. If a "batch" is perpetually pushed back, batching is being used as cover for avoidance.

## How Agents Use It
- **Embedded**: in time-blocking or schedule-design lenses, when recommending how to partition the day, as a check on whether a proposed schedule interleaves tasks that should be batched (e.g., "all code review together" vs. "code review scattered across four slots").
- **Sanity-gate**: on each time-allocation recommendation, ask whether the proposed task order forces switching between dissimilar cognitive modes, and if so, whether reordering into batches would reduce total time by more than the imposed waiting cost.
