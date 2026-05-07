---
name: fmea
display_name: Failure Mode and Effects Analysis
class: lens
underlying_class: native
domain: security
source: Ford Motor Company, 1960s; adapted for safety-critical systems (IEC 60812, MIL-STD-1629A)
best_for:
  - Identifying and ranking risks before deployment
  - Prioritizing mitigation work in resource-constrained environments
  - Building accountability for threat modeling in engineering teams
one_liner: "Failure Mode and Effects Analysis — systematically enumerate failure modes and prioritize via Severity × Occurrence × Detection."
---

# Failure Mode and Effects Analysis

## Overview

FMEA is a structured method for identifying what can go wrong in a system, rating each failure by severity (how bad if it happens), occurrence (how likely), and detection (how likely you catch it before users do), then multiplying these three scores into a Risk Priority Number (RPN). The system fails when RPN exceeds a threshold or when a single failure is unacceptable regardless of RPN. Practitioners use FMEA to avoid shipping obvious gaps and to justify risk acceptance decisions to stakeholders. The discipline is the enumeration — most teams skip it or delegate it to a single person, losing the breadth that comes from structured disagreement.

## Analytical Procedure

### Phase 1 — Enumerate Failure Modes

1. **Define the system boundary.** Write the inputs, outputs, and interfaces the system exposes. For a security context, include: authentication endpoints, cryptographic operations, data storage, network transit, privilege boundaries, and audit/logging mechanisms. Do not include implementation details yet.

2. **For each component or process in the boundary, ask: "What can fail here?"** Do not filter for likelihood. Generate the list:
   - Function failure: the component does nothing, or only partially
   - Function reversal: the component does the opposite (e.g., deny instead of allow)
   - Premature or delayed activation
   - Unintended activation
   - Loss of information or loss of integrity
   - Incorrect output value or type
   - Cascading failure (this component breaks and takes down a dependent)
   
   Write each failure mode as a verb phrase: "Cryptographic key is not rotated," "Authentication token is accepted after expiration," "Audit log entry is deleted without authorization."

3. **For each failure mode, describe the immediate effect.** What happens when this failure occurs? Be specific:
   - Bad: "Security is compromised."
   - Good: "An attacker can authenticate as an arbitrary user by reusing an expired token."

4. **For each failure mode and effect, trace to the end-user or operator consequence.** What is the worst-case outcome?
   - Confidentiality breach: what data is exposed to whom?
   - Integrity breach: what is modified or destroyed?
   - Availability loss: what service stops or degrades?
   - Regulatory/legal consequence: what compliance requirement is violated?

### Phase 2 — Rate Severity, Occurrence, and Detection

5. **Assign a Severity score to each failure mode.** Use the scale below. This is the impact *if the failure occurs*, not the likelihood. Rate from the perspective of the user or operator who would be harmed.

   | Score | Severity | Criteria |
   |---|---|---|
   | 9–10 | Critical | Breach of confidentiality, integrity, or availability that affects core mission; regulatory violation; data loss; compromise of multiple users |
   | 7–8 | High | Significant breach affecting a subset of users or one user's sensitive data; undetected tampering; loss of audit trail |
   | 5–6 | Moderate | Partial breach or degradation; user detects issue; workaround exists; single user affected |
   | 3–4 | Low | Cosmetic or minimal impact; easily reversible; no confidentiality or integrity loss |
   | 1–2 | Negligible | No impact or impact so minor it goes unnoticed |

6. **Assign an Occurrence score to each failure mode.** This is how likely it is to occur *before detection*. If you have no data, make a reasoned guess based on attack surface, code complexity, or operational frequency. Use the scale below.

   | Score | Likelihood | Criteria |
   |---|---|---|
   | 9–10 | Very High | Occurs in production regularly (>1 per month); trivial to trigger; active exploit known; part of normal operational load |
   | 7–8 | High | Occurs occasionally (1-12 per year); can be triggered by a determined attacker; requires moderate skill |
   | 5–6 | Moderate | Occurs rarely (once per year or less); requires specific conditions or access; not yet observed in production |
   | 3–4 | Low | Theoretically possible but has not occurred; requires multiple preconditions; no known attack vector |
   | 1–2 | Very Low | So unlikely it's not worth mitigating; requires extreme conditions or multiple simultaneous failures |

