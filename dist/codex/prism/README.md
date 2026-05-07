# Prism

**Instruments over personas.** A Claude Code plugin for building
domain-expert analysis agents that actually reason like experts — not by
pretending to be one, but by loading the structured analytical
instruments experts actually use.

v0.5.6 ships a library of **742 instrument files** across 5 classes and 62
domains, all indexed by a single `catalog.yml` triage file.

## The problem with persona prompts

Telling an LLM "You are a senior security engineer" changes its tone but
not its reasoning depth. It will write more assertive sentences and
sprinkle in domain vocabulary, but the underlying analysis remains
ad-hoc. Ask it to review an API and you'll get a confident-sounding list
of suggestions that misses the same things an untrained reviewer would
miss.

Real security engineers don't run on vibes. They walk checklists: STRIDE
for threat modeling, OWASP Top 10 for API review, CVSS for severity.
These checklists are the reason their analysis is deep — they force
coverage, they surface blind spots, and they produce findings that
compare across reviews.

The same is true in every domain. Curriculum reviewers use Bloom's
Taxonomy and achievement-standard alignment. Strategists use Porter's
Five Forces and pre-mortems. Decision scientists use Prospect Theory and
Occam's Razor. Cultural critics read through Marxist and Foucauldian
stances.

**Prism treats these instruments as first-class, reusable assets.** You
build agents by composing instruments, not by writing adjective-heavy
persona prompts.

## The 5 classes

In v0.1, Prism called every instrument a "lens" — which was imprecise.
Real instruments come in different shapes, and flattening them all into
one template loses information. v0.2 introduced an explicit 5-class
taxonomy; v0.3 scales it out to 657 files. See `CLASSES.md` for the full
reference.

| Class | What it is | Examples |
|---|---|---|
| **Lens (렌즈)** | Structured executable analytical procedure with input, steps, output format, and confidence signal. | STRIDE, OWASP API Top 10, CVSS, Bloom's Taxonomy, First Principles, Pre-mortem |
| **Frame (분류 프레임)** | Taxonomy or classification matrix — categories with discriminating criteria, no built-in procedure. | Cynefin, Kano Model, BCG Matrix, Webb's DOK, MoSCoW |
| **Model (이론 모델)** | Descriptive or predictive theoretical model — variables, relationships, predictions. | Porter's Five Forces, Prospect Theory, Nash Equilibrium, Lotka-Volterra |
| **Stance (비판적 관점)** | Interpretive position — commitments about what is worth looking for. | Marxist criticism, Foucauldian power/knowledge, Deconstruction, Bourdieu's Habitus |
| **Heuristic (원리 / 격언)** | Single rule of thumb — too small to be a lens, used as a check. | Occam's Razor, Hanlon's Razor, Chesterton's Fence, Hickam's Dictum |

The **strict definition of a lens** is specific: it must have a defined
input type, an executable procedure, a structured output format, AND a
confidence evaluation. If any of the four is missing, the instrument
belongs to one of the four sister classes.

## Agent workflow

Agents run a 7-step pipeline. Simple agents use only steps 1, 3, and 7;
richer agents enable the optional middle steps as needed.

```
1. Triage          — read catalog.yml; select items of any class
2. Classify        — apply FRAMES to sort the input               [optional]
3. Analyze         — apply LENSES in sequence                     [core]
4. Model-interpret — instantiate MODELS on input or findings      [optional]
5. Critical-read   — apply STANCES to surface hidden structures   [optional]
6. Sanity-gate     — run HEURISTIC bundles as final checks        [optional]
7. Synthesize      — cross-check across all items, prioritize
```

Each class maps to exactly one workflow step. The agent config declares
which items to load and what `usage` tag each has (`always`,
`when-relevant`, `on-request`).

## Core ideas

- **Instruments > personas.** An agent's analytical depth lives in the
  instrument files. The persona is a one-line framing; the instruments do
  the work.
- **Instruments are reusable.** Once written, the same `stride.md`
  powers a security-reviewer agent, a DevSecOps pipeline agent, and a
  threat-modeling workshop facilitator.
- **Catalog first, load on demand.** Every item lives in `catalog.yml`
  at the repo root as a triage index. Agents read the catalog first,
  select what applies, and only then load the full files. This keeps
  context small.
- **Agents stay thin.** An agent config is ~40 lines: a one-sentence
  persona, per-class lists of item references with usage tags, and the
  workflow steps the agent actually uses.

## Installation and usage

