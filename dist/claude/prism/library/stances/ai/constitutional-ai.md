---
name: constitutional-ai
display_name: Constitutional AI
class: stance
underlying_class: native
domain: ai
source: Yuntao Bai, Andy Jones, et al. — "Constitutional AI: Harmlessness from AI Feedback" (2022); Anthropic research on RLHF alternatives and principle-based alignment
best_for:
  - Reading AI system behaviors to expose what principles are actually being enforced
  - Identifying gaps between stated constitutional values and enacted constraints
  - Understanding how natural-language rules encode and reproduce particular framings of harm
one_liner: "Stance that governs AI behavior via natural-language principles and surfaces the gap between principle and action."
---

# Constitutional AI

## Overview

Constitutional AI is a commitment to treating **AI system behavior not as the expression of an objective harmlessness function, but as the enactment of specific natural-language principles that encode particular cultural and institutional assumptions about what counts as harmful, trustworthy, or aligned**. The stance's purpose is to make visible the work that principles perform: what they permit and forbid, whose interests they protect, what harms they render invisible, and what alternative framings of safety they foreclose. It is an interpretive position applied to AI artifacts (training procedures, behavior logs, policy documents, red-team findings), not a procedure for building systems. Its findings become visible when you stop asking "is this system safe?" and start asking "what does this system's constitution assume about harm, agency, and responsibility?"

## Foundational Commitments

- **Principles are not neutral.** A constitutional principle like "be helpful, harmless, and honest" appears universal but depends on unstated background assumptions: what counts as "helpful" (to whom?), what harms are salient versus invisible, whose conception of honesty is operative. Every principle is a position, not a fact.

- **Principles are enacted through training, not simply stated.** What matters is not the text of the constitution but which principles actually shape the system's learned behaviors, which are weighted higher in case of conflict, and which get consistently violated or consistently upheld. A principle that appears in the document but never shapes behavior is not truly constitutional.

- **Natural language is an imprecise medium for encoding constraints.** Principles must be operationalized—translated into feedback signals, training data, examples, and red-team scenarios. This translation is where ambiguity, cultural specificity, and unexamined assumptions enter. The gap between the principle and its operationalization is the site where the stance looks hardest.

- **Harm is culturally and institutionally specific.** What is flagged as harmful depends on the institutional context (academic research vs. commercial product vs. defense), the jurisdiction, the deployment model, and the assumed user. Constitutional AI systems often encode the assumptions of their builders without acknowledging that these are assumptions.

- **Alignment is relational, not absolute.** A system can be aligned with one set of values while misaligned with others. The stance asks: aligned with *whom*, toward *what*, at the expense of *what*? Alignment is not a property of the system but a relationship between the system and a set of stakeholders.

- **Principles often conflict, and their resolution reveals priorities.** When a principle-based system faces a case where "be helpful" and "avoid harm" point in different directions, how the system resolves the conflict (through training, feedback weighting, tie-breakers) exposes its actual commitments.

- **The constitution is not the system's only constraint.** Training objectives, base-model biases, deployment guardrails, user interaction patterns, and organizational incentives all shape behavior alongside the written principles. A purely constitutional reading that ignores these context factors will miss how the system actually works.

## Guiding Questions

**The stated constitution and its coverage**
- What principles are explicitly part of the system's constitution?
- Which harms or risks are named as problems the constitution addresses, and which are not mentioned?
- Are principles stated at the same level of abstraction, or do some get detailed operationalization while others remain vague?
- What categories of impact (bias, privacy, labor, environmental, economic) are in scope, and which are implicitly out of scope?

**Operationalization and training**
- How were principles translated into training signals? (Rubrics? Examples? Red-team scenarios? Feedback functions?)
- Which principles received more detailed, more expensive, or more frequent training feedback?
- In cases where principles conflict, how did the training procedure resolve them? What was the relative weighting?
- What behaviors does the system exhibit that cannot be explained by the stated constitution alone?

**What counts as harm under this constitution**
- What specific harms does the system refuse or flag? (Deception? Violence? Discrimination? Privacy violation? Labor displacement? Environmental damage?)
- For each flagged category, what is the operational definition?
- What harms could the system cause that are *not* named by the constitution? (Second-order effects, structural impacts, distributional harm that affects some users/stakeholders and not others.)

