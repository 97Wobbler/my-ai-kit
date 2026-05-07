---
name: "stateful"
description: "Router for the Stateful plugin. Use when the user asks what Stateful is, how to install repository-local state, how to resume a stateful repo, or how to run status/doctor/close, roadmap planning, or archive workflows. Routes to stateful-init, stateful-doctor, stateful-close, stateful-plan, and stateful-archive when the request is specific. Triggers on \"$stateful\", \"stateful\", \"repo state\", \"repo stateful\", \"상태 하네스\", \"레포 하네스\"."
---

# Stateful

This skill was compiled from a Skill Forge runtime-neutral spec for the
Codex CLI runtime.

Source spec: `plugins/stateful/specs/stateful.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- Ask clarification questions sparingly; `request_user_input` is Plan Mode only.

# stateful

Stateful installs a repository-local operating layer for long-running agent
work. It creates:

- `.stateful/workplan.yaml` — machine-readable task DAG
- `.stateful/docs/` — status, decisions, risks, roadmap, and todo narrative state
- `.stateful/session/handoff.md` — next-session recovery note
- `.stateful/protocols/` — autorun, gates, and recovery rules
- `.agents/skills/<repo-skill>/SKILL.md` — Codex repo skill
- `.claude/skills/<repo-skill>/SKILL.md` — Claude Code slash entry point
- `scripts/stateful/` — validate, sync, status, and close-session scripts
- Codex routing block in `AGENTS.md`
- Claude routing block in `CLAUDE.md`

## Routing

Classify the user's request into one of these intents:

1. **Install / initialize**
   - Signals: "install Stateful", "init stateful", "이 레포에 하네스 설치",
     "상태 하네스 만들어", "set up repo state".
   - Route to `stateful-init`.

2. **Doctor / validate / status**
   - Signals: "doctor", "validate stateful", "status", "check the
     workplan", "하네스 검사".
   - Route to `stateful-doctor`.

3. **Close / handoff**
   - Signals: "close session", "handoff", "세션 종료", "인계 문서".
   - Route to `stateful-close`.

4. **Roadmap to workplan**
   - Signals: "roadmap을 일감으로", "plan from roadmap", "promote roadmap",
     "next tasks from roadmap", "로드맵 실행 계획".
   - Route to `stateful-plan`.

5. **Archive / compact completed work**
   - Signals: "archive completed tasks", "compact workplan", "완료 일감 정리",
     "문서 정리 dry-run", "summarize completed work".
   - Route to `stateful-archive`.

6. **Explain**
   - If the user asks what Stateful is or invokes `$stateful` without a
     concrete action, explain the concept briefly and show the common
     workflows below.

## Common Workflows

Install into the current repository:

```bash
python3 <codex-skills-root>/stateful-init/scripts/stateful_init.py --root . --skill repo
```

When this skill is loaded, the runtime has the file path for this `SKILL.md`; resolve
`<codex-skills-root>` as the parent directory that contains `stateful/` and
`stateful-init/`.

Check an installed stateful:

```bash
python3 scripts/stateful/validate-workplan.py
python3 scripts/stateful/sync-state.py
python3 scripts/stateful/status.py --tool <runtime>
```

Close a session:

```bash
python3 scripts/stateful/close-session.py --summary "What changed this session"
```

Propose workplan tasks from roadmap:

```bash
python3 scripts/stateful/plan.py --dry-run
```

Review completed tasks for archival summary:

```bash
python3 scripts/stateful/archive.py --dry-run
```

Before starting a task, claim it so the next agent can recover unfinished work
later:

```bash
python3 scripts/stateful/task.py claim R001 --tool <runtime> --summary "What is being attempted"
```

## Operating Principle

Stateful is not a project manager. It is a state contract for agents:
future sessions recover from repository files and git history, not from
chat memory.

## Runtime Overrides

Use Codex invocation examples and AGENTS.md naming when explaining installed repo-local state. For status examples, prefer --tool codex.
