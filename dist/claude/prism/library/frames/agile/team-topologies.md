---
name: team-topologies
display_name: Team Topologies
class: frame
underlying_class: native
domain: agile
source: Matthew Skelton & Manuel Pais, "Team Topologies", O'Reilly, 2019
best_for:
  - Sorting an organizational unit or team by its primary interaction mode and flow of work
  - Diagnosing misalignment between team structure and the architecture/dependencies they manage
one_liner: "Classify teams into four types — stream-aligned, platform, complicated-subsystem, enabling."
---

# Team Topologies

## Overview

Team Topologies sorts teams into four fundamental types based on their primary purpose, the work they own, and the kind of interaction they have with other teams. Its core claim is that **team structure constrains system architecture and communication patterns** — and organizational structures that misalign team boundaries with value streams, platform capabilities, or architectural concerns create friction, handoffs, and misunderstood dependencies. Selecting the right team type for a mission is a structural intervention that cascades into which tools, processes, and communication patterns are appropriate.

## Categories

1. **Stream-aligned Team**
   - Owns a **vertical slice of the business capability** from end to end.
   - Responsible for the full delivery pipeline of a specific customer value stream or product feature.
   - Discriminating criterion: can deliver a user-visible outcome autonomously without needing approval, handoff, or synchronous coordination with other feature teams.
   - Example: a team responsible for the checkout flow in an e-commerce system, including backend, frontend, database, and operations; a team owning a specific feature set for a SaaS product.

2. **Platform Team**
   - Owns a **shared capability or infrastructure** that reduces friction for Stream-aligned teams.
   - Provides tools, abstractions, or services (CI/CD, observability, authentication, networking) that enable other teams to move faster.
   - Discriminating criterion: success is measured by how much cognitive load it removes from Stream-aligned teams, not by how much it builds.
   - Example: a DevOps team that owns the deployment pipeline and observability stack; a team that provides a shared API or data catalog.

3. **Complicated-Subsystem Team**
   - Owns a **narrow, deeply specialized domain** where significant expert knowledge is required.
   - Responsible for a single subsystem that is either algorithmically complex, legally/compliance-critical, or requires rare expertise.
   - Discriminating criterion: a Stream-aligned team could not reasonably absorb this work without losing velocity; the subsystem cannot be reasonably simplified into a platform.
   - Example: a team owning a machine-learning model training pipeline; a team responsible for PCI-DSS compliance and payment processing; a team managing a real-time bidding engine.

4. **Enabling Team**
   - Owns **no permanent product or infrastructure**, but provides coaching, guidance, and temporary help to other teams.
   - Exists to reduce barriers, spread knowledge, or unblock organizational impediments.
   - Discriminating criterion: success is that the team makes itself unnecessary — when the blocking pattern is solved or knowledge is diffused, the team redeploys or dissolves.
   - Example: a team that coaches Stream-aligned teams on microservices practices; a team that builds proof-of-concept work to validate a new approach; an internal DevX team that improves developer experience and removes friction.

## Classification Procedure

1. **Identify the unit to classify.** Name the team and describe the work it owns or is being asked to own.

2. **Ask: Does this team own a complete, end-to-end value stream?**
   - If **yes** → Stream-aligned. Go to step 5.
   - If **no**, go to step 3.

3. **Ask: Is this team building a permanent, reusable capability that reduces friction for other teams?**
   - If **yes** → Platform. Go to step 5.
   - If **no**, go to step 4.

4. **Ask: Is this team responsible for a narrow, deeply specialized domain requiring rare expertise, where the subsystem cannot be simplified into a platform?**
   - If **yes** → Complicated-Subsystem. Go to step 5.
   - If **no** (the work is temporary, advisory, or aimed at spreading knowledge) → Enabling.

5. **Validate the classification against organizational context.** Check whether the team's actual interactions, communication lines, and autonomy match the expected pattern for its category (e.g., a Stream-aligned team should not be routinely blocked on approvals from other feature teams).

6. **Name the specific implications** for the team's charter, metrics, and expected interactions (see Implications below).

## Implications per Category

| Category | Expected interaction pattern | What the organization should do |
|---|---|---|
| **Stream-aligned** | Async interaction with other stream teams via APIs/contracts; synchronous with their own domain experts. | Minimize handoffs. Size teams for cognitive load (6–9 people). Align team boundaries to customer journeys or product areas, not technical layers. Measure by flow/delivery metrics. |
| **Platform** | Provide self-service capabilities and documentation; engage Stream-aligned teams as primary users and co-designers. | Treat as internal product with a paying user base (Stream-aligned teams). Measure by adoption, reduction in toil, and velocity of teams using the platform. Avoid over-building. |
| **Complicated-Subsystem** | Owned by specialists; interact with Stream-aligned teams via well-defined interfaces. Isolate complexity behind abstractions. | Fund deep expertise; resist pressure to "productize" the subsystem into a platform prematurely. Clarify whether the subsystem can eventually migrate to Platform. |
| **Enabling** | Temporary, collaborative relationships with other teams. Must have a clear **exit criteria** or redeploy plan. | Measure by problem solved or knowledge transferred, not by lines of code. Set sunset dates. Resist permanent enablement teams — they often hide unaddressed organizational friction. |

## Common Misclassifications

- **Stream-aligned teams that are actually layer-based siloes.** A team owns "the API layer" for multiple value streams instead of owning a complete slice of one stream. The tell: the team is a bottleneck and cannot move without waiting for other teams to define their interfaces. Solution: restructure around value streams, not layers.

- **Platform teams that don't reduce cognitive load.** The team builds infrastructure that Stream-aligned teams still have to fight with, or over-engineers abstractions no one uses. The tell: Stream-aligned teams bypass the platform and build their own tooling. Solution: measure by actual adoption and feedback; stop building until the platform is easier than the alternative.

- **Complicated-Subsystem mistaken for Stream-aligned.** The team owns a hard domain but it could be simplified into a reusable platform for other teams. The tell: multiple teams are reimplementing the same specialized work. Solution: graduate to Platform or provide better abstraction.

- **Enabling team with no exit date.** An Enabling team never transfers knowledge or solves the blocking problem, and becomes a permanent support function. The tell: the same Enabling team is coaching the same Stream-aligned teams a year later with no visible change. Solution: set explicit completion criteria at team inception.

- **Classifying the whole organization as Stream-aligned.** Flatly reorganizing everything into independent feature teams without Platform or Complicated-Subsystem teams often pushes infrastructure and shared concerns downward, fragmenting expertise and duplicating effort. The tell: high toil, many teams rebuilding the same infrastructure, security/compliance violations. Solution: ensure Platform and specialized teams exist before pushing all delivery to Stream-aligned teams.
