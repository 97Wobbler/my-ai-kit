---
name: cvss-v3-1
display_name: CVSS v3.1
class: lens
underlying_class: native
domain: security
source: FIRST (Forum of Incident Response and Security Teams), 2019
best_for:
  - Quantifying vulnerability severity for triage and remediation prioritization
  - Communicating risk in standardized terms across security teams and vendors
  - Comparing vulnerabilities across different systems and contexts
one_liner: "Quantify vulnerability severity on a 0.0–10.0 scale via eight base metrics."
---

# CVSS v3.1

## Overview
CVSS v3.1 is a standardized framework that scores the inherent severity of a vulnerability based on eight base metrics describing its technical properties: Attack Vector, Attack Complexity, Privileges Required, User Interaction, Scope, and the impacts on Confidentiality, Integrity, and Availability. The output is a single numeric score (0.0–10.0) that enables stakeholders to prioritize patching and security investment. Practitioners use it to avoid scoring vulnerabilities by gut feel and to communicate risk uniformly to non-technical decision makers.

## Analytical Procedure

### Step 1 — Gather Vulnerability Metadata
1. Obtain the vulnerability description, affected software, and attack scenario.
2. Consult the CVE entry, security advisory, or proof-of-concept to confirm:
   - What an attacker must do to trigger the vulnerability
   - What systems or roles must be in place
   - What damage (data leak, service disruption, system takeover) is possible
3. Record the attack scenario in 1–2 sentences. This is your scoring reference.

### Step 2 — Score Attack Vector (AV)
Determine how an attacker delivers the attack. Choose exactly one:

| Value | Definition | Example |
|---|---|---|
| **Network (N)** | Over a network, no physical access required | Remote SQL injection via web form |
| **Adjacent Network (A)** | Same local network segment required | ARP spoofing within a subnet |
| **Local (L)** | Local system access required, but not elevated privileges | Local privilege escalation via shell |
| **Physical (P)** | Physical access to the device required | Tampering with hardware to extract keys |

**Scoring rule:** Select the least restrictive vector that applies. If the vulnerability can be exploited remotely OR locally, use Network.

### Step 3 — Score Attack Complexity (AC)
How much variability in the target environment affects the attack's success? Choose exactly one:

| Value | Definition | Example |
|---|---|---|
| **Low (L)** | Attack works the same way regardless of the target's configuration; attacker has full control of success | Buffer overflow with fixed offset; SQL injection with predictable query |
| **High (H)** | Attack requires precise conditions: specific OS version, compiler optimization, ASLR disabled, or timing window | TOCTOU race condition; gadget chain that only works on one glibc version |

**Scoring rule:** If the attack requires the attacker to gather intelligence or adapt to the target, use High. Otherwise, Low.

### Step 4 — Score Privileges Required (PR)
What level of authorization must the attacker possess *before* launching the attack?

| Value | Definition | Example |
|---|---|---|
| **None (N)** | No authentication or privileges required | Unauthenticated remote code execution |
| **Low (L)** | Attacker has unprivileged user-level access | Authenticated user escalates to admin |
| **High (H)** | Attacker has admin or system-level privileges | DBA-only vulnerability in database |

**Scoring rule:** This is the attacker's pre-attack state, not post-attack. If privilege escalation is the vulnerability itself, set PR=None.

### Step 5 — Score User Interaction (UI)
Must a user (other than the attacker) perform an action for the attack to succeed?

| Value | Definition | Example |
|---|---|---|
| **None (N)** | Attack executes without user action | Automated worm; vulnerability triggered by network packet alone |
| **Required (R)** | Another user must take action | Victim must click a phishing link; administrator must open a malicious file |

**Scoring rule:** Include only actions by humans. Automated agent actions (e.g., crawler fetching a page) do not count.

### Step 6 — Score Scope (S)
Does the vulnerability affect only the vulnerable component, or can it also harm resources outside that component?

| Value | Definition | Example |
|---|---|---|
| **Unchanged (U)** | Only the vulnerable component is affected | Privilege escalation within a single process |
| **Changed (C)** | Other components or services beyond the vulnerable one are impacted | Container escape affecting the host; application sandbox bypass affecting OS |

**Scoring rule:** Ask: "After exploitation, is there a security boundary (process, sandbox, privilege level, service boundary) that the attacker has crossed?" If yes, use Changed.

### Step 7 — Score Confidentiality Impact (C)
How much sensitive information can an attacker read?

| Value | Definition | Example |
|---|---|---|
| **None (N)** | No information disclosure | Denial-of-service attack |
| **Low (L)** | Attacker gains limited access to some data; not all data is accessible | Read access to non-sensitive fields in a database |
| **High (H)** | Attacker gains broad access to sensitive data | Read entire database; extract all user records; access encryption keys |

