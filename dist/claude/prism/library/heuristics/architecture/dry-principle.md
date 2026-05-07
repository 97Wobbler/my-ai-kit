---
name: dry-principle
display_name: DRY Principle
class: heuristic
underlying_class: native
domain: architecture
source: Andy Hunt and Dave Thomas, *The Pragmatic Programmer* (1999)
best_for:
  - Code review and refactoring
  - Knowledge management and documentation
  - System design and maintainability
one_liner: "Every piece of knowledge must have a single, authoritative representation."
---

# DRY Principle

## The Rule

Do not repeat yourself. Every piece of knowledge should exist in exactly one place in the codebase. If the same logic, constant, or piece of information is defined multiple times, changes and inconsistencies become inevitable.

## When It Applies

- Identifying duplicate SQL queries, validation logic, or error-handling patterns and extracting them into shared functions.
- Refactoring data transformations or business rules that appear in multiple service implementations.
- Managing configuration, constants, and schema definitions that must remain synchronized across multiple files.
- Deciding whether to extract a common pattern into a shared library or utility module.

## When It Misleads

- When applied to combine unrelated pieces of code that happen to look similar but serve different purposes. Extracting them into one function creates a false coupling and makes the code harder to understand and modify independently.
- When it leads to over-abstraction: creating a shared function to avoid repeating code twice when the abstraction itself becomes more complex and harder to maintain than the duplication.
- In teams where DRY is enforced rigidly without considering the cost of sharing. A shared function with many conditional branches is sometimes worse than two separate implementations.
- When "knowledge" is conflated with "similar-looking code." Two similar algorithms solving different problems are not the same knowledge.

## Common Misuse

Creating increasingly convoluted abstractions to avoid repetition, or building a "shared utility layer" that nobody understands because it tries to handle too many variations. The heuristic is about *knowledge*, not textual similarity. Two pieces of code that look alike but express different domain concepts should not be merged just to avoid repetition.

## How Agents Use It

- **Embedded**: in code review or refactoring lenses, as a step to identify when the same knowledge is represented in multiple places and the cost of consolidating it.
- **Sanity-gate**: on refactoring or abstraction recommendations, ask: "Is this consolidation reducing genuine duplication of *knowledge*, or are we combining unrelated concepts to achieve textual brevity?"