7. **Assign a Detection score to each failure mode.** This is how likely you will *catch it before a user is harmed*. Consider both automated and manual detection.

   | Score | Likelihood | Criteria |
   |---|---|---|
   | 9–10 | Very Low | Detection is passive; system continues to operate unaware; failure is hidden or delayed; monitoring is absent or ineffective |
   | 7–8 | Low | Detection requires manual investigation or specific conditions; logging exists but is not actively monitored; days or weeks to notice |
   | 5–6 | Moderate | Detection happens but with latency (hours); alerting is present but not always reliable; requires correlation across data sources |
   | 3–4 | High | Immediate or near-immediate detection (seconds to minutes); alert is unambiguous; strong detection mechanism |
   | 1–2 | Very High | Failure is detected before activation or is impossible to miss; built-in safeguard; multiple independent detection paths |

8. **Calculate RPN for each failure mode:** RPN = Severity × Occurrence × Detection. The range is 1–1000. Document this calculation.

### Phase 3 — Prioritize and Decide

9. **Rank all failure modes by RPN (descending).** The top items are your priorities. Typical decision thresholds:
   - RPN ≥ 300: Investigate and mitigate before deployment (unless Severity ≤ 4).
   - RPN 100–299: Plan mitigation; may be acceptable if cost is very high or Severity is low.
   - RPN < 100: Accept the risk or monitor in production.
   - Any failure with Severity 9–10: Mitigate regardless of RPN.

10. **For each failure mode in the top tier, define a mitigation strategy.** Document:
    - What will be changed (code, configuration, process, monitoring)?
    - How will the change prevent or detect the failure?
    - Who is responsible and by when?
    - How will you verify the mitigation worked?

11. **Re-rate Occurrence and Detection after mitigation is implemented.** Recalculate RPN to confirm that the risk is acceptable.

## Evaluation Criteria

| Check | Pass |
|---|---|
| System boundary is explicitly defined (inputs, outputs, interfaces, components) | Y/N |
| Failure modes are enumerated across all major components | Y/N |
| At least one person not on the design team reviewed the list | Y/N |
| Each failure mode includes immediate effect and end-user consequence | Y/N |
| Severity, Occurrence, and Detection are each justified (not guessed) | Y/N |
| RPN is calculated correctly for all modes | Y/N |
| Failures with Severity 9–10 have mitigations or explicit risk acceptance | Y/N |
| At least one mitigation plan includes verification criteria | Y/N |

## Red Flags

- All Occurrence scores are 1–2. Either the system is trivial or the team is in denial about attack surface. Push back.
- All Detection scores are 1–2. This is common and usually wrong — most teams detect failures much later than they think. Be conservative.
- No failures with Severity 7+ are identified. The team is not thinking about the bad case. Rerun the brainstorm with an adversary present.
- The same person lists all failure modes. Breadth is lost. Rerun with a team.
- Mitigations are listed as "improve monitoring" or "add logging" without specifics. These are placeholders, not mitigations.
- RPN > 200 but no mitigation plan exists. The team is accepting the risk without documenting it.
- A failure mode's Severity or Occurrence is rated low because "we'll just fix it in the next release." That's not a reason to lower the rating; it's a reason to accelerate the release or add a temporary control.

## Output Format

```
## FMEA Report

**System:** <name and boundary>
**Evaluated by:** <names>
**Date:** <YYYY-MM-DD>

### Failure Modes (Ranked by RPN)

| ID | Failure Mode | Effect | Consequence | Severity | Occurrence | Detection | RPN | Mitigation |
|---|---|---|---|---|---|---|---|---|
| 1 | <mode> | <immediate effect> | <end-user impact> | <1-10> | <1-10> | <1-10> | <S×O×D> | <action or "Accept"> |

### Critical Failures (Severity 9–10, Regardless of RPN)

| ID | Failure Mode | Severity | Status | Owner | Target Date |
|---|---|---|---|---|---|
| <...> | <...> | <...> | <Open / In Progress / Closed> | <...> | <...> |

### Mitigation Plans (RPN ≥ 300 or Severity 9–10)

**Failure Mode:** <description>
**Current RPN:** <value>
**Proposed Change:** <specific, measurable action>
**Verification:** <how will you confirm the change worked?>
**Owner:** <name>
**Target Date:** <YYYY-MM-DD>

---

### Confidence
<high | medium | low> — <justification: e.g., "High if team included security and operations perspectives and Occurrence/Detection ratings were anchored to data. Medium if ratings are estimates. Low if enumeration was incomplete or team was homogeneous.">
```
