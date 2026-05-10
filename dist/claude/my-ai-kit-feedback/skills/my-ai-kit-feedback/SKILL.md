---
name: "my-ai-kit-feedback"
description: "Privacy-conscious dogfooding issue reporter for my-ai-kit plugins and skills. Use only when the user explicitly invokes my-ai-kit-feedback or explicitly asks to draft/report a my-ai-kit plugin feedback issue from provided session evidence."
---

# My Ai Kit Feedback

This skill was compiled from a Skill Forge runtime-neutral spec for the
Claude Code runtime.

Source spec: private Skill Forge source (not included in distribution): `my-ai-kit-feedback.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- Use Claude Code's native blocking question flow when clarification is required.
- Use network access only when current or external facts are required.
- Run the relevant validation checks before reporting completion.

## Purpose

Use this skill to turn an explicitly reported my-ai-kit plugin or skill problem
into a privacy-conscious GitHub issue draft. The skill is for dogfooding and
public user feedback: it helps capture what the user expected, what happened,
which runtime was involved, and what session evidence supports the report.

The skill must not behave like a background telemetry collector. It is a
consent-gated issue-writing workflow.

## Activation Rules

Use this skill only when the user explicitly invokes `my-ai-kit-feedback` or
explicitly asks to draft, report, or file feedback about a my-ai-kit plugin or
skill.

Do not activate for generic frustration, words like "weird" or "broken", or
ordinary debugging requests unless the user directly connects the request to
my-ai-kit feedback reporting.

If the user asks for normal implementation help, debugging, or plugin usage
guidance, do not convert it into a feedback report unless they ask.

## Privacy Rules

These rules override every other workflow step.

1. Do not automatically discover, search, or read session logs.
2. Do not read home-directory runtime state such as `.codex`, `.claude`, shell
   history, config files, transcripts, logs, or cache directories unless the
   user explicitly provides exact paths or pasted excerpts for this invocation.
3. Prefer user-pasted excerpts, screenshots transcribed by the user, or
   user-written summaries over raw session files.
4. Summarize evidence by default. Include only short quotes when they are
   necessary to show the behavior.
5. Before any quote or path appears in an issue draft, redact secrets, tokens,
   personal names, email addresses, company names, private repository names,
   local absolute paths, and unrelated task content.
6. Never include full transcripts by default.
7. Stop if the user is unsure whether they have permission to share the
   session content.

## Three Consent Gates

Always pass through these gates in order. Do not collapse them into one broad
approval.

### Gate 1: Scope And Evidence Consent

Confirm the report scope before reading or analyzing evidence.

Collect:

- affected plugin and skill, for example `autorun` / `autorun` or `lucid` /
  `branch`;
- runtime: Claude Code, Codex CLI, Codex app, or unknown;
- expected behavior;
- actual behavior;
- approximate time window or session context;
- evidence source: pasted excerpt, user summary, or exact local path supplied
  by the user;
- target repository: public `97Wobbler/my-ai-kit` by default, or a maintainer
  dev repository if the user explicitly chooses it.

If the user has not provided evidence yet, give a collection guide and stop for
their response. Do not inspect runtime directories yourself.

### Gate 2: Evidence Review And Redaction

After the user provides evidence, summarize what the evidence shows and list
the redactions you will apply.

Classify evidence as:

- strong: directly shows expected versus actual behavior;
- medium: supports the timeline or environment but not the failure itself;
- weak: anecdotal or ambiguous.

Ask for approval before turning the evidence into an issue draft. If the user
does not approve the redaction plan, revise it or stop.

### Gate 3: Publication Approval

Draft the GitHub issue first. Do not create it yet.

Ask the user to approve:

- target repository;
- title;
- labels;
- body;
- whether to create the issue now or leave it as a draft.

Only create an issue after the user explicitly says to create or publish it.
If no GitHub tool is available, provide the final issue text.

## Evidence Collection Guide

When the user needs help collecting evidence, give guidance instead of
collecting it yourself.

Preferred order:

1. Ask the user to paste a short excerpt around the failure and remove secrets
   first.
2. Ask the user to write a short timeline from memory.
3. If excerpts are needed, ask the user to search locally by plugin name, skill
   name, time window, and distinctive phrases, then paste only relevant lines.
4. If the user wants file-based analysis, ask them to provide exact file paths
   and confirm that reading those files is allowed for this invocation.

Suggested collection prompts:

```text
Which plugin and skill were you using?
What did you expect the skill to do?
What did it actually do?
What phrase or event in the session best marks the problem?
Can you paste 20-80 relevant lines after redacting secrets and private names?
```

For local searches, suggest that the user run their own narrow searches such
as:

```bash
rg -n "autorun|lucid|my-ai-kit|MCP|workplan|expected phrase" ~/.codex ~/.claude
```

Tell the user to inspect and redact the results before sharing. Do not run
that command yourself unless they explicitly provide consent and scope.

## Analysis Workflow

After Gate 1 and evidence receipt:

1. Identify the smallest concrete behavior mismatch.
2. Separate product bug, skill instruction bug, docs gap, UX friction, runtime
   limitation, and user expectation mismatch.
3. Extract a short expected-versus-actual statement.
4. Build a reproduction timeline from the user's evidence.
5. Note whether the issue is specific to one runtime or likely cross-runtime.
6. Identify likely acceptance criteria.
7. Prepare labels and issue body.

Avoid overclaiming. If evidence is insufficient, mark uncertainty explicitly
and ask for one targeted missing detail.

## Issue Draft Format

Use this structure:

```markdown
## Summary

