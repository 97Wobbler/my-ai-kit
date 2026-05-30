---
name: "canon"
description: "Reconcile multiple STT transcript files from the same audio into a canonical transcript. Use when the user has 2-4 transcript variants and wants a canonical transcript, ambiguity review, or STT conflict reconciliation; triggers include \"canonical transcript\", \"STT 전사 비교\", \"전사 정리\", \"canonical 전사\", and \"모호함 리포트\"."
---

# Canon

This skill was compiled from a Skill Forge runtime-neutral spec for the
Codex CLI runtime.

Source spec: private Skill Forge source (not included in distribution): `canon.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- Ask clarification questions sparingly; `request_user_input` is Plan Mode only.
- For manual file edits, use `apply_patch` and preserve unrelated user changes.
- Delegate only when the runtime supports subagents and the task can run safely in parallel.
- Run the relevant validation checks before reporting completion.

## Purpose

Use this skill to turn multiple STT transcript variants from the same recording into a traceable canonical transcript. The skill does not run STT. It assumes transcript files, a Scribe manifest, or a Scribe STT job directory already exist.

The core job is evidence-first reconciliation: compare variants, use any upfront context as a prior when supplied, ask a targeted clarification packet generated from the transcript evidence before high-impact normalization, choose the most defensible wording after that packet is answered, and isolate remaining ambiguity for review.

## Input Contract

Expected input:

- A Scribe STT MCP output directory, or its `manifest.json`, is a first-class accepted input.
- A Scribe STT MCP job directory, or its `job.json`, is a first-class accepted input. If `manifest.json` already exists beside the job file, prefer the manifest as the transcript index and use `job.json` for job status, partial-output, and failure context.
- When `manifest.json` is provided, use it as the input index for `audio_path`, `created_at`, variant metadata, and relative transcript paths.
- Generated `variants/<variant_id>.md` files referenced by `manifest.json` are transcript inputs and should be reconciled as the STT variants.
- Partial Scribe job output can be used when at least two completed variant markdown files exist. If fewer than two completed variants exist, report the job status and ask whether to retry, wait, run another variant, or do a light single-transcript cleanup.
- 2-4 transcript files from the same audio when no Scribe manifest is available.
- Optional companion metadata such as `variants/<variant_id>.json`, model names, language, timestamp availability, speaker label availability, and notes.
- Optional user-provided context such as meeting purpose, interview topic, product names, participant names, abbreviations, or preferred terminology.

If fewer than two transcript variants are available, ask whether the user wants a light cleanup instead. Do not pretend single-transcript cleanup has multi-STT confidence. If a job failed after writing partial outputs, decide from the manifest and job status whether enough completed variants exist to continue; if not, surface the failure and the smallest next action.

## Output Contract

Default output directory:

- If all input files share one parent directory, write under `<input-parent>/canonical-transcript/`.
- Otherwise write under `<cwd>/canonical-transcript/`.
- If the output path exists, inspect it and ask before overwriting or appending.

Create these files:

```text
canonical-transcript/
  canonical.md
  ambiguity-review.md
  reconciliation-ledger.md
