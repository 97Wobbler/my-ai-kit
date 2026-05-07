---
name: "debate"
description: Instrumented multi-agent debate where each participant analyzes a document, proposal, or problem through explicit Prism instruments by default. Three modes — review, ideate, solve. Infers mode from context when no flag is given. Use `--persona-only` only when the user explicitly wants unguided persona debate. Triggers on "analyze from multiple perspectives", "have agents debate", "debate", "consensus", "multi-angle review", "find solutions", "brainstorm ideas", "ideation session"
targets:
  - codex
capabilities:
  user_questions: required
  file_edits: false
  subagents: required
  plan_mode: none
  network: false
  validation: optional
runtime_overrides:
  claude: |
    In Claude Code, plugin skills are invoked with the plugin namespace, for example `/prism:debate`.
    Use Claude Code's native user-question and subagent/task orchestration capabilities when the workflow requires participant confirmation or parallel persona analysis.
  codex: |
    In Codex, plugin skills are invoked through the installed skill name, for example `$debate`, `use prism:debate`, or a natural-language request that matches this skill.
    Use `request_user_input` only in Plan Mode. In Default mode, ask concise plain-text questions and wait when participant selection is blocking.
    Spawn subagents only when the user explicitly asks for debate, multiple agents, or parallel agent work; otherwise explain the missing prerequisite and stop.
outputs:
  codex: skills/debate/SKILL.md
---

# debate

An orchestration engine where multiple instrument-grounded agents
independently analyze a target, with the orchestrator controlling rounds
and driving consensus, convergence, or divergence.

Default behavior is **instrumented debate**: every participant must
receive explicit Prism instrument paths and read directives before being
spawned. Pure persona debate is allowed only when the user explicitly
passes `--persona-only` or says they want persona-only / no instruments.

---

## Modes

| Mode | Purpose | Exit condition | Typical scenarios |
|---|---|---|---|
| `review` | Multi-perspective analysis with judgment | Consensus reached or MAX_ROUNDS exhausted | Code review, design review, PRD review |
| `ideate` | Maximize idea divergence and expansion | MAX_ROUNDS exhausted (no convergence judgment) | Brainstorming, ideation, exploratory analysis |
| `solve` | Propose solutions and converge on the best | Convergence reached or MAX_ROUNDS exhausted | Bug resolution, incident response, strategy planning |

### Mode selection rules

1. **Explicit flag** — if the user specifies `--review`, `--ideate`, or `--solve`, enter that mode immediately
2. **Context inference** — without a flag, infer from signals:
   - Analysis / review / judgment / assessment → `review`
   - Ideas / divergence / brainstorming / exploration → `ideate`
   - Fix / resolve / alternatives / strategy → `solve`
3. **Default to `review`** when uncertain — the most general-purpose mode
4. **Mode transition** — after `review` completes, if unresolved issues remain and the user asks "find solutions too," transition to `solve` is natural. **Never auto-transition** — always confirm with the user first

### Instrumentation mode rules

1. **Default to instrumented mode.** Treat every debate as Prism
   instrumented unless the user explicitly opts out.
2. **Persona-only opt-out.** Enter persona-only mode only when the user
   passes `--persona-only`, says "persona-only," or says "without
   instruments."
3. **No silent fallback.** If appropriate instruments cannot be found or
   resolved, stop and tell the user what is missing. Do not continue as a
   persona-only debate unless the user explicitly opts out.

---

## Prerequisites

- **Target**: document, text, code, proposal, problem statement, etc.
- **Participating agents**: composed from one or more of these sources:
  - Agent files in `.claude/agents/` (project or user root), if the user names them
  - Automatically composed instrument-grounded participants inferred from the target
  - Prism instruments (all classes: `lens`, `frame`, `model`, `stance`, `heuristic`) loaded via `/prism fetch`
- **If no agents are specified**, infer 3-5 useful participants from the
  target and instrument set. Ask the user only when the target is too
  vague to choose meaningful participants.

### Prism integration

Default flow:

