---
name: pasta
display_name: PASTA Threat Model
class: lens
underlying_class: native
domain: security
source: Gartner; formalized by Neumerus Labs; adopted industry-wide from ~2012
best_for:
  - Systematic threat enumeration across attack stages
  - Attack-surface prioritization for defense
  - Communication of threat landscape to non-technical stakeholders
one_liner: "Seven-stage threat modeling that decomposes attack scenarios systematically."
---

# PASTA Threat Model

## Overview

PASTA (Process for Attack Simulation and Threat Analysis) decomposes an attacker's workflow into seven sequential stages — from reconnaissance through exfiltration — and maps your system's assets and controls to each stage. Rather than asking "what could go wrong?" abstractly, PASTA asks "what does an attacker actually do, step by step, and where can we stop them?" Practitioners use it when they need to move beyond checklist compliance toward architecture-level threat prioritization and when explaining risk to budget-holders who need the threat narrative made concrete.

## Analytical Procedure

### Stage 0 — Define Scope and Assets

1. **Bound the system.** List the applications, data stores, networks, and users in scope. Draw a box on a diagram or list them in a table. Scope creep kills threat modeling — explicitly exclude out-of-band systems.

2. **Enumerate assets of value.** For each system component, identify what an attacker would want to steal, corrupt, or prevent access to. Be specific:
   - Data assets: PII, credentials, proprietary algorithms, payment card data
   - Functional assets: uptime, transaction throughput, audit log integrity
   - Relational assets: customer trust, regulatory standing

3. **Enumerate entry points.** List every interface through which an attacker could interact with your system:
   - Network endpoints (APIs, ports, protocols)
   - Physical access points (data centers, offices)
   - Supply chain (vendors, dependencies, build systems)
   - Social vectors (phishing, social engineering)

### Stage 1 — Reconnaissance

4. **List reconnaissance activities an attacker would perform to learn about your system:**
   - DNS queries, WHOIS lookups, subdomain enumeration
   - Search engine scraping (public repos, cached pages, job postings)
   - Network scanning (open ports, service banners, SSL certificates)
   - Personnel research (LinkedIn, GitHub commits, email patterns)
   - Public vulnerability disclosures specific to your tech stack

5. **For each activity, ask: "What information would the attacker gain, and how would it inform the next stage?"**
   - Example: Discovering your build system is Jenkins v2.440 narrows the attacker's payload choices for Stage 2.

6. **Identify controls that prevent or detect reconnaissance:**
   - Rate limiting on enumeration queries
   - Subdomain isolation (not listing internal hosts in public DNS)
   - De-identification of error messages
   - Monitoring for port scans and SSH brute-force attempts

### Stage 2 — Weaponization

