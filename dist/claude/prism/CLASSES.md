# CLASSES — the Prism 5-class taxonomy

Prism composes domain-expert analysis agents out of **structured
instruments**, not persona prompts. But not every useful instrument is the
same kind of thing. v0.2 makes the distinction explicit by sorting every
instrument into exactly one of five classes: **lens, frame, model, stance,
heuristic**.

This file is the reference for contributors. If you are adding a new item,
read the strict lens definition first, decide which class applies, then use
the matching file format template below.

---

## The strict definition of a lens

A **lens** must satisfy **all four** criteria:

1. **Defined input type** — the file specifies what artifact it operates
   on (an API spec, a lesson plan, an incident report, a claim, …).
2. **Executable procedure** — numbered steps or a question walk concrete
   enough that someone unfamiliar with the framework can run them step by
   step. "Assess the threat level" is not executable. "For each data flow
   crossing a trust boundary, list what identity information is attached
   and whether the receiving component re-validates it" is.
3. **Structured output format** — a fixed template (headers, tables,
   fields, scales), not free prose.
4. **Confidence evaluation** — findings carry a confidence signal (high /
   medium / low, or a scored rubric), so downstream synthesis can weigh
   them.

**If any of the four is missing, the artifact is not a lens.** It may still
be valuable — it belongs to one of the four sister classes below.

---

## Picking the right class

Start from the source instrument, not from what you want to build.

| Question about the source instrument | Class |
|---|---|
| Does it include a procedure *and* an output template *and* a confidence signal? | **lens** |
| Is it purely a taxonomy / classification matrix (categories + criteria, no next-step procedure)? | **frame** |
| Is it a theoretical or predictive model (variables, relationships, predictions) with no built-in "how to apply" steps? | **model** |
| Is it an interpretive commitment — a position about *what is worth looking for* in any artifact? | **stance** |
| Is it a single-rule aphorism or rule of thumb? | **heuristic** |

If multiple answers are "yes," that usually means the source is a frame or
model that *someone has operationalized into a lens*. Record the source's
native class as `underlying_class: frame | model | heuristic` in the lens
file frontmatter so the pattern stays visible to future contributors.

**Do not invent a 6th class.** Five is the final taxonomy.

---

## Class 1 — Lens (렌즈)

**What it is:** A structured, executable analytical procedure that
satisfies all four criteria above.

**Canonical examples:**
- STRIDE (threat modeling)
- OWASP API Top 10 review
- CVSS v3.1 Scoring
- Bloom's Taxonomy classification
- Pre-mortem
- IRAC (legal analysis)
- ACH (Analysis of Competing Hypotheses)

**Storage:** `library/lenses/<domain>/<name>.md`

**File format:**
```markdown
---
name: <framework name>
domain: <general | security | education | ...>
source: <author, institution, year>
underlying_class: <native | frame | model | heuristic>
best_for: <one line — when this lens is most useful>
---

# <framework name>

## Overview
<2-3 sentences: what it is and why practitioners use it>

## Analytical Procedure
<numbered, directly-executable steps. The load-bearing section —
if this is vague, the whole lens is vague.>

## Evaluation Criteria
<checklist, rubric, or scoring matrix the analyst fills in>

## Red Flags
<concrete patterns that, when observed, indicate a problem>

## Output Format
<template for structured output — headers, fields, scales,
and an explicit confidence signal per finding>
```

**Agent usage:** Applied in the **analyze** step. Each selected lens is run
in sequence; findings are collected per lens and tagged with confidence.

---

## Class 2 — Frame (분류 프레임)

**What it is:** A taxonomy or classification matrix. Pure frames provide
categories and classification criteria but no execution procedure. They
tell you *how to sort*, not *what to do next*.

**Canonical examples:**
- Cynefin (Clear / Complicated / Complex / Chaotic / Confused)
- Kano Model (Must-be / Performance / Attractive / Indifferent / Reverse)
- BCG Growth-Share Matrix
- Webb's Depth of Knowledge
- MoSCoW
- Porter's Generic Strategies
- CEFR language levels

**Storage:** `library/frames/<domain>/<name>.md`

