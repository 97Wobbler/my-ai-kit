---
name: galls-law
display_name: Gall's Law
class: heuristic
underlying_class: native
domain: architecture
source: John Gall, *Systemantics* (1975)
best_for:
  - System design and complexity management
  - MVP and incremental delivery strategies
  - Risk assessment of greenfield projects
one_liner: "Complex systems evolve from working simple systems, not vice versa."
---

# Gall's Law

## The Rule

A complex system that works is invariably found to have evolved from a simple system that worked. The corollary: a complex system designed from scratch will fail.

## When It Applies

- Justifying an MVP or minimum viable product approach over a fully-featured launch. A simple feature set that ships and acquires real users will be a more stable foundation than an elaborate unreleased system.
- Explaining why microservices migrations should start with a working monolith, then split services incrementally, rather than attempting to design a service-oriented architecture up front.
- Evaluating the risk of a large greenfield project that attempts to design the "right" architecture without validating assumptions on real data and usage patterns.
- Arguing for iterative prototyping and early feedback over long design phases when the domain is novel or highly uncertain.

## When It Misleads

- When the simple system's constraints become a trap. If you build a monolith without considering scalability, later scaling becomes vastly harder than if you had designed for it earlier.
- In domains with high up-front complexity requirements (e.g., distributed systems, security-critical systems). Starting too simple can lock you into architectural decisions that are expensive to undo.
- When the "simple system" misses load, latency, or reliability requirements that only emerge in production. You cannot always iterate your way out of a fundamentally wrong design.
- If used as an excuse to defer all design thinking to "we'll figure it out later." Some architectural decisions are cheaper to make up front.

## Common Misuse

Using Gall's Law to justify infinite scope creep: "We started simple, so let's just keep adding features until it does everything." The rule is about *controlled evolution*, not unlimited accretion. The law also gets misapplied when teams build a simple system, ship it, and then declare "we're done designing" — they stop thinking about how to evolve it cleanly.

## How Agents Use It

- **Embedded**: in system design or architecture review lenses, as a step to validate whether complexity is being justified as necessary from the start, or whether iterative evolution is a more prudent path.
- **Sanity-gate**: when evaluating a large, ambitious design proposal, ask: "Could we ship a smaller, working version first and iterate? What assumptions would we validate by doing so, and what would we risk missing?"