1. **Search/select instruments before spawning subagents.**
   - If the user named instruments, use those first.
   - Otherwise, use the `search` workflow to find appropriate instruments
     for the target, mode, and each participant role. Search by target
     domain, artifact type, risk type, and intended output.
   - Prefer 1-3 instruments per participant. Avoid giving every
     participant the same generic instrument unless the target genuinely
     needs a shared frame.
2. **Fetch concrete paths and summaries.**
   - Use `/prism fetch` semantics to resolve selected instruments to
     absolute paths and concise summaries.
   - If a path cannot be resolved, replace that instrument before
     spawning the subagent.
3. **Insert instrument read directives into every subagent prompt.**
   - Each subagent prompt must include a `## Prism Instruments - Subagent
     Directive` block before the target.
   - The block must list instrument name, class, path, and why it was
     assigned to that participant.
   - The block must instruct the subagent to read the files first and use
     their procedures, checklists, discriminating questions, or stance as
     the analysis frame.
4. **Validate before spawn.**
   - In instrumented mode, do not spawn any subagent whose prompt lacks
     both a Prism instrument path and an explicit read/apply instruction.

Persona-only mode skips steps 1-4 only when explicitly requested with
`--persona-only` or equivalent wording. In that mode, mark the final
report as `Instrumentation: persona-only`.

---

## Execution flow

### STEP 0 — Session initialization

The orchestrator (main session) performs:

1. Prepare the target as a `[TARGET]` block (document, problem statement, etc.)
2. Determine mode (apply rules above)
3. Determine instrumentation mode (default `instrumented`; explicit
   `--persona-only` opt-out)
4. Select participants:
   - If the user named personas/agents, keep them and assign instruments
     suited to each role.
   - If the user did not name personas/agents, infer 3-5 complementary
     instrument-grounded participants from the target and selected
     instruments.
5. In instrumented mode, search/select/fetch instruments and build a
   `PRISM_INSTRUMENT_DIRECTIVE` for each participant.
6. Validate every participant prompt before spawn:
   - instrumented mode: requires at least one resolved Prism path and a
     read/apply instruction
   - persona-only mode: requires an explicit `Instrumentation:
     persona-only` note
7. Set configuration:
   - `MAX_ROUNDS`: default 4 (user-configurable)
   - `CONSENSUS_THRESHOLD`: default 0.75 (used in review/solve modes)
8. Initialize state: `round = 1`, `issues = []`, `solution_pool = []`

---

### STEP 1 — Round execution (iterative)

Each round: **spawn all participating agents in parallel via the Agent tool.**
Use mode-specific prompt templates.

#### Common prompt header

```
You are [AGENT_NAME].
Role description: [AGENT_DESCRIPTION]
[PRISM_INSTRUMENT_DIRECTIVE — required unless `--persona-only`]

## Target
[TARGET]

## Current round
Round [N] / [MAX_ROUNDS]

## Previous round summary (omit for Round 1)
[PREVIOUS_ROUND_SUMMARY]
```

#### Required instrument directive format

Use this block in every instrumented subagent prompt:

```markdown
## Prism Instruments - Subagent Directive

Instrumentation: instrumented

Before analysis, read and apply these Prism instruments:

| Instrument | Class | Path | Why assigned |
|---|---|---|---|
| [instrument-name] | [lens/frame/model/stance/heuristic] | [absolute path] | [fit to this participant and target] |

Use the instruments as active procedures, not citations. Follow their
analytical steps, discriminating questions, failure modes, and output
expectations where relevant. If instruments conflict, name the conflict
and resolve it explicitly in your JSON response.
```

Use this note only in explicit persona-only mode:

```markdown
Instrumentation: persona-only (`--persona-only` requested). No Prism
instrument files are attached.
```

#### Mode-specific tasks and output formats

---

### MODE: review

**Task block:**
```
## Your task
1. Analyze the target from your persona's perspective.
2. If previous rounds exist, review other agents' arguments and state agreement/disagreement explicitly.
3. Follow the JSON output format below exactly. No text output outside JSON.
```

