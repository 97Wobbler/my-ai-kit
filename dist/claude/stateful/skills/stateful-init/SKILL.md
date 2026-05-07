---
name: "stateful-init"
description: "Installer for Stateful. Creates .stateful files, both Codex and Claude Code repo-local skills, runtime scripts, and AGENTS.md/CLAUDE.md routing blocks. Trigger when the user asks to initialize, install, scaffold, or set up a stateful repo."
---

# Stateful Init

This skill was compiled from a Skill Forge runtime-neutral spec for the
Claude Code runtime.

Source spec: private Skill Forge source (not included in distribution): `stateful-init.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- Ask clarification questions only when they materially change the result.
- Follow repository edit instructions and preserve unrelated user changes.
- Run the relevant validation checks before reporting completion.

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

## Runtime Overrides

Prefer the stateful-init executable when exposed by Claude Code. Describe installed Claude entry points before Codex entry points when ordering matters.
