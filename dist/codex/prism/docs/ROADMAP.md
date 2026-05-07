# Prism Roadmap

Prism is a Claude Code plugin that provides a catalog of analytical instruments
across 5 classes — lens, frame, model, stance, heuristic — for use when building
domain-expert agents and skills. This roadmap describes where the catalog stands
today and what each upcoming minor version changes.

## v0.1.0

- Renamed from lenslab. Same 657-instrument library across 50 domains.
- Plugin identity clarified: Prism is a catalog reference provider, not an agent
  or skill generator.
- Top-level class term unified as "instrument" (lens, frame, model, stance,
  heuristic are its five sub-classes).
- Breaking change from lenslab v0.3.0: name, plugin identifier, and package
  version all reset to 0.1.0 to mark a fresh start under the new identity.
- Existing `create-agent` slash command and `agent-creator` skill still ship in
  this release for continuity, but are deprecated and removed in v0.2.0.

## v0.2.0

Structural changes that align the plugin with its clarified identity.

- **New skills**
  - `search` — read-only skill for exploring the instrument catalog by
    class, domain, or free-text query. Returns candidate instruments for
    whatever the caller is building (an agent, a skill, or a one-off prompt).
  - `make-instrument` — interview-style skill for creating a new instrument.
    Takes a minimal input (framework name, domain), asks targeted clarifying
    questions for any ambiguous fields, then auto-generates the instrument body
    using an LLM (Haiku-class model, following the same template pipeline
    already used for the v0.3 batch).
- **3-layer custom instrument storage**
  - Bundle (read-only): the 657 built-in instruments shipped with Prism.
  - Global: `~/.claude/prism/library/` — the user's personal instruments,
    available in any project.
  - Project: `<project>/.claude/prism/library/` — instruments scoped to a
    single repository.
  - Lookup precedence: project > global > bundle. Closer context overrides
    broader context.
- **Removed**
  - `create-agent` slash command and `agent-creator` skill. Agent and skill
    creation belong to Claude Code's native mechanisms — Prism only supplies
    the catalog they reference.
- **Restructured**
  - `agents/examples/*.yml` becomes `docs/cookbook/*.md` as composition
    recipes: narrative markdown explaining how a set of instruments can be
    combined for a given task, not an executable agent config.
- **Scripts**
  - `sync_catalog.py --source {bundle|global|project}` targets any layer of
    the 3-layer storage.

## v0.2.1

A consolidation pass on top of v0.2.0, focused on giving Prism a single
memorable user-facing entry point.

- **Router skill** — `make-instrument` has been folded into a new `/prism`
  router skill. The router itself is a thin classifier (~80 lines) that
  dispatches the request into one of three intents — about, make, help —
  and loads the corresponding reference file from `skills/prism/references/`
  (`about.md`, `make.md`, `help.md`). The full interview protocol and the
  5-class decision tree now live in `references/make.md`.
- **Catalog-browse unchanged in shape, stronger in framing** — still a
  separate skill, but its description has been rewritten to position it as
  a proactive recommender that should be consulted whenever the user is
  about to build an agent or skill, not just a passive browse tool.
- **Single memorable entry point** — `/prism` (explain), `/prism <name>`
  (create), and `/prism help` (quick reference) all flow through the same
  router, so users only have to remember one command.

## v0.5.6 (Current)

Debate defaults to instrumented execution.

- **Instrumented debate by default.** `prism:debate` now searches/selects
  relevant Prism instruments before spawning participants, resolves their
  paths with fetch semantics, and injects a read/apply directive into every
  subagent prompt.
- **Explicit persona-only mode.** Unguided persona debate is still
  available, but only when the user opts out with `--persona-only` or
  equivalent wording.
- **No silent fallback.** If instruments cannot be found or resolved, the
  debate must stop and report the issue instead of quietly running as a
  persona-only discussion.

## v0.5.5

Codex marketplace source fix.

- **Remote source uses `url`.** The Codex marketplace entry now points at
  the repository-root plugin through a Git-backed `url` source, matching
  the official Codex plugin packaging guidance for plugins that live at
  the repository root.

## v0.5.4

Codex plugin install packaging fix.

- **Codex marketplace target fixed.** Points the Codex marketplace entry at
  the repository root plugin bundle (`./.`) so Codex installs the real
  `skills/`, `library/`, and `catalog.yml` directories instead of a thin
  symlink wrapper that does not survive plugin installation.
- **Codex install flow corrected.** Documents the official flow:
  `codex plugin marketplace add`, then `/plugins`, then `Install plugin`,
  then start a new thread.