**Output JSON:**
```json
{
  "agent": "[AGENT_NAME]",
  "round": "[N]",
  "analysis": {
    "key_findings": ["Key finding (one sentence each)"],
    "concerns": ["Concern or issue"],
    "strengths": ["Strength or positive aspect"]
  },
  "stance_on_pending_issues": [
    {
      "issue": "Pending issue text",
      "position": "agree | disagree | neutral",
      "rationale": "Rationale for position (2-3 sentences)"
    }
  ],
  "new_issues": [
    {
      "issue": "Newly raised issue",
      "severity": "critical | major | minor",
      "rationale": "Why this matters"
    }
  ],
  "overall_recommendation": "approve | approve_with_conditions | reject",
  "recommendation_rationale": "Rationale for final recommendation (3-5 sentences)"
}
```

---

### MODE: ideate

**Task block:**
```
## Your task
1. Analyze the target from your persona's perspective and propose as many diverse ideas as possible.
2. Draw inspiration from other agents' ideas to extend, remix, or combine. Prioritize expansion over criticism.
3. Seek angles that don't overlap with existing ideas.
4. Follow the JSON output format below exactly.
```

**Output JSON:**
```json
{
  "agent": "[AGENT_NAME]",
  "round": "[N]",
  "perspective": "This agent's unique lens on the target (1-2 sentences)",
  "ideas": [
    {
      "title": "Idea title",
      "description": "Detailed description (2-3 sentences)",
      "novelty": "high | medium | low",
      "inspired_by": "Other agent's idea that inspired this (null if original)",
      "tags": ["classification tags"]
    }
  ],
  "combinations": [
    {
      "source_ideas": ["Titles of ideas being combined"],
      "combined_idea": "New idea born from combination",
      "synergy": "Why this combination creates value"
    }
  ],
  "unexplored_angles": ["Suggested directions not yet explored"]
}
```

---

### MODE: solve

**Task block (Round 1):**
```
## Your task
1. Analyze the problem from your persona's perspective and propose a solution.
2. Follow the JSON output format below exactly.
```

**Task block (Round 2+):**
```
## Your task
1. Review other agents' solutions.
2. Specify which elements you accept, which need improvement, and which are unacceptable.
3. Present a new or improved version that integrates prior proposals.
4. Explicitly note any withdrawals or revisions to your previous proposal.
```

**Output JSON:**
```json
{
  "agent": "[AGENT_NAME]",
  "round": "[N]",
  "problem_framing": "Core perspective on the problem (1-2 sentences, Round 1 only)",
  "proposed_solution": {
    "title": "Solution title",
    "description": "Detailed description (3-5 sentences)",
    "key_steps": ["Execution step"],
    "feasibility": "high | medium | low",
    "feasibility_rationale": "Feasibility assessment rationale"
  },
  "review_of_others": [
    {
      "agent": "Agent under review",
      "elements_accepted": ["Acceptable elements"],
      "elements_rejected": [
        { "element": "Unacceptable element", "reason": "Rejection reason" }
      ],
      "suggested_improvement": "Improvement suggestion (null if none)"
    }
  ],
  "tradeoffs": [
    {
      "tradeoff": "Tradeoff description",
      "severity": "critical | major | minor",
      "mitigation": "Mitigation approach (null if none)"
    }
  ],
  "convergence_signal": {
    "willing_to_adopt": ["Elements willing to integrate"],
    "dealbreakers": ["Absolutely unacceptable elements"]
  },
  "revised_from_previous": "Changes from previous round (null for Round 1)"
}
```

---

### STEP 2 — Judgment (orchestrator)

After each round, the orchestrator analyzes collected JSON results.
**Judgment logic varies by mode.**

#### review mode — consensus judgment

**1. Recommendation agreement rate (quantitative)**

| overall_recommendation distribution | Judgment |
|---|---|
| Same value >= 75% | Direction consensus |
| Same value 50–74% | Partial consensus (conditional proceed) |
| Same value < 50% | No consensus |

