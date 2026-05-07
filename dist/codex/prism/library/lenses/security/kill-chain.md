---
name: kill-chain
display_name: Kill Chain Analysis
class: lens
underlying_class: native
domain: security
source: Lockheed Martin Cyber Kill Chain, 2011
best_for:
  - Mapping adversary behavior to defensive controls
  - Threat model validation and gap analysis
  - Incident response timeline reconstruction
one_liner: "Break down the adversary's full intrusion path into seven stages and plan detection/block strategies per stage."
---

# Kill Chain Analysis

## Overview

The Kill Chain breaks an adversary's attack into seven sequential phases, from initial reconnaissance through data exfiltration. By mapping an observed or hypothesized attack to these phases, defenders can identify which controls are present, which are missing, and at which stage an attack can be detected or interrupted. Practitioners use this when analyzing a breach retroactively, testing defensive readiness, or designing a threat model for a specific adversary or attack surface.

## Analytical Procedure

### Phase 1 — Establish Attack Scope

1. **Define the target or scenario.** What system, asset, or organization is under attack? What is the assumed adversary capability level (script kiddie, organized crime, state-sponsored)? Write both as one sentence each.

2. **Identify the attack chain trigger.** What initiates the sequence — an email, a public-facing web app, a supply-chain compromise, physical access? Be specific.

3. **Define the success condition.** What does the adversary achieve at the end? Data theft, persistence, lateral movement, destruction, espionage? This anchors the reconstruction.

### Phase 2 — Map Each Kill Chain Phase

For each of the seven phases below, answer all sub-questions. If a phase does not apply to your scenario, note that explicitly and why.

#### 1. Reconnaissance
- **Active recon:** Does the adversary perform DNS lookups, port scans, or public service enumeration? List tools/indicators if observable.
- **Passive recon:** Does the adversary collect information from public sources (WHOIS, social media, job postings, code repositories)? What information is harvested?
- **Timeline:** When does reconnaissance occur relative to delivery? Same day? Months prior?
- **Detection possibility:** What logs, DNS records, or network traffic would reveal this phase?

#### 2. Weaponization
- **Artifact creation:** What malware, exploit, phishing kit, or macro is built? What framework or kit is used (Metasploit, Cobalt Strike, custom)?
- **Payload construction:** Does the weapon include command & control (C2) callbacks, privilege escalation, data exfiltration routines, or destructive payloads?
- **Staging:** Where is the weapon prepared (attacker infrastructure, compromised third-party server, cloud instance)?
- **Detection possibility:** What file hashes, code signatures, or behavioral patterns would identify the weapon before delivery?

#### 3. Delivery
- **Vector:** How does the weapon reach the target (spear-phishing email, malicious URL, USB drop, supply-chain trojanized software, drive-by download)?
- **Trigger:** What user action or system behavior causes execution (opening attachment, clicking link, mounting USB, auto-update)?
- **Volume:** Is this targeted (one recipient) or broad (bulk phishing)?
- **Detection possibility:** What email gateway, URL filter, or endpoint detection would block or alert on the delivery?

#### 4. Exploitation
- **Vulnerability:** What specific CVE, zero-day, or misconfiguration is exploited? If human-engineered (phishing + click), note that.
- **Execution context:** Does the exploit run as the user, escalate privilege, or execute in kernel space?
- **Pre-conditions:** What software versions, patch levels, or user configurations must be present for exploitation to succeed?
- **Detection possibility:** What antivirus signatures, behavior-based detection, or exploit prevention technology would stop it?

#### 5. Installation
- **Persistence mechanism:** How does the adversary ensure the malware survives reboot (registry run keys, scheduled tasks, service installation, cron job, firmware modification)?
- **Footprint:** What files, processes, network connections, or registry artifacts does installation create?
- **Privilege requirement:** Does installation require admin/root?
- **Detection possibility:** What file integrity monitoring, process allowlisting, or host-based intrusion detection would catch installation?

#### 6. Command & Control (C2)
- **Protocol:** How does the malware communicate home (HTTP/S, DNS, SMTP, custom binary protocol, P2P)?
- **Frequency:** Is C2 continuous, periodic, or on-demand?
- **Infrastructure:** Where are the C2 servers (attacker-owned domain, compromised server, bulletproof hosting, proxy chain)?
- **Resilience:** Does the malware use domain generation algorithms (DGA), hardcoded IPs, DNS fallback, or peer discovery to maintain contact?
- **Detection possibility:** What network monitoring, DNS sinkholing, or egress filtering would detect or block C2?

