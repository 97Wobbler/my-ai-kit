---
name: affinity-diagram
display_name: Affinity Diagram
class: lens
underlying_class: native
domain: ux
source: Beyer & Holtzblatt (Contextual Design, 1998); widely adopted in user research and design thinking
best_for:
  - Clustering qualitative research data into themes
  - Surfacing hidden patterns in user feedback
  - Building shared understanding across cross-functional teams
one_liner: "Cluster qualitative data by theme to make patterns and structure visible."
---

# Affinity Diagram

## Overview
An affinity diagram organizes unstructured qualitative data—interview transcripts, survey responses, observations, user complaints—into hierarchical clusters by finding natural thematic groupings. Unlike forcing data into a predefined taxonomy, the diagram emerges from the data itself; the discipline is resisting the urge to impose structure too early. Practitioners use this to find patterns that wouldn't appear in quantitative metrics and to move a team from "we have hundreds of data points" to "we understand the landscape."

## Analytical Procedure

### Phase 1 — Prepare and Atomize

1. **Collect your raw qualitative data.** This can be interview transcripts, user research notes, support tickets, survey open-ended responses, usability testing observations, or field notes. Aim for at least 20-30 data points; fewer than 10 will not surface reliable patterns.

2. **Extract atomic insights.** Read through each source once. On a separate note or card (physical or digital), write one discrete observation, quote, or user need per card. Be specific:
   - Good: "User said they forget their password once a month and get frustrated waiting for the reset email"
   - Bad: "Users have password issues"
   - Good: "Observed user clicking the back button three times before finding the help section"
   - Bad: "Navigation is confusing"
   Aim for 50-150 cards depending on data richness.

3. **Deduplicate aggressively.** Read the full set. Remove exact duplicates. If two cards say nearly the same thing in different words, keep one and delete the other. Mark any card that is too vague or contradictory—set these aside for now.

### Phase 2 — First Pass Grouping

4. **Lay out all cards where you can see them simultaneously.** If physical, use a wall or large table. If digital, use a tool that supports drag-and-drop (Figma, Miro, Google Sheets with cards).

5. **Silently scan for obvious similarity without naming it.** Do NOT start with labels. Let your eye find cards that *feel* like they belong together. Start moving cards into loose piles. You are looking for magnetic attraction, not logical rules.

6. **Stop when you have 4-8 piles.** If you have more than 8 piles, you have not abstracted enough. If you have fewer than 4, you may have over-grouped. (This is not a hard rule, but a sign to pause and check your grouping.)

7. **For each pile, write a tentative label on a new card.** The label should describe what the pile is *about*, not what you think you should do about it:
   - Good: "Difficulty remembering account credentials"
   - Bad: "Build a password manager"
   - Good: "Preference for voice over text in noisy environments"
   - Bad: "Add voice input feature"

### Phase 3 — Second Pass Refinement

8. **Review each pile against the label.** Does every card in the pile fit the label? If not, move the misfitting card to another pile or create a new pile for it. If moving a card breaks its old pile's coherence, the label was too narrow—relabel.

9. **Check for outliers.** Some cards may not fit any pile. This is often where surprising insights hide. Create a small "other" or "doesn't fit" pile and revisit it later.

10. **Look for sub-themes within large piles.** If a pile has more than 10-12 cards, it may contain two separate themes. Try splitting it. If the split feels forced, leave it together.

11. **Verify coverage.** Make sure every card is assigned to exactly one pile. No card should belong to two themes (if it does, the themes overlap and need clarification).

### Phase 4 — Hierarchy and Naming

12. **Build a second-level abstraction if the data supports it.** Group your 4-8 piles into 2-3 larger buckets. Write labels for these as well. Example: piles labeled "Remembering passwords," "Resetting passwords," "Managing multiple accounts" might roll up into "Identity Management Friction."

13. **Finalize all labels at both levels.** Make sure each label is:
   - **Specific enough** to be meaningful (not "User Experience" or "Issues")
   - **Neutral** (describes what users experience, not what you should build)
   - **Consistent in style** (all noun phrases, or all gerunds, etc.)

## Evaluation Criteria

| Check | Pass |
|---|---|
| At least 20 atomic insights extracted from source data | Y/N |
| No more than 20% of cards are duplicates or near-duplicates | Y/N |
| First-pass grouping results in 4-8 piles | Y/N |
| Every card in a pile fits its pile's label | Y/N |
| Labels are descriptive, not prescriptive (no solutions embedded) | Y/N |
| Second-level hierarchy is present (if ≥7 first-level piles) | Y/N |
| Outlier pile has been reviewed for hidden patterns | Y/N |

## Red Flags

- Cards are labeled with design solutions ("Add search," "Redesign menu") instead of user observations. The diagram has skipped insight in favor of recommendations.
- More than 12 first-level piles. This usually means either every card got its own cluster (no grouping happened) or the data is too diverse to yield coherent themes (possible, but requires review of what data was collected).
- A pile contains contradictory observations with no sub-theme. Example: "User wants notifications" and "User hates notifications" in the same pile. Investigate — is the contradiction context-dependent (different user segments)? If so, split by context, not by theme.
- Outlier pile is discarded without inspection. Outliers often reveal edge cases, power users, or entirely different user segments.
- Labels use jargon or acronyms unfamiliar to someone not in the research. A label should be clear to a new team member.

## Output Format

```
## Affinity Diagram Report

**Data source:**
<type and count of raw data points, date range>

**Cards extracted:** <number of atomic insights>

**Final structure:**

### Level 1 Clusters

#### <Cluster Name 1>
- Card 1.1: <observation>
- Card 1.2: <observation>
...
Count: _

#### <Cluster Name 2>
...

### Level 2 Hierarchy (if applicable)

#### <Meta-bucket 1>
- Clusters: <Cluster Name 1>, <Cluster Name 2>
- Pattern: <1-2 sentences describing what these clusters have in common>

### Outliers / "Doesn't Fit"
- Card: <observation>
- Reason: <why it didn't cluster>
...

### Key Patterns Observed
1. <Major theme or insight that crossed multiple clusters>
2. <Pattern that surprised the team or contradicts prior assumptions>
3. ...

### Confidence
<high | medium | low> — <justification: e.g., "high — data source was 40 structured interviews with consistent population; clusters are stable across independent grouping attempts. Limitation: all users are desktop-based; mobile users not represented.">
```
---