```

`canonical.md` is the readable transcript. `ambiguity-review.md` is the review surface for remaining uncertainty, with high-impact items clearly separated from low-impact notes and a resumable `pending-clarifications` surface for staged review. `reconciliation-ledger.md` records how transcript variants were aligned and reconciled, including which clarification items were answered, deferred, or still pending.

## STT-To-Canon Handoff

When the previous step generated Scribe STT variants and the user's original request asked for canonical output, continue directly into this skill instead of stopping at "files were created." Use the generated `manifest.json` or job directory as the input, run the evidence-first scan, and present the clarification packet before writing canonical prose that depends on high-impact inferred terms.

If the Scribe MCP response includes a handoff block, follow it as routing guidance only. Still verify that the referenced `manifest.json`, `job.json`, and variant files exist before reconciling.

When STT generation is incomplete:

- If two or more completed variant markdown files exist, you may proceed with canon as `status: draft` and clearly label the input set as partial.
- If exactly one completed variant exists, ask whether to run or wait for another variant, retry failed output, or perform light cleanup.
- If no completed variant exists, do not start canon; report the STT failure or job status and recommend the next transcription action.
- If the job is still running, do not block indefinitely. Check status, report completed variants, and proceed only when enough completed outputs exist or the user asks to wait.

## Workflow

### 1. Resolve Inputs And Upfront Context

Identify transcript files and optional manifests from the user's request or the current working directory. If paths are unclear, ask for the transcript file paths before reading broadly.

If a Scribe STT MCP `manifest.json` is provided, or a provided directory contains one, read it before scanning for loose transcript files. Resolve each `variants[].text_path` relative to the manifest directory; these are normally `variants/<variant_id>.md` files. Treat those variant markdown files as the primary transcript inputs. Use manifest fields such as `variant_id`, `backend`, `preset_id`, `model`, `language`, `segment_count`, `audio_path`, and `created_at` to label and trace reconciliation decisions.

If a Scribe STT `job.json` is provided, read it before loose transcript scanning. If a sibling `manifest.json` exists, use it as the primary transcript index. Use `job.status`, per-variant status, `errors`, `cancel_requested`, and `completed_at` to label whether the input is complete, partial, failed, cancelled, or still running.

If the manifest also references `variants/<variant_id>.json`, use it only as companion structured metadata or a fallback for segment timing. Do not prefer JSON over the readable variant markdown unless the markdown file is missing or unusable.

Accept common text-like formats such as `.txt`, `.md`, `.srt`, `.vtt`, `.json`, and `.csv` when their contents are transcript-like. Preserve timestamps and speaker labels when present.

Capture optional user-provided context from the initial request or companion notes and treat it as a prior for evidence interpretation. Do not require context before reading and scanning the transcript variants. Do not run a separate preflight recording-context interview.

Persistent context memory is exploratory only. Do not claim to load, store, or apply previous Scribe context unless the user explicitly supplies a file or notes in the current request.

### 2. Evidence-First Alignment Scan

Read the transcript variants and create a first comparable alignment before asking context questions.

- If reliable timestamps exist, align by timestamp windows and speaker turns.
- If timestamps are missing, align by paragraph, sentence, or semantic sequence.
- If speaker labels conflict, preserve the uncertainty in the ledger and escalate only when the speaker identity changes meaning or accountability.

During this scan, extract:

- candidate proper nouns: people, companies, products, projects, teams, acronyms, places;
- likely abbreviations, acronyms, expansions, and recurring domain terms;
- candidate speakers and roles;
- dates, numbers, versions, URLs, email-like strings, and task or decision language;
- repeated words that differ across STT variants;
- segments where variants diverge in meaning;
- likely STT error patterns, including homophones, repeated substitutions, casing or spacing errors, dropped negation, duplicated fragments, and punctuation artifacts.

For every candidate recommendation that is not directly present in transcript text, record provenance using these labels:

- `transcript evidence only`
- `user-supplied context`
- `current-session context`
- `workspace/repo context`
- `prior approved Scribe memory`
- `external lookup`

Also record contamination risk as `none`, `low`, `medium`, or `high`. Use `high` when a recommendation depends on context from earlier in the same assistant thread or another local workspace rather than the supplied transcript or user-provided context. If persistent memory was not consulted, say so explicitly in the scan notes or ledger.

Do not finalize canonical wording during this scan. Do not write high-impact inferred terms into canonical prose as confirmed fact before the clarification packet is answered. If the user explicitly asks for a draft before review, mark the file `status: draft`, flag the specific terms as provisional inline or in an adjacent note, and include provenance for each high-impact provisional term.

For very long transcripts, split by natural boundaries such as timestamps, agenda sections, speaker turns, or long pauses. If using subagents, assign non-overlapping ranges and require each result to return segment IDs, evidence summaries, conflict groups, proper-noun and glossary candidates, likely STT error patterns, and local ambiguity items.

### 3. Build Staged Clarification Packets

After the evidence-first scan, generate staged clarification packets from observed transcript evidence. Use upfront user context as a prior: apply it to reduce unnecessary questions, but keep uncertainty visible when transcript evidence still conflicts.

Clarification stages are ordered by impact:

- Stage 1: product names, service names, project names, people names, speaker roles, numbers, dates, versions, URLs, negation, decisions, commitments, accountability, and action items. Ask these first when they affect canonical prose or downstream interpretation.
- Stage 2: recurring terminology, glossary candidates, acronyms, abbreviations, preferred casing, expansions, and repeated STT error patterns that affect many segments.
- Stage 3: local medium-impact wording only when it affects the user's intended use, such as publication, legal review, research coding, product decisions, or direct quotation.

Each stage must be small enough for one user reply. Prefer a capped top-N set or representative groups when there are too many items. Defer the rest into `pending-clarifications` instead of asking a dense all-at-once interview. A stage can ask for:

- missing basic recording context such as recording type, purpose, topic, and participant roles when not already supplied;
- preferred spelling for extracted proper-noun, abbreviation, acronym, and terminology candidates;
- high-impact conflict choices where variants imply different names, numbers, dates, speakers, commitments, negation, action items, or decisions;
- glossary and style-rule candidates discovered from recurring terms, casing, expansions, or repeated STT error patterns.

Each recommendation in a stage must show:

- transcript evidence, including the exact observed wording or a short paraphrase of the conflicting span;
- affected location or segment range when known;
- recommended value and alternatives;
- provenance labels from the evidence-first scan;
- contamination risk and the reason for that risk;
- the impact if the recommendation is wrong.

Ask the active stage and wait before generating canonical prose that depends on unresolved high-impact decisions. Do not ask the user to resolve low-impact filler, punctuation, or purely stylistic issues. If the scan finds no high-impact uncertainty and no context answer would materially change wording, record that no clarification packet was needed and continue.

When a stage is too large:

- ask only the highest-impact top-N items or one representative group per recurring issue;
- write the rest to `pending-clarifications` with `why_pending: stage capacity` or a more specific reason;
- keep high-impact inferred terms out of confirmed canonical prose until the user confirms them;
- continue to the next stage only after applying the user's answers to the active stage and updating pending status.

Do not hide lower-priority ambiguity. Defer it into `ambiguity-review.md` and the ledger when it does not block canonical prose.

### 4. Generate Canonical Transcript

Generate the canonical transcript only after the clarification packet or required stage has been answered, or after explicitly recording that no packet was needed. Refine the segment alignment as needed while selecting final wording.

For each segment, choose wording using this priority:

1. user-confirmed names, terms, speakers, and recording context from upfront notes or the clarification packet;
2. agreement across STT variants;
3. supplied context with explicit provenance;
4. surrounding transcript context and domain vocabulary;
5. grammatical and conversational plausibility;
6. preservation of numbers, negation, commitments, and decision language.

Keep spoken transcript character. Clean obvious STT artifacts, duplicated fragments, and impossible punctuation, but do not turn the transcript into meeting minutes or product analysis.

When a high-impact term remains unconfirmed, do not silently normalize it. Either keep the transcript-evidence wording, mark the normalized term as provisional with visible provenance, or route it to `ambiguity-review.md` and keep `canonical.md` in `draft` status.

### 5. Classify Remaining Ambiguity

Classify uncertainty by user-impact, not by how much the model hesitates.

`high`:

- proper noun, speaker identity, number, date, decision, commitment, negation, or action item may be wrong;
- STT variants imply materially different meanings;
- the segment affects interpretation, accountability, or future product decisions.

`medium`:

- wording differs but the likely meaning is stable;
- context supports a recommended reading, but an alternative remains plausible.

`low`:

- filler words, endings, punctuation, minor disfluency, or style;
- wording differs without changing meaning.

Route remaining ambiguity into `ambiguity-review.md`. Include unresolved staged-review items in `pending-clarifications` so the user can resume later by editing the review file or answering inline. Do not start another default interview for low-impact ambiguity after canonical generation; put low-impact items in a concise low-impact notes section unless the user explicitly requested exhaustive review.

### 6. Review Strategy

Always write `ambiguity-review.md`, even when there are no high-impact items. Use it to preserve unresolved high-impact items, optional medium-impact items, and concise low-impact notes that should not trigger another interview by default.

Use this threshold:

- 0-10 high-impact Stage 1 items: ask or summarize them as the active stage and write the file.
- 11-40 high-impact Stage 1 items: ask only the top-N or grouped representatives that can fit in one reply, write the rest to `pending-clarifications`, and ask the user to edit `user_decision` or `correction` fields for deferred items when needed.
- More than 40 high-impact Stage 1 items: group by issue type first, ask representative naming, speaker-role, number/date, negation, decision, commitment, or action-item groups, and keep the remainder pending before doing final cleanup.
- Stage 2 and Stage 3 items: ask only when they materially change many segments or the user's intended use. Otherwise record them as pending or optional review notes.

Ambiguity review item format:

```md
### A-001

