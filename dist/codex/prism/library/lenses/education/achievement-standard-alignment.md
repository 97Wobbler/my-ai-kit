---
name: Achievement Standard Alignment (성취기준 정합성 분석)
domain: education
source: Korean National Curriculum (2015/2022 revisions), Ministry of Education; adapted from content-skill separation analysis used in K-12 curriculum review
underlying_class: native
best_for: Verifying that learning content, assessment items, or AI-generated problems are correctly aligned to a specific Korean national curriculum achievement standard
one_liner: "Separate content and skill elements of Korean curriculum standards to verify item/content alignment."
---

# Achievement Standard Alignment (성취기준 정합성)

## Overview
The Korean national curriculum organizes learning targets as **achievement standards (성취기준)** — coded statements that bundle a content element (내용 요소) and a skill element (기능 요소). An item "aligned" to an achievement standard must exercise BOTH elements. Practitioners use this lens when reviewing textbook content, assessment items, or AI-generated problems against the official curriculum to catch three common failure modes: wrong code, content-only alignment (skill missing), and code drift (2015 vs 2022 revision confusion).

## Analytical Procedure

### Phase 1 — Decode the achievement standard

1. **Capture the full code and text.** Standards look like `[9수05-03]` or `[12국문01-02]`. The structure is:
   - `[9수05-03]`: grade band (9 = middle school 3rd year), subject (수 = mathematics), domain number (05), standard number within domain (03).
   - Write the code, grade band, subject, domain, and the verbatim standard text.

2. **Identify the curriculum revision year.** Korean curricula differ meaningfully between 2015개정 and 2022개정. Standards with the same code may refer to different content across revisions. Always name the revision.

3. **Split the standard text into content element (내용 요소) and skill element (기능 요소).**
   - **내용 요소** — the WHAT: the concept, fact, or domain knowledge (e.g., "이차방정식의 해", "함수의 극한").
   - **기능 요소** — the HOW: the cognitive or procedural skill (e.g., "판별식으로 해의 개수를 판단한다", "그래프를 해석한다").
   - If the standard text doesn't clearly separate the two, consult the curriculum document's "성취기준 해설" and "교수·학습 방법 및 유의 사항" sections. Do not guess.

4. **Identify the cognitive level.** Cross-reference with Bloom's Taxonomy — what cognitive demand does the 기능 요소 imply? Record as Remember/Understand/Apply/Analyze/Evaluate/Create. This will be used to detect under- or over-demand later.

### Phase 2 — Evaluate the item

5. **Describe the item being reviewed.** Problem statement, choices (if applicable), expected answer, solution path.

6. **Check content alignment (내용 일치):**
   - Does the item's content domain match the 내용 요소?
   - Is the content at the appropriate grade level (not using concepts from a higher grade)?
   - Is the content at the appropriate scope (not narrower or broader than the standard)?

7. **Check skill alignment (기능 일치):**
   - Does solving the item actually require the 기능 specified in the standard?
   - Common failure: the item tests *recall of the content* when the standard demands *application of a procedure*.
   - Common failure: the item uses a shortcut that bypasses the intended skill (e.g., students can guess the answer from answer choices without applying the procedure).

8. **Check cognitive level alignment:**
   - Is the cognitive demand of the item consistent with the level inferred from the 기능 요소?
   - Under-demand: standard expects Apply, item only tests Remember.
   - Over-demand: standard expects Understand, item demands Analyze.

9. **Check scope boundaries:**
   - Does the item accidentally require content from a different standard (out-of-scope prerequisites)?
   - Does the item cover only a sliver of the standard (under-coverage)?

10. **Check language and context appropriateness:**
    - Is vocabulary at grade level?
    - Are examples culturally/developmentally appropriate?
    - Are units, notation, and conventions consistent with the textbook the standard points to?

### Phase 3 — Diagnose and classify

11. **Assign an alignment verdict:**
    - **정합 (Aligned)** — content, skill, and cognitive level all match.
    - **부분 정합 (Partially aligned)** — content matches but skill is mis-targeted, or vice versa.
    - **불일치 (Misaligned)** — the item does not exercise what the standard requires.
    - **코드 오류 (Wrong code)** — the cited standard is wrong; another standard may actually apply.

12. **For partially aligned or misaligned items, specify the remediation:** change the item stem, change the answer choices, change the cited standard, or split into multiple items.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Curriculum revision year is stated (2015 / 2022) | Y/N |
| 내용 요소 and 기능 요소 are separated explicitly | Y/N |
| Cognitive level (Bloom's) of the standard is identified before evaluating the item | Y/N |
| Content alignment is judged independently of skill alignment | Y/N |
| Cognitive level of the item is compared to that of the standard | Y/N |
| Every misaligned finding has a specific remediation | Y/N |

## Red Flags

- The achievement standard is cited by code alone with no text quoted. The reviewer is trusting the code without reading the content.
- Revision year is missing. 2015개정 and 2022개정 use similar-looking codes and mixing them produces silent errors.
- 내용 요소 alone was checked; 기능 요소 was not. This is the most common AI-generated-problem failure mode: the problem is "about the right topic" but does not exercise the skill.
- The item is multiple choice with answer choices that can be eliminated by pattern matching without applying the skill. The 기능 요소 is not actually tested.
- Items at analytic/evaluative 기능 have a single correct answer with no rubric. Higher-order skills require criteria-based scoring.
- The reviewer accepts "aligned" without citing the 성취기준 해설. For borderline cases, the official 해설 is the tiebreaker and it is often overlooked.

## Output Format

```
## Achievement Standard Alignment Assessment

### Standard Being Targeted
- Code: <[9수05-03]>
- Revision: <2015개정 | 2022개정>
- Grade band / Subject / Domain: <...>
- Verbatim text: <...>
- 내용 요소 (content element): <...>
- 기능 요소 (skill element): <...>
- Cognitive level (Bloom's): <Remember / Understand / Apply / Analyze / Evaluate / Create>
- Source of 해설 consulted: <yes/no — reference>

### Item Under Review
<problem statement, choices, expected answer, solution path>

### Alignment Check
| Dimension | Verdict | Evidence |
|-----------|---------|----------|
| Content (내용) | ✓ / ✗ / 부분 | <...> |
| Skill (기능)   | ✓ / ✗ / 부분 | <...> |
| Cognitive level | ✓ / ✗ / 부분 | <...> |
| Scope boundaries | ✓ / ✗ / 부분 | <...> |
| Language/context appropriateness | ✓ / ✗ / 부분 | <...> |

### Verdict
<정합 | 부분 정합 | 불일치 | 코드 오류>

### Findings
1. <finding>
2. ...

### Remediation
- <specific change to item, choice, or standard citation>
- ...

### Confidence
<high/medium/low> — <justification>
```
