---
name: daci
display_name: DACI Decision Framework
class: lens
underlying_class: native
domain: decision
source: Intuit (origin uncertain, circa 2000s); popularized in tech and organizational decision-making
best_for:
  - Clarifying decision ownership when multiple stakeholders are involved
  - Preventing deadlock by separating who decides from who inputs
  - Scaling decisions in matrixed organizations
one_liner: "Split accountability and consensus by assigning Driver / Approver / Contributors / Informed to a decision."
---

# DACI Decision Framework

## Overview
DACI assigns four distinct roles to stakeholders in a single decision: the Driver (owns the decision process), the Approver (has veto power), Contributors (provide input), and Informed (are notified of the outcome). The discipline is specificity — most decisions fail not because the choice was wrong but because nobody knew who was actually deciding or why others were excluded from the room. Practitioners use this when a decision involves multiple teams, when silence from a stakeholder later becomes "we weren't consulted," or when a decision-maker is unclear.

## Analytical Procedure

1. **State the decision in one sentence.** Make it binary or multi-option, but concrete. Bad: "How do we improve performance?" Good: "Do we migrate the auth service to Rust, keep it in Python, or rebuild it in Go?"

2. **List all stakeholders with a material interest in the decision.** Include people who will execute it, people who will be affected by it, people who control resources it depends on, and people whose reputation is tied to its success or failure. Write names or roles, not vague categories.

3. **For each stakeholder, assign one role and only one role:**
   - **Driver**: Owns the decision process. Gathers input, runs the meeting, synthesizes disagreement, makes the final call if consensus fails. There is exactly one Driver per decision.
   - **Approver**: Has veto power. Rarely used; signals that this decision is constrained by a higher authority (legal, exec, board). Usually 0–1 per decision. If you have 3 Approvers, the decision is actually owned by their collective (go back to step 2).
   - **Contributors**: Provide input, expertise, or constraints. They answer questions but do not decide. They lose decision power in exchange for clarity: they know they will be heard and know when to stop advocating.
   - **Informed**: Must be notified of the outcome but do not participate in the decision. This role exists to prevent surprises and to keep people in the loop without slowing down the decision.

4. **Validate the role assignments against the decision's scope.** A common error is making someone a Contributor when they should be Approver (they have blocking power and didn't know it), or making someone Informed when they should be Contributor (they have expertise you need). Ask: Does this person have veto power? (→ Approver) Can they cause the decision to fail in execution? (→ Contributor) Will this decision affect their work? (→ Informed or Contributor, depending on whether you need their input).

5. **Set a decision deadline and a rationale.** When will the Driver decide? Why that date? Write it down to prevent indefinite deliberation. Include how long Contributors will have to give input before the Driver makes the call.

6. **Run the decision process.** The Driver collects input from Contributors (synchronously in a meeting or asynchronously in a doc), surfaces objections and evidence, and makes a call. The Approver (if one exists) validates or rejects. If rejected, the Driver and Approver align or escalate.

7. **Document and notify.** Write down: the decision, the reasoning, who decided (Driver and Approver), who contributed, and when it becomes effective. Distribute this to all four role groups. Informed stakeholders receive notification; Contributors can see the reasoning; the Approver sees the final choice.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Decision is stated as a concrete choice, not a vague goal | Y/N |
| All material stakeholders are listed by name or role | Y/N |
| Each stakeholder has exactly one role (D/A/C/I) | Y/N |
| Only one Driver is assigned | Y/N |
| 0–1 Approver is assigned (not multiple with veto) | Y/N |
| Deadline and rationale for the deadline are documented | Y/N |
| Contributors were given a clear window to input before decision | Y/N |
| Final decision, reasoning, and process are documented and distributed | Y/N |

## Red Flags

- Multiple people claim to be "the Driver" or nobody knows who it is. The decision will stall or fork.
- An Approver rejects the decision after the fact with new criteria that weren't shared upfront. The decision was never actually authorized.
- A key stakeholder was left as "Informed" but their input would have changed the decision if sought. They become an opponent instead of a Contributor.
- The decision deadline passes and the Driver hasn't decided. The deadline was not credible or the Driver was absent.
- Contributors gave contradictory input and the Driver's reasoning for choosing one over the other is absent. You cannot tell whether the "right" input was selected or the Driver just picked their preference.
- The decision is documented but never distributed. People find out through the grapevine and assume they weren't consulted.

## Output Format

```
## DACI Assessment

**Decision:**
<one sentence, concrete choice>

**Deadline & Rationale:**
Decide by <date>. Reason: <why this date>

### Role Assignments
| Stakeholder | Role | Justification |
|---|---|---|
| <name/role> | Driver/Approver/Contributor/Informed | <why this role> |

### Validation Check
- Does the Driver have authority to decide without an Approver veto? <yes/no>
- Do Contributors have the expertise or veto power needed to shape the decision? <yes/no>
- Are any key stakeholders missing? <yes/no — list if yes>

### Decision Process
1. **Input window**: Contributors given <duration> to provide input.
2. **Synthesis**: Driver summarized input on <date> in: <link or location>.
3. **Objections**: Key disagreements and how Driver addressed them:
   - <objection>: <how addressed>
4. **Approver validation**: <approved/rejected/pending> on <date>
5. **Final call**: <decision> by Driver on <date>

### Distribution
- **Approver informed**: <yes/no> on <date>
- **Contributors shown reasoning**: <yes/no> on <date>
- **Informed notified of outcome**: <yes/no> on <date>

### Confidence
<high | medium | low> — <justification>
- High: All roles assigned, deadline credible, decision documented and distributed.
- Medium: Roles assigned but deadline is soft, or decision documented but distribution incomplete.
- Low: Unclear Driver or Approver, missing Contributors, or no documented reasoning.
```