<One concise paragraph.>

## Affected Area

- Plugin:
- Skill:
- Runtime:
- Version or install source:

## Expected Behavior

<What the user reasonably expected.>

## Actual Behavior

<What happened instead.>

## Evidence Summary

<Summarized evidence with redactions. Include only short quotes if needed.>

## Reproduction / Timeline

1. <Step or observed moment>
2. <Step or observed moment>
3. <Step or observed moment>

## Impact

<Why this matters: extra turns, confusing decision point, broken fallback, lost
trust, manual cleanup, etc.>

## Suspected Cause

<Optional. Mark as hypothesis if uncertain.>

## Suggested Acceptance Criteria

- <Observable fix or behavior>
- <Regression check, doc update, or prompt rule>

## Privacy Note

This issue was drafted from user-provided, redacted session evidence. Raw
session logs are not included.
```

## Label Suggestions

Suggest labels without assuming they already exist:

- `plugin:<plugin-name>`
- `skill:<skill-name>`
- `runtime:claude` or `runtime:codex`
- `dogfood`
- one of `bug`, `ux`, `docs`, `enhancement`, or `needs-triage`

## GitHub Creation

Default target for public users:

```text
97Wobbler/my-ai-kit
```

Maintainers may choose:

```text
97Wobbler/my-ai-kit-dev
```

Before using any GitHub action or command, show the final title, body, labels,
and target repository. Ask for explicit publication approval.

If approved and a GitHub-capable tool is available, create the issue. If issue
creation fails, report the error and preserve the final draft.

## Completion Criteria

The skill is complete when one of these is true:

- a privacy-reviewed issue draft is delivered;
- the user explicitly approved publication and the issue was created;
- the user chose to stop before sharing evidence or before publication.

## Runtime Overrides

In Claude Code, plugin skills are invoked with the plugin namespace, for example `/my-ai-kit-feedback:my-ai-kit-feedback`.
Do not read `~/.claude/`, project transcripts, or any local session files unless the user explicitly provides exact paths or pasted excerpts for this invocation.
If the user approves issue creation, prefer preparing the final issue text first, then use the available GitHub workflow or `gh issue create` only after explicit final approval.
