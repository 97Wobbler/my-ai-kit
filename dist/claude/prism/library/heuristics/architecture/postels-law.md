---
name: postels-law
display_name: Postel's Law / Robustness Principle
class: heuristic
underlying_class: native
domain: architecture
source: Jon Postel, RFC 760/761/793 (1980)
best_for:
  - API design and schema evolution
  - Integration resilience
  - Protocol and boundary system design
one_liner: "Conservative in what you send, liberal in what you accept."
---

# Postel's Law / Robustness Principle

## The Rule

Be conservative in what you do, be liberal in what you accept from others. In practice: emit output that strictly adheres to the specification, but accept input in a wider variety of formats and be forgiving of deviations.

## When It Applies

- Parsing JSON or XML responses from external systems that may not be perfectly spec-compliant; accept extra fields, tolerate minor format variations, strip whitespace.
- Designing an API client that needs to work with multiple versions of an upstream service; accept fields the spec does not require, ignore unknown fields gracefully.
- Building a data importer or ETL system that must handle slightly malformed or inconsistent input from different sources.
- Setting boundaries between internal and external services, where you want resilience against third-party changes.

## When It Misleads

- When combined with Hyrum's Law: accepting a wide range of input formats means clients will depend on that leniency. Once you've been lenient, tightening validation becomes a breaking change.
- In security-critical contexts, where lenient input parsing can introduce vulnerabilities (e.g., XML external entity (XXE) attacks, prototype pollution in JSON).
- When the upstream system is under your control and you want to enforce a strict contract to catch errors early.
- In systems that aggregate or relay data, where silently accepting and passing along invalid input can corrupt downstream systems.

## Common Misuse

Misinterpreting "liberal input" as "accept anything" and building error handling that papers over real problems instead of diagnosing them. A parser that silently ignores a malformed required field is not being robust; it is hiding a signal. The rule works best when the acceptance is *explicit and intentional*, not accidental permissiveness.

## How Agents Use It

- **Embedded**: in API review or integration design lenses, as a step to distinguish between the strict output contract (what you guarantee) and the lenient input boundary (what you tolerate). Document the difference explicitly.
- **Sanity-gate**: on API or integration recommendations, ask: "Is our output specification strict enough?" and "Are we accepting input more broadly than we should, given security and data-integrity constraints?"