#### 7. Actions on Objective
- **Attacker actions:** What does the adversary do once they have foothold and C2 (data exfiltration, lateral movement, privilege escalation, persistence hardening, destruction, espionage)?
- **Dwell time:** How long does the adversary remain undetected before achieving objective?
- **Scope:** Does compromise remain isolated (single machine) or spread (network segment, domain, supply chain)?
- **Detection possibility:** What data loss prevention (DLP), endpoint detection & response (EDR), or SIEM rules would alert?

### Phase 3 — Identify Control Gaps

8. **For each phase, list the existing defensive controls.** Examples: phishing training, email filtering, vulnerability scanning, patch management, network segmentation, EDR, SIEM, incident response playbook.

9. **Mark each phase as one of:**
   - **Defended:** Control(s) exist and are actively monitored; adversary would be caught or blocked.
   - **Monitored:** Control(s) exist but may not trigger alerting; adversary could proceed but leave detectable traces.
   - **Undefended:** No control present; adversary can operate freely.

10. **For each undefended or monitored phase, cost the remediation.** Examples: tool cost, labor, integration effort, false positive rate.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Attack scenario is stated specifically (not "a company" but "SaaS platform with public API") | Y/N |
| All seven phases are addressed (none skipped or assumed) | Y/N |
| Each phase has ≥3 sub-questions answered | Y/N |
| Reconnaissance and Delivery sub-questions include detection/observability angle | Y/N |
| Control gaps are explicitly marked Defended / Monitored / Undefended | Y/N |
| Remediation for undefended gaps includes rough cost or effort estimate | Y/N |

## Red Flags

- One or more phases are skipped because "that doesn't apply to us." Kill Chain works for every attack; if a phase seems absent, it usually means the adversary is hiding it well or your visibility is limited.
- All phases come back as "Defended" with no gaps. Either your controls are genuinely airtight (rare) or the analysis was not adversarial enough — assume the attacker is intelligent and patient.
- Reconnaissance and Weaponization are treated as "outside our control" and dismissed. Both are observable if you look at threat intel, DNS logs, and network flow data.
- Detection possibility is left blank for multiple phases. Without knowing how each phase would be detected, you cannot prioritize controls.
- No dwell time or lateral movement scenario is explored in Actions on Objective. Initial compromise is not the end state; trace what happens next.

## Output Format

```
## Kill Chain Assessment

**Scenario:**
Target: <specific system/org>
Adversary capability: <level>
Success condition: <objective>

### Phase Mapping

| Phase | Sub-findings | Control Status | Observable Indicators |
|---|---|---|---|
| **1. Reconnaissance** | Passive/active methods; timeline; sources | Defended / Monitored / Undefended | DNS logs, WHOIS queries, netflow |
| **2. Weaponization** | Artifact type; payload; staging location | Defended / Monitored / Undefended | File hashes, code signatures, malware repos |
| **3. Delivery** | Vector; trigger; volume | Defended / Monitored / Undefended | Email gateway logs, URL filters, sandbox alerts |
| **4. Exploitation** | CVE/zero-day; execution context; pre-conditions | Defended / Monitored / Undefended | Antivirus, exploit prevention, behavioral detection |
| **5. Installation** | Persistence mechanism; footprint; privilege needed | Defended / Monitored / Undefended | File integrity, process allowlisting, registry audits |
| **6. Command & Control** | Protocol; frequency; infrastructure; resilience | Defended / Monitored / Undefended | Network monitoring, DNS sinkholing, egress rules |
| **7. Actions on Objective** | Attacker actions; dwell time; scope | Defended / Monitored / Undefended | DLP, EDR, SIEM rules, data exfiltration alerts |

### Control Gaps & Remediation

| Undefended Phase | Recommended Control | Effort/Cost |
|---|---|---|
| <phase> | <control> | <estimate> |

### Kill Chain Break Points
List the 2-3 phases where an adversary is most likely to be caught or stopped given the current control posture. Explain why.

### Confidence
<high | medium | low> — <justification based on visibility into each phase and control completeness>
```
