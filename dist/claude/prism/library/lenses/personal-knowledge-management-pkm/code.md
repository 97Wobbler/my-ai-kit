---
name: code
display_name: CODE (Capture, Organize, Develop, Evolve)
class: lens
underlying_class: native
domain: personal-knowledge-management-pkm
source: Roam Research, Obsidian PKM practices, Tiago Forte (Building a Second Brain); origin formalized by PKM practitioners 2018–2024
best_for:
  - Auditing a personal knowledge system for coherence and actionability
  - Identifying gaps between captured knowledge and synthesized insight
  - Measuring knowledge maturity from raw input to applied output
one_liner: "Capture-Organize-Distill-Express — refine knowledge into actionable insight."
---

# CODE (Capture, Organize, Develop, Evolve)

## Overview
CODE is a PKM lifecycle lens that audits how well a knowledge system progresses from raw capture (notes, clips, links) through organization (tagging, linking, structuring) to development (synthesis, writing, insight) and finally evolution (review, iteration, application). It operates on the artifact set of a personal knowledge base — the files, structure, metadata, and output — and identifies where knowledge stalls or loses fidelity. Practitioners use it to diagnose why a knowledge system feels noisy, why insights rarely surface, or why effort spent capturing doesn't translate to output.

## Analytical Procedure

### Phase 1 — Inventory the Four Layers

1. **Capture Layer.** List the sources your system ingests from: reading apps (Readwise, Pocket), notes (voice memos, quick captures), research (PDFs, web clips), conversations (Slack, emails). Note the frequency and format of each (e.g., "10 Readwise highlights/week, unstructured"). Mark which sources have automated ingestion and which require manual entry.

2. **Organize Layer.** Map how captured items are tagged, linked, or structured. Walk through a recent capture and trace its path: Does it go directly into a "New" folder? Is it immediately tagged? Does it get linked to existing notes? How long before it moves from inbox to archive? Document the actual workflow, not the intended one.

3. **Develop Layer.** Identify where synthesis happens. Scan your system for:
   - Writing projects (essays, blog posts, long-form notes)
   - Evergreen notes or working notes that combine multiple sources
   - Concept maps, timelines, or structured arguments
   - Outputs actually shipped (published, shared, acted upon)
   Record the ratio of develop artifacts to total notes.

4. **Evolve Layer.** Check for review and iteration practices. Look for:
   - Regular review cycles (weekly, monthly, quarterly)
   - Notes that have been updated or linked to more than once
   - Feedback loops (e.g., "applied this idea on date X, learned Y, updated note")
   - Deprecation (notes marked obsolete, archived, or contradicted by later work)
   Record how many notes have been touched more than once in the last 90 days.

### Phase 2 — Trace Knowledge Flow

5. **Pick a recent Develop artifact** (essay, decision, project output) that you're proud of. Work backward:
   - What Organize elements (tags, links, collections) fed into it?
   - Which Capture sources showed up in the citations or references?
   - How many times was the piece revised before shipping?
   - How much of the underlying knowledge was already in your system before you started writing?

6. **Measure the conversion funnel.** Count the ratio:
   - Captures entered this week: X
   - Captures organized/tagged: X * (%)
   - Captures used in a Develop artifact in the last 90 days: X * (%)
   - Captures acted upon (applied to a decision, project, or output): X * (%)

### Phase 3 — Identify Bottlenecks

7. **For each layer, identify the bottleneck:**
   - **Capture bottleneck:** Sources are numerous but capture is manual or inconsistent. Signal: large backlogs, untagged clips.
   - **Organize bottleneck:** Captures pile up without tagging or linking. Signal: inboxes stay full, search fails, you can't find related notes.
   - **Develop bottleneck:** Knowledge is organized but synthesis rarely happens. Signal: tags and links exist but few writing projects use them; high notes-to-output ratio.
   - **Evolve bottleneck:** Output is created but rarely revisited or refined. Signal: notes are one-shots; reviews don't happen; no feedback loop.

8. **Rate the severity** of each bottleneck: None / Mild / Moderate / Severe.

9. **Identify the first critical bottleneck** — the earliest layer where flow breaks. Fixing downstream layers before this one is premature optimization.

### Phase 4 — Audit Fidelity Loss

