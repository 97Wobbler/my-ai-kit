---
name: chestertons-fence
display_name: Chesterton's Fence
class: heuristic
underlying_class: native
domain: general
source: G. K. Chesterton, The Thing, 1929
best_for:
  - refactoring and simplification decisions
  - process or policy elimination
  - schema or configuration cleanup
one_liner: "Do not remove a rule whose purpose you do not yet understand."
---

# Chesterton's Fence

## The Rule

Before removing a rule, structure, or process, find out why it exists; do not destroy what you do not yet understand.

## When It Applies

- Refactoring code with branches, flags, or error handlers marked as "dead" or "never executed."
- Removing process steps, approval gates, or review stages that feel like bureaucratic overhead.
- Simplifying schemas, configuration, or APIs by dropping fields that appear unused.
- Deleting legacy code or deprecated features when no obvious client depends on them.

## When It Misleads

- As an absolute veto: "you cannot change anything until you document every fence." That paralyzes necessary work and shelters genuine dead weight.
- When the cost of preserving the fence is concrete and demonstrable, and the original threat it guarded against is verifiably gone. The heuristic is a pause, not a permanent bar.
- In adversarial or expired contexts, where the fence was built to serve interests opposed to your own or by a regime that no longer exists. Understanding the purpose does not obligate you to preserve it.
- When the fence was put up by accident, without intent, and serves no function beyond historical habit — the absence of purpose is itself the discovery.

## Common Misuse

Treating "I ran git blame and found a commit from 2018" as "I investigated the fence." The heuristic is satisfied only when you understand *why* the fence was built, not merely that *someone* built it. Many engineers mistake archaeology (finding the commit) for archaeology (learning the context). A second common misuse is citing Chesterton's as a permanent restraint on refactoring, when it is actually a checklist item: once you understand the purpose, you are free to weigh whether removing the fence is worth the risk.

## How Agents Use It

- **Embedded**: in refactoring, simplification, and deprecation lenses, as a mandatory check-step before any deletion recommendation. The agent must explicitly state the fence's original purpose or flag that the purpose is unknown and cannot be determined.
- **Sanity-gate**: on each "remove X" finding, force the agent to articulate X's original purpose and the confidence level in that understanding. If confidence is low, require either deeper investigation or a risk-mitigation plan for removal.