- location:
- issue_type:
- severity:
- recommended:
- alternatives:
- reason:
- source_variants:
- evidence:
- provenance:
- contamination_risk:
- user_decision:
- correction:
```

Pending clarification item format:

```md
### P-001

- id:
- stage:
- impact:
- location_range:
- recommendation:
- alternatives:
- transcript_evidence:
- provenance:
- contamination_risk:
- why_pending:
- next_action:
- user_decision:
```

Use stable pending IDs so a later edited `ambiguity-review.md` or inline answer can be mapped back to canonical text and ledger entries. `stage` must be `1`, `2`, or `3`. `impact` must be `high`, `medium`, or `low`. `next_action` should name the smallest useful user action, such as `confirm recommended spelling`, `choose alternative`, `provide role`, `accept provisional wording`, or `leave transcript-evidence wording`.

### 7. Write Outputs

`canonical.md` should include:

```md
# Canonical Transcript

- source_files:
- context:
- input_status: complete | partial | failed-partial
- clarification_packet:
- status: draft | user-reviewed | final

## Transcript

...

## Remaining Ambiguities

## Pending Clarifications
```

`reconciliation-ledger.md` should include:

```md
# Reconciliation Ledger

## Inputs

## Context Supplied By User

## Provenance Model

## Evidence-First Scan Notes

