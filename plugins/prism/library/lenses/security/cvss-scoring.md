---
name: CVSS v3.1 Scoring
domain: security
source: FIRST.org, Common Vulnerability Scoring System v3.1 Specification
underlying_class: model
best_for: Assigning an objective, comparable severity score to a discovered vulnerability so remediation can be prioritized across a portfolio
one_liner: "Assign objective scores to discovered vulnerabilities via the eight CVSS v3.1 Base Metrics and compute remediation SLAs."
---

# CVSS v3.1 Scoring

## Overview
CVSS turns vulnerability severity into a number between 0 and 10 by scoring eight Base Metrics. The number is not the point — the point is the *conversation the metrics force*. Two reviewers who disagree on severity will usually find that they disagree on one specific metric (often Attack Vector or Scope), and naming which one breaks the deadlock. Practitioners use it to compare findings fairly across teams, features, and time.

## Analytical Procedure

1. **Describe the vulnerability in one paragraph.** Include: the vulnerable component, the attacker action required, the resulting impact. If you can't write this paragraph, you don't have enough information to score — go collect more.

2. **Score each of the 8 Base Metrics.** Do not guess — for each, name the specific evidence that led to the value. The metrics are divided into two groups: Exploitability (how easy) and Impact (how bad).

### Exploitability Metrics

#### Attack Vector (AV)
How does the attacker reach the vulnerable component?
- **Network (N)** — reachable over the network from beyond the local subnet (internet-exposed). Highest severity.
- **Adjacent (A)** — requires the attacker to be on the same physical or logical network (same Wi-Fi, same VLAN, Bluetooth range).
- **Local (L)** — requires local access to the target (shell, logged-in user).
- **Physical (P)** — requires physical touch (USB, hands on the device).

Check: Is there a path from "internet attacker" to "vulnerable code"? If yes, AV=N regardless of intermediate steps.

#### Attack Complexity (AC)
Conditions beyond the attacker's control that must be true.
- **Low (L)** — exploit works reliably, first try, no special conditions.
- **High (H)** — requires specific configuration, timing, or preparation the attacker can't guarantee (e.g., race condition, specific memory layout).

Check: "Do I need to get lucky?" If no, AC=L. Most real-world vulnerabilities are AC=L; AC=H is reserved for genuine reliability barriers.

#### Privileges Required (PR)
What level of access the attacker must have before exploiting.
- **None (N)** — unauthenticated.
- **Low (L)** — ordinary user account.
- **High (H)** — admin, root, or equivalent.

Check: If the attacker must compromise credentials first, score for the *minimum* privilege level that allows the exploit, not the highest.

#### User Interaction (UI)
Does a legitimate user have to do something for the exploit to work?
- **None (N)** — no user action needed. The attacker can trigger it alone.
- **Required (R)** — user must click, visit, open, run, etc.

Check: Stored XSS that fires on page load = N (the user just visits). Reflected XSS via a crafted link = R.

### Scope

#### Scope (S)
Does the exploit affect only the vulnerable component, or does it cross a security authority boundary?
- **Unchanged (U)** — impact stays within the vulnerable component's authority (e.g., one tenant on a multi-tenant system).
- **Changed (C)** — impact extends to other components under different authority (e.g., sandbox escape, container escape, VM escape, cross-tenant leak).

Check: Is the attacker gaining access to data or functionality that a DIFFERENT system/component owns? If yes, S=C. This metric has an outsized effect on the final score — get it right.

### Impact Metrics (scored after considering Scope)

#### Confidentiality (C)
- **High (H)** — attacker obtains all data in the component, OR some data with serious consequences.
- **Low (L)** — attacker obtains some data but not critical.
- **None (N)** — no disclosure.

#### Integrity (I)
- **High (H)** — attacker can modify any/all protected data, OR modification has serious consequences.
- **Low (L)** — some data can be modified but the attacker does not control what or how much.
- **None (N)** — no modification.

#### Availability (A)
- **High (H)** — attacker can fully deny access to the component.
- **Low (L)** — reduced performance or intermittent disruption.
- **None (N)** — no availability impact.

3. **Compute the Base Score.** Use the FIRST.org CVSS calculator or the v3.1 formula. Don't eyeball it — the formula is non-linear and Scope=Changed in particular is counterintuitive.

4. **Map score to severity band:**
   - **0.0** — None
   - **0.1–3.9** — Low
   - **4.0–6.9** — Medium
   - **7.0–8.9** — High
   - **9.0–10.0** — Critical

5. **Suggest remediation SLA based on severity:**
   - Critical: fix or mitigate within 24 hours
   - High: within 7 days
   - Medium: within 30 days
   - Low: within 90 days
   These are starting points. Adjust for exposure and compensating controls, but document deviations.

6. **Write the CVSS vector string.** Format: `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H`. This is the canonical form that tools consume.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Vulnerability is described in one clear paragraph before scoring | Y/N |
| Every Base Metric has a justification (not just a value) | Y/N |
| Scope metric explicitly considers whether a security authority boundary is crossed | Y/N |
| Final score is computed with a calculator, not estimated | Y/N |
| CVSS vector string is produced in canonical form | Y/N |
| Remediation SLA is assigned based on severity band | Y/N |

## Red Flags

- Every finding scores 9.0+. Either the portfolio is genuinely catastrophic (rare) or the reviewer treats CVSS as a pressure tool rather than a measurement.
- Scope is always U. Reviewers often forget to ask about cross-boundary impact. Double-check anything involving tenancy, sandboxing, or auth federation.
- Attack Vector is Physical or Local for a vulnerability in a cloud service. Almost certainly mis-scored — re-verify the actual reachability.
- PR is N (none) but the exploit requires "just a user account." PR=None means no account at all. A valid user account is PR=L.
- The same vulnerability gets wildly different scores from two reviewers and neither can point to which metric they disagree on. The lens is being used as vibes.

## Output Format

```
## CVSS v3.1 Assessment

**Vulnerability description:**
<paragraph — component, attacker action, impact>

### Base Metrics

| Metric | Value | Justification |
|--------|-------|---------------|
| Attack Vector (AV) | N / A / L / P | <evidence> |
| Attack Complexity (AC) | L / H | <evidence> |
| Privileges Required (PR) | N / L / H | <evidence> |
| User Interaction (UI) | N / R | <evidence> |
| Scope (S) | U / C | <evidence — is a security boundary crossed?> |
| Confidentiality (C) | N / L / H | <evidence> |
| Integrity (I) | N / L / H | <evidence> |
| Availability (A) | N / L / H | <evidence> |

### Score
- **Base Score:** _._
- **Severity:** None / Low / Medium / High / Critical
- **Vector:** `CVSS:3.1/AV:_/AC:_/PR:_/UI:_/S:_/C:_/I:_/A:_`

### Remediation SLA
- Target: <fix within N days>
- Interim mitigation: <what to do in the meantime, if any>

### Confidence
<high/medium/low> — <justification; flag any metric that is uncertain>
```
