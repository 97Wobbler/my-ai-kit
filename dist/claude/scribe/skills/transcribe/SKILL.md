---
name: "transcribe"
description: "User-facing Scribe transcription workflow for local audio files. Use when the user provides an audio file path and asks to transcribe it, convert speech to text, create a transcript, STT an audio recording, or says \"음성파일 전사\", \"전사해줘\", or \"이 파일 텍스트로 바꿔줘\"."
---

# Transcribe

This skill was compiled from a Skill Forge runtime-neutral spec for the
Claude Code runtime.

Source spec: private Skill Forge source (not included in distribution): `transcribe.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- Ask clarification questions only when they materially change the result.
- Follow repository edit instructions and preserve unrelated user changes.
- Delegate only when the runtime supports subagents and the task can run safely in parallel.
- Run the relevant validation checks before reporting completion.

## Purpose

Use this skill when a user wants a usable transcript from a local audio file. The user should be able to provide only an audio path and a request such as "transcribe this", "make a transcript", "run STT", or "음성파일 전사해줘".

This skill is the user-facing workflow facade for Scribe STT. It owns path resolution, safe default inference, minimal blocking questions, Scribe MCP orchestration, long-audio expectation setting, fallback confirmation, post-STT quality review, and the final response. Scribe MCP tools are implementation details by default.

Do not use this skill for reconciling existing transcript files unless the user also needs STT from audio. Existing multi-variant transcript reconciliation belongs to `scribe:canon`.

## Input Contract

Accepted input:

- A local audio file path supplied in the user request.
- A relative path that can be resolved from the current working directory.
- A quoted or unquoted path with spaces.
- A file path plus optional user preferences such as language, desired quality, output directory, deadline, model size, or "canonical transcript".
- A directory only when the user's request or nearby files make the target audio file unambiguous.

Supported audio formats are whatever the Scribe STT backend and local media stack can read. Common cases include `.m4a`, `.mp3`, `.wav`, `.mp4`, `.mov`, `.aac`, `.flac`, and `.ogg`.

If the request contains multiple audio paths, ask whether to transcribe all files or only selected files before starting unless the wording clearly says to process all.

If the path is missing, ambiguous, does not exist, is not a file, or points to a directory with multiple plausible audio files, ask one blocking question for the exact file path. Do not scan broad unrelated directories to guess.

## Safe Defaults

Infer defaults conservatively so a plain file-path request can start without an interview:

- `language`: omit the hint unless the user states one or the filename/context makes it obvious and low risk.
- `output_root`: prefer an obvious nearby or sibling transcript directory when one is clearly present and unambiguous for the same work area, such as `transcripts/`, `transcript/`, or a similarly named directory beside the audio file or its parent. Put this run under a new `<audio-stem>-scribe/` child of that transcript directory. Otherwise create a sibling directory named `<audio-stem>-scribe/` beside the audio file. If the selected path exists, use `<audio-stem>-scribe-2/`, `<audio-stem>-scribe-3/`, and so on rather than overwriting.
- `variant_count`: use `1` for a normal "transcribe this" request.
- `preset`: use Scribe's default balanced path for a single transcript.
- `canonical output`: use multiple variants only when the user asks for canonical reconciliation, high-confidence cleanup, comparison, or ambiguity reduction, or when they explicitly accept the extra time.
- `post-STT review`: always do at least a lightweight quality scan of the generated transcript before the final response.
- `speaker labels`: do not invent diarized speaker labels. Preserve speaker labels only when the STT output contains them or the user supplied reliable labels separately.
- `timestamps`: preserve generated timestamps when present.

Prefer the first usable transcript over a slow multi-variant run when the user's request is simply "transcribe this file." Offer canon as the next action after output exists.

## Minimal Blocking Questions

Ask only when the answer materially changes the run or avoids unsafe behavior.

Blocking questions:

- exact audio path when missing or ambiguous;
- whether to overwrite or choose a new output directory when the user explicitly requested an existing output path;
- whether to process multiple audio files when the request includes more than one and intent is unclear;
- whether to install missing local STT dependencies if the Scribe status check reports setup is required;
- whether to use a degraded fallback that lowers expected quality, changes the promised output type, or bypasses the normal Scribe MCP path;
- whether to continue with canonical reconciliation when that requires materially more time and the user did not already request high-confidence output.

Do not ask preflight questions for language, model size, variant count, long-audio strategy, output root, job ids, manifest paths, or presets when safe defaults are enough. Ask about output root only when there are multiple plausible transcript output locations and choosing incorrectly would surprise the user.

If the user supplies optional preferences, honor them when they are compatible with the current Scribe tools. If a preference is unsupported, explain the smallest adjustment and ask only when there are multiple reasonable alternatives.

## User Communication Policy

Default user-facing updates should describe workflow state, not implementation details.

Say once when the file is found and transcription starts. For long audio, include a single expectation-setting sentence:

```text
I found the file and started transcription. This recording is long, so it may take a while; I will report back when there is a usable result or a decision is needed.
```

After that, report only meaningful milestones:

- dependencies are missing and setup needs approval;
- transcription started;
- first usable transcript is ready;
- a degraded fallback choice is needed;
- the run failed and needs a recovery decision;
- high-impact uncertainty needs a short clarification;
- the workflow is done.

For long audio, keep Scribe-specific updates sparse and milestone-based. Do not send repeated "still running" messages just because polling continues. If the host runtime or general agent instructions force periodic progress updates, keep them non-technical, non-repetitive, and avoid adding Scribe backend detail unless the user asks for status.

Avoid default updates about MCP tool names, job ids, `job.json`, process ids, CPU, memory, transport state, partial file absence, model internals, or polling loops. Surface those details only when the user asks for debugging detail or when they are required to make a recovery decision.

## Hidden MCP Orchestration

Use Scribe MCP tools as the default execution path when they are available.

Default orchestration:

1. Check STT readiness.
2. If dependencies are missing, ask before installing anything. If OS-level dependency installation is required, report the exact manual requirement and stop until the user confirms it is handled.
3. Inspect the audio file enough to choose synchronous versus background execution when the tool provides file metadata or long-audio guards.
4. For normal short audio, run a single transcript with the balanced default path.
5. For long audio or any case likely to exceed a foreground tool-call limit, start a background Scribe job.
6. Poll or collect background jobs sparingly. Continue in the same workflow until there is a usable transcript, a terminal failure, or a user decision is required.
7. Read `manifest.json`, `job.json`, and generated `variants/<variant_id>.md` files only as needed to determine status, transcript paths, and post-STT routing.

When the MCP response includes a Scribe handoff block, treat it as routing guidance. Verify referenced files exist before using them.

If the MCP tool returns a long-audio guard instead of a transcript, switch to the background job path rather than asking the user to understand the guard.

Do not kill MCP processes, bypass the transport, or run local backend scripts as the first response to slow execution. Use cancellation tools when available. Direct local runtime execution is a degraded rescue path and requires confirmation.

## Long Audio Handling

Long recordings are expected to run slowly. Do not present slowness itself as failure.

For long audio:

- prefer the background job path;
- set expectations once before waiting;
- keep status checks internal unless state changes or the user asks for status;
- collect completed output when available;
- do not repeatedly tell the user that the job is still running;
- when a runtime-level progress update is unavoidable, say only that the transcription is still in progress and you will return when there is a result or decision point;
- do not cancel solely because the run is long unless the user asks, resources are clearly exhausted, or the tool reports a terminal problem.

If only partial output exists:

- if one completed variant exists, treat it as a usable draft transcript and offer review or another variant;
- if two or more completed variants exist, the output can route to `scribe:canon` as partial input;
- if no completed variant exists, report the failure or running status and present the smallest next action.

## Degraded Fallback Confirmation

Get visible user confirmation before any fallback that changes the quality or trust contract.

Confirmation is required before:

- switching from multi-variant output to a single rough transcript;
- using a smaller or faster model than the requested/default quality path when quality will likely drop;
- bypassing Scribe MCP tools with direct local scripts or another runtime path;
- continuing from partial output when the requested output was canonical or high-confidence;
- discarding timestamps, segment data, or variant metadata because only plain text could be produced;
- committing, publishing, or moving generated transcript artifacts outside the chosen output directory.

The confirmation question must name the tradeoff in user terms:

```text
The normal Scribe path is not producing a result yet. I can make a rough single-pass transcript with a faster lower-quality path, but names and domain terms will need review. Continue with that fallback?
```

If the user already requested speed over quality, smaller-model or single-pass choices can be treated as expected behavior, but label the final quality status accordingly.

## Post-STT Routing

After STT output exists, do not stop at "files were created." Choose the next route from the available evidence and the user's original intent.

Route to `scribe:canon` when:

- two or more completed transcript variants exist for the same audio;
- the user asked for canonical, high-confidence, reconciled, cleaned-up, or ambiguity-reduced output;
- the output manifest or job handoff says canon is ready and the user's request implies more than a raw draft;
- partial output has at least two completed variants and the user accepts proceeding with a partial input set.

For canon handoff:

- use the generated `manifest.json` or job directory as input;
- preserve the audio path and variant metadata;
- follow `scribe:canon` evidence-first clarification rules;
- do not present MCP internals as the reason for the handoff.

Route to single-transcript review when:

- exactly one transcript variant exists;
- the user asked only for a transcript;
- a degraded fallback produced one transcript;
- canon is not available or would overstate confidence.

Single-transcript review is lighter than canon. It should:

- scan the transcript for likely STT errors, proper nouns, acronyms, project or product names, numbers, dates, decisions, action items, and negations;
- ask only for high-impact uncertainty that materially affects transcript usefulness or downstream summary;
- write a lightweight `transcript-review.md` beside the transcript when any high-impact or notable medium-impact uncertainty is found;
- after identifying high-impact items, call `scribe_build_review_state` when the Scribe MCP tool is available, or use the equivalent structured review state if the MCP response already provided one;
- pass the high-impact items plus transcript, review, and manifest paths into the structured gate so it returns `review_state`, top-level `requires_user_response`, and `clarification_packet`;
- make the structured gate authoritative for workflow control. If Markdown review notes and `review_state` disagree, follow `review_state` and mention the mismatch as a review warning;
- if `requires_user_response=true`, treat it as a hard conversational gate: the workflow is not complete, and the assistant must end the turn with a direct question or explicit choice and wait for the user;
- do not satisfy the gate by listing high-impact terms in a completion summary. A one-way list of terms, artifact links, or "review needed" label without a question or choice is non-compliant;
- cap staged clarification to the top 3-5 high-impact items, prioritizing terms that affect names, numbers, dates, decisions, commitments, action items, speaker attribution, or negation;
- after the first packet, use ping-pong clarification: wait for the user's answers, then ask the next small batch only if needed;
- avoid claiming multi-variant confidence.

If the transcript is obviously rough but usable, label it as `draft` and recommend review before downstream summary or publication.

Distinguish the state explicitly:

- `transcript generated`: a transcript file exists and has been checked enough to report its path and quality status;
- `review needed`: high-impact uncertainty remains and the user has not confirmed, corrected, or accepted it;
- `review complete`: the user has resolved the high-impact uncertainty or explicitly accepted the remaining risk.

Do not describe the workflow as fully done when the transcript is generated but high-impact review is still needed. In that state, report that transcription output exists and present the next review step.

## Output Contract

Default output layout for a single-pass transcript:

```text
<audio-stem>-scribe/
  manifest.json
  variants/
    <variant_id>.md
    <variant_id>.json
  transcript-review.md
