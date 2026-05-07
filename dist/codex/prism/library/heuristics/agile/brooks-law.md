---
name: brooks-law
display_name: Brooks's Law
class: heuristic
underlying_class: native
domain: agile
source: Frederick P. Brooks, The Mythical Man-Month, 1975
best_for:
  - staffing decisions on delayed projects
  - team communication analysis
  - schedule estimation and re-planning
  - resource allocation discussions
one_liner: "Adding manpower to a late software project makes it later."
---

# Brooks's Law

## The Rule

Adding human resources to a delayed software project decreases productivity and extends the schedule rather than accelerates it.

## When It Applies

- A project is weeks or months behind schedule and leadership proposes hiring more developers or contractors to "catch up."
- A team needs to onboard new engineers mid-project and is asking whether the immediate context-switching cost is worth the eventual extra hands.
- Estimating the penalty of late hiring: new staff require knowledge transfer, pair programming, code review feedback, and async clarification—all adding latency to existing team members.
- Quantifying team communication overhead: with n people, there are n(n-1)/2 communication paths (n=5 → 10 paths; n=10 → 45 paths; n=20 → 190 paths).
- Understanding why Little's Law (L = λ × W) predicts schedule slippage: adding people increases WIP (work in progress) without proportionally increasing throughput, so lead time (W) grows even though you added capacity (λ).

## When It Misleads

- Assuming that *all* additions of headcount cause delays. Onboarding a junior engineer onto a healthy, well-documented codebase with strong pair-programming culture can add value within weeks rather than drain it.
- Treating the law as absolute. Some contexts—greenfield projects with clear interfaces, high test coverage, or existing architectural stability—allow new hires to become productive faster.
- Ignoring the *timing* of hiring. Bringing in staff early (at project start) is often less harmful than mid-crisis hiring. Early hires grow with the project; mid-crisis hires must catch up from scratch.
- Misapplying the law to justify understaffing: "We're already late, so adding people won't help—let's just work longer hours." This conflates two different problems (late schedule vs. insufficient headcount).

## Common Misuse

Invoking Brooks's Law as a blanket excuse to freeze hiring when a project is genuinely understaffed due to attrition or scope growth. The law does not say "never add staff"; it warns that *unplanned* additions to a *failing* project create organizational friction. A more nuanced response is: restructure the work to reduce communication overhead (split into smaller teams with clearer boundaries) or reduce scope rather than add raw headcount to a tangled project.

Another misuse: ignoring the distinction between Fred Brooks's original context (IBM OS/360, massive fixed scope, pre-internet communication) and modern environments (distributed teams, async-first tools, code review automation). The underlying math—communication paths grow as O(n²)—remains, but the friction coefficient has changed.

## How Agents Use It

- **Embedded**: in retrospectives and staffing reviews, as a step to ask: "When we added headcount last quarter, what was the actual onboarding penalty vs. the productivity gain? Are we in a regime where hiring made things worse, or did we manage communication well enough to make it work?"
- **Sanity-gate**: when a PM proposes adding 3 engineers to a 6-month-delayed project, apply the heuristic to estimate ramp-up friction. Ask: "What is the current n(n-1)/2? After adding 3, it doubles. Can we split the team structure to lower that, or reduce scope instead?" 
- **Context-specific signals**:
  - Code review bottleneck: if adding people creates more PRs than reviewers can handle, you've hit the communication ceiling.
  - Architectural instability: if the system has few agreed-upon interfaces, new hires cause thrashing.
  - Test coverage: if coverage is high and CI is fast, onboarding friction is lower.
  - Deadline flexibility: if you can extend the deadline by 3 weeks, hiring may make sense; if you cannot, focus on scope reduction.

Related principle: Little's Law (L = λ × W) quantifies the penalty. In many delayed projects, W (lead time per task) is already high due to communication latency; adding λ (throughput in headcount) only increases L proportionally unless you reduce W through better processes.
