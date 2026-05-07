# lenslab — Consolidated Design Document (v0.2 refactor)

---

> **Historical reference (v0.2 design phase)**
>
> This document captures the design conversation and candidate catalog
> that seeded the v0.3 batch generation. For the current library state
> and live catalog, see:
>
> - `catalog.yml` — authoritative triage index (auto-generated)
> - `library/` — actual framework files
> - `python3 scripts/sync_catalog.py --stats` — class/domain breakdown
> - `scripts/PHASE3_RUN.md` — batch generation pipeline
>
> §7 of this file (the 600-item seed catalog) should be treated as
> historical; do not modify it to reflect library state changes.

---

This document captures the full state of the lenslab project after the
v0.1 build and the subsequent design conversation. It is intended as:

1. A reference document for the project owner.
2. Input material for a Claude Code session that will execute the v0.2 refactor.
3. A source-of-truth for the 5-class taxonomy.

---

## 1. Project identity

**lenslab** is a Claude Code plugin for building domain-expert analysis agents
powered by structured analytical frameworks instead of vague persona prompts.

- GitHub: `97Wobbler/lenslab`
- Author: `97Wobbler`
- Version: `0.1.0` (current) → `0.2.0` (this refactor)

## 2. Core thesis

**Persona prompts change tone; lenses change reasoning.**

Telling an LLM "You are a senior security engineer" produces assertive-sounding
but shallow analysis. Real experts reason with structured frameworks — STRIDE,
Bloom's Taxonomy, Eisenhower Matrix, Retrosynthetic Analysis. These are the
procedures that force coverage, surface blind spots, and produce findings that
compare across reviews.

lenslab treats these frameworks as first-class reusable assets. Agents compose
them; they do not impersonate experts.

## 3. The definition of a "lens" (strict)

A **lens** must satisfy all four:

1. **Defined input type** — it specifies what kind of artifact it operates on
   (a DFD, an assessment item, a backlog, a proposal, etc.).
2. **Executable procedure** — numbered steps, a question set, or a matrix
   walk. "Apply this and results happen."
3. **Structured output format** — a fixed template (table, scored rubric,
   finding list), not free-form prose.
4. **Confidence evaluation** — each finding carries a confidence signal
   (solid / plausible / shaky, or high / medium / low).

If any of the four is missing, the artifact is **not a lens**. It may still be
valuable — but it belongs to one of the four sister classes below.

## 4. The 5-class taxonomy (v0.2 core change)

The v0.1 plugin treated everything as a "lens," which was imprecise. Many
valuable frameworks are not lenses in the strict sense — yet they are still
analytically powerful if used correctly. The v0.2 taxonomy gives each its own
class with its own file format and agent-usage pattern.

### Class 1 — Lens (렌즈)

**What it is:** A structured, executable analytical procedure satisfying all
four criteria above.

**Examples:** STRIDE, OWASP API Top 10, CVSS, Retrosynthetic Analysis, FMEA,
8D Problem Solving, SOAP + Differential Diagnosis, ACH (Analysis of Competing
Hypotheses), IRAC, Bloom's Taxonomy, Achievement Standard Alignment,
Pre-mortem, First Principles Thinking, Socratic Method.

**File format:** The current lens .md format. `Overview` + `Analytical
Procedure` + `Evaluation Criteria` + `Red Flags` + `Output Format`.

**Agent usage:** Applied directly in the `analyze` step. Each selected lens is
run in sequence; findings are collected per lens and tagged with confidence.

**Storage:** `library/lenses/<domain>/<name>.md`

---

### Class 2 — Frame (분류 프레임)

**What it is:** A taxonomy or classification matrix. Pure frames provide
categories and classification criteria but no execution procedure. They tell
you *how to sort*, not *what to do next*.

**Examples:** Cynefin (Simple/Complicated/Complex/Chaotic/Confused),
Kano Model (Must-be/One-dimensional/Attractive/Indifferent/Reverse),
BCG Growth-Share Matrix, Porter's Generic Strategies, Wardley Map axes,
Webb's Depth of Knowledge, CEFR language levels, MoSCoW.

**File format (proposed):**
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
<how to decide which category an instance belongs to — the minimum
procedure needed to make the frame usable>

## Implications per Category
<once classified, what does it mean? What should happen next?>

## Common Misclassifications
<border cases and typical errors>
```

**Agent usage:** Two modes.

- **Triage mode**: Use the frame BEFORE lenses to characterize the input. E.g.,
  "Is this a Complex or Complicated problem?" (Cynefin) → select different
  lens bundles based on classification.
- **Convert-to-lens mode**: Wrap a procedure around the frame to turn it into
  a lens. E.g., Cynefin + a procedure becomes "Cynefin Diagnostic Lens" that
  walks an input through the categories and returns a classification +
  implications + next-step recommendations.

**Storage:** `library/frames/<domain>/<name>.md`

---

### Class 3 — Model (이론 모델)

**What it is:** A descriptive or predictive theoretical model. Models explain
how some domain works; they're not procedures. But they can be *instantiated*
against a specific input to generate predictions, explanations, or lens
findings.

**Examples:** Prospect Theory (Kahneman/Tversky), Nash Equilibrium,
Porter's Five Forces, IS-LM, Solow Growth, Marcus Theory (electron transfer),
Noether's Theorem, Lotka-Volterra, Signaling Games, Principal-Agent,
Attachment Theory, Dual Process Theory, SAID Principle applied to training.

**File format (proposed):**
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
2. Identify values/parameters
3. Read off predictions
4. Check for boundary conditions that invalidate the model>

## Boundary Conditions
<when the model does NOT apply or breaks down>

## Output Format
<what applying the model to an input produces>
```

**Agent usage:** Models are instantiated during the `analyze` step as a
structured reference. The procedure in the file tells the agent how to map
the input onto the model's variables and extract predictions. A model
becomes a lens only when paired with a concrete application procedure;
without it, it is only a reference.

**Storage:** `library/models/<domain>/<name>.md`

---

### Class 4 — Stance (비판적 관점 / 해석적 입장)

**What it is:** An interpretive position or critical framework. Stances do
not have procedures or predictions — they have *commitments* about what is
worth looking for. They make certain things visible that other stances
ignore.

**Examples:** Marxist criticism (class, production relations, ideology),
Feminist criticism (gender, power, representation), Foucauldian Power/Knowledge
(discourse, subject production), Deconstruction (binary oppositions, margins),
Bourdieu's Habitus + Field + Capital, Postcolonial theory (Said, Spivak),
Thick Description (Geertz), Actor-Network Theory (Latour).

**File format (proposed):**
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
<the set of questions this stance asks of any artifact:
"Who speaks? Whose speech is treated as natural? What is occluded?"
etc. This is what replaces the Analytical Procedure of a lens.>

## What It Reveals
<the kinds of findings that only become visible through this stance>

## What It Obscures
<the blind spots — what this stance tends to miss or suppress>

## Output Format
<how to present findings made through this stance>
```

**Agent usage:** Stances are applied in a dedicated `critical-read` step of
the workflow (if the agent includes one). They operate on the same input as
lenses but with different questions. A stance file is not converted to a
lens — it operates in its own mode. Multiple stances can be applied to the
same input and their findings compared.

**Storage:** `library/stances/<domain>/<name>.md`

---

### Class 5 — Heuristic (원리 / 격언)

**What it is:** A single rule of thumb. A one-liner principle that sharpens
judgment in a specific situation. Heuristics are too small to be lenses, but
they function as checks inside or alongside lens-based analysis.

**Examples:** Occam's Razor, Hanlon's Razor, Chesterton's Fence,
Hickam's Dictum (as counterweight to Occam), SAID Principle, Pigeonhole
Principle, Parkinson's Law, 2-minute rule, Pareto 80/20, Mise en Place,
"Don't break the line" (Toyota Andon), "If you see one cockroach, there
are many" (debugging).

**File format (proposed):**
```markdown
---
name: <heuristic name>
domain: <...>
source: <...>
best_for: <when this heuristic is most useful>
---

# <heuristic name>

