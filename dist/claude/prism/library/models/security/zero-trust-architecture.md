---
name: zero-trust-architecture
display_name: Zero Trust Architecture
class: model
underlying_class: native
domain: security
source: NIST, "Zero Trust Architecture," SP 800-207, 2020
best_for:
  - Explaining how attack surface and lateral movement scope shrink as trust granularity increases
  - Predicting security posture improvement as implicit-trust assumptions are replaced with continuous verification
  - Diagnosing which trust boundaries are doing load-bearing work in a system
one_liner: "Continuous verification on every access shrinks attack surface and blast radius."
---

# Zero Trust Architecture

## Overview

Zero Trust Architecture is a security systems model that claims the risk
posture of a system improves monotonically as the architecture moves from
**implicit trust (access granted on network position or identity alone)** to
**explicit continuous verification (every access request is evaluated
against policy, regardless of source or prior grants)**. The model is both
diagnostic and prescriptive: it explains *why* perimeter-based security
fails under modern conditions (remote work, supply-chain compromise,
insider threats, lateral movement), and it predicts that architectures
requiring re-authentication and re-authorization on *every* access will
exhibit smaller blast radius, slower attack propagation, and lower dwell
time on average. The model is explanatory and mechanistic — it does not
dictate how to implement verification, only that continuous verification
reduces exploitability.

## Core Variables and Relationships

The core dynamic is the relationship between **trust implicit in system
design** and **exploitable attack surface**:

1. **Trust implicit in architecture** — the set of access decisions made
   once rather than per-transaction. Lower implicit trust → larger explicit
   verification overhead, but smaller attack surface.
   - Network segmentation assumptions (perimeter as trust boundary)
   - Identity/authentication at session entry vs. per-transaction
   - Role-based access control (RBAC) without runtime context
   - Implicit trust in internal network traffic
   - Implicit trust in physical location or device ownership

2. **Access decision granularity** — how finely the system evaluates each
   access request. Finer granularity → more verification events, more
   policy enforcement points.
   - Per-request verification vs. per-session
   - Factors evaluated per request: identity, device state, network
     context, behavior history, time-of-day, risk score
   - Attribute-based access control (ABAC) vs. role-based
   - Real-time signals available at decision time (MFA, endpoint
     security status, network location)

3. **Lateral movement friction** — the number of independent verification
   events an attacker must clear to move from one resource to another.
   Higher friction → slower propagation.
   - Network micro-segmentation (resource-to-resource gates)
   - Transport security (encryption, mutual TLS)
   - Identity verification (re-authentication required between zones)
   - Behavior monitoring (anomalous access patterns trigger blocking)
   - Least-privilege defaults (no implicit access grants)

4. **Monitoring and logging scope** — the coverage of decision logs and
   anomaly signals that feed back into policy. Wider scope → faster
   detection of deviation from baseline.
   - All access decisions logged with context (user, resource,
     permission granted/denied, risk factors)
   - Behavioral baselines per user/resource
   - Real-time alerting on anomaly thresholds
   - Correlation across access events to detect lateral movement

5. **Blast radius on compromise** — the set of resources an attacker can
   reach after compromising a single principal (user, service, device).
   Lower blast radius → lower damage ceiling.
   - Blast radius = f(implicit trust) − f(verification friction)
   - Single compromised credential grants access to: all resources the
     principal has ever accessed + all resources reachable via lateral
     movement without re-verification
   - Micro-segmentation and per-request verification shrink this set
     dramatically

The core relationship is qualitative:

    Reduction in exploitable attack surface ∝ increase in
    implicit-trust removal + verification granularity + monitoring coverage

Systems with near-zero implicit trust (every access re-verified, behavior
monitored, anomalies trigger blocking) force attackers to clear a new
authorization gate for each lateral move, and log each attempt — making
detection probability very high and dwell time very low.

## Key Predictions

