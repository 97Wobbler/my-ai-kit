---
name: kiss-principle
display_name: KISS Principle
class: heuristic
underlying_class: native
domain: architecture
source: US Navy, 1960s (attributed to Kelly Johnson)
best_for:
  - System design simplification
  - Architecture review and refactoring
  - Technical decision-making and trade-off analysis
one_liner: "Keep it simple, stupid — simplicity is the highest engineering value."
---

# KISS Principle

## The Rule

Most systems work better if they are kept simple rather than complex. Simplicity should be a primary design goal.

## When It Applies

- Choosing between two architectural approaches; prefer the one that requires fewer moving parts, even if it sacrifices some flexibility.
- Evaluating whether to add a new abstraction layer, build tool, or framework; the burden of understanding and maintaining that layer must be justified.
- Reviewing a design proposal that introduces inheritance, generics, or indirection to handle hypothetical future cases.
- Pruning features from a release when time pressure makes shipping a smaller, focused product more valuable than a comprehensive one.

## When It Misleads

- In domains with inherent complexity (distributed systems, real-time systems, security). Forcing simplicity may mean ignoring load-bearing complexity; the result is a simple system that fails under real conditions.
- When "simple" is confused with "familiar." Choosing a familiar library because you know it, even though a different one is simpler, violates the principle in spirit.
- When simplicity early means exponential complexity later. A simple initial design can become vastly harder to extend, patch, or scale. Sometimes complexity up front is a trade against worse complexity later.
- In team dynamics, if "keep it simple" becomes a reason to avoid mentorship or to reject solutions that are unfamiliar but more correct.

## Common Misuse

Using KISS as a rhetorical weapon against any design that the speaker does not understand. The principle is about *appropriate* simplicity, not simplicity at all costs. Another misuse: conflating simplicity with brevity. A simple design may require verbose explanation; the brevity of code is not the measure of the principle.

## How Agents Use It

- **Embedded**: in architecture review or design choice lenses, as a step to evaluate the complexity-to-benefit ratio of each proposed element.
- **Sanity-gate**: when a design includes multiple indirection layers, abstraction boundaries, or "future-proofing" mechanisms, require explicit justification: "Why is this complexity necessary *today*?"