## The Rule
<one-sentence statement of the heuristic>

## When It Applies
<the situations where the rule sharpens judgment>

## When It Misleads
<situations where blindly applying the rule produces worse decisions>

## Common Misuse
<the typical failure modes>

## How Agents Use It
<either: as a check inside a lens's procedure, OR
as a sanity gate in the synthesize step>
```

**Agent usage:** Two modes.

- **Embedded mode**: A lens's procedure cites a heuristic as one of its
  steps. E.g., Occam's Razor is invoked in the ACH lens's "eliminate
  hypotheses" step.
- **Gate mode**: A bundle of heuristics is applied in the `synthesize` step
  as a final sanity check. E.g., "Before finalizing, run through Occam's,
  Hanlon's, Chesterton's, and Hickam's on each top finding."

Agents rarely consume a single heuristic directly. They're most useful
bundled: a "Decision Heuristics Bundle" or "Debugging Heuristics Bundle" as
one file per domain.

**Storage:** `library/heuristics/<domain>.md` (bundled) or
`library/heuristics/<domain>/<name>.md` (individual)

---

## 5. The v0.1 → v0.2 directory refactor

### Current (v0.1)

```
lenslab/
├── .claude-plugin/plugin.json
├── skills/agent-creator/SKILL.md
├── commands/create-agent.md
├── agents/examples/
│   ├── security-analyst.yml
│   └── curriculum-reviewer.yml
├── library/lenses/
│   ├── catalog.yml
│   ├── general/       (5 files)
│   ├── security/      (3 files)
│   └── education/     (3 files)
└── README.md
```

### Target (v0.2)

```
lenslab/
├── .claude-plugin/plugin.json          # version bump to 0.2.0
├── skills/agent-creator/SKILL.md       # updated workflow for 5 classes
├── commands/create-agent.md            # unchanged
├── agents/examples/                    # updated to reference multiple classes
│   ├── security-analyst.yml
│   └── curriculum-reviewer.yml
├── library/lenses/
│   ├── general/       # only the true lenses stay here
│   ├── security/
│   └── education/
├── library/frames/            # NEW
│   └── general/
├── library/models/            # NEW
│   └── general/
├── library/stances/           # NEW
│   └── general/
├── library/heuristics/        # NEW
│   └── general.md     # bundled general-purpose heuristics
├── catalog.yml        # MOVED to top level; adds `class` field
├── CLASSES.md         # NEW — the 5-class taxonomy spec
└── README.md          # updated to explain the 5 classes
```

### Reclassification of existing 12 files

All 12 v0.1 files were written with explicit procedures, so they all
technically qualify as **lenses** (procedural forms of underlying frames or
heuristics). The refactor keeps them all as lenses but documents their
underlying class in the frontmatter so contributors understand the pattern.

| v0.1 file | v0.2 location | Underlying class | Notes |
|---|---|---|---|
| library/lenses/general/rumsfeld-matrix.md | library/lenses/general/rumsfeld-matrix.md | lens (from frame) | Frame = Known/Unknown 2×2; this file adds the proxy generation procedure |
| library/lenses/general/eisenhower-matrix.md | library/lenses/general/eisenhower-matrix.md | lens (from frame) | Frame = Urgent/Important 2×2; procedure added |
| library/lenses/general/occams-razor.md | library/lenses/general/occams-razor.md | lens (from heuristic) | Heuristic = "prefer fewer assumptions"; file adds enumeration + typing + weighting procedure |
| library/lenses/general/first-principles.md | library/lenses/general/first-principles.md | lens | Native procedure |
| library/lenses/general/socratic-method.md | library/lenses/general/socratic-method.md | lens | Native procedure (6-category question walk) |
| library/lenses/security/stride.md | library/lenses/security/stride.md | lens | Native procedure |
| library/lenses/security/owasp-top10.md | library/lenses/security/owasp-top10.md | lens | Native procedure |
| library/lenses/security/cvss-scoring.md | library/lenses/security/cvss-scoring.md | lens (from model) | Model = 8 Base Metrics; procedure adds mapping + scoring steps |
| library/lenses/education/blooms-taxonomy.md | library/lenses/education/blooms-taxonomy.md | lens (from frame) | Frame = 6 cognitive levels; procedure adds classification + distribution check |
| library/lenses/education/achievement-standard-alignment.md | library/lenses/education/achievement-standard-alignment.md | lens | Native procedure |
| library/lenses/education/cognitive-load-theory.md | library/lenses/education/cognitive-load-theory.md | lens (from model) | Model = 3 load types + working memory cap; procedure adds element counting + check sequence |

Add new frontmatter field `underlying_class` to each file: `frame | model | stance | heuristic | native`. This documents whether the lens is a native procedure or an operationalization of another class.

### Starter files for each new class (v0.2)

For the new directories to be meaningful at launch, ship at least 1-2 starter
files per new class:

- **library/frames/general/cynefin.md** — Simple/Complicated/Complex/Chaotic/Confused
  with classification criteria and category implications (without forcing a
  lens procedure).
- **library/frames/general/kano-model.md** — Must-be/One-dimensional/Attractive/
  Indifferent/Reverse category definitions.
- **library/models/economics/prospect-theory.md** — Reference point, loss aversion,
  probability weighting variables + application procedure.
- **library/models/strategy/porters-five-forces.md** — 5 forces as model variables +
  application procedure for a specific industry.
- **library/stances/humanities/marxist-criticism.md** — Foundational commitments,
  guiding questions, what it reveals/obscures.
- **library/stances/humanities/foucauldian-power-knowledge.md** — Discourse,
  subject production, visibility of the "natural."
- **library/heuristics/general.md** — Bundled: Occam's, Hanlon's, Chesterton's Fence,
  Hickam's Dictum, Pigeonhole, Parkinson's, Mise en Place.

## 6. Updated agent workflow

The v0.1 workflow is `triage → analyze → synthesize`. The v0.2 workflow
adds optional class-specific steps:

```
1. Triage          — read catalog.yml; select which lenses / frames / models
                     / stances / heuristics apply
2. Classify        — apply FRAMES to sort the input (optional, if frames selected)
3. Analyze         — apply LENSES in sequence (core step)
4. Model-interpret — instantiate MODELS on findings (optional, if models selected)
5. Critical-read   — apply STANCES to surface hidden structures (optional)
6. Sanity-gate     — run HEURISTICS as final checks (optional)
7. Synthesize      — cross-check across all applied classes; produce
                     prioritized recommendations
