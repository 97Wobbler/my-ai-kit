---
name: coin-doctrine
display_name: COIN Doctrine
class: lens
underlying_class: native
domain: military-strategy
source: U.S. counterinsurgency doctrine, formally codified in FM 3-24 (2006); developed from lessons in Iraq and Afghanistan
best_for:
  - Diagnosing failure modes in stabilization operations
  - Sequencing population security, governance, and economic development
  - Assessing whether a counterinsurgency campaign is attempting phases in the right order
one_liner: "Counterinsurgency's sequential three-step stabilization — Clear, Hold, Build."
---

# COIN Doctrine

## Overview

COIN Doctrine structures counterinsurgency campaigns into three sequential phases—Clear, Hold, Build—with the principle that each phase must establish conditions for the next. The lens operates on campaign plans, resource allocation decisions, and stabilization timelines. Practitioners use it to detect when operations are out of sequence (holding territory before it is cleared, building institutions in unsecured areas) or when one phase is starved of resources while the campaign claims to be advancing. The discipline is enforcing the dependency order, not the individual tactics.

## Analytical Procedure

### Phase 1 — Map the Current Campaign State

1. **Identify the geographic unit under assessment.** This must be a discrete territory with defined boundaries (a district, province, or sector), not the entire country. COIN operates at the local level.

2. **For each location, mark its current state as one of:**
   - **Pre-clear:** Insurgent presence is dominant or unchallenged; government forces have not committed to population control.
   - **Clearing:** Deliberate military operations are underway to remove insurgent armed presence; civilians are either being protected or relocated.
   - **Post-clear:** Insurgent armed forces have been displaced or destroyed; security vacuums exist but are being actively filled by government presence.
   - **Holding:** Government forces maintain continuous presence (checkpoints, patrols, bases); population has returned or is returning; routine order is being restored.
   - **Building:** Government institutions (courts, tax collection, services) are functioning; economic activity is visibly returning; the population is cooperating with government initiatives.
   - **Built:** Institutions are self-sustaining; insurgent recurrence is treated as crime, not warfare; the territory has moved beyond the campaign phase.

   Do not assume a location is in one state because the campaign plan says so. Use evidence: unit presence, casualty rates, civilian movement, checkpoint functionality, school operation, market activity.

3. **Plot each location on a timeline or map.** This becomes your baseline state diagram.

### Phase 2 — Diagnose Sequencing Errors

4. **For each location currently in "Holding" or "Building" state, ask:** Was this location properly cleared first? 
   - Evidence of proper clearing: documented military operations that resulted in casualty ratios or captured/killed leadership; civilian displacement and protected areas during operations; post-operation security sweeps.
   - Evidence of improper clearing (or skipped clearing): holding forces encounter sustained ambushes; insurgent shadow government still collects taxes; civilian informants refuse to cooperate; "holding" operations look defensive, not occupational.
   
   If evidence points to "improper clearing," flag this as **Sequence Error Type A: Holding without Clear.**

5. **For each location currently in "Building" state, ask:** Is this territory actually held?
   - Evidence of proper holding: government forces have established permanent presence (barracks, logistics, communication); population movement is restricted and predictable; insurgent movement is rare or detected; intelligence gathering has expanded.
   - Evidence of improper holding: building programs are guarded by passing patrols, not resident forces; schools/clinics close when security forces leave; population movement remains unpredictable; insurgent recruitment is still occurring.
   
   If evidence points to "improper holding," flag this as **Sequence Error Type B: Building without Hold.**

6. **For each location in "Holding," assess resource commitment.** 
   - Count the ratio of government security personnel to civilian population. COIN doctrine typically requires 1 soldier/policeman per 20–50 civilians for effective holding (varies by terrain and insurgent strength).
   - Measure the continuity of presence: Are the same units rotating out and in? Are command relationships and local intelligence continuity maintained?
   - If ratios are below doctrine and presence is transient, flag as **Resource Error: Under-manned holding.**

