# Skill Forge Spec Format

Skill Forge specs are Markdown files with YAML frontmatter. They describe skill
behavior once, then compiler targets scaffold runtime-specific `SKILL.md`
files and apply guardrails that prevent accidental drift.

Skill Forge is not a natural-language transpiler. The compiler does not
rewrite the neutral workflow into different runtime procedures. It copies the
neutral body intact, adds runtime capability notes, appends explicit
runtime-specific overrides, and can check whether generated files are stale.

## Required Frontmatter

```yaml
---
name: example-skill
description: "Trigger description used by runtime skill discovery."
targets:
  - claude
  - codex
---
```

## Optional Frontmatter

```yaml
capabilities:
  user_questions: optional
  file_edits: true
  subagents: none
  plan_mode: optional
  network: false
  validation: required
runtime_overrides:
  claude: |
    Use Claude Code native question tools when blocking clarification is needed.
  codex: |
    Use request_user_input only in Plan Mode; otherwise ask concise text questions.
outputs:
  claude: plugins/example/skills/claude/example/SKILL.md
  codex: plugins/example/skills/codex/example/SKILL.md
```

## Body

The Markdown body is the neutral workflow and should be treated as the common
behavior contract. The compiler copies it as-is into each generated skill.

Write the body with abstract capabilities, not target-specific tool names.

Prefer:

- Ask blocking clarification questions when required.
- Update files only after the user confirms the target path.
- Run validation before reporting completion.

Avoid:

- Call `AskUserQuestions`.
- Call `request_user_input`.
- Use Claude Code TaskCreate.
- Use Codex `update_plan`.

Target-specific details belong in `runtime_overrides` or in the compiler's
runtime capability notes.

## Compiler Contract

Compilation is scaffold plus guardrail:

- `name` and `description` become generated skill frontmatter.
- `capabilities` become generated runtime notes.
- the Markdown body is copied unchanged into the `Workflow` section.
- `runtime_overrides.<target>` is copied unchanged into `Runtime Overrides`.
- `outputs.<target>` tells the compiler where to write or check each runtime
  file.

The compiler intentionally does not:

- infer tool calls from workflow prose;
- rewrite workflow steps differently per runtime;
- reorder instructions based on target;
- generate plugin manifests or marketplace entries.

Use runtime overrides for environment differences that require judgment.

## Capability Values

- `user_questions`: `none`, `optional`, or `required`
- `file_edits`: `true` or `false`
- `subagents`: `none`, `optional`, or `required`
- `plan_mode`: `none`, `optional`, or `required`
- `network`: `true` or `false`
- `validation`: `none`, `optional`, or `required`

The MVP validator accepts missing capabilities and fills conservative defaults.

## Commands

Validate a spec:

```bash
python3 plugins/skill-forge/scripts/validate_skill_spec.py <spec>
```

Compile one target to an explicit path:

```bash
python3 plugins/skill-forge/scripts/compile_skill.py <spec> --target codex --out <path>/SKILL.md
```

Compile every declared target using `outputs`:

```bash
python3 plugins/skill-forge/scripts/compile_skill.py <spec> --target all
```

Check generated files for drift without writing:

```bash
python3 plugins/skill-forge/scripts/compile_skill.py <spec> --target all --check
```
