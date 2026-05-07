---
name: mitre-att-ck
display_name: MITRE ATT&CK
class: frame
underlying_class: native
domain: security
source: MITRE Corporation, 2013–present
best_for:
  - Sorting an observed adversary behavior or artifact into a standardized TTP category
  - Aligning defensive controls to known attack patterns
  - Building threat models grounded in real-world adversary behavior
one_liner: "Matrix that classifies observed adversary behavior into standardized TTP categories."
---

# MITRE ATT&CK

## Overview

MITRE ATT&CK is a curated matrix of **Tactics, Techniques, and Sub-techniques** that map real-world adversary behavior across the attack lifecycle. Its core claim is that defenders can only build effective countermeasures and detection rules if they first classify what the adversary is *actually trying to do* — not what the attack looks like in isolation. By sorting observed behaviors into Tactics (the "why"), Techniques (the "how"), and Sub-techniques (the "how specifically"), the frame constrains which defensive playbooks, detection signatures, and architectural controls are appropriate. A single artifact (a file, a network flow, a process behavior) often participates in multiple Techniques and Tactics simultaneously; the frame's value is in making those relationships visible and systematic.

## Categories

The frame is organized into **14 Tactics** (phases of an attack campaign), each containing **dozens to hundreds of Techniques**, and many Techniques containing **Sub-techniques** that add specificity.

### Tactics (ordered by typical attack lifecycle)

1. **Reconnaissance**
   - Adversary gathers information about the target and its environment *before* attacking.
   - Includes open-source intelligence, network scanning, and social engineering surveys.
   - Discriminating criterion: the target is not yet compromised; the adversary is in the *information-gathering* phase.
   - Example: gathering employee names from LinkedIn, scanning for open ports, WHOIS lookups.

2. **Resource Development**
   - Adversary creates, acquires, or stages tools, accounts, domains, and infrastructure *outside* the target environment.
   - Includes setting up command-and-control servers, registering malicious domains, acquiring credentials.
   - Discriminating criterion: the adversary has not yet made contact with the target; all activity is in-house preparation.
   - Example: registering a lookalike domain, acquiring a bulletproof hosting account, developing malware.

3. **Initial Access**
   - Adversary gains a **first foothold** into the target environment through a single, specific entry vector.
   - Includes phishing, supply-chain compromise, exposed services, and physical access.
   - Discriminating criterion: this is the moment the target becomes *compromised*; there is a specific Technique that opened the door.
   - Example: phishing with a malicious attachment, exploiting an unpatched internet-facing application, insider access.

4. **Execution**
   - Adversary **runs code** or commands within the target environment.
   - Includes native tools (PowerShell, bash), scripts, and malware deployment.
   - Discriminating criterion: code or commands are executing on the target; the focus is on *how* it runs, not *what* it does yet.
   - Example: executing a PowerShell script, running a scheduled task, invoking a macro.

5. **Persistence**
   - Adversary ensures it can **return** to the target even if the initial access is lost.
   - Includes creating backdoors, modifying startup scripts, stealing credentials, and establishing alternative access channels.
   - Discriminating criterion: the goal is *longevity*; the technique keeps the adversary present across reboots or account logoffs.
   - Example: adding a cron job, creating a new admin account, modifying the Windows registry for autostart.

6. **Privilege Escalation**
   - Adversary **elevates** from a foothold with limited rights to higher-privilege access within the same system or domain.
   - Includes kernel exploits, credential theft, abuse of misconfigurations, and DLL hijacking.
   - Discriminating criterion: the adversary already has access; they are moving *up* within the existing system.
   - Example: exploiting a kernel vulnerability, abusing `sudo` misconfiguration, dumping LSASS.

7. **Defense Evasion**
   - Adversary **avoids detection or removal** by security tools and processes.
   - Includes obfuscation, disabling logging, living-off-the-land techniques, and social engineering of human defenders.
   - Discriminating criterion: the intent is to *hide from defenses*, not to achieve a new capability; often layered with other Tactics.
   - Example: disabling Windows Defender, clearing event logs, using LOLBins, code obfuscation.