Prism is a Claude Code plugin. It also includes an initial Codex Plugin
manifest for parallel Codex support. It ships four skills
(`search`, a proactive recommender that should be consulted
whenever you are about to build an agent or skill; `fetch`, which
prepares selected instruments in a form ready to hand off to a
sub-agent; and `/prism`, the user-facing router for explaining Prism
and creating new instruments via an interview; and `debate`, an
instrumented multi-perspective orchestration skill) and the `library/` +
`catalog.yml` pair that the catalog skills consume.

### Step 1. Install the plugin

```bash
# Register the marketplace entry
claude plugin marketplace add 97Wobbler/prism

# Install the plugin
claude plugin install prism
```

Or clone and reference locally if you want to hack on the library or
the skill:

```bash
git clone https://github.com/97Wobbler/prism.git
# Then follow your plugin loader's instructions for local plugins.
```

After install, the `search`, `fetch`, `prism`, and `debate` skills should
appear in Claude Code's skill list and the 742 files under `library/`
are reachable via `catalog.yml`.

For Codex, register the repository as a marketplace:

```bash
codex plugin marketplace add 97Wobbler/prism@v0.5.6
```

Then install and enable the plugin through the Codex plugin directory:

```text
codex
/plugins
```

Choose the Prism marketplace, open the Prism plugin, select
`Install plugin`, then start a new thread. `marketplace add` only
registers the marketplace source; it does not by itself install the
plugin bundle.

For local testing, use the repository path instead:

```bash
codex plugin marketplace add /path/to/prism
```

The repository exposes `.agents/plugins/marketplace.json` and
`.codex-plugin/plugin.json` at the repository root, so Codex installs the
same `skills/`, `library/`, and `catalog.yml` that Claude Code uses. This
is an initial compatibility layer: some skill prose still references
Claude Code concepts such as `.claude` storage or native `/agents` flows
and should be adapted in follow-up patches.

### Step 2. Explore the catalog and compose an agent

Whenever you are about to build an agent or skill, consult the
`search` skill first — it is a proactive recommender, not just a
lookup tool, and it will surface instruments from the 742-file library
that match your domain before you write any prompt. It reads
`catalog.yml` as a triage index and returns a grouped-by-class view
filtered by your query. Once you have picked the instruments you need,
use `fetch` to prepare them in a form that can be handed off directly
to a sub-agent. Then open Claude Code's native `/agents` flow and
build an agent that references the `library/` paths you picked,
optionally following a recipe in `docs/cookbook/` (see below).

A typical two-step workflow looks like this:

```
1. /prism search security lens   — browse security-related lenses
2. /prism fetch stride owasp-top10 — prepare selected instruments for a sub-agent
```

If the catalog is missing an instrument you need, invoke `/prism
<framework name>`: the prism skill runs an interview, classifies the
source into one of the 5 classes, LLM-generates the body, and saves it
to the global (`~/.claude/prism/library/`) or project
(`./.claude/prism/library/`) layer. The bundled `library/` layer is
read-only.

```bash
/prism                 # overview — what Prism is and how to use it
/prism CVSS            # specific framework → direct creation
/prism 칸반 방식        # Korean input works; ambiguous → short interview
/prism help            # quick reference
```

### Step 3. Run the agent on a real artifact

Open a new Claude Code session in the project where the config was
written and point Claude at the artifact you want analyzed:

```
> Use .claude/agents/security-analyst.yml to review docs/api-spec.yaml.
```

The agent walks its configured workflow steps — for `security-analyst`
that means triage -> classify (Cynefin) -> analyze (STRIDE, OWASP API
Top 10, CVSS) -> sanity-gate (heuristics bundle) -> synthesize — and
emits findings grouped by root cause, each tagged with a confidence
level (`high` / `medium` / `low`) and, where CVSS applies, a severity
score. See the `output_format` block at the bottom of each example yml
for the exact shape.

### Composition recipes

`docs/cookbook/` contains five composition recipes — narrative
walkthroughs explaining how to combine Prism instruments for a given
persona. These are not executable agent configs; they are the reasoning
behind a composition, meant to be read before you build an agent in
Claude Code's native `/agents` flow.

- **[docs/cookbook/security-analyst.md](docs/cookbook/security-analyst.md)** —
  STRIDE + OWASP API Top 10 + CVSS as always lenses, rumsfeld-matrix as
  a when-relevant meta lens, Cynefin as a when-relevant triage frame,
  and the general heuristics bundle as a sanity gate.