**2. Issue resolution rate (quantitative)**

```
resolution_rate = (pending_issues where all agents agree) / (total pending_issues)
```
- >= 0.8 → sufficient
- < 0.8 → next round needed

**3. Critical issue presence (takes priority)**
- Any unresolved `severity: critical` `new_issues` → no consensus (blocking condition)

**Exit condition (AND):** agreement >= 75% + resolution >= 80% + no critical issues remaining

#### ideate mode — no judgment

- No convergence/consensus judgment is performed
- Instead, track the count of unique new ideas per round
- Include "cumulative idea pool status" in round summaries
- On MAX_ROUNDS exhaustion, compile the full idea pool into a report

#### solve mode — convergence judgment

**1. Solution convergence rate (quantitative)** — core approach similarity

| Agreement rate | Judgment |
|---|---|
| >= 75% | Direction convergence |
| 50–74% | Partial convergence |
| < 50% | No convergence |

**2. Dealbreaker presence (takes priority)**
- Any remaining `dealbreakers` → no convergence (blocking condition)

**3. Critical tradeoff mitigation rate (quantitative)**
```
mitigation_rate = (critical tradeoffs with mitigation) / (total critical tradeoffs)
```
- >= 0.8 → sufficient
- < 0.8 → next round needed

**Exit condition (AND):** no dealbreakers + convergence >= 75% + mitigation >= 80%

---

### STEP 3 — Round summary (orchestrator)

When exit conditions are not met, the orchestrator generates a summary
for the next round.

#### review mode summary
```
PREVIOUS_ROUND_SUMMARY:
  Agreed items: [items where all agents agree]
  Pending issues: [items with disagree/neutral + new critical/major issues]
  Agent stances:
    [AGENT]: recommendation + rationale summary (1-2 sentences)
```

#### ideate mode summary
```
PREVIOUS_ROUND_SUMMARY:
  Idea pool (cumulative): [all unique ideas — title + proposer]
  New this round: [ideas first appearing this round]
  Combined ideas: [ideas from combinations]
  Unexplored directions: [aggregated unexplored_angles]
```

#### solve mode summary
```
PREVIOUS_ROUND_SUMMARY:
  Solution pool:
    [Agent A]: [solution.title] — [description summary, 1 sentence]
    [Agent B]: ...
  Agreed elements: [intersection of all willing_to_adopt]
  Unresolved tradeoffs: [critical items with null mitigation]
  Dealbreakers: [remaining dealbreaker list]
```

---

### STEP 4 — Final report

Generated when exit conditions are met or MAX_ROUNDS is exhausted.

#### review mode report

```markdown
# Debate Final Report — Review

**Target:** [target summary]
**Participants:** [agent list]
**Rounds completed:** [N] / [MAX_ROUNDS]
**Consensus status:** Consensus reached | Partial consensus | No consensus

---

## 1. Final recommendation
**Agreed recommendation:** [approve | approve_with_conditions | reject | split]
[Core rationale summary, 2-4 sentences]

## 2. Agreed items
- [Item 1]
- [Item 2]

## 3. Remaining disagreements
| Issue | Severity | Agent positions |
|---|---|---|
| [content] | critical/major/minor | [A: agree, B: disagree, ...] |

## 4. Per-agent final positions
### [Agent A]
- **Recommendation:** approve/reject/...
- **Key findings:** ...
- **Main concerns:** ...

## 5. Conditional approval actions (if applicable)
1. [Required action]

---
*Generated: [timestamp] | Skill: debate (review)*
```

#### ideate mode report

