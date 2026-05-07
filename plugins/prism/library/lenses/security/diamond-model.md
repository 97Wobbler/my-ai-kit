---
name: diamond-model
display_name: Diamond Model
class: lens
underlying_class: native
domain: security
source: Phishing Tactics, Techniques, and Procedures (Mandiant/FireEye, 2013–2015); formalized by Lockheed Martin Cyber Kill Chain research
best_for:
  - Structuring intrusion analysis when attribution or threat actor motive is unclear
  - Separating observable facts (infrastructure, capabilities, victims) from inference (adversary identity)
one_liner: "Decompose an intrusion incident along adversary, capability, infrastructure, and victim axes for structured threat analysis."
---

# Diamond Model

## Overview

The Diamond Model structures intrusion analysis around four observable vertices—Adversary, Capability, Infrastructure, Victim—and the edges (relationships) between them. Rather than jumping to "who did this," the model forces analysts to first catalog what happened, how it happened, and where it happened, postponing identity inference until evidence justifies it. Practitioners use this when an incident is fresh, attribution is contested, or multiple threat actors appear to share tools or infrastructure.

## Analytical Procedure

### Phase 1 — Establish the Diamond Vertices

1. **Identify the Victim.** 
   - Which specific organization, system, or user was targeted or compromised?
   - Document: affected asset(s), operational impact (data stolen, systems disrupted, etc.), discovery date.
   - If multiple victims are present, treat each as a separate diamond (or note if they share a motive).

2. **Catalog the Infrastructure used by the attacker.**
   - List all IP addresses, domains, email accounts, or other attacker-controlled or attacker-leased resources observed in the intrusion.
   - For each, note: how it was used (C2 server, phishing sender, malware host), when first seen, when last seen, and whether it was publicly attributable to a known provider (cloud host, registrar, ISP).
   - Separate infrastructure the attacker owns outright from infrastructure they merely rented or compromised.

3. **Enumerate the Capabilities.**
   - Write down every tool, malware, or technique used in the attack chain. Include: exploit CVEs, malware families, reconnaissance tools, living-off-the-land techniques (native OS utilities).
   - For each capability, note: version/variant (if identifiable), first observed date, public availability (open-source, dark web, custom).
   - Do not infer motive or skill level yet; just list what was deployed.

4. **Describe the Adversary.**
   - At this stage, do not name an organization or state. Instead, describe what you know directly: How many operators were involved? What language(s) appear in tooling or communications? What timezone patterns suggest? How long was the intrusion active?
   - Note: this vertex will remain sparse until Phase 2 inference.

### Phase 2 — Map Edges and Relationships

5. **Connect Victim to Adversary.**
   - Why this victim? Was the target industry-specific, geographically selective, or opportunistic? Was a specific company process or employee targeted?
   - Is there evidence of prior reconnaissance? Was the victim selected from a list or at random from a port scan?

6. **Connect Adversary to Capability.**
   - Is the malware custom-built or off-the-shelf? Does code style or obfuscation suggest development rigor?
   - Did the attacker use capabilities in a way that requires special knowledge (e.g., exploiting a 0-day, chaining multiple CVEs) or generic knowledge (standard phishing + freely available tool)?

7. **Connect Capability to Infrastructure.**
   - Where was each tool hosted or staged? Which infrastructure did it communicate with?
   - Was infrastructure reused across multiple attacks, or was it clean per incident? Does reuse suggest laziness, resource constraints, or confidence?

8. **Connect Infrastructure to Adversary.**
   - Can any infrastructure be traced to a known buyer, registrant, or operator? Are there WHOIS records, passive DNS patterns, or registrar logs?
   - Are there operational security (OPSEC) indicators—rented infrastructure from a specific bulletproof hoster, payment method, language of support ticket—that narrow the suspect pool?

### Phase 3 — Test for Relationships Across Diamonds

9. **Check for infrastructure reuse across victims.**
   - Did the same IP, domain, or malware appear in another intrusion? Does it suggest a single actor or a commoditized tool?
   - If reuse is found, note the time gap and the organizational or geographic distance between victims. Tight coupling suggests same actor.

10. **Test capability kinship.**
    - Do the malware families, exploit chains, or TTPs match known groups in public reporting or your own incident history?
    - Is kinship explained by shared code (open-source malware), shared developer (custom tool), or coincidence (many groups use phishing)?

### Phase 4 — Confidence Tagging and Red Lines

11. **Tag each inference with confidence.**
    - **Observational** (high confidence): directly logged or captured (packet capture, malware binary, email header).
    - **Derived** (medium confidence): inferred from consistent patterns (e.g., timezone of operator activity from multiple intrusions).
    - **Attributed** (low to medium confidence): assigned to a named threat actor; see Phase 5.

12. **Identify what you do NOT know.**
    - What would it take to move a derived inference to observational? (e.g., "We need a WHOIS subpoena" or "We need the malware author's signing key.")
    - What infrastructure or capability detail is still missing? Unsolved pieces are investigation leads for follow-up.

### Phase 5 — Attribution (Optional, High-Barrier Entry)

