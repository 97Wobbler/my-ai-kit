# Phase 2 Seed Prompt — Prism v0.2.0

> Paste the entire **"PROMPT STARTS HERE"** block below into a fresh Claude Code
> session. Everything above it is just user-facing commentary for you to read
> before starting.

---

## Before you paste the prompt

### What to do first (manual steps)

1. **Rename the local project directory** if you haven't already:

   ```bash
   # Close any Claude Code session pointing at this directory first
   cd /path/to/workspace
   mv lenslab prism
   ```

2. **Start a new Claude Code session** in the renamed directory:

   ```bash
   cd /path/to/workspace/prism
   claude
   ```

3. **Paste the prompt block** (everything between the two `===` rulers below)
   into the new session as your first message.

### Why this seed prompt exists

The planning for Phase 2 was done in a long session during Phase 1. To avoid
starting Phase 2 with a cold context, this document carries forward every
decision, every rationale, the workflow pattern that was used in Phase 1, and
pointers to the files you should read. Paste it, and the new session will know
enough to start executing immediately.

---

## Prompt starts here

===

We're starting **Phase 2 of the Prism plugin project**. Phase 1 (rename
lenslab → Prism) shipped as v0.1.0. The local directory was just renamed from
`lenslab/` to `prism/`, so your working directory is
`/path/to/workspace/prism`. The git remote is
`https://github.com/97Wobbler/prism.git`.

**Your first action**: read the three files listed below in order. Do not
start any task until you have read all three. They are your complete brief.

1. `docs/phase2-plan.yml` — the authoritative task list and dependency graph
2. `docs/ROADMAP.md` — the version-level direction (v0.1 / v0.2 / v0.3 / out of scope)
3. `CLASSES.md` — the 5-class taxonomy and file format templates

After reading those three, read these for context as needed:

4. `README.md` — current user-facing documentation (reflects v0.1.0 state)
5. `docs/phase1-plan.yml` and `docs/phase1-substitution-map.md` — how Phase 1
   was executed, useful as precedent for Phase 2 task breakdown style
6. `skills/agent-creator/SKILL.md` — the skill you will be removing; read it so
   you understand what the replacement skills need to cover
7. `agents/examples/*.yml` — the 4 example agents being converted to cookbook
   recipes in T4

## The one-sentence goal

Prism v0.2.0 is a **pure catalog reference plugin**. Remove `agent-creator` and
`create-agent`. Add `search` (read-only catalog exploration) and
`make-instrument` (interview-style instrument creation). Introduce 3-layer
custom instrument storage (bundle / global / project). Convert
`agents/examples/` into `docs/cookbook/` composition recipes. Ship as v0.2.0.

## Decisions already locked in (do not re-litigate these)

These were debated at length in the Phase 1 session. You are allowed to push
back if you discover a real problem, but do not revisit them for stylistic
reasons.

1. **Project name is Prism.** Repo at github.com/97Wobbler/prism. `lenslab` is
   the archived predecessor at github.com/97Wobbler/lenslab (read-only, banner
   added).

2. **The umbrella term for the 5 classes is `instrument`.** Not 'framework',
   not 'tool'. Use 'instrument' everywhere. Individual class names (lens,
   frame, model, stance, heuristic) are unchanged.

3. **Prism does NOT generate agents or skills.** Agent creation belongs to
   Claude Code's native mechanisms; skill creation belongs to the official
   `skill-creator` skill. Prism's only job is to provide a catalog of
   instruments that those native mechanisms can reference.

4. **Two and only two skills in v0.2.0**:
   - `search` — read-only. Answers "what instruments exist for X?"
   - `make-instrument` — interactive. Creates a single new instrument file via
     a short interview followed by LLM-driven body generation.

   There is NO `create-agent`, `create-skill`, or `contribute-instrument` in
   v0.2.0. The contribution-upload skill is planned for v0.3.0.

