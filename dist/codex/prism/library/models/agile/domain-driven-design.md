---
name: domain-driven-design
display_name: Domain-Driven Design
class: model
underlying_class: native
domain: agile
source: Eric Evans, Domain-Driven Design: Tackling Complexity in the Heart of Software, Addison-Wesley, 2003
best_for:
  - Structuring large software systems to match business domains and reduce accidental complexity
  - Predicting where communication breakdowns and integration failures will occur in multi-team codebases
  - Deciding how to partition a monolith or coordinate microservices along domain boundaries
one_liner: "Reflect the business domain model in code structure to manage complexity and improve team communication."
---

# Domain-Driven Design

## Overview

Domain-Driven Design (DDD) claims that the primary source of software complexity is not technical but *linguistic and organizational*: teams build wrong systems because they misunderstand the business domain, or because the business domain is encoded differently in different parts of the codebase. DDD's solution is to make the domain model explicit, shared, and the driver of code structure. The model is both descriptive (explaining why certain codebases succeed or fail) and prescriptive (how to organize and communicate to reduce failure modes). It operates at the system-architecture level: applying it requires identifying domain boundaries, designing a shared language, and structuring code to reflect domain concepts rather than technical convenience.

## Core Variables and Relationships

Domain-Driven Design works through three linked mechanisms:

1. **Ubiquitous Language (UL)** — a shared vocabulary between domain experts and engineers.
   - **Presence and consistency**: Is there a single, agreed name for each business concept across code, tests, documentation, and conversation?
   - **Drivers of UL quality**: Frequency of domain expert–engineer collaboration, whether code variable names match business terms, presence of written glossaries or domain models.
   - **Effect**: Shared language → fewer misinterpretations → faster feature delivery and fewer rework cycles. Fragmented language → silent bugs, false agreement, high-cost refinement loops.

2. **Bounded Contexts** — explicit boundaries within which a single UL applies, and clear contracts at the boundaries.
   - **Boundary definition**: Physical (separate services), organizational (separate teams), or logical (separate code modules within a service).
   - **Drivers of boundary clarity**: Are different teams responsible for different domains? Do different business processes use the same term to mean different things (e.g., "Order" means different things in Sales vs. Fulfillment)?
   - **Context mapping**: Are the translation layers and dependencies between contexts explicit and versioned?
   - **Effect**: Clear contexts + well-defined contracts → teams can work independently. Fuzzy boundaries + implicit assumptions → cross-context bugs, breaking changes, coordination overhead.

3. **Aggregates** — cohesive groups of domain objects that form a consistency boundary and are manipulated as a unit.
   - **Aggregate design**: Does the aggregate capture the true business invariants? Are relationships within the aggregate strong (transactional) and relationships across aggregates weak (eventual consistency)?
   - **Drivers of aggregate correctness**: Understanding of business rules and transaction requirements, willingness to tolerate eventual consistency.
   - **Effect**: Well-designed aggregates → predictable consistency, easier testing, fewer deadlocks. Poorly designed aggregates (too large, wrong boundaries) → distributed transactions, consistency bugs, performance problems.

The three mechanisms interact: **Ubiquitous Language determines the entities and relationships that define Aggregates, which are organized into Bounded Contexts.** When all three are aligned, the codebase becomes a *direct model of the business domain*, and feature changes that are simple in business terms are simple in code terms. When they drift apart, cost and defect rate rise sharply.

## Key Predictions

- **Organizational structure predicts code structure.** If Sales, Fulfillment, and Finance are separate teams using different terminology, a monolith will accumulate three tangled linguistic layers. Separating into bounded contexts (whether services or modules) with explicit contracts brings code structure into alignment with org, reducing friction.

- **Silent semantic divergence leads to high-cost bugs.** When the same term (e.g., "Customer") is used in different contexts with different meanings (one team means "account holder," another means "user of the product"), integration bugs emerge late and require expensive rework — UL forces these divergences into the open early.

- **Poorly bounded aggregates drive consistency nightmares.** If an aggregate spans an inconsistency boundary (e.g., trying to maintain a transactional invariant that requires coordinating across organizational silos), the system will exhibit deadlocks, retry loops, and silent invariant violations. Redesigning the aggregate boundary often resolves the issue.

- **Mismatch between code layer and domain layer accelerates technical debt.** A codebase organized by technology (controllers, services, repositories) rather than domain concepts (Orders, Payments, Shipments) makes it hard to follow a business requirement through code and easy to miss implications — new team members onboard slower, feature velocity decreases.

- **Explicit context mapping prevents contract creep.** When context boundaries are implicit or unenforced, consumers gradually make undocumented assumptions about inputs and side effects. Explicit anti-corruption layers or event-based contracts make these assumptions visible and versionable.

## Application Procedure

Instantiate DDD against a concrete software system or proposed architecture.

1. **Define the business domain(s)** at a level one step up from implementation. What are the core business processes? Do any terms have different meanings in different processes or teams? Write them down — this is the beginning of UL.

