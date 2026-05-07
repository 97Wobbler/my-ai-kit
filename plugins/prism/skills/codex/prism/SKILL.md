---
name: "prism"
description: "User-facing entry point for the Prism plugin. Use this skill to EXPLAIN what Prism is and to CREATE new instruments (lens / frame / model / stance / heuristic) from a named framework. Triggers on \"/prism\", \"/prism help\", \"/prism <framework>\", \"prism이 뭐야?\", \"prism 소개해줘\", \"prism 써보고싶어\", \"새 lens 만들어줘\", \"새 렌즈/프레임 만들어줘 <X>\", \"make a lens\", \"create a new prism instrument\", \"add <framework> as a frame\". NOT for browsing or looking up what already exists in the catalog — route those requests to the `search` skill instead. NOT for loading instruments into subagents — route those to the `fetch` skill."
---

# Prism

This skill was compiled from a Skill Forge runtime-neutral spec for the
Codex CLI runtime.

Source spec: `plugins/prism/specs/prism.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- Use `request_user_input` only in Plan Mode. In Default mode, ask a concise direct question and wait.
- For manual file edits, use `apply_patch` and preserve unrelated user changes.
- Use network access only when current or external facts are required.
- Run the relevant validation checks before reporting completion.

# prism (router)

This skill is a **thin router** for the Prism plugin's user-facing entry
point. It does not contain the about-text, the interview protocol, or the
quick-reference help itself — those live in `references/`. The router's
only job is to classify the user's request into one of three intents and
load the matching reference file.

## Routing logic

Classify the incoming request into exactly one of the three intents
below. When ambiguous, default to **about** (first-contact friendliness).

1. **About / explain** — the user wants to know what Prism is.
   - Triggers: `/prism` with no arguments, "what is prism?", "prism이
     뭐야?", "prism 소개해줘", "what does this plugin do?", "prism 써보고싶어",
     or any first-contact phrasing without a named framework.
   - Action: load `references/prism/about.md` in full and follow
     its instructions exactly. Do not paraphrase it from memory.

2. **Create / make** — the user names a specific framework or
   methodology they want turned into a Prism instrument.
   - Triggers: "/prism <framework name>", "create a lens for X", "add a
     frame for Y", "새 렌즈 만들어줘 Z", "I want to add PASTA threat
     modeling", "make an instrument for <name>". The tell: there is a
     concrete framework in the request.
   - Action: load `references/prism/make.md` in full and follow
     its interview protocol exactly. The full 5-class decision tree and
     the per-class file-format reminders live in that file plus
     `CLASSES.md`.

3. **Help / quick reference** — the user wants short usage docs.
   - Triggers: "/prism help", "/prism usage", "how do I use prism",
     "prism 사용법".
   - Action: load `references/prism/help.md` in full and render
     it to the user.

## NOT this skill — route to search or fetch

If the user is asking **what instruments already exist** (a lookup or
browse request), stop here and route them to the `search` skill.
Do not try to answer catalog queries from this router. Signals that this
is a `search` job, not a `/prism` job:

- "what lenses exist for security?"
- "show me the catalog", "what's in the prism catalog?"
- "do we already have a frame for prioritization?"
- "list instruments for <domain>"
- "any heuristics for <topic>?"

In those cases, tell the user one sentence: "That is the `search`
skill's job — invoke it and it will walk the 3-layer catalog for you."
Do not enumerate catalog entries from this skill.

If the user wants to **load instruments for a subagent prompt**, route them to the `fetch` skill.
Signals that this is a `fetch` job:

- "이 instrument를 서브에이전트에 넘겨줘"
- "fetch stride for my subagent"
- "instrument 로드해줘"

If the user wants **multiple agents to debate, review, brainstorm, or
find solutions together**, route them to the `debate` skill.
Signals that this is a `debate` job:

- "여러 관점에서 분석해줘", "에이전트들끼리 토론해줘"
- "다각도 리뷰해줘", "브레인스토밍해줘"
- "해결책 찾아줘 — 여러 에이전트로", "debate", "consensus"

Editing an existing instrument is also out of scope: open and edit the
file directly. Building an agent config is also out of scope: use Claude
Code's native `/agents` flow; Prism only supplies the catalog and the
cookbook recipes.

## File loading protocol

The router loads **exactly one** reference file per invocation:

- Decide the intent using the rules above.
- Read the corresponding file in full (`references/prism/about.md`,
  `references/prism/make.md`, or `references/prism/help.md`).
- Execute its instructions as if they were this skill's body.
- Never summarize, paraphrase, or reconstruct a reference file from
  memory — always open and read it.
- **Do not narrate routing or file-loading decisions to the user** —
  render the reference file's content directly, without meta commentary
  about which intent was classified or which file was opened.

The five Prism classes (**lens, frame, model, stance, heuristic**) are
defined in `CLASSES.md` at the plugin root. Both `references/prism/about.md`
and `references/prism/make.md` assume that taxonomy; the router itself does not
need to restate it.

## Runtime Overrides

In Codex, plugin skills are invoked through the installed skill name, for example `$prism`, `use prism:prism`, or a natural-language request that matches this skill.
Use `request_user_input` only in Plan Mode. In Default mode, ask concise plain-text questions and wait when the save layer or instrument details are blocking.
For manual file edits, prefer `apply_patch` and preserve unrelated user changes in project/global Prism layers.