5. **3-layer custom instrument storage**:
   - **Bundle** (`library/` inside the plugin): read-only, the 657 builtin
     instruments. Shipped with Prism.
   - **Global** (`~/.claude/prism/library/`): user's personal instruments,
     available in every project.
   - **Project** (`./.claude/prism/library/`): instruments scoped to the
     current repo.

   **Lookup precedence: project > global > bundle.** Closer context overrides
   broader. On a name collision, warn to stderr and use the closer layer.

6. **The composite catalog view is computed at runtime, not persisted.** Each
   layer has its own `catalog.yml` (bundle's is the one shipped with the
   plugin; global and project catalogs are optional). `sync_catalog.py
   --source {bundle|global|project}` rewrites one layer's catalog in place.
   A new default mode `--source all` prints a merged preview to stdout.

7. **make-instrument uses interview-style input then auto-generates via LLM.**
   There is no `--blank` mode. The user provides a framework name and domain;
   the skill asks up to 3 clarifying questions if genuinely ambiguous (class
   undetermined, source unknown, output format unclear); then an LLM writes
   the body.

8. **agents/examples/*.yml → docs/cookbook/*.md conversion.** These files
   become narrative markdown "composition recipes" explaining WHY a given set
   of instruments is used together for a given domain. Each file must start
   with a disclaimer that it is NOT an executable agent config.

## Workflow you MUST follow (the subagent-delegation pattern)

This pattern was used successfully in Phase 1. Follow it exactly.

**Main session = orchestration, never execution.** Do not edit files or run
long commands yourself. Your job is:

1. Read `docs/phase2-plan.yml`. Understand the task list (T1-T8) and the
   dependency graph.
2. Create tasks in TaskCreate for each of T1-T8 and wire up the dependencies
   (`addBlockedBy`). Set the `owner` field when you assign a task to a
   subagent.
3. Find the current blocker-free tasks.
4. For each blocker-free task, spawn a subagent via the `Agent` tool. The
   subagent prompt must be self-contained: tell it to read
   `docs/phase2-plan.yml` first, then reference the specific task ID (e.g.,
   "Execute T1 from docs/phase2-plan.yml"), then give it the concrete
   deliverables and commit instructions.
   - **Parallel-safe tasks** (no dependencies between each other): launch as
     background via `run_in_background: true`. The plan marks these as
     `parallelizable: true`.
   - **Dependent tasks**: launch sequentially (foreground) so the main session
     can collect output and feed it into the next task.
5. When a subagent reports completion, **spawn an independent review
   subagent** (use the `Explore` subagent type — it's read-only). The reviewer
   reads the just-completed work and verifies it matches the task's success
   criteria. Reviewer outputs PASS / CONDITIONAL PASS / FAIL.
6. Only on PASS (or CONDITIONAL PASS with minor issues) mark the task
   completed in TaskUpdate and proceed to the next blocker-free task.
7. On FAIL, spawn a remediation subagent or fix in the main session.
8. Update `docs/phase2-plan.yml`'s `task_states` section each time a task
   completes, so the plan doubles as a progress ledger.
9. At the end, follow T7 and T8 for manifest bump, tag, and push.

## Parallelism plan from phase2-plan.yml

| Round | Tasks | Execution mode |
|---|---|---|
| 1 | T1 (search), T2 (make-instrument), T4 (cookbook conversion), T5 (sync_catalog --source) | 4 parallel background subagents |
| 2 | T3 (remove agent-creator) | sequential, after T1 and T2 complete |
| 3 | T6 (update README) | sequential, after all content tasks |
| 4 | T7 (bump manifest + sanity check), T8 (push + user install verification) | sequential |

**Round 1 is where most of the work happens.** Four independent subagents can
run concurrently because they touch different files.

## Review subagent protocol

After every execution subagent, run a review subagent with this basic shape:

```
Subagent type: Explore (read-only)

Prompt:
Review <task-id> of Phase 2. Read docs/phase2-plan.yml for the task's
definition and success criteria. Then verify:
1. Deliverables exist
2. No files were touched outside the task's scope
3. Python/JSON/YAML validity where applicable
4. Cross-references are consistent (grep for residual references to removed items)
5. Any task-specific criteria listed in the plan

Report: A / B / C / D / E sections (or your task-specific headings) with
PASS / CONDITIONAL PASS / FAIL for each, then a final verdict.
```

## Known pitfalls from Phase 1 — avoid these

1. **Don't run subagents in parallel when one depends on another's output.**
   Phase 1 had an incident where a README-editing subagent ran in parallel
   with a script-creating subagent, and the README ended up describing
   features that didn't yet exist on disk. Sequential for dependent tasks,
   always.

2. **Don't revert linter edits.** The user may have edited README or other
   files between turns. System reminders will tell you about these changes.
   Respect them; do not overwrite. Integrate them into your next edit.

3. **Plugin cache paths use marketplace/plugin name, not owner/repo.** When
   you need to clean caches for user testing:
   ```bash
   rm -rf ~/.claude/plugins/cache/prism ~/.claude/plugins/cache/temp_local_*
   rm -rf ~/.claude/plugins/marketplaces/prism
   ```
   Do not try `~/.claude/plugins/marketplaces/97Wobbler-prism` — that path
   does not exist.

4. **Don't touch `library/` content.** The 657 instruments are Phase 1's
   frozen library. Phase 2 does not edit them. Only the catalog layer above
   them changes.

5. **Don't touch `docs/archive/`.** Historical documents from v0.2 design.

6. **Don't touch `scripts/prompts/*.txt`.** These are the BATCH generator
   prompts used by `scripts/prism_batch.py` for bulk generation. The
   interactive `make-instrument` skill uses its own per-class templates
   inside SKILL.md — those are separate.

## Verification at the very end

After T8 push, the user will manually verify the plugin:

```
/plugin marketplace remove prism
! rm -rf ~/.claude/plugins/cache/prism ~/.claude/plugins/cache/temp_local_* ~/.claude/plugins/marketplaces/prism
/plugin marketplace add 97Wobbler/prism
/plugin install prism
/reload-plugins
# Check that /prism:search and /prism:make-instrument appear
# Check that /prism:create-agent does NOT appear
```

If installation fails, the most likely causes are (in order of probability):
1. Cache not fully cleaned (retry the rm -rf)
2. marketplace.json or plugin.json schema error (see Phase 1 learnings about
   `source: "./"` vs `"."`, `author` must be an object)
3. Actual plugin.json bug — verify with the raw.githubusercontent.com fetch

## Ready check

Before starting, tell me:
1. Current working directory (should be `/path/to/workspace/prism`)
2. git remote -v (should show origin pointing at github.com/97Wobbler/prism)
3. git log --oneline -5 (should show v0.1.0 tag and T3 rename commit)
4. ls of the repo root

If anything looks wrong, stop and report it. Otherwise, proceed to read the
three required files (`docs/phase2-plan.yml`, `docs/ROADMAP.md`,
`CLASSES.md`), then create the TaskCreate entries for T1-T8 and begin Round 1.

===

## Prompt ends here

---

## Notes for you (the human) before pasting

- The seed prompt above is self-contained; you don't need to explain anything
  additional when starting the new session. Just paste it.
- If you want the new session to run more autonomously, add a line like
  "Auto-proceed through all tasks without confirmation unless a review
  subagent returns FAIL." — but the default behavior is to ask you before
  each risky action.
- Phase 2 is larger than Phase 1 (~2x the tasks). Expect the full run to
  take 30-60 minutes of subagent work plus your installation verification
  at the end.
- If the new session's context fills up mid-run, it can stop after any
  completed task (the plan's `task_states` section is the resume point).
  You can then start yet another session pointing at the same plan.

## Files written for Phase 2

- `docs/phase2-plan.yml` — the authoritative task list
- `docs/PHASE2_SEED_PROMPT.md` — this file
- `docs/ROADMAP.md` — already existed from Phase 1, still accurate

Both `docs/phase2-plan.yml` and `docs/PHASE2_SEED_PROMPT.md` should be
committed to the repo so the next session can find them.
