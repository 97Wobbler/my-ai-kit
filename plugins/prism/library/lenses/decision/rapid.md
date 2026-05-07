---
name: rapid
display_name: RAPID Decision Framework
class: lens
underlying_class: native
domain: decision
source: Bain & Company, 1980s–present
best_for:
  - Clarifying decision authority and unblocking stalled proposals
  - Mapping stakeholder roles in multi-party decisions
  - Preventing decision paralysis when consensus isn't achievable
one_liner: "Clarify decision rights and roles to speed up organizational decisions."
---

# RAPID Decision Framework

## Overview
RAPID names five roles in any decision: Recommend (who proposes), Agree (who must sign off), Perform (who executes), Input (who provides data/expertise), and Decide (who has final authority). A decision stalls when roles are unclear, when the wrong person has authority, or when stakeholders assume they have a role they don't. Practitioners use RAPID to map authority before debate begins, not to resolve debate itself — it is a clarity tool, not a consensus tool. The discipline is accepting that consensus is not always the goal.

## Analytical Procedure

### Phase 1 — Extract the Decision

1. **State the decision in one sentence.** What binary or small-cardinality choice is being made? (Examples: "Adopt vendor X or keep legacy system?" "Expand to market Y, defer it, or exit?" "Use tech A or tech B for the new platform?")

2. **Identify all stakeholders affected by or who have opinions about the decision.** List by role in the organization (e.g., "VP Engineering," "Data team lead," "CFO," "Product manager"). Do not yet assign RAPID roles — just list them.

3. **For each stakeholder, write down what they would naturally assume their role is.** Most stalled decisions fail because stakeholders assume they have veto power (Agree) when they actually have advisory power (Input), or vice versa.

### Phase 2 — Assign RAPID Roles

4. **Assign Recommend.** Who is best positioned to synthesize the available information and propose a direction? This is usually one person or a small team. Write the name and a one-sentence justification. If you cannot identify a single Recommend, the decision is not yet defined enough — return to Phase 1.

5. **Assign Decide.** Who has the authority to choose among the options if consensus cannot be reached? Write the name. This must be one person (not a committee — committees defer). If you cannot name a single Decide without hedging, authority is genuinely unclear and needs escalation before the framework applies.

6. **Assign Agree (veto holders).** Who can block the decision? These are people who have decision rights they cannot delegate. This is almost always a small number (0–3 people). For each Agree, write: name, the specific aspect they can veto (e.g., "cost overrun >20%," "timeline before Q3," "vendor with security issues"), and the reason they have this veto. Be honest: if they are listed only because "we've always asked them," they may not actually be Agree.

7. **Assign Input.** Who has expertise or data that informs the decision but no veto? List by domain (e.g., "Legal," "Security," "Finance"). For each Input role, specify what information they own (e.g., "contract risk analysis," "load-test results"). If someone is listed as Input only because they asked to be included in meetings, they may not belong here.

8. **Assign Perform.** Who will execute the decision once it's made? Usually the team that carries the decision. If the decision is policy or strategic, Perform may be multiple teams or distributed. List them and note what they are responsible for. If Perform is unclear, re-examine whether the decision is concrete enough.

9. **Check for duplicates and gaps.**
   - Can one person hold Recommend and Decide? Yes, but risky — removes a check.
   - Can one person hold Agree and Decide? No — Agree must be able to veto Decide.
   - Can one person hold Input and Agree? Yes, if they have both expertise and veto rights.
   - Is anyone missing? Did you account for legal, finance, security, or end-user representation?

### Phase 3 — Pressure Test

10. **For each Agree role, ask: "If this person says no, does the decision stop?"** If the answer is no, they are not Agree — downgrade them to Input.

11. **For each Input role, ask: "If we ignored this input, would the decision still be defensible?"** If the answer is no, they should be Agree. If the answer is yes, they stay Input.

12. **For the Recommend role, ask: "Would they be willing to be publicly accountable for this proposal?"** If no, they should not be Recommend — find someone who will own it.

13. **For the Decide role, ask: "Can this person live with the consequences of being wrong?"** If no, find someone who can. Decide is not a ceremonial role.

14. **Trace the information flow.** Starting from Input → Recommend, verify that Recommend actually receives the information they need and that the timeline allows for synthesis. If Input is not ready until after Recommend must propose, you have a sequencing problem — note it.

### Phase 4 — Document and Communicate

15. **Write a one-paragraph RAPID summary** that names each role and clarifies what *each person explicitly does not have*. Example: "Sarah (Recommend) will propose the platform choice by Friday. Finance (Input) will provide cost projections; they do not have veto power. CTO (Agree) can block on security grounds only. CEO (Decide) will choose if we're split. Engineering (Perform) will execute whatever is chosen."

16. **Share this summary with all stakeholders before the decision discussion begins.** Confirm or revise roles based on pushback. The goal is for everyone to agree on what they *don't* have, not what they do.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Decision is stated as a single binary or small-cardinality choice | Y/N |
| Recommend is a named individual, not a committee | Y/N |
| Decide is a named individual who can say no to Recommend | Y/N |
| Each Agree has a specific veto scope (not just "sign off") | Y/N |
| Agree roles do not include people for whom the answer to "if they say no, we stop" is "maybe" | Y/N |
| Input roles are distinguished from Agree by the "ignore this input" test | Y/N |
| Perform is clear about execution scope and timeline | Y/N |
| RAPID summary was shared with stakeholders *before* debate | Y/N |

## Red Flags

- Decide is a committee or a consensus. That is not RAPID; it is consensus-seeking, which works only if genuine agreement exists.
- Agree includes someone "to keep them happy." They are not Agree; you are mistaking political inclusion for decision authority.
- Input includes everyone who has an opinion. Input should be small and specific. If it is large, you have not yet decided what information actually matters.
- No Recommend is named, or Recommend is the same person as Decide. Recommend without external authority is a rubberstamp, not a proposal.
- Perform is surprised by the decision. This means it was not involved in Input or the recommendation phase — a red flag for feasibility.
- RAPID summary is shared *after* the decision is made. This is not RAPID clarification; it is retroactive legitimation.
- Stakeholders are allowed to assume their role differs from what was documented. Return to Phase 4 and re-confirm.

## Output Format

```
## RAPID Decision Map

**Decision:**
<one sentence>

### Roles

| Role | Name | Authority / Responsibility | Constraints |
|---|---|---|---|
| Recommend | <name> | Propose direction by [date] | <none or timeline constraints> |
| Decide | <name> | Choose among options if consensus fails | Must live with consequences |
| Agree | <name> | Veto on <specific scope> | <boundary of veto power> |
| Input | <domain> | Provide <specific data/expertise> | Does not veto |
| Perform | <team/name> | Execute <specific scope> | Feasibility owner |

### Pressure Test Results

| Check | Finding |
|---|---|
| Agree roles can actually stop the decision | Yes / No |
| Input roles would be missed if ignored | Yes / No / Some |
| Recommend will own the proposal publicly | Yes / No |
| Decide can accept being wrong | Yes / No |
| Information flow is feasible in timeline | Yes / No |

### RAPID Summary
<One paragraph naming each role and clarifying what they do NOT have.>

### Issues / Gaps
- <issue, if any>
- <issue, if any>

### Confidence
<high | medium | low> — <justification>
```
```
