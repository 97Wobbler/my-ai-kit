---
name: v2mom
display_name: V2MOM (Salesforce)
class: lens
underlying_class: native
domain: okr
source: Salesforce; popularized by Marc Benioff (Salesforce founder) and incorporated into organizational planning frameworks
best_for:
  - Aligning teams around a shared vision with explicit trade-off analysis
  - Identifying obstacles before they derail execution
  - Translating high-level aspirations into measurable outcomes
one_liner: "Vision / Values / Methods / Obstacles / Measures — structure strategic execution and manage failure risk proactively."
---

# V2MOM (Salesforce)

## Overview

V2MOM is a five-component strategic planning framework that forces clarity at each stage from inspiration to measurement. The acronym stands for Vision (where you're going), Values (what matters to you), Methods (how you'll get there), Obstacles (what will stop you), and Measures (how you'll know you succeeded). Organizations use this lens when a plan sounds good but lacks coherence—when some teams are optimizing for different things, or when leadership can articulate the destination but not the path. The discipline is the interrogation: each component must be concrete enough to guide daily decisions and specific enough that a team member unfamiliar with leadership can understand it.

## Analytical Procedure

### Phase 1 — Extract the Existing Plan

1. **State the Vision in one sentence.** What does success look like in 12–24 months? It should be aspirational but grounded. If it reads like a mission statement, it's too broad. If it reads like a tactic, it's too narrow.

2. **List the Values (3–5 items).** What matters most in how you execute? Not your company-wide values—the values *for this initiative*. Examples: "speed over perfection," "customer feedback above internal convention," "cost-efficiency in engineering."

3. **List the Methods (5–10 items).** How will you get to the Vision? Each should be a directional action or initiative, not a detail. Good: "Build a self-service API." Bad: "Write 50 endpoints."

4. **Enumerate the Obstacles (3–7 items).** What will try to stop you? Be specific: resource constraints, market conditions, competing priorities, technical debt, regulatory limits, or organizational patterns.

5. **Define the Measures (3–5 items).** What does "done" look like numerically? Each measure should be tied to a Method and traceable monthly. Avoid vanity metrics.

### Phase 2 — Validate Internal Coherence

6. **For each Method, trace it to a Value.** Does this initiative honor what you said matters? If a Method contradicts a Value, flag it as a conflict. Example: Value = "customer feedback above internal convention"; Method = "Implement quarterly release cadence with no mid-cycle changes." Conflict detected.

7. **For each Measure, trace it backward to its Method and forward to its Vision impact.** Can you draw a causal chain? If a Measure exists but no Method drives it, that's a ghost metric. If a Method has no Measure, you have no way to know if it's working.

8. **Check for orphaned Obstacles.** For each Obstacle, identify which Method(s) it threatens and what specific mitigation or contingency exists. If an Obstacle is listed but no Method addresses it, mark it as unmitigated risk.

9. **Scan for missing Obstacles.** For each Method, ask: "What could prevent this from working?" If the Obstacles list doesn't include at least one threat per major Method, the planning is incomplete.

### Phase 3 — Pressure-Test Feasibility

10. **For each Method, estimate the resource cost** (headcount, budget, time) and compare against what you actually have. List what you'll have to stop doing or deprioritize if you proceed. If Methods are feasible only if Obstacles don't occur, that's plan fragility—note it.

11. **For each Obstacle, ask: "What's our threshold for triggering the contingency?"** An unquantified threat is just worry. Example: Obstacle = "Key engineer leaves." Threshold = "If we lose 2+ engineers in Q1, we delay Feature X by one quarter." Without the threshold, the obstacle is theater.

12. **Identify single points of failure.** If one person, resource, or external condition is required by multiple critical Methods and nothing else can substitute, you have a brittle plan. Flag it.

### Phase 4 — Assemble the Assessment

13. **Check completeness.** Every Method should trace to a Value; every Measure should trace to a Method; every Obstacle should have a named mitigation. Create a matrix showing these links. Gaps = holes in the plan.

14. **Check contradiction.** If two Methods are in tension (require the same scarce resource, or pull in opposite directions), note it and decide: Is one higher priority, or do you need to sequence them?

15. **Estimate delivery confidence.** Given the Methods, resource constraints, and unmitigated Obstacles, what's your confidence in hitting the Vision in the stated timeframe? Low confidence doesn't mean the plan is bad—it means you've identified a genuine risk that leadership needs to accept consciously.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Vision is one sentence, aspirational but grounded | Y/N |
| Values are initiative-specific, not generic company values | Y/N |
| Methods are directional initiatives, not implementation details | Y/N |
| Obstacles are concrete threats, not vague concerns | Y/N |
| Measures are numeric, traceable, tied to Methods | Y/N |
| Every Method traces to at least one Value | Y/N |
| Every Measure traces backward to a Method | Y/N |
| Every Obstacle has a named mitigation or contingency threshold | Y/N |
| No orphaned Methods (Methods with no Measure) | Y/N |
| At least one Obstacle threatens each major Method | Y/N |

## Red Flags

- Vision reads like a mission statement or tagline. It's too abstract to guide trade-offs.
- Methods are numbered steps that read like a Gantt chart. V2MOM should be strategic, not a task list.
- Obstacles list contains only generic risks ("execution risk," "market changes") with no specificity. This signals that threats weren't examined closely.
- A Method contradicts a stated Value, but the plan proceeds as if there's no conflict.
- Multiple Methods require the same scarce resource (person, budget, tool) but the plan doesn't sequence or choose between them.
- Measures include metrics with no clear connection to the Methods driving them (e.g., "10% YoY growth" exists, but no Method aims at growth).
- Obstacles have no contingency threshold. They're listed but not operationalized.
- The plan was finalized in a single meeting. V2MOM requires at least two rounds of challenge and revision to uncover gaps.
- Leadership describes the plan differently in different rooms. That indicates the Vision, Values, or Methods aren't actually clear.

## Output Format

```
## V2MOM Assessment

**Vision:**
<one sentence: where you're going in 12–24 months>

**Values (for this initiative):**
1. <value>
2. <value>
...

**Methods (how you'll get there):**
1. <directional initiative>
2. <directional initiative>
...

**Obstacles (what will try to stop you):**
1. <specific threat and mitigation/threshold>
2. <specific threat and mitigation/threshold>
...

**Measures (how you'll know you succeeded):**
1. <metric, target, cadence>
2. <metric, target, cadence>
...

### Coherence Matrix
| Method | Tied to Value? | Tied to Measure? | Threat from Obstacle? |
|---|---|---|---|
| <...> | Yes/No | Yes/No | Yes/No |

### Unmitigated Obstacles
- <obstacle with no named mitigation>

### Resource Constraints
<What do you have to stop doing to execute these Methods?>

### Single Points of Failure
- <person, resource, or condition with no substitute>

### Delivery Confidence
<high/medium/low> — <justification based on Methods, resources, and unmitigated risk>

### Confidence in Assessment
<high/medium/low> — <whether the V2MOM as presented is complete and has been pressure-tested, or whether gaps remain>
```
