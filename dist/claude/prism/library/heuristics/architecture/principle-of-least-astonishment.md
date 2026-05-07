---
name: principle-of-least-astonishment
display_name: Principle of Least Astonishment
class: heuristic
underlying_class: native
domain: architecture
source: Design principle (origins in Unix culture; codified in software engineering)
best_for:
  - API and interface design
  - Code review and naming
  - User experience and developer experience
one_liner: "Software should behave as expected; avoid surprising the user or maintainer."
---

# Principle of Least Astonishment

## The Rule

Software components, functions, APIs, and interfaces should behave in the way that is most consistent with user expectations. If a function or API does something unexpected, it will lead to bugs, confusion, and misuse.

## When It Applies

- Naming a function; if it is called `delete()`, it should delete, not archive. If it is called `parse()`, it should parse, not fetch and parse.
- Designing an API where parameter order or return type matches conventions in the domain or language.
- Choosing default behaviors for configuration or feature flags; defaults should favor the common case, not a surprising edge case.
- Reviewing error messages, logging output, or UI wording to ensure they convey what actually happened, not what a developer thought should happen.

## When It Misleads

- When "expected" behavior is unclear because the domain itself is novel. Early in a new API's life, "expected" may not be established.
- In optimization-heavy contexts, where the most performant behavior is not the most intuitive. A poorly-named but fast operation can be worse than a well-named but slower one.
- When applied to domain logic that is intentionally non-obvious or counterintuitive by necessity. A tax calculation or game rule may not match naive intuition.
- If it becomes an excuse to preserve legacy behavior. Sometimes surprising behavior is a bug, not a feature.

## Common Misuse

Using "principle of least astonishment" to defend a design without analyzing what users will actually expect. The principle requires understanding the user's mental model, not imposing the designer's idea of what "should" be surprising. Another misuse: conflating "explicit" with "unsurprising." Explicit, verbose behavior is not automatically less astonishing than concise behavior.

## How Agents Use It

- **Embedded**: in API design or code review lenses, as a step to check whether naming, signatures, defaults, and error conditions match reasonable user expectations in the domain.
- **Sanity-gate**: on API and interface recommendations, ask: "Is this behavior consistent with the name and the context? Would a developer reading the name alone predict what will happen?"
