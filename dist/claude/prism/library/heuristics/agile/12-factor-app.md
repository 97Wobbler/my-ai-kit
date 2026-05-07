---
name: 12-factor-app
display_name: 12-Factor App Principle
class: heuristic
underlying_class: native
domain: agile
source: Adam Wiggins, Heroku, 2011
best_for:
  - cloud-native application design
  - deployment and operations planning
  - codebases migrating to managed platforms
one_liner: "Structural discipline for deployable, scalable apps — separate config, explicit dependencies, stateless processes."
---

# 12-Factor App Principle

## The Rule

Design applications by treating the codebase, configuration, dependencies, and stateless processes as separate, independently deployable units that scale horizontally without re-architecture.

## When It Applies

- Evaluating whether an application can move safely from development to cloud-hosted environments (Heroku, Kubernetes, managed platforms).
- Assessing whether a codebase will survive horizontal scaling or load-balancing without session affinity hacks.
- Planning operational changes: environment variables, secrets management, and configuration separation.
- Reviewing monolithic applications that are showing deployment friction or coupling between compute and state layers.
- Designing multi-tenant or SaaS systems where reproducible builds and independent scaling are non-negotiable.

## When It Misleads

- In systems where state affinity is genuinely unavoidable (certain graph algorithms, stateful protocols, game servers with client connections). 12-Factor assumes statelessness is always achievable; sometimes it is not.
- For legacy or domain-specific applications where the cost of retrofitting 12-Factor discipline exceeds the operational gain (internal tools, single-instance batch processors, embedded systems).
- When "stateless by the framework" obscures the real state problem. A stateless HTTP layer that writes to a database is still carrying state; 12-Factor does not solve the database scaling problem, only moves it.
- In organizations where the deployment target is fixed and singular (on-premise, appliance, single data center). The principle's value is the optionality it preserves; if optionality is not valuable, the cost of discipline is wasted.

## Common Misuse

Teams cite 12-Factor as a design goal and then ignore the configuration-separation principle, baking environment-specific settings into code or configuration files that are committed to version control. The principle is hollow without genuine externalization of config (environment variables, config servers, secrets vaults). 

Another common failure is treating 12-Factor as a checklist for "cloud-readiness" without understanding the underlying constraint: if you want to scale horizontally, add instances without redeploy, and survive infrastructure churn, stateless design is not optional. Checklist compliance without that alignment is cargo cult.

## How Agents Use It

- **Embedded**: in cloud-migration or deployment-design lenses, as a mandatory architecture review step. Check each of the 12 factors explicitly; flag any that are violated and assess whether the violation is intentional and justified.
- **Sanity-gate**: for any production architecture recommendation, ask: "Can we run two instances of this application side-by-side, pointed at the same backing services, with no session affinity or shared local state?" If the answer requires qualification or workaround, identify which 12-Factor principles are being bent and whether that bend is load-bearing.