- **[docs/cookbook/curriculum-reviewer.md](docs/cookbook/curriculum-reviewer.md)** —
  Achievement Standard Alignment + Bloom's Taxonomy as always lenses,
  Cognitive Load Theory as when-relevant, Cynefin as a when-relevant
  classification frame, and the general heuristics bundle as a sanity
  gate.
- **[docs/cookbook/product-strategist.md](docs/cookbook/product-strategist.md)** —
  strategy lenses with Porter's Five Forces as the model-interpret step.
- **[docs/cookbook/film-critic.md](docs/cookbook/film-critic.md)** —
  film-theory lenses plus stances for the critical-read step.
- **[docs/cookbook/critical-decomposer.md](docs/cookbook/critical-decomposer.md)** —
  multi-layer-reading + conceptual-analysis + presupposition-analysis +
  toulmin-argument-model as always lenses, analytic-critique as the
  always stance, and general + philosophy heuristic bundles as a sanity
  gate. Demonstrates the "instruments > personas" thesis by decomposing
  a monolithic 5-phase critical analysis system prompt into reusable
  catalog citizens.

Each recipe explains *why* its instruments were composed the way they
were — the value the source YAML could not carry. To turn a recipe into
a running agent, open a Claude Code session and use the native `/agents`
creation flow, referencing the instrument paths listed in the recipe.

### Browsing the catalog

Before building or modifying an agent, it helps to see what's available.
The catalog is a single YAML file at the repo root; there are two common
ways to inspect it:

```bash
# Counts by class and a top-20 domain breakdown
python3 scripts/sync_catalog.py --stats
```

```
Total: 742 items

By class:
  lens: 327
  frame: 106
  model: 139
  stance: 80
  heuristic: 90

By domain (top 20):
  philosophy: 25
  agile: 24
  economics: 22
  general: 22
  ...
```

For everything else, open `catalog.yml` directly and scroll — each
entry has a slug, a one-line summary (often Korean, since the library
is bilingual), and the `library/` path the agent config will reference.

## Included items

The library ships with **742 instrument files** across 5 classes and
62 domains. The v0.2 plugin shipped with 18 hand-written files; the jump
to 657 (v0.3) was made possible by a class-specific batch generation
pipeline that runs Haiku 4.5 in parallel against a curated seed catalog
(see `scripts/PHASE3_RUN.md`), and subsequent releases have grown the
catalog through contributor batches and hand-authored instruments.

Use `catalog.yml` as the single triage index — the `search` skill
reads it first and only loads individual files when the domain
matches.

### By class

| Class | Count | Example entries |
|---|---|---|
| Lens | 327 | `stride`, `first-principles`, `pre-mortem`, `swot`, `multi-layer-reading`, `conceptual-analysis` |
| Frame | 106 | `cynefin`, `kano-model`, `2-2-matrix`, `pestel`, `bcg-growth-share-matrix`, `wardley-map`, `testing-pyramid` |
| Model | 139 | `prospect-theory`, `cap-theorem`, `amdahls-law`, `metcalfes-law`, `technical-debt`, `porters-five-forces` |
| Stance | 80 | `marxist-criticism`, `foucauldian-power-knowledge`, `analytic-critique`, `hermeneutic-circle` |
| Heuristic | 90 + 2 bundles | `hyrums-law`, `postels-law`, `brooks-law`, `goodharts-law`, `chestertons-fence`, `pareto-80-20` |

The heuristics class also ships a curated `library/heuristics/general.md`
bundle (Occam's Razor, Hanlon's Razor, Chesterton's Fence, Hickam's
Dictum, Pigeonhole Principle, Pareto 80/20, Parkinson's Law, Mise en
Place) for use as a single sanity-gate input.

### Domain coverage

The 62 domains include: security, strategy, product-management, ux,
law, medicine, ai, data, chemistry, physics, biology, ecology, economics,
finance, philosophy, theology, linguistics, literary-theory, music-theory,
film-theory, history, sociology, psychology, manufacturing, operations,
education, agile, okr, negotiation, marketing, communication,
decision, information-analysis, meta-science, military-strategy,
storytelling, sports, cooking, geology, astronomy, mathematics,
game-theory, productivity, personal-knowledge-management-pkm, and
several others.

Not every domain is populated in every class — lenses are the most
broadly covered (47 domains); frames, models, stances, and heuristics
each cover the subset where that class is the natural fit.

## File formats

