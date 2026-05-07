# Film Critic — Composition Recipe

> **This is NOT an executable agent config.** It is a composition recipe — a
> narrative explaining how a set of Prism instruments can be combined for a
> given task. To actually build an agent, use Claude Code's native agent
> creation mechanism (`/agents` or a hand-written `.claude/agents/*.md`) and
> reference the instruments below manually. Prism is a catalog; the agent
> runtime lives in Claude Code.

## Persona / purpose

A film critic for narrative cinema, responsible for formal analysis of
craft (mise-en-scène, editing, sound) alongside interpretive readings of
the film as a cultural artifact. This recipe produces a two-layered
verdict: a craft assessment that is relatively stable across readers,
and an ideological reading that is openly stance-dependent, with the
two kept deliberately separate.

## Instruments used

### Lenses
- `library/lenses/film-theory/bordwells-formal-analysis.md` —
  **usage: always** — map the film's large-scale form (narrative form,
  plot/story split, principles of unity).
- `library/lenses/film-theory/mise-en-scene-analysis.md` —
  **usage: always** — staging, lighting, costume, performance, anchored
  to scenes.
- `library/lenses/film-theory/editing-analysis.md` —
  **usage: when-relevant** — used where cutting rhythm carries weight.
- `library/lenses/film-theory/sound-analysis.md` —
  **usage: when-relevant** — used where diegetic/non-diegetic contrast,
  score, or silence carries weight.
- `library/lenses/film-theory/cinematography-analysis.md` —
  **usage: when-relevant** — used where camera movement, framing, or
  lens choice carries weight.
- `library/lenses/film-theory/mckees-story-structure.md` —
  **usage: when-relevant** — screenplay-level verdicts (inciting
  incident, turning points, climax).

### Frames
- `library/frames/film-theory/genre-theory.md` —
  **usage: when-relevant** — locate the film in its generic tradition
  so that genre-breaking choices become the evaluable moves.
- `library/frames/film-theory/eisensteins-5-types-of-montage.md` —
  **usage: on-request** — reserved for films where editing is doing
  interpretive work beyond continuity.

### Stances
- `library/stances/film-theory/auteur-theory.md` —
  **usage: when-relevant** — applied when comparing across a director's
  filmography.
- `library/stances/film-theory/mulveys-male-gaze.md` —
  **usage: when-relevant** — applied when cinematography findings invite
  a reading of spectatorial position.
- `library/stances/humanities/marxist-criticism.md` —
  **usage: when-relevant** — applied when class coding is visible in the
  mise-en-scène.
- `library/stances/humanities/foucauldian-power-knowledge.md` —
  **usage: when-relevant** — applied when the narrative structure
  foregrounds surveillance, institutions, or knowledge circulation.
- `library/stances/literary-theory/feminist-criticism.md` —
  **usage: when-relevant** — applied when gender is structural to the
  film's arguments.
- `library/stances/literary-theory/psychoanalytic-criticism.md` —
  **usage: on-request** — reserved by explicit request.
- `library/stances/literary-theory/postcolonial-theory.md` —
  **usage: on-request** — reserved by explicit request.

### Heuristics
- `library/heuristics/general.md` — **usage: always** — Hanlon's Razor,
  Chesterton's Fence, Occam's Razor, applied as a sanity gate on the
  interpretive claims.

## Why this composition

This recipe deliberately splits craft from ideology. Bordwell and
mise-en-scène analysis are `always` because without a craft floor the
interpretive readings become free-floating essays. Editing, sound, and
cinematography are `when-relevant` because running all three on every
film produces generic paragraphs about shot lengths — the lens earns
its place only when the film foregrounds that element.

The stances are the most deliberate piece of the composition. Seven
are declared, but the instruction is explicit: pick them based on the
film's material, not by running every stance on every film. A labor
drama invites Marxist criticism; a film about surveillance invites
Foucault; a thriller with a female protagonist may invite Mulvey.
Running all seven by default produces theory-slop; running zero
produces a craft review that pretends it is objective. The `when-
relevant` tag encodes "choose deliberately" rather than "always apply."

The critical-read step is the methodologically important move: each
stance operates on findings from the Analyze step, not on the film
in isolation. This chains the interpretive reading to specific
observations (shot 47's framing, the mise-en-scène in scene 12) and
makes it anchorable. A stance-driven reading that cannot point to a
finding is rhetoric, not criticism.

Genre theory is placed at Classify, not Analyze, because it reframes
every subsequent finding: a genre-conforming choice is baseline craft
(not evaluable), while a genre-breaking choice is the move worth
writing about. Running it last would produce observations that genre
theory would have trivialized.

The heuristic gate is narrow and targets interpretive pathologies:
(1) Hanlon's Razor on any reading that imputes deliberate political
strategy to filmmakers (often it is genre convention or production
constraint), (2) Chesterton's Fence on "this scene is gratuitous"
claims, (3) Occam's Razor on readings that require multiple layered
allegories to hold together. These are exactly the failure modes
that distinguish earned criticism from ornamental criticism.

Trade-off: `auteur-theory` is `when-relevant` rather than `always`
because auteurism overreaches on a single-film review — it needs a
director's filmography to be grounded. Same logic for Eisenstein's
five types of montage: on-request because it is only diagnostic for
formalist or essayistic cinema.

## Workflow sketch (7-step pipeline)

| Step | Class(es) used | What happens |
|------|---------------|--------------|
| 1. Triage | — | Confirm Bordwell + mise-en-scène apply; decide which of editing/sound/cinematography earn passes; deliberately select stances based on the film's material. |
| 2. Classify | Frames (Genre theory) | Locate the film in its tradition; separate baseline craft from evaluable moves. |
| 3. Analyze | Lenses (Bordwell → mise-en-scène → selected additional lenses) | Anchor observations to timestamps or shot numbers. |
| 4. Model-interpret | Frame (Eisenstein's montage) | On-request only, for films where editing is doing interpretive work. |
| 5. Critical-read | Stances (selected) | Each stance reads the findings from step 3; readings are explicitly attributed to the stance that produced them. |
| 6. Sanity-gate | Heuristics (Hanlon, Chesterton, Occam) | Filter interpretive claims; drop readings that fail. |
| 7. Synthesize | All | Separate formal verdict from interpretive verdicts; mark interpretive anchors (scenes where multiple stances converge); leave productive tensions unresolved. |
