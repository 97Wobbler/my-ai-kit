---
name: "traceback"
description: "Recover relevant prior context from local Codex or Claude sessions. Use when the user asks what happened before, why a decision was made, to find a past conversation, restore session context, or trace earlier work on the current request."
---

# Traceback

This skill was compiled from a Skill Forge runtime-neutral spec for the
Codex CLI runtime.

Source spec: private Skill Forge source (not included in distribution): `traceback.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- Run the relevant validation checks before reporting completion.

# Traceback

Recover only the prior context relevant to the current request.

1. Use project path, date, session ID, filenames, and distinctive phrases as discovery clues. Search the current project first.
2. If the current-project search finds no useful result, tell the user that the search is expanding, then continue across local projects without waiting for approval.
3. Inspect metadata and small previews first. Expand only the sessions and tool evidence needed to understand the work.
4. Follow related, continued, compacted, connected, or subagent sessions when relevant. Group duplicates by actual work context rather than file count.
5. Filter system instructions, hooks, injected skill bodies, repeated snapshots, and unrelated conversation from the result.
6. Distinguish recorded facts, reconstruction, and incomplete or stale information. Re-read referenced workspace files when current state matters.

Session files are read-only evidence. Assume their full contents may be inspected during recovery, but do not expose raw transcripts or session identifiers in the response unless the user asks or they materially help continuation.

## Feedback

If this plugin behaves unexpectedly, open an issue at `97Wobbler/my-ai-kit` with the plugin name, runtime, expected behavior, and observed behavior.

## Runtime Overrides

Use fast file search and narrow previews before reading larger session records. Treat session data as read-only evidence.
