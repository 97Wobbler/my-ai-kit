---
name: OWASP API Security Top 10 (2023)
domain: security
source: OWASP Foundation, API Security Top 10 — 2023 Edition
underlying_class: native
best_for: Endpoint-by-endpoint vulnerability review of an HTTP/REST/GraphQL API
one_liner: "Audit API endpoints against the OWASP API Top 10 2023 categories and cluster findings by root cause."
---

# OWASP API Security Top 10 (2023)

## Overview
A practitioner-maintained list of the ten most impactful API vulnerabilities, refreshed every few years based on field data from bounty programs, incidents, and audits. Unlike abstract threat modeling, this lens is checklist-driven and endpoint-specific. Practitioners use it as the baseline review when they inherit an API and need to know the most common ways it can break before going deeper.

## Analytical Procedure

1. **Enumerate the API surface.** Produce a table of every endpoint: method, path, authentication required, roles permitted, request schema, response schema. If no such table exists, generate it from code or spec (OpenAPI/GraphQL schema) before proceeding — you cannot audit what you haven't listed.

2. **For each endpoint, walk through the 10 categories in order.** Apply the specific test for each:

### API1 — Broken Object Level Authorization (BOLA)
Test: For each endpoint that accepts an object ID (user_id, order_id, document_id), try accessing it with a session belonging to a different user who should not have access.
- Does the endpoint check that the caller owns the resource?
- Where is the check — controller, service, or data layer?
- Are IDs predictable (sequential integers) or unguessable (UUIDs)?
- Is there a tenant/org boundary that must also be enforced?

### API2 — Broken Authentication
Test: Map the login, session, and token refresh flows.
- Password policy: minimum entropy, breach corpus check (HIBP), lockout after failures?
- Session tokens: random, length, rotation on privilege change, invalidation on logout?
- JWT usage: algorithm allow-list, signature verification, expiration enforced?
- MFA: available, enforced for sensitive roles, not bypassable via account recovery?
- Credential storage: bcrypt/argon2/scrypt, not MD5/SHA/plain?

### API3 — Broken Object Property Level Authorization (BOPLA)
Combines legacy mass assignment and excessive data exposure.
- For write endpoints: does the server accept and persist any client-sent property, including ones not in the documented schema? (try adding `is_admin: true`)
- For read endpoints: does the response include fields the current role shouldn't see? (password hashes, internal IDs, PII of other users)

### API4 — Unrestricted Resource Consumption
Test: identify what each endpoint costs per request.
- Rate limits: per IP, per user, per endpoint, per cost-class?
- Payload size limits: body, query parameters, file uploads?
- Query complexity: GraphQL query depth, pagination max page_size, SQL LIMIT presence?
- Expensive operations: image processing, PDF generation, email sending — are they throttled or queued?
- Third-party call costs: does each request trigger paid downstream calls (SMS, LLM tokens, map tiles)?

### API5 — Broken Function Level Authorization
Test: for each endpoint, list roles that should be allowed. Then try each role against each endpoint and record actual behavior.
- Are role checks present on admin endpoints?
- Can an unauthenticated caller reach admin endpoints by guessing paths?
- Are debug/internal endpoints exposed in production builds?

### API6 — Unrestricted Access to Sensitive Business Flows
Test: identify flows that can be automated to cause damage even without technical vulnerabilities.
- Checkout/purchase: can a bot buy out inventory?
- Refund/credit issuance: can it be triggered without human review?
- Review/rating submission: can it be gamed by a script?
- Friend requests, invites, comments: can they flood other users?
- Mitigations: device fingerprinting, behavioral detection, throttling beyond simple rate limits?

### API7 — Server Side Request Forgery (SSRF)
Test: identify every endpoint where the server fetches a URL provided by the client (webhooks, URL preview, import-from-URL, avatar-from-URL).
- Does the server validate the URL against an allow-list or block internal IPs (169.254.169.254, 127.0.0.1, 10.0.0.0/8, etc.)?
- Does it follow redirects that could land on internal IPs?
- Does it honor DNS rebinding? (resolve once and cache the IP)

### API8 — Security Misconfiguration
Test: review deployment and runtime config.
- TLS: version, cipher suites, HSTS header?
- CORS: Access-Control-Allow-Origin value, credentials allowed?
- Headers: Content-Security-Policy, X-Frame-Options, X-Content-Type-Options, Referrer-Policy?
- Default credentials: on admin panels, databases, monitoring tools?
- Error responses: stack traces in production? Debug mode enabled?
- Cloud: public S3 buckets, open security groups, IMDSv1 still enabled?

### API9 — Improper Inventory Management
Test: find endpoints the security team doesn't know about.
- Are there staging/dev APIs reachable from the internet?
- Are there old API versions (v1, v2) still live but undocumented?
- Are there shadow APIs deployed by teams without going through review?
- Is the API gateway inventory in sync with what's actually deployed?
- Are third-party integrations inventoried with their scopes and data access?

### API10 — Unsafe Consumption of APIs
Test: for each third-party API your service calls, review how you handle its response.
- Do you validate the response schema, or trust whatever comes back?
- Do you pass third-party data directly into queries, templates, or HTML without sanitizing?
- Is the third-party endpoint pinned to a specific URL, or dynamically configurable?
- Is TLS verification enabled on outgoing calls?
- Are redirects from the third party followed blindly?

3. **Rate each finding** using CVSS v3.1 or a local equivalent. Include attack vector, privileges required, and scope.

4. **Cluster findings by root cause.** Ten findings across three endpoints may all share one broken middleware. Fixing the middleware is one action, not ten.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Complete endpoint inventory exists before testing | Y/N |
| Every endpoint was walked through all 10 categories | Y/N |
| BOLA (API1) was tested with actual cross-account access attempts, not just code review | Y/N |
| Inventory (API9) includes non-production environments | Y/N |
| Findings are clustered by root cause, not just listed flat | Y/N |
| Each finding has CVSS or equivalent score | Y/N |

## Red Flags

- Only some categories have findings. OWASP Top 10 is top 10 because they're all common — missing findings in half the categories usually means they weren't actually tested.
- BOLA is "covered by JWT" with no test. JWT authenticates; it does not authorize object-level access. This is the #1 most common real-world API bug.
- Rate limiting is "implemented" but only at the edge (load balancer). Per-user and per-endpoint limits aren't in place, so authenticated abuse is unconstrained.
- "We use HTTPS" is the entire security misconfiguration section. Many headers and cloud defaults are missing.
- Third-party APIs are out of scope. API10 exists because they're the source of many breaches — refusing scope is a finding in itself.

## Output Format

```
## OWASP API Security Top 10 Assessment

### Endpoint Inventory
| Method | Path | Auth | Roles | Notes |
|--------|------|------|-------|-------|
| ...    | ...  | ...  | ...   | ...   |

### Findings by Category

#### API1 — BOLA
- <endpoint> — <finding> — CVSS <score> — <evidence>
- ...

#### API2 — Broken Authentication
- ...

... (all 10 categories, even if empty — if empty, state "verified, no findings" with what was checked)

### Root-Cause Clusters
1. <cluster name> — affects <N findings> — fix: <single remediation>
2. ...

### Prioritized Remediation List
| Priority | Finding(s) | Effort | Fix |
|---|---|---|---|
| ... | ... | ... | ... |

### Confidence
<high/medium/low> — <justification>
```
