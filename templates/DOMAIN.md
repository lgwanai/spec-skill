# Domain Model Template

Template for `.planning/DOMAIN.md` - the project's shared business vocabulary.

Use this artifact when the product involves people interacting with a system: web apps, mobile/desktop apps, CLIs used by humans, admin tools, business workflows, role-specific behavior, collaboration, or any feature where different people can do different things.

For pure libraries, infrastructure work, internal refactors, or machine-only jobs, write "Not required for this project/phase" with the reason instead of forcing a full model.

<template>

```markdown
# Domain Model: [Project Name]

**Defined:** [date]
**Interaction Gate:** [Required / Not required]
**Reason:** [Why human-domain modeling is or is not needed]

## Domain Summary

[One paragraph explaining the business world this system represents. Use the user's language first, then normalize terms.]

## Core Concepts

| Concept | Meaning | In Scope | Out of Scope |
|---------|---------|----------|--------------|
| [Concept] | [Plain-language definition] | [What this means here] | [What this does not mean here] |

## Progressive Concept Decomposition

Start broad, confirm the big modules/entities, then drill down only where more detail is needed for requirements, data modeling, behavior, derived access rules, or verification.

| Level | Parent Concept | Child Concept | Why It Exists | Decompose Further? |
|-------|----------------|---------------|---------------|--------------------|
| 1 | [Root / Product Area] | [Top-level module/entity] | [User-visible or business reason] | [Yes / No / Later] |
| 2 | [Parent] | [Child entity/module] | [What this child explains or enables] | [Yes / No / Later] |

## Decomposition Notes

- **Confirmed top-level concepts:** [Concept A, Concept B]
- **Needs deeper design now:** [Concept that affects current requirements or data]
- **Do not expand yet:** [Concept intentionally left coarse until later phase]

## Concept Attributes

### [Concept Name]

**Definition:** [What this thing is]

**Required attributes:**
- `[attribute]` - [meaning, type/range if known]

**Optional attributes:**
- `[attribute]` - [meaning]

**Lifecycle / states:**
- [State 1] -> [State 2] -> [State 3]

**Business rules / invariants:**
- [Rule that must always hold]

## Relationships

| Source | Relationship | Target | Cardinality | Notes |
|--------|--------------|--------|-------------|-------|
| [Concept A] | [owns/contains/creates/uses] | [Concept B] | [1:1 / 1:N / N:M] | [Boundary or rule] |

## Vocabulary Decisions

| Term | Use This Meaning | Avoid / Do Not Mean | Decision |
|------|------------------|---------------------|----------|
| [Term] | [Definition] | [Common confusion] | [Confirmed / Assumed / Open] |

## Open Domain Questions

- [ ] [Question that affects data model, derived access rules, or workflows]

---
*Domain model defined: [date]*
*Last updated: [date] after [trigger]*
```

</template>

<guidelines>

**When this is required:**
- A human uses the system through UI, CLI, app, dashboard, chat, form, or workflow.
- Different actors may have different allowed operations, goals, or views.
- The product manipulates business objects with identity, state, ownership, or lifecycle.
- The data model would be unstable if terms are left vague.

**When this can stay lightweight:**
- Pure code libraries, internal refactors, developer tooling without business objects.
- Infrastructure setup, CI changes, bug fixes with no product behavior change.
- Machine-to-machine integrations where actors and access rules are already externally defined.

**Concept definition rule:**
Define what the thing is before listing features about it. A "card" is not a button or screen; it is a domain object with meaning, attributes, rules, and relationships.

**Progressive decomposition rule:**
Do not fully explode the domain on the first pass. First confirm large concepts/modules, then recursively decompose the concepts that block system design. Stop when the current planning work has enough information for requirements, data shape, behavior, and verification.

**Entity/module rule:**
Treat domain concepts as modules or entities when useful. A domain model can contain product modules, business entities, and supporting concepts, but each entry must explain what it represents and why it matters.

**Scope rule:**
Every important concept should say what it excludes. This prevents broad terms from absorbing unrelated features later.

**Stability rule:**
If a concept appears in multiple roles' use cases, define it here before writing requirements.

</guidelines>

<example>

```markdown
# Domain Model: Word Memory Cards

**Defined:** 2026-07-08
**Interaction Gate:** Required
**Reason:** Students and parents interact with learning objects in different ways.

## Domain Summary

The system helps learners review vocabulary through word memory cards. A card represents one vocabulary item plus learning material and review state; decks group cards for practice.

## Core Concepts

| Concept | Meaning | In Scope | Out of Scope |
|---------|---------|----------|--------------|
| Word Card | A reviewable vocabulary item | Word, meaning, example, pronunciation, memory state | A generic flashcard for any subject |
| Deck | A collection of word cards | Manually created or imported word groups | Full course curriculum |
| Review Session | One practice run through cards | Shows cards, records answers, updates state | Live class teaching |
| Memory State | Learner's current recall status | New, learning, remembered, difficult | Clinical learning diagnosis |

## Progressive Concept Decomposition

| Level | Parent Concept | Child Concept | Why It Exists | Decompose Further? |
|-------|----------------|---------------|---------------|--------------------|
| 1 | Learning Product | Word | The atomic vocabulary item being learned | Yes |
| 1 | Learning Product | Word Card | The reviewable representation of a word | Yes |
| 1 | Learning Product | Word Deck | A set of cards selected for practice | Later |
| 2 | Word | Spelling, meaning, pronunciation, example | These attributes determine what appears on a card | No |
| 2 | Word Card | Prompt side, answer side, memory state | These define review behavior | Yes |
| 3 | Word Card | Card display surface | The UI module that presents a card during review | No |

## Concept Attributes

### Word Card

**Definition:** A vocabulary item that a learner can review.

**Required attributes:**
- `word` - the vocabulary word
- `meaning` - explanation or translation
- `memory_state` - learner-specific recall state

**Optional attributes:**
- `example_sentence` - example usage
- `pronunciation` - phonetic text or audio reference

**Lifecycle / states:**
- Created -> Added to deck -> Reviewed -> Updated by learner performance

**Business rules / invariants:**
- A word card can exist in a deck before any learner has reviewed it.
- Memory state belongs to a learner's relationship with the card, not only to the card itself.
```

</example>
