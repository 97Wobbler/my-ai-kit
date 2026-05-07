---
name: single-responsibility-principle
display_name: Single Responsibility Principle
class: heuristic
underlying_class: native
domain: agile
source: Robert C. Martin, Clean Architecture, 2017
best_for:
  - Class and module design review
  - Refactoring over-coupled code
  - API boundary definition
one_liner: "A class should have only one reason to change."
---

# Single Responsibility Principle

## The Rule
A class or module should have only one reason to change — that is, only one axis of responsibility or domain reason to modify it.

## When It Applies
- Designing a new class and deciding what cohort of behavior belongs in it versus split across multiple classes.
- Reviewing a class that has grown to handle both persistence and business logic, or validation and transformation.
- Extracting a library or API from application code — SRP forces you to isolate domain concerns from infrastructure concerns.
- Triaging where to place a new method when a class is already doing two unrelated things well.

## When It Misleads
- Taken to extremes, SRP can fragment a codebase into hundreds of single-method classes, where the cognitive overhead of navigation and composition exceeds the benefit of decoupling.
- When the "single responsibility" is vague or defined too broadly (e.g., "handle user data" is one reason, but "validate, persist, cache, and serialize user data" is actually four).
- In codebases where the cost of splitting a responsibility is higher than the cost of keeping it together — tight performance budgets, synchronous request-response loops, or teams too small to maintain the split code.
- SRP assumes that responsibilities will change independently; if two responsibilities always change together, splitting them creates false separation.

## Common Misuse
Treating SRP as a size rule ("classes should be small") rather than a cohesion rule. A 500-line class handling one domain concern (e.g., a complex state machine) is often better than a 50-line class handling three unrelated concerns. The misuse is also confusing "responsibility" with "method" — a class with ten methods cohering around one purpose is not violating SRP; a class with three methods each serving a different master probably is.

## How Agents Use It
- **Embedded**: in a code review or refactoring lens, as a check step after identifying a class's actual behaviors — ask whether each behavior is driven by a separate stakeholder or change axis.
- **Sanity-gate**: when a design or refactoring recommendation involves merging classes, ask whether their responsibilities are truly unified or whether the merge is driven by convenience. When splitting, ask whether the new classes will change together in practice or represent genuinely independent concerns.
