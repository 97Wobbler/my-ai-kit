---
name: impact-mapping
display_name: Impact Mapping
class: lens
underlying_class: native
domain: product-management
source: Gojko Adzic, 2012 (Impact Mapping: Making a Big Impact with Software Products and Projects)
best_for:
  - Aligning delivery roadmap to measurable business outcomes
  - Surfacing hidden dependencies between actors and features
  - Shifting conversations from feature lists to impact hypotheses
one_liner: "Hierarchically map business goal → actors → behavior change → deliverable to make contribution explicit."
---

# Impact Mapping

## Overview
Impact Mapping is a lightweight planning technique that links a business goal to the people who can influence it, then to the behaviors those people need to change, and finally to the software features that enable those behaviors. Instead of starting with a feature list, you start with "Why?" and work outward. Practitioners use it to prevent feature creep, to pressure-test that a feature will actually move the needle on the goal, and to make tradeoffs visible to both delivery and business teams.

## Analytical Procedure

### Phase 1 — Establish the Goal

1. **Write the business goal in one sentence.** It must be measurable or at least observable. Examples: "Increase user retention to 60% after 30 days" or "Reduce support ticket volume by 40%." Avoid vague goals like "improve user experience" or "increase engagement." If the goal is vague, ask "How will we know we've won?"

2. **Define the baseline and target.** What is the current state? What is the target state? By when? Attach a number if possible. If a number is genuinely impossible, write the observable signal instead (e.g., "Customer feedback shifts from 'this is broken' to 'this works'").

3. **Identify any constraints or scope limits.** Budget, timeline, technical debt, regulatory barriers, or team capacity. Write these down now — they will shape which actors and behaviors are realistic.

### Phase 2 — Identify Actors

4. **List everyone who can influence the goal.** These are people whose behavior change would move the metric. Cast a wide net: end users, administrators, managers, support staff, partners, even competitors if their actions matter. Do not filter yet.

5. **For each actor, write one sentence describing their current relationship to the goal.** Are they blocking it? Unaware of it? Incentivized against it? This forces specificity.

6. **Prioritize actors by influence.** Which 2–4 actors would have the biggest impact if their behavior changed in the right direction? These are your focus. Keep 1–2 secondary actors for later iteration.

### Phase 3 — Define Impact (Behavior Change)

7. **For each primary actor, ask: "What must this person do differently to move the goal?"** Write as a behavior, not a feature. Bad examples: "Use the new dashboard," "Click the export button." Good examples: "Spend < 5 minutes on data entry instead of 20," "Decide to renew their subscription before it expires," "Delegate the approval process instead of rubber-stamping."

8. **For each behavior, ask: "Why aren't they doing this already?"** Common answers: lack of awareness, no incentive, friction in the current process, competing priorities, don't know how, afraid of risk. This answer is diagnostic — it will later inform which feature addresses the root cause.

