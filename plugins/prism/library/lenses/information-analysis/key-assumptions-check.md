---
name: key-assumptions-check
display_name: Key Assumptions Check
class: lens
underlying_class: native
domain: information-analysis
source: Donald Rumsfeld (2002, "unknown unknowns"); operationalized in risk analysis and decision theory
best_for:
  - Surfacing unstated beliefs before committing to a decision
  - Identifying which assumptions, if wrong, would change the outcome
  - Separating defensible premises from inherited folklore
one_liner: "Enumerate unstated assumptions and flag each for testability."
---

# Key Assumptions Check

## Overview
Every argument, recommendation, or plan rests on assumptions — some stated, most buried. This lens systematically excavates them, categorizes them by verifiability, and flags which ones, if false, would reverse the conclusion. Practitioners use it before making irreversible decisions, adopting a framework, or accepting a proposal that feels right but whose reasoning chain hasn't been made explicit.

## Analytical Procedure

### Phase 1 — Extraction

1. **State the core claim or decision.** Write it as a single sentence. If it's a recommendation (e.g., "We should migrate to Postgres"), state it plainly.

2. **List the explicit reasoning chain.** Write 3–5 steps that justify the claim. Use the form: "We concluded X because Y" or "The recommendation rests on Z."

3. **For each step in the reasoning, ask: "What would have to be true for this step to be valid?"** Write down every prerequisite, no matter how obvious it seems. Examples:
   - "This metric is accurate" (prerequisite: measurement methodology is sound)
   - "Our competitor can't do this" (prerequisite: we know their technical constraints)
   - "The cost will be $50K" (prerequisite: the estimate is based on current pricing and scope hasn't shifted)

4. **Expand the list by asking "What am I taking for granted here?"** Go through the problem context, the data, the constraints, the timeline. Write down:
   - Factual assumptions (claims about the world: "user retention is 60%")
   - Causal assumptions (claims about cause-and-effect: "improving UX will reduce churn")
   - Scope assumptions (claims about what is and isn't relevant: "mobile doesn't matter for this use case")
   - Temporal assumptions (claims about how long things hold: "this regulatory status won't change in 12 months")
   - Stakeholder assumptions (claims about who cares and why: "customers will pay more for this feature")

### Phase 2 — Categorization

5. **For each assumption, assign a category:**
   - **Verifiable** — Can be checked directly (testable against data or reality)
   - **Defensible** — Not directly testable but grounded in evidence, logic, or expert consensus
   - **Inherited** — Accepted because it's part of the framework, precedent, or received wisdom; origin of the assumption is unknown or unexamined
   - **Speculative** — Grounded in intuition, analogy, or best guess; no empirical or logical foundation is present

6. **For each assumption, rate its criticality:**
   - **Pivotal** — If this assumption is false, the conclusion reverses or the decision should change materially
   - **Important** — If false, it weakens the case but doesn't overturn it
   - **Incidental** — If false, it affects details but not the substance

### Phase 3 — Pressure Test

7. **For each Pivotal assumption, ask: "What would convince me this is wrong?"** Write down:
   - What evidence would disconfirm it?
   - When would you check for that evidence?
   - How much would you invest in testing it before acting?

8. **For each Inherited assumption, ask: "Where did this come from?"** Trace it back one step. Is it:
   - A past decision with written justification? (Find that justification and re-evaluate it)
   - An industry standard? (Who set it and when? Does it still apply?)
   - An assumption from a predecessor or adjacent team? (Do they know they're relying on it?)

9. **For each Speculative assumption, ask: "What's the next-easiest way to move this toward Defensible or Verifiable?"** Examples:
   - Run a small pilot, survey, or reference check
   - Ask a domain expert to assess the assumption's plausibility
   - Look for analogous situations in your own or adjacent organizations

## Evaluation Criteria

| Check | Pass |
|---|---|
| Core claim is stated as a single sentence | Y/N |
| Explicit reasoning chain is 3–5 steps | Y/N |
| At least 2 assumptions per reasoning step identified | Y/N |
| Every assumption is tagged with a category (Verifiable/Defensible/Inherited/Speculative) | Y/N |
| Every assumption is tagged with a criticality level (Pivotal/Important/Incidental) | Y/N |
| At least one Pivotal assumption has a disconfirmation test written | Y/N |
| At least one Inherited assumption has its origin traced | Y/N |

## Red Flags

- All assumptions are tagged "Defensible" or "Verifiable." Either the decision is trivial or the excavation stopped too early. Inherited and Speculative assumptions hide in recommendations that feel obvious.
- No Pivotal assumptions exist. If nothing would change the conclusion, the decision isn't actually a decision — it's foregone. Re-examine whether the claim is as solid as it appears.
- Inherited assumptions have no origin story. "This is how we've always done it" is a flag, not a justification. Trace it.
- Disconfirmation tests are never run. Assumptions that are never checked become invisible constraints. If you won't test it, why did you write it down?
- Speculative assumptions outnumber Defensible ones. This is not necessarily a failure, but it signals that the decision is being made under high uncertainty. Acknowledge it explicitly.

## Output Format

```
## Assumptions Assessment

**Core claim:**
<single sentence>

**Explicit reasoning chain:**
1. <step>
2. <step>
3. ...

### Assumption Inventory

| # | Assumption | Category | Criticality | Disconfirmation test / Origin / Path to defensible |
|---|---|---|---|---|
| 1 | <...> | Verifiable / Defensible / Inherited / Speculative | Pivotal / Important / Incidental | <...> |
| 2 | ... | ... | ... | ... |

### Pivotal Assumptions — Pressure Test
1. **Assumption:** <...>
   - **What would prove it wrong?** <...>
   - **When to check:** <...>
   - **Investment threshold:** <...>

### Inherited Assumptions — Origin Trace
1. **Assumption:** <...>
   - **Origin:** <...>
   - **Still valid?** <...>

### Speculative Assumptions — Move to Defensible
1. **Assumption:** <...>
   - **Next step:** <...>

### Summary
- Total assumptions: _
- Verifiable: _ | Defensible: _ | Inherited: _ | Speculative: _
- Pivotal: _ | Important: _ | Incidental: _
- Assumptions with no test/trace plan: _

### Confidence
<high/medium/low> — <justification of whether the claim can be acted on given the assumption profile>
```