```

Simple agents use only steps 1, 3, 7. Richer agents enable the optional
steps. The agent config YAML gets new fields:

```yaml
lenses:      [...]
frames:      [...]
models:      [...]
stances:     [...]
heuristics:  [...]
```

Each with the same `usage` field (`always | when-relevant | on-request`).

## 7. The 600-item catalog

The following catalog was assembled during the v0.2 design conversation. Each
entry is tagged with its natural class (L / F / M / S / H) and its domain.
This is a reference, NOT a plan to create 600 files. The agent-creator skill
references this catalog when it needs to generate a new lens — most items
require operationalization work before becoming lens files.

Format: `[class] name — one-liner`

### General / Meta

- [L] First Principles Thinking — decompose to irreducible requirements, rebuild from scratch, compare delta with default
- [L] Socratic Method — 6 question categories stress-test a claim
- [L] Rumsfeld Matrix — Known/Unknown 2×2 + proxy techniques to surface Unknown Unknowns
- [L] Eisenhower Matrix — Urgent/Important 2×2 triage with distribution health check
- [L] Pre-mortem (Klein) — assume failure, work backward to causes
- [F] Cynefin (Snowden) — Simple/Complicated/Complex/Chaotic/Confused problem classification
- [F] 2×2 Matrix (generic) — any orthogonal-dimension sort
- [H] Occam's Razor — prefer explanations with fewer assumptions
- [H] Hanlon's Razor — don't attribute to malice what stupidity explains
- [H] Chesterton's Fence — don't remove a rule until you know why it exists
- [H] Pareto 80/20 — 20% of input causes 80% of output
- [H] Parkinson's Law — work expands to fill the time available
- [H] Pigeonhole Principle — more items than bins means at least one bin has ≥2

### Brainstorming / Ideation

- [L] SCAMPER — Substitute/Combine/Adapt/Modify/Put to other use/Eliminate/Reverse
- [L] Six Thinking Hats (de Bono) — sequential 6-role review
- [L] Disney Method — Dreamer/Realist/Critic cycle
- [L] Brainwriting 6-3-5 — silent parallel writing structure
- [L] Crazy 8s (GV) — 8 sketches in 8 minutes
- [L] Reverse Brainstorming — worsen the problem to discover causes
- [L] Worst Possible Idea — inversion to extract quality attributes
- [L] Morphological Analysis (Zwicky) — dimension × value combinatorial grid
- [S] Lateral Thinking (de Bono) — provocative operations, random entry
- [H] Random Stimulus — force an unrelated input into the problem

### Information Analysis / Intelligence

- [L] ACH (Analysis of Competing Hypotheses, Heuer) — hypothesis × evidence inconsistency matrix
- [L] Key Assumptions Check — enumerate tacit assumptions
- [L] Devil's Advocacy — structured opposition
- [L] Red Team Analysis — adversary-perspective attack on own plan
- [L] Indicators & Warnings — pre-define observable precursors
- [L] Argument Mapping — visual claim/premise/rebuttal tree
- [F] PMESII-PT — 8-dimension situational analysis
- [F] DIME — 4 instruments of national power
- [M] Bayesian Reasoning — prior × likelihood → posterior
- [S] Critical Geopolitics — power/space/discourse lens on geography

### Security / Threat Modeling

- [L] STRIDE — element × 6 threat categories walk
- [L] OWASP API Top 10 — endpoint-by-endpoint 10-category check
- [L] CVSS v3.1 — 8 Base Metrics severity scoring
- [L] PASTA — 7-stage attack simulation threat model
- [L] DREAD — 5-factor risk rating
- [L] Attack Trees (Schneier) — AND/OR tree of attack paths
- [L] Kill Chain (Lockheed Martin) — Recon→Actions 7-phase attack model
- [L] Diamond Model — Adversary/Capability/Infrastructure/Victim intrusion analysis
- [L] HAZOP — parameter × guideword hazard review
- [L] FMEA — Failure Mode × Severity × Occurrence × Detection = RPN
- [F] MITRE ATT&CK — adversary TTP matrix
- [F] NIST CSF — Identify/Protect/Detect/Respond/Recover maturity
- [M] FAIR — risk as frequency × magnitude factor model
- [M] Zero Trust Architecture (NIST SP 800-207) — never-trust principle as system model

### Strategy / Market Analysis

- [M] Porter's Five Forces — industry attractiveness 5-force model
- [L] SWOT — 4-quadrant internal/external scan
- [F] PESTEL — 6-factor macro environment
- [F] BCG Growth-Share Matrix — growth × share 2×2 portfolio
- [F] Ansoff Matrix — market × product 2×2 growth strategy
- [L] Blue Ocean ERRC Grid — Eliminate/Reduce/Raise/Create
- [L] Value Chain Analysis (Porter) — activity-by-activity margin contribution
- [L] Business Model Canvas — 9-block business visualization
- [L] Value Proposition Canvas — Jobs/Pains/Gains ↔ Features/Relievers/Creators
- [F] Wardley Map — value chain × evolution stage
- [F] Three Horizons (McKinsey) — H1/H2/H3 investment split
- [M] Jobs-to-be-Done — what job does the customer "hire" the product for
- [M] Disruption Theory (Christensen) — low-end/new-market disruption patterns
- [F] Kano Model — 5 feature categories by customer satisfaction
- [L] 5C Analysis — Company/Customers/Competitors/Collaborators/Context scan

### Product Management

- [L] RICE Scoring — Reach × Impact × Confidence ÷ Effort
- [L] ICE Scoring — Impact × Confidence × Ease
- [F] MoSCoW — Must/Should/Could/Won't
- [L] Opportunity Scoring (Ulwick ODI) — importance − satisfaction gap
- [L] North Star Framework — single metric + contributing inputs
- [L] HEART Metrics (Google) — Happiness/Engagement/Adoption/Retention/Task success
- [L] AARRR Pirate Metrics — Acquisition/Activation/Retention/Referral/Revenue
- [L] Double Diamond — Discover/Define/Develop/Deliver
- [L] Impact Mapping (Adzic) — Why→Who→How→What tree
- [L] Story Mapping (Patton) — journey × priority grid
- [L] Working Backwards / PR-FAQ (Amazon) — write the press release first
- [H] Product-Market Fit (Sean Ellis 40% rule) — "very disappointed" survey threshold
- [M] Hooked Model (Eyal) — Trigger/Action/Variable Reward/Investment loop
- [L] Dual-Track Agile (Cagan) — Discovery and Delivery parallel tracks

### Agile / Engineering

- [L] Scrum ceremonies — sprint/backlog/standup/review/retro
- [L] Kanban (WIP, CFD, Little's Law) — flow-based work management
- [L] Shape Up (Basecamp) — 6-week bets with appetite scoping
- [L] DORA Metrics — deployment freq / lead time / MTTR / change failure rate
- [L] SPACE Framework — developer productivity 5-axis
- [F] Team Topologies — Stream/Platform/Complicated-subsystem/Enabling 4 team types
- [M] Domain-Driven Design — Bounded Context, Ubiquitous Language, Aggregate
- [L] Event Storming (Brandolini) — domain event post-it workshop
- [L] C4 Model — Context/Container/Component/Code architecture diagrams
- [H] 12-Factor App — cloud-native 12 principles
- [H] SOLID Principles — OOP design 5 rules
- [H] Conway's Law — org structure determines system structure
- [L] WSJF (SAFe) — Cost of Delay ÷ Job Size prioritization

### OKR / Goal Management

- [L] OKRs (Doerr) — Objective + 3-5 Key Results
- [H] CFRs — Conversations/Feedback/Recognition operational rituals
- [L] V2MOM (Salesforce) — Vision/Values/Methods/Obstacles/Measures
- [L] Balanced Scorecard — 4-perspective KPI system
- [L] Hoshin Kanri — X-Matrix policy deployment
- [H] SMART Goals — Specific/Measurable/Achievable/Relevant/Time-bound
- [H] FAST Goals (Sull) — Frequent/Ambitious/Specific/Transparent
- [M] Goal-Setting Theory (Locke/Latham) — specificity + difficulty drive performance
- [L] KPI Tree — top KPI decomposition

### Marketing

- [F] 4P / 7P Marketing Mix — Product/Price/Place/Promotion (+People/Process/Physical)
- [L] STP — Segmentation/Targeting/Positioning
- [L] Customer Journey Map — awareness→advocacy touchpoints
- [L] AIDA — Attention/Interest/Desire/Action
- [L] PAS — Problem/Agitate/Solution
- [L] FAB — Features/Advantages/Benefits
- [L] RACE (Smart Insights) — Reach/Act/Convert/Engage
- [L] SOSTAC (PR Smith) — Situation/Objectives/Strategy/Tactics/Action/Control
- [M] Growth Loops — output-as-input feedback design
- [L] NPS / CES / CSAT — 3 customer sentiment metrics
- [L] 5A (Kotler) — Aware/Appeal/Ask/Act/Advocate
- [L] Empathy Map — Think/Feel/See/Hear/Say/Do

### Education

- [L] Bloom's Taxonomy (Revised) — Remember→Create 6-level cognitive classification
- [L] Achievement Standard Alignment (한국 교육과정) — content × skill × cognitive level
- [L] Cognitive Load Theory (Sweller) — intrinsic/extraneous/germane load diagnosis
- [L] Backward Design (UbD, Wiggins/McTighe) — goal→assessment→instruction
- [L] ADDIE — Analyze/Design/Develop/Implement/Evaluate
- [L] Kirkpatrick 4 Levels — Reaction/Learning/Behavior/Results
- [L] Gagne's 9 Events of Instruction
- [L] Merrill's First Principles of Instruction
- [L] 5E Model — Engage/Explore/Explain/Elaborate/Evaluate
- [M] ZPD (Vygotsky) — zone of proximal development
- [F] Webb's Depth of Knowledge (DOK) — 4-level alternative to Bloom's
- [L] Universal Design for Learning (UDL) — representation/engagement/expression
- [F] SAMR Model — Substitution/Augmentation/Modification/Redefinition
- [F] TPACK — technological/pedagogical/content knowledge intersection
- [H] Retrieval Practice — active recall beats re-reading
- [H] Spaced Repetition — distributed practice > massed
- [M] Dual Coding Theory (Paivio) — verbal + visual encoding

### Productivity

- [L] GTD (Allen) — Capture/Clarify/Organize/Reflect/Engage
- [H] Pomodoro — 25+5 rhythm
- [S] Deep Work (Newport) — deep/shallow classification stance
- [L] Time Blocking — calendar-based intentional scheduling
- [L] PARA (Forte) — Projects/Areas/Resources/Archives
- [L] Second Brain CODE — Capture/Organize/Distill/Express
- [L] Zettelkasten (Luhmann) — atomic linked notes
- [L] Ivy Lee Method — daily 6 tasks prioritized
- [L] Bullet Journal — rapid logging + migration
- [H] 2-minute rule — execute if under 2 min
- [L] MITs — daily 3 most important tasks
- [L] Flowtime Technique — uninterrupted-until-done alternative to Pomodoro
- [H] Task Batching — similar-task grouping to reduce context switching
- [H] Theme Days (Dorsey) — day-level role specialization
- [H] Eat That Frog (Tracy) — hardest task first
- [L] Energy Management (Schwartz/Loehr) — body/emotion/mind/spirit
- [H] Ultradian Rhythms — 90-120 min cycles
- [H] Attention Residue (Leroy) — post-switch cognitive cost
- [S] Digital Minimalism (Newport) — value-aligned tech use stance
- [H] Maker's vs Manager's Schedule (PG) — 4-hour blocks vs 1-hour meetings

### Decision / Leadership

- [L] OODA Loop (Boyd) — Observe/Orient/Decide/Act
- [F] Cynefin — Simple/Complicated/Complex/Chaotic context classification
- [L] RAPID (Bain) — Recommend/Agree/Perform/Input/Decide
- [L] DACI — Driver/Approver/Contributors/Informed
- [L] RACI — Responsible/Accountable/Consulted/Informed
- [L] Pre-mortem (Klein) — failure imagination
- [M] Expected Value — probability-weighted outcome computation
- [F] Tuckman's Stages — Forming/Storming/Norming/Performing
- [F] Lencioni's 5 Dysfunctions — trust-absence pyramid
- [F] Situational Leadership (Hersey-Blanchard) — maturity-based style
- [F] Radical Candor (Scott) — Care × Challenge 2×2
- [M] Growth vs Fixed Mindset (Dweck) — belief model

### Operations / Process Improvement

- [H] Lean Waste (TIMWOODS) — 8 wastes
- [L] Six Sigma DMAIC — Define/Measure/Analyze/Improve/Control
- [L] Theory of Constraints (Goldratt) — identify/exploit/subordinate/elevate bottleneck
- [L] 5 Whys — iterative cause drilling
- [L] Ishikawa (Fishbone) — 6M cause classification
- [L] PDCA — Plan/Do/Check/Act
- [L] Value Stream Mapping — material/info flow visualization
- [H] Poka-yoke — mistake-proofing
- [L] A3 Problem Solving — one-page structured reporting
- [S] Toyota Kata — habit-of-improvement stance

### Data / Research

- [L] CRISP-DM — data science process
- [L] OSEMN — Obtain/Scrub/Explore/Model/iNterpret
- [L] Bradford Hill Criteria — 9 causation inference criteria
- [L] A/B Testing Principles — power/MDE/sequential/peeking
- [L] Cohort Analysis — time/trait cohort tracking
- [H] Bias Taxonomy — selection/survivorship/confirmation/recall/publication
- [M] Causal DAG (Pearl) — confounder identification via graph
- [L] Difference-in-Differences — quasi-experimental causal inference
- [L] PRISMA — systematic review reporting
- [L] GRADE — evidence quality grading

### UX / Design

- [L] Nielsen's 10 Heuristics — usability evaluation
- [L] Cognitive Walkthrough — new-user task simulation
- [L] Service Blueprint — customer/front/back/support 4-layer
- [L] Affinity Diagram — qualitative data clustering
- [M] Fitts's Law — target size × distance → time
- [M] Hick's Law — choice count → log(decision time)
- [M] Miller's Law (7±2) — working memory capacity
- [M] Gestalt Principles — proximity/similarity/closure/continuity

### Finance / Investment

- [L] DCF — discounted cash flow valuation
- [L] DuPont Analysis — ROE decomposition
- [M] Unit Economics (LTV/CAC) — lifetime value ÷ acquisition cost
- [M] SaaS Metrics — MRR/ARR/Net Retention/Rule of 40
- [L] Moat Analysis (Buffett) — structural competitive advantage
- [H] Margin of Safety (Graham) — price vs intrinsic value buffer

### Communication / Writing

- [L] Pyramid Principle (Minto) — top-down conclusion-first structure
- [H] BLUF — Bottom Line Up Front
- [L] STAR — Situation/Task/Action/Result
- [L] Inverted Pyramid — most-important-first (journalism)
- [H] Rule of Three — 3-item grouping for memorability

### Sports / Athletic Performance

- [L] Periodization (Matveyev) — macro/meso/microcycle training plan
- [L] Conjugate Method (Westside) — parallel max-strength/dynamic/rep work
- [L] Tactical Periodization (Frade) — game model–centered training design
- [F] Four Moments of Football — attack/defend/transition × 2
- [H] SAID Principle — specific adaptation to imposed demands
- [H] Progressive Overload — incremental stress → adaptation
- [M] GAS (Selye) — Alarm/Resistance/Exhaustion stress response
- [L] RPE/RIR — subjective intensity management
- [H] FITT Principle — Frequency/Intensity/Time/Type
- [F] Heart Rate Zones — 5-zone energy system targeting
- [L] LTAD (Balyi) — 7-stage long-term athlete development
- [L] FIFA 11+ / RAMP — injury prevention warmup
- [L] Sabermetrics — context-adjusted baseball stats
- [M] Expected Goals (xG) — shot quality probability model
- [M] IZOF (Hanin) — individual optimal arousal zone
- [M] Flow (Csikszentmihalyi) — challenge-skill balance model
- [M] Self-Determination Theory — autonomy/competence/relatedness motivation

### Meta-science / Philosophy of Science / Epistemology

- [S] Popper's Falsificationism — science requires falsifiable claims
- [S] Kuhn's Paradigm Framework — normal/crisis/revolution
- [S] Lakatos's Research Programmes — hard core + protective belt
- [M] Inference to the Best Explanation — explanation selection method
- [L] Hypothetico-Deductive Method — hypothesis→prediction→observation
- [M] Bayesian Epistemology — belief as probability
- [S] Duhem-Quine Thesis — holistic confirmation
- [S] Merton's CUDOS — norms of science
- [S] Gettier Problem — JTB analysis
- [L] Open Science Practices — preregistration/open data/etc
- [L] Meta-analysis (Cochrane) — weighted effect size combination
- [F] Levels of Evidence Pyramid — case→meta hierarchy
- [H] Cohen's d — effect size interpretation
- [L] Bibliometric Analysis — h-index, citation network
- [H] Hempel's Raven Paradox — confirmation logic puzzle
- [H] Underdetermination — multiple theories fit the same data

### Personal Knowledge Management (PKM)

- [L] Zettelkasten — atomic notes + links
- [L] PARA — 4-folder organization
- [L] CODE — Second Brain workflow
- [S] Evergreen Notes (Matuschak) — atomic + concept-oriented stance
- [L] LYT / Maps of Content (Milo) — hub-based note navigation
- [L] Progressive Summarization (Forte) — bold→highlight→summary→expression
- [L] Commonplace Book (Locke) — indexed excerpt collection
- [S] Digital Garden — public-in-progress stance
- [L] Feynman Technique — teach-to-a-child cycle
- [L] Cornell Note-Taking — 3-zone page structure
- [L] SQ3R / PQ4R — structured reading method
- [H] Active Recall — retrieval over re-reading
- [H] Spaced Repetition — Leitner/Anki scheduling
- [L] Incremental Reading (SuperMemo) — interleaved chunked reading
- [H] Atomic Notes Principle — one idea per note

### AI / ML / LLM

- [L] CRISP-DM — data science process
- [L] ML Test Score (Breck) — 28-test production ML checklist
- [F] MLOps Maturity Model — level 0-2 deployment automation
- [L] Model Cards (Mitchell) — model documentation template
- [L] Datasheets for Datasets (Gebru) — dataset documentation template
- [F] NIST AI RMF — Govern/Map/Measure/Manage
- [H] AI Fairness Metrics — demographic parity / equal opportunity / equalized odds
- [L] SHAP/LIME — local interpretability methods
- [L] Confusion Matrix + P/R/F1 — classification evaluation
- [L] ROC/PR Curves — threshold-independent evaluation
- [M] Scaling Laws (Chinchilla, Kaplan) — model/data/compute power law
- [L] Chain-of-Thought Prompting — explicit reasoning step generation
- [L] RAG — retrieval-augmented generation pattern
- [S] Constitutional AI — natural-language principle alignment stance
- [L] RLHF / DPO — preference-based training
- [L] Red-Teaming LLMs — adversarial probing
- [L] Eval Harness Frameworks — HELM/BIG-bench/lm-eval
- [F] Prompt Taxonomy — zero-shot/few-shot/CoT/ReAct/self-consistency
- [L] Causal DAG for ML — confounder check
- [F] Drift Detection — covariate/label/concept drift

### NLP (Neuro-Linguistic Programming, communication)

- [F] Representational Systems (VAK) — visual/auditory/kinesthetic modality
- [L] Meta Model — generalization/deletion/distortion question probes
- [L] Milton Model — hypnotic ambiguous language patterns
- [L] Well-Formed Outcomes — 5-condition goal specification
- [L] Rapport Building (Pacing & Leading) — mirror and lead
- [L] Anchoring — state-stimulus association
- [L] Reframing — context/content meaning shift
- [L] Perceptual Positions — 1st/2nd/3rd person shifts
- [F] Neurological Levels (Dilts) — environment→identity hierarchy
- [L] SCORE Model — Symptoms/Causes/Outcome/Resources/Effects

### Game Theory

- [M] Prisoner's Dilemma — canonical non-cooperative dilemma
- [M] Nash Equilibrium — no unilateral deviation improves
- [M] Dominant Strategy — always-best regardless of opponent
- [M] Minimax / Maximin — worst-case optimization
- [M] Mixed Strategy Equilibrium — probabilistic strategies
- [M] Pareto Optimality — no improvement without harm
- [M] Tit-for-Tat (Axelrod) — cooperate then mimic
- [M] Evolutionary Stable Strategy (Maynard Smith) — invasion-resistant strategies
- [M] Stackelberg — leader-follower sequential game
- [M] Cournot / Bertrand — quantity vs price competition
- [M] Bayesian Games (Harsanyi) — incomplete information games
- [M] Signaling Games (Spence) — costly-signal equilibria
- [M] Principal-Agent — incentive alignment problem
- [M] Mechanism Design — rules-to-induce-outcome engineering
- [M] Auction Theory — first/second/Vickrey formats
- [M] Shapley Value — cooperative game fair contribution
- [M] Chicken Game — mutual-escalation deadlock
- [M] Commitment Devices (Schelling) — self-limiting for bargaining leverage

### Manufacturing / Process Engineering

- [S] Toyota Production System — Jidoka + JIT philosophy
- [L] SMED (Shingo) — setup time reduction methodology
- [H] Heijunka — production leveling
- [L] Andon System — visual signal for line stop
- [L] OEE — Availability × Performance × Quality
- [L] Takt Time / Cycle Time / Lead Time — rhythm/cycle/total time
- [L] DFMA — Design for Manufacturing & Assembly
- [L] DFSS (DMADV) — design for Six Sigma
- [L] FMEA — failure mode × severity × occurrence × detection
- [L] Fault Tree Analysis (FTA) — AND/OR logical failure decomposition
- [L] HAZOP — parameter × guideword hazard review
- [L] SPC — statistical process control charts
- [M] Process Capability (Cp, Cpk) — spec margin quantification
- [L] MSA — measurement system R&R analysis
- [L] APQP / PPAP — automotive quality planning protocol
- [L] 8D Problem Solving (Ford) — 8-step structured CAPA
- [L] Quality Function Deployment / House of Quality — customer → engineering translation
- [M] Taguchi Robust Design — noise-tolerant parameter design
- [L] TRIZ (Altshuller) — 40 inventive principles × contradiction matrix
- [M] Axiomatic Design (Suh) — Independence + Information axioms

### Negotiation

- [L] BATNA (Fisher/Ury) — best alternative as leverage
- [L] ZOPA — zone of possible agreement
- [L] Getting to Yes (Harvard) — people/interests/options/criteria
- [L] Tactical Empathy (Voss) — labeling/mirroring/calibrated questions
- [H] Anchoring in Negotiation — first offer effect
- [F] Integrative vs Distributive Bargaining — expand vs divide

### Storytelling / Narrative

- [F] Hero's Journey (Campbell) — 12-stage monomyth
- [L] Save the Cat Beat Sheet (Snyder) — 15-beat screenplay structure
- [F] Three-Act Structure — setup/confrontation/resolution
- [F] Freytag's Pyramid — exposition/rising/climax/falling/denouement
- [L] Dan Harmon's Story Circle — 8-step Campbell simplification
- [L] Pixar Formula — "Once upon a time... / One day... / Because of that..."
- [F] Kishōtenketsu (기승전결) — East Asian 4-act non-conflict structure

### Architecture / Systems Philosophy

- [S] Pattern Language (Alexander) — reusable pattern stance
- [H] Form Follows Function (Sullivan) — function-as-origin principle
- [H] Vitruvian Triad — firmitas/utilitas/venustas
- [H] Worse is Better (Gabriel) — simple-and-shipping beats perfect-and-late

### Theology / Religious Studies

- [L] Four Senses of Scripture — literal/allegorical/moral/anagogical
- [L] PaRDeS — Peshat/Remez/Derash/Sod Torah interpretation
- [L] Historical-Critical Method — textual→source→form→redaction sequence
- [L] Form Criticism — literary form + Sitz im Leben
- [L] Lectio Divina — lectio/meditatio/oratio/contemplatio
- [F] Wesleyan Quadrilateral — Scripture/Tradition/Reason/Experience
- [S] Via Negativa — apophatic stance
- [F] Theodicy Frameworks — Augustinian/Irenaean/Process/Free-will
- [F] Smart's Seven Dimensions of Religion — doctrinal/mythic/ethical/ritual/experiential/institutional/material
- [S] Eliade's Sacred/Profane — phenomenological religion stance
- [S] Otto's Numinous — Mysterium Tremendum et Fascinans
- [L] Liberation Theology Method — See/Judge/Act
- [F] Usul al-Fiqh — Quran/Sunnah/Ijma/Qiyas legal sources
- [M] Kalam/Cosmological/Ontological/Teleological Arguments — 4 classical God-existence arguments
- [F] Axial Age Framework (Jaspers) — BCE 800-200 comparative analysis
- [L] Four Noble Truths + Eightfold Path — diagnostic→prescription

### Law

- [L] IRAC / CREAC / FIRAC — Issue/Rule/Application/Conclusion argument format
- [L] Case Briefing — Facts/Posture/Issue/Holding/Reasoning extraction
- [L] Elements-Based Analysis — cause of action element-by-element proof
- [L] Tort Analysis — Duty/Breach/Causation/Damages
- [L] Contract Analysis — Offer/Acceptance/Consideration/Assent/Capacity/Legality
- [L] Criminal Liability — Actus Reus/Mens Rea/Concurrence/Causation/Harm
- [L] Balancing Tests — Strict/Intermediate/Rational Basis scrutiny
- [L] Mathews v. Eldridge Balancing — procedural due process test
- [L] Statutory Interpretation Canons — ejusdem generis etc.
- [S] Textualism/Originalism/Purposivism/Living Constitutionalism — 4 interpretive stances
- [L] Chevron Two-Step — ambiguity + reasonableness review
- [L] 4-Factor Fair Use Test — purpose/nature/amount/market
- [L] Polaroid 8 Factors (Trademark) — likelihood of confusion factors
- [M] Dworkin's Principles vs Rules — dual-norm structure
- [S] Legal Realism vs Formalism — interpretive stances
- [S] Law and Economics (Posner) — efficiency lens
- [S] Critical Legal Studies — power-ideology stance
- [F] Just War Theory — jus ad bellum / in bello / post bellum

### Medicine / Clinical Reasoning

- [L] SOAP Notes — Subjective/Objective/Assessment/Plan
- [L] Differential Diagnosis — enumerate → narrow by likelihood × severity
- [F] VINDICATE Mnemonic — Vascular/Infectious/... cause category checklist
- [H] Occam's Razor vs Hickam's Dictum — parsimony vs multi-disease tension
- [M] Bayesian Clinical Reasoning — pretest × LR = posttest
- [M] NNT — number needed to treat
- [F] USPSTF Grade Recommendations — A/B/C/D/I evidence grading
- [L] Clinical Decision Rules — Wells/CURB-65/Ottawa scoring
- [F] Red Flags Screening — warning-sign checklist
- [L] ABCDE Approach — emergency triage sequence
- [S] Dual Process Theory in Medicine (Croskerry) — System 1/2 stance
- [L] Cognitive Forcing Strategies (Croskerry) — debiasing procedures
- [L] Illness Scripts — time × symptoms × risk × pathophysiology templates
- [F] EBM Hierarchy — case/cohort/RCT/review/meta evidence pyramid
- [M] Biopsychosocial Model (Engel) — 3-domain health model
- [F] ICF — functioning/activity/participation × environment

### Architecture (Physical)

- [H] Vitruvian Triad — firmitas/utilitas/venustas
- [L] Parti Diagram — conceptual organization sketch
- [L] Site Analysis — context/climate/circulation/views etc.
- [L] Program Analysis — functional requirements + adjacencies + areas
- [L] Figure-Ground / Nolli Map — building-void urban reversal
- [S] Pattern Language (Alexander) — 253 patterns across scales
- [S] Genius Loci (Norberg-Schulz) — place-phenomenology stance
- [L] Space Syntax (Hillier) — graph-based spatial analysis
- [L] CPTED — crime prevention through environmental design
- [F] Universal Design 7 Principles — equitable/flexible/simple/etc
- [F] Biophilic Design 14 Patterns — nature-connection evidence-based patterns
- [F] Passive House Principles — airtightness/insulation/heat recovery/etc
- [L] Massing Study — volume-block functional analysis
- [F] Typology Analysis (Rossi) — historical urban type analysis
- [S] Critical Regionalism (Frampton) — place-resistance stance
- [F] LEED/BREEAM/WELL — green building certification systems

### Music Theory

- [L] Roman Numeral Analysis — functional harmony notation
- [F] Functional Harmony (T-S-D) — tonic/subdominant/dominant categorization
- [L] Voice Leading Rules — counterpoint line-management rules
- [L] Species Counterpoint (Fux) — 5-species training framework
- [L] Schenkerian Analysis — Ursatz-level structural reduction
- [L] Sonata Form Analysis — exposition/development/recapitulation
- [F] Form Analysis — binary/ternary/rondo/through-composed
- [L] Motivic Analysis — thematic development tracking
- [L] Set Theory (Forte) — atonal pitch-class set analysis
- [L] Neo-Riemannian Theory — P/L/R transformations
- [L] GTTM (Lerdahl/Jackendoff) — 4-layer tonal music analysis
- [L] Spectromorphology (Smalley) — electroacoustic analysis language
- [F] Mode Analysis — church modes and modal music
- [L] Rhythmic Analysis — meter + grouping tension
- [F] Tonnetz — chord-distance 3D lattice

### Film Theory

- [L] Mise-en-scène Analysis — frame-content intentional reading
- [L] Cinematography Analysis — framing/lens/movement/lighting/color
- [L] Editing Analysis — cut types and their function
- [L] Sound Analysis — diegetic/non-diegetic + bridges
- [F] Eisenstein's 5 Types of Montage — metric/rhythmic/tonal/overtonal/intellectual
- [H] Kuleshov Effect — meaning from juxtaposition
- [L] Bordwell's Formal Analysis — narration/style/form/meaning
- [S] Auteur Theory — director-as-author stance
- [S] Mulvey's Male Gaze — feminist film stance
- [S] Deleuze's Movement-Image / Time-Image — cinema-as-philosophy stance
- [F] Metz's Grande Syntagmatique — 8 sequence types
- [F] Genre Theory — repetition-and-difference analysis
- [H] 180-Degree Rule — continuity editing principle
- [L] McKee's Story Structure — inciting incident → resolution

### Cooking / Culinary

- [F] Mother Sauces (Escoffier) — 5 base sauces for derivative classification
- [H] Mise en Place — total prep before execution
- [F] 5 Tastes + Umami Synergy — glutamate × nucleotide potentiation
- [M] Maillard Reaction — non-enzymatic browning chemistry
- [M] Heat Transfer Modes — conduction/convection/radiation
- [L] Salt Fat Acid Heat (Nosrat) — 4-element flavor diagnosis
- [L] Baker's Percentage — flour-base ratio formulation
- [L] Ruhlman's Ratios — ratio-not-recipe principle
- [M] Emulsion Theory — disperse-phase stabilization
- [L] Fermentation Frameworks — substrate × organism × environment × time
- [S] McGee Food Science — reductionist culinary stance
- [L] Flavor Pairing (Flavor Bible) — ingredient affinity database
- [L] Thai Flavor Balance — 5-axis taste check
- [L] Kaiseki/Omakase Structure — seasonality + technique + ingredient sequence
- [L] Sensory Evaluation — triangle test / descriptive / hedonic
- [L] Plating Principles — height/color/rhythm/whitespace/focal point

### Military Strategy

- [S] Sun Tzu Principles — know-self-and-enemy stance
- [M] Clausewitz's Trinity — government/army/people 3-body model
- [L] Center of Gravity Analysis — critical-source identification
- [L] Warden's Five Rings — leadership/processes/infrastructure/population/forces
- [L] OODA Loop (Boyd) — Observe/Orient/Decide/Act
- [H] Principles of War — 9-element doctrine
- [F] Maneuver vs Attrition Warfare — 2 strategic paradigms
- [L] METT-TC — mission/enemy/terrain/troops/time/civil
- [L] IPB — Intelligence Preparation of the Battlefield
- [L] F3EAD — Find/Fix/Finish/Exploit/Analyze/Disseminate
- [L] COIN Doctrine — Clear/Hold/Build counterinsurgency
- [F] Phase Operations (0-V) — Shape/Deter/Seize/Dominate/Stabilize/Enable
- [M] Deterrence Theory (Schelling) — capability × will × communication
- [M] Escalation Dominance — control at every rung
- [F] Hybrid / 4GW Warfare — composite-threat classification
- [S] Maskirovka — deception-as-doctrine stance
- [F] Just War Theory — jus ad bellum / in bello / post bellum

### Ecology

- [L] Trophic Cascade Analysis — top-down effect tracking
- [F] Niche Analysis — fundamental vs realized
- [M] Carrying Capacity — K population ceiling
- [F] Succession — primary/secondary ecological trajectory
- [M] Island Biogeography (MacArthur & Wilson) — area × distance → species count
- [M] Metapopulation Dynamics (Levins) — patch network persistence
- [M] Source-Sink Dynamics — population flow between habitats
- [F] Resilience vs Resistance (Holling) — recovery vs withstand
- [F] Planetary Boundaries (Rockström) — 9-boundary Earth system model
- [F] Doughnut Economics (Raworth) — social floor × ecological ceiling
- [L] Ecosystem Services (TEEB/MA) — 4-category valuation
- [L] DPSIR — Drivers/Pressures/State/Impact/Response
- [L] Adaptive Management — decision-monitor-learn cycle
- [F] Landscape Ecology — patch/corridor/matrix
- [L] Shannon / Simpson Diversity — quantitative biodiversity
- [F] IUCN Red List Criteria — 5-category extinction risk
- [L] Population Viability Analysis — extinction probability simulation
- [F] r/K Selection — reproduction strategy spectrum
- [L] Life Cycle Assessment — cradle-to-grave environmental impact
- [M] Ecological Footprint — consumption in global hectares

### Geology

- [H] Principle of Superposition — lower is older
- [H] Original Horizontality — sediments deposit horizontally
- [H] Cross-cutting Relationships — cutter is younger
- [H] Faunal Succession — fossil sequence as time marker
- [S] Uniformitarianism (Hutton/Lyell) — "present is key to past" stance
- [L] Walther's Law — vertical succession = lateral environments
- [L] Sequence Stratigraphy — sea-level-driven systems tract
- [M] Plate Tectonics — unified tectonic model
- [F] Wilson Cycle — supercontinent breakup-reassembly
- [F] Rock Cycle — igneous/sedimentary/metamorphic transformations
- [F] Bowen's Reaction Series — crystallization sequence
- [L] Mineral Identification — Mohs/cleavage/luster/streak
- [L] Structural Geology — fold/fault kinematic analysis
- [L] Stereonet Analysis — spherical projection of planar/linear structures
- [L] Radiometric Dating — U-Pb/K-Ar/C-14 absolute ages
- [L] Stable Isotope Analysis — δ¹⁸O/δ¹³C paleo-proxies
- [M] Milankovitch Cycles — orbital-climate forcing
- [L] Facies Analysis — depositional environment reconstruction
- [L] Geomorphic Process Analysis — weather/erode/transport/deposit
- [L] Geohazard Assessment — seismic/volcanic/mass-movement/tsunami evaluation
- [F] Big Five Mass Extinctions — deep-time extinction comparison

### Chemistry

- [L] VSEPR Theory — electron-pair geometry prediction
- [L] Lewis Structures + Formal Charge — resonance stability evaluation
- [L] Retrosynthetic Analysis (Corey) — target-to-precursor disconnection
- [M] Le Chatelier's Principle — equilibrium response to perturbation
- [F] HSAB Theory (Pearson) — Hard-Soft Acid-Base classification
- [M] FMO Theory (Fukui) — HOMO/LUMO frontier interaction
- [L] Woodward-Hoffmann Rules — orbital symmetry pericyclic allowed/forbidden
- [L] Hammett Equation — substituent σ × ρ linear free-energy
- [M] Marcus Theory — electron transfer rate model
- [F] Lipinski's Rule of Five — oral drug-likeness
- [L] ADMET Analysis — 5-axis drug property prediction
- [L] QSAR — structure-activity regression modeling
- [F] Green Chemistry 12 Principles — sustainable design rubric
- [H] Degree of Unsaturation — structural formula inference
- [L] Spectroscopy Interpretation (NMR/IR/MS) — systematic signal-to-structure

### Physics

- [L] Dimensional Analysis — unit consistency check
- [L] Fermi Estimation — order-of-magnitude reasoning
- [L] Buckingham Pi Theorem — dimensionless variable reduction
- [M] Noether's Theorem — symmetry ↔ conservation law
- [L] Limiting Cases Analysis — extreme-value formula validation
- [M] Principle of Least Action — variational mechanics
- [M] Lagrangian/Hamiltonian Formalism — coordinate-free mechanics
- [L] Perturbation Theory — solvable-base + small correction expansion
- [M] Effective Field Theory — scale-separated integration
- [M] Renormalization Group — scale-flow universality class
- [M] Landau Theory of Phase Transitions — order parameter expansion
- [S] Gedankenexperiment (Einstein) — thought-experiment stance
- [L] Anthropic Reasoning — observer-existence as evidence

### Astronomy / Astrophysics / Cosmology

- [L] HR Diagram — luminosity-temperature stellar classification
- [F] Stellar Classification (OBAFGKM) — spectral + luminosity class
- [L] Standard Candles Hierarchy — Cepheid → SN Ia distance ladder
- [S] Copernican Principle — non-privileged observer stance
- [S] Cosmological Principle — large-scale homogeneity/isotropy
- [M] Drake Equation — SETI probability product
- [M] Great Filter Hypothesis — civilization bottleneck framing
- [F] Exoplanet Detection Methods — transit/RV/imaging/microlensing comparison
- [L] Habitable Zone Analysis — liquid-water orbital range
- [L] Multi-messenger Astronomy — EM + GW + neutrino + CR combined
- [M] Lambda-CDM Concordance Model — standard cosmology baseline
- [L] Light Curve Analysis — brightness-over-time decomposition
- [F] Initial Mass Function — Salpeter/Chabrier stellar population weighting
- [L] Virial Theorem Analysis — gravitational mass estimation

### Sociology

- [S] Weber's Verstehen — interpretive-meaning stance
- [S] Durkheim's Social Facts / Anomie — social-realism stance
- [S] Marx's Base-Superstructure — materialist stance
- [S] Bourdieu's Habitus + Field + Capital — relational sociology stance
- [L] Goffman's Dramaturgy — front/back stage interaction analysis
- [S] Symbolic Interactionism — micro meaning-construction stance
- [S] Structural Functionalism (Parsons) — AGIL systems stance
- [S] Conflict Theory — power-struggle stance
- [M] Granovetter's Strength of Weak Ties — network information flow model
- [L] Social Network Analysis — centrality/betweenness/structural holes
- [M] Diffusion of Innovations (Rogers) — 5-category adoption curve
- [L] Moral Panic (Cohen) — 5-stage threat construction
- [S] Labeling Theory (Becker) — deviance-as-label stance
- [S] Intersectionality (Crenshaw) — crossing-axis oppression stance
- [S] Social Construction of Reality (Berger/Luckmann) — institutionalization stance
- [S] Actor-Network Theory (Latour) — human-nonhuman symmetry stance
- [S] Foucault's Power/Knowledge — discourse-power stance
- [S] Giddens' Structuration — structure-agency duality stance
- [M] Schelling Segregation Model — weak preferences → strong separation
- [M] Granovetter Threshold Models — cascade ignition by heterogeneous thresholds

### Economics

- [L] Supply-Demand Framework — price-allocation equilibrium analysis
- [L] Elasticity Analysis — price/income/cross response quantification
- [H] Opportunity Cost — alternative-forgone pricing
- [L] Marginal Analysis (MR=MC) — equi-marginal optimum
- [M] Comparative Advantage (Ricardo) — relative-opportunity-cost trade model
- [F] Market Failure Taxonomy — externality/public good/asymmetry/power
- [M] Coase Theorem — transaction cost → efficiency result
- [M] Prospect Theory (Kahneman/Tversky) — reference-point + loss aversion + probability weighting
- [L] Nudge / Choice Architecture — intervention design framework
- [M] IS-LM / AD-AS — macro equilibrium models
- [M] Phillips Curve — inflation-unemployment trade-off
- [M] Solow Growth Model — capital + labor + technology growth accounting
- [M] Endogenous Growth (Romer) — R&D-driven technology model
- [S] Institutional Economics (North) — rules-of-the-game stance
- [M] Efficient Market Hypothesis (Fama) — weak/semi-strong/strong price-information
- [M] Modigliani-Miller — capital structure irrelevance theorem
- [M] Arrow's Impossibility Theorem — social welfare function non-existence
- [L] Gini Coefficient / Lorenz Curve — inequality quantification
- [M] Revealed Preference (Samuelson) — choice-based preference inference
- [L] Cost-Benefit Analysis with Shadow Pricing — non-market valuation
- [M] Resource Curse / Dutch Disease — resource-led decline pattern
- [H] Tinbergen Rule — N goals require ≥N instruments

### Philosophy

- [S] Hegelian Dialectic — thesis/antithesis/synthesis concept motion
- [F] Categorical Imperative (Kant) — universal maxim test
- [F] Utilitarianism (Bentham/Mill) — greatest happiness principle
- [F] Virtue Ethics (Aristotle) — arete + phronesis character ethics
- [L] Veil of Ignorance (Rawls) — original-position justice selection
- [F] Trolley Problem — deontology vs consequentialism pressure test
- [H] Is-Ought Problem (Hume) — fact-value separation
- [H] Naturalistic Fallacy (Moore) — natural ≠ good
- [H] Ship of Theseus — identity-over-time puzzle
- [H] Chesterton's Fence — don't-remove-until-understood
- [H] Hanlon's Razor — stupidity over malice
- [H] Russell's Teapot — burden of proof on existence claim
- [L] Pascal's Wager — expected-utility theological argument
- [S] Wittgenstein's Language Games — use-based meaning stance
- [L] Gricean Maxims — Cooperative Principle 4 maxims
- [L] Speech Act Theory (Austin/Searle) — locution/illocution/perlocution 3-layer
- [S] Phenomenological Reduction (Husserl) — bracketing stance
- [S] Hermeneutic Circle — part-whole interpretation stance
- [S] Deconstruction (Derrida) — binary destabilization stance
- [L] Double Effect Doctrine — intended vs foreseen harm distinction
- [H] Ought Implies Can (Kant) — duty presupposes capability
- [L] Transcendental Argument — "X requires Y" conditional logic

### Psychology / Cognitive Science

- [M] Dual Process Theory (Kahneman) — System 1/2 cognition model
- [H] Cognitive Biases Taxonomy — anchoring/availability/representativeness catalog
- [F] Maslow's Hierarchy of Needs — 5-level need pyramid
- [F] Erikson's Psychosocial Stages — 8-stage lifespan development
- [F] Kohlberg's Stages of Moral Development — 3-level moral reasoning
- [F] Big Five / FFM — OCEAN personality dimensions
- [F] Attachment Theory (Bowlby) — 4 attachment styles
- [L] ABC Model (Ellis REBT) — Activating/Belief/Consequence intervention
- [M] Cognitive Dissonance (Festinger) — inconsistency-driven attitude change
- [M] Self-Efficacy (Bandura) — belief-performance link
- [M] Learned Helplessness (Seligman) — uncontrollability-motivation loss
- [M] Broaden-and-Build (Fredrickson) — positive emotion resource accumulation
- [F] PERMA Model (Seligman) — wellbeing 5 elements
- [M] Polyvagal Theory (Porges) — hierarchical autonomic response
- [S] IFS (Internal Family Systems) — multiplicity-of-mind therapy stance
- [M] Social Identity Theory (Tajfel) — group-identity mechanics

### Biology / Evolution

- [M] Natural Selection — variation + heritability + differential reproduction
- [M] Kin Selection / Inclusive Fitness (Hamilton) — rB > C
- [M] Reciprocal Altruism (Trivers) — cooperation in iterated interaction
- [M] Sexual Selection (Darwin) — reproductive trait selection
- [M] Red Queen Hypothesis — coevolutionary arms race
- [S] Extended Phenotype (Dawkins) — gene-beyond-body stance
- [M] Punctuated Equilibrium (Gould/Eldredge) — stasis + rapid change
- [M] Central Dogma (Crick) — DNA→RNA→Protein information flow
- [L] Phylogenetic Reconstruction — parsimony/ML/Bayesian tree inference
- [M] Niche Construction Theory — organism-environment reciprocity
- [M] Lotka-Volterra Dynamics — predator-prey oscillation

### History

- [F] Longue Durée / Annales (Braudel) — event/conjuncture/structure 3-layer time
- [H] Whig History Critique — teleological-narrative caution
- [F] Great Man vs Structural History — hero vs condition tension
- [L] Counterfactual History — "what if" causal weighting
- [L] Microhistory (Ginzburg) — small case → large structure
- [S] History from Below (Thompson) — subaltern-experience stance
- [S] Subaltern Studies — excluded-voice recovery stance
- [M] Cliodynamics (Turchin) — mathematical history (Secular Cycles)
- [S] Historical Materialism (Marx) — mode-of-production stance
- [L] Begriffsgeschichte (Koselleck) — conceptual history method

### Literary Theory / Humanities

- [L] Close Reading / New Criticism — form-only textual analysis
- [S] Structuralism (Saussure/Levi-Strauss) — differential-system stance
- [S] Post-structuralism / Deconstruction — instability-of-structure stance
- [L] Reader-Response (Iser) — reader-text interaction analysis
- [L] Narratology (Genette) — story/discourse/order/duration/focalization
- [L] Propp's Morphology — 31 folktale functions
- [S] Bakhtin's Dialogism / Chronotope — polyphony stance
- [S] Intertextuality (Kristeva) — text-as-mosaic stance
- [F] Hero's Journey (Campbell) — monomyth 12-stage
- [S] Postcolonial Theory (Said/Spivak/Bhabha) — colonial-discourse stance
- [S] Feminist Criticism — gender-power-representation stance
- [S] Psychoanalytic Criticism (Freud/Lacan) — unconscious-structure stance
- [S] Ecocriticism — nonhuman-world stance
- [L] Thick Description (Geertz) — action-meaning-web analysis

### Linguistics / Anthropology

- [S] Sapir-Whorf Hypothesis — language-thought relativity stance
- [M] Universal Grammar (Chomsky) — innate-grammar model
- [L] Comparative Method — historical sound correspondence reconstruction
- [F] Emic vs Etic — insider/outsider category distinction
- [L] Participant Observation — embedded ethnographic method
- [L] Kinship Terminology Analysis — social-structure inference

### Mathematics / Logic

- [L] Mathematical Induction — base + step proof
- [L] Proof by Contradiction — reductio ad absurdum
- [H] Pigeonhole Principle — cardinality-based existence
- [L] Invariant Analysis — preserved-quantity problem solving
- [L] Polya's How to Solve It — Understand/Plan/Do/Look back
- [S] Category Theory — abstract-structure stance
- [M] Bayesian Networks — conditional-independence DAG inference

---

## 8. Next-step recommendations

1. **v0.2 refactor (immediate)** — restructure the plugin into the 5-class
   layout, reclassify existing 12 files, add 1-2 starter items per new class,
   update catalog.yml / README.md / SKILL.md. See the seed prompt for a code
   session.

2. **"Core 30" lens expansion (after v0.2)** — pick 30 high-impact frameworks
   from the catalog that are not yet operationalized and build them as lens
   files. Priority candidates: ACH, FMEA, Pre-mortem, Retrosynthetic Analysis,
   SOAP + Differential Diagnosis, IRAC, Porter's Five Forces (as a model +
   lens pair), Cynefin (as a frame + lens pair), Thick Description,
   Lectio Divina, Tactical Empathy (Voss), Story Circle (Harmon), Parti
   Diagram, Backward Design (UbD), Zettelkasten, TRIZ, METT-TC, DPSIR,
   Walther's Law, Bayesian Clinical Reasoning.

3. **Agent type library (v0.3+)** — instead of only `.claude/agents/` configs
   inside user projects, ship `agents/library/` inside the plugin as a
   collection of reference agents (not just examples). `security-analyst`,
   `curriculum-reviewer`, `clinical-reasoner`, `strategy-analyst`,
   `pedagogical-reviewer`, `ethnographer`, etc. Each can be copied and
   customized.

4. **Contribution flow** — a PR to lenslab for a new framework must specify
   its class, its file location, and whether it requires operationalization
   to become a lens. A GitHub Action validates the file format per class.

5. **Anti-bloat guardrail** — the catalog has 600+ candidates, but only ~50
   will be operationalized in the first year. The plugin should NOT try to
   turn every catalog entry into a file. The catalog is a reference for the
   agent-creator skill, not a backlog.