For the full file format templates of each class, see **`CLASSES.md`**
at the repo root. In brief:

- **Lens**: `Overview / Analytical Procedure / Evaluation Criteria /
  Red Flags / Output Format`
- **Frame**: `Overview / Categories / Classification Procedure /
  Implications per Category / Common Misclassifications`
- **Model**: `Overview / Core Variables and Relationships / Key
  Predictions / Application Procedure / Boundary Conditions / Output
  Format`
- **Stance**: `Overview / Foundational Commitments / Guiding Questions
  / What It Reveals / What It Obscures / Output Format`
- **Heuristic**: `The Rule / When It Applies / When It Misleads /
  Common Misuse / How Agents Use It` (usually bundled as one file per
  domain)

## Extending the library

### Three storage layers

Prism instruments live in three layers, looked up with precedence
**project > global > bundle**:

- **Bundle** — `library/` inside the plugin checkout. Read-only; the
  657 builtin instruments shipped with Prism. Never write here by hand.
- **Global** — `~/.claude/prism/library/`. Your personal instruments,
  available in every project on this machine.
- **Project** — `./.claude/prism/library/`. Instruments scoped to the
  current repo, the most specific layer.

Each layer has its own `catalog.yml` sitting next to its `library/`.
Rebuild a single layer's catalog with
`python3 scripts/sync_catalog.py --source {bundle|global|project}`, or
print a merged cross-layer preview (no write) with
`python3 scripts/sync_catalog.py --source all`. When the same
instrument name appears in multiple layers, the closer layer wins.

### Adding an instrument by hand

To add a single new instrument file by hand:

1. **Identify the instrument.** It must be a real method used by
   practitioners, not something you just thought of. Cite the source.
2. **Pick the correct class.** Read `CLASSES.md` § "Picking the right
   class." Does the source include a procedure? → lens. Is it just a
   taxonomy? → frame. A theoretical model? → model. An interpretive
   commitment? → stance. A single-rule aphorism? → heuristic.
3. **Write the file** at `library/{class}s/{domain}/{slug}.md` using
   the matching template in `CLASSES.md`. The load-bearing section
   differs by class (Analytical Procedure for a lens; Classification
   Procedure for a frame; Application Procedure for a model; Guiding
   Questions for a stance; When It Applies / Misleads for a heuristic).
4. **Register the item in its layer's `catalog.yml`** by running
   `python3 scripts/sync_catalog.py --source {bundle|global|project}`
   (no flag is equivalent to `--source bundle`). The script scans the
   chosen layer's `library/`, extracts metadata from each file's
   frontmatter, and rewrites that layer's `catalog.yml` grouped by
   class and domain. It is idempotent and preserves hand-written
   catalog entries by default — pass `--overwrite` only if you want
   frontmatter to replace them. Use `--dry-run` to preview changes or
   `--stats` for a class/domain breakdown.
5. **Open a PR** with the new file, the catalog update, and (if
   appropriate) a composition recipe in `docs/cookbook/` that
   demonstrates how to use it.

### Adding many instruments at once

To add instruments in bulk, see `scripts/PHASE3_RUN.md` for the batch
generation pipeline. The entry point is `scripts/prism_batch.py`,
which is a markdown-output adapter over a reusable parallel runner. It
drives Haiku 4.5 with
class-specific few-shot prompts from `scripts/prompts/` and writes
generated files straight into `library/{class}s/{domain}/`. The full
v0.3 batch of 639 files cost roughly a few dollars on Haiku 4.5.

Once the batch run finishes, run `python3 scripts/sync_catalog.py`
(equivalent to `--source bundle`) to register every new file in
`catalog.yml`. The same script is the right entry point whenever any
layer's `library/` changes — after a batch run, after hand-editing
files, or after pruning obsolete entries — just point `--source` at
the layer you touched.

Contributions of non-English-language and domain-local instruments are
especially welcome — the existing `achievement-standard-alignment` lens
is Korea-specific by design, and similar local instruments exist for
many other educational, legal, regulatory, and cultural contexts
worldwide.

## Why "Prism"

A lens shapes what you see without telling you what to think. A lab is
where you craft and test new instruments. Together: a workshop for
building analytical instruments, and a collection of ones already made.
v0.2 introduced the 5-class taxonomy — lenses are still the headline
instrument, but they now sit alongside frames, models, stances, and
heuristics as first-class citizens. The library has grown from 18
hand-written files (v0.1) to 742 across 62 domains.

## License

MIT. See `LICENSE` for details.
