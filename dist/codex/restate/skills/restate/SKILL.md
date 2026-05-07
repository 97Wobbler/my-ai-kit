---
name: "restate"
description: "Meta-analyze and restate user requests to verify comprehension before execution. Triggers when user wants to confirm understanding, asks you to paraphrase their request, or says \"내 말 이해했어?\", \"내가 무슨 말 하는지 알겠어?\", \"do you understand?\", \"do you understand what I mean?\", \"can you understand me?\", \"restate\", \"paraphrase what I asked\""
---

# Restate

This skill was compiled from a Skill Forge runtime-neutral spec for the
Codex CLI runtime.

Source spec: `specs/restate.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- No special runtime capabilities are required.

**Activation Principle**: Leverage expert requirement engineering knowledge to surface hidden assumptions and clarify ambiguities in user requests.

## Role

When user invokes this skill: **DO NOT execute the original request**. Instead, perform meta-analysis and restate their request to verify mutual understanding.

## Output Language

**CRITICAL**: ALWAYS respond to the user in **the same language** being used in the current conversation when presenting your restatement analysis. Match the user's language choice throughout the restatement.

## Restatement Structure

Present your analysis in this 4-part structure:

### 1. Core Request
"Your request: [one-sentence summary]"

### 2. My Understanding
- **Goal**: What are you trying to achieve?
- **Scope**: Where/what does this apply to?
- **Constraints**: Any special conditions to consider?
- **Assumptions**: [implicit assumptions I'm inferring]

### 3. Unclear Aspects
[List anything ambiguous as specific questions]

### 4. Confirmation
"Is my understanding correct?"

## Context Boundaries

**Available Context**:
- User's message immediately before the `/restate` command
- Conversation history (last 5 turns) for resolving implicit references
- Any files, code, or topics mentioned in the original request

**How to Use Context**:
- If request references "this file", "that module" -> Check conversation for what was discussed
- If request uses pronouns ("it", "that", "them") -> Resolve from recent messages
- If request seems incomplete or assumes prior context -> Look for setup in previous turns

**Example**:
```text
User: "Let's refactor the authentication module"
User: "Add better error handling"
User: /restate

Understand "Add better error handling" refers to "the authentication module"
```

## Execution Rules

**PROHIBITED Actions**:
- Execute the original request
- Start any work
- Read or modify files
- Run any commands

**REQUIRED Actions**:
- Analyze only, do not execute
- Surface implicit assumptions explicitly
- Convert ambiguities into specific questions
- Present output in the user's language

## Success/Failure Criteria

**SUCCESS Indicators**:
- User confirms with "yes", "correct", "that's right"
- At least 1 hidden assumption surfaced
- Ambiguous aspects converted to concrete questions

**FAILURE Signals**:
- User responds "that's not what I meant"
- You introduced concepts not in the original request
- You started execution without confirmation

## Error Handling

- **No prior request found** -> Respond: "There is no request to restate. Please provide a request first."
- **Request is already crystal clear** -> Still perform restatement, but note: "This request is already very clear"
- **Request is too vague to analyze** -> Ask: "This request is too brief. Could you provide more details?"

## Runtime Overrides

Do not use request_user_input for this skill; produce the restatement directly in the conversation.