2. **Identify candidate Bounded Contexts** by asking: Which teams own which responsibilities? Where would a business term need translation? Map the current org structure and the current code structure — are they aligned?

3. **For each context, design or audit the Ubiquitous Language** by walking through:
   - A recent feature request or bug report. Can you trace it from business statement to code variable names without translation? Do synonyms exist in different parts of the system?
   - Are domain experts and engineers using the same words in meetings and in code? If not, explicitly agree and rename code.

4. **For each bounded context, identify the main Aggregates** by asking: What are the true consistency boundaries in the business logic? Which objects must be updated together in a transaction?
   - If an aggregate spans multiple organizational teams or requires coordination across services, it is likely mis-bounded. Redesign by moving the boundary so consistency is local.

5. **Document the contracts between contexts.**
   - What information flows between contexts? Is it pull (queries) or push (events)? Is versioning explicit?
   - If contexts communicate via a shared database table or request–response with implicit schema assumptions, there is implicit coupling; make it explicit and versionable.

6. **Audit code structure for domain alignment.**
   - Can a new engineer understand a feature by reading the code top-to-bottom, following domain entities and aggregates?
   - Do folder/module names match domain concepts, or do they reflect technical layers (controllers, utils)?

7. **Check boundary conditions** (below). If any apply, note what complementary modeling is needed.

8. **Generate recommendations:**
   - Which contexts need explicit contract definition or anti-corruption layers?
   - Which aggregates are mis-bounded and should be redesigned?
   - Which code refactorings would bring structure into alignment with business?
   - Where should UL be formalized (written glossaries, renaming)?

## Boundary Conditions

Domain-Driven Design is optimized for software systems with a clear, well-understood business domain and cross-functional collaboration. It is less applicable or requires modification in these cases:

- **Highly exploratory or research-driven software** where the domain itself is being discovered, not executed. DDD assumes you can articulate the domain; in early-stage exploration, the domain is fluid, and investing in precise aggregates and context contracts is premature. Complement with evolutionary or exploratory patterns.

- **Data-integration or ETL-heavy systems** where the problem is not domain modeling but schema translation and data pipeline choreography. DDD's notion of aggregates assumes mutable business entities; in pure data plumbing, use data-catalog and schema-versioning models instead.

- **Small, single-team systems** with minimal domain complexity and low personnel churn. The cost of DDD (explicit contexts, formal contracts, glossaries) may exceed the communication cost it prevents. DDD is an investment in scaling cognition; its ROI is highest in large systems or high-churn environments.

- **Real-time systems with extreme latency constraints**, where the consistency assumptions underlying aggregate design (e.g., eventual consistency between contexts) conflict with tight latency SLAs. Supplement with real-time data-structure and consistency-model analysis.

- **Systems with external or regulatory domain models** (e.g., banking, healthcare, insurance) where the domain model is partially imposed by regulation rather than discovered through collaboration. DDD works best when the team has agency to shape the domain model; when domain model is externally defined, use compliance and validation models alongside DDD.

- **Distributed or collaborative editing scenarios** where the same aggregate may be modified by multiple agents concurrently (e.g., real-time collaboration tools). Aggregate boundaries assume exclusive ownership; in concurrent-edit contexts, use CRDT or operational-transform models instead.

## Output Format

```
## Domain-Driven Design Analysis: <system name>

**System boundary:** <one-sentence scope: what is the software system?>
**Current org structure:** <teams, their domains, their responsibilities>

### Ubiquitous Language audit
| Domain concept | Current term(s) in use | Synonyms or ambiguity | Unified term (proposed) |
|---|---|---|---|
| ... | ... | ... | ... |

### Bounded Contexts
| Context name | Owner | Current boundaries (code/org) | Clarity (clear/fuzzy/mixed) | Key contracts |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

### Aggregates (per context)
**Context: <name>**
- Aggregate: <name> — consistency boundary, key invariants, relationships to other aggregates (cross-context ref or event-based)
- Aggregate: <name> — ...

### Context mapping
| From context | To context | Interaction type | Contract clarity | Risk |
|---|---|---|---|---|
| ... | ... | Query / Event / Shared table | Explicit / Implicit | High / Med / Low |

### Key structural issues
- <Misalignment between org and code structure>
- <Aggregate mis-boundary or consistency problem>
- <Implicit UL divergence or hidden synonyms>
- <Unmapped context dependency or contract ambiguity>

### Recommendations
- **UL improvements:** <Renames, glossary, domain workshops>
- **Context design:** <Proposed boundaries, anti-corruption layers, contract formalization>
- **Aggregate redesign:** <Specific aggregates to split, merge, or rebound>
- **Code structure:** <Module organization, folder naming, to align with domain>

### Boundary-condition check
<Which boundary conditions apply and what complementary modeling is needed>

### Confidence: high | medium | low
<Reasoning: UL clarity + team alignment + aggregate complexity + org stability + domain-model maturity>
```
