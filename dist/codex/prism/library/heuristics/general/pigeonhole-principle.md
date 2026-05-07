---
name: pigeonhole-principle
display_name: Pigeonhole Principle
class: heuristic
underlying_class: native
domain: general
source: Dirichlet, 1834
best_for:
  - capacity planning
  - collision analysis
  - scheduling constraints
one_liner: "If you put n items into n-1 boxes, at least one box must hold two or more."
---

# Pigeonhole Principle

## The Rule

If n items are placed into fewer than n containers, at least one container must hold more than one item.

## When It Applies

- Capacity-planning arguments ("we have 50 requests per second and 20 workers; at least some requests must queue").
- Scheduling and assignment reasoning where the number of tasks exceeds the number of available slots.
- Security and collision arguments: hash collisions, token collision space, birthday attacks.
- Proving lower bounds or impossibility results in any system with fixed slots and flowing volume.

## When It Misleads

- When the "containers" are not actually fixed. In elastic systems (auto-scaling, dynamic pools), the principle must be restated or does not apply to the steady state.
- When ignoring time, batching, or buffering. A queuing system may have 50 requests per second and 20 workers, but the pigeonhole count is an average rate, not a per-instant guarantee; requests can be batched, delayed, or dropped without violating the constraint.
- When the "items" are not discrete or countable in the assumed way. If 50 requests per second averages across 60 seconds, the per-second pigeonhole is different from the per-minute pigeonhole.
- When applied to probabilistic or statistical claims without care. "At least one collision is guaranteed" is a hard statement; "a collision is likely" requires different math.

## Common Misuse

The heuristic is quoted to foreclose debate ("it's mathematically impossible to avoid this") without identifying the pigeons and holes precisely. The rule is only as sharp as the counting. Agents often cite it without specifying: Are we counting per-instant or per-period? Are the containers truly fixed? Is the item count exact or a rate? Sloppy pigeonhole arguments collapse when these details are pressed.

## How Agents Use It

- **Embedded**: in capacity analysis, rate-limiting, and collision-risk assessments as a formal check step. After the constraint is stated, verify the pigeonhole count explicitly.
- **Sanity-gate**: when a finding claims "it can't possibly happen" or "we have enough capacity," test by constructing an explicit pigeonhole argument. If n items, m containers, and n > m are all defensible, the claim fails.
