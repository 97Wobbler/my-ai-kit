---
name: "studycoach"
description: "Project-local self-study coach using the Rumsfeld Known/Unknown matrix. Use when the user explicitly asks to start or resume a self-study project, study a domain, review learning progress, update a learning matrix, or says \"공부하자\", \"자습\", \"학습 시작\", \"다음 뭐 배우지\", \"진행률 확인\", \"매트릭스 업데이트\", \"학습 세션\", \"studycoach 시작\", or \"rumsfeld 시작\"."
targets:
  - claude
  - codex
capabilities:
  user_questions: required
  file_edits: true
  subagents: none
  plan_mode: none
  network: false
  validation: optional
runtime_overrides:
  claude: |
    In Claude Code, plugin skills are invoked with the plugin namespace, for example `/studycoach:studycoach`.
    Use Claude Code's native user-question flow when the user must choose init, skip, append, replace, or a study topic.
  codex: |
    In Codex, plugin skills are invoked through the installed skill name, for example `$studycoach` or "use studycoach".
    Use `request_user_input` only in Plan Mode. In Default mode, ask concise plain-text questions and wait for the answer.
    For manual file edits, prefer `apply_patch`; when generating YAML from templates, preserve unrelated user changes.
outputs:
  claude: plugins/studycoach/skills/claude/studycoach/SKILL.md
  codex: plugins/studycoach/skills/codex/studycoach/SKILL.md
---

## Purpose

Study Coach is a structured self-study system that diagnoses knowledge gaps, builds phased learning roadmaps, runs interactive study sessions, and tracks progress through a Rumsfeld Known/Unknown matrix.

The skill is installed as a plugin, but every learning project's mutable state belongs to the project directory where the learner invokes the skill. Never write learning state into the installed plugin directory.

## Project State

Each learning project stores state under:

```text
<learning-project-root>/
├── CLAUDE.md or AGENTS.md
└── .rumsfeld/
    ├── matrix.yaml
    ├── roadmap.yaml
    ├── progress.yaml
    └── notes/
        ├── YYYY-MM-DD-<topic>.md
        └── concept-<slug>.md
```

Resolve the learning project root by walking up from `cwd` until a `.rumsfeld/` directory is found. If none is found, offer to initialize a new learning project at `cwd`; do not create state silently.

Support references and templates live in the installed plugin root:

```text
references/
├── diagnostic-guide.md
├── init.md
├── resume.md
└── session.md
templates/
├── CLAUDE.template.md
├── AGENTS.template.md
├── matrix.yaml
├── progress.yaml
└── roadmap.yaml
```

When loading support files, resolve the plugin root by walking up from this `SKILL.md` until you find `.claude-plugin/`, `.codex-plugin/`, `references/`, or `templates/`.

## Modes

Always route to exactly one mode before acting.

| Mode | When | Support file |
|---|---|---|
| `init` | No `.rumsfeld/` exists and the user explicitly confirms initializing at `cwd` | `references/init.md` |
| `resume` | `.rumsfeld/` exists and the user needs orientation, status, roadmap review, matrix review, or a study-topic choice | `references/resume.md` |
| `session` | Resume mode has briefed the learner and the learner explicitly confirms a study topic now | `references/session.md` |

## Routing

1. Search upward from `cwd` for `.rumsfeld/`.
2. If not found, ask: `이 디렉토리(<cwd>)에 새 학습 프로젝트를 초기화할까요? 아니면 기존 학습 프로젝트가 있는 다른 경로에서 호출하시겠어요?`
3. If the user confirms initialization, read `references/init.md` and follow it.
4. If the user declines initialization, stop and tell them to re-invoke from the correct project directory.
5. If `.rumsfeld/` is found, read `references/resume.md`, brief the learner, and offer choices.
6. Start `session` mode only after the learner explicitly chooses to study a topic now.

Do not auto-start teaching just because the user says "공부하자"; resume mode still briefs them first.

## Cross-Mode Invariants

- Store mutable state only under the resolved project root's `.rumsfeld/`.
- Preserve matrix history. Do not delete matrix items; transition them with evidence.
- Keep one `.rumsfeld/` per directory tree. A new domain belongs in a new directory.
- Treat the roadmap as a plan, not a prison. Deviations are allowed but must be logged in `progress.yaml`.
- Use evidence from the learner before classifying matrix items.
- Keep trigger scope narrow: do not activate for generic mentions of learning unless the user is clearly asking to manage or run a Rumsfeld learning project.

## Required Fixes From The Original Standalone Skill

The plugin version intentionally corrects these issues:

1. Existing projects enter `resume` mode first, not `session` mode.
2. Trigger language is explicit and narrower; "resume" is not described as "session".
3. The diagnostic interview is recorded as `session-001`; therefore initialized `progress.yaml` must set `total_sessions: 1` and `last_session_date` to the init date.
4. Study sessions always write a session note; status-only resume actions do not.
5. Replacing an existing project instruction file must create a timestamped backup such as `CLAUDE.md.bak.YYYYMMDD-HHMMSS` or `AGENTS.md.bak.YYYYMMDD-HHMMSS`, never a single reusable `.bak`.

## Init Summary

Init mode runs a five-round diagnostic interview, creates `.rumsfeld/` state files from templates, and writes or updates the runtime's project instruction file. Existing instruction files require an explicit user choice: append, skip, or replace with timestamped backup.

## Resume Summary

Resume mode reads `progress.yaml`, `roadmap.yaml`, and `matrix.yaml`, then briefs the learner in about 6-10 lines: domain, current phase, completed sessions, last covered topic, suggested next topic, open questions, and recent transitions. It then asks whether to study, choose another topic, review state, or manually update the matrix.

## Session Summary

Session mode teaches through dialogue, not lecture. Start with why the concept exists, connect to the learner's Known Knowns and Unknown Knowns, verify understanding through graduated basic/applied/advanced problems, then wrap up by sweeping all four quadrants for confirmed transitions. Write notes and update YAML only after the learner confirms the proposed changes.
