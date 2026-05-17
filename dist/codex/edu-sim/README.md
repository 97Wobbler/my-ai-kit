# Edu Sim

`edu-sim` runs a fixed pool of 30 Korean teacher personas against
an edutech proposal and synthesizes a Markdown report focused on surprises,
minority reactions, and blind spots.

It is not a statistical market-research simulator. The persona pool is
deliberately exhaustive for every run so unusual reactions are not lost through
sampling.

## Skill

- Claude Code: `/edu-sim:edu-sim`
- Codex CLI: `$edu-sim`

Example prompt:

```text
페르소나 시뮬레이션 돌려줘:
학부모 앱에 학생별 AI 학습 리포트를 매주 자동 공유하는 기능을 검토 중이야.
```

## Runtime Files

```text
personas.yaml
prompts/persona_response.tmpl
prompts/synthesis.tmpl
scripts/run.sh
scripts/synthesize.sh
scripts/lib/
```

Each run writes isolated output under:

```text
runs/{ISO8601_timestamp}_{slug}/
```

Key outputs:

- `input.md`: original user input
- `responses/P*.json`: raw persona responses
- `report.md`: synthesized report
- `errors.log`: stderr and retry details
- `auth_status.log`: Claude auth/billing path check

## Requirements

- Claude Code CLI on `PATH`
- authenticated `claude -p` access
- Python 3
- PyYAML

If PyYAML is missing:

```bash
python3 -m pip install PyYAML
```

To reduce rate-limit pressure:

```bash
MAX_CONCURRENCY=1 bash scripts/run.sh "$run_dir"
```

## Persona Pool Changes

`personas.yaml` is versioned source data. Do not reuse persona IDs. If a
persona is retired, leave the ID as a gap and add a new ID for replacement.

### Change History

- 2026-05-13: Initial 30-persona pool added from `temp/personas.yaml`.
