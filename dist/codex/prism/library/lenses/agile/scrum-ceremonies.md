---
name: scrum-ceremonies
display_name: Scrum Ceremonies
class: lens
underlying_class: native
domain: agile
source: Ken Schwaber and Jeff Sutherland (Scrum Guide, 2020)
best_for:
  - Evaluating the health and effectiveness of Scrum rituals in a team
  - Diagnosing dysfunction in sprint execution and team synchronization
  - Auditing ceremony compliance and time-boxing adherence
one_liner: "Check that each sprint ritual is aligned with its intended purpose and executed efficiently."
---

# Scrum Ceremonies

## Overview

The five ceremonies of Scrum — Sprint Planning, Daily Standup, Sprint Review, Sprint Retrospective, and Backlog Refinement — are the structured moments where a team synchronizes intent, surfaces obstacles, and learns. This lens evaluates whether each ceremony is serving its intended purpose or has drifted into theater. Practitioners apply it when ceremonies feel rote, when teams complain about meeting overhead, or when sprint outcomes suggest the team is misaligned despite ritual attendance.

## Analytical Procedure

### Phase 1 — Define the Intended Purpose of Each Ceremony

1. **For each of the five ceremonies, write its canonical purpose in one sentence.** Use the definitions below as your baseline:
   - **Sprint Planning:** Commit to a bounded set of work for the sprint and agree on how to accomplish it.
   - **Daily Standup:** Synchronize daily progress, expose blockers, and re-plan if needed.
   - **Sprint Review:** Inspect the increment delivered and gather feedback from stakeholders.
   - **Sprint Retrospective:** Reflect on process, identify what worked and what didn't, and agree on one improvement to try next sprint.
   - **Backlog Refinement:** Ensure upcoming backlog items are clear, estimated, and ready for commitment.

2. **For each ceremony, record the actual duration, attendees, and cadence.** Measure from the last four sprints:
   - Who actually attends? (vs. who should attend)
   - How long does it run? (vs. time-boxed duration)
   - Does it happen at all? (vs. scheduled frequency)

3. **Observe one instance of each ceremony live, or review a recording.** Take notes on:
   - What question(s) the facilitator actually asked or tried to answer.
   - What decisions or commitments emerged.
   - What was left unresolved or deferred.
   - Whether the outcome matched the stated purpose.

### Phase 2 — Compare Observed to Intended

4. **For each ceremony, create a two-column table:**

| Intended Purpose | What Actually Happened |
|---|---|
| <canon purpose from Step 1> | <observed outcome from Step 3> |

5. **Mark each ceremony with one of three verdicts:**
   - **Aligned:** The ceremony accomplished its purpose; the team made decisions or gained clarity that matched the intent.
   - **Drifted:** The ceremony happened but produced output that doesn't match intent (e.g., standup became a status report instead of blocker identification).
   - **Absent:** The ceremony was skipped, severely compressed, or attendees were disengaged.

### Phase 3 — Identify the Root Cause of Drift or Absence

