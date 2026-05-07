---
name: atomic-notes-principle
display_name: Atomic Notes Principle
class: heuristic
underlying_class: native
domain: personal-knowledge-management-pkm
source: Luhmann, 1981; popularized by Ahrens (Zettelkasten), 2017
best_for:
  - Note-taking system design
  - Knowledge synthesis and retrieval
  - Long-form writing from notes
one_liner: "One idea per note — it becomes easier to combine and reuse."
---

# Atomic Notes Principle

## The Rule
Each note should contain a single, self-contained idea; when a note tries to hold multiple ideas, its reusability and clarity decay.

## When It Applies
- Designing or auditing a note-taking system where notes are meant to be referenced, linked, or remixed across different projects.
- Writing long-form documents or arguments by pulling and combining notes; atomic notes reduce the friction of reuse.
- Building a body of work over years where old notes must remain retrievable and useful without their original context.
- Creating search or tagging schemes; atomic notes make it vastly easier to tag accurately because each note has one semantic anchor.
- Collaborating on a shared knowledge base where multiple people need to understand and extend notes written by others.

## When It Misleads
- In heavily narrative or book-like writing where ideas are meant to build sequentially and breaking them apart fragments the argument — a chapter is not a note.
- For lightweight, exploratory note-taking where the goal is capture speed and the notes will never be reused; atomicity adds friction without benefit.
- When "one idea" is artificially small-grained, you produce thousands of fragments that are no longer meaningful without their neighbors; atomicity is not granularity fetishism.
- In domains where context-dependence is non-negotiable — a clinical case note cannot be atomic without losing diagnostic power.

## Common Misuse
Treating atomicity as a universal law rather than a design choice. The rule is sharp only when the note-taking system is explicitly meant to support synthesis, remixing, or long-term retrieval across projects. If a person takes notes only to capture a meeting and throws them away after, atomicity is busy-work.

Another frequent misuse is confusing atomicity with brevity. A note can be long and still atomic if it explores one idea fully; conversely, a short note can be non-atomic if it mashes together multiple ideas. The unit of composition is the idea, not the word count.

## How Agents Use It
- **Embedded**: in note-taking system design or audit lenses, as a check-step on existing note collections — agent examines a sample of notes and flags those containing multiple disjoint ideas, then suggests splitting them.
- **Sanity-gate**: when evaluating a note-taking recommendation or system design, ask: "Can a note in this system be used in three different projects without carrying dead weight?" If not, atomicity is weak.
