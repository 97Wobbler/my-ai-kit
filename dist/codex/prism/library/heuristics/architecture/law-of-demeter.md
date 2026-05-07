---
name: law-of-demeter
display_name: Law of Demeter
class: heuristic
underlying_class: native
domain: architecture
source: Ian Holland, Northeastern University (1987)
best_for:
  - Object-oriented design review
  - API design and encapsulation
  - Coupling and dependency analysis
one_liner: "Talk only to your immediate neighbors; avoid chained method calls."
---

# Law of Demeter

## The Rule

An object should only interact directly with objects it has direct knowledge of. Avoid navigating through the internal structure of other objects (e.g., `a.getB().getC().doSomething()`). Also called the "Principle of Least Knowledge."

## When It Applies

- Reviewing code that chains getters across multiple objects. If the chain is more than two levels deep, it is likely violating the law.
- Designing an API or object interface where you want to hide the internal structure of a complex object from its users.
- Assessing the impact of a refactoring that moves or renames a field deep in a nested structure; many callers may break if they are chained.
- Reducing coupling between components by ensuring that each layer exposes only what its direct clients need.

## When It Misleads

- In functional programming or query-oriented paradigms where chaining is idiomatic (e.g., fluent APIs, method chaining, LINQ/SQL operations). The law was conceived for imperative OOP and does not translate equally.
- When applied too strictly, it can lead to verbose wrapper layers that obscure the actual intent. Sometimes a direct accessor is clearer than a deeply nested delegation chain.
- In data-heavy systems where you genuinely need to traverse a known structure (e.g., serialization, validation). Requiring a wrapper for every level of access can hide intent.
- When the "neighbor" is not well-defined in the design. The law assumes clear object boundaries that may not exist in older or more loosely-coupled systems.

## Common Misuse

Using the law as a reason to build elaborate facade layers that hide nothing and clarify nothing. The spirit of the law is *encapsulation*: if you must access something deep in a structure, that is a signal that the structure's boundaries are wrong, not that you need a wrapper method.

## How Agents Use It

- **Embedded**: in OOP design or API review lenses, as a step to examine call chains and flag those that suggest the calling code is too tightly coupled to the internal structure of its dependencies.
- **Sanity-gate**: on API or refactoring recommendations, ask: "Does this change require callers to know about the internal structure? Can we hide that detail behind a single method?"