7. **For the assets identified in Stage 0 and the entry points discovered in Stage 1, enumerate weaponization options — the payloads and exploits an attacker would prepare:**
   - Malware tailored to your OS/language (e.g., a .NET loader if your backend is C#)
   - Credential stuffing lists if your authentication is known to be weak
   - Zero-day or known CVE exploits for your specific versions
   - Social engineering templates (spear phishing emails, fake login pages)
   - Supply chain compromises (malicious packages published under names similar to your dependencies)

8. **For each payload, note its source and ease of acquisition:**
   - Tier 1: Off-the-shelf tools (Metasploit, Empire, Cobalt Strike)
   - Tier 2: Publicly disclosed exploits (GitHub, ExploitDB)
   - Tier 3: Custom or stolen exploits (nation-state level)

9. **Identify controls:**
   - Dependency scanning (SCA tools that detect known-vulnerable packages)
   - Code signing enforcement (reject unsigned executables)
   - Sandbox/AppContainer policies (isolate high-risk code execution)
   - Security awareness training (reduce successful phishing)

### Stage 3 — Delivery

10. **For each weapon, enumerate delivery mechanisms the attacker would use to get it into your environment:**
    - Email (as attachment, link, embedded object)
    - Web (drive-by download, watering hole, reflected XSS)
    - Network (lateral movement via unpatched systems, supply chain injection)
    - Physical media (USB drops, rogue hardware)
    - Cloud infrastructure (misconfigured S3 bucket, exposed Docker registry)

11. **Map delivery methods to your entry points.** Not all delivery methods are equally viable for all entry points. A weaponized binary is useless if your API only accepts JSON.

12. **Identify controls:**
    - Email gateway filtering (attachment blocking, link rewriting)
    - WAF rules (block known malware signatures, injection patterns)
    - Network segmentation (limit lateral movement)
    - Code review and CI/CD gating (prevent malicious code commits)
    - Hardware inventory and rogue device detection

### Stage 4 — Exploitation

13. **For each delivered weapon, enumerate exploitation paths — the actions an attacker takes on your system to achieve code execution, privilege escalation, or data access:**
    - Triggering a buffer overflow or format string vulnerability
    - Exploiting OS or library CVEs
    - Abusing legitimate functionality (SQL injection via a web form, LDAP injection via single sign-on)
    - Privilege escalation via misconfigured sudo, Windows registry, or capability leaks
    - Breaking out of a container or bypassing AppArmor/SELinux

14. **For each exploitation path, assess feasibility given your system's patch level and configuration.**
    - If you are 6 months behind on OS patches, many stage-4 exploits become trivial.
    - If you run containers as root with `--privileged`, escape becomes low-friction.

15. **Identify controls:**
    - Timely patching (OS, libraries, frameworks)
    - Secure configuration hardening (disable unnecessary services, principle of least privilege)
    - Runtime protections (ASR rules in Windows, seccomp profiles in Linux)
    - Input validation and output encoding (prevent injection)
    - Anomaly detection on process spawning, file system writes, network connections

### Stage 5 — Installation

16. **Once the attacker has code execution, what will they do to ensure persistence — to remain in the system even after a reboot or log-out?**
    - Install a backdoor (SSH key in `~/.ssh/authorized_keys`, rootkit, reverse shell)
    - Create a scheduled task or cron job
    - Inject code into a legitimate running process
    - Modify startup scripts or boot firmware
    - Plant a supply chain compromise (modify build output, commit a backdoor to a git repo)

17. **For each persistence mechanism, ask: "If this were in my system today, how long would it take for my incident response team to detect it?"** Days? Weeks? Never?

18. **Identify controls:**
    - File integrity monitoring (Tripwire, AIDE, Wazuh) — detects unauthorized modifications
    - Process allowlisting (Falcon, Carbon Black) — blocks unknown executables
    - Log retention and SIEM correlation (correlate events across machines, detect one-off anomalies)
    - Periodic full-system scanning (virus scans, rootkit scans)
    - Immutable infrastructure (redeploy from source, don't patch in place) where feasible

### Stage 6 — Command and Control

19. **Once installed, the attacker needs to communicate with the compromised system — to issue commands, retrieve data, etc. Enumerate command-and-control (C2) channels they might establish:**
    - HTTPS to a domain the attacker controls (most common — blends with legitimate traffic)
    - DNS tunneling (encodes commands in DNS queries)
    - Cloud services (Slack, OneDrive, Discord) as a dead-drop for commands
    - Peer-to-peer mesh (compromised systems talk to each other, reducing reliance on a single C2 server)
    - Piggyback on existing outbound connections (SOCKS proxying through a legitimate app like a web browser)

20. **For each C2 channel, assess detectability:**
    - Is the destination IP/domain known-bad? (Check threat intel feeds.)
    - Does the traffic pattern match legitimate use? (A download of 1 GB to an external IP at 3 am is suspicious; one small HTTPS request to Slack is not.)
    - Can you block it without breaking legitimate services?

21. **Identify controls:**
    - Egress filtering (allow only known-good destination IPs/domains for outbound connections)
    - Encrypted DNS (DoH, DoT) with malware filtering (Cloudflare, Quad9)
    - Threat intel integration in firewalls/proxies (block known-bad C2 domains in real time)
    - Network segmentation (DMZ, isolated VLAN for high-risk systems)
    - DNS sinkholing (detect beaconing to known-bad domains without blocking)
    - Behavioral analytics (detect unusual outbound traffic volumes or patterns)

### Stage 7 — Exfiltration

22. **With command and control established, what will the attacker do? Enumerate exfiltration objectives:**
    - Steal data (customer records, source code, configurations, encryption keys)
    - Corrupt data (delete backups, alter audit logs, modify transaction records)
    - Sabotage availability (delete files, max out CPU, trigger cascading failures)
    - Establish blackmail (encrypt data, demand ransom)

23. **For each objective, enumerate exfiltration methods:**
    - Direct transfer (FTP, SCP, custom HTTP POST to attacker server)
    - Slowroll (steal data in small chunks over weeks to avoid detection)
    - Staged extraction (move data to an intermediate, less-monitored system first)
    - Public channels (upload to a public paste site or cloud storage, retrieve later)
    - Physical exfiltration (copy to USB, mail a hard drive)

24. **Assess data sensitivity and compliance risk.** A breach of 1000 password hashes is lower-risk than a breach of unencrypted Social Security Numbers or PHI.

25. **Identify controls:**
    - Data classification and DLP (Data Loss Prevention) rules — block transfers of high-sensitivity data to external IPs
    - Encryption at rest and in transit (even if exfiltrated, data is unusable without keys)
    - Egress filtering (block large transfers to unexpected destinations)
    - Monitoring for bulk data access (user suddenly queries 1M rows instead of their typical 100)
    - Honeypot data (plant fake credentials, fake customer records) — if the attacker exfiltrates it, you detect the breach immediately

## Evaluation Criteria

| Check | Pass |
|---|---|
| Scope is explicitly bounded (in/out of scope listed) | Y/N |
| All assets of value are enumerated (data, function, relational) | Y/N |
| All entry points are listed (network, physical, supply chain, social) | Y/N |
| All 7 stages are walked through (none skipped) | Y/N |
| For each stage, at least 3 attacker activities or methods are listed | Y/N |
| For each stage, at least 2 controls are identified | Y/N |
| Controls are tied to specific stage vulnerabilities (not generic security checklist) | Y/N |
| Feasibility/likelihood of each attack path is assessed, not just enumerated | Y/N |

## Red Flags

- Scope is vague or unbounded. "Our whole application" is not actionable — you'll miss critical assets or identify controls that don't fit your actual architecture.
- Stages 1–3 are detailed but stages 5–7 are generic ("monitor for anomalies"). PASTA's power is in tracing the entire attack chain — skipping persistence and C2 leaves your blind spot unaddressed.
- All identified controls are preventive; none are detective or responsive. Even with perfect prevention, assume breach — controls should also detect installation and C2, and enable containment.
- Reconnaissance stage assumes no prior knowledge, but your threat model should account for insider threats, ex-employees, and supply-chain partners who already have entry points.
- Weaponization is listed by CVE number without assessing whether your system is actually vulnerable (due to mitigating configurations, WAF rules, etc.).
- Controls are identified but not prioritized by impact or cost. A firewall rule that blocks 100% of attacks is higher-value than a monitoring rule that detects them after the fact.

## Output Format

```
## PASTA Threat Model Report

**System:** <name/scope>
**Analyst:** <name>
**Date:** <date>
**Threat Actor Profile:** <insider / opportunistic external / nation-state / other>

### Scope and Assets

**In scope:**
- <system component>
- ...

**Out of scope:**
- <excluded system>
- ...

**Assets of value:**
| Asset | Type | Owner | Sensitivity |
|---|---|---|---|
| <name> | Data / Function / Relational | <team> | High / Medium / Low |

**Entry points:**
| Entry Point | Vector | Access Level |
|---|---|---|
| <network endpoint / physical location / supply chain / social> | <method> | Unauthenticated / Authenticated / Internal |

### Stage 1 — Reconnaissance
**Attacker activities:**
1. <activity and likely gain>
2. ...

**Controls:**
- <control and what it prevents/detects>
- ...

### Stage 2 — Weaponization
**Likely payloads:**
- <payload type, source/tier>
- ...

**Controls:**
- ...

### Stage 3 — Delivery
**Delivery methods (by entry point):**
| Entry Point | Delivery Method | Feasibility |
|---|---|---|
| <entry> | <method> | High / Medium / Low |

**Controls:**
- ...

### Stage 4 — Exploitation
**Exploitation paths:**
| Vulnerability | Exploitation Method | Current Mitigation | Likelihood |
|---|---|---|---|
| <CVE or design flaw> | <how attacker exploits> | <current control> | High / Medium / Low |

**Controls:**
- ...

### Stage 5 — Installation
**Persistence mechanisms likely to succeed:**
1. <mechanism and detectability (days to detect)>
2. ...

**Controls:**
- ...

### Stage 6 — Command and Control
**C2 channels:**
| Channel | Detectability | Block Impact |
|---|---|---|
| <HTTPS to attacker domain / DNS tunneling / cloud dead-drop / P2P / other> | <Easy / Moderate / Hard to detect> | <High / Medium / Low impact on legitimate traffic> |

**Controls:**
- ...

### Stage 7 — Exfiltration
**Attack objectives and methods:**
| Objective | Method | Sensitivity of data at risk | Detection difficulty |
|---|---|---|---|
| <steal / corrupt / sabotage / blackmail> | <direct transfer / slowroll / staged / public channel / physical> | High / Medium / Low | Easy / Moderate / Hard |

**Controls:**
- ...

### Attack Chain Criticality

**Highest-confidence attack path (most likely to succeed):**
<Stage 1 entry point> → <Stage 2 weapon> → <Stage 3 delivery> → <Stage 4 exploitation> → <Stage 5 persistence> → <Stage 6 C2> → <Stage 7 objective>

**Gaps in the chain (stages with weakest controls):**
1. <stage and why>
2. ...

**Recommended priority controls (highest impact, lowest cost):**
1. <control and justification>
2. ...

### Confidence
<high | medium | low> — <justification based on completeness of scope, asset enumeration, attack path traceability, and control coverage>
```
---
