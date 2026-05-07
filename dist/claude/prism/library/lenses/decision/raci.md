---
name: raci
display_name: RACI Matrix
class: lens
underlying_class: native
domain: decision
source: Origin uncertain; widely attributed to Galloway but documentation predates formal attribution
best_for:
  - Clarifying decision authority and participation in a specific decision or project
  - Preventing bottlenecks caused by unclear ownership
  - Reducing rework due to miscommunication about who decides vs. who advises
one_liner: "Assign Responsible / Accountable / Consulted / Informed per task to remove role ambiguity and delay."
---

# RACI Matrix

## Overview
RACI is a role-mapping framework that clarifies four distinct participation modes for any decision, project, or process: who is **Responsible** (does the work), who is **Accountable** (owns the outcome), who must be **Consulted** (provides input before action), and who must be **Informed** (notified after decision). Practitioners use it when stakeholder confusion causes rework, delayed decisions, or duplicated effort. The discipline is precision — vague assignments like "stakeholder" or "involved party" produce RACI matrices that are useless in practice.

## Analytical Procedure

### Phase 1 — Scope the decision or process

1. **Write the decision or process in one sentence.** Examples: "Hiring a senior engineer," "Choosing the database for the analytics service," "Setting quarterly OKRs." Be specific enough that someone outside the team understands what is being decided.

2. **List all roles, teams, or people who might have a stake in this decision.** Do not filter yet — include everyone who has expressed an opinion, who will be affected, or who controls a resource that the decision touches.

3. **For each role, ask: "Does this role have legal, technical, budget, or timeline power over this decision?"** Mark roles that answer yes. These are candidates for Accountable or Responsible.

### Phase 2 — Map each role to exactly one RACI category

4. **Assign Accountable (A).** Exactly one role per decision. This role owns the outcome; if the decision fails or is wrong, this role answers for it. Ask: "Who would be fired if this goes wrong?" or "Who can overrule everyone else?" There can be only one.
   - If no one is accountable, the decision will drift and be remade later. Assign one now.
   - If multiple people claim accountability, the decision is already broken. Resolve this before proceeding.

5. **Assign Responsible (R).** The person(s) who do the actual work — research, analysis, drafting, execution. A single decision can have multiple Responsible roles (e.g., engineering and design both responsible for a UX feature). Ask: "Who will spend the most time on this after the decision is made?"
   - Responsible reports to Accountable. If they conflict during execution, Accountable breaks the tie.

6. **Assign Consulted (C).** Roles whose input is *required* before the decision is locked. Not "nice to have" — genuine dependencies. Typical examples: legal (for regulatory risk), security (for breach risk), finance (for budget trade-offs), end users (for usability). Ask: "What knowledge or veto would cause this decision to be remade if we discovered it only afterward?"
   - Consulted roles are interviewed *before* the decision. Consulting them *after* is not RACI — that is miscommunication.

7. **Assign Informed (I).** Roles who learn about the decision *after* it is made. They need to know the outcome to do their job, but not the rationale or reasoning. Examples: marketing learning about a feature ship date, ops learning about infrastructure changes, customers learning about a deprecation. Ask: "Who needs to know this happened, but not why or how we decided?"

8. **For each role not yet assigned, make an explicit choice:** Either it has no RACI role (it is not a stakeholder — drop it from the matrix), or reassign it to one of the four categories above. Every role in your original list must map to exactly one of {A, R, C, I, or "no role"}.

### Phase 3 — Validate the matrix

9. **Check for isolated Accountable.** If the Accountable role is not close to the Responsible roles (in hierarchy, location, or communication cadence), the decision will slip into ambiguity. If Accountable is remote from Responsible, clarify the escalation path.

10. **Count Consulted roles.** If there are more than 4–5 Consulted roles, the decision velocity will collapse — you will spend more time in consultation loops than in execution. If you have >5, ask: "Which of these truly have veto power?" and downgrade others to Informed.

11. **Verify no Responsible role reports to itself.** A role should not be both Responsible and Accountable for the same decision (creates accountability loss — "it was the system" rather than owning a choice). Exception: in very small teams, this may be unavoidable; if so, flag it explicitly.

12. **Present the matrix to all assigned roles.** Do not publish a RACI matrix unilaterally. Ask each role: "Is this how you understood your role?" and "Can you commit to this?" Misalignments discovered here are cheap fixes. Misalignments discovered during execution are expensive.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Decision/process is scoped in one clear sentence | Y/N |
| Exactly one Accountable role assigned | Y/N |
| All Responsible roles identified (can be multiple) | Y/N |
| Consulted roles have genuine veto or required input (≤5) | Y/N |
| Informed roles are notified after decision (not before) | Y/N |
| Every role in the original list is mapped to A/R/C/I or dropped | Y/N |
| All assigned roles reviewed and agreed to the mapping | Y/N |

## Red Flags

- No Accountable role, or multiple competing Accountable roles. The decision will either drift or produce conflict.
- Accountable role is very distant (hierarchically or geographically) from Responsible roles. Expect slow feedback loops and misalignment.
- More than 5 Consulted roles. The consultation phase will become a bottleneck.
- Consulted roles are not actually interviewed before decision; they are informed after. This is a misuse of the framework.
- The RACI matrix was created without asking the assigned roles for agreement. Roles will reject it in practice, and the matrix becomes theater.
- Responsible and Accountable are the same person *and* they are junior or new. Accountability without authority is a setup for failure.
- A critical role (e.g., legal, security) is marked Informed instead of Consulted. This usually means the decision was made without proper governance.

## Output Format

```
## RACI Assessment

**Decision/Process:**
<one sentence describing the decision or process being mapped>

### Stakeholder List (Phase 1)
- <role/team>
- <role/team>
...

### Role Assignments (Phase 2)

| Role | Category | Justification |
|---|---|---|
| <role> | A | <why this role owns the outcome> |
| <role> | R | <why this role does the work> |
| <role> | C | <what veto or required input they provide> |
| <role> | I | <why they need to know the outcome> |

### Validation Checks (Phase 3)

| Check | Result | Notes |
|---|---|---|
| Exactly one Accountable? | Y/N | <any concerns> |
| Accountable close to Responsible? | Y/N | <escalation path if remote> |
| Consulted count ≤5? | Y/N | <trim list if needed> |
| All roles reviewed and agreed? | Y/N | <date of sign-off or names of dissenters> |

### Escalation Path
<If Accountable and Responsible are distant: describe how disagreements will be resolved>

### Confidence
<high | medium | low> — <justification: e.g., "high — all roles reviewed and agreed in writing; low — Accountable role is unfamiliar with the domain and may reverse decisions">
```
