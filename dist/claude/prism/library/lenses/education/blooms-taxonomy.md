---
name: Bloom's Taxonomy (Revised, 2001)
domain: education
source: Benjamin Bloom (1956); revised by Anderson & Krathwohl, 2001
underlying_class: frame
best_for: Classifying learning objectives, assessment items, or course activities by cognitive demand to ensure appropriate depth
one_liner: "Classify objectives / content / assessment via Bloom's six levels and surface alignment gaps across the three."
---

# Bloom's Taxonomy (Revised)

## Overview
Bloom's revised taxonomy sorts cognitive tasks into six levels from lowest to highest demand: Remember → Understand → Apply → Analyze → Evaluate → Create. The value is not the hierarchy for its own sake — it's detecting mismatches between stated objectives, taught content, and assessed items (the "curriculum alignment triangle"). A course that claims to teach Analysis but only tests Remember is misaligned, and Bloom's makes that visible. Practitioners use it when auditing curricula, writing test banks, and designing lessons.

## Analytical Procedure

1. **Extract the items to classify.** This can be:
   - **Learning objectives** ("Students will be able to ___")
   - **Assessment questions** (individual items on a test/quiz)
   - **Activities** (lesson tasks)
   Tag each item with its source so you can trace mismatches later.

2. **For each item, identify the main verb and the main noun (cognitive object).** The verb signals the cognitive level; the noun signals the content. If there are multiple verbs, split the item — compound items can't be cleanly classified.

3. **Classify using the verb + the actual task demand.** The verb is a hint, not a final answer — "explain" can be Understand or Analyze depending on what's being explained. Use the level descriptions:

### Level 1 — Remember
Retrieve information from long-term memory.
- **Verbs (typical):** recall, list, name, identify, define, state, recognize
- **Task demand:** Can be completed by looking up or reciting. No transformation needed.
- **Example:** "List the three branches of the U.S. government."

### Level 2 — Understand
Construct meaning from instructional material.
- **Verbs:** explain, describe, summarize, paraphrase, classify, compare (superficially), interpret
- **Task demand:** Requires rephrasing or grouping, but not application to a new situation.
- **Example:** "Explain what checks and balances means in your own words."

### Level 3 — Apply
Use a procedure in a given situation.
- **Verbs:** use, apply, execute, implement, solve (with known procedure), demonstrate, calculate
- **Task demand:** A known method is applied to a novel instance. The method is given; the instance is new.
- **Example:** "Solve this system of equations using elimination."

### Level 4 — Analyze
Break material into parts and determine how parts relate.
- **Verbs:** analyze, differentiate, organize, attribute, deconstruct, distinguish
- **Task demand:** The student identifies structure, bias, assumption, or relationships not explicit in the text.
- **Example:** "Identify which rhetorical devices Lincoln uses in the Gettysburg Address and how each contributes to his argument."

### Level 5 — Evaluate
Make judgments based on criteria and standards.
- **Verbs:** evaluate, critique, judge, justify, defend, argue (for/against), recommend
- **Task demand:** The student applies criteria (given or self-generated) to judge quality, effectiveness, or validity. There is no single right answer, but some answers are defensible and others aren't.
- **Example:** "Evaluate which of these two proposed policies better addresses urban water scarcity, using the three criteria discussed in class."

### Level 6 — Create
Put elements together to form a new coherent whole.
- **Verbs:** design, construct, plan, produce, generate, author, compose
- **Task demand:** The student produces something that did not exist before. Novelty is the defining feature.
- **Example:** "Design an experiment to test whether caffeine affects short-term memory."

4. **Tally by level.** Produce a distribution across the 6 levels for each source (objectives, content, assessment).

5. **Check alignment across sources.** Overlay the three distributions. The gold standard is that all three are approximately aligned. Common misalignments:
   - **Objectives > Assessment** — the course claims to teach Analyze/Evaluate but only tests Remember/Understand. Students learn what's tested, so the stated objective is fiction.
   - **Content > Assessment** — the instruction covers higher levels but assessment doesn't, so learning isn't measured.
   - **Assessment > Content** — assessment demands something never taught, which is unfair.

6. **Flag the top 3 misalignments** as findings, each with the source→source mismatch named explicitly.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Each item has a verb and a cognitive object identified | Y/N |
| Compound items were split before classification | Y/N |
| Classification is based on task demand, not just the verb | Y/N |
| Distribution is computed per source (objectives / content / assessment) | Y/N |
| Misalignments across sources are named, not just tallied | Y/N |
| At least top 3 misalignments are reported as findings | Y/N |

## Red Flags

- Everything clusters at Remember and Understand. Common in curricula that plateau at fact-recall. Either the course is intentionally foundational (document why) or it's under-challenging.
- Objectives say "analyze" and "evaluate" but every assessment item is multiple choice with one right answer. Higher-level thinking is claimed but not assessed.
- The verb list treats "explain" as always Understand. "Explain why this proof is invalid" is Evaluate, not Understand. Classification by verb alone is a known failure mode.
- No Create-level items at all. Some disciplines genuinely don't require Create, but most college-level courses should have some. Absence warrants explanation.
- Items at Analyze/Evaluate/Create don't specify criteria. Without criteria, the student can't know what a good answer looks like, and the grader can't grade fairly.

## Output Format

```
## Bloom's Taxonomy Assessment

### Source inventory
- Objectives: <n items>
- Content activities: <n items>
- Assessment items: <n items>

### Classification Table
| Item | Source | Verb | Object | Level | Justification |
|------|--------|------|--------|-------|---------------|
| ... | objective | analyze | rhetorical devices | 4 - Analyze | student must identify structure not stated in source |

### Distributions
|            | Remember | Understand | Apply | Analyze | Evaluate | Create |
|------------|----------|------------|-------|---------|----------|--------|
| Objectives |    _%    |     _%     |   _%  |    _%   |    _%    |   _%   |
| Content    |    _%    |     _%     |   _%  |    _%   |    _%    |   _%   |
| Assessment |    _%    |     _%     |   _%  |    _%   |    _%    |   _%   |

### Misalignments
1. <Objectives → Assessment>: objectives expect _% at Analyze; assessment has _%. Gap of _%.
2. <...>
3. <...>

### Recommendations
- <concrete changes to items, assessments, or objectives to reduce the top gap>

### Confidence
<high/medium/low> — <justification>
```
