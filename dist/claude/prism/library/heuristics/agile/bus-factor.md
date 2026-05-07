---
name: bus-factor
display_name: Bus Factor
class: heuristic
underlying_class: native
domain: agile
source: Folklore, popularized in Extreme Programming and agile communities
best_for:
  - knowledge transfer planning
  - risk assessment in critical systems
  - code review strategy
  - onboarding and documentation priorities
one_liner: "What is the minimum number of team members whose departure would catastrophically cripple the project?"
---

# Bus Factor

## The Rule

The bus factor (or truck factor) is the minimum number of team members whose sudden departure—via a bus accident, illness, resignation, or other unforeseeable event—would leave the project in a critically damaged state due to lost knowledge.

A bus factor of 1 indicates a single point of failure: one person holds essential knowledge that no one else possesses.

## When It Applies

- Identifying critical knowledge bottlenecks: "If Alice quit tomorrow, would we be able to deploy the payment system?"
- Prioritizing documentation and cross-training efforts: systems with a bus factor of 1 should receive the most attention for knowledge sharing.
- Assessing organizational risk: a startup where the principal architect is the only person who understands the database schema faces existential risk.
- Planning code review practices: if only one senior engineer reviews security-critical code, you have a bus factor of 1 for that domain.
- Deciding whether to allow solo on-call rotations: a system where only one person knows how to respond to a specific outage is unsafe.

## When It Misleads

- Treating bus factor as the sole measure of knowledge distribution. Two people knowing something doesn't guarantee they can both execute it; one may be on parental leave, in a different time zone, or away during an incident.
- Assuming documentation alone raises the bus factor. Written docs can become stale, outdated, or incomplete. The person who wrote them must stay involved in enough reviews to keep the knowledge current.
- Over-investing in spreading knowledge to those who don't have capacity to maintain it. A junior engineer may understand the codebase better after pairing with the expert, but may not have the judgment to respond to production incidents.
- Ignoring that bus factor varies by criticality. It may be acceptable for the bus factor of a toy project to be 1; for a revenue-generating system, it should be at least 2, and ideally 3.

## Common Misuse

Treating bus factor as a fixed number rather than a dynamic measure per subsystem. The overall project may have a healthy bus factor of 3, but the database migration code, the payment webhook handler, and the Kubernetes cluster config each have a bus factor of 1 due to specialist knowledge. Mitigating the overall metric without addressing the subsystem-level risk is false confidence.

Another misuse: conflating bus factor with seniority. Promoting the junior engineer to "share knowledge" without actually building a culture of pair programming, code review, and async knowledge sharing only spreads shallow understanding. When the expert is needed, the junior is still dependent.

## How Agents Use It

- **Embedded**: in code review and onboarding lenses, as a step to flag: "Does any one person hold exclusive knowledge of this critical path? If yes, pair with a second person or create explicit documentation + video walkthrough before merging."
- **Sanity-gate**: when evaluating a major refactor or migration, ask: "For each new or modified critical component, what is the bus factor? Is it acceptable for our risk tolerance?" If any critical path drops to 1, reject the plan until knowledge sharing is designed in.
- **Staffing decisions**:
  - If the bus factor of a critical subsystem is 1, that person should be prioritized for mentoring, high-leverage work, and career growth (to reduce turnover risk).
  - If retention of one person is essential, invest in their development and satisfaction; otherwise, the project is brittle.
- **Tactical mitigations**:
  - Pair programming on critical code.
  - Mandatory code review by at least 2 people for the subsystem.
  - Runbooks and incident response docs kept up to date by the expert.
  - Annual "knowledge transfer sprints" where the expert trains others and steps back from doing it alone.
  - Rotating on-call duty so multiple people can respond to incidents.

A healthy bus factor for critical systems is 3+: any one person can leave, and the project remains functional (though possibly at reduced velocity while the second or third person ramps up).