- **A system that requires re-authentication and device-context verification
  on every cross-network access (including intra-datacenter) will exhibit
  dwell times 2–10× shorter than a perimeter-based system, even if the
  identity verification mechanism itself is equally compromisable.** The
  gain is from mandatory re-verification at each boundary, not from
  stronger cryptography.

- **When a principal (user or service account) is compromised, the attacker's
  reach in a zero-trust system is bounded by the least-privilege scope of
  that principal, not by network position.** A compromised service account
  with read-only access to a specific database cannot escalate to admin-level
  reach across the company network; it can only access that database until
  re-authentication is triggered.

- **The blast radius from a single-credential compromise shrinks by 1–2
  orders of magnitude if lateral movement requires independent re-verification
  at each micro-segment boundary.** In contrast, a perimeter-based system
  where internal network position is implicitly trusted enables the attacker
  to move freely once inside.

- **Behavioral anomaly detection (flagging access patterns that deviate from
  baseline) becomes effective only when access decisions are logged with
  sufficient granularity and real-time.** Batch-logged, coarse-grained access
  (daily logs, binary grant/deny) is nearly useless; continuous fine-grained
  logging (per-request context: user, resource, device, network, time, risk
  score) enables detection of low-and-slow attacks.

- **The security gain from zero trust plateaus if policy evaluation is fast
  but coverage is incomplete** — e.g., verifying all employee access but not
  service-to-service calls, or monitoring network traffic but not direct
  cloud-storage access. Unmonitored paths become high-value attack vectors.

## Application Procedure

Instantiate the model against a concrete system or organization to assess
its current zero-trust maturity and predict security improvement from moving
toward zero trust.

1. **Define the scope of the system.** What assets are you protecting (data,
   compute, network)? What principals access those assets (users, services,
   devices)? What is the threat model (insider, supply-chain, accidental
   breach)?

2. **Map implicit trust assumptions in the current architecture.**
   - Which decisions are made once (at session start, device enrollment,
     network entry) rather than per-transaction?
   - What trust is granted by network position (VPN, intranet, corporate
     network)?
   - What trust is granted by identity alone, without runtime context
     (RBAC roles, static group membership)?
   - What access paths are unmonitored or unlogged?

