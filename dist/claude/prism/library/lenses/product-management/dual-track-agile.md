---
name: dual-track-agile
display_name: Dual-Track Agile
class: lens
underlying_class: native
domain: product-management
source: Marty Cagan, INSPIRED (2008) and Empowered (2020)
best_for:
  - Validating product ideas before committing engineering effort
  - Keeping discovery and delivery synchronized without blocking each other
  - Identifying when a product team is conflating learning with shipping
one_liner: "Run discovery and delivery in parallel so only validated ideas are built."
---

# Dual-Track Agile

## Overview

Dual-Track Agile separates product discovery (validating *what* to build) from delivery (building it well). Discovery runs on a shorter, more volatile cadence; delivery runs on a predictable sprint cycle. The two tracks stay coupled through a lightweight synchronization point where validated ideas enter the backlog. Teams use this lens when they notice engineering is building features that don't solve real problems, or when discovery insights arrive too late to influence the sprint. The discipline is resisting the urge to merge the tracks — kept separate, they prevent waste; merged, they become waterfall in a backlog.

## Analytical Procedure

### Phase 1 — Map Current State

1. **Identify the discovery track.** What activities are happening to validate ideas before they reach engineering?
   - User interviews, prototyping, A/B tests, analytics queries, competitive research, user testing
   - Document the *current* cadence (weekly? ad hoc? daily?).
   - Note the artifacts produced (findings, prototypes, validated learning, or just opinions?).

2. **Identify the delivery track.** What is the engineering team building?
   - Sprint backlog, roadmap commitments, currently in-flight work
   - Document the sprint cycle length (1 week? 2 weeks? continuous?).
   - Note what triggered each item (user request, stakeholder mandate, bug, hypothesis, legacy debt?).

3. **Map the handoff.** How do ideas move from discovery into the backlog?
   - Is there a formal gate or a weekly sync? Or do ideas just appear in backlog comments?
   - How many cycles of lag exist between a validated insight and engineering picking it up?
   - Who decides what delivery prioritizes?

4. **Audit the backlog for track confusion.** Go through the top 10 items in the current backlog.
   - Mark each as **Validated** (discovery has evidence it solves a problem), **Speculative** (idea with no user validation yet), or **Debt** (bugfix, refactor, tech work).
   - Count the Speculative items. If >30% of the backlog is Speculative, discovery and delivery are not decoupled — delivery is shipping guesses.

### Phase 2 — Evaluate Track Health

5. **Check discovery cycle time.** Pick a recent validated insight (something that moved into delivery). How long did discovery take to reach confidence?
   - Measure from first hypothesis to "ready to build" (not "shipped").
   - If >2 sprints, discovery is too slow or too rigorous. If <3 days, it skipped validation.
   - Document the actual cycle time.

6. **Check discovery-to-delivery lag.** Once an idea is validated, how long until engineering starts work?
   - Measure from "ready to build" date to sprint inclusion date.
   - If >1 sprint, the backlog is stale or priorities are not synchronized.
   - If 0 days (immediate), check whether discovery waited for a sprint to start or engineering is reactive — both are red flags.

7. **Inventory discovery debt.** List all active discovery initiatives (ongoing research, open prototypes, unresolved questions).
   - How many have been open >2 sprints without resolution?
   - Are any blocked on engineering (can't validate without a feature) or on external data (waiting for user access)?
   - Document blockers.

8. **Audit decision rights.** For the items currently in delivery, who actually decided to build them?
   - Trace back: Did discovery validate it? Did a stakeholder mandate it? Did engineering volunteer?
   - If >50% came from stakeholder mandate or engineering volunteer, the product team does not own discovery.

### Phase 3 — Stress-Test Synchronization

9. **Run a synchronization scenario.** Assume a discovery team finishes validating a high-priority idea *during* an active sprint.
   - What happens? Is it queued for the next sprint? Does it interrupt current work? Does it languish in a comment?
   - Document the actual policy. If there is no policy, that's a finding.

10. **Check capacity allocation.** How much of the engineering team's sprint capacity is reserved for discovery support (prototyping, user testing sessions, analytics work)?
    - Should be 10–25% in a mature dual-track setup. If 0%, discovery is not integrated. If >40%, delivery is starved.
    - Document the actual allocation (ask the team lead, don't guess).

11. **Verify the confidence threshold.** What evidence does an idea need before it's "ready to build"?
    - Cagan's model expects: user interviews (5+), prototype test (3+ users), measurable success metric defined.
    - Does your team have an explicit threshold, or is it implied?
    - Document what you find.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Discovery and delivery tracks are mapped with explicit cadences | Y/N |
| Backlog audit completed; Speculative % calculated | Y/N |
| Discovery cycle time measured (validated insight to "ready to build") | Y/N |
| Discovery-to-delivery lag measured (ready to build to sprint start) | Y/N |
| Decision rights traced for >5 current backlog items | Y/N |
| Synchronization policy tested with a scenario | Y/N |
| Confidence threshold for "ready to build" is explicit | Y/N |

## Red Flags

- Speculative backlog is >30%. The tracks are merged; delivery is guessing.
- Discovery cycle time is >4 sprints. Either discovery is over-rigorous or it lacks authority to move ideas forward.
- Discovery-to-delivery lag is >2 sprints. The backlog is a time-delayed cache, not a live synchronization point.
- No synchronization policy exists (ideas just appear in backlog or are dropped). The tracks are not actually coupled.
- >50% of delivery backlog came from stakeholder mandate (not discovery validation). The product team does not own the product.
- Discovery debt exists but is never resolved. Open research questions languish; prototypes are never tested.
- Confidence threshold is vague ("we'll know it when we see it"). This enables delivery to ship before discovery is ready, or discovery to over-investigate.
- Capacity for discovery support is <5% or >50%. Either discovery is isolated or delivery is starved.

## Output Format

```
## Dual-Track Agile Assessment

### Current State Map
**Discovery track:**
- Activities: [list]
- Current cadence: [days/weeks]
- Artifacts produced: [findings/prototypes/metrics/other]

**Delivery track:**
- Sprint length: [days/weeks]
- Backlog size: [count]
- Items by origin: [count Validated | count Speculative | count Debt]

**Handoff mechanism:**
- Formal gate? [yes/no]
- Sync cadence: [frequency or "ad hoc"]
- Lag from ready-to-build to sprint start: [days/sprints]

### Backlog Audit
| Item | Status | Origin | Track readiness |
|---|---|---|---|
| <...> | Validated/Speculative/Debt | Discovery/Stakeholder/Engineering | Ready/Blocked/Unclear |

Speculative ratio: _% (threshold: <30%)

### Track Health Metrics
- Discovery cycle time (hypothesis → ready to build): _ sprints
- Discovery-to-delivery lag (ready to build → sprint start): _ days
- Open discovery debt (unresolved): _ items (oldest: _ sprints)
- Discovery support capacity: _%

### Decision Authority
| Backlog item | Validated? | Who decided? | Track owner |
|---|---|---|---|
| <...> | Y/N | Discovery/Stakeholder/Engineering | Product/Other |

### Synchronization
- Policy for mid-sprint discoveries: [explicit | implicit | absent]
- Scenario test result: [accepted into next sprint | deferred | dropped]

### Confidence Threshold
Explicit criteria for "ready to build":
1. <...>
2. <...>
3. ...

### Findings
1. <observation + impact>
2. <...>

### Confidence
<high/medium/low> — <justification (e.g., "high because all metrics are documented and policy is explicit; low because decision authority is unclear")>
```
---
