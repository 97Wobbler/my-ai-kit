# Phase 1 Substitution Map

This document is the authoritative plan for the `lenslab → Prism` and
`framework → instrument` substitutions in Phase 1 (T1 → T2 → T3).

T2 uses this as its editing checklist. Any hit not explicitly marked `replace`
is out of scope for Phase 1 (T2 in particular). `rename-in-T3` items are only
touched by T3. `phase2` and `skip` items are not touched at all in Phase 1.

**Scanned ranges:** all tracked `*.md / *.yml / *.yaml / *.json / *.py / *.txt`
files, excluding `library/`, `docs/archive/`, `scripts/prompts/`,
`.batch-state/`, `logs/`, `.git/`, `.claude/` (these are explicitly excluded
by the Phase 1 policy in `docs/phase1-plan.yml`).

**Term substitution rules** (from `docs/phase1-plan.yml § conventions.term_substitution_policy`):

- `lenslab` → `prism` in plugin identifier fields (plugin.json `name`,
  marketplace.json `name`, package / import / URL slugs).
- `lenslab` → `Prism` in user-facing prose and headings.
- `lenslab_batch.py` filename and all references → handled by T3 (not T2).
- `framework` → `instrument` **only** when used as the 5-class umbrella term
  (i.e. as a stand-in for lens / frame / model / stance / heuristic). When
  `framework` refers to a specific named framework (Porter's, Kano, etc.),
  leave it alone.
- Individual framework *slugs* in `catalog.yml` (e.g. `north-star-framework`)
  are part of a specific framework's identifier and are left alone.

## Summary

| Category | lenslab hits | framework hits | Total |
|---|---|---|---|
| replace (T2) | 22 | 33 | 55 |
| rename-in-T3 | 19 | 0 | 19 |
| phase2 | 0 | 3 | 3 |
| skip | 28 | 32 | 60 |
| **Total** | **69** | **68** | **137** |

Breakdown of lenslab hits by file:
- replace (22): plugin.json 3, marketplace.json 2, catalog.yml 1, README.md 12,
  CLASSES.md 2, sync_catalog.py 1, parallel_runner.py 1.
- rename-in-T3 (19): lenslab_batch.py 8, PHASE3_RUN.md 9, parallel_runner.py 1,
  README.md 1.
- skip (28): PHASE3_RUN.md 1, ROADMAP.md 2, phase1-plan.yml 25.

Breakdown of framework hits by file:
- replace (33): plugin.json 2, marketplace.json 1 (with 2 occurrences on one line),
  README.md 17, CLASSES.md 4, SKILL.md 8, parse_consolidation.py 1.
- phase2 (3): product-strategist.yml 2, security-analyst.yml 1.
- skip (32): catalog.yml 16 (slug + path lines for 8 individual frameworks),
  CLASSES.md 5, SKILL.md 1, ROADMAP.md 1, phase1-plan.yml 8, product-strategist.yml 1.

Counts cover only in-scope files after the exclusion rules above are applied.
(The raw `grep -rn 'framework'` result on the repo includes hundreds of hits
under `library/` and `scripts/prompts/` which this map intentionally ignores.)

---

## lenslab hits

### replace (do in T2)

**`.claude-plugin/plugin.json`** — plugin identifier + user-facing strings
- line 2: `"name": "lenslab",` → `"name": "prism",`
- line 9: `"homepage": "https://github.com/97Wobbler/lenslab"` → `"https://github.com/97Wobbler/prism"`
- line 10: `"repository": "https://github.com/97Wobbler/lenslab"` → `"https://github.com/97Wobbler/prism"`

**`.claude-plugin/marketplace.json`** — marketplace identifier
- line 2: `"name": "lenslab",` → `"name": "prism",`
- line 12: `"name": "lenslab",` (plugins[0].name) → `"name": "prism",`

**`catalog.yml`** — header comment only
- line 1: `# lenslab — catalog` → `# Prism — catalog`

**`README.md`** — user-facing prose + identifiers
- line 1: `# lenslab` → `# Prism`
- line 32: `**lenslab treats these frameworks...` → `**Prism treats these instruments...` (note: `frameworks` here is umbrella; see framework-hits replace section)
- line 38: `In v0.1, lenslab called every framework a "lens"...` → `In v0.1, Prism called every instrument a "lens"...`
- line 94: `lenslab is a Claude Code plugin.` → `Prism is a Claude Code plugin.`
- line 95: `(\`/lenslab:create-agent\`)` → `(\`/prism:create-agent\`)`
- line 102: `claude plugin marketplace add 97Wobbler/lenslab` → `... 97Wobbler/prism`
- line 105: `claude plugin install lenslab` → `claude plugin install prism`
- line 112: `git clone https://github.com/97Wobbler/lenslab.git` → `... 97Wobbler/prism.git`
- line 116: `After install, \`/lenslab:create-agent\` should appear...` → `... \`/prism:create-agent\` ...`
- line 120: `### Step 2. Create an agent with \`/lenslab:create-agent\`` → `... \`/prism:create-agent\``
- line 123: `/lenslab:create-agent security ...` → `/prism:create-agent security ...`
- line 311: `The entry point is \`scripts/lenslab_batch.py\`,` → leave file path alone here **OR** update to `scripts/prism_batch.py` **during T3** (see note in rename-in-T3 section). T2 should NOT touch this line.
  - **Classification override:** line 311 is `rename-in-T3`, not `replace`. Listed here for completeness.
- line 329: `## Why "lenslab"` → `## Why "Prism"` (heading)

**`CLASSES.md`** — user-facing prose
- line 1: `# CLASSES — the lenslab 5-class taxonomy` → `# CLASSES — the Prism 5-class taxonomy`
- line 3: `lenslab composes domain-expert analysis agents out of **structured frameworks**,` → `Prism composes domain-expert analysis agents out of **structured instruments**,` (note: `frameworks` here is umbrella; covered in framework replace section)

**`skills/agent-creator/SKILL.md`** — skill prose
- (No `lenslab` literal strings appear — confirmed by grep. This file has
  `framework` hits handled in the framework section below. Listed here for
  completeness so T2 knows it already ships with no `lenslab` literals.)

**`scripts/PHASE3_RUN.md`** — rename identifiers only; historical factual
content about the v0.3 batch run is kept intact. `lenslab_batch` file path
references stay as-is in T2; T3 will rewrite them during the file rename.
- line 17: `cd /path/to/prism` → this is a cwd path placeholder. It refers to the current local checkout directory; the repo directory name on disk is not part of the plugin identifier. **skip** (local path, not a plugin identifier). Classification override below.
- line 18: `python3 scripts/lenslab_batch.py \` → **rename-in-T3** (file path ref)
- line 26: `python3 scripts/lenslab_batch.py ...` → **rename-in-T3**
- line 32: `python3 scripts/lenslab_batch.py --limit 20 ...` → **rename-in-T3**
- line 37: `python3 scripts/lenslab_batch.py --class heuristic ...` → **rename-in-T3**
- line 64: `.batch-state/lenslab-run/items/*.json` → this is a historical state directory name from an actual past run. Keeping it would falsify nothing. However, it is also referenced in `scripts/lenslab_batch.py` as `--output-state` default. Whether to leave or rewrite is a judgment call. **Classification:** `rename-in-T3` (since it co-moves with the batch script's default). T2 does not touch it.
- line 65: `lenslab_batch also...` → **rename-in-T3**
- line 92: `.batch-state/lenslab-run/items/*.json` → **rename-in-T3** (same as line 64)
- line 126: `python3 scripts/lenslab_batch.py --class lens ...` → **rename-in-T3**
- line 134: `.batch-state/lenslab-run/items/<name>.json` → **rename-in-T3**

PHASE3_RUN.md has **no pure lenslab-as-plugin-name prose hits**. Every
`lenslab` literal in it is either the on-disk cwd (skip) or the batch script /
state dir (rename-in-T3). T2 therefore edits 0 lines in this file. This is
deliberate and documented here so T2 does not mistakenly "fix" it.

**`scripts/sync_catalog.py`** — docstring / header comment strings only
(per T2 task description)
- line 52: `# lenslab — catalog` (inside `HEADER_COMMENT` triple-quoted string) → `# Prism — catalog`

**`scripts/parallel_runner.py`** — credit comment (per T2 task description)
- line 8: `# Used in lenslab for batch document generation (Phase 3 — 600 items, haiku 4.5).` → `# Used in Prism for batch document generation (Phase 3 — 600 items, haiku 4.5).`
- line 11: `# Do not modify the core logic; adapt via the calling driver (lenslab_batch.py).` → keep `lenslab_batch.py` in the comment for T2 (this reference is updated by T3 when the file is renamed). **Classification override:** line 11 is `rename-in-T3`.

**`scripts/parse_consolidation.py`** — docstring only (per T2 task description)
- (No `lenslab` literal here. This file's only match was on `framework`.
  Listed for completeness.)

### rename-in-T3 (do in T3, not T2)

**`scripts/lenslab_batch.py`** — the file itself is renamed to
`scripts/prism_batch.py`. All the references below are updated in the same
T3 commit, not in T2.

The batch script's own content hits (which are also `rename-in-T3`):
- line 2: `"""lenslab batch document generator using haiku 4.5 via claude -p.` → `"""Prism batch document generator using haiku 4.5 via claude -p.`
- line 11: `python3 scripts/lenslab_batch.py --dry-run` → `python3 scripts/prism_batch.py --dry-run`
- line 12: `python3 scripts/lenslab_batch.py --limit 5 --workers 1` → `python3 scripts/prism_batch.py --limit 5 --workers 1`
- line 13: `python3 scripts/lenslab_batch.py --workers 5 --batch-size 10` → `python3 scripts/prism_batch.py --workers 5 --batch-size 10`
- line 36: `# 클래스 → 복수형 출력 디렉토리 (lenslab 레이아웃: library/ 하위로 통합됨)` → `# 클래스 → 복수형 출력 디렉토리 (Prism 레이아웃: library/ 하위로 통합됨)`
- line 232: `description="lenslab batch markdown generator (haiku 4.5)"` → `description="Prism batch markdown generator (haiku 4.5)"`
- line 263: `default=str(PROJECT_DIR / ".batch-state" / "lenslab-run"),` → `default=str(PROJECT_DIR / ".batch-state" / "prism-run"),`
- line 284: `print("=== lenslab batch (haiku) ===")` → `print("=== Prism batch (haiku) ===")`

`scripts/PHASE3_RUN.md` references to the script and to `.batch-state/lenslab-run`:
- lines 18, 26, 32, 37, 64, 65, 92, 126, 134 — all updated by T3 when the
  batch-script rename lands. (See the detailed list in the replace section.)

`scripts/parallel_runner.py`:
- line 11: `(lenslab_batch.py)` → `(prism_batch.py)` — updated by T3 alongside the rename.

`README.md`:
- line 311: `The entry point is \`scripts/lenslab_batch.py\`` → updated by T3 to `scripts/prism_batch.py`.

### phase2 (out of Phase 1 scope)

(None for `lenslab`. The `agents/examples/*.yml` files do not contain the
literal string `lenslab`.)

### skip (leave as-is)

**`docs/ROADMAP.md`** — deliberate historical references that explain the
rename to the reader. Rewriting them would delete the explanation.
- line 10: `Renamed from lenslab. Same 657-instrument library across 50 domains.` → keep
- line 15: `Breaking change from lenslab v0.3.0: name, plugin identifier, ...` → keep

**`docs/phase1-plan.yml`** — this is the plan document driving Phase 1 itself.
All of its `lenslab` references describe *the work being done*, not the final
state of the product. Rewriting them in-flight would corrupt the plan.
- lines 2, 7, 9, 10, 14, 27, 30, 51, 55, 61, 64, 76, 79, 82, 85, 90, 91, 99,
  116, 132, 137, 144, 149, 151, 153 → keep all

**`docs/phase1-substitution-map.md`** (this file) — meta-references to the
substitution work; not a user-facing artifact.

**`scripts/PHASE3_RUN.md` line 17** — `cd /path/to/prism`
is the local on-disk checkout path of the author. The repo directory name on
disk is not a plugin identifier; changing the literal would silently break
the instructions for the author and all existing checkouts. Keep as-is.

---

## framework hits

### replace (do in T2)

Each entry below is marked umbrella → the `framework` token is standing in
for "one of the 5 classes (lens / frame / model / stance / heuristic)" and
not for a specific named framework.

**`.claude-plugin/plugin.json`**
- line 4: `"description": "Create domain-expert analysis agents by composing structured frameworks — lenses, frames, models, stances, and heuristics — instead of vague persona prompts."` → `"... composing structured instruments — lenses, frames, models, stances, and heuristics — ..."`. Umbrella: the dash-introduced list IS the 5-class enumeration.
- line 16: `"frameworks",` (keyword) → `"instruments",`. Umbrella: keyword is the product's top-level vocabulary.

**`.claude-plugin/marketplace.json`**
- line 7: `"description": "Frameworks over personas — ... composing structured analytical frameworks (lenses, frames, models, stances, heuristics) ..."` → `"Instruments over personas — ... composing structured analytical instruments (lenses, frames, models, stances, heuristics) ..."`. Two umbrella uses on the same line (the "Frameworks over personas" slogan and the parenthetical enumeration).

**`README.md`**
- line 3: `**Frameworks over personas.**` → `**Instruments over personas.**` (slogan, umbrella)
- line 6: `frameworks experts actually use.` → `instruments experts actually use.` (umbrella — the whole paragraph is setting up the 5 classes)
- line 8: `657 framework files` → `657 instrument files` (umbrella — counts across all 5 classes)
- line 32: `**lenslab treats these frameworks as first-class, reusable assets.**` → `**Prism treats these instruments as first-class, reusable assets.**` (umbrella)
- line 33: `build agents by composing frameworks, not by writing adjective-heavy` → `... composing instruments, ...` (umbrella)
- line 38: `In v0.1, lenslab called every framework a "lens"` → `In v0.1, Prism called every instrument a "lens"` (umbrella — explicitly generalizes over all class members)
- line 39: `Real frameworks come in different shapes, and flattening them all into` → `Real instruments come in different shapes, ...` (umbrella)
- line 54: `confidence evaluation. If any of the four is missing, the framework` → `... the instrument` (umbrella — refers to "whatever is being classified into one of the 5 classes")
- line 78: `- **Frameworks > personas.**` → `- **Instruments > personas.**` (umbrella slogan)
- line 79: `framework files. The persona is a one-line framing; the frameworks do` → `instrument files. The persona is a one-line framing; the instruments do` (umbrella; 2 hits on one line)
- line 81: `- **Frameworks are reusable.**` → `- **Instruments are reusable.**` (umbrella)
- line 223: `The v0.3 library ships with **657 framework files** across 5 classes` → `**657 instrument files** across 5 classes` (umbrella — the "5 classes" right after makes this unambiguous)
- line 284: `To add a single new framework file by hand:` → `To add a single new instrument file by hand:` (umbrella)
- line 286: `1. **Identify the framework.** It must be a real method used by` → `1. **Identify the instrument.** ...` (umbrella; describing any of the 5 classes)
- line 308: `### Adding many frameworks at once` → `### Adding many instruments at once` (umbrella section heading)
- line 310: `To add frameworks in bulk, see \`scripts/PHASE3_RUN.md\`` → `To add instruments in bulk, ...` (umbrella)
- line 323: `Contributions of non-English-language and domain-local frameworks are` → `... domain-local instruments are` (umbrella — contributions apply to all classes)
- line 325: `is Korea-specific by design, and similar local frameworks exist for` → `... similar local instruments exist for` (umbrella)

**`CLASSES.md`**
- line 4: `frameworks**, not persona prompts. But not every useful framework is the` → `instruments**, ... But not every useful instrument is the` (umbrella — explicitly sets up the 5-class distinction)
- line 6: `framework into exactly one of five classes: **lens, frame, model, stance,` → `instrument into exactly one of five classes: ...` (umbrella — the sentence literally enumerates the 5 classes)
- line 22: `enough that someone unfamiliar with the framework can run them step by` → `... unfamiliar with the lens can run them ...`. **Context:** this line is **inside the strict definition of a lens** (criterion #2). It is referring to the specific lens being documented, not the umbrella. **Classification override: skip.**
- line 39: `Start from the source framework, not from what you want to build.` → `Start from the source instrument, ...` (umbrella — describing the classification decision process)
- line 41: `| Question about the source framework | Class |` → `| Question about the source instrument | Class |` (umbrella — table column that routes to one of the 5 classes)
- line 77: `name: <framework name>` → **skip**. This is inside a file-format example block. `<framework name>` here is a placeholder for an individual framework's name (e.g. "STRIDE"). Not umbrella.
- line 84: `# <framework name>` → **skip** (same reason as line 77)
- line 225: `**What it is:** An interpretive position or critical framework. Stances do` → **skip**. Here `critical framework` is a domain term of art in literary/critical theory meaning "a framework for criticism"; it refers to an individual framework, not the umbrella.
- line 420: `without prior knowledge of the framework; output format includes` → **skip**. Inside the "Checklist before submitting a new item" → "For a lens: Analytical Procedure is concrete enough to execute without prior knowledge of the framework". Same as line 22: refers to the specific lens being submitted. Not umbrella.

**`skills/agent-creator/SKILL.md`**
- line 8: `You are building a **framework-composing analysis agent** — a lightweight` → `You are building a **instrument-composing analysis agent** — ...` (umbrella: composing from all 5 classes)
- line 10: `frameworks, not by pretending to be a persona.` → `instruments, not by pretending to be a persona.` (umbrella)
- line 15: `reasoning depth. Structured frameworks (STRIDE, OWASP Top 10, Cynefin,` → `Structured instruments (STRIDE, OWASP Top 10, Cynefin, ...)` (umbrella — the list crosses all 5 classes: STRIDE is a lens, Cynefin is a frame, Prospect Theory is a model, etc.)
- line 20: `**v0.2 introduces 5 classes of framework.** Not every useful framework is` → `**v0.2 introduces 5 classes of instrument.** Not every useful instrument is` (umbrella — explicit "5 classes of X"; 2 hits on one line)
- line 22: `each framework you add, compose them into a minimal agent config, and` → `each instrument you add, ...` (umbrella)
- line 38: `\`critical-read\` step to surface what other frameworks miss. E.g.,` → `... what other instruments miss.` (umbrella)
- line 97: `- The source framework has a procedure, an output template, and a` → `- The source instrument has a procedure, ...` (umbrella — this is the decision rule for which class to pick, so the subject is any-class)
- line 121: `concrete enough that someone unfamiliar with the framework can` → **skip** (same as CLASSES.md line 22/420: inside a "For a lens:" bullet, refers to the specific lens)
- line 299: `- Don't write persona prompts full of adjectives. The frameworks do` → `... The instruments do` (umbrella)

**`scripts/parse_consolidation.py`**
- line 6: `pending framework. Also prints stats to stdout.` → `pending instrument. ...` (umbrella — this script writes one JSONL record per item across all 5 classes).

### phase2 (out of Phase 1 scope)

**`agents/examples/product-strategist.yml`** — the entire file is rewritten
as `docs/cookbook/product-strategist.md` in Phase 2.
- line 16: `- path: library/lenses/product-management/north-star-framework.md` — individual framework slug; would be `skip` even if in scope.
- line 115: `tensions between frameworks (e.g., Kano says it's a delighter` — umbrella, but `phase2`.
- line 164: `<explicit disagreements between frameworks>` — umbrella, `phase2`.

**`agents/examples/security-analyst.yml`** — same Phase-2 rewrite.
- line 69: `Call out explicit tensions between frameworks (e.g., STRIDE` — umbrella, `phase2`.

### skip (leave as-is)

**`catalog.yml`** — all `framework` hits are parts of individual item slugs
or paths referring to a specific framework's library file. These are
NOT umbrella uses.
- line 72, 76: `space-framework` (the SPACE framework, an individual agile lens)
- line 116, 120: `eval-harness-frameworks` (individual AI lens)
- line 424, 428: `fermentation-frameworks` (individual cooking lens)
- line 656, 660: `supply-demand-framework` (individual economics lens)
- line 1889, 1893: `north-star-framework` (individual PM lens)
- line 2921, 2924: `axial-age-framework` (individual theology frame)
- line 2933, 2936: `theodicy-frameworks` (individual theology frame)
- line 3987, 3990: `kuhns-paradigm-framework` (individual meta-science stance)

**`CLASSES.md` lines 22, 77, 84, 225, 420** — see replace section for the
per-line rationale. These are either (a) file-format template placeholders
for an individual framework's name, or (b) references to "the framework"
inside a lens-specific bullet where "the framework" means the specific lens
being documented.

**`skills/agent-creator/SKILL.md` line 121** — same reason as CLASSES.md 22/420.

**`docs/ROADMAP.md` line 29** — `framework name, domain` refers to the name
of a *specific* framework the user is creating, not the umbrella term. Skip.

**`docs/phase1-plan.yml`** — all `framework` hits describe the substitution
policy itself (e.g. "Replace only when used as the 5-class umbrella term").
Rewriting them would erase the policy being followed. Skip all.
- lines 8, 34, 35, 36, 51, 55, 61, 64 → keep

---

## Notes

### Ambiguities and edge cases

1. **CLASSES.md line 22 / line 420, SKILL.md line 121** — all three use the
   construction "someone unfamiliar with the framework can run them step by
   step." Taken in isolation this looks umbrella, but each is inside a
   lens-specific context (the lens definition or a "For a lens:" bullet).
   They describe what it means for a *particular* lens's Analytical
   Procedure to be concrete. Classified as **skip** on that basis. If T2
   disagrees, the safe alternative is to swap `framework` → `lens` (which
   is the specific class being referenced), NOT `framework` → `instrument`.
   But the map treats them as skip for simplicity.

2. **CLASSES.md line 225** — "critical framework" is a fixed phrase from
   literary/critical theory. A "critical framework" is a specific kind of
   interpretive apparatus, not the 5-class umbrella. Skip.

3. **CLASSES.md lines 77, 84** — these are inside a file-format template
   (`name: <framework name>` / `# <framework name>`). The angle-bracketed
   placeholder is filled in by the individual framework's actual name
   (e.g. "STRIDE", "Porter's Five Forces"). They are not umbrella; skip.

4. **PHASE3_RUN.md line 17** — `cd /Users/.../lenslab` is the on-disk
   checkout path of the plan author. The repo directory name is not the
   plugin identifier; local clones can be at any path. Skip.

5. **PHASE3_RUN.md is otherwise entirely `rename-in-T3` or `skip`.** T2
   touches zero lines in this file. This is intentional and documented so
   T2 does not "helpfully" update `lenslab_batch.py` path references in it
   ahead of the rename.

6. **agents/examples/*.yml** — the plan (`phase1-plan.yml` scope.out) says
   these files become `docs/cookbook/*.md` in Phase 2. None of the three
   framework hits in them (product-strategist.yml line 115, 164;
   security-analyst.yml line 69) are rewritten in Phase 1. They are
   umbrella uses that would qualify for replace under the policy, but the
   whole file is being rewritten in Phase 2, so Phase 1 does not touch it.

7. **`docs/ROADMAP.md` lines 10 and 15 (lenslab skip)** — these say
   "Renamed from lenslab" and "Breaking change from lenslab v0.3.0". They
   are intentional historical markers explaining the rename. The whole
   point of the ROADMAP line is the word `lenslab`; removing it would
   erase the explanation.

8. **`.claude/agents/finance-analyst.yml`** — this file has `framework`
   hits (line 160) but is under `.claude/` which is excluded by the scan
   policy. It is a user-scoped agent config, not a plugin artifact. Not
   in scope for Phase 1.

9. **`docs/phase1-plan.yml` itself** — the plan document describing the
   rename work. Every `lenslab` and `framework` hit in it describes the
   work-in-progress state, not the end state. Rewriting it in T2 would
   corrupt the instructions the tasks are still reading. Skip all.

10. **Git log / commit messages** — several past commits contain `lenslab`
    in their messages (e.g. "v0.3: expand installation and usage section
    in README" is actually fine, but earlier ones reference `lenslab`).
    Commit messages are immutable history and are not in scope for any
    task in Phase 1.

### Files not touched at all in Phase 1

- `library/**` (all 657 instrument files)
- `scripts/prompts/*.txt` (rewritten in Phase 2)
- `docs/archive/CONSOLIDATION.md`
- `.claude/**` (user-scoped, not plugin-scoped)
- `.batch-state/**`, `logs/**`, `data/**`
- `docs/phase1-plan.yml`, `docs/phase1-substitution-map.md` (this file)
- `docs/ROADMAP.md` — already uses `Prism` / `instrument`; only the two
  historical lenslab references remain and they are intentional.
- `agents/examples/*.yml` (rewritten in Phase 2)

### Files that T2 edits (derived from the replace section above)

1. `.claude-plugin/plugin.json`
2. `.claude-plugin/marketplace.json`
3. `catalog.yml` (header comment only)
4. `README.md`
5. `CLASSES.md`
6. `skills/agent-creator/SKILL.md`
7. `scripts/sync_catalog.py` (HEADER_COMMENT only)
8. `scripts/parallel_runner.py` (credit comment at line 8 only — line 11 is T3)
9. `scripts/parse_consolidation.py` (docstring line 6 only)

T2 must NOT touch: `scripts/PHASE3_RUN.md`, `scripts/lenslab_batch.py`.

### Files that T3 edits (the rename commit)

1. `scripts/lenslab_batch.py` → renamed to `scripts/prism_batch.py` + all
   content hits above.
2. `scripts/PHASE3_RUN.md` — all `lenslab_batch` and `.batch-state/lenslab-run`
   references.
3. `scripts/parallel_runner.py` line 11 `(lenslab_batch.py)` → `(prism_batch.py)`.
4. `README.md` line 311 `scripts/lenslab_batch.py` → `scripts/prism_batch.py`.

T3 also verifies `python3 -m py_compile scripts/prism_batch.py` and no
importer references to `lenslab_batch` remain (per the T3 task description
in `docs/phase1-plan.yml`).
