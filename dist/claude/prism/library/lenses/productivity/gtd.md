---
name: gtd
display_name: Getting Things Done (GTD)
class: lens
underlying_class: native
domain: productivity
source: David Allen, Getting Things Done (2001)
best_for:
  - Auditing personal or team task systems for completeness and cognitive load
  - Diagnosing why work feels chaotic or why deadlines slip
  - Designing capture and clarification workflows
one_liner: "Getting Things Done — externalize and clarify all open loops to align execution and unload cognitive overhead."
---

# Getting Things Done (GTD)

## Overview

GTD is a workflow discipline that moves tasks and commitments from your head into an external, trusted system. The core insight is that the mind is poor at remembering *what* you committed to but excellent at remembering *where to find* that commitment. By externalizing everything, clarifying what each item means, and organizing by context and energy level, you free working memory for actual execution. Practitioners use GTD to recover focus when projects proliferate, when interruptions are constant, or when the gap between commitments and capacity feels unsustainable.

## Analytical Procedure

### Phase 1 — Collect Everything

1. **List all active projects, goals, and commitments.** Write anything that occupies mental RAM: work projects, home repairs, emails unanswered, ideas half-started, promises made. Do not filter yet. Use the following categories to ensure coverage:
   - Work projects (in-flight, blocked, waiting)
   - Personal projects (learning, home, health, relationships)
   - Administrative (taxes, licenses, records)
   - Someday/Maybe (things you want to do but not now)
   - Calendar commitments (deadlines, meetings, events)
   - Waiting-for (delegated work, approvals pending)

2. **For each item, write it in simple past-tense noun form.** Not "I need to call the dentist." Better: "Schedule dentist appointment." This forces clarity about what *done* looks like.

### Phase 2 — Clarify Each Item

3. **For each collected item, answer: What is the desired outcome?** Write it in one sentence. If you can't write it, you don't understand the commitment. Examples:
   - Bad: "Fix the bug."
   - Good: "Customers can upload CSV files without timeout errors."

4. **For each item, answer: What is the next physical action?** Not a goal or a phase — the very next concrete step. Examples:
   - Bad: "Finish the report."
   - Good: "Email the Q2 template to finance and ask for closing numbers."

5. **For items with no clear next action, ask:** Is this truly a commitment, or is it a vague wish? If it's a commitment, identify the next action. If it's a wish, move it to Someday/Maybe or delete it. If clarification requires input from someone else, the next action becomes "Ask X for clarification."

### Phase 3 — Organize by Context and Energy

6. **Assign each item to a context.** A context is a set of tools, location, or person required:
   - `@computer` — requires a terminal, IDE, or software
   - `@phone` — requires a call or Slack DM
   - `@home` — requires your home setup
   - `@errand` — requires travel or a store
   - `@meeting` — requires a group or specific person
   - `@energy-high` — requires full attention (design work, debugging)
   - `@energy-low` — can be done half-asleep (email triage, data entry)
   
   Some items belong in multiple contexts; list the primary one.

7. **Assign an energy or priority tag** if your context system doesn't separate by energy level:
   - `high-energy` — requires deep focus, creativity, or problem-solving
   - `low-energy` — routine, mechanical, or can be done while fatigued
   - `waiting` — blocked on external input; no action until condition met

### Phase 4 — Reflect (Weekly Review)

8. **Every 7 days, run a reflection cycle:** Review every item in your system (projects, next actions, waiting-for, calendar). Answer:
   - Did I complete any items? Mark done and remove.
   - Did any blocked items unblock? Move to active.
   - Did any new commitments enter the system since last review? Run them through Phases 1–3.
   - Are there projects with no next actions? Add one.
   - Is there anything I committed to that I no longer want? Delete it or move to Someday/Maybe.

9. **After the review, answer:** Does the system still feel trustworthy? If not, the system is leaking — there are uncaptured commitments. Revisit Phase 1.

### Phase 5 — Engage (Execute)

10. **When in a context, show only items for that context.** If you're `@computer`, do not see `@phone` items. Eliminate context switching.

11. **Within a context, pick the item that matches your current energy level.** If you're tired, pick `low-energy` items. If fresh, pick `high-energy` work.

12. **Do not pick a new item until the current one is truly done** (outcome achieved, next action completed, or explicitly moved to blocked/waiting).

## Evaluation Criteria

| Check | Pass |
|---|---|
| All active projects and commitments are captured (no mental items remain) | Y/N |
| Every item has a clarified desired outcome (one sentence, past-tense language) | Y/N |
| Every item has an identified next action (concrete, verb-based) | Y/N |
| Items are organized by context (@computer, @phone, @home, etc.) | Y/N |
| Energy/priority tags are present where context alone is insufficient | Y/N |
| Waiting-for and Someday/Maybe items are separated from active next actions | Y/N |
| Weekly review was completed in the past 7 days | Y/N |
| No item lacks a clear next action (no "think about this" items remain) | Y/N |

## Red Flags

- Items in the system lack next actions or outcomes. They are commitments without clarity — the system becomes a source of anxiety, not relief.
- The same item appears in multiple contexts but is tagged `waiting` or blocked in all of them. It should be in Someday/Maybe, not active.
- Calendar and task system are out of sync. Deadlines appear on the calendar but the task is not in the next-actions list.
- The system hasn't been reviewed in more than 10 days. Trust deteriorates rapidly; unmaintained systems become ignored systems.
- Items remain in the system for weeks with no progress and no blocking reason. Either the outcome is no longer desired (delete it) or the next action is too large (break it into smaller actions).
- Energy levels are ignored, and all items are treated as equal priority. This leads to task switching and low energy/high-demand mismatches.
- "Someday/Maybe" is overloaded or never reviewed. It becomes a graveyard for wishes, not a backlog.

## Output Format

```
## GTD Audit Report

### Phase 1 — Capture
- Total items collected: _
- Items by category:
  - Work projects: _
  - Personal projects: _
  - Administrative: _
  - Someday/Maybe: _
  - Waiting-for: _

### Phase 2 — Clarify
| Item | Desired Outcome | Next Action | Clear? |
|---|---|---|---|
| <...> | <...> | <...> | Y/N |

**Items lacking clarity:** _ (should be zero)

### Phase 3 — Organize
| Item | Context | Energy | Blocked? |
|---|---|---|---|
| <...> | @computer, @home | high-energy | N |

**Active next actions by context:**
- @computer: _
- @phone: _
- @home: _
- @errand: _
- @meeting: _
- (other): _

**Waiting-for items:** _
**Someday/Maybe items:** _

### Phase 4 — Reflect
- Last weekly review: <date>
- Days since last review: _
- Items completed since last review: _
- New items added since last review: _
- System trust rating: <high/medium/low>

### Phase 5 — Engage
- Execution mismatches detected: <describe context/energy misalignments>
- Recommended next actions: <e.g., "Break 'redesign checkout flow' into 3 smaller steps; add @computer tag to 'review budget spreadsheet'">

### Confidence
<high/medium/low> — <justification: e.g., "high — system fully captured, reviewed in the past 7 days, all items have clear outcomes and next actions"; or "low — items lack next actions and system has not been reviewed in 14 days">
```
