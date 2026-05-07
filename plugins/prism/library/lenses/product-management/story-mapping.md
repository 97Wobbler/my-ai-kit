---
name: story-mapping
display_name: Story Mapping
class: lens
underlying_class: native
domain: product-management
source: Jeff Patton, "User Story Mapping: Discover the Whole Story, Build the Right Product" (2014)
best_for:
  - Sequencing product work by user journey and delivery priority
  - Identifying gaps and overlaps in feature coverage
  - Communicating scope and release boundaries to stakeholders
one_liner: "Visualize user journey on a priority grid to plan releases."
---

# Story Mapping

## Overview
Story Mapping arranges user stories on a two-dimensional grid: horizontally by the order they occur in a user's journey (the narrative arc), vertically by priority and depth. Instead of a flat backlog, you get a visual map that shows *which* user activities are covered, *when* they happen, *how complete* that coverage is, and where delivery boundaries fall. Practitioners use this when building a new product or feature area and need to plan what ships together and what can wait — it forces you to see coverage holes that a linear backlog obscures.

## Analytical Procedure

### Phase 1 — Establish the User Journey

1. **Identify the user role.** Name the primary user persona this map is for (e.g., "first-time app user," "paying subscriber," "support agent"). Write it as a single noun phrase.

2. **List the major activities, in chronological order.** These are the high-level user goals or milestones, not individual tasks. For a checkout flow: "Browse products" → "Add to cart" → "Enter shipping" → "Pay" → "Confirm order." Write 5–12 activities. If you have more than 12, you're too granular; if fewer than 5, you're too broad.

3. **For each activity, generate the user stories that support it.** These are the detailed capabilities the user needs. Use the format: "As a [role], I want to [action], so that [outcome]." Write 3–8 stories per activity. If an activity has no stories yet, mark it "not yet mapped" — this is a signal that coverage is incomplete.

4. **Verify the sequence.** Walk through the journey with a real user or stakeholder. Ask: "What would you do next?" If the sequence doesn't match their mental model, adjust. The horizontal axis must reflect actual user behavior, not system logic.

### Phase 2 — Layer by Priority and Depth

5. **Draw the priority spine.** On the vertical axis, designate the topmost row as "Release 1 (MVP)" — the minimum set of stories required for the product to be viable for that user. Every other row below is "Release 2," "Release 3," etc., or "Nice to have / Future."

6. **Sort stories vertically under each activity.** Place stories that are essential to completing the activity above; place refinements, edge cases, and "nice-to-have" variants below. A story at the top-left (first activity, first row) is the highest priority overall.

7. **Identify acceptance criteria for each story.** Write 2–4 concrete criteria (Given/When/Then format or plain language). Mark any criteria that are unclear or dependent on other stories — these become risk flags.

### Phase 3 — Find Gaps and Overlaps

8. **Scan each activity column for coverage.** Are there stories in every row, or are some rows thin? Thin rows (few stories in a given release) suggest incomplete thinking about scope or unequal distribution of work.

9. **Check for orphaned stories.** If a story appears in the map but doesn't support any activity, or if an activity has no stories, flag it. This is usually a sign of scope creep or a missing user need.

10. **Test the release boundaries.** For each proposed release, ask: "Can a user complete their core journey with just these stories?" Trace a user path through Release 1. If critical stories are missing, adjust the boundary or acknowledge the gap as a known risk.

### Phase 4 — Translate to Execution

11. **Define a delivery sequence.** Walk the map left-to-right, top-to-bottom. This gives your natural task order: complete all Release 1 stories for the first activity, then the second, then move to Release 2. Call this the "walking skeleton" — it keeps the product always in a shippable state.

12. **Identify dependencies and blockers.** For each story, note if it depends on stories in earlier activities or other teams. Draw arrows or mark these explicitly. Unblocked stories can start immediately; blocked stories need a prerequisite.

13. **Estimate scope (optional but recommended).** Assign relative story points or t-shirt sizes to each story. Sum the stories in each release row to forecast effort per release.

## Evaluation Criteria

| Check | Pass |
|---|---|
| User role is named explicitly | Y/N |
| 5–12 major activities are identified and ordered chronologically | Y/N |
| Each activity has 3–8 supporting stories in story format | Y/N |
| At least one complete user journey can be traced through Release 1 | Y/N |
| Acceptance criteria are present for core stories | Y/N |
| Release boundaries are marked and all boundary decisions are justified | Y/N |
| No stories are orphaned; every story supports at least one activity | Y/N |
| Dependencies between stories are marked | Y/N |

## Red Flags

- All stories are in the top row (MVP). This usually means the map is too coarse, or every feature was declared essential without prioritization.
- Activities have no stories, only placeholder text. The journey is outlined but not mapped; the product definition is still vague.
- Stories do not follow the "As a / I want / so that" format or lack acceptance criteria. Without concrete criteria, stories remain open to misinterpretation.
- More than 15 activities for a single release. The scope is too broad; either split into multiple releases or collapse activities that are variants of the same user goal.
- Release 1 has >20 stories or >50 story points. The MVP is likely unsalvageable; trim ruthlessly or split into Phase 1a and Phase 1b.
- The map does not reflect actual user behavior (e.g., activities are out of sequence with how users actually work). Go back to Phase 1 and re-interview.
- Orphaned stories outnumber mapped stories. The map is not functioning as a coherence tool; revisit the activities.

## Output Format

```
## Story Map: [User Role]

### User Journey (Activities)
1. [Activity 1] → 2. [Activity 2] → 3. [Activity 3] → ...

### Story Map Grid

| Activity | Release 1 (MVP) | Release 2 | Release 3 | Future |
|---|---|---|---|---|
| **[Activity 1]** | [Story] / [Acceptance] | [Story] | [Story] | [Story] |
| | [Story] / [Acceptance] | | | |
| **[Activity 2]** | [Story] / [Acceptance] | [Story] | | |
| | [Story] / [Acceptance] | | | |

### Coverage Analysis
- Missing or thin rows: <list which releases lack complete coverage>
- Orphaned stories: <any stories not supporting an activity?>
- Dependencies: <critical blockers between stories>

### Release Boundaries & Justification
- **Release 1 MVP:** <description of what user can accomplish with Release 1 stories only>
- **Release 2 rationale:** <what capability is added; why not in Release 1?>
- **Release 3 / Future:** <aspirational; what constraints prevent earlier delivery?>

### Delivery Sequence
Walking skeleton (left-to-right, top-to-bottom):
1. [Activity 1, Release 1 stories in priority order]
2. [Activity 2, Release 1 stories]
3. [Activity 1, Release 2 stories]
...

### Scope & Effort (if estimated)
- Release 1: [N story points / effort estimate]
- Release 2: [N story points / effort estimate]
- Release 3+: [N story points / effort estimate]

### Confidence
<high/medium/low> — <justification. For example: "high — user interviews confirmed the activity sequence, all core stories have acceptance criteria, and release boundaries are agreed by product and engineering. Low — Release 2 stories are still rough; we may discover dependencies during Release 1 execution.">
```
---
