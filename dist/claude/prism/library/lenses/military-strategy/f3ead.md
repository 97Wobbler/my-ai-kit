---
name: f3ead
display_name: F3EAD Loop
class: lens
underlying_class: native
domain: military-strategy
source: origin uncertain; widely used in military operations planning and special operations doctrine
best_for:
  - Executing tactical cycles with clear phase gates
  - Rapid targeting and strike planning
  - Iterative intelligence-driven operations
one_liner: "Find-Fix-Finish-Exploit-Analyze-Disseminate — closed-loop operations cycle from target discovery to result dissemination."
---

# F3EAD Loop

## Overview
F3EAD (Find, Fix, Finish, Exploit, Analyze, Disseminate) is a six-phase operational cycle that moves from target identification through execution to intelligence dissemination. Rather than a strategic framework, it is a concrete tempo for tactical action — each phase has defined inputs, tasks, and handoff criteria. Practitioners use it to compress decision-making timelines and ensure nothing falls through the gap between strike execution and the next targeting cycle. The discipline is maintaining phase discipline under time pressure.

## Analytical Procedure

### Phase 1 — Find

1. **Define the intelligence requirement.** State what category of target you are looking for (location, network node, asset) and what constitutes confirmation. Write this in measurable terms: geolocation grid, network signature, observed behavior pattern, or physical characteristic.

2. **List all collection sources available.** Include human intelligence (HUMINT), signals intelligence (SIGINT), imagery intelligence (IMINT), open-source intelligence (OSINT), and any real-time sensors. Assign collection responsibility and dwell time (how long the source can watch before operational security decay).

3. **Set a time gate for Find completion.** Decision-makers need a firm cutoff — finding does not mean certainty, it means sufficient confidence to move to Fix. Document the confidence threshold (e.g., "two independent collection sources" or "geolocation confidence > 80%").

4. **Establish deconfliction protocol.** Identify who must approve target data before passing to Fix phase (legal review, command authority, allied coordination). Write the escalation path.

### Phase 2 — Fix

1. **Validate target location and identity.** Cross-check Find output against known target profiles. If targeting a person, confirm distinguishing characteristics. If targeting a location, mark grid coordinates and verify no changes since last observed.

2. **Assess target stability.** How long will the target remain at this location or in this state? Hours, minutes, days? This determines timeline urgency for subsequent phases.

3. **Check for protected persons, sites, or civilians.** Document all nearby protected sites (hospitals, schools, religious buildings), high-value non-combatants, and any legal constraints on the target. Record these explicitly — absence of this step is a common failure mode.

4. **Assign targeting officer and execution unit.** Name the person responsible for moving the target to Finish phase and identify the unit with authority to execute. No phase proceeds without explicit ownership.

5. **Set the Fix window.** Decide the maximum acceptable delay between Fix and Finish. If target stability window is 4 hours, set execution window to 3 hours. If window closes, return to Find phase.

### Phase 3 — Finish

1. **Generate execution plan.** Write the 5-line OPORD (Operation Order): who, what, when, where, why. Include withdrawal route, communication plan, and rules of engagement (ROE).

2. **Conduct pre-execution verification.** Re-confirm target location with the most recent intelligence (not the Find-phase data). This is the last chance to abort.

3. **Execute the strike or seizure.** Document execution time, method, and immediate Battle Damage Assessment (BDA) — did the strike hit the intended target?

4. **Establish perimeter security and preserve evidence.** Secure the site (if ground operation) or establish a surveillance buffer (if strike). Protect materials, documents, or other intelligence value for Analyze phase.

5. **Mark Finish completion time.** Log the end of this phase for cycle-time analysis.

### Phase 4 — Exploit

1. **Collect on-site materials.** If a location strike, photograph the scene. If a capture, secure documents, electronics, communications devices. If a network target, capture metadata and communications. The exploitation window is usually minutes to hours — be fast.

2. **Interview or interrogate (if applicable).** Follow legal authorities and ROE. Document all questioning and responses for Analyze phase.

3. **Establish chain of custody.** Name the officer responsible for moving each piece of material to the Analyze team. No hand-offs without documentation.

4. **Secure counterintelligence assessment.** Check whether the target or site poses an operational security (OPSEC) risk — did the operation reveal your sensor network, tactics, or intent? Document findings.

### Phase 5 — Analyze

1. **Conduct technical analysis of captured materials.** Have materials assessed by subject-matter experts: cryptanalysts for communications, document analysts for written material, network analysts for digital traffic.

2. **Correlate findings with previous intelligence.** Cross-reference captured data against your existing database of targets, networks, and patterns. What is new? What confirms previous analysis? What contradicts it?