13. **Only after Phase 1–4 are complete: propose an Adversary identity** (if evidence supports it).
    - Compare the diamond vertices against known threat actors' historical campaigns in your intel database or public reporting.
    - Require at least two independent pieces of evidence (infrastructure overlap + capability kinship, or two separate capability matches across different attack campaigns).
    - Explicitly state the confidence level: are you certain, likely, or speculative? Reserve "attribution" for high-confidence assertions; use "suspected" or "assessed" for medium confidence.

14. **Document alternative hypotheses.**
    - What other threat actors could have produced this diamond?
    - Why does your leading hypothesis fit better than alternatives?

## Evaluation Criteria

| Check | Pass |
|---|---|
| All four vertices (Adversary, Capability, Infrastructure, Victim) are populated with observable data | Y/N |
| Infrastructure list includes at least 3 observables (IP, domain, email, hash, etc.) with timelines | Y/N |
| Capabilities are enumerated without speculation about intent or skill level | Y/N |
| All edges (6 potential relationships) are explored, even if some are empty | Y/N |
| Each inference is tagged Observational / Derived / Attributed with justification | Y/N |
| At least one alternative hypothesis for Adversary identity is documented | Y/N |
| Investigation gaps and follow-up leads are explicitly listed | Y/N |

## Red Flags

- The Adversary vertex is filled with a named group (e.g., "APT28") before Phase 4 is complete. You are reasoning backward from a suspect instead of forward from evidence.
- Capabilities are described with judgments ("sophisticated," "targeted," "advanced"). These are interpretations; stick to what was observed.
- Infrastructure is sparse or missing IP/domain data. You cannot correlate across incidents without concrete observables.
- Edges are asserted without evidence ("The adversary is clearly state-sponsored because they used a 0-day"). State sponsorship requires separate justification; capability sophistication does not imply state actor.
- Victim selection is left blank. Understanding motive or targeting logic is central to threat assessment.
- The diamond is used to confirm a preexisting suspect rather than to interrogate what the evidence actually shows. This reverses the method and introduces confirmation bias.

## Output Format

```
## Diamond Model Analysis

**Incident:** <date range, affected organization(s)>

### Phase 1 — Diamond Vertices

**Victim**
- Organization: <name>
- Assets affected: <systems, data, impact>
- Discovery date: <date>

**Infrastructure**
| Observable | Type | First Seen | Last Seen | Provider / Owner | Notes |
|---|---|---|---|---|---|
| <IP / domain / email> | C2 / phishing / malware host / staging | <date> | <date> | <provider> | <reused? / OPSEC markers?> |

**Capability**
| Tool / Malware | Version | Deployment | First Seen | Availability | Notes |
|---|---|---|---|---|---|
| <name> | <variant> | <how used> | <date> | open-source / custom / leaked | <obfuscation, exploit targets, TTPs> |

**Adversary (observational)**
- Operator count: <estimated from log patterns, behavioral analysis>
- Language indicators: <keyboard layout, error messages, timestamps>
- Timezone: <inferred from activity patterns>
- Known aliases: <if any>

### Phase 2 — Edges and Relationships

**Victim ↔ Adversary**
- Targeting logic: <industry, geography, specific process, or opportunistic>
- Evidence: <prior recon, phishing to specific user, strategic asset selection>
- Confidence: <Observational / Derived / Attributed>

**Adversary ↔ Capability**
- Custom or COTS?: <custom-built indicators / off-the-shelf>
- Skill signals: <code quality, exploit chaining, operational discipline>
- Confidence: <level>

**Capability ↔ Infrastructure**
- Deployment chain: <malware host → C2 IP → staging domain>
- OPSEC: <clean per-incident, or reused across campaigns>
- Confidence: <level>

**Infrastructure ↔ Adversary**
- Registrant / provider forensics: <WHOIS, payment method, bulletproof hoster>
- Operator-specific markers: <language in support tickets, timing of renewals>
- Confidence: <level>

### Phase 3 — Cross-Diamond Correlation

**Infrastructure reuse:**
- <Observable> also appeared in: <other incident(s)>
- Time gap: <duration>
- Organizational/geographic distance: <assess coupling>

**Capability kinship:**
- Malware family / exploit overlap with: <known campaigns>
- Likelihood of shared code vs. shared developer: <assessment>

### Phase 4 — Investigation Gaps

1. <Missing observable needed to elevate an inference>
2. <Follow-up required: subpoena, passive DNS, reverse shell analysis>
3. <Alternative explanation not yet ruled out>

### Phase 5 — Adversary Attribution (if justified)

**Assessed adversary:** <name or "Unknown">
- Primary evidence: <infrastructure + capability match / code analysis / targeting pattern>
- Supporting evidence: <secondary indicators>
- Alternative hypotheses: <other suspects and why they fit less well>
- Confidence: <high / medium / low>

### Confidence
<high/medium/low> — <justification. E.g., "High for infrastructure and capabilities (directly observed); Medium for adversary (two independent matches to known group, but no direct WHOIS/payment link); Low for motive (victim selection could be strategic or opportunistic)">
```
---
