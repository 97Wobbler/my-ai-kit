---
name: conways-law
display_name: Conway's Law
class: heuristic
underlying_class: native
domain: agile
source: Melvin Conway, 1968
best_for:
  - system architecture review
  - org restructuring impact analysis
  - cross-team integration failures
one_liner: "Organizational structure determines system structure."
---

# Conway's Law

## The Rule
The structure of a system reflects the structure of the organization that designed it.

## When It Applies
- Diagnosing why a monolithic codebase has siloed components that don't interact well — the teams that own them likely sit in separate reporting chains.
- Predicting integration friction between services built by teams with poor communication paths or no shared ownership model.
- Explaining why a "designed-for-modularity" architecture failed in practice — the org chart didn't match the intended module boundaries.
- Justifying a team restructure as a prerequisite to a technical refactor, not just a management move.

## When It Misleads
- Treating org structure as the *only* determinant of system structure. Individual engineers, strong technical leadership, and explicit architectural decisions do push back against org gravity — they just require constant effort to maintain.
- In early-stage or exploratory work where the org has not yet stabilized. The rule is stronger once patterns have time to settle in.
- As an excuse to reorganize every time a system architecture problem appears. The org chart is *one* lever, not a cure-all; many technical problems are cheaper to solve with code than with reorganization.
- When applied backward: assuming that because a system *looks* modular, the org *must be* aligned. Modular systems can emerge from misaligned orgs through heroic effort, or be built by tiny teams, or evolve differently than their creators intended.

## Common Misuse
Citing Conway's Law to justify a reorganization without actually analyzing which parts of the system are suffering from poor communication or duplicate work. The heuristic diagnoses a *symptom*, not a *remedy*. A common pattern is to reorganize around the current system structure, then find that the system structure was actually wrong — now the org is locked in place, enforcing the mistake.

Another misuse: treating the law as deterministic. It is a strong tendency, not an iron rule. Well-managed teams with explicit cross-team architecture, clear interfaces, and strong communication can deviate from it.

## How Agents Use It

- **Embedded**: in architecture review or system design lenses, as a step to validate whether team communication paths align with the proposed module boundaries. If they don't, flag the risk of drift or integration friction.
- **Sanity-gate**: when evaluating a recommendation to refactor or modularize a system, ask: "Have we also restructured the teams that will own these modules, or are we asking the org chart to fight the system design?" If the answer is "the org chart will fight it," either revise the architecture to match the existing org, or note that the refactor will require continuous active management to prevent it from drifting.
