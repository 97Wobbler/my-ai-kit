---
name: pomodoro
display_name: Pomodoro Interval Discipline
class: heuristic
underlying_class: native
domain: productivity
source: Francesco Cirillo, 1987
best_for:
  - task estimation and scheduling
  - sustained focus in fragmented workdays
  - preventing burnout from unbroken work
one_liner: "Force focus and recovery on fixed intervals to reclaim a sense of time."
---

# Pomodoro Interval Discipline

## The Rule
Break work into fixed 25-minute focus intervals separated by 5-minute breaks; after four intervals, take a longer break. The constraint sharpens judgment about what fits in a single session.

## When It Applies
- Estimating how much work is actually doable in a day when tasks are abstract or open-ended.
- Protecting focus time in environments with frequent interrupts (chat, slack, ambient meetings).
- Detecting when a task is genuinely too large by observing how many pomodoros it actually consumes versus your initial guess.
- Recovering a sense of elapsed time after a stretch of context-switching or async work where time becomes invisible.

## When It Misleads
- On tasks requiring a long ramp-up (learning a codebase, getting into a proof, architectural thinking). The first two pomodoros are often wasted on context-build; the rule can make you feel productive while you're still loading.
- In work with external pacing (live collaboration, code review awaiting feedback, waiting for a build or test run). Pomodoros become a pretense of progress while you are actually blocked.
- When applied as a hard ceiling rather than a checkpoint. Some work genuinely requires two or three unbroken hours; forcing a break at the 25-minute mark does not shorten the work, only interrupt the flow state.
- On creative or exploratory work where the break rhythm breaks the momentum that was just starting to build.

## Common Misuse
Treating the pomodoro as a unit of accomplishment rather than a unit of honest effort. Declaring "I did five pomodoros" does not mean the work is 5× done if three of those intervals were spent in a blocked state or on context-switching overhead. The heuristic sharpens *time sense*, not *productivity measurement*.

Another misuse: rigidly applying the break schedule even when the work is flowing. The rule is a guardrail against drifting into 4-hour unbroken sprints, not a mandate to interrupt a state of genuine focus.

## How Agents Use It
- **Embedded**: in task-breakdown or time-estimation lenses, use pomodoro blocks as a unit to surface tasks that don't fit a reasonable session count (more than 8–10 pomodoros signals "this task is too large or ill-defined").
- **Sanity-gate**: on each scheduled work block longer than 90 minutes with no explicit break or context-shift, ask whether the agent has accounted for fatigue, context-switching cost, or unplanned interrupts, or whether the estimate assumes unbroken flow that will not survive the actual workday.