9. **Write 2–3 impact statements per actor in this format:**
   - Actor: [name]
   - Current behavior: [what they do now]
   - Desired behavior: [what they should do]
   - Barrier: [why they don't do it now]

### Phase 4 — Map Deliverables

10. **For each desired behavior, brainstorm features or changes that would enable it.** Do not limit yourself to software — include process changes, policy changes, training, or organizational changes. Write each as a deliverable, not a technical spec. Examples: "Provide a one-click export," "Send a renewal reminder 30 days before expiry," "Create a checklist template for approvers."

11. **For each deliverable, ask: "Is this actually sufficient to change the behavior, or is it necessary but not sufficient?"** If it's just necessary, what else is needed? You may find that multiple deliverables are needed to move a single behavior.

12. **Estimate the **dependency chain** for each deliverable.** Does it depend on another deliverable? Does it assume a behavior change elsewhere? Does it block other features? Visualize these dependencies — they often reveal that a "simple" feature is downstream of a complex prerequisite.

13. **Assign confidence to each deliverable.** For each, write: "If we build this and the actor engages with it, will they change the behavior?" If confidence is low (< 60%), write why. This is often because the deliverable assumes something about the actor that isn't tested yet.

### Phase 5 — Test and Refine

14. **For each high-confidence, high-impact deliverable, write a one-sentence hypothesis:** "If we [deliverable], then [actor] will [behavior], and the goal will [improve by X]." Example: "If we send a renewal reminder 30 days before expiry, then SMB owners will renew before expiry, and retention will increase from 52% to 60%."

15. **Identify the riskiest hypotheses.** These are deliverables where the link between deliverable → behavior → goal is weakest. Plan to test these first or validate them with user research before building.

16. **Review the deliverable list with stakeholders.** Which can be cut? Which must be kept? This is where prioritization happens and scope gets negotiated visually — the map makes tradeoffs tangible.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Goal is measurable or observable and specific (not "improve experience") | Y/N |
| Baseline and target state are defined | Y/N |
| At least 2 primary actors are identified with current behavior described | Y/N |
| Each actor has 2–3 impact statements linking current → desired behavior | Y/N |
| At least one barrier (why they don't act now) is documented per actor | Y/N |
| Each deliverable is linked to a specific behavior and actor (not a generic feature) | Y/N |
| Dependency chain is mapped (at least 3 explicit dependencies called out) | Y/N |
| Confidence < 60% on at least one deliverable is documented with reason | Y/N |
| All high-priority deliverables have written hypotheses | Y/N |

## Red Flags

- The goal is unchanged from an executive mandate — no baseline or reasoning. This almost always means the goal hasn't been tested for feasibility.
- Actors list is entirely end users. High-value impact maps include operators, admins, and support staff whose behavior also affects the goal.
- Impact statements are written as features ("use the dashboard") not behaviors ("spend less time on data entry"). The team is still thinking in terms of what to build, not what to change.
- No barriers documented. The implication is that users will magically adopt the behavior once the feature ships — rarely true.
- Confidence is uniformly high across all deliverables. Either the problem is simpler than claimed or risky hypotheses are being underestimated.
- Dependencies are missing or invisible. Common sign: the team plans to build in order of "importance" without checking whether earlier work unblocks later work.
- The map is a checklist of requests from different stakeholders. It should trace lineage back to goal — if it's just a feature menu, it's not an impact map.

## Output Format

```
## Impact Map

**Business Goal:**
- Goal statement: <one measurable sentence>
- Current state: <baseline metric or observable>
- Target state: <target metric and timeframe>
- Constraints: <budget, timeline, scope, tech debt, team limits>

### Actors & Influence
| Actor | Current relationship to goal | Influence priority |
|---|---|---|
| <name> | <one sentence> | High / Medium / Low |

### Impact Statements (per primary actor)
**Actor: <name>**
- Current behavior: <what they do now>
- Desired behavior: <what they should do>
- Barrier: <why they don't do it>

### Deliverables & Hypotheses
| Deliverable | Links to actor | Behavior enabled | Hypothesis | Confidence | Riskiest assumption |
|---|---|---|---|---|---|
| <feature/change> | <actor name> | <desired behavior> | "If we [deliver], then [actor] will [behave], and [goal] will improve by [signal]" | H/M/L | <assumption to test> |

### Dependency Chain
- <Deliverable A> blocks <Deliverable B> because <reason>
- <Deliverable C> depends on <Deliverable D> because <reason>
- ...

### Prioritized Build Order
1. <deliverable> — <justification>
2. <deliverable> — <justification>
3. ...

### Open Questions & Validation Needed
- <question>: <how you'd test it>
- <question>: <how you'd test it>

### Confidence
<high/medium/low> — <justification: e.g., "High — goal is measurable, actors are identified via user interviews, and dependencies are mapped. Medium — two hypotheses (A and B) are untested and should be validated before build. Low — goal is ambiguous and actors don't include support staff, a critical influencer we've overlooked.">
```
