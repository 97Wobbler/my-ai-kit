---
name: retrieval-practice
display_name: Retrieval Practice
class: heuristic
underlying_class: native
domain: education
source: Cormacchione & Kornell (2008); Dunlosky et al. (2013)
best_for:
  - curriculum design
  - study strategy recommendations
  - assessment planning
one_liner: "Learning by testing produces longer-lasting memory."
---

# Retrieval Practice

## The Rule
Testing yourself on material produces stronger, longer-lasting retention than re-reading the same material, even when the test is harder and re-reading feels more fluent.

## When It Applies
- Designing study schedules for students preparing for exams or certification.
- Choosing between passive review (re-reading notes, watching videos again) and active recall (flashcards, practice problems, quizzes).
- Structuring curricula where spacing and interleaving of retrieval events compound retention gains.
- Evaluating learning technologies or platforms: does the interface encourage retrieval or re-exposure?

## When It Misleads
- On novel, unfamiliar content where the learner has no prior knowledge to retrieve from. Retrieval practice requires something to retrieve; it is not a substitute for initial encoding.
- In domains where procedural fluency (smooth, error-free execution) is the immediate goal and errors during retrieval practice degrade performance or safety (surgery, aviation, live performance). The long-term retention advantage can be outweighed by the cost of errors in the moment.
- When the retrieval task is too easy and becomes rote memorization of surface patterns rather than deep understanding. The benefit of retrieval practice depends on the retrieval being *effortful*; low-effort retrieval gives minimal gain.

## Common Misuse
Confusing "retrieval practice" with "any quiz." A quiz that simply re-exposes the student to material they just saw (closed-book exam taken the day after instruction) is not the same as spaced retrieval practice weeks later. The spacing and delay are load-bearing. Another common error: treating retrieval practice as a punishment or compliance mechanism rather than a learning tool, leading educators to overweight test anxiety and underweight the genuine cognitive benefit.

## How Agents Use It
- **Embedded**: in curriculum design or study-plan lenses, as a mandatory check before recommending passive review strategies. The lens should ask: "What is the retrieval event, and when is it spaced?"
- **Sanity-gate**: on each recommendation to study a topic, require the agent to identify a concrete retrieval opportunity (quiz date, problem set, teaching the material to someone else) and verify it is spaced at least days, not hours, after initial instruction. If no retrieval event is named, flag the recommendation as incomplete.