- **Search skill YAML fixed.** Quotes the `search` skill description so
  Codex parses the frontmatter and exposes `prism:search`.

## v0.5.3

Superseded Codex packaging attempt.

- Removed the symlink wrapper, but the release was incomplete and is
  superseded by v0.5.4.

## v0.5.2

Codex marketplace packaging fix.

- **Codex marketplace path fixed.** Moves the Codex marketplace entry to the
  expected `./plugins/prism` plugin root instead of the repository root, which
  Codex rejects as an empty local plugin source path.
- **Shared bundle preserved.** Adds a thin plugin wrapper that links to the
  existing `skills/`, `library/`, `catalog.yml`, and docs instead of
  duplicating the 742-file instrument library.
- **Codex install caveat documented.** Notes that current Codex CLI builds
  may require manually materializing the plugin cache after
  `codex plugin marketplace add` because no custom marketplace install
  command is exposed.

## v0.5.1

Codex compatibility patch for skill loading.

- **Codex skill description limit.** Shortens the `search` skill frontmatter
  description below Codex's 1024-character limit so the plugin can load.

## v0.5.0

Initial Codex Plugin compatibility layer. Adds `.codex-plugin/plugin.json`
and `.agents/plugins/marketplace.json` with the existing `skills/`
directory exposed to Codex while preserving the Claude Code plugin
manifest and installation path.

- **Codex manifest added.** The plugin now declares `skills: "./skills/"`
  for Codex Plugin loading.
- **Codex marketplace added.** The repository can be registered via
  `codex plugin marketplace add 97Wobbler/prism@v0.5.0`.
- **Claude behavior preserved.** Existing `.claude-plugin/` metadata remains
  in place for Claude Code users.
- **Known compatibility follow-up.** Some skill prose still references
  Claude Code-specific storage and agent flows; those adaptations are left
  for a later pass.

## v0.4.3

Skipped. The initial Codex compatibility work was promoted to v0.5.0 because
it adds a new plugin ecosystem surface rather than a patch-level fix.

## v0.4.2