3. **Identify verification gaps.** For each major resource category
   (databases, APIs, file systems, cloud services), what verification
   happens on *every* access vs. what is implicit?
   - Is re-authentication required, or just initial login?
   - Is device state (encryption, patching, antivirus) checked per-access?
   - Is network context (location, VPN status) verified per-request?
   - Is behavioral anomaly checked (deviation from user's baseline)?

4. **Estimate lateral movement friction.** Starting from a single
   compromised principal, how many independent authorization gates must the
   attacker clear to reach: (a) the most sensitive data, (b) another high-value
   account, (c) a critical service?
   - Count network segments that require independent authentication
   - Count resource-level access-control boundaries
   - Estimate time and detection probability per boundary cleared

5. **Assess monitoring coverage and logging granularity.**
   - What fraction of access decisions are logged (target: 100%)?
   - What context is logged per decision (user, resource, outcome, risk
     factors)?
   - How quickly are behavioral anomalies detected?

6. **Read off zero-trust maturity and predicted gain.**
   - Maturity level: % of access paths subject to per-request verification +
     per-request risk assessment + real-time monitoring
   - Predicted improvement in dwell time, blast radius on compromise, and
     detection probability

7. **Check boundary conditions** (below). If any apply, note where the model
   may overestimate achievable security gain.

## Boundary Conditions

Zero Trust Architecture is a powerful model for *reducing* the exploitability
of compromised credentials, but it does not address all security problems and
can break down in several ways:

- **Weakness in the verification mechanism itself.** If re-authentication is
  based on a weak signal (single-factor password, or device fingerprint that
  is easy to spoof), zero trust buys you nothing — every gate is just as
  easy to bypass. The model assumes verification is reasonably robust; if the
  authorization oracle is broken, the whole architecture fails. Complement
  with threat modeling of the verification pathway itself.

- **Coverage gaps.** Zero trust requires *all* access paths to be
  instrumented for continuous verification. If any major pathway is
  unmonitored (e.g., shared cloud storage, legacy system not integrated into
  policy engine, physical USB access to servers), attackers will route around
  the verification gates. The model's benefit is only as good as the least
  monitored access path.

- **Cost of verification overhead.** Zero trust requires per-request (or
  near-per-request) evaluation, which adds latency and infrastructure cost.
  For high-volume, latency-sensitive workloads (low-latency trading, real-time
  analytics), this overhead may be unacceptable. The model predicts security
  gain but does not account for the performance/cost tradeoff.

- **Insider threats with legitimate access.** Zero trust is designed to catch
  *unauthorized* access and lateral movement. An insider with a legitimate
  account and authorization to access sensitive data can exfiltrate it, and
  zero trust will not block it — it will only log it. Detecting insider abuse
  requires behavioral analysis and anomaly detection beyond the core model;
  pure zero trust is not sufficient.

- **Phishing and social engineering.** Zero trust can slow down lateral
  movement after a credential is stolen, but it does not prevent the
  credential theft in the first place. A user phished into revealing their
  password + MFA device loses both, and re-authentication will succeed
  (attacker has the credentials). Complement with user training, browser
  isolation, and endpoint security.

- **Supply-chain and third-party integrations.** If the system integrates
  deeply with third-party APIs or cloud services that do not support
  fine-grained real-time authorization, you cannot apply zero trust end-to-end
  — trust boundaries will still exist at integration points. The model assumes
  control over all verification gates; it does not handle federated or
  loosely-coupled systems well.

## Output Format

```
## Zero Trust Maturity Assessment: <system/organization name>

**Scope:** <assets, principals, threat model>
**Current architecture:** <brief characterization: perimeter-based, hybrid, zero-trust-forward>
**Assessment date:** <date>

### Implicit trust assumptions (current)
| Trust boundary | Scope | Verification trigger |
|---|---|---|
| Network (perimeter) | All intra-network traffic | Session entry (VPN/login) |
| Identity (RBAC) | Resource access | Authentication at login |
| Device | Network access | Enrollment or login |
| (other implicit trusts) | | |

### Access decision granularity
| Access path | Verification timing | Context evaluated | Coverage |
|---|---|---|---|
| User→Resource | Per-session / per-request | Identity only / +device / +behavior | % instrumented |
| Service→Service | Per-call / implicit | Identity / mTLS only | % instrumented |
| (other paths) | | | |

### Lateral movement friction estimate
- From compromised <user/service account>:
  - Boundaries to cross (network segments, resource-control gates): <N>
  - Re-authentication required per boundary: <yes/no>
  - Estimated time to reach <target resource>: <X minutes>
  - Estimated detection probability per boundary: <low/medium/high>

### Monitoring and logging coverage
- % of access decisions logged: <X%>
- Context logged per decision: <user, resource, device, network, time, risk score, ...>
- Real-time anomaly detection: <yes / partial / no>
- Baseline coverage (% of principals with behavioral profiles): <X%>

### Zero Trust maturity
- Implicit-trust removal: <level 0–5>
- Verification granularity: <level 0–5>
- Monitoring coverage: <level 0–5>
- **Composite maturity:** <0–5 or descriptive level: nascent / developing / mature / advanced>

### Predicted security improvement (moving toward zero trust)
- Dwell time reduction: <estimated factor or qualitative>
- Blast radius reduction on credential compromise: <estimated factor>
- Detection latency for lateral movement: <current vs. target>

### Boundary-condition notes
<which boundary conditions apply (weak verification mechanism, coverage gaps,
insider threat scope, etc.) and what complementary controls are needed>

### Confidence: high | medium | low
<reasoning: coverage of attack surface + robustness of verification mechanism
+ organizational ability to monitor and enforce policy + threat model fit>
```
```