8. **Credential Access**
   - Adversary **steals or derives** credentials (passwords, keys, tokens, hashes).
   - Includes credential dumping, keylogging, phishing, and brute-force attacks.
   - Discriminating criterion: the outcome is usable credentials that grant access *as another user* or service.
   - Example: dumping SAM hashes, stealing AWS API keys, password-spraying, keystroke logging.

9. **Discovery**
   - Adversary **maps** the target environment — systems, users, groups, shares, processes, and software inventory.
   - Includes network enumeration, account enumeration, file system browsing, and local privilege enumeration.
   - Discriminating criterion: the adversary is building a *picture* of what exists; they are not yet acting on that knowledge.
   - Example: running `ipconfig`, enumerating Active Directory groups, listing running processes, scanning SMB shares.

10. **Lateral Movement**
    - Adversary **moves** from one compromised system to another within the network.
    - Includes pass-the-hash, pass-the-ticket, RDP compromise, and exploitation of multi-system services.
    - Discriminating criterion: the adversary already has access to *at least one* system and is reaching for *another*.
    - Example: using a stolen ticket to access a file server, RDP-ing to another machine, exploiting a service that spans systems.

11. **Collection**
    - Adversary **gathers** data of interest (files, emails, screenshots, clipboard, audio, keystrokes).
    - Includes data from the file system, email, cloud storage, and input capture.
    - Discriminating criterion: the goal is to *assemble* specific information, not to exfiltrate it yet.
    - Example: copying files to a staging directory, dumping email from Exchange, taking screenshots, recording keystrokes.

12. **Command and Control**
    - Adversary **establishes a communication channel** with compromised systems to issue commands and receive output.
    - Includes C2 protocols over HTTP(S), DNS, P2P, and dead-drop sites.
    - Discriminating criterion: the channel is for *ongoing instruction*, not initial access or data exfil.
    - Example: HTTPS reverse shell, DNS tunneling, Slack C2, Cobalt Strike beacon.

13. **Exfiltration**
    - Adversary **removes** collected data from the target environment to a system under their control.
    - Includes data compressed and encrypted in transit, exfil over C2, and use of legitimate services (cloud upload, email).
    - Discriminating criterion: data *leaves* the target's network boundary; it is now in the adversary's possession.
    - Example: exfiltrating via HTTPS, uploading to attacker-controlled S3, mailing data to a drop address.

14. **Impact**
    - Adversary **manipulates, disrupts, or degrades** the target's systems, data, or operations to achieve final objectives.
    - Includes encryption (ransomware), deletion, defacement, and service degradation.
    - Discriminating criterion: the goal is *damage*, *disruption*, or *coercion*, not stealth or further access.
    - Example: encrypting files with ransomware, deleting volume shadow copies, defacing a website, DDoS.

## Classification Procedure

1. **Observe** the artifact or behavior in question — a process, a file, a network flow, a registry modification, a user action.

2. **Ask: What is the adversary's goal at this moment?** Align the behavior to one of the 14 Tactics listed above. Example: if the adversary is stealing credentials from LSASS, the goal is Credential Access, not Execution (Execution is the method used to run the dumping tool).

3. **Once the Tactic is chosen, consult the MITRE ATT&CK matrix** for that Tactic and identify which **Technique(s)** match the observed behavior. Many Techniques contain multiple Sub-techniques; choose the most specific Sub-technique if one applies.

4. **Verify by asking: Does this Technique have the same goal *and* the same execution method as the observed behavior?** If the goal matches but the method differs, you may be in the wrong Tactic; re-examine.

5. **Record the full path:** Tactic → Technique → Sub-technique (if applicable), and note any supporting artifacts (command lines, file hashes, network indicators) that confirm the classification.

6. **Cross-reference:** A single artifact often participates in multiple Tactics (e.g., a PowerShell script used in Execution may also be part of Defense Evasion). Record all applicable classifications.

## Implications per Category

