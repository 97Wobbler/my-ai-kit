---
name: red-team-analysis
display_name: Red Team Analysis
class: lens
underlying_class: native
domain: information-analysis
source: origin uncertain; military red-teaming doctrine; adapted for strategic planning (1970s–present)
best_for:
  - Finding blind spots and unexamined vulnerabilities in a plan before execution
  - Stress-testing strategy by simulating adversarial intent
  - Uncovering assumptions about what will or won't work
one_liner: "Attack your own plan from the adversary's perspective to surface fatal flaws in advance."
---

# Red Team Analysis

## Overview
Red Team Analysis inverts the usual perspective: instead of defending a plan or proposal, you simulate a capable adversary attacking it. The goal is not to prove the plan wrong but to identify what an intelligent opponent would exploit, what assumptions are exposed, and what failure modes the plan's architects may have dismissed too quickly. Practitioners use this when stakes are high enough that a plan's success is not guaranteed and when overconfidence or groupthink is a known risk.

## Analytical Procedure

### Phase 1 — Plan Framing

1. **State the plan in plain language.** Write the goal, the main actions, the expected outcome, and the time horizon. Assume the reader has no context.

2. **Identify the plan's critical assumptions.** These are the statements that, if false, would cause the plan to fail. Look for:
   - Assumptions about external actors' behavior (e.g., "competitors won't retaliate quickly")
   - Assumptions about internal capability (e.g., "we can execute this in 6 months")
   - Assumptions about market or environmental stability (e.g., "regulations won't tighten")
   - Assumptions about probability or timing (e.g., "the window of opportunity lasts until Q4")
   Write at least 5. Write more if the plan is complex.

3. **Identify the plan's dependencies and leverage points.** What would an adversary target to make the plan fail? Look for:
   - Resources that could be cut off or made expensive
   - Relationships that could be severed or poisoned
   - Information the plan relies on that could be corrupted
   - Timing windows that could be foreclosed
   - Coalitions that could be disrupted
   - Regulatory or reputational vulnerabilities

### Phase 2 — Adversarial Simulation

4. **Adopt an adversary persona.** Write a 2–3 sentence description of who is trying to stop you (or who would be harmed by your success). Do not make them a cartoon villain. A capable adversary is intelligent, resourced, and motivated. Answer: What is their goal? What is their time horizon? What constraints do *they* face?

5. **For each critical assumption in Phase 1, ask: "How would the adversary invalidate this?"** Generate at least 2 concrete tactics per assumption. Be specific about tools, timelines, and resource requirements. Examples:
   - Instead of: "They'd undermine trust." Write: "Day 1–7: seed social media with evidence of your previous failures. Day 8–14: petition to regulators with questions about your compliance record. By day 21, a journalist picks it up."
   - Instead of: "They'd slow us down." Write: "They patent a related technique (cost $50k, 2 months). They license it exclusively to your largest competitor. You're blocked for 18 months."

6. **For each leverage point in Phase 1, ask: "What is their move?"** Write the specific action the adversary would take, the cost to them, the impact on your plan, and the lag time before impact shows.

7. **Aggregate and rank the adversary's moves by impact and cost-to-execute.** The highest-impact, lowest-cost moves are the ones you should worry about most. These are the plan's real vulnerabilities.

### Phase 3 — Plan Stress-Test

8. **For each high-ranked adversarial move, ask: "Do we have a response?"** Write the counter-move or mitigation you could deploy. If you have no response, note it. If your response is slow or expensive, note that too.

9. **Assess whether the plan still succeeds under the adversary's best strategy.** Does the plan have slack (extra time, budget, relationships) that allows it to absorb the hit? Or does it fail?

10. **Identify the assumptions or dependencies that the adversary can break for minimal cost.** These are the plan's genuine Achilles heels. Write them down separately.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Plan statement is plain-language and under 150 words | Y/N |
| At least 5 critical assumptions are identified and stated explicitly | Y/N |
| At least 3 leverage points or dependencies are named | Y/N |
| Adversary persona is specific and credible (not a strawman) | Y/N |
| Each assumption has ≥2 concrete adversarial tactics (not vague) | Y/N |
| Each tactic includes resource cost, timeline, and expected impact | Y/N |
| Adversarial moves are ranked by impact and cost-to-execute | Y/N |
| A response (or lack thereof) is documented for each top-ranked move | Y/N |

## Red Flags

- The adversary persona is weak or abstract ("the competitors" or "the bad guys"). A vague adversary produces vague threats.
- All tactics are slow or expensive for the adversary. A plan with no cheap, fast way to break it is usually overestimating its robustness.
- No assumptions are invalidated by the adversary's moves. Either the plan is genuinely solid (rare) or the red team was too lenient.
- Responses to adversarial moves are stated in general terms ("we'll communicate better" or "we'll be flexible"). Without specifics, you have no mitigation.
- The red team identifies moves but never assesses whether the plan still succeeds under the adversary's best play. Without that verdict, the analysis is incomplete.
- The plan's advocates are doing the red team analysis. There is a strong bias toward finding only tolerable threats.

## Output Format

```
## Red Team Assessment

**Plan statement:**
<plain-language summary of goal, actions, expected outcome, time horizon>

### Phase 1 — Plan Framing

**Critical assumptions:**
1. <assumption>
2. <assumption>
... (at least 5)

**Leverage points and dependencies:**
1. <point>
2. <point>
... (at least 3)

### Phase 2 — Adversarial Simulation

**Adversary persona:**
<2–3 sentences: goal, time horizon, constraints>

**Adversarial moves ranked by impact and cost:**

| Assumption or dependency | Adversary's tactic | Cost to adversary | Timeline | Impact on plan | Likelihood |
|---|---|---|---|---|---|
| <...> | <concrete action> | <resource cost> | <when effect appears> | <consequence> | High/Medium/Low |
| <...> | <...> | <...> | <...> | <...> | <...> |

### Phase 3 — Stress-Test

**Response to top-ranked moves:**
1. Move: <tactic>
   Response: <your counter, or "no mitigation identified">
   
2. Move: <tactic>
   Response: <...>

**Plan resilience under adversary's best strategy:**
<Does the plan succeed or fail if the adversary executes their highest-impact, lowest-cost plays? Why?>

**Achilles heels (assumptions the adversary can break cheaply):**
1. <assumption> — adversary cost: <$>, timeline: <>, your recovery time: <>
2. <...>

### Confidence
<high/medium/low> — <justification (e.g., adversary persona is credible; tactics are grounded in observable behavior; gaps in your response layer are documented; or: analysis is constrained by limited knowledge of adversary capabilities)>
```
