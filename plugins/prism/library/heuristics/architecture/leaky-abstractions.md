---
name: leaky-abstractions
display_name: Law of Leaky Abstractions
class: heuristic
underlying_class: native
domain: architecture
source: Joel Spolsky (2002)
best_for:
  - Framework and abstraction layer evaluation
  - Performance debugging and optimization
  - Technology selection and risk assessment
one_liner: "All non-trivial abstractions leak — plan for when they break."
---

# Law of Leaky Abstractions

## The Rule

Abstractions that hide complex underlying systems will inevitably leak details. When they do, the person trying to use the abstraction is forced to understand the underlying system anyway, negating the value of the abstraction.

## When It Applies

- Selecting an ORM for a data-heavy application. The abstraction promises to hide SQL, but query performance problems force you to read the generated SQL and understand database internals.
- Evaluating garbage collection as an abstraction over manual memory management. The GC pause times and tuning parameters become visible constraints when your system has latency requirements.
- Assessing a cloud service that abstracts away infrastructure details; when a service dependency fails or behaves unexpectedly, you must understand the underlying system to diagnose it.
- Predicting technical debt in a codebase that relies heavily on opaque framework magic; the more the framework tries to hide, the more painful debugging becomes.

## When It Misleads

- Treating all abstraction as bad. Abstractions are essential; they just need to acknowledge their leakiness and provide escape hatches.
- Assuming that because an abstraction is imperfect, you should reject it entirely and build a lower-level solution. The lower level leaks differently and may be harder to debug.
- In very simple, low-scale systems where the abstraction genuinely does hide all the messy details and you never need to think about the underlying layer.
- When the leak is so rare or extreme that planning for it is not cost-effective.

## Common Misuse

Choosing an abstraction based on marketing claims alone without testing it against your actual use case. The law is not an absolute condemnation; it is a call to be realistic about what abstractions hide and what they reveal. A common misuse is blaming the abstraction for leaking without first investigating whether you chose it for the wrong reason.

## How Agents Use It

- **Embedded**: in technology selection or framework evaluation lenses, as a step to identify the likely leak points of an abstraction and the expertise required to debug when it fails.
- **Sanity-gate**: on framework or abstraction recommendations, require explicit documentation of the escape hatch: "If this abstraction leaks, how do we diagnose and recover? What underlying system knowledge is required?"
