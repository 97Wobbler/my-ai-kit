---
name: parkinsons-law
display_name: Parkinson's Law
class: heuristic
underlying_class: native
domain: general
source: C. Northcote Parkinson, The Economist, 1955
best_for:
  - estimation and deadline setting
  - scope creep diagnosis
  - process bloat review
one_liner: "Work expands to fill the time allotted — slack gets consumed without constraints."
---

# Parkinson's Law

## The Rule

Work expands to fill the time available for its completion; absent hard constraints, available slack will be consumed by the work itself, administrative overhead, or scope that was never named.

## When It Applies

- Estimating how long a task will take when the deadline is soft, negotiable, or unspecified.
- Reviewing projects that slip quietly without identifying concrete blockers or external dependencies.
- Evaluating meetings, approval processes, and reporting chains that have grown over time without documented justification.
- Assessing whether a team's velocity is limited by real work or by process surface area.

## When It Misleads

- Genuinely hard problems do not become faster just because the deadline is compressed; the work does not fit in less time simply because you announce it must.
- In domains where quality and correctness are invisible until failure (security, safety-critical systems, data integrity), compressing time directly trades defect rate for schedule, a poor bargain.
- In exploratory or research-phase work where the scope cannot be known in advance, aggressive deadline compression collapses the exploration itself.
- When slack is removed but the underlying constraints (third-party dependencies, regulatory approval, physical testing cycles) remain unchanged, the work still takes as long and now has no buffer for the inevitable delays.

## Common Misuse

Using Parkinson's Law as a management cudgel to justify arbitrary time compression without examining what the slack is actually funding. The heuristic is a diagnosis — "why does this task take so long?" — not a prescription that all tasks should be done in half the time. Equally common is treating it as a universal law when it most clearly applies to administrative tasks and meetings, where scope is genuinely elastic, and less clearly to technical or creative work where the problem size is fixed by nature, not by available hours.

## How Agents Use It

- **Sanity-gate**: when a plan or estimate includes comfortable time buffers or generous deadlines without concrete justification for the size, question whether the buffer will actually be consumed by the named work or by unnamed scope creep and process overhead. If no clear reason for the specific buffer exists, flag it as a Parkinson's risk.
- **Embedded**: in project-planning or scope-review lenses, as a checkpoint after the work has been estimated under soft deadline conditions — ask whether the estimate would change materially if the deadline were fixed and hard.