**Whose interests are protected**
- From whose position does the constitution make sense? (Which stakeholder groups' interests are centered; which are peripheral or absent?)
- Who decides whether a principle has been violated? (The system itself? Users? Auditors? The company?)
- What kinds of user are assumed in the principle's framing? (Naive? Malicious? Resource-constrained? Operating in a high-stakes domain?)

**Where the constitution is silent or strained**
- What kinds of request or use case does the system handle without clear constitutional guidance?
- Where does the system's actual behavior diverge from what the constitution would predict?
- Are there cases where the constitution *forbids* something the system permits, or vice versa?

**History and contingency of the constitution**
- When was each principle added, and in response to what observed behavior or external pressure?
- Have any principles been removed or deprioritized, and why?
- What alternative constitutions were considered and rejected?

**Scope of accountability**
- For whom is the system responsible under this constitution? (Individual users? Organizations? Downstream affected parties? Society?)
- What recourse exists if the constitution is violated? (Feedback to builders? User appeal? Transparency mechanism? None?)
- Does the constitution address its own failure modes—what the system should do if it cannot satisfy all principles?

## What It Reveals

- **The specificity of apparent universals.** Principles like "be honest" or "avoid harm" appear culture-free until you look at how they are operationalized, at which point their institutional and geographic assumptions become visible.

- **The work of translation from principle to behavior.** Where a principle required the most complex operationalization, detailed red-teaming, or frequent feedback, the stance can infer that the concept was harder to encode—which itself is informative about ambiguity or disagreement.

- **Priorities revealed through weighting and conflict resolution.** When two principles cannot both be satisfied, how the system actually chooses (not how it says it chooses) reveals the constitution's true hierarchy.

- **Harms that remain unnamed.** The constitution's silence about certain categories of risk is not neutral; it implicitly deprioritizes them. The stance surfaces what the constitution does not name.

- **The cultural and institutional specificity of the framework.** What appears as technical alignment work is often cultural transmission—encoding the assumptions of particular communities (AI safety researchers, tech companies, academic institutions) into systems that users from other communities will interact with.

- **Tension between principle-based and goal-based alignment.** A system aligned to stated principles may still fail in contexts where principles are vague, conflict, or miss the actual stakes. The stance reveals this tension.

## What It Obscures

- **Material conditions of model development.** A purely constitutional reading can miss how data sourcing, labeler working conditions, compute availability, commercial incentives, and regulatory pressure shape what training was possible. The constitution describes the goal; it does not explain the resource constraints. (Pair with political economy or labor-process analysis when material conditions are decisive.)

- **Non-principle sources of safety.** Constitutional AI emphasizes principles, but much AI safety work happens elsewhere: base-model quality, architectural constraints, deployment restrictions, human review, monitoring infrastructure. A system aligned via its constitution while depending heavily on guardrails outside the constitution is not what the framework implies. (Combine with systems-level or architectural analysis.)

- **Distributional and temporal questions.** The constitution typically asks "is this harmful" as a binary or scalar question; it is weaker on "harmful to whom over what timescale" or "at what scale of deployment do these harms emerge." (Use a stakeholder-impact or temporal-dynamics stance for these questions.)

- **The limits of natural language for encoding constraint.** Principles stated in English are inherently ambiguous. A constitutional reading that does not grapple with this ambiguity—that treats the constitution as if it were a formal specification—understates the role of interpretation in each deployed system instance.

- **Incentives for principle drift.** A constitutional AI system faces pressure to expand or reframe principles to justify economically or politically motivated decisions. The stance is weaker at detecting when principle-language is being used to rationalize decisions made on other grounds. (Use a political-economy or organizational-interest analysis alongside.)

- **Comparative absence.** The stance is good at reading what a constitution does; it is weaker at asking whether the constitutional approach itself is the right way to do alignment. Non-principle approaches (learned reward models, constitutional debates between systems, specification gaming, default-deny) may be better in some contexts but the stance does not inherently compare them.

## Output Format

```
## Constitutional Reading: <System / Policy / Behavior Log>

### Stated Constitution
- Explicit principles: <list with brief definition of each>
- Coverage: <what categories of harm / safety are in scope; what is notably absent>
- Principle hierarchy / weightings: <are some principles foregrounded; which get more detailed operationalization>

### Operationalization
- Training procedures used to encode principles: <rubrics, feedback signals, examples, red-team data, …>
- Conflict resolution: <how the system prioritizes when two principles conflict; examples from behavior>
- Feedback granularity: <which principles got detailed, expensive feedback; which remained vague>

### What Counts as Harm
- Specific harms flagged by the system: <list with operational definitions from actual refusals or warnings>
- Harms *not* named in the constitution: <categories the system causes but does not refuse>

### Whose Interests Are Protected
- Stakeholder positions centered in the constitution: <whose interests the framework makes salient>
- Stakeholder positions marginalized or absent: <whose interests are not the constitution's problem>

### Where Constitution and Behavior Diverge
- Cases where actual behavior contradicts stated principles: <specific examples>
- Behaviors not predictable from the constitution alone: <what else is shaping the system>
- Cases where the constitution is ambiguous or silent: <how the system handles them>

### History of the Constitution
- Principles added in response to: <observed failures, external pressure, red-team findings>
- Principles removed or downweighted: <when and why>

### Conversation with Other Stances
- What a political-economy reading would add (material incentives for principle drift): <brief>
- What a systems-level reading would add (guardrails and architecture outside the constitution): <brief>
- What a stakeholder-impact stance would add (distributional and temporal questions the constitution misses): <brief>

### Confidence: high | medium | low
<basis: how directly the constitution exposes its principles in training data or system logs; how closely actual behavior aligns with stated principles; whether divergences are explained or remain opaque>
```
