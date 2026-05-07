---
name: hanlons-razor
display_name: Hanlon's Razor
class: heuristic
underlying_class: native
domain: general
source: Robert J. Hanlon, aphorism (origin uncertain, popularized mid-20th century)
best_for:
  - incident post-mortems
  - cross-team conflict diagnosis
  - security incident triage
one_liner: "Explain by incompetence what can be attributed to incompetence rather than malice."
---

# Hanlon's Razor

## The Rule

Never attribute to malice that which is adequately explained by stupidity, incompetence, or ordinary human error.

## When It Applies

- Investigating a bug, incident, or regression where the first instinct is to assume sabotage or bad faith.
- Post-mortems where blame is hardening before diagnosis is finished.
- Cross-team conflicts where one side is reading the other as adversarial rather than misaligned or under-resourced.
- Security incidents where the initial theory is intentional compromise, but simpler explanations (forgotten credentials, misconfiguration, stale documentation) fit the evidence equally well.

## When It Misleads

- In genuinely adversarial contexts (active fraud, security attacks, politically motivated behavior). Hanlon's is a **default prior**, not a shield against evidence of intent.
- When the same "error" recurs predictably and benefits the same party, at which point the competence hypothesis starts carrying more weight than the error hypothesis.
- When applied to exonerate a system: "nobody intended this" does not absolve a process or architecture that produced the outcome reliably.
- In regulated or safety-critical domains, where intent is relevant to liability but negligence carries the same consequences; Hanlon's can become a way to avoid accountability for systemic failures.

## Common Misuse

Confusing "assume good faith" with "assume no responsibility." The heuristic addresses *attribution of motive*, not *allocation of accountability*. A mistake can be genuinely negligent and still merit investigation, correction, and consequences.

Also commonly weaponized in reverse: "of course they intended it" becomes "of course they're incompetent," both evading the actual diagnosis. The rule works only when you are actually testing the hypotheses against evidence, not using it as a rhetorical trump card to shut down investigation.

## How Agents Use It

- **Sanity-gate**: before escalating a finding as intentional wrongdoing or malicious behavior, ask whether a plain mistake, missing context, under-resourcing, or misaligned incentives would explain the same facts equally well. If yes, test the competence/error hypothesis first.
- **Embedded** (optional): in incident-response and post-mortem lenses, apply Hanlon's as a mandatory step before any "intentional" or "bad faith" classification is recorded in the final report.
