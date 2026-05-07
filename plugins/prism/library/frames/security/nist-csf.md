---
name: nist-csf
display_name: NIST Cybersecurity Framework
class: frame
underlying_class: native
domain: security
source: National Institute of Standards and Technology (NIST), 2014–2024
best_for:
  - Classifying a cybersecurity capability or control maturity level
  - Sorting organizational security posture across functions
  - Mapping readiness to implement or scale security practices
one_liner: "Classify organizational security functions by maturity across Identify, Protect, Detect, Respond, Recover."
---

# NIST Cybersecurity Framework

## Overview

The NIST Cybersecurity Framework (CSF) sorts an organization's security posture into five functional domains, each representing a distinct phase of cybersecurity activity. Its core claim is that **different security functions require different kinds of investment and operational readiness** — and that maturity within each function is measurable along a spectrum from Ad Hoc to Managed to Optimized. The framework is not a scorecard you passively fill in: classifying a capability into a function and maturity level clarifies what kind of capability building is appropriate next, and which gaps are most critical.

## Categories

1. **Identify**
   - Governance and discovery of assets, risks, and dependencies across the enterprise.
   - Encompasses risk management programs, asset inventory, supply chain risk, and business continuity planning.
   - Discriminating criterion: the organization can enumerate what it owns, what it depends on, and what the relevant threats are.
   - Example: an IT asset registry linked to business processes, a documented supply chain risk assessment, a threat modeling inventory.

2. **Protect**
   - Safeguards and hardening to prevent or slow unauthorized access and malicious activity.
   - Encompasses access controls, encryption, segmentation, configuration management, awareness training, and defensive architecture.
   - Discriminating criterion: the organization has deployed technical and policy controls that raise the cost or difficulty of a compromise.
   - Example: multi-factor authentication, network segmentation, endpoint detection software, security awareness training.

3. **Detect**
   - Continuous monitoring and alerting to recognize unauthorized activity, anomalies, and indicators of compromise.
   - Encompasses logging, SIEM, intrusion detection, behavioral analysis, threat intelligence correlation, and analysis capabilities.
   - Discriminating criterion: the organization has visibility into traffic and behavior and can distinguish normal from abnormal within a defined time window.
   - Example: a SIEM collecting logs from multiple sources, behavioral analytics on user activity, a SOC team reviewing alerts.

4. **Respond**
   - Incident triage, containment, eradication, and recovery to limit damage and restore normal operations.
   - Encompasses incident response planning, playbooks, communication protocols, forensics capabilities, and coordination with external stakeholders.
   - Discriminating criterion: the organization has pre-planned procedures to execute when an incident is detected, and a team trained to execute them under time pressure.
   - Example: a documented IR playbook, a war room process, pre-authorized escalation chains, threat intelligence sharing agreements.

5. **Recover**
   - Restoration of systems and data to operational state and validation that compromise is eliminated.
   - Encompasses backup and recovery procedures, post-incident validation, lessons-learned processes, and restoration prioritization.
   - Discriminating criterion: the organization can reliably restore to a known-good state and has tested the process under pressure.
   - Example: validated backups held offline, a tested recovery time objective (RTO) per system, a post-incident review cadence.

## Classification Procedure

1. Name the specific security capability or control you are evaluating (e.g., "our access control architecture," "our incident response process," "our asset inventory").
2. Ask **"Which of the five CSF functions does this capability belong to?"** Refer to the descriptions above. A capability may touch multiple functions; classify it into the one it most directly addresses.
3. Determine the **maturity level** of the capability by answering:
   - Is the capability **present at all** (ad hoc / reactive only)?
   - Is it **formalized and repeatable** (managed / policy-driven)?
   - Is it **continuously improved and optimized** (optimized / data-driven)?
4. Record the function and maturity level. Identify which functions are **absent or immature** in your current posture — these are the gap priorities.
5. For each gap, ask which function it is in: this determines what kind of capability building is appropriate (e.g., Detect gaps require monitoring infrastructure; Respond gaps require playbook development and drills).

## Implications per Category

| Function | Maturity signal | What gaps here mean |
|---|---|---|
| **Identify** | Complete asset inventory linked to business criticality; documented risk baseline. | You cannot make informed protection decisions; you will over-protect low-risk assets and under-protect critical ones. |
| **Protect** | Segmentation, least-privilege access, encryption at rest and in transit; regular config audits. | An attacker who gains a foothold can move laterally and exfiltrate at will; defenses are perimeter-only. |
| **Detect** | Real-time or near-real-time log aggregation; alert rules calibrated to false-positive rate. | Breaches go unnoticed for weeks or months; you learn of compromise from external parties. |
| **Respond** | Tested playbooks, defined roles, timeline targets; regular tabletop drills. | Incident response is chaotic; containment is slow; attackers have time to exfiltrate or establish persistence. |
| **Recover** | Validated backups tested quarterly; documented RTO/RPO per system. | Recovery from ransomware or destructive attacks is unreliable; downtime extends and confidence in restoration is low. |

Implicit deployment order: **Identify baseline first** (you cannot manage what you do not know), **then Protect and Detect in parallel** (prevention and detection are co-dependent), **then Respond and Recover** (only fully enabled after you have confidence in the first three). A gap in Identify casts doubt on the adequacy of all downstream functions.

## Common Misclassifications

- **Conflating Protect with Detect.** Hardening a system (Protect) and monitoring it (Detect) are orthogonal. An unmonitored hardened system is brittle; an unprotected system cannot be detected in time. Both are necessary.
- **Treating Respond as Protect.** Incident response playbooks (Respond) are *not* prevention controls (Protect); they assume a breach has occurred. Classifying an IR plan as a protective control underestimates residual risk.
- **Assuming Identify is complete when it is only asset inventory.** Inventory is necessary but not sufficient; Identify also requires understanding what depends on what, which assets are critical, and what threats are relevant. A list of IPs without business context does not close the Identify gap.
- **Over-investing in Detect without Identify.** You cannot alert on what you do not understand; uncontextualized logs generate alert fatigue. A mature Detect function depends on a prior Identify function that clarifies what "abnormal" means.
- **Confusing Respond with Recover.** Incident response (triage and containment) and recovery (restoration to clean state) are distinct phases. An organization may have fast response but slow recovery, or vice versa. The CSF treats them as separate for this reason.
