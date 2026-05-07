---
name: case-briefing
display_name: Case Briefing
class: lens
underlying_class: native
domain: law
source: Origin uncertain; foundational framework taught in U.S. law schools since mid-20th century
best_for:
  - Extracting the legal essence of a judicial opinion
  - Building a comparable library of precedents
  - Teaching case analysis to junior lawyers
one_liner: "Systematically extract facts, procedural history, issues, holding, and reasoning from a case."
---

# Case Briefing

## Overview
A case brief distills a judicial opinion into five standardized components: the facts (what happened), the posture (who sued whom and what relief they sought), the issue (the legal question the court decided), the holding (what the court decided, stated as a rule), and the reasoning (why the court reached that holding). Practitioners use this framework to quickly absorb the legal content of an opinion without wading through rhetorical flourish or procedural details, and to build a searchable inventory of precedent. The discipline is precision — "the court held X" is not a holding if X is vague.

## Analytical Procedure

### Step 1 — Extract the Facts

1. **Read the opinion's fact section (usually the first substantive part).** Write down every fact the opinion later references in its legal analysis. Do not include facts mentioned only in passing or in hypotheticals.

2. **Organize facts chronologically.** Start with the state of the world before the dispute arose, then the events that triggered it, then the parties' actions and responses.

3. **Test each fact for relevance.** Ask: "Would the holding be different if this fact were different?" If no, the fact is descriptive padding and does not belong in the brief. If yes, include it.

4. **Write the facts in 3-5 sentences, using past tense.** A reader unfamiliar with the case should be able to predict what legal dispute is coming.

### Step 2 — Determine the Posture

5. **Identify the parties.** Name the plaintiff (or appellant) and defendant (or respondent) by their legal roles, not their descriptive labels. Write as: "[Party A] v. [Party B]."

6. **Identify the procedural history.** What court decided the case originally? What happened there? What order is this opinion reviewing? Write chronologically: "District court granted X; Court of Appeals reversed; Supreme Court granted cert."

7. **Identify the relief sought.** What did the plaintiff ask for at each stage? (Damages, injunction, specific performance, reversal, etc.) Write as one sentence: "[Plaintiff] seeks [specific relief] on appeal."

### Step 3 — Identify the Legal Issue

8. **State the narrow legal question the court is answering.** Not "Is the law on point X settled?" but "Does Statute Y apply when Condition Z is present?" or "Must a party satisfy Requirement A before relief under Doctrine B is available?"

9. **Phrase the issue as a question, not a statement.** Bad: "The burden of proof for retaliation claims." Good: "What burden of proof applies to retaliation claims under Title VII?"

10. **Test the issue against the holding.** A proper issue is a yes/no or categorical question that the holding answers directly. If the holding does not answer the issue, the issue was misstated.

11. **Write the issue in one sentence.** If you need multiple sentences, you have multiple issues — separate them.

### Step 4 — Extract the Holding

12. **Find the sentence or sentences where the court states its rule.** Look for language like "We hold," "The rule is," "We conclude," or "Therefore." Dissents and concurrences do not state holdings.

13. **State the holding as a rule, not an application.** Bad: "The plaintiff proved intentional discrimination." Good: "An employer's failure to promote an employee based on race violates Title VII without regard to the defendant's stated reason."

14. **Narrow the holding to what the court actually decided.** Do not add a holding implied but not stated. Do not broaden a holding to cover fact patterns the opinion does not address. If the court leaves a question open, say so: "The court left open whether the rule applies when...".

15. **If the opinion addresses multiple issues, state multiple holdings separately.** Label them Holding 1, Holding 2, etc.

### Step 5 — Trace the Reasoning

16. **Identify the legal authorities the court relies on.** Prior precedents, statutes, constitutional provisions, rules of interpretation — list them in the order the court invokes them.

17. **For each authority, write one sentence explaining how the court uses it.** (Does it establish the rule directly? Do prior facts distinguish it? Is it analogical?)

18. **Identify any policy arguments.** Does the court cite fairness, efficiency, incentive effects, or legislative intent? Write those down.

19. **Write the reasoning as a causal chain.** "Because A (precedent/statute/policy) and B (fact) are present, C (holding) follows." If you cannot connect the dots, the reasoning may be elliptical — note that.

20. **Check for unsupported leaps.** Does the court assume something without argument? Mark those explicitly: "The court assumes without discussion that...".

### Step 6 — Quality Check

21. **Reread the opinion.** Confirm that each component (facts, posture, issue, holding, reasoning) is faithful to what the court actually says and decides.

22. **Test the brief for sufficiency.** Someone reading only your brief should be able to explain the opinion to a colleague. If they cannot, a component is too vague.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Facts include all facts the opinion relies on in legal analysis | Y/N |
| Facts are organized chronologically and written in past tense | Y/N |
| Posture clearly identifies parties, procedural history, and relief sought | Y/N |
| Issue is phrased as a single question | Y/N |
| Holding is stated as a rule, not an application | Y/N |
| Holding directly answers the issue | Y/N |
| Reasoning identifies authorities and traces the causal chain | Y/N |
| Brief contains no unsupported inferences about what the court decided | Y/N |

## Red Flags

- Facts section includes facts not referenced in the opinion's legal analysis. These are noise; remove them.
- Issue is phrased as a statement ("The question of retaliation claims") rather than a question. Rephrase.
- Holding describes what the parties did, not what rule the court announced. The holding must be a principle, not a judgment.
- Holding is broader than the opinion supports — the court did not address that fact pattern. Narrow it.
- Reasoning section is missing or paraphrases the opinion without identifying which authorities did which work. Trace the causal chain explicitly.
- Holding and reasoning contradict each other, or the reasoning does not logically lead to the holding. Reread the opinion.
- Brief is longer than one page. Every component can be stated precisely and briefly. If yours is longer, cut.

## Output Format

```
## Case Brief

**Case:** <Name v. Name> | <Court> | <Year>

### Facts
<3-5 sentences, chronological, past tense, covering all facts relied on in analysis>

### Posture
<Plaintiff/Appellant> v. <Defendant/Respondent>. [Procedural history in order]. <Plaintiff/Appellant> seeks [relief].

### Issue
<What legal question does the court answer? Phrased as single question.>

### Holding
<The rule the court announces, stated as a principle not an application.>

[If multiple issues: Holding 2: <...>]

### Reasoning
1. <First authority and how it is used>
2. <Second authority and how it is used>
3. [Policy arguments, if any]
4. <Causal chain connecting authorities, facts, and holding>
[Note any unsupported leaps: "The court assumes without discussion that..."]

### Confidence
<high/medium/low> — <Justification: Does the opinion clearly state each component? Are there ambiguities in what the court decided? Is the holding narrow enough to be falsifiable against fact patterns the opinion does not address?>
```
