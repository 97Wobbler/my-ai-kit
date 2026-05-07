---
name: Eisenhower Matrix (Urgent/Important Matrix)
domain: general
source: Attributed to Dwight D. Eisenhower; popularized by Stephen Covey (The 7 Habits of Highly Effective People, 1989)
underlying_class: frame
best_for: Triaging a list of candidate actions or issues when you can't do everything and must justify what you drop
one_liner: "Urgent/important 2x2 that sorts backlog or recommendations into Do / Schedule / Delegate / Eliminate."
---

# Eisenhower Matrix

## Overview
A 2×2 that sorts actions or issues by urgency (time pressure) and importance (alignment with goals/impact). The usefulness is not the quadrants themselves — it's forcing explicit classification, which exposes the common failure mode of treating urgent items as automatically important. Practitioners use it whenever a backlog, triage list, or recommendation set must be ruthlessly narrowed.

## Analytical Procedure

1. **Inventory every candidate action/issue.** Write each as a single line starting with a verb ("Fix X", "Review Y", "Negotiate Z"). No compound items — split "fix X and review Y" into two entries.

2. **Define the goal explicitly.** Importance is meaningless without a reference goal. Write one sentence: "The goal these actions serve is _______." Everything is scored against this, not against some implicit hierarchy.

3. **Score each item on importance (independent of urgency):**
   - **High**: directly advances the stated goal OR prevents a regression that would block the goal
   - **Medium**: supports the goal indirectly (enables something that supports it)
   - **Low**: does not clearly connect to the goal
   If you can't write the connection in one sentence, it's Low.

4. **Score each item on urgency (independent of importance):**
   - **High**: has a hard deadline within the next 7 days OR delay causes compounding damage (data loss, missed window, user-visible breakage)
   - **Medium**: has a soft deadline or degrades quality if delayed more than 1-2 sprints
   - **Low**: no deadline; delay has no visible effect

5. **Place each item in the matrix:**
   - **Q1 (Urgent + Important): Do.** These execute immediately. If Q1 is crowded, something has gone wrong upstream — note it.
   - **Q2 (Not Urgent + Important): Schedule.** These are the real work. If Q2 is empty, you are only reacting, not building.
   - **Q3 (Urgent + Not Important): Delegate or decline.** These steal attention from Q2. For each, name who can handle it or why it can be declined.
   - **Q4 (Not Urgent + Not Important): Eliminate.** Drop these without guilt. If you can't, interrogate why they're still on the list.

6. **Sanity-check the distribution.** Healthy distributions usually have Q2 as the largest quadrant. If Q1 or Q3 dominates, you're in firefighting mode and should flag that as a finding, not just as an action list.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Every item is scored on both axes independently | Y/N |
| Each "High importance" item has a one-sentence connection to the stated goal | Y/N |
| Q1 has at most 20% of total items | Y/N |
| Q2 has at least 40% of total items | Y/N |
| Every Q3 item has a delegation target or decline reason | Y/N |
| Every Q4 item has been eliminated from the plan | Y/N |

## Red Flags

- Everything lands in Q1. This is urgency capture — importance is being driven by whoever shouts loudest.
- Q2 is empty. You are purely reactive. The work you care about is not getting done.
- Items are scored on both axes at the same time (e.g., "this is urgent AND important because..."). The independence of the axes is the whole point.
- Stated goal is vague ("improve the product"). Every item will score High because nothing is excluded.
- Delegation targets are missing for Q3. The matrix becomes a way to justify doing Q3 yourself anyway.
- Same items show up in Q1 for multiple consecutive triages. Chronic urgency is a structural problem, not a to-do list problem.

## Output Format

```
## Eisenhower Matrix Assessment

**Goal this assessment serves:** <one sentence>

### Q1 — Do (Urgent + Important, n=_)
- <item> — owner: <name> — deadline: <date>
- ...

### Q2 — Schedule (Important, not Urgent, n=_)
- <item> — owner: <name> — target window: <sprint/date>
- ...

### Q3 — Delegate or Decline (Urgent, not Important, n=_)
- <item> — delegate to: <name> OR decline because: <reason>
- ...

### Q4 — Eliminate (n=_)
- <item> — why it was on the list: <reason, for learning>
- ...

### Distribution Health
- Q1: _% | Q2: _% | Q3: _% | Q4: _%
- Pattern: <balanced | firefighting | drift | reactive>
- Structural concern: <one sentence, if any>

### Confidence
<high/medium/low> — <justification>
```
