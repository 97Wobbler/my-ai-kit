---
name: attack-trees
display_name: Attack Trees
class: lens
underlying_class: native
domain: security
source: Bruce Schneier, 1999
best_for:
  - Systematically enumerating attack vectors against a system or asset
  - Identifying which defenses stop which attacks
  - Prioritizing security investments by attack cost and impact
one_liner: "Structure attack paths as AND/OR trees to enumerate every infiltration vector."
---

# Attack Trees

## Overview

An attack tree is a hierarchical decomposition of a security goal (the attacker's objective) into progressively finer attack steps, connected by AND/OR logic gates. The root is the attacker's goal; leaves are elementary attacks (actions that require no further decomposition). AND nodes mean *all* child attacks must succeed; OR nodes mean *any* child attack succeeds. Practitioners use attack trees to enumerate threats exhaustively, identify single points of failure, cost defenses, and communicate security risk in a structured format. The discipline is the decomposition—most threat assessments stop at "someone could breach the perimeter" without mapping *how*.

## Analytical Procedure

### Phase 1 — Define the Goal and Scope

1. **State the attacker's objective in concrete, measurable terms.** Not "compromise the system" but "read all emails in user's mailbox without authentication" or "trigger a fraudulent transaction under $10k." This becomes your tree root.

2. **Define the attacker profile.** Specify:
   - **Capability:** Script kiddie, professional criminal, nation-state, insider?
   - **Access:** No network access? Physical proximity? Existing low-privilege account?
   - **Motivation:** Financial gain, espionage, sabotage, reputational damage?
   - **Time budget:** Hours, weeks, months?
   
   Attacks that are theoretically sound but require 10 years and a supercomputer are not equally dangerous to attacks that take a day and $100 of tools.

3. **Define scope boundaries.** Which systems/data/users are in scope? Is the attacker allowed to socially engineer employees? Perform supply-chain attacks? Use zero-days? Document these constraints explicitly.

### Phase 2 — Decompose the Goal

4. **Identify the top-level subgoals.** What are the 2-5 major ways the attacker could achieve the root goal? These are your first-level children. Use OR logic (attacker needs *any* of these).
   - Example: To read emails, attacker could (a) steal credentials, (b) compromise the mail server, (c) intercept traffic, (d) exploit a mail client vulnerability.

5. **For each subgoal, ask: "What must be true for this subgoal to succeed?"** Decompose further. Stop decomposing when you reach an action the attacker can execute directly (e.g., "guess password" or "run PoC exploit from public GitHub"). These are your leaf nodes.

6. **Choose AND vs. OR at each node.**
   - **OR node:** Attacker succeeds if any child attack works. Use when there are multiple independent paths.
   - **AND node:** Attacker must succeed at all children. Use when conditions must be satisfied sequentially or together.
   - Example: "Phishing email reaches user AND user opens attachment AND attachment executes" is an AND chain.

7. **For each node, annotate:**
   - **Effort:** Estimated time, cost, tools, or skill required (e.g., "minutes," "thousands of dollars," "requires 0-day").
   - **Likelihood:** If applicable given the attacker profile (high/medium/low). Likelihood of a brute-force guess depends on password policy, which you defined in Phase 1.
   - **Detection risk:** How likely the attack is to trigger monitoring or alerts.

### Phase 3 — Identify Defenses and Cut Points

8. **For each leaf node, identify all defenses that would prevent it.** Example: For "guess password," defenses include rate limiting, account lockout, multi-factor authentication, password complexity requirements.

9. **Mark which defenses are in place and which are missing.** If a defense is present, mark the leaf as "defended" but *do not* remove it from the tree—keep it to track coverage.

10. **Identify critical dependencies.** Are there nodes whose success enables multiple siblings? Are there attacks where a single defense stops many paths? These are high-leverage points for investment.

### Phase 4 — Analyze and Prioritize

11. **For each path from root to leaf, calculate attack cost.** Combine effort, likelihood, and detection risk into a single estimate. "This path: 2 hours + $500 + high detection risk = medium attractiveness to attacker."

12. **Identify paths with no defense.** These are critical gaps.

13. **Identify defenses that protect many paths.** Prioritize strengthening these.

14. **Check for AND nodes where one child is much harder than others.** These are bottlenecks—hardening the easy siblings may offer poor ROI if the hard one is the true blocker.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Root goal is stated in concrete, measurable terms (not vague) | Y/N |
| Attacker profile (capability, access, motivation, time budget) is defined | Y/N |
| All top-level subgoals are enumerated (none obvious are missing) | Y/N |
| Leaf nodes are truly elementary—they cannot be decomposed further without repeating a parent | Y/N |
| Every OR node has ≥2 children; AND nodes have ≥2 children | Y/N |
| Each node (non-leaf) has at least one defense identified | Y/N |
| Effort/cost is estimated for all leaves (not all are "unknown") | Y/N |
| At least one critical gap (undefended path) is explicitly called out | Y/N |

## Red Flags

- Root goal is stated vaguely ("steal data," "harm the company"). Without concrete metrics, you cannot prioritize defenses.
- Tree has only one level of decomposition below the root. The analyst stopped too early.
- All nodes are AND gates or all are OR gates. Real systems have mixed logic; consistent patterns suggest the attacker profile wasn't truly applied (e.g., "attacker always must do X then Y" is unrealistic).
- A leaf node is described as "exploiting a vulnerability" without specifying which one, how it works, or what access it requires. This is a placeholder, not an attack.
- No defenses are listed anywhere on the tree. Either the system is completely unprotected (possible but rare) or the analysis was incomplete.
- A defense is listed as in place but cost is not reduced accordingly. The tree is not reality-reflecting.
- Multiple high-effort paths are marked as equally critical. If one requires a nation-state and the other requires a script, your prioritization is broken.

## Output Format

```
## Attack Tree Analysis

**Goal (attacker's objective):**
<concrete, measurable statement>

**Attacker profile:**
- Capability: <script kiddie | organized | nation-state | insider | etc.>
- Access: <none | physical | low-privilege account | etc.>
- Motivation: <financial | espionage | disruption | etc.>
- Time budget: <hours | days | weeks | months | unlimited>

**Scope boundaries:**
- In scope: <systems, data, users>
- Allowed tactics: <social engineering | supply chain | zero-days | etc.>

### Tree Structure (text or ASCII diagram)

```
[Root Goal]
├─ [OR] Subgoal A
│  ├─ [AND] Condition A1
│  │  ├─ [Leaf] Attack a1a — Effort: <X> | Likelihood: <high/med/low> | Defended: Y/N
│  │  └─ [Leaf] Attack a1b — Effort: <X> | Likelihood: <high/med/low> | Defended: Y/N
│  └─ [Leaf] Attack a2 — Effort: <X> | Likelihood: <high/med/low> | Defended: Y/N
└─ [OR] Subgoal B
   └─ [Leaf] Attack b1 — Effort: <X> | Likelihood: <high/med/low> | Defended: Y/N
```

### High-Risk Paths (undefended or weakly defended)

| Path | Effort | Detection Risk | Status | Defense gap |
|---|---|---|---|---|
| Root → A → A1 → a1a | Low | Low | Undefended | No rate limiting on login |
| Root → B → b1 | Medium | High | Partially defended | Exploit requires specific version; patching schedule quarterly |

### Critical Dependencies

- Defense X (e.g., "MFA") prevents Y% of paths and is in place.
- Bottleneck: Node A requires access that Node B also requires; hardening access control stops both.
- Single point of failure: Node C; no redundancy.

### Recommendations

1. **Priority 1:** <Defense or architectural change with high impact and clear ROI>
2. **Priority 2:** <...>
3. **Priority 3:** <...>

### Confidence
<high | medium | low> — <justification: e.g., "high—attacker profile is realistic, decomposition is exhaustive to action level, all major defenses are inventoried"; or "medium—insider threat vectors may be underspecified; zero-day risk is assumed low without evidence">
```
