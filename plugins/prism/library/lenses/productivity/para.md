---
name: para
display_name: PARA Method (Forte)
class: lens
underlying_class: native
domain: productivity
source: Tiago Forte, Building a Second Brain (2022)
best_for:
  - Organizing personal or team knowledge into actionable and retrievable form
  - Deciding where to place new information to maximize future utility
  - Auditing an existing information system for coherence and saturation
one_liner: "Classify information into Projects, Areas, Resources, Archives to maximize actionability."
---

# PARA Method (Forte)

## Overview
PARA is a taxonomy for organizing any information system—digital or physical—around outcomes rather than topics. It sorts information into four buckets: Projects (time-bound deliverables with clear endpoints), Areas (ongoing domains of responsibility or interest), Resources (reference material indexed by topic), and Archives (completed or inactive projects and areas). Practitioners use PARA when an existing filing system has grown opaque or when a new system needs to be seeded with coherent structure. The discipline is ruthless boundary-drawing: information that feels related topically often belongs in different buckets because its *use pattern* differs.

## Analytical Procedure

### Phase 1 — Inventory Existing Information

1. **Collect all information artifacts.** Across your workspace (digital folders, notebooks, bookmarks, shared drives, email), list every distinct unit: folders, documents, projects, reference materials, decision logs, templates. Aim for 20–50 items for a personal system; scale accordingly for teams.

2. **Record the metadata for each artifact:**
   - Name or title
   - Current location (folder, app, physical shelf)
   - Last accessed date (if available)
   - Rough size (KB/MB for digital, page count for physical)
   - Original intent (why it was created or saved)

### Phase 2 — Classify by Use Pattern, Not Topic

For each artifact, answer these three questions in order. Do not skip forward.

3. **Question 1: Is this artifact tied to a specific deadline or completion date?**
   - YES → goes in **Projects**. Proceed to step 4.
   - NO → proceed to Question 2 (step 5).

4. **For Projects artifacts, record:**
   - Project name and endpoint (when does it finish or become inactive?)
   - Stakeholders or owner
   - Current status (active, paused, completed)
   - Decision: keep in Projects or archive now?

5. **Question 2: Is this artifact part of an ongoing responsibility or interest that has no end date?**
   - YES → goes in **Areas**. Proceed to step 6.
   - NO → proceed to Question 3 (step 7).

6. **For Areas artifacts, record:**
   - Area title (e.g., "Health & Fitness," "Client XYZ," "Product Strategy")
   - Metrics or signals of success (if any; optional for personal areas)
   - Review cycle (how often should this be revisited?)
   - Decision: is this a current area or should it be archived?

7. **Question 3: Is this artifact reference material—information you may need to look up but that does not drive an active outcome?**
   - YES → goes in **Resources**. Proceed to step 8.
   - NO → flag as orphan (step 10).

8. **For Resources artifacts, record:**
   - Primary topic or category
   - Subcategory or tag (if applicable)
   - Why it was saved (use case)
   - Searchability: Is the title clear? Can a colleague or future-you find it by keyword?

9. **Question 3 continued — if an artifact does not fit Projects, Areas, or Resources, move it immediately to Archives.** Do not delay. Archival is not deletion; it is de-prioritization. Record the reason (completed, obsolete, seasonal, on-hold).

### Phase 3 — Audit Structure and Density

10. **Measure the distribution.**
    - Count artifacts in each bucket.
    - Expected rough distribution for a healthy system: Projects 10–20%, Areas 20–30%, Resources 40–50%, Archives 20–30%.
    - If Projects exceed 30%, the system is overloaded with concurrent outcomes.
    - If Areas exceed 40%, core responsibilities are unclear or boundaries are porous.
    - If Resources are sparse (<30%), the system is not capturing reference material; utility will decay.

11. **Audit naming consistency within Resources.** Pick 10 random Resources artifacts. Can you predict where each one is filed by reading its name? Can you guess the search query that would find it? If no to either, rename for discoverability.

12. **Audit Projects for staleness.** Identify any project marked "active" that has not been touched in 30+ days (or your team's sprint cycle). Review it: is it truly active or should it be paused or archived? Decision must be explicit.

13. **Audit Areas for drift.** For each current Area, ask: "Do I allocate time to this this month?" If no, move it to Archives pending seasonal re-activation. If yes but the file is empty or outdated, refresh it with a current summary.

## Evaluation Criteria

| Check | Pass |
|---|---|
| All artifacts from inventory were classified (no orphans left unresolved) | Y/N |
| Each Project has a clear endpoint or completion date | Y/N |
| Each Area has a name that reflects an ongoing responsibility, not a topic | Y/N |
| Resources are searchable by title (no vague names like "Misc" or "Stuff") | Y/N |
| Archive reason is recorded for each archived item | Y/N |
| Distribution percentages fall within expected ranges (or deviation is intentional and justified) | Y/N |
| Projects are reviewed at least weekly; areas at least monthly | Y/N |

## Red Flags

- All artifacts are scattered across Projects and Resources with almost no Areas. This suggests either the system is task-focused with no ongoing maintenance, or ongoing responsibilities are not being tracked.
- Resources folder is empty or minimal. The system is capture-poor; useful reference material is being discarded or lost in time-bound projects.
- Archives contain artifacts archived >6 months ago that are never revisited. Either archival is a graveyard and should be culled, or archived projects/areas should be returned to active status seasonally.
- A single artifact appears in multiple buckets (duplicated). This is normal during transition, but persistent duplication suggests unclear ownership.
- Projects list includes items with no deadline and no owner. These are not projects; they are ideas or areas masquerading as outcomes.
- Resources lack consistent naming or tagging. A colleague cannot find or retrieve material; the system has low utility for collaboration or knowledge transfer.

## Output Format

```
## PARA Audit

**System name/owner:**
<name>

**Audit date:**
<date>

### Inventory Summary
- Total artifacts: _
- Projects: _ (%)
- Areas: _ (%)
- Resources: _ (%)
- Archives: _ (%)

### Phase 1 — Classification
| Artifact | Classification | Endpoint/Scope | Decision |
|---|---|---|---|
| <...> | Projects / Areas / Resources / Archives | <...> | Keep / Archive / Rename |

### Phase 2 — Distribution Assessment
Expected: Projects 10–20%, Areas 20–30%, Resources 40–50%, Archives 20–30%
Actual: Projects _%  Areas _%  Resources _%  Archives _%
Assessment: <within range / over / under; justification>

### Phase 3 — Structural Issues Found
- Resources naming audit: <pass / fail; example fixes>
- Stale projects (no activity >30 days): <list or none>
- Empty or drifted areas: <list or none>
- Duplicate artifacts: <count or none>
- Orphaned items (unclassified): <count or none>

### Remediation Actions
1. <action> — Owner: <person> — Due: <date>
2. ...

### Maintenance Plan
- Projects review cycle: <weekly / bi-weekly / other>
- Areas review cycle: <monthly / quarterly / other>
- Resources grooming: <monthly / quarterly / annual>
- Archive review: <quarterly / annual>

### Confidence
<high | medium | low> — <justification: Does the system now have clear, enforceable boundaries? Are use patterns and storage locations aligned?>
```
