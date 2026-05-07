---
name: principles-of-war
display_name: Principles of War
class: heuristic
underlying_class: native
domain: military-strategy
source: Carl von Clausewitz, On War (1832); formalized by U.S. military doctrine (20th century)
best_for:
  - strategic planning and campaign design
  - evaluating military or competitive operations
  - detecting when a plan violates doctrine without explicit justification
one_liner: "Judge operational soundness against the nine principles of war."
---

# Principles of War

## The Rule
A military operation that violates the nine classical principles of war without explicit reasoning about the trade-off is likely to fail or to succeed despite poor planning rather than because of it.

## When It Applies
- Evaluating a campaign or operational plan for internal coherence before execution.
- Diagnosing why a past operation failed despite adequate resources and no clear enemy surprise.
- Assessing competitive or organizational strategies that mirror military structure (competitive campaigns, market offensives, organizational restructuring).
- Reviewing a plan that appears to have blind spots but lacks clear justification for departing from doctrine.

## When It Misleads
- The enemy or competitive environment has changed enough that classical doctrine no longer applies. Adherence to Napoleonic or Cold War principles may be liability in asymmetric, cyber, or non-kinetic domains.
- The nine principles (objective, offensive, mass, economy of force, maneuver, unity of command, security, surprise, simplicity) are often stated differently across military traditions and eras, making any single checklist incomplete or culture-bound.
- A plan that violates one principle deliberately in order to achieve a higher principle is not automatically worse — the trade-off may be sound. The heuristic catches *unexamined* violations, not *deliberate* ones.
- In highly uncertain or exploratory settings, strict adherence to doctrine can rigidify thinking and prevent adaptation to new information.

## Common Misuse
Treating the nine principles as a scoring rubric or algorithm ("if you hit all nine, you win"). The heuristic is diagnostic, not predictive — it flags when a plan is missing an explicit justification for doctrinal departure, not whether the departure is right. Agents often cite "we follow the principles" without actually mapping each principle to the plan's architecture, letting the checklist substitute for reasoning.

## How Agents Use It
- **Embedded**: in military or competitive strategy lenses, after the operation is drafted, as a mandatory audit step. For each of the nine principles, the agent forces the planner to state explicitly whether the plan adheres, violates with justification, or violates and hasn't noticed.
- **Sanity-gate**: on each top recommendation for a major campaign or operation, ask: "Which classical principle does this plan de-prioritize, and why is that trade-off necessary?" If the answer is blank or defensive, the finding is premature.
