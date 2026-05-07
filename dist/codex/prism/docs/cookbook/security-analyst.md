# Security Analyst — Composition Recipe

> **This is NOT an executable agent config.** It is a composition recipe — a
> narrative explaining how a set of Prism instruments can be combined for a
> given task. To actually build an agent, use Claude Code's native agent
> creation mechanism (`/agents` or a hand-written `.claude/agents/*.md`) and
> reference the instruments below manually. Prism is a catalog; the agent
> runtime lives in Claude Code.

## Persona / purpose

A security reviewer for API services who flags design- and implementation-
level vulnerabilities before code reaches production. This recipe produces
architecture-anchored threat findings, each one scored and tagged with
confidence, with an explicit gate against the common failure modes of
security review (malice-first explanations, rip-out recommendations,
single-cause root-causing).

## Instruments used

### Lenses
- `library/lenses/security/stride.md` — **usage: always** — enumerate
  threats by category (Spoofing, Tampering, Repudiation, Info disclosure,
  DoS, Elevation) at the architectural level.
- `library/lenses/security/owasp-top10.md` — **usage: always** — walk the
  API endpoint-by-endpoint through the top 10 web/API risks.
- `library/lenses/security/cvss-scoring.md` — **usage: always** — attach
  a numeric severity (Base score) to every finding that survives STRIDE
  and OWASP.
- `library/lenses/general/rumsfeld-matrix.md` — **usage: when-relevant** —
  surface known-unknowns and unknown-unknowns as investigation gaps
  (not as findings in themselves).
- `library/lenses/general/first-principles.md` — **usage: on-request** —
  reserved for when the user explicitly wants to question the system's
  basic design assumptions.

### Frames
- `library/frames/general/cynefin.md` — **usage: when-relevant** — sort
  components into Clear / Complicated / Complex so that downstream CVSS
  confidence can be calibrated by problem domain.

### Heuristics
- `library/heuristics/general.md` — **usage: always** — Hanlon's Razor,
  Chesterton's Fence, Occam's/Hickam's pair, applied as a sanity gate
  over the top findings.

## Why this composition

STRIDE, OWASP Top 10, and CVSS form a three-legged stool that each alone
is insufficient. STRIDE is architectural and catches structural issues
(e.g., missing repudiation controls) that endpoint-level scans cannot
see. OWASP is endpoint-concrete and catches the exploit patterns STRIDE
is too abstract to name. CVSS is neither — it is a scoring scheme that
forces a common severity vocabulary across the other two so that the
output is sortable and triageable. Running just one or two of the three
produces a review with blind spots or no priority order.

The `rumsfeld-matrix` inclusion is the non-obvious move. Security
reviews fail most often not because a known threat was missed, but
because an unknown trust boundary existed and nobody thought to look for
it. Rumsfeld's matrix is cheap insurance against that failure mode, but
it is only worth running when the system has genuine novelty (new
dependencies, unclear ownership, missing docs) — hence `when-relevant`
rather than `always`.

Cynefin is included at the classify step precisely to calibrate CVSS.
In a Complex component (emerging architecture, unclear contracts), CVSS
Base scoring is weakly diagnostic and overstates confidence; flagging
the Cynefin category prevents the reviewer from treating all CVSS
numbers as equally trustworthy.

The general heuristics bundle exists to kill three specific review
pathologies: (1) framing misconfiguration as malice, (2) recommending
"just remove this check" without considering why it was there, and (3)
attributing a compound failure to a single cause. None of the security
lenses prevent these; they are a final-stage cognitive gate.

Trade-off: `first-principles` is `on-request` only. A security review
that questions the system's reason for existing is valuable, but it is
not what stakeholders usually want from a pre-production gate, so
invoking it without consent derails the deliverable.

## Workflow sketch (7-step pipeline)

| Step | Class(es) used | What happens |
|------|---------------|--------------|
| 1. Triage | — | Read the target system, confirm STRIDE/OWASP/CVSS apply, decide whether rumsfeld-matrix is warranted. |
| 2. Classify | Frames (Cynefin) | Tag components Clear/Complicated/Complex; note Complex components for weakened CVSS confidence. |
| 3. Analyze | Lenses (STRIDE → OWASP → CVSS, optionally Rumsfeld) | Enumerate, prioritize, score. Rumsfeld findings become investigation gaps, not vulnerabilities. |
| 4. Model-interpret | — | Not used by this recipe. |
| 5. Critical-read | — | Not used by this recipe. |
| 6. Sanity-gate | Heuristics (general bundle) | Apply Hanlon / Chesterton / Occam-Hickam to the top findings; amend or drop those that don't survive. |
| 7. Synthesize | All | Cluster findings by root cause; findings that both STRIDE and OWASP flag at the same component are high-confidence; surface tensions between frameworks. |
