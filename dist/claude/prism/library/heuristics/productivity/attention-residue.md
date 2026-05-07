---
name: attention-residue
display_name: Attention Residue (Leroy)
class: heuristic
underlying_class: native
domain: productivity
source: Sophie Leroy, 2009
best_for:
  - task switching decisions
  - context-heavy work planning
  - productivity diagnosis
one_liner: "After a task switch, cognitive residue from the prior task hurts performance."
---

# Attention Residue

## The Rule

When you switch tasks, your attention does not follow instantaneously; the cognitive load of the prior task persists and degrades performance on the new one.

## When It Applies

- Diagnosing unexplained performance drops in work that requires deep focus after context-heavy interruptions.
- Scheduling decisions where back-to-back high-attention tasks are being packed without transition time.
- Evaluating why context-switch cost feels worse than the sum of individual task-switching overheads.
- Assessing whether a "productivity crisis" stems from too many interruptions or from residue accumulation across a day of switching.
- Prioritizing deep work: if a task is cognitively heavy and requires full attention, the preceding task matters as much as the following buffer.

## When It Misleads

- Not all task switches incur equal residue. Switching from a closed task (email marked done) to a new one leaves less residue than switching mid-problem.
- Residue dissipates over time — a 15-minute transition can clear most of the load. Treating residue as permanent confuses the decay curve with the initial spike.
- Some people naturally compartmentalize better than others. Leroy's research shows variance; claiming residue affects everyone equally ignores individual differences in attention control.
- In highly interruptible work (support, on-call), residue is only one cost among many; using it to justify "no interruptions ever" ignores the domain's actual constraints.

## Common Misuse

Invoking attention residue as a blanket excuse for any drop in output after a context switch, without examining whether the residue was actually load-bearing (i.e., whether the prior task was cognitively heavy) or whether the new task simply required ramp-up. Residue is a real phenomenon, but it is also easy to overdiagnose when other explanations — missing context, shallow engagement, inadequate prior preparation — are more direct.

## How Agents Use It

- **Embedded**: in work-schedule and prioritization lenses, at the step where task sequencing is decided. The heuristic prompts explicit ordering: heavy-attention tasks should not follow heavy-attention tasks without a break, and shallow tasks should precede deep work, not follow it.
- **Sanity-gate**: when evaluating a productivity recommendation that involves time-boxing or task scheduling, ask whether the plan accounts for residue decay (15–30 min transition time after context-heavy work) or assumes attention switches instantaneously.
