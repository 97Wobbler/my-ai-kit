---
name: STRIDE Threat Modeling
domain: security
source: Loren Kohnfelder & Praerit Garg, Microsoft, 1999 (original memo); formalized by Microsoft SDL
underlying_class: native
best_for: Systematic threat enumeration for a system or feature at design time, before code is written
one_liner: "Enumerate threats systematically via DFD element × six categories (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege)."
---

# STRIDE

## Overview
STRIDE forces you to walk every component and data flow of a system and ask, for each, whether six specific categories of threat apply. The structure is its value — ad-hoc threat brainstorming leaves gaps; STRIDE makes gaps visible because an empty column in the matrix either means "no threat" (defensible) or "didn't check" (a failure). Practitioners use it early in design and again whenever trust boundaries change.

## Analytical Procedure

1. **Draw or describe the system as a Data Flow Diagram (DFD):**
   - **External entities** (users, third-party APIs — things outside your trust boundary)
   - **Processes** (your services, functions, binaries)
   - **Data stores** (databases, queues, caches, files)
   - **Data flows** (the arrows connecting all of the above)
   - **Trust boundaries** (dotted lines crossing data flows where identity/privilege changes)
   If you can't draw this cleanly, STRIDE can't be applied — stop and clarify the architecture first.

2. **For EACH element in the DFD, ask the six STRIDE questions.** Not every category applies to every element type — use the matrix below as a filter:

   | Element type | S | T | R | I | D | E |
   |---|---|---|---|---|---|---|
   | External entity | ✓ | | ✓ | | | |
   | Process | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
   | Data store | | ✓ | ✓ (audit logs) | ✓ | ✓ | |
   | Data flow | | ✓ | | ✓ | ✓ | |

3. **Apply the category-specific checks:**

### S — Spoofing (identity)
- Is there an authentication mechanism on this element?
- Can an attacker present credentials that belong to someone else? (stolen tokens, replay, credential stuffing)
- Is there mutual authentication for server-to-server flows, or only client→server?
- Are identity tokens bound to a context (device, session, transport) or freely transferable?
- Is there any component that trusts the caller's asserted identity without verification?

### T — Tampering (integrity)
- Can the data in transit be modified? (no TLS, weak TLS, mTLS not enforced)
- Can data at rest be modified without detection? (missing integrity checks, unsigned artifacts)
- Can the attacker modify the code running on this component? (write-access to binaries, unsigned updates, loadable plugins)
- Are configuration files, feature flags, or database rows write-protected from the threat actors who shouldn't touch them?

### R — Repudiation (audit)
- Is there an audit log for this action?
- Can the audit log itself be modified or deleted by the actor being audited?
- Are logs written before the action is confirmed, or after? (before = can log without doing; after = can do without logging)
- Is the log entry tied to a strong identity (not just an IP)?
- Does the log contain enough context to reconstruct what happened, not just that something happened?

### I — Information Disclosure (confidentiality)
- What data does this component handle? Classify it (public / internal / confidential / secret).
- Is each data class encrypted in transit? At rest?
- Does this component log sensitive data? Error messages? URLs?
- Are there side-channels (timing, cache, response length) that leak information?
- Are error messages revealing internal structure (stack traces, DB errors, path disclosure)?

### D — Denial of Service
- Is there a rate limit on this entry point? By IP? By identity? By cost?
- Can a single malformed request consume disproportionate resources? (regex DoS, zip bomb, recursive JSON)
- Are upstream dependencies protected with circuit breakers?
- Is there a quota on the resource this component allocates? (memory, disk, connections, threads)
- Can an authenticated user degrade the experience of other users via shared state?

### E — Elevation of Privilege
- Are there roles/permissions? Where are they checked?
- Is permission checking done at the controller layer, the service layer, or the data layer? (answer should be: the data layer at minimum)
- Can a low-privilege user invoke a high-privilege function directly? (IDOR, hidden endpoints, debug routes)
- Are there any "admin backdoors" (hardcoded credentials, impersonation, debug flags)?
- Is there a privilege separation between the process owner and the application user?

4. **Record every applicable threat as a finding.** Do not pre-filter for feasibility — that's the job of the rating step.

5. **Rate each finding:** Likelihood (H/M/L) × Impact (H/M/L). Use DREAD, CVSS, or a simple 3×3. Be explicit about the scoring system.

6. **Propose at least one mitigation per High/Medium finding.** Mitigations are named, actionable, and testable (e.g., "enforce TLS 1.3 with mTLS on service-to-service calls" — not "improve security").

## Evaluation Criteria

| Check | Pass |
|---|---|
| A complete DFD (or equivalent) was produced before STRIDE was applied | Y/N |
| Every applicable element × category cell was checked (not just a subset) | Y/N |
| Trust boundaries are explicitly marked | Y/N |
| Every finding has a likelihood and impact rating | Y/N |
| Every High finding has a proposed mitigation | Y/N |
| Mitigations are testable (can be verified after implementation) | Y/N |

## Red Flags

- Zero findings in one or more categories. Possible, but verify it's "checked and none apply," not "didn't check." Annotate explicitly.
- Most findings cluster in one category (usually S or I). Other categories were skimmed. Redo the underrepresented ones.
- Mitigations of the form "validate input" or "use HTTPS everywhere." These are not mitigations, they're slogans. Name the specific mechanism.
- No data classification was done before the I-category. Without classifying the data, disclosure impact can't be rated.
- Privilege checks are all at the controller/UI layer. This is a known anti-pattern — IDOR attacks bypass it trivially.

## Output Format

```
## STRIDE Threat Model

### System Scope
<1-paragraph description + attached DFD or structured description>

### Trust Boundaries
- <boundary 1>: between <component A> and <component B>, governed by <auth mechanism>
- ...

### Threats

| ID | Element | Category | Threat | Likelihood | Impact | Mitigation |
|----|---------|----------|--------|------------|--------|-----------|
| T01 | auth-service | S | Token replay across sessions | H | H | Bind tokens to TLS session via token binding RFC 8471 |
| T02 | ... | ... | ... | ... | ... | ... |

### High-Priority Findings
1. <ID> — <one-line summary> — owner: <team>
2. ...

### Unchecked Cells (explicitly noted)
- <element> × <category>: reason it was skipped
- ...

### Confidence
<high/medium/low> — <justification>
```
