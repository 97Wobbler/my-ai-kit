---
name: General-purpose Heuristics Bundle
domain: general
source: Assorted — see each entry for attribution
best_for: A sanity-gate bundle applied at the end of analysis to catch common reasoning failures across almost any domain
one_liner: "Bundle — Occam, Hanlon, Chesterton's Fence, Hickam, Pigeonhole, Pareto, Parkinson, Mise en Place."
---

# General-purpose Heuristics Bundle

This bundle contains ~8 domain-general heuristics suitable for use as a
**sanity gate** in the synthesize step of a lenslab analysis. Each entry
follows the standard heuristic template. Apply the whole bundle as a
quick final walkthrough on the top findings before finalizing
recommendations; do not use any single heuristic as a stand-alone verdict.

For per-heuristic format details see CLASSES.md § "Class 5 — Heuristic."

---

## Occam's Razor

**The Rule**
Among competing explanations that account for the same evidence, prefer
the one that requires the fewest additional assumptions.

**When It Applies**
- Choosing between rival hypotheses that all fit the observed data.
- Debugging, diagnosis, or root-cause analysis where an exotic theory
  is competing with a plain one.
- Evaluating proposed designs or architectures where one version
  introduces new moving parts to explain something a simpler version
  already handles.

**When It Misleads**
- The domain is genuinely complex and the simple story omits a
  load-bearing mechanism (medicine, ecosystems, socio-technical
  systems).
- "Simple" is being confused with "familiar." A solution is not simpler
  just because you've seen it before.
- The simple theory and the complex theory explain *different* bits of
  the evidence. Occam's is a tie-breaker between theories of equal
  explanatory scope — if the scopes differ, it does not apply.

**Common Misuse**
Using Occam's as a rhetorical weapon to dismiss hypotheses you don't
like, without actually enumerating the assumptions each hypothesis
requires. The heuristic is disciplined only when the assumption counts
are made explicit.

**How Agents Use It**
- **Embedded**: inside an ACH or root-cause lens, at the "eliminate
  hypotheses" step, after the assumption ledger is built.
- **Sanity-gate**: on each top finding, ask: "Is there a simpler
  explanation we didn't consider that would have covered the same
  evidence?"

---

## Hanlon's Razor

**The Rule**
Never attribute to malice that which is adequately explained by
stupidity, incompetence, or ordinary human error.

**When It Applies**
- Investigating a bug, incident, or regression where the first
  instinct is to assume sabotage or bad faith.
- Post-mortems where blame is hardening before diagnosis is finished.
- Cross-team conflicts where one side is reading the other as
  adversarial.

**When It Misleads**
- In genuinely adversarial contexts (security incidents, active
  fraud, politically motivated behavior). Hanlon's is a **default
  prior**, not a shield against evidence of intent.
- When the same "error" recurs predictably and benefits the same
  party, at which point the competence hypothesis starts carrying
  more weight than the error hypothesis.
- When applied to exonerate a system: "nobody intended this" does
  not absolve a process that produced the outcome reliably.

**Common Misuse**
Confusing "assume good faith" with "assume no responsibility." The
heuristic addresses *attribution of motive*, not *allocation of
accountability*.

**How Agents Use It**
- **Sanity-gate**: before escalating a finding as intentional
  wrongdoing, ask whether a plain mistake, missing context, or
  under-resourcing would explain the same facts equally well.

---

## Chesterton's Fence

**The Rule**
(G. K. Chesterton, The Thing, 1929.) Before removing a fence, find out
why the fence was put there. Do not destroy a rule or structure whose
purpose you do not yet understand.

**When It Applies**
- Refactoring code with "obviously dead" branches, flags, guards, or
  error paths.
- Removing process steps, approval gates, or policies that seem like
  bureaucratic overhead.
- Simplifying configuration, schemas, or APIs to drop fields that
  "no one uses."

**When It Misleads**
- As an absolute blocker: "you must understand why every fence exists
  or leave everything as-is." That paralyzes change and protects
  genuine dead weight.
- When the cost of preserving the fence is concrete and the purpose
  of the fence is obsolete (the original threat is gone). The
  heuristic is a pause, not a veto.
- In adversarial environments, where the fence was put up by someone
  whose interests are opposed to yours — the purpose may be clear and
  still worth removing.

**Common Misuse**
Treating "I couldn't find git-blame history" as "I investigated the
fence." The heuristic is discharged when you know *why* the fence
exists, not just that *someone* built it.

**How Agents Use It**
- **Embedded**: in refactoring or simplification lenses, as a
  mandatory step before any deletion recommendation.
- **Sanity-gate**: on each "remove X" recommendation, force the agent
  to state X's original purpose explicitly, or flag that the purpose
  is unknown.

---

## Hickam's Dictum

**The Rule**
(John Hickam, medical aphorism, mid-20th century.) "Patients can have
as many diseases as they damn well please." Where Occam's Razor
suggests preferring a single explanation, Hickam's says not to force
parsimony when multiple independent problems may be present.

**When It Applies**
- As a counterweight to Occam's Razor, specifically when:
  - The system has many components, any of which can fail
    independently (production systems, complex codebases, living
    bodies).
  - A single-cause story requires the "one cause" to be unusually
    convenient, large, or coincidental.
  - Evidence refuses to collapse into a single coherent story no
    matter how you arrange it.
- Triaging complex, multi-symptom incidents where pattern-matching
  on "the bug" drops important signals.

**When It Misleads**
- In genuinely simple situations with one obvious cause, where
  Hickam's becomes an excuse to add speculative secondary causes.
