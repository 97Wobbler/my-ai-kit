# Diagnostic Interview Guide

Use this guide in init mode to populate the Rumsfeld matrix from learner evidence.

## Principles

- Go conversational, not checklist-like.
- Ask 3-5 questions per round, wait for answers, and go deeper based on the response.
- Treat "모른다" as useful data for the Known Unknowns quadrant.
- Actively look for correct transferable intuitions, misconceptions disguised as knowledge, and areas the learner cannot yet formulate as questions.

## Rounds

### Round 1: Experience And Motivation

- What direct experience do you have in this domain?
- What is your goal, and why this domain now?
- What mental image do you currently have of this domain?

### Round 2: Concept Probing

- Present 8-12 representative terms spanning the domain.
- Ask the learner to classify each term: "설명할 수 있다 / 들어봤다 / 처음 듣는다".
- For terms they claim to know, ask them to explain and verify depth.

### Round 3: Transferable Skills

- Identify the learner's existing domains of expertise.
- Ask bridge questions from those domains into the new domain.
- Look for structural parallels that reveal Unknown Knowns.

### Round 4: Fundamental Assumptions

- Ask foundational "why" questions for the domain.
- Use these to distinguish system understanding from surface familiarity.

### Round 5: Unknown Unknowns Estimation

Based on the earlier rounds, propose likely Unknown Unknowns:

- structural holes in the learner's current mental model;
- important concepts they never referenced;
- common beginner blind spots in the domain.

Present these as estimates, explain why each matters, and invite correction.

## Output

Generate `matrix.yaml` with all four quadrants populated. Each item should include a concise description, evidence from the interview, and any caveat on partial knowledge. Unknown Unknowns should explain why they matter and what risk remains if they stay unknown.
