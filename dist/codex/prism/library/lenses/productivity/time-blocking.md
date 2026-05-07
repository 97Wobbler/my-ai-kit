---
name: time-blocking
display_name: Time Blocking
class: lens
underlying_class: native
domain: productivity
source: origin uncertain; popularized by Cal Newport (Deep Work) and time management practitioners
best_for:
  - Preventing context-switch tax and fragmentation
  - Aligning calendar to priorities, not just reactivity
  - Validating whether a schedule actually protects focus work
one_liner: "Intentional calendar-based scheduling to prevent time fragmentation."
---

# Time Blocking

## Overview

Time blocking allocates contiguous calendar slots to specific activities or outcome categories before the day begins, enforcing that time is committed rather than reactive. The discipline is the *pre-commitment* — most people build a to-do list and let the calendar fill reactively around it. Practitioners use time blocking when deep focus is required, when switching between task types is expensive, or when they suspect their calendar is driven by other people's urgency rather than their own priorities.

## Analytical Procedure

### Phase 1 — Audit Current Schedule

1. **Export your actual calendar for the past two weeks.** Include all events: meetings, work sessions, breaks, personal time. Export as a flat list with start time, end time, title, and category (meeting, focus work, admin, reactive).

2. **Measure fragmentation.** For each day, count the number of distinct time blocks (contiguous stretches without a context switch). Calculate the average and note the days with the most and fewest fragments. A typical reactive calendar has 8–15 fragments per day; a blocked calendar has 3–5.

3. **Classify each block by origin:**
   - **Imposed** — scheduled by someone else (meetings, standup, all-hands)
   - **Reactive** — unscheduled time you filled reactively (Slack, email, unplanned urgent work)
   - **Planned** — time you assigned to a specific project or outcome before the day started
   - **Admin** — overhead: context-switch recovery, hygiene, commute, meals
   Write down the total hours in each category. Most reactive calendars are 40–50% imposed, 30–40% reactive, 10–20% planned, and 10% admin.

4. **Identify your highest-value work.** Look at the past two weeks and list the 3–5 outcomes that moved your primary responsibility forward. For each, estimate the actual contiguous time spent on it (not context-fragmented time). Note if that time was in the morning, afternoon, or spread across the day.

### Phase 2 — Design Blocked Schedule

5. **Set a weekly time budget.** Decide how many hours per week belong to each of: deep focus on primary work, meetings, reactive work (email/Slack/interrupts), and admin. Be honest about constraints (existing recurring meetings, commute). A sustainable blocked schedule typically allocates 15–20 hours/week to focus work in a 40-hour week.

6. **Block your focus time first.** Choose 2–4 contiguous slots per week (e.g., Tu–Th mornings, 9am–12pm). Mark these on your calendar immediately as "Focus" or project-specific blocks. Make these sacred — don't schedule meetings into them.

7. **Block meeting/reactive time.** Consolidate meetings into 1–2 days per week or specific afternoons. Create a "Slack window" (e.g., 11am–12pm and 3pm–4pm) for synchronous communication. Everything else is assumed to be async. If you can't consolidate, note which meetings are truly fixed and which are negotiable.

8. **Define handoff points.** Specify when you *exit* focus time and check messages (not mid-block). Specify when meetings start and end, and what happens in the 5 minutes before the next block (transition, not lingering in the previous context).

### Phase 3 — Validation Against Reality

9. **Simulate the blocked schedule against your real constraints.** For one week, live with the proposed blocks without changing them reactively. Record:
   - How many focus blocks were interrupted (by you or others)?
   - How many times you context-switched within a focus block?
   - How many urgent interrupts were truly urgent, and how many were "could have waited until the next Slack window"?
   - How much of the reactive/meeting time was actually used?

10. **Calculate adherence.** Blocked time is successful if you protect ≥80% of focus blocks without interruption and ≥80% of context-switches happen at the planned handoff points, not in the middle of work.

11. **Identify friction.** If adherence is low, interrogate the gaps:
    - Are meetings being added despite the block? If yes, who is adding them and why? Can you reset expectations?
    - Are you interrupting yourself? If yes, what trigger (notification, thought, anxiety)? Can you address the trigger, not just the symptom?
    - Is the block size wrong? (Too long and you lose focus; too short and you never reach flow.)
    - Is reactive work underbudgeted? If every Slack window is overflowing, you need more reactive time or to reduce incoming volume.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Calendar audit covers ≥2 weeks of actual data | Y/N |
| Current schedule fragmentation is measured (blocks/day) | Y/N |
| Each calendar block is classified by origin (Imposed/Reactive/Planned/Admin) | Y/N |
| Highest-value outcomes from the period are identified | Y/N |
| Proposed blocked schedule accounts for all imposed commitments | Y/N |
| Focus blocks are ≥90 min contiguous | Y/N |
| Reactive time windows are defined with specific hours (not "throughout the day") | Y/N |
| Simulation ran for ≥1 week with adherence measured | Y/N |
| Adherence ≥80% or friction points are identified | Y/N |

## Red Flags

- All focus blocks are early morning, but your peak energy is afternoon. The schedule doesn't match your chronotype.
- Focus blocks exist on paper but you answer Slack during them. You haven't actually changed behavior — you've just created a false record.
- Reactive time is "throughout the day whenever possible" rather than fixed windows. This defeats the purpose; you're still reactive.
- The blocked schedule doesn't account for your largest time-sink (e.g., you blocked 20 hrs/week for focus but have 18 hrs of imposed meetings). The math is broken.
- You block time but don't measure what actually happened. Without a simulation, you're planning in fantasy.
- Friction analysis is absent. If blocks are being broken, the fix is not "be more disciplined"; it's to identify *why* and address the root (bad boundaries, underbudgeted reactive time, unrealistic block length).

## Output Format

```
## Time Blocking Assessment

### Audit Results
- **Calendar period:** <dates>
- **Average fragments per day (current):** <number>
- **Time distribution (hours/week):**
  - Imposed: <hours> (<percent>)
  - Reactive: <hours> (<percent>)
  - Planned: <hours> (<percent>)
  - Admin: <hours> (<percent>)
- **Highest-value outcomes (past 2 weeks):**
  1. <outcome — contiguous time spent>
  2. <outcome — contiguous time spent>
  3. <outcome — contiguous time spent>

### Blocked Schedule Design
- **Focus blocks:** <e.g., Tu–Th 9am–12pm, M 8am–11am> (total: <hours/week>)
- **Meeting consolidation:** <e.g., Wed afternoon all-hands, Thu 2–4pm for 1:1s>
- **Reactive windows:** <e.g., 11am–12pm, 3–4pm daily>
- **Handoff points:** <e.g., end of focus block: 5 min buffer, then check messages at window time>

### Simulation Results (1 week)
- **Focus blocks protected (%):** <percent without mid-block interruption>
- **Planned context-switches (%):** <percent that happened at handoff points, not mid-block>
- **Truly urgent interrupts:** <count and examples>
- **Reactive window utilization:** <percent of allocated time used>

### Friction Analysis
| Barrier | Frequency | Root cause | Mitigation |
|---|---|---|---|
| <e.g., Slack interrupts during focus> | <count> | <e.g., notifications on, no norms set> | <e.g., mute notifications, comms window only> |

### Adherence Verdict
- **Overall:** <Sustained / Needs adjustment / Blocked schedule not viable>
- **Confidence:** <high/medium/low> — <e.g., protected focus time, but reactive time consistently overflowed; recommend expanding reactive budget and re-running simulation before declaring success>
```