**File format:**
```markdown
---
name: <frame name>
domain: <...>
source: <...>
best_for: <what this frame is useful for sorting>
---

# <frame name>

## Overview
<2-3 sentences>

## Categories
<enumerated list with discriminating criteria per category>

## Classification Procedure
<how to decide which category an instance belongs to — the
minimum procedure needed to make the frame usable>

## Implications per Category
<once classified, what does it mean? What should happen next?>

## Common Misclassifications
<border cases and typical errors>
```

**Agent usage:** Two modes.
- **Classify step** — Before lenses run, the frame characterizes the input
  (e.g., "Is this a Complex or Complicated problem?" → select different
  lens bundles based on the answer).
- **Convert to lens** — Wrap a procedure around the frame to turn it into
  a lens (see "Converting other classes to lenses" below).

---

## Class 3 — Model (이론 모델)

**What it is:** A descriptive or predictive theoretical model. Models
explain how a domain works; they are not procedures. They become useful
when *instantiated* against a specific input to generate predictions or
explanations.

**Canonical examples:**
- Prospect Theory (Kahneman & Tversky)
- Nash Equilibrium
- Porter's Five Forces
- IS-LM
- Lotka-Volterra
- Marcus Theory (electron transfer)
- Principal-Agent
- Attachment Theory

**Storage:** `library/models/<domain>/<name>.md`

**File format:**
```markdown
---
name: <model name>
domain: <...>
source: <author, publication, year>
best_for: <what phenomena this model explains or predicts>
---

# <model name>

## Overview
<what the model claims, in 3-4 sentences>

## Core Variables and Relationships
<the variables the model uses and how they interact>

## Key Predictions
<what the model predicts — non-obvious consequences>

## Application Procedure
<how to instantiate the model against a concrete input:
1. Map the input's entities to the model's variables
2. Identify values / parameters
3. Read off predictions
4. Check for boundary conditions that invalidate the model>

## Boundary Conditions
<when the model does NOT apply or breaks down>

## Output Format
<what applying the model to an input produces>
```

**Agent usage:** Applied in the **model-interpret** step. The agent maps
the input (or earlier lens findings) onto the model's variables and reads
off predictions. A model becomes a lens only when paired with a fixed
Analytical Procedure and confidence rubric.

---

## Class 4 — Stance (비판적 관점)

**What it is:** An interpretive position or critical framework. Stances do
not have procedures or predictions — they have **commitments** about what
is worth looking for. They make certain things visible that other stances
ignore.

**Canonical examples:**
- Marxist criticism (class, production relations, ideology)
- Feminist criticism (gender, power, representation)
- Foucauldian Power / Knowledge (discourse, subject production)
- Deconstruction (binary oppositions, margins)
- Bourdieu's Habitus + Field + Capital
- Thick Description (Geertz)
- Actor-Network Theory (Latour)
- Postcolonial theory (Said, Spivak)

**Storage:** `library/stances/<domain>/<name>.md`

**File format:**
```markdown
---
name: <stance name>
domain: <...>
source: <...>
best_for: <what kind of artifact this stance can illuminate>
---

# <stance name>

## Overview
<what the stance is committed to — its core claim about the world>

## Foundational Commitments
<the axioms the stance accepts without arguing for them in each use>

## Guiding Questions
<the set of questions this stance asks of any artifact. This is
what replaces the Analytical Procedure of a lens.>

## What It Reveals
<the kinds of findings that only become visible through this stance>

## What It Obscures
<the blind spots — what this stance tends to miss or suppress>

## Output Format
<how to present findings made through this stance>
```

**Agent usage:** Applied in the **critical-read** step. Stances operate on
the same input as lenses but with different questions. Multiple stances
can be applied to the same input, and their findings compared against each
other. A stance file is **not** converted to a lens — it operates in its
own mode.

---

## Class 5 — Heuristic (원리 / 격언)

**What it is:** A single rule of thumb. A one-line principle that sharpens
judgment in a specific situation. Heuristics are too small to be lenses,
but they function as checks inside or alongside lens-based analysis.

**Canonical examples:**
- Occam's Razor
- Hanlon's Razor
- Chesterton's Fence
- Hickam's Dictum (counterweight to Occam's)
- Pigeonhole Principle
- Pareto 80/20
- Parkinson's Law
- Mise en Place

**Storage:** `library/heuristics/<domain>.md` (bundled, preferred) or
`library/heuristics/<domain>/<name>.md` (individual, when a single heuristic
deserves its own file).

