---
name: okrs
display_name: OKRs (Doerr)
class: lens
underlying_class: native
domain: okr
source: John Doerr, "Measure What Matters" (2018); adapted from Intel (Grove) and Google
best_for:
  - Translating strategic intent into measurable, bounded outcomes
  - Aligning teams across an organization toward shared results
  - Decoupling effort from results and surfacing misalignment early
one_liner: "Convert intent into measurable outcomes via an objective plus three to five key results."
---

# OKRs (Doerr)

## Overview
OKRs separate *what you want to achieve* (Objective) from *how you'll know you achieved it* (Key Results). An Objective is qualitative and inspirational; Key Results are quantitative and time-bound. Teams use OKRs to translate strategy into executable commitments and to surface misalignment—when a team's KRs don't ladder up to organizational OKRs, the gap is visible and discussable. Practitioners reach for OKRs when they need to move beyond task lists and historical planning cadences and instead make explicit what success actually looks like.

## Analytical Procedure

### Phase 1 — Articulate the Objective

1. **Write the strategic intent in 3–7 words.** Use active language. It should be memorable and motivating but not vague. Test: could someone unfamiliar with your business repeat it back to you accurately after hearing it once?
   - Bad: "Improve our platform" (too generic)
   - Good: "Become the fastest checkout on the web" (concrete and testable in spirit)

2. **Answer: Why does this objective matter right now?** Write 1–2 sentences. What changes if we achieve it? What breaks if we don't? This is the constraint that justifies the goal—it anchors the team to reality, not ambition theater.

3. **Identify the owner.** One person or small team is accountable for driving progress. Name them.

### Phase 2 — Define Key Results

4. **For each Objective, write 3–5 Key Results.** Each KR must satisfy all four criteria below. If a candidate KR fails any, it is not a Key Result—it is a task or metric to track separately.

   **Criterion A — Measurable:** The KR has a unit (count, percentage, dollar, rate, score). You must be able to report a number at quarter's end. "Improve morale" is not measurable; "increase eNPS score from 32 to 50" is.

   **Criterion B — Achievable but ambitious:** The team should believe there is a 60–70% chance of hitting the target if everything goes right and they execute well. Not a guarantee, not a moonshot.

   **Criterion C — Outcome, not activity:** The KR describes a result, not the effort. "Conduct 20 user interviews" is activity. "Reduce support ticket resolution time from 48h to 24h" is outcome. The team chooses the path; you specify the destination.

   **Criterion D — Directly influenced by the team:** The team's work materially affects the KR. If success depends entirely on another team, supplier, or market, it is not a KR for this team.

5. **For each KR, define the start state and the target.** Example: "Reduce checkout abandonment rate from 18% to <12%." If the KR is a new metric with no baseline, run a 1–2 week measurement pilot to establish it, then commit.

6. **Sequence the KRs in priority order.** The first KR is the must-have. If the team runs out of time or resources, which KRs get dropped? Order reflects that.

### Phase 3 — Ladder and Validate

7. **Map each team's OKRs to the Objective(s) they support.** Draw a simple tree: Organization OKR at the top, then Team 1 OKRs, Team 2 OKRs, etc., as branches. Gaps or tangents in the tree are failures—they mean the team is working on something unstratgic or that a strategic gap is unowned.

8. **Ask: "If every team hits their OKRs, do we achieve the organizational Objective?"** If the answer is "probably not" or "maybe," the OKRs are misaligned. Go back to Phase 2 and rewrite.

9. **Check for resource conflicts.** If two teams' OKRs require the same scarce resource (engineer, designer, partner), call it out now. Decide: rewrite one OKR, or explicitly accept the resource conflict as a known risk.

10. **Finalize and publish.** Write the OKRs in a shared document (wiki, spreadsheet, slides—pick one place). Include the start/target for each KR, the owner, and the rationale (from Phase 1, step 2).

## Evaluation Criteria

| Check | Pass |
|---|---|
| Each Objective is ≤7 words and uses active language | Y/N |
| Rationale for each Objective explains why it matters now | Y/N |
| Each team/person has exactly one owner per Objective | Y/N |
| Each KR satisfies all four criteria: Measurable, Ambitious, Outcome, Influenced | Y/N |
| Each KR has a baseline (start state) and a target | Y/N |
| Team OKRs ladder to Organization OKRs (tree is connected) | Y/N |
| No resource conflicts are unacknowledged | Y/N |
| At least one KR per Objective is outcome-based, not activity-based | Y/N |

## Red Flags

- An Objective is vague ("grow the business") or longer than 7 words. It cannot be repeated accurately or remembered.
- A KR is missing a unit or a target number. "Improve X" or "achieve more Y" is not a KR.
- A KR is actually a task ("hire 3 engineers," "launch feature X"). These are activities, not outcomes. Rewrite as the outcome: "reduce incident MTTR to <2h."
- A team's OKRs have no visible connection to the organization's Objective. Either the team is working on legacy debt (fine, but call it out) or the alignment is broken.
- The KR target is clearly unachievable (100% conversion rate) or trivial (99% uptime when you're already at 99.9%). Ambition is 60–70%, not fantasy or coast.
- Multiple teams own the same OKR or the owner is "everyone." Accountability dissolves when ownership is diffuse.
- No baseline is given ("improve latency" with no start point). You cannot measure progress if you do not know where you started.

## Output Format

```
## OKR Assessment

**Organization Objective:**
<Objective statement>

**Rationale:**
<1–2 sentences: Why now, what changes if achieved>

**Owner:**
<Name or team>

### Key Results

| Rank | Key Result | Start | Target | Measurable? | Outcome? | Achievable? | Influenced? |
|---|---|---|---|---|---|---|---|
| 1 | <KR statement> | <value> | <value> | Y/N | Y/N | Y/N | Y/N |
| 2 | ... | | | | | | |

### Alignment Check

**Organizational hierarchy:**
- Org Objective: <...>
  - Team A, Objective <...> (ladders via KR #_)
  - Team B, Objective <...> (ladders via KR #_)
  - Unowned gap: <...>

### Resource Conflicts
<List any shared resources under contention, or "None identified.">

### Validation Questions
- If all team OKRs are achieved, does the Organization Objective succeed? <Yes/No/Probably>
- Is any KR missing a baseline? <Yes/No>
- Is any KR actually a task? <Yes/No>

### Confidence
<high | medium | low> — <justification based on completeness of ladder, clarity of KRs, and realistic baseline/target pairs>
```
