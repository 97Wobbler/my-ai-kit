---
name: "skill-forge-compile"
description: "Validate and compile Skill Forge runtime-neutral specs into Claude Code and Codex CLI SKILL.md files. Use when a user has a Skill Forge spec and wants generated runtime skill implementations."
---

# Skill Forge Compile

This skill was compiled from a Skill Forge runtime-neutral spec for the
Claude Code runtime.

Source spec: private Skill Forge source (not included in distribution): `skill-forge-compile.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- Ask clarification questions only when they materially change the result.
- Follow repository edit instructions and preserve unrelated user changes.
- Run the relevant validation checks before reporting completion.

Use this skill when a runtime-neutral Skill Forge spec already exists and the
user wants Claude Code or Codex CLI skill outputs.

Compilation is scaffold plus guardrail: the compiler copies the neutral
workflow body unchanged, adds runtime capability notes, appends explicit
runtime overrides, and can check generated files for drift. It does not
rewrite natural-language workflow steps into target-specific procedures.

## Workflow

1. Locate the spec file and read `references/spec-format.md` if the format is
   unclear.
2. Run validation:

```bash
python3 plugins/skill-forge/scripts/validate_skill_spec.py <spec>
```

3. Compile requested targets. If the spec declares `outputs`, prefer the
   output paths from the spec:

```bash
python3 plugins/skill-forge/scripts/compile_skill.py <spec> --target all
```

   For one-off output paths, pass `--out` with a single target:

```bash
python3 plugins/skill-forge/scripts/compile_skill.py <spec> --target claude --out <claude-skill-path>/SKILL.md
python3 plugins/skill-forge/scripts/compile_skill.py <spec> --target codex --out <codex-skill-path>/SKILL.md
```

4. Inspect generated output for target-specific correctness.
5. When `outputs` are declared, verify drift before reporting completion:

```bash
python3 plugins/skill-forge/scripts/compile_skill.py <spec> --target all --check
```

6. Run repository-level checks requested by the user or by the repository
   instructions.

## Runtime Rules

- The neutral workflow body is copied as-is; use `runtime_overrides` for
  environment differences instead of expecting semantic rewrites.
- Do not edit generated runtime files by hand unless immediately copying the
  correction back into the SSOT spec or compiler template.
- Generated files are artifacts. Treat the `.skill.md` spec, compiler templates,
  and capability mapping as the durable sources.

## References

- `references/spec-format.md`
- `references/runtime-capabilities.md`

## Runtime Overrides

Follow repository edit instructions when writing compiled skill outputs.