| Tactic | Defensive Implication | Example Controls |
|---|---|---|
| **Reconnaissance** | Monitor *external* intelligence leakage; assume it will happen. Focus on limiting the surface area adversaries can profile. | Email filtering, privacy controls on public profiles, network segmentation limits external reconnaissance value. |
| **Resource Development** | Threat intelligence on malicious infrastructure; domain registration monitoring; supplier vetting. | Blacklist malicious domains, monitor for typosquatting, vet third-party dependencies. |
| **Initial Access** | Perimeter controls; user security awareness; patch management; limiting exposure of internet-facing services. | MFA, email filtering, application allow-listing, EDR blocking suspicious execution paths. |
| **Execution** | Process execution controls; code integrity checks; script block logging; behavior-based detection. | AppLocker, attack surface reduction rules, PowerShell logging, EDR process/file monitoring. |
| **Persistence** | Monitor for unauthorized modifications to startup, scheduled tasks, registry, and system config; MFA on privileged accounts. | File integrity monitoring, audit of scheduled tasks and autostart locations, host-based IDS. |
| **Privilege Escalation** | Patch management; least-privilege principles; monitor for abnormal elevation patterns; segment by role. | Patch Tuesday, UAC hardening, privilege access management (PAM), access reviews. |
| **Defense Evasion** | Logging completeness; immutable audit trails; behavioral detection (e.g., disabling Defender); forensic recovery. | Sysmon logging, cloud audit logs, EDR behavioral rules, redundant security tooling. |
| **Credential Access** | Credential hygiene; MFA; credential store hardening; monitor for dumping tools; input validation. | LSASS protection, Windows Credential Guard, MFA, conditional access policies, block known dumping tools. |
| **Discovery** | Limit what unprivileged users can enumerate; monitor for bulk query patterns (e.g., directory enumeration). | Least-privilege AD permissions, WMI restrictions, audit account enumeration, network segmentation. |
| **Lateral Movement** | Network segmentation; monitor for anomalous lateral flows; ticket/token invalidation; host-based firewall rules. | Microsegmentation, conditional access for lateral access, Kerberos Golden Ticket detection, firewall rules. |
| **Collection** | Data classification and DLP; monitor for mass data access; archive hardening; screenshot/input capture logging. | DLP rules, audit trails on sensitive repos, screen capture alerts, limit clipboard access. |
| **Command and Control** | Egress filtering; DNS sinkholing; network IDS signatures; block known C2 infrastructure. | Proxy rules, DNS filtering, Zeek or Suricata rules for C2 traffic, block-list of known beacons. |
| **Exfiltration** | Egress monitoring (volume, direction, destination); DLP; network segmentation to limit egress paths. | NGFW rules, DLP rules, monitor for encrypted outbound tunnels, limit egress to known-good IPs. |
| **Impact** | Backup hardening; immutable snapshots; incident response readiness; communication plans. | Offline backups, snapshot protection, incident playbooks, business continuity plans. |

## Common Misclassifications

- **Execution mistaken for Persistence.** A one-time PowerShell script execution is Execution; if the script is installed to run at every startup, it is Persistence. The tell is whether the behavior repeats automatically across reboots or logoffs.

- **Privilege Escalation mistaken for Lateral Movement.** Both involve moving to a new access level, but Privilege Escalation happens on the *same system* (user → admin), while Lateral Movement crosses *system boundaries* (system A → system B). If the adversary is still on the same box, it is Privilege Escalation.

- **Discovery mistaken for Credential Access.** Both are reconnaissance-like phases, but Discovery is about *mapping the environment* (what users exist, what shares are there), while Credential Access is about *stealing usable authentication material*. If the output is a list of users, it is Discovery; if the output is a password hash, it is Credential Access.

- **Command and Control mistaken for Exfiltration.** A reverse shell (C2) is a bidirectional command channel; exfiltration is the act of *moving* data out. A C2 channel may *carry* exfiltration traffic, but the Tactic classification depends on the intent: if the adversary is issuing commands, it is C2; if they are shipping stolen data out, it is Exfiltration.

- **Defense Evasion layered with other Tactics.** Disabling Windows Defender is Defense Evasion, but it often happens *during* Execution or Credential Access. Log the primary Tactic (the thing the adversary is trying to *accomplish*) and note Defense Evasion as a supporting technique.

- **Treating Reconnaissance as compromise.** Pre-breach reconnaissance (phishing domain surveys, LinkedIn scraping) is *not* a compromise; the target's systems are not yet affected. Confusion here leads to false positives in threat intelligence correlation.
