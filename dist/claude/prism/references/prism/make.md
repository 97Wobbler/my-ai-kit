<!-- Rendering rule: Do not narrate routing or file-loading decisions to the user — run the workflow below directly, without meta commentary about which intent was classified or which file was opened. -->

# Create a Prism instrument

You are helping a user add **one** new instrument to their Prism library.
Prism sorts every instrument into exactly one of five classes — **lens,
frame, model, stance, heuristic** — and each class has its own file
format. Your job: collect the minimum needed, determine the right class,
generate the body, save it to the correct layer.

See `CLASSES.md` at the repo root for the full decision tree and the five
file-format templates. This reference points at CLASSES.md rather than
duplicating templates verbatim.

**Core principle.** This is an **interview**, not a form. Ask only the
questions whose answers you cannot already infer. Most requests ("create
a lens for CVSS scoring") already tell you name, domain, and class — in
that case go straight to generation.

## When this workflow applies

- "create a new lens for <X>"
- "add a frame / framework for <Y domain>"
- "make an instrument for <Z>"
- "I want to write up <framework name> as a Prism <class>"
- "새 렌즈/프레임/모델 만들어줘"

The user's entry point is `/prism {framework name}`; the router dispatches
here once a framework name is present.

## When NOT to use this workflow

- **Batch generation** (many instruments at once) → use
  `python3 scripts/prism_batch.py` with the appropriate prompt template.
  This workflow creates exactly one file per invocation.
- **Browsing the catalog** → use the `search` skill.
- **Editing an existing instrument** → read and edit the file directly.
- **Creating an agent config** → that is Claude Code's native agent
  mechanism; Prism only provides the catalog.

## Workflow

### Step 1 — Collect minimal input

From the user's initial request, extract:

1. **Framework name** (required) — e.g., "CVSS v3.1", "Cynefin".
2. **Domain** — infer if obvious (`CVSS` → `security`, `Bloom's
   Taxonomy` → `education`). Otherwise ask once.
3. **Target class** — infer if stated outright ("a new **lens** for…").
   Otherwise determine via the Step 2 decision tree.

A confident inference is better than a redundant question.

### Step 2 — Disambiguate (at most 3 questions)

Ask clarifying questions **only** when a field is genuinely ambiguous.
The canonical ambiguous fields, in priority order:

1. **Class undetermined.** Walk the CLASSES.md decision tree:
   - Procedure **and** output template **and** confidence signal →
     **lens**.
   - Taxonomy with categories + criteria, no "next step" procedure →
     **frame**.
   - Theoretical/predictive model (variables, relationships,
     predictions) with no built-in Analytical Procedure → **model**.
   - Interpretive commitment about what is worth looking for →
     **stance**. (Do NOT convert stances to lenses.)
   - Single-rule aphorism → **heuristic**.

   Two "yes" answers usually mean the source is a frame or model
   someone operationalized into a lens — ask which shape the user
   wants. If promoting from another class, record
   `underlying_class: frame | model | heuristic` in the frontmatter.

2. **Source / attribution unknown.** If unknown, use
   `source: "origin uncertain"`. Never invent an attribution.

3. **Output format unclear** (lenses and models only). Ask for a
   one-sentence sketch — without it a lens cannot carry a confidence
   signal and fails criterion 4.

Hard limit: **3 questions total**. If still underdetermined, write
what you have, flag the gap in the body, and let the user revise.

### Step 3 — Determine target class

Apply the decision tree above. Announce the chosen class with a
one-sentence reason before generating. For a lens operationalized
from another class, name both (e.g., "lens with `underlying_class:
frame`").

### Step 4 — Generate the body via LLM call

Generate the file using the class-appropriate template below. These
are **section-header reminders**; full templates with guidance live
in CLASSES.md. Match the section order and header spelling exactly —
do not rename or add sections.

**Voice & style (applies to all classes):**
- Body in English, technical but accessible.
- Frontmatter `one_liner` in Korean (한국어), terse, matching the
  existing catalog style.
- Cite source (author, institution, year) when known; otherwise
  `origin uncertain`. Never fabricate attribution.
- Target 600–1200 words for lens/frame/model/stance; heuristics are
  tighter.
- No filler, no "in conclusion," no meta-commentary.

**Per-class section order** (see CLASSES.md for the full template
including frontmatter fields and detailed guidance):

- **Lens** → `Overview`, `Analytical Procedure`, `Evaluation
  Criteria`, `Red Flags`, `Output Format` (must include an explicit
  confidence signal per finding). The `Analytical Procedure` is
  load-bearing: vague steps mean a vague lens.
- **Frame** → `Overview`, `Categories`, `Classification Procedure`,
  `Implications per Category`, `Common Misclassifications`. Do NOT
  add `Output Format` or confidence — those are lens-only.
- **Model** → `Overview`, `Core Variables and Relationships`, `Key
  Predictions`, `Application Procedure`, `Boundary Conditions`,
  `Output Format`. The `Application Procedure` must walk input →
  variables → predictions → boundary check.
- **Stance** → `Overview`, `Foundational Commitments`, `Guiding
  Questions`, `What It Reveals`, `What It Obscures`, `Output
  Format`. The `Guiding Questions` are the working instrument.
- **Heuristic** → one entry per file (or append to a bundle):
  `The Rule`, `When It Applies`, `When It Misleads`, `Common
  Misuse`, `How Agents Use It`.

Frontmatter always includes `name`, `display_name`, `class`, `domain`,
`source`, `best_for` (list), `one_liner` (Korean). Lenses also
include `underlying_class` (`native` or the source class). See
CLASSES.md § "File format" for each class for the exact frontmatter.

### Step 5 — Ask where to save

Present two layer options. Never write to the bundle (`./library/`) —
it is read-only.

```
Where should I save this instrument?
  [1] Project  → ./.claude/prism/library/<plural-class>/<domain>/<name>.md
  [2] Global   → ~/.claude/prism/library/<plural-class>/<domain>/<name>.md
```

`<plural-class>` is one of `lenses`, `frames`, `models`, `stances`,
`heuristics`. `<name>` is a slug of the framework name (lowercase,
hyphens, no punctuation).

**Save location decision tree:**

1. User explicitly picks a layer → use it.
2. "here" / "this project" → project layer.
3. "everywhere" / "global" / "across projects" → global layer.
4. Unclear → **project** (closer wins; easier to promote to global
   later than to pull back from it).
5. **Never** write to `./library/` (bundle ships with the plugin and
   stays immutable).

Create any missing parent directories before writing.

### Step 6 — Post-save instructions

After writing, tell the user exactly one follow-up command:

- Saved to project → `python3 scripts/sync_catalog.py --source project`
- Saved to global  → `python3 scripts/sync_catalog.py --source global`

This refreshes only the layer you wrote to. Do NOT run the command
yourself — the user may be in a different working directory. Remind
the user that `search` will include the new instrument in its
merged view once the catalog is refreshed.

## Examples

- **Unambiguous** — "Create a new lens for PASTA threat modeling."
  Infer name=PASTA, domain=security, class=lens. Skip clarifying
  questions. Generate. Ask: project or global?
- **Ambiguous class** — "Add Cynefin for decision-making." Cynefin
  is a classification frame; propose class=**frame** with a one-line
  rationale. If the user wants the lens variant, set
  `underlying_class: frame` and generate a lens instead.
- **Unknown source** — "Make a heuristic for 'if a test is flaky
  three times, delete it.'" Class=heuristic is obvious; set
  `source: "origin uncertain"`, do not invent an author.