7. **For locations attempting "Building," assess whether prerequisites are met.**
   - Can a market operate without armed escorts? Can courts function without bunkers? Can teachers show up reliably?
   - If the answer to any is "no," the location is not truly held, and building programs are vulnerability targets, not community investments.
   - Flag as **Premature Building:** if building programs exist in locations where daily civilian life still requires military protection.

### Phase 3 — Assess Doctrine Compliance

8. **Measure phase balance.** Count the number of locations in each state. A mature COIN campaign typically has:
   - Fewer locations in "Clearing" (ongoing operations are resource-intensive).
   - Growing locations in "Holding" (the bottleneck phase; often the longest).
   - Fewer locations in "Building" (only after holding is genuinely established).
   
   If the campaign reports "building" in more than 20% of territory while holding is thin, or if clearing operations are still expanding rather than maturing, the campaign is likely out of sequence or resource-starved in the holding phase.

9. **Trace resource allocation to phase distribution.** Does the budget and personnel distribution match the phase map?
   - Clearing requires kinetic force (infantry, air support, artillery).
   - Holding requires presence force (police, garrison, checkpoints).
   - Building requires governance and services (administrators, teachers, engineers).
   
   If the force structure is still 80% kinetic but the campaign claims to be primarily in holding/building, the doctrine is not aligned with capability.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Each location has been assigned to one of six states with cited evidence | Y/N |
| Locations in "Holding" or "Building" were checked for prerequisite completion of prior phases | Y/N |
| At least one sequencing error (Type A, B, or Premature Building) was identified or none exist and explanation provided | Y/N |
| Resource allocation (personnel and budget) was compared to phase distribution | Y/N |
| If sequencing errors exist, their remediation cost and timeline were estimated | Y/N |

## Red Flags

- A location jumps directly from "Pre-clear" to "Building" with no holding phase. This is often a political or donor pressure artifact, not a military success.
- Holding-phase locations are described with adjectives like "improving" or "stabilizing" but casualty rates among security forces remain high and unchanged month-to-month. Holding is not occurring; fighting is.
- Building programs (schools, health clinics, governance training) are concentrated in large cities or provincial capitals while rural or remote areas remain in pre-clear. This is sequencing by geography, not by military reality, and building may collapse if those cities are not actually held.
- The campaign plan uses "Clear/Hold/Build" language but has no geographic resolution — "we are clearing the insurgency" nationwide. COIN operates district by district. If the plan doesn't subdivide, the doctrine is being paid lip service only.
- Resource allocation is frontloaded to clearing operations (kinetic forces) while holding and building are described as "partner forces" or "low-cost." Holding without sufficient presence is always a failure.

## Output Format

```
## COIN Assessment

**Territory:** <geographic unit name>

### Phase State Map
| Location | Current State | Evidence | Prerequisites Met? | Notes |
|---|---|---|---|---|
| <...> | Pre-clear/Clearing/Post-clear/Holding/Building/Built | <...> | Y/N/Partial | <...> |

### Sequencing Errors
- **Type A (Holding without Clear):** <locations and evidence>
- **Type B (Building without Hold):** <locations and evidence>
- **Premature Building:** <locations where building occurs in uncontrolled areas>
- **Under-manned Holding:** <locations below recommended personnel ratios with counts>

### Resource Alignment
- Clearing force (kinetic): <personnel count and operations>
- Holding force (garrison/police): <personnel count and locations>
- Building force (governance/services): <personnel and program count>
- **Alignment verdict:** <aligned/misaligned with phase distribution and explain gap>

### Phase Balance Assessment
| Phase | Locations in State | % of Territory | Doctrine Expectation | Status |
|---|---|---|---|---|
| Clearing | <count> | <...>% | <10–20%> | <on-track/over/under> |
| Holding | <count> | <...>% | <50–70%> | <on-track/over/under> |
| Building | <count> | <...>% | <10–20%> | <on-track/over/under> |

### Key Findings
1. <sequencing issue with remediation estimate if applicable>
2. <resource allocation gap if present>
3. <risk of phase collapse if locations are vulnerable to insurgent recurrence>

### Confidence
<high | medium | low> — <justification based on quality of evidence, completeness of field assessment, and alignment with doctrine>
```
---