10. **Check three recent notes for information loss:**
    - Original source (article, podcast, etc.)
    - Your capture (highlight, summary, or full transcript)
    - Your organized tag/link
    - How it showed up in a Develop piece (if at all)
    
    At each step, estimate what was lost: nuance, context, evidence, original intent. Mark losses as Minor / Significant / Fatal.

11. **Trace a failure case.** Find a capture you *thought* would be useful but never surfaced in any Develop artifact. Why didn't it get linked? Was it mistagged? Did you never write about that topic? Did you forget it existed?

## Evaluation Criteria

| Check | Pass |
|---|---|
| All four layers (Capture, Organize, Develop, Evolve) are inventoried with concrete evidence | Y/N |
| At least one Develop artifact was traced back to its sources | Y/N |
| Conversion funnel percentages are calculated from actual counts, not estimates | Y/N |
| Each layer has a rated bottleneck (None/Mild/Moderate/Severe) | Y/N |
| First critical bottleneck is identified | Y/N |
| Fidelity loss is traced through at least one complete flow (source → capture → organize → develop) | Y/N |

## Red Flags

- Capture layer is automated but Organize layer is manual with no triggers. Inboxes will grow without bound.
- Organize layer looks sophisticated (many tags, dense links) but Develop layer is empty. The system is beautiful but inert — knowledge is being filed, not used.
- All bottlenecks are rated "Severe." Either the system is actually broken or you're not being honest about what's actually stuck. Pick the one true first bottleneck.
- Fidelity loss is "Fatal" at the Capture→Organize step but the Develop artifacts don't reflect this (they seem coherent). Either your captures are better than you think or the artifacts aren't actually drawing from the system.
- No Evolve evidence exists. Notes are never reread, refined, or corrected. The system is a one-way archive, not a living knowledge base.
- Conversion funnel shows <2% of captures used in Develop work within 90 days. The ROI on capture effort is too low; either capture selectivity must increase or the system is capturing noise.

## Output Format

```
## CODE Assessment

**System name/description:**
<your PKM system (Obsidian, Roam, Logseq, etc.)>

### Phase 1 — Four Layers

#### Capture Layer
- Sources: <list with frequency and format>
- Automated sources: <which ones>
- Manual entry burden: <estimate hours/week>

#### Organize Layer
- Tagging scheme: <primary tags and counts>
- Linking practice: <how links are created and used>
- Inbox workflow: <actual path from capture to archive>

#### Develop Layer
- Writing projects (last 90d): <count and brief list>
- Evergreen/working notes: <count>
- Shipped outputs: <count and type>
- Develop-to-total ratio: _%

#### Evolve Layer
- Review cycle: <frequency and method, or "none">
- Retouch rate (% of notes modified 2+ times in 90d): _%
- Feedback loops: <examples or "none">

### Phase 2 — Knowledge Flow Trace

**Chosen Develop artifact:** <title and date>

**Upstream sources:**
- Organize elements used: <tags/links/collections>
- Capture sources cited: <which sources appeared in final output>
- Revisions: <number of drafts before shipping>
- Pre-existing knowledge: <% of content already in system before writing>

**Conversion funnel (last 90 days):**
- Captures entered: X
- Captures organized: X * (_%
- Captures in Develop work: X * (_%
- Captures acted upon: X * (_%

### Phase 3 — Bottlenecks

| Layer | Bottleneck type | Evidence | Severity |
|---|---|---|---|
| Capture | <None/Source overload/Manual entry/Other> | <...> | None/Mild/Moderate/Severe |
| Organize | <None/Untagged backlog/Weak linking/Other> | <...> | None/Mild/Moderate/Severe |
| Develop | <None/Low synthesis/Few projects/Other> | <...> | None/Mild/Moderate/Severe |
| Evolve | <None/No review/One-shot notes/Other> | <...> | None/Mild/Moderate/Severe |

**First critical bottleneck:** <layer and description>

### Phase 4 — Fidelity Loss

**Sample 1: <source title>**
- Original → Capture loss: <Minor/Significant/Fatal> — <what was lost>
- Capture → Organize loss: <Minor/Significant/Fatal> — <what was lost>
- Organize → Develop loss: <Minor/Significant/Fatal> — <did it appear in output?>

**Sample 2 & 3:** <repeat format>

**Failure case:** <a capture that never surfaced; why>

### Recommendations (in priority order)

1. Address <first critical bottleneck> first: <one specific action>
2. <next>

### Confidence
<high | medium | low> — <justification based on data completeness and bottleneck clarity>
```