```markdown
# Debate Final Report — Ideate

**Topic:** [target summary]
**Participants:** [agent list]
**Rounds completed:** [N] / [MAX_ROUNDS]
**Unique ideas generated:** [N]

---

## 1. Idea map

### By category
#### [Category/tag A]
- **[Idea title]** (by [Agent]) — [1-sentence description] | novelty: high/medium/low
- ...

#### [Category/tag B]
- ...

## 2. Notable combinations
| Source ideas | Combined result | Synergy |
|---|---|---|
| [A's X + B's Y] | [Combined idea] | [Synergy description] |

## 3. Unexplored directions
> Angles suggested by agents but not yet deeply explored
- [Direction 1]
- [Direction 2]

## 4. Per-agent perspective summary
### [Agent A]
- **Unique perspective:** ...
- **Ideas proposed:** N
- **Highest novelty idea:** ...

---
*Generated: [timestamp] | Skill: debate (ideate)*
```

#### solve mode report

```markdown
# Debate Final Report — Solve

**Problem:** [problem summary]
**Participants:** [agent list]
**Rounds completed:** [N] / [MAX_ROUNDS]
**Convergence status:** Converged | Partial convergence | No convergence

---

## 1. Agreed solution
**Title:** [integrated solution title]
[Core approach, 3-5 sentences]

### Execution steps
1. [Step 1]
2. [Step 2]

### Feasibility
**Overall assessment:** high | medium | low
[Rationale, 2-3 sentences]

## 2. Agreed core elements
- [Element 1]
- [Element 2]

## 3. Tradeoffs and mitigations
| Tradeoff | Severity | Mitigation |
|---|---|---|
| [content] | critical/major/minor | [approach or "unresolved"] |

## 4. Unresolved divergences (if applicable)
| Issue | Agent positions | Orchestrator judgment |
|---|---|---|
| [divergence] | [A: option X, B: option Y] | [judgment] |

## 5. Per-agent final proposals
### [Agent A]
- **Proposal:** [title]
- **Core approach:** ...
- **Feasibility:** high/medium/low

## 6. Recommended next steps
1. [Immediate action 1]
2. [Immediate action 2]

---
*Generated: [timestamp] | Skill: debate (solve)*
```

---

## Orchestrator checklist

### Before each round
- [ ] Target is fully included in subagent prompts
- [ ] Previous round summary is accurately composed
- [ ] Each subagent is **independently** spawned (no shared context)
- [ ] Instrumentation mode is recorded (`instrumented` by default, or explicit `persona-only`)
- [ ] In instrumented mode, each subagent prompt includes a resolved Prism instrument path
- [ ] In instrumented mode, each subagent prompt includes an explicit read/apply instruction
- [ ] In persona-only mode, the user's opt-out is explicit in the prompt or request

### After each round
- [ ] JSON parse failures: exclude affected agent from round results, notify user
- [ ] Mode-specific judgment logic correctly applied (ideate has none)
- [ ] review/solve: check blocking conditions (critical issues / dealbreakers) first
- [ ] review/solve: compute quantitative metrics, evaluate exit conditions

### When writing final report
- [ ] Use the correct report format for the active mode
- [ ] If terminated by MAX_ROUNDS exhaustion, explicitly list unresolved items
- [ ] If mode transition is natural, suggest next step to user (never force)

---

## NOT this skill

- **Catalog browsing** — route to `/prism search`
- **Instrument creation** — route to `/prism`
- **Standalone instrument loading** — route to `/prism fetch`. Debate uses search/fetch internally when preparing instrumented participants
- **Single-analyst sequential multi-tool analysis** — use Prism's standard 7-step workflow directly. Debate is for **multi-perspective parallel analysis + consensus/divergence** only

---

## Operational rules

- Subagents must be spawned **in parallel** via the Agent tool — no sequential execution
- Each subagent has independent context — no real-time sharing of other subagents' current-round responses
- Inter-round information transfer happens only through orchestrator-generated summaries
- MAX_ROUNDS default is 4 — most debates converge in 2-3 rounds; 4 is the safety ceiling
- On JSON parse failure, exclude that agent from the round and notify the user in one line
- Instrumented mode is the default. Do not silently downgrade to persona-only.
- Use persona-only mode only for an explicit `--persona-only` opt-out.
- Final reports must include `Instrumentation: instrumented` with the
  participant→instrument mapping, or `Instrumentation: persona-only` with
  the explicit opt-out reason.
