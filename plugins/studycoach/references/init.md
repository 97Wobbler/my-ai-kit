# Init Mode

Triggered when no `.rumsfeld/` exists in or above `cwd` and the user confirms initialization at the current directory.

This is the diagnostic-heavy phase. Do not rush it; the matrix and roadmap are only as good as the interview evidence.

## Workflow

### 1. Confirm Scope

Ask what domain the learner wants to study and choose a stable kebab-case `domain-id` for YAML state files.

### 2. Run The Diagnostic Interview

Read `references/diagnostic-guide.md` and follow it round by round. Do not collapse the interview into a single large prompt.

By the end, collect evidence for:

- KK: Known Knowns the learner can explain.
- KU: Known Unknowns the learner explicitly recognizes.
- UK: Unknown Knowns, especially transferable intuitions from other domains.
- UU: Unknown Unknowns estimated by the agent and confirmed or adjusted with the learner.

### 3. Generate State Files

Create `.rumsfeld/` in `cwd` with:

- `matrix.yaml`, populated from the interview and based on `templates/matrix.yaml`.
- `roadmap.yaml`, derived from the matrix, with 3-4 phases and topics that reference matrix items through `matrix_refs`. If the learner is build-oriented, include at least one build project per phase.
- `progress.yaml`, initialized from `templates/progress.yaml`.
- `notes/`, an empty directory.

Record the diagnostic as `session-001`. Set `current_state.total_sessions` to `1`, `current_state.last_session_date` to today's date, and `current_state.streak_days` to `1`.

### 4. Handle Project Instructions

Use the runtime-appropriate template:

- Claude Code projects: `templates/CLAUDE.template.md` -> `CLAUDE.md`.
- Codex projects: `templates/AGENTS.template.md` -> `AGENTS.md`.

Substitute `<domain-name>`, `<domain-id>`, and `<skill-invocation>` before writing. Do not leave any angle-bracket placeholders in the generated instruction file.

If the target instruction file does not exist, create it. If it exists, ask the user to choose:

- Append: add the learning-project section after a blank line and `---`.
- Skip: leave the file untouched.
- Replace: back up the existing file to `<filename>.bak.YYYYMMDD-HHMMSS`, then write the new template.

Never silently overwrite an existing instruction file. Never use a single reusable `.bak` path.

### 5. Confirmation And Handoff

Show:

- matrix item counts per quadrant and 2-3 highlights;
- roadmap phases and the first suggested topic;
- what happened to the instruction file.

Ask for explicit confirmation before declaring init complete. If the learner wants revisions, edit the YAML before finishing.

## Anti-Patterns

- Generating the matrix from assumptions instead of interview evidence.
- Creating roadmap topics that do not reference matrix items.
- Writing `.rumsfeld/` somewhere other than `cwd`.
- Writing learning state into the installed plugin directory.