## Clarification Packets

## Pending Clarifications

## Alignment Notes

## Segment Decisions
```

For each segment decision, record the segment ID, location, selected canonical wording or summary, notable alternatives, confidence, ambiguity IDs, pending clarification IDs when relevant, evidence used, provenance labels, and contamination risk. If current-session context influenced a decision, write that fact explicitly instead of presenting it as transcript-only evidence.

### 8. Apply User Review

When the user returns with an edited `ambiguity-review.md`, pending clarification decisions, or inline answers, match answers by stable ambiguity and pending IDs, apply corrections to `canonical.md`, update related ledger entries, and change status to `user-reviewed` or `final` only when all high-impact ambiguity is resolved or explicitly accepted. If medium-impact or low-impact pending items remain, keep them in `Pending Clarifications` with a clear next action instead of blocking finalization unless the user's stated use requires them.

## Guardrails

- Do not invent missing speech.
- Do not use outside facts to override the transcript unless the user provided them as context.
- Do not silently normalize names, brands, or acronyms without evidence or user confirmation.
- Do not treat current-session or workspace context as clean transcript evidence. Label it as current-session context or workspace/repo context and record contamination risk.
- Do not write high-impact inferred terms into canonical prose as confirmed fact before user confirmation. If an early draft is unavoidable, mark those terms provisional and include provenance.
- Do not mix research interpretation, product recommendations, or meeting-summary claims into the canonical transcript.
- Do not discard uncertainty; route important uncertainty into `ambiguity-review.md`.
- Do not present persistent Scribe context memory as implemented; it is exploratory unless a future version explicitly adds it.
- Do not expose private or sensitive transcript content in final chat beyond the user's requested summary.

## Completion Criteria

Before reporting completion:

- confirm all declared output files exist;
- confirm every high-impact ambiguity has an entry in `ambiguity-review.md`;
- confirm every inferred proper noun or terminology recommendation has evidence, provenance, and contamination risk recorded;
- confirm `canonical.md` preserves timestamps and speaker labels when available;
- report whether the transcript is `draft`, `user-reviewed`, or `final`;
- list the next required user action if high-impact ambiguity remains.

## Runtime Overrides

Codex users may invoke this skill as `$canon`, `$scribe:canon`, or by saying "use scribe:canon".
Use `request_user_input` only in Plan Mode, and only for grouped or staged evidence-derived clarification, or truly blocking input/output-path decisions.
In Default mode, ask concise grouped or staged plain-text clarification and wait when a blocking answer is required.
For manual file edits, prefer `apply_patch`; use `rg` for file searches when available.
