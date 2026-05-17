---
name: "edu-sim"
description: "Run a Korean edutech teacher persona simulation. Use when the user asks to simulate teacher reactions, run a persona simulation, collect 30 Korean teacher persona opinions, find blind spots in an edutech policy/product/business proposal, or says \"페르소나 시뮬레이션 돌려줘\", \"교사들이 어떻게 반응할지 시뮬레이션\", or \"30명 교사 의견 받아줘\"."
---

# Edu Sim

This skill was compiled from a Skill Forge runtime-neutral spec for the
Codex CLI runtime.

Source spec: private Skill Forge source (not included in distribution): `edu-sim.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- Use `request_user_input` only in Plan Mode. In Default mode, ask a concise direct question and wait.
- For manual file edits, use `apply_patch` and preserve unrelated user changes.
- Run the relevant validation checks before reporting completion.

## Purpose

Use this skill to test an edutech policy, product feature, business strategy, or experiment against a fixed pool of 30 Korean teacher personas. The goal is not statistical representation or majority voting. The goal is to surface unexpected reactions, minority concerns, and decision blind spots.

The skill is installed as a plugin. Runtime assets live in the installed plugin root:

```text
personas.yaml
prompts/
scripts/
```

Mutable run output belongs under the plugin root's `runs/` directory unless the user explicitly asks for a different output location.

## Inputs

Accept a free-form Korean text or Markdown proposal. Preserve the user's simulation target verbatim:

- Do not summarize it.
- Do not rewrite it.
- Do not normalize business terms.
- Do not add assumptions that were not in the input.

If the user only asks to start the simulation but does not provide a target, ask for the target text before running scripts.

## Run Directory

Create one isolated run directory:

```text
runs/{ISO8601_timestamp}_{slug}/
```

Use the plugin root as the base directory. Build `slug` from the first 30 characters of the input by replacing characters outside Korean letters, ASCII letters, and digits with `-`. Store the exact input in:

```text
<run_dir>/input.md
```

If creating the directory manually is inconvenient, use:

```bash
python3 scripts/lib/persona_tool.py slug <run_dir>/input.md
```

## Workflow

1. Resolve the plugin root by walking upward from this `SKILL.md` until you find `personas.yaml`, `prompts/`, and `scripts/`.
2. Create `runs/{ISO8601_timestamp}_{slug}/` and write the user's original simulation target to `input.md`.
3. Run `bash scripts/lib/check_auth.sh "$run_dir"`.
4. Show the auth/billing warning output to the user if it indicates `ANTHROPIC_API_KEY` or an unexpected billing path.
5. If the billing path may be different from the user's intent, stop and ask whether to proceed before running the 30 calls.
6. Run `bash scripts/run.sh "$run_dir"`.
7. Give one or two short progress updates while the run is active. The script prints completion counts such as `20/30 complete: P20`.
8. Run `bash scripts/synthesize.sh "$run_dir"`.
9. Present `<run_dir>/report.md` to the user as the result file.
10. End with the run directory path only briefly. Do not re-summarize the report in chat.

## Runtime Behavior

`scripts/run.sh` calls `claude -p` once per persona with:

- `--append-system-prompt` from the persona's `system_prompt`
- `--model claude-sonnet-4-6`
- `--output-format json`
- `--max-turns 1`
- `--disallowedTools "*"`

Do not add `--bare` to these scripted `claude -p` calls. The calls must preserve
the same Claude Code subscription login path that passed the auth preflight.

Default concurrency is 3. To reduce rate-limit pressure, rerun with:

```bash
MAX_CONCURRENCY=1 bash scripts/run.sh "$run_dir"
```

`scripts/synthesize.sh` combines:

- the original `input.md`
- `id` plus `metadata` for all personas
- compacted persona responses from `responses/P*.json`

The final report is written to:

```text
<run_dir>/report.md
```

## Error Handling

Single persona failure:

- Retry once.
- On the second failure, continue the run and write:

```json
{"error": true, "persona_id": "P0X", "reason": "<reason>"}
```

Rate limits:

- Wait 60 seconds when stderr looks like HTTP 429 or rate limit text.
- Stop after three consecutive rate-limit failures.
- Preserve already collected response files.

Synthesis failure:

- Retry once.
- If it still fails, tell the user that synthesis failed and point to the preserved `responses/P*.json` files.

## Dependencies

This workflow shells out to the local Claude Code CLI. It expects:

- `claude` available on `PATH`
- authenticated Claude Code access that can run `claude -p`
- Python 3
- PyYAML for reading `personas.yaml`

If PyYAML is missing, install it with:

```bash
python3 -m pip install PyYAML
```

## Output Discipline

- Do not paste all 30 persona responses into chat.
- Do not summarize `report.md` after generation unless the user explicitly asks.
- Treat `report.md` as the primary output.
- Keep `responses/P*.json`, `errors.log`, `auth_status.log`, and `input.md` in the run directory for reproducibility.

## Runtime Overrides

In Codex, plugin skills are invoked through the installed skill name, for example `$edu-sim` or "use edu-sim".
Use `request_user_input` only in Plan Mode. In Default mode, ask a concise direct question only if the billing/auth path is ambiguous or the simulation input is missing.
For manual file edits, use `apply_patch`; for this skill's normal run state, create files under the per-run `runs/` directory only.