**File format (per heuristic entry):**
```markdown
## <heuristic name>

**The Rule**
<one-sentence statement of the heuristic>

**When It Applies**
<the situations where the rule sharpens judgment>

**When It Misleads**
<situations where blindly applying the rule produces worse decisions>

**Common Misuse**
<the typical failure modes>

**How Agents Use It**
<either: as a check inside a lens's procedure, OR
as a sanity gate in the synthesize step>
```

A bundled heuristics file is a single `.md` with frontmatter and multiple
`## <heuristic name>` sections — one per heuristic.

**Agent usage:** Two modes.
- **Embedded mode** — A lens's procedure cites a heuristic as one of its
  steps (e.g., ACH's "eliminate hypotheses" step cites Occam's Razor).
- **Sanity-gate mode** — A bundle is applied in the **sanity-gate** step as
  a final check on the top findings before synthesis.

Agents rarely consume a single heuristic directly; bundles are the
primary consumption unit.

---

## Agent workflow with 5 classes

The v0.2 workflow generalizes v0.1's three-step `triage → analyze →
synthesize` into a seven-step pipeline. Simple agents use only steps 1, 3,
and 7; richer agents enable the optional middle steps.

```
1. Triage          — read catalog.yml; select which items (of any class) apply
2. Classify        — apply FRAMES to sort the input            [optional]
3. Analyze         — apply LENSES in sequence                  [core]
4. Model-interpret — instantiate MODELS on input or findings   [optional]
5. Critical-read   — apply STANCES to surface hidden structures[optional]
6. Sanity-gate     — run HEURISTIC bundles as final checks     [optional]
7. Synthesize      — cross-check across all applied classes;
                     produce prioritized recommendations
```

The agent config YAML gets five optional item sections, each accepting the
same `usage: always | when-relevant | on-request` tag:

```yaml
lenses:      [...]
frames:      [...]
models:      [...]
stances:     [...]
heuristics:  [...]
```

v0.1 agent configs with only `lenses:` remain valid — the new sections are
additive.

---

## Converting other classes to lenses

A contributor often starts with a frame, model, or heuristic and wants a
lens. The conversion is not automatic: a lens requires all four criteria
the source may not supply.

**Frame → Lens.** The frame already gives you categories and
classification criteria. To promote it, add:
1. a defined input type
2. a step-by-step classification procedure (not just "sort by
   category — decide how")
3. an output format (which category, why, what follows from it)
4. a confidence signal on the classification

Document the result with `underlying_class: frame` so contributors know
the lens is an operationalization, not a native procedure.

**Model → Lens.** The model supplies variables, relationships, and
predictions. To promote it, add:
1. an Analytical Procedure that explicitly walks: map input → variables,
   fix parameters, read predictions, check boundary conditions
2. a structured output format
3. a confidence signal that reflects both boundary-condition fit and
   prediction strength

Document with `underlying_class: model`.

**Heuristic → Lens.** A single heuristic almost never becomes a lens on
its own — the result is usually trivial. If you need a "lens" in the
spirit of a heuristic, promote the underlying *decision problem* the
heuristic addresses (e.g., Occam's Razor → a lens for "selecting between
competing hypotheses" that enumerates assumptions, weights them, and
records confidence). The result is a lens that *uses* the heuristic, not
a heuristic that is now a lens.

Document with `underlying_class: heuristic`.

**Stance → Lens.** Don't. A stance expresses a commitment; forcing it
into a lens flattens exactly what makes it useful. Keep stances as
stances and run them in the `critical-read` step.

---

## Checklist before submitting a new item

- [ ] Picked the correct class using the table above.
- [ ] Used the matching file format template without renaming sections.
- [ ] Put the file in the correct directory
      (`library/lenses/<domain>/` / `library/frames/<domain>/` / `library/models/<domain>/` /
      `library/stances/<domain>/` / `library/heuristics/`).
- [ ] For a lens: `Analytical Procedure` is concrete enough to execute
      without prior knowledge of the framework; output format includes
      a confidence signal.
- [ ] Registered the item in `catalog.yml` under the right class section,
      with a `one_liner` specific enough to triage on.
- [ ] For a lens operationalized from another class, recorded
      `underlying_class` in both the file frontmatter and the catalog
      entry.
