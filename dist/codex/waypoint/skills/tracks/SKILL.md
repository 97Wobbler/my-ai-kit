---
name: "tracks"
description: "Enable or maintain Waypoint's optional docs/tracks.md work-track layer. Use when the user asks for Waypoint tracks, work items, active work tracks, epic/story alternatives, or a larger-than-todo planning layer."
---

# Tracks

This skill was compiled from a Skill Forge runtime-neutral spec for the
Codex CLI runtime.

Source spec: private Skill Forge source (not included in distribution): `tracks.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- Ask clarification questions sparingly; `request_user_input` is Plan Mode only.
- For manual file edits, use `apply_patch` and preserve unrelated user changes.
- Run the relevant validation checks before reporting completion.

## Purpose

Use this skill to enable or maintain Waypoint's optional active-work track
layer. Tracks are for work that is larger than a short todo but still
operational enough that it should not become only a high-level roadmap entry.

Waypoint tracks use this vocabulary:

- `Track`: a coherent line of work that may span multiple sessions or agent
  runs.
- `Work item`: a substantial executable unit inside a track.
- `Todo`: a short-lived checklist item that can continue to live in
  `docs/todo.md` or inline under a work item when useful.

Tracks must remain visible documentation. Do not create hidden primary state,
generated task graphs, mandatory lifecycle machinery, or a replacement for the
runtime's native todo tools.

## Modes

Classify the user's request:

| Request | Mode | Writes |
|---|---|---|
| "What are Waypoint tracks?", "should I use tracks?" | `explain` | No |
| "enable tracks", "create docs/tracks.md", "add track layer" | `enable` | Yes, if safe |
| "add/update this track", "mark this work item done" | `maintain` | Yes, in routed docs |
| "audit tracks", "are these tracks stale?" | `review` | No by default |

If the user only needs a short checklist, keep using `docs/todo.md`. If the
user is setting durable roadmap direction, keep that in `docs/plan.md`. Use
`docs/tracks.md` only for the optional middle layer.

## Enable Workflow

1. Resolve the target repository. Use the current working directory unless the
   user provides a path.
2. Read `AGENTS.md` when present, then inspect `.waypoint/config.yaml`,
   `docs/plan.md`, and `docs/todo.md` when they exist.
3. Do not overwrite an existing `docs/tracks.md`. If it exists, switch to
   `maintain` mode.
4. Resolve the installed Waypoint plugin root by walking up from this skill
   until you find `templates/`, `scripts/`, and `mcp/`.
5. Create `docs/tracks.md` from `templates/docs/tracks.md`.
6. Update `AGENTS.md` only as needed:
   - add `docs/tracks.md` to the Document Map;
   - route larger active work, tracks, and work items to `docs/tracks.md`;
   - keep `docs/plan.md` and `docs/todo.md` routes intact.
7. Update `.waypoint/config.yaml` only as a locator by adding:

```yaml
documents:
  tracks: docs/tracks.md
```

8. Do not add `docs/tracks.md` to the default greenfield `init` file set.
   Tracks are opt-in.

## Maintain Workflow

1. Read the repository router and relevant planning docs.
2. Keep track entries compact:
   - status;
   - owner;
   - last reviewed date;
   - outcome;
   - work items;
   - active notes only.
3. Move durable choices that emerge from track work into the decisions home.
4. Move repeatable procedures into the workflows home.
5. Move short scratch checklists into the todo home when they do not need
   session-to-session context.
6. Summarize completed track details instead of letting `docs/tracks.md` become
   an archive.

## Review Workflow

For review-only requests, report:

- tracks with no recent review date;
- tracks whose work items are all complete but whose status is not `Done`;
- track notes that look like durable decisions or repeatable procedures;
- track items that are small enough to belong in `docs/todo.md`;
- roadmap direction that should be promoted to `docs/plan.md`.

Do not edit files during review unless the user explicitly asks to apply a
specific update.

## Validation

After edits, run the Waypoint doctor fallback when available:

```bash
python3 <waypoint-plugin-root>/scripts/waypoint_doctor.py --repo-root <target-repo>
```

If the target repository is not a Waypoint repository, still preserve existing
instructions and report what validation could not run.

## Safety Boundaries

- Tracks are optional.
- Do not force repositories away from todo-only planning.
- Do not turn `.waypoint/config.yaml` into task state.
- Do not weaken existing repository rules.
- Ask before making durable naming, taxonomy, public documentation, security,
  privacy, release, or irreversible migration decisions.

## Feedback

If this plugin behaves unexpectedly, open an issue at `97Wobbler/my-ai-kit`
with the plugin name, runtime, expected behavior, and observed behavior.

## Runtime Overrides

Users may call this skill as `$tracks` when unambiguous, or by saying `use waypoint:tracks`.
Use `request_user_input` only in Plan Mode. In Default mode, ask concise direct questions only when the target repository, enable-vs-maintain mode, or routing update scope is blocking.
For manual file edits, use `apply_patch` and preserve unrelated user changes.