6. **For each ceremony that is Drifted or Absent, answer these questions:**
   - Is this a facilitator skill gap? (Does the person running it know what question to ask?)
   - Is this a team role confusion? (Do people understand why they are there?)
   - Is this a time-boxing failure? (Did the ceremony get squeezed out by upstream delays?)
   - Is this a stakeholder clarity gap? (Is the team unclear on who the audience is, e.g., in Review?)
   - Is this a technical blocker? (For standup: are blockers actually blockable by the team, or are they external dependencies the standup can't resolve?)

7. **For ceremonies that are Aligned, ask:** Is this sustainable? Would the team continue if the current facilitator left? Is the quality fragile (depends on one person) or robust (the team owns the ritual)?

### Phase 4 — Severity and Patterns

8. **Count the verdicts across all five ceremonies:**
   - How many Aligned, Drifted, Absent?
   - If more than one ceremony is Drifted or Absent, is there a common root cause (e.g., "ceremonies before 10 AM never happen" or "we skip retro when sprints are chaotic")?

## Evaluation Criteria

| Check | Pass |
|---|---|
| Canonical purpose written for all five ceremonies | Y/N |
| Actual attendance, duration, cadence measured for last 4 sprints | Y/N |
| At least one ceremony was observed live or recorded | Y/N |
| Intended vs. actual outcome was compared for each ceremony | Y/N |
| Each ceremony assigned a verdict (Aligned/Drifted/Absent) | Y/N |
| Root-cause questions answered for Drifted/Absent ceremonies | Y/N |
| Fragility assessment completed for Aligned ceremonies | Y/N |

## Red Flags

- All five ceremonies are marked "Aligned" but team members describe meetings as overhead or waste. The verdicts are wishful.
- A ceremony is marked "Aligned" but you cannot identify a single decision or artifact it produced. Attendance is not alignment.
- Daily Standup happens but the team ignores blockers that emerge ("we'll handle that offline"). The ceremony is not unblocking the actual work.
- Sprint Retrospective recommendations are never enacted in the following sprint; the team treats retro as cathartic but not binding.
- Backlog Refinement and Sprint Planning are conflated or happen back-to-back with no time separation, creating confusion about what was refined vs. what was committed.
- The facilitator cannot articulate why a ceremony exists or what the team should walk away with. This signals the ritual is cargo-cult.

## Output Format

```
## Scrum Ceremonies Audit

### Intended Purposes
- **Sprint Planning:** <one-sentence purpose>
- **Daily Standup:** <one-sentence purpose>
- **Sprint Review:** <one-sentence purpose>
- **Sprint Retrospective:** <one-sentence purpose>
- **Backlog Refinement:** <one-sentence purpose>

### Observed Metrics (last 4 sprints)
| Ceremony | Time-boxed | Actual duration | Attendees (target vs. actual) | Cadence | Notes |
|---|---|---|---|---|---|
| Sprint Planning | <T> min | <T> min | <X> vs <Y> | <frequency> | |
| Daily Standup | <T> min | <T> min | <X> vs <Y> | <frequency> | |
| Sprint Review | <T> min | <T> min | <X> vs <Y> | <frequency> | |
| Sprint Retrospective | <T> min | <T> min | <X> vs <Y> | <frequency> | |
| Backlog Refinement | <T> min | <T> min | <X> vs <Y> | <frequency> | |

### Ceremony Verdicts
| Ceremony | Verdict | Intended Outcome | Observed Outcome | Root Cause (if Drifted/Absent) |
|---|---|---|---|---|
| Sprint Planning | Aligned / Drifted / Absent | <...> | <...> | <...> |
| Daily Standup | Aligned / Drifted / Absent | <...> | <...> | <...> |
| Sprint Review | Aligned / Drifted / Absent | <...> | <...> | <...> |
| Sprint Retrospective | Aligned / Drifted / Absent | <...> | <...> | <...> |
| Backlog Refinement | Aligned / Drifted / Absent | <...> | <...> | <...> |

### Root-Cause Summary (Drifted/Absent only)
- Facilitator skill gap: [yes/no] — <detail>
- Role confusion: [yes/no] — <detail>
- Time-boxing failure: [yes/no] — <detail>
- Stakeholder clarity gap: [yes/no] — <detail>
- Technical blocker: [yes/no] — <detail>

### Fragility Assessment (Aligned ceremonies only)
- Ceremonies dependent on single facilitator: [list]
- Ceremonies robust to facilitator change: [list]

### Pattern Analysis
- Aligned ceremonies: <count/5>
- Drifted ceremonies: <count/5>
- Absent ceremonies: <count/5>
- Common root cause across multiple ceremonies: <if any>

### Confidence
<high | medium | low> — <justification based on observation depth, team size, sprint data available>
```
---
