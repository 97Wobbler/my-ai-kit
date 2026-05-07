---
name: "skill-forge-spec"
description: "Create runtime-neutral SSOT skill specs for Claude Code and Codex CLI. Use when a user wants to design a cross-runtime skill, convert an existing skill idea into a shared spec, or avoid maintaining separate Claude/Codex skill prompts by hand."
---

# Skill Forge Spec

This skill was compiled from a Skill Forge runtime-neutral spec for the
Codex CLI runtime.

Source spec: `plugins/skill-forge/specs/skill-forge-spec.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- Ask clarification questions sparingly; `request_user_input` is Plan Mode only.
- For manual file edits, use `apply_patch` and preserve unrelated user changes.
- Run the relevant validation checks before reporting completion.

Use this skill to create the source-of-truth spec for a cross-runtime skill.
The output is a Markdown file with YAML frontmatter that can be compiled later
by `skill-forge-compile`.

Skill Forge treats compilation as scaffold plus guardrail. The generated
runtime skills should share one neutral behavior contract, while environment
differences stay explicit in runtime overrides.

## Workflow

1. Identify the intended skill behavior, trigger conditions, target users, and
   expected outputs.
2. Separate common behavior from runtime mechanics:
   - common behavior belongs in the Markdown body;
   - environment-specific mechanics belong in `runtime_overrides`.
3. Translate runtime-specific tool needs into abstract capabilities.
4. Add `outputs` paths when generated files should be written or checked for
   drift.
5. Keep runtime-specific tool names out of the neutral workflow.
6. Validate the draft against `references/spec-format.md`.

## Capability Mapping

Use these abstract capability names in frontmatter:

- `user_questions`: whether the skill must ask blocking questions.
- `file_edits`: whether the skill may edit files.
- `subagents`: whether the skill may delegate parallel work.
- `plan_mode`: whether planning-only behavior is required.
- `network`: whether external facts may be needed.
- `validation`: whether the skill must run checks before completion.

## Authoring Rules

- The spec body should describe product behavior once and will be copied
  unchanged into generated runtime skills.
- Put runtime-specific tool names and invocation details in
  `runtime_overrides`, not the neutral body.
- If the skill requires clarification, set `user_questions: required`.
- If Codex is a target and user questions are required, add a Codex runtime
  override that mentions Plan Mode and Default mode behavior.
- Do not expect the compiler to infer tool calls, reorder workflow steps, or
  rewrite natural-language procedures for each runtime.
- Prefer a small, explicit MVP spec over a broad speculative schema.

## Output Contract

Generated runtime skills should be reviewed by a human. If the generated output
needs manual correction, copy the correction back into the source spec,
capability mapping, runtime override, or template before treating the output as
current.

## References

- Read `references/spec-format.md` for the exact frontmatter shape.
- Read `references/runtime-capabilities.md` when choosing capability values.

## Runtime Overrides

Ask clarification questions sparingly. In Plan Mode, structured user input is available; in Default mode, ask concise direct questions and wait.