- When used to avoid committing to a diagnosis — "it could be
  many things" is not a useful finding.

**Common Misuse**
Treating "multiple independent causes" as a default whenever the
investigation is hard. Hickam's earns its keep when the evidence
actively resists a single-cause story, not whenever a single-cause
story is inconvenient.

**How Agents Use It**
- **Sanity-gate** (paired with Occam's): for each top finding framed as
  a single root cause, ask whether forcing a single-cause story
  requires downweighting evidence that points elsewhere. If yes, test
  the multi-cause alternative before finalizing.

---

## Pigeonhole Principle

**The Rule**
If n items are placed into fewer than n containers, at least one
container must hold more than one item. More generally: when constraints
force many things into few slots, collisions are guaranteed.

**When It Applies**
- Capacity-planning arguments ("we have 50 requests per second and 20
  workers; at least some requests must queue").
- Scheduling, assignment, and rate-limit reasoning.
- Security arguments about collisions in hashes, IDs, tokens.
- Any proof-by-contradiction that hinges on "there must exist at
  least one …"

**When It Misleads**
- Almost never on its direct terrain, but it is often misapplied by
  *ignoring slack, batching, or time*. In a queuing system with
  variable arrival, the pigeonhole count is an average, not a
  per-instant guarantee.
- When the "containers" are not actually fixed (elastic scaling)
  the argument must be restated carefully.

**Common Misuse**
Quoting the principle without identifying the pigeons and the holes
precisely. The rule is only as sharp as the counting.

**How Agents Use It**
- **Embedded**: in capacity / rate-limit / collision analyses as a
  formal check step.
- **Sanity-gate**: when a finding claims "it can't possibly happen,"
  test with an explicit pigeonhole count.

---

## Pareto 80/20

**The Rule**
(Vilfredo Pareto, 1896; generalized by Joseph Juran.) In many
distributions, roughly 80% of the effects come from roughly 20% of the
causes. The ratio is approximate and the exact numbers vary — the
usable claim is that distributions in real systems are typically
heavy-tailed, not uniform.

**When It Applies**
- Prioritizing bug fixes, performance optimizations, or support
  tickets where a handful of items dominate the volume.
- Deciding what to cut when time or budget is limited.
- Root-cause analysis: look at the top of the distribution first.

**When It Misleads**
- When the distribution is actually uniform or bimodal and you
  invented an 80/20 story to justify cutting the long tail. Always
  look at the real distribution before applying the rule.
- When the "20% of causes" is easy to address but the remaining 80%
  of effects have disproportionately high *severity* (security,
  safety, correctness). Pareto by count ≠ Pareto by risk.
- In creative, exploratory, or compounding-return domains, where the
  long tail is where the breakthroughs live.

**Common Misuse**
Treating 80/20 as a law of nature, citing it without ever plotting
the distribution. Pareto is an empirical observation to check, not a
prior to assume.

**How Agents Use It**
- **Sanity-gate**: before recommending "focus on everything," force
  the agent to identify the top-N contributors by actual
  distribution and justify any item in the recommendation list that
  is outside the top bucket.

---

## Parkinson's Law

**The Rule**
(C. Northcote Parkinson, The Economist, 1955.) "Work expands to fill
the time available for its completion." More generally: bureaucratic
activity and scope creep grow to consume whatever slack is given,
unless actively constrained.

**When It Applies**
- Estimating how long a task will take when the deadline is soft or
  unspecified.
- Reviewing projects that are slipping quietly without clear blockers.
- Evaluating meetings, processes, and approval chains that have grown
  over time for no traceable reason.

**When It Misleads**
- Genuinely hard problems are not made easier by arbitrary deadline
  compression; the work doesn't fit in less time just because you
  announce it must.
- In domains where quality is invisible until failure (security,
  correctness, safety), applying Parkinson's to squeeze time directly
  trades off against defect rate.

**Common Misuse**
Using it as a management bludgeon to justify arbitrary compression.
Parkinson's is a diagnosis of why slack is dangerous when uncoached,
not a prescription that all tasks should be done in half the time.

**How Agents Use It**
- **Sanity-gate**: when a plan includes comfortable time buffers with
  no concrete reason for the specific size, question whether the
  buffer will be actually absorbed by the work or by scope that
  hasn't been named.

---

## Mise en Place

**The Rule**
(French culinary practice; "everything in its place.") Before starting
the active work, stage all the ingredients, tools, and state you will
need and verify they are ready. The setup phase is not overhead — it
is the work that makes the active phase survivable under time
pressure.

**When It Applies**
- Deployments, incident drills, migrations, and any task where a
  wrong move under time pressure is expensive.
- Debugging sessions: have logs, reproduction steps, dashboards, and
  rollback plan open before touching the system.
- Writing or code review sessions where context-switching mid-task
  is costly.

**When It Misleads**
- When the setup ritual becomes a way to avoid starting the actual
  work ("I'll just prepare one more thing"). Mise en place is in
  service of the active phase, not a substitute for it.
- In genuinely exploratory work where you don't yet know what you'll
  need — over-preparing locks in a plan that the exploration should
  disturb.

**Common Misuse**
Treating mise en place as a general productivity aphorism divorced
from its time-critical setting. Its bite is specifically about tasks
where a mid-task discovery of "I don't have X" is expensive; it is
much weaker advice in leisurely settings.

**How Agents Use It**
- **Sanity-gate**: on recommendations that involve time-critical
  execution (cutover, hotfix, rollback, go-live), check whether the
  prerequisites are explicitly listed and verified, not assumed.
