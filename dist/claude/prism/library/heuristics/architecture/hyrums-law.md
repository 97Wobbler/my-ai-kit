---
name: hyrums-law
display_name: Hyrum's Law
class: heuristic
underlying_class: native
domain: architecture
source: Hyrum Wright, popularized in *Software Engineering at Google* (~2012)
best_for:
  - API stability and compatibility analysis
  - Breaking-change impact assessment
  - Library versioning decisions
one_liner: "API users depend on observable behavior, not just the spec."
---

# Hyrum's Law

## The Rule

With a sufficiently large number of API users, every observable behavior of your system will be depended upon by someone, regardless of whether it is documented as part of the contract.

## When It Applies

- Deciding whether a seemingly minor change to an internal library is safe to ship (e.g., reordering fields in a JSON response, changing error message text, adjusting timing or latency characteristics).
- Evaluating the impact of a critical bug fix that changes previously incorrect behavior that clients may have relied on.
- Designing new public APIs or library interfaces where you anticipate high adoption.
- Justifying strict backwards compatibility commitments even when the original design had flaws.

## When It Misleads

- In closed, single-team systems where you control all callers. If your API has only five internal users and you've audited all five, the rule loses its bite.
- Early in a product's lifecycle, before significant adoption. The dependency tax is paid only after enough users accumulate.
- When applied as an absolute blocker to improvement. The law identifies a real cost, not a veto; sometimes breaking changes are justified if the burden is transparent and users get reasonable migration time.
- In domains with short product lifespans or fast-moving standards, where stability commitments carry less weight.

## Common Misuse

Treating Hyrum's Law as a reason to never fix bugs or improve APIs. The real pattern is: once users exist, *any* observable change incurs communication and migration cost. The heuristic is a reminder to measure that cost, not to forbid all change. Another misuse: surprising users with undocumented incompatible changes and then invoking the law as justification ("they shouldn't have relied on that").

## How Agents Use It

- **Embedded**: in API review or system design lenses, as a step to identify which behaviors are observable and therefore likely to be depended upon. For each proposed change, ask: "Which observable behaviors does this alter, and who might depend on them?"
- **Sanity-gate**: before approving a change framed as "internal only" or "undocumented, so safe," require explicit evidence that the affected surface has no external callers or that migration cost has been estimated.