3. **Update targeting priorities.** Based on new intelligence, identify new targets (secondary targets found in the network) and update existing target profiles. Generate a list of "next targets" for the Find phase to prioritize.

4. **Assess intelligence gap closure.** Did the operation answer the original intelligence requirement? Did it create new questions? Document the gap.

5. **Produce an intelligence product.** Write a brief intelligence summary (2-5 pages) suitable for dissemination to decision-makers and partner units.

### Phase 6 — Disseminate

1. **Classify and mark the intelligence product.** Apply appropriate classification markings and handling caveats. Confirm authorities for sharing with allies and interagency partners.

2. **Identify dissemination recipients.** Decision-makers and targeting cells (for Find phase of next cycle), operational commanders, intelligence fusion centers, and allied intelligence services (if applicable).

3. **Deliver products through classified and unclassified channels.** Use secure classified dissemination for sensitive material; use unclassified summary sheets for wider distribution.

4. **Capture lessons learned.** Document what worked and failed in this cycle: Find dwell time, Fix validation failures, Finish execution surprises, exploitation gaps. This input feeds process improvement and the next cycle's Find prioritization.

5. **Close the loop formally.** Confirm receipt by recipients. Archive the complete cycle record (Find decision, target package, Finish BDA, Analyze output, Disseminate distribution) for audit and future reference.

6. **Identify feedback for collection sources.** If a source provided poor Find intelligence or Fix validation failed because of missing data, feed that back to collection managers so they adjust dwell, tasking, or methodology.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Find phase has explicit confidence threshold and time gate | Y/N |
| Fix includes protected-site deconfliction and target stability assessment | Y/N |
| Finish phase includes re-confirmation of target location before execution | Y/N |
| Exploit phase has chain-of-custody documentation | Y/N |
| Analyze phase produces correlation against existing intelligence, not isolated findings | Y/N |
| Disseminate includes lessons-learned capture and feedback to collection | Y/N |
| Each phase has a named owner/officer | Y/N |
| Cycle-time targets are set and tracked | Y/N |

## Red Flags

- Find phase ends without a time gate. Target development can be endless; cycles break when decision-makers have no cutoff.
- Fix phase has no deconfliction check. Striking a protected site or mis-identified target is a mission-ending failure — this step cannot be skipped.
- Finish phase proceeds without re-confirmation of target location. Hours or days may have passed since Find; the target may have moved.
- Exploit phase collects materials with no chain of custody. Without documentation, captured intelligence cannot be used in court or shared with allies.
- Analyze phase produces findings in isolation, not correlated with existing intelligence. Isolated findings are useless for targeting the next cycle.
- Disseminate phase is one-way delivery. Feedback to Find/Fix teams and collection managers is missing, so the same gaps repeat in the next cycle.
- No ownership named for any phase. Responsibility diffuses and phases slip.

## Output Format

```
## F3EAD Execution Report

**Operation ID:** <identifier>
**Cycle start date/time:** <timestamp>

### Find Phase
- Intelligence requirement: <what we were looking for>
- Sources tasked: <HUMINT/SIGINT/IMINT/OSINT>
- Confidence threshold: <metric and threshold>
- Find completion time: <timestamp>
- Confidence in target location/identity: high | medium | low — <justification>

### Fix Phase
- Target grid/location: <coordinates or description>
- Target stability window: <duration, e.g., "4 hours">
- Protected sites nearby: <list or "none identified">
- Targeting officer: <name>
- Execution unit: <unit designation>
- Fix approval: <timestamp, approver>
- Confidence in target profile: high | medium | low — <justification>

### Finish Phase
- Execution time: <timestamp>
- Method: <strike type, seizure, etc.>
- Battle Damage Assessment: <BDA result>
- Finish completion time: <timestamp>

### Exploit Phase
- Materials collected: <list>
- Chain of custody officer: <name>
- Counterintelligence assessment: <risk level and findings>
- Exploit completion time: <timestamp>

### Analyze Phase
- Technical analysis findings: <summary by material type>
- New targets identified: <list>
- Intelligence gaps closed: <list>
- Intelligence gaps created: <list>
- Confidence in correlation to existing intelligence: high | medium | low — <justification>

### Disseminate Phase
- Classification: <classification level>
- Recipients: <list by org>
- Lessons learned: <bullet list of process findings>
- Feedback to Find/Fix teams: <findings requiring collection or tactical adjustment>
- Disseminate completion time: <timestamp>

### Cycle Performance
- Total cycle time: <hours/minutes>
- Find-to-Finish delay: <hours/minutes>
- Confidence in overall operation outcome: high | medium | low — <justification>
```
---