```

For background jobs, `job.json` may also be present. For multi-variant runs, multiple `variants/<variant_id>.*` files should be present and the next route may create `canonical-transcript/` via `scribe:canon`.

When writing `transcript-review.md`, use this structure:

```md
# Transcript Review

- audio_path:
- transcript_path:
- input_status: complete | partial | degraded
- quality_status: draft | usable-draft | needs-review | failed
- review_scope: single-transcript

## High-Impact Items

## Medium-Impact Notes

## Low-Impact Notes

## Recommended Next Action
```

Use `High-Impact Items` for likely proper-noun, number, date, speaker, commitment, decision, action-item, or negation errors. Keep low-impact filler, punctuation, and style notes concise.

## Final Response

The final response must include:

- transcript path;
- quality status;
- whether output is complete, partial, or degraded;
- whether timestamps or speaker labels are present when known;
- review or canon path if created;
- current state: `transcript generated`, `review needed`, or `review complete`;
- next recommended action or the short staged clarification packet required for review.

Keep the final response short and user-oriented. Do not include transcript content by default unless the user asked for inline output.

If `review_state.requires_user_response=true` or the top-level `requires_user_response=true`, the final response is a review-gate turn, not a completion summary. It must include the transcript path, quality status, review path, `State: review needed`, and then end with the `clarification_packet` as a direct question or explicit choice. Do not say the workflow is complete, and do not close with a one-way list of terms.

Expected shape while the structured gate is active:

```text
Transcript generated: `<path/to/variants/balanced.md>`.
Quality: usable draft, single-pass STT, timestamps present, no speaker diarization.
State: review needed. Review file: `<path/to/transcript-review.md>`.

