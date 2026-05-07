---
name: program-analysis
display_name: Program Analysis
class: lens
underlying_class: native
domain: architecture-physical
source: origin uncertain
best_for:
  - Auditing building layouts against functional requirements
  - Validating spatial adjacency decisions
  - Identifying program gaps or conflicts early
one_liner: "Check program composition by matching functional requirements against spatial adjacencies."
---

# Program Analysis

## Overview
Program Analysis breaks down a building's intended uses (functional requirements) and tests whether the spatial layout supports those uses efficiently. It maps requirements to zones, checks that adjacencies make operational sense, and measures area allocation against use intensity. Practitioners use this lens when evaluating a site plan, floor layout, or schematic design to catch misalignments before detailed design locks in costly mistakes.

## Analytical Procedure

### Phase 1 — Extract Requirements

1. **List all functional requirements for the building or floor.** Write each as a verb+noun pair tied to occupancy or activity type:
   - "Patient waiting and registration"
   - "Medication storage and dispensing"
   - "Emergency intake and triage"
   - "Staff break and shift change"
   Do not write "efficient workflow" or "good circulation." Write what actually happens.

2. **For each requirement, identify the user groups involved.** Name them (e.g., nurses, patients, visitors, maintenance staff). Separate groups often mean separate zones.

3. **For each requirement, estimate the area per unit.** Use standards (e.g., 100 SF per patient station, 50 SF per workstation, 15 SF per person for assembly). Write the source of the standard. If you have no standard, flag it and note what data you'd need.

4. **Calculate total area per requirement.** Multiply unit area by count. Sum all requirements to get total program area. Compare to the actual building/floor area. If actual is much smaller, the program is over-scoped; if much larger, there is slack space.

### Phase 2 — Map Adjacencies and Circulation

5. **For each pair of requirements, rate the adjacency need:**
   - **Critical** — the two activities share users or materials in real time (e.g., exam room and ultrasound).
   - **Important** — the two activities are sequential and frequent (e.g., waiting and check-in).
   - **Beneficial** — proximity saves time but is not essential (e.g., restroom near waiting area).
   - **Neutral** — no operational relationship.
   - **Incompatible** — should be distant or separated (e.g., noisy equipment and quiet reading room).
   Create a matrix with requirements as rows and columns; fill in the rating.

6. **Measure distances in the proposed layout.** For each Critical or Important adjacency, walk (or measure in plan) the distance between the two zones. Record actual distance and time at normal pace. Flag anything over 150 feet or 2 minutes as a layout failure unless the building type permits it (e.g., a hospital will have longer paths than a clinic).

7. **Trace the circulation path for a typical user flow.** Pick a common activity sequence (e.g., patient arrival → registration → waiting → exam → checkout). Walk or diagram the path on the plan. Count direction changes, barriers, and backtracking. More than 1 major backtrack is a red flag.

### Phase 3 — Evaluate Area Allocation

8. **For each requirement, compare allocated area to calculated need.** 
   - If actual < calculated by >15%, note the squeeze and flag which user group is affected.
   - If actual > calculated by >30%, flag the over-allocation unless it serves a secondary function.
   - Neutral or slack areas (corridors, mechanical, unassigned) should be 15–25% of total. If over 30%, there is wasted space.

9. **Check for area conflicts.** If two requirements are assigned overlapping or adjacent space (e.g., noisy break room next to a quiet office), note it as a design collision.

10. **Validate clear heights, setbacks, and structural constraints.** If a requirement has minimum headroom (e.g., manufacturing) or needs column-free spans, confirm the layout accommodates it. Record any constraint violations.

## Evaluation Criteria

| Check | Pass |
|---|---|
| All functional requirements identified and written as activities (not qualities) | Y/N |
| Area calculations tied to standards or explicit assumptions | Y/N |
| Total program area compared to actual building area with variance noted | Y/N |
| Adjacency matrix completed with Critical/Important/Beneficial/Neutral/Incompatible ratings | Y/N |
| At least 3 Critical or Important adjacencies measured with distance and time recorded | Y/N |
| One complete user flow traced and backtracking identified | Y/N |
| Area allocation reviewed against calculated needs with over/under noted | Y/N |
| Structural or code constraints checked and recorded | Y/N |

## Red Flags

- Requirements are stated as abstractions ("efficiency," "flexibility," "connectivity") rather than activities. You cannot audit a layout against vague goals.
- Adjacency matrix is all Neutral or no Incompatible ratings. Every building has at least one pair of incompatible activities; missing them means you haven't interrogated the program.
- Measured distances for Critical adjacencies exceed 200 feet with no justification. The layout is not supporting core operations.
- Slack space exceeds 30% of total area. Either the program is under-scoped or the building is oversized.
- Area allocations are guesses ("feels about right") rather than tied to standards or counts. Without a baseline, over/under-allocation is invisible.
- No user flows were traced. You cannot know if the layout works until someone walks it.

## Output Format

```
## Program Analysis Report

**Building/Floor:** <name>
**Total Area (program):** <area> SF | **Actual Area:** <area> SF | **Variance:** <+/-%>

### Phase 1 — Functional Requirements
| Requirement | User Groups | Unit Area | Qty | Total Area | Standard/Source |
|---|---|---|---|---|---|
| <activity> | <...> | <...> | <...> | <...> | <...> |

**Program Summary:** Total programmed area: ___ SF. Shortfall/surplus: ___.

### Phase 2 — Adjacency Matrix
| Req A | Req B | Rating | Measured Distance | Time | Violation? |
|---|---|---|---|---|---|
| <...> | <...> | Critical/Important/Beneficial/Neutral/Incompatible | <...> ft | <...> min | Y/N |

**Circulation Analysis:**
- Typical user flow: <sequence>
- Path length: ___ ft
- Direction changes: ___
- Backtracking instances: ___
- Verdict: <acceptable | strained | failed>

### Phase 3 — Area Allocation
| Requirement | Calculated Need | Actual Allocation | Variance | Flag |
|---|---|---|---|---|
| <...> | <...> SF | <...> SF | <...>% | Over/Under/OK |

**Slack/Unassigned:** ___ SF (___ % of total)

### Structural & Code Constraints
| Requirement | Constraint | Met? | Notes |
|---|---|---|---|
| <...> | <...> | Y/N | <...> |

### High-Priority Issues
1. <layout mismatch or adjacency failure with impact>
2. ...

### Confidence
<high/medium/low> — <justification: adequacy of standards used, completeness of user flow testing, clarity of program requirements>
```