**Scoring rule:** Consider data types the system holds (PII, secrets, financial records) and how much of it is exposed.

### Step 8 — Score Integrity Impact (I)
Can the attacker modify or delete data?

| Value | Definition | Example |
|---|---|---|
| **None (N)** | No modifications possible | Read-only vulnerability |
| **Low (L)** | Attacker can modify some data but impact is limited; integrity checks may detect changes | Insert a minor log entry; modify non-critical settings |
| **High (H)** | Attacker can modify or delete critical data without detection | Alter financial transactions; erase logs; modify authentication credentials |

**Scoring rule:** Consider whether the modification would be obvious to legitimate users or systems.

### Step 9 — Score Availability Impact (A)
Can the attacker disrupt service or cause a denial of service?

| Value | Definition | Example |
|---|---|---|
| **None (N)** | No service disruption possible | Information disclosure only |
| **Low (L)** | Attacker can degrade performance or cause temporary unavailability | Increase response time; crash a worker process (restarted automatically) |
| **High (H)** | Attacker can cause sustained or complete service outage | Crash the main process repeatedly; exhaust disk space; render system unrecoverable without manual intervention |

**Scoring rule:** Consider how quickly the system recovers and how much user-facing disruption occurs.

### Step 10 — Calculate the Base Score
Use the CVSS v3.1 scoring formula (or a reference calculator) with the eight metrics from Steps 2–9:

1. Map each metric to its numeric weight (defined by the CVSS standard).
2. Apply the formula: Base Score = Roundup(min((AV + AC + PR + UI + S + C + I + A) / 8, 10.0)).
   (The actual formula is more nuanced; use the [official CVSS calculator](https://www.first.org/cvss/calculator/3.1) if manual calculation is error-prone.)
3. Record the resulting score (e.g., 7.5).

### Step 11 — Assign Severity Rating
Map the Base Score to a severity label:

| Score Range | Severity |
|---|---|
| 9.0–10.0 | Critical |
| 7.0–8.9 | High |
| 4.0–6.9 | Medium |
| 0.1–3.9 | Low |
| 0.0 | None |

## Evaluation Criteria

| Check | Pass |
|---|---|
| Vulnerability scenario is documented in 1–2 sentences | Y/N |
| All eight base metrics are explicitly scored and justified | Y/N |
| Each metric choice references specific evidence (CVE, PoC, or advisory text) | Y/N |
| Attack Vector reflects the least restrictive applicable attack method | Y/N |
| Scope change is justified with a named security boundary | Y/N |
| Base Score calculation is shown (or calculator output is attached) | Y/N |
| Severity rating matches the computed Base Score | Y/N |

## Red Flags

- Metrics are scored based on *possible but not demonstrated* attacks. CVSS scores the attack as described in the vulnerability report, not every theoretical variant.
- Scope is marked Unchanged despite the attack crossing a privilege or isolation boundary. Scope change is often under-scored.
- Privileges Required is set to None for a vulnerability that actually requires authentication. Re-check the attack scenario.
- Confidentiality, Integrity, and Availability are all marked High, but the vulnerability is actually just a read-only info disclosure. At least one impact must be None or Low.
- Base Score and Severity Rating don't match the computed value. Verify the formula or calculator output.
- The rationale for each metric is generic ("this is a network attack, so AV=Network"). Rationales should cite specific details from the CVE or advisory.

## Output Format

```
## CVSS v3.1 Assessment

**Vulnerability:**
<CVE ID or name>

**Attack Scenario:**
<1–2 sentence description of how the vulnerability is exploited>

### Base Metrics

| Metric | Value | Justification |
|---|---|---|
| Attack Vector (AV) | N / A / L / P | <evidence from advisory or PoC> |
| Attack Complexity (AC) | L / H | <environmental variability or attacker prerequisites> |
| Privileges Required (PR) | N / L / H | <pre-attack authorization state> |
| User Interaction (UI) | N / R | <whether another user must act> |
| Scope (S) | U / C | <named boundary crossed, if any> |
| Confidentiality (C) | N / L / H | <breadth of information exposed> |
| Integrity (I) | N / L / H | <whether data can be modified> |
| Availability (A) | N / L / H | <whether service can be disrupted> |

### Score Calculation

Base Score: **X.X** (severity: <Critical | High | Medium | Low | None>)

*Formula application or calculator screenshot:* <reference>

### Confidence

<high | medium | low> — <justification of confidence in scoring based on clarity and completeness of vulnerability disclosure>
```