Please choose one:
1. Answer these review items now: `<item 1 question>`, `<item 2 question>`, `<item 3 question>`.
2. Accept draft risk and proceed with the transcript as-is.
3. Defer review and leave the transcript marked `review needed`.
```

The final line must be a direct question or choice that waits for the user's response.

If `transcript-review.md` has non-empty `High-Impact Items` but no structured review state is available, the final response must not stop at artifact links. It must either:

- ask the top 3-5 high-impact clarification questions directly in chat;
- present a concise choice such as "review these top terms now" versus "proceed with the draft and accept the uncertainty"; or
- state that review is needed and ask for permission to continue with the staged clarification packet.

Use the smallest packet that moves the workflow forward. Do not ask a long list in one turn.

Example:

```text
Transcript generated: `<path/to/variants/balanced.md>`.
Quality: usable draft, single-pass STT, timestamps present, no speaker diarization.
State: review needed. Review file: `<path/to/transcript-review.md>`.
Please confirm these first 3 high-impact items: `<item 1>`, `<item 2>`, `<item 3>`. After that I can continue the review or use the draft as-is if you accept the uncertainty.
```

If the workflow failed, the final response must include:

- what user-visible step failed;
- whether any partial transcript exists;
- the smallest recovery choice;
- whether a degraded fallback is available and what quality tradeoff it carries.

## Guardrails

- Do not invent speech that is missing from STT output.
- Do not infer speaker labels without diarization metadata or user-supplied labels.
- Do not treat a single transcript as equivalent to multi-variant canonical reconciliation.
- Do not silently normalize names, acronyms, numbers, dates, decisions, or negation when the transcript is uncertain.
- Do not expose private transcript content in chat beyond what the user requested.
- Do not ask broad context interviews before STT. Ask targeted questions only after evidence shows they matter, unless the path or execution choice is blocked.
- Do not claim persistent Scribe memory, glossary, or diarization exists unless a future version explicitly implements it.
- Do not publish or snapshot generated transcripts.

## Completion Criteria

Before reporting completion:

- confirm the transcript file exists, or clearly report that no transcript was produced;
- confirm the output root and manifest or job status when available;
- classify quality as `draft`, `usable-draft`, `needs-review`, `canonical-ready`, `canon-complete`, `partial`, `degraded`, or `failed`;
- run or route to the appropriate post-STT review path;
- when high-impact items are found, call `scribe_build_review_state` or consume the equivalent structured review state;
- distinguish `transcript generated`, `review needed`, and `review complete`;
- when `requires_user_response=true`, stop before completion and end with a capped clarification packet or explicit next-action choice in chat;
- report transcript path, quality status, review state, and next action in the final response.

## Runtime Overrides

Claude Code users may invoke this skill as `/scribe:transcribe`.
Use Claude Code's native user-question flow only for truly blocking decisions, degraded fallback confirmation, or a short high-impact post-STT clarification packet.
Use the Scribe MCP tools when available, but keep tool names, job ids, job paths, transport details, and backend internals out of user-facing updates unless the user asks for debugging detail.
