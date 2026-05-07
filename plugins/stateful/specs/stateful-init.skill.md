---
name: "stateful-init"
description: "Installer for Stateful. Creates .stateful files, both Codex and Claude Code repo-local skills, runtime scripts, and AGENTS.md/CLAUDE.md routing blocks. Trigger when the user asks to initialize, install, scaffold, or set up a stateful repo."
targets:
  - claude
  - codex
capabilities:
  user_questions: optional
  file_edits: true
  subagents: none
  plan_mode: none
  network: false
  validation: required
runtime_overrides:
  claude: |
    Prefer the stateful-init executable when exposed by Claude Code. Describe installed Claude entry points before Codex entry points when ordering matters.
  codex: |
    Use local shell commands for installer execution. Describe installed Codex entry points before Claude entry points when ordering matters.
outputs:
  claude: plugins/stateful/skills/claude/stateful-init/SKILL.md
  codex: plugins/stateful/skills/codex/stateful-init/SKILL.md
---

# stateful-init

Install Stateful into the current repository unless the user gives a different
path.

## Procedure

1. Locate this skill directory from the loaded `SKILL.md` path.
2. Run the installer wrapper bundled with this skill:

```bash
python3 <this-skill-directory>/scripts/stateful_init.py --root <target-repo> --skill repo
```

Use a different `--skill` value only if the user asks for a specific repo
skill name.

3. Run the generated checks in the target repo:

```bash
python3 scripts/stateful/validate-workplan.py
python3 scripts/stateful/sync-state.py
python3 scripts/stateful/status.py
```

4. Report the files created and any warnings.

## Rules

- Do not overwrite unrelated project content.
- The installer uses marker blocks when patching `AGENTS.md` and `CLAUDE.md`.
- If the target repo already has `.stateful/config.yaml`, do not force
  reinstall unless the user explicitly asks.
- Keep the initial workplan small. The installed scaffold is a starter
  contract; project-specific task decomposition can happen afterward.