Software-engineering law expansion across architecture and agile domains.
Sources 56 well-known software-engineering laws from a curated GeekNews
article and selects 27 high-signal additions missing from the catalog,
skipping satirical or weak entries (Putt, Dilbert, Zawinski, Sturgeon,
Cunningham, Ringelmann, Price, Gilb, 90-90 Rule) and items already covered
(Conway, SOLID, Pareto, Parkinson, Hanlon, Occam, Sunk Cost, Confirmation
Bias, First Principles, Chesterton's Fence).

- **9 architecture heuristics + 1 distributed-systems bundle.**
  - `hyrums-law` — observable behavior becomes the real contract.
  - `postels-law` — robustness principle, paired with Hyrum.
  - `galls-law` — complex systems evolve from working simple ones.
  - `leaky-abstractions` — every non-trivial abstraction leaks.
  - `kiss-principle`, `dry-principle`, `law-of-demeter`,
    `principle-of-least-astonishment` — classic design heuristics.
  - `distributed-fallacies` — bundled file covering all 8 Fallacies of
    Distributed Computing as a single sanity-gate input.
- **9 agile heuristics.**
  - `brooks-law` — adding people to a late project, with the n(n-1)/2
    communication-paths math and Little's Law as quantitative grounding.
  - `bus-factor`, `boy-scout-rule`, `linus-law`, `kernighans-law`, `yagni`,
    `second-system-effect`, `pesticide-paradox`.
  - `premature-optimization` — Knuth's actual claim with the
    architectural-vs-micro distinction made explicit, addressing the
    common HN misreading.
- **2 cross-domain heuristics.**
  - `goodharts-law` in `okr` — KPI/metric-design sanity gate, with
    Campbell's Law noted as a sister principle.
  - `hofstadters-law` in `productivity` — self-referential estimation
    multiplier, paired with reference-class forecasting.
- **6 new models.** `amdahls-law`, `gustafsons-law`, and `lehmans-laws`
  in a new `models/architecture/` domain; `cap-theorem` in `models/data`
  with PACELC noted as a modern refinement; `technical-debt` in
  `models/agile` with Fowler's deliberate/inadvertent × prudent/reckless
  quadrant; `metcalfes-law` in `models/strategy` with the Briscoe-
  Odlyzko-Tilly n·log(n) critique to avoid overstating network effects.
- **1 new frame.** `testing-pyramid` in `frames/agile` — three-layer
  classification (unit / integration / E2E) with Honeycomb and Trophy
  alternatives noted as serious modern critiques for backend services
  and frontend respectively.
- **Catalog grows from 715 to 742 entries.** 62 domains unchanged
  (`models/architecture/` is the first model directory under that name,
  but the domain itself already existed via heuristics).

## v0.4.1

Philosophy domain expansion and a new cookbook recipe that demonstrates
the "instruments > personas" thesis by decomposing a monolithic system
prompt into reusable catalog citizens.

- **3 new philosophy lenses.**
  - `multi-layer-reading` — generates and labels multiple defensible
    readings of a short claim across semantic, figurative, performative,
    and contextual layers. Operationalizes the hermeneutic-circle stance
    into a lens with full 4-requirement compliance (input / procedure /
    output / confidence). `underlying_class: stance`.
  - `conceptual-analysis` — extracts key concepts, produces charitable
    and critical definition pairs, maps boundaries with edge cases, and
    rates operationalizability (operationalizable / partial / unfalsifiable).
  - `presupposition-analysis` — walks five categories of hidden assumption
    (definitional / empirical / structural / normative / scope), grades
    plausibility (strong / contested / weak), and states failure impact.
- **1 new philosophy stance.**
  - `analytic-critique` — brackets moral evaluation, refuses truth/falsity
    assumptions before analysis, separates attribution from evidence, and
    demands explicit context for vague claims. Distills the Constraints
    section of the original Critical Decomposition system prompt into a
    reusable interpretive posture.
- **New cookbook recipe: `critical-decomposer`.** Composes the three new
  lenses + existing `toulmin-argument-model` + `analytic-critique` stance
  + general and philosophy heuristic bundles into a 7-step pipeline that
  reconstructs the original 5-phase Critical Decomposition engine. The
  recipe includes a "Reconstruction note" section that explains why adding
  catalog citizens and writing a recipe is preferable to importing the
  system prompt as a monolithic skill.
- **`sync_catalog.py` encoding fix.** Added UTF-8 stdout/stderr
  reconfiguration with replacement fallback at script startup. Prevents
  `UnicodeEncodeError` when printing em-dashes and other non-ASCII
  characters on Windows consoles (cp949, cp1252).
- **Catalog grows from 711 to 715 entries.** 62 domains unchanged.

## v0.4.0

New `debate` orchestration skill — multi-agent discussion engine with
three modes (review / ideate / solve).

- **New `prism:debate` skill.** Multiple agent personas independently
  analyze a document, brainstorm ideas, or propose solutions through
  structured rounds. The orchestrator (main session) controls rounds,
  collects JSON responses from parallel subagents, and evaluates
  consensus/convergence based on mode-specific criteria.
- **Three modes:**
  - `review` — multi-perspective analysis with quantitative consensus
    judgment (recommendation agreement >= 75%, issue resolution >= 80%,
    no unresolved critical issues).
  - `ideate` — divergent brainstorming with no convergence pressure;
    tracks idea pool growth across rounds.
  - `solve` — solution proposals converging toward a best answer through
    cross-review, tradeoff mitigation, and dealbreaker resolution.
- **Mode inference.** Explicit flags (`--review`, `--ideate`, `--solve`)
  override; otherwise the skill infers from context. Default: `review`.
- **Prism instrument integration.** In v0.4.0, stances and lenses from
  the catalog could serve as optional expertise sources for debate
  participants via `/prism fetch`. v0.5.6 later changed this default so
  `prism:debate` is instrumented unless explicitly run as persona-only.
- **Router and references updated.** `prism:prism` SKILL.md, `about.md`,
  and `help.md` now include debate routing rules and usage documentation.

## v0.3.2

Skill naming overhaul and a new `fetch` skill for instrument delivery
to subagents.

- **`catalog-browse` → `search` rename.** The read-only catalog
  exploration skill is now `prism:search` — shorter, verb-based, and
  consistent with the new `fetch` sibling. All references across
  README, router, references, and docs updated; the old
  `skills/catalog-browse/` directory removed.
- **New `prism:fetch` skill.** Resolves instrument names to absolute
  file paths and returns a ready-made instruction block that can be
  pasted into a subagent prompt. The block includes a table of
  instruments (name, class, one-liner, path) and a per-class guide
  telling the subagent which section to follow (Analytical Procedure
  for lenses, Guiding Questions for stances, etc.). This closes the
  gap where subagents were told instrument names but never given the
  actual file content or reading instructions.
- **Two-step workflow.** The intended usage is now:
  1. `/prism search <domain> <class>` — discover instruments.
  2. `/prism fetch <instrument-names>` — prepare them for a subagent.

## v0.3.1

A patch release that drains the immediately-actionable carry-over from
the v0.3.0 follow-through audit. No new instruments, no new domains,
no user-facing surface changes — only catalog deconfliction and a
generation-pipeline hardening.

- **`nist-ai-rmf` deconfliction.** v0.3.0 added an `applied-ethics`
  lens version of NIST AI RMF without noticing the catalog already
  held an `ai` frame version with the same name slug. Both files
  coexisted under different `(class, domain)` pairs, leaving
  semantically duplicate entries in triage. v0.3.1 removes the frame
  (`library/frames/ai/nist-ai-rmf.md`) and keeps the lens. Total
  instrument count drops from 712 to 711; the `ai` domain loses one
  frame; `applied-ethics` is unchanged.
- **`scripts/prism_batch.py` prompt hardening.** Two recurring failure
  modes from the v0.3.0 generation run were patched in all five
  class-specific system prompts (`lens` / `frame` / `model` / `stance`
  / `heuristic`):
  - **Slug enforcement** — the prompt now states explicitly that the
    frontmatter `name` field MUST be byte-identical to the spec slug
    given in the user prompt, citing the v0.3.0 incident where Haiku
    expanded `tod` into `transit-oriented-development` and silently
    broke the spec/catalog mapping.
  - **`source:` colon escaping** — the prompt now requires any
    frontmatter value containing a colon (most commonly book titles
    and subtitles in `source:`) to be wrapped in double quotes, to
    keep strict YAML parsers happy without relying on the
    `_shallow_parse` fallback in `sync_catalog.py`.

  These changes do not affect existing instruments — only future
  `prism_batch.py` runs.

## v0.3.0

A 12-domain expansion driven by an external contributor batch. The
catalog grows from 658 to 712 instruments — about 8% — and the domain
count rises from 50 to 62. All new instrument bodies were generated
via the same `scripts/prism_batch.py` pipeline (Haiku 4.5 + class-
specific system prompts + golden few-shot examples) that authored the
original 656, ensuring tone and structural consistency with the
existing catalog.

- **12 new domains** — `systems-thinking`, `complexity-science`,
  `public-policy`, `media-studies`, `behavioral-finance`,
  `urban-planning`, `political-science`, `anthropology`,
  `neuroscience`, `applied-ethics`, `graph-theory`, `psychoanalysis`.
  Two of these (systems-thinking and complexity-science) shipped first
  in a quality-gated P1 commit because their concepts (causal loops,
  stocks/flows, archetypes, power laws, SOC, emergence, NP-hardness)
  are implicitly presupposed by other lenses.
- **5 existing-domain reinforcements** — Toulmin in `philosophy`;
  Stasis theory + Classical canons + Peirce icon-index-symbol in
  `linguistics` (rhetoric absorbed rather than given its own domain
  by deliberate decision); social psychology block (bystander effect,
  situationism, social proof, Milgram obedience) in `psychology`;
  Schelling focal points in `game-theory` (distinct from the existing
  `schelling-segregation-model` in sociology); 6 individual cognitive
  biases (availability, confirmation, anchoring, base-rate, sunk-cost,
  hindsight) in the `general` heuristics bundle.
- **Three load-bearing placement decisions** — NP-hardness lives under
  `complexity-science`, not `graph-theory` (which is reserved for the
  algorithmic layer: network analysis, spanning trees). Psychoanalysis
  (Freud / Lacan / Jung) is its own domain, separated from
  `psychology` for triage clarity, with future expansion expected
  toward Klein / Winnicott / Bion. `applied-ethics` covers EU AI Act,
  NIST AI RMF, GDPR, OECD AI Principles, bioethics 4 principles, and
  research ethics — ISO 42001 was deferred as too narrow in
  application context for this round.
- **Pipeline maturation** — 5 system prompts and 10 golden-example
  frontmatters that still carried v0.1's Korean `one_liner` convention
  were translated to English first (commits `4d4e184`, `1707b2f`),
  preserving the v0.2.3 catalog-as-LLM-surface invariant. An
  independent `Explore`-agent integrity audit caught 12 frontmatter
  defects in the generated batch (1 slug mismatch, 11 unquoted colons
  in `source:` fields where book titles contained colons), all fixed
  in commit `db58f78` before the version bump.
- **v0.2.3 follow-through — library frontmatter sync.** v0.2.3
  translated the 658 catalog `one_liner` fields to English but left the
  matching `library/.md` frontmatter `one_liner` fields in Korean,
  creating a permanent mismatch between the LLM-consumed catalog
  surface and the human-readable instrument files. v0.3.0 closes this
  gap by patching all 646 library frontmatters in place (only the
  `one_liner` field; bodies remain Korean). After the patch, every
  instrument's frontmatter `one_liner` matches its catalog entry
  byte-for-byte.
- **Instrument-count limit acknowledged** — the project's stated
  out-of-scope item ("growing the bundle beyond ~700 instruments")
  is now within ~10 of its ceiling. Future contributions should
  prefer reinforcing existing domains or replacing low-quality
  entries over net-new growth.

## v0.2.3

A catalog-only patch release. No user-facing surface or runtime behavior
changes — every adjustment lives in `catalog.yml` and the heuristics
library.

- **`xy-problem` heuristic added** — registered under
  `library/heuristics/general/xy-problem.md` and the `general` section of
  the catalog. Encodes the "answer the X behind the Y" anti-pattern as a
  one-rule heuristic for requirement-gathering, debugging, and code-review
  lenses to consume in embedded or sanity-gate mode.
- **All 658 catalog `one_liner` fields translated KO→EN** — the catalog
  is consumed by the LLM triage step (instrument selection / retrieval),
  and English summaries align better with the predominantly English
  instrument names and source terminology (`razor`, `dictum`, `chronotope`,
  `OODA`, …). User-facing surfaces — README, `/prism help`, and every
  instrument body `.md` file — remain Korean. Translation was performed
  via a four-step extract → translate → merge → verify pipeline that
  preserved comments, blank lines, indentation, and field order
  byte-for-byte (line-based regex substitution, no YAML roundtrip).

## v0.2.2

A first-contact UX pass on top of v0.2.1, tightening what `/prism` shows
on invocation.

- **about.md slimmed down** — the about reference was ~60 lines covering
  class definitions, 3-layer storage, and out-of-scope rules. v0.2.2 cuts
  it to ~25 lines: one-paragraph summary, a one-line-each reminder of the
  5 classes, and three "바로 시작" entry points. Full class semantics and
  storage architecture are now on-demand — the user asks, Claude reads
  `CLASSES.md` to answer.
- **No-narration rule** — all three `references/*.md` files and the
  router `SKILL.md` now carry an explicit "do not narrate routing or
  file-loading decisions" instruction. Claude should render the reference
  content directly on `/prism` invocation, without meta commentary about
  which intent was classified.

## Future

Extensions on top of the v0.4 structure.

- `/prism contribute` — a new intent branch of the `/prism` router for
  upstreaming a local instrument. Walks through fork, branch, and PR against
  the Prism repo, using a new `references/contribute.md` reference file
  loaded by the router when the user's request matches the contribute
  intent.
- Enhanced catalog discovery: fuzzy name matching, class/domain graph
  navigation, and "instruments commonly used together" hints derived from
  cookbook compositions.
- Community curation workflow for accepted upstream contributions, including
  review criteria and a lightweight acceptance pipeline.

### Carry-over from v0.3.0 (deferred)

- **ISO 42001 in `applied-ethics`** — explicitly deferred during the
  v0.3.0 contributor batch. The certification framework's application
  context is too narrow for general-purpose triage to benefit, but it
  belongs in the catalog as soon as a concrete use case appears.
- **`psychoanalysis` domain expansion** — Klein, Winnicott, Bion (object
  relations and post-Freudian schools) are the natural next stances for
  this domain, which currently holds Freud / Lacan / Jung. Adding them
  would also unlock comparison lenses across schools.
- **Pre-`prism_batch` triage check for cross-class name collisions.**
  v0.3.1 fixed the one duplicate (`nist-ai-rmf`) and updated the
  generation prompts so future spec slugs are enforced verbatim, but
  the spec-authoring step itself still has no automated check that a
  proposed `name` does not already exist somewhere else in the
  catalog under a different class. Adding a pre-batch validator that
  rejects spec slugs colliding with any existing `(class, name)` (or
  even just `name`) would prevent recurrence at the source.

## Out of scope

Things Prism explicitly does not do, regardless of version.

- **Meta-workflows** (e.g., project-management pipelines, self-iterating dev
  loops). These are larger than a single instrument and belong in the user's
  own skills or a separate harness project.
- **Agent and skill generation.** Use Claude Code's native agent creation or
  the official `skill-creator` skill. Prism's role is to supply the catalog
  that those tools reference.
- **Growing the bundle beyond ~700 instruments.** The v0.3 batch (639 new
  files generated via Haiku) already demonstrated that batch instrument
  generation is a solved, reproducible problem. The project's value is in
  curation and retrieval, not volume.
