# Use Cases Template

Template for `.planning/USE_CASES.md` - actors, roles, and the operations people perform on domain concepts.

Use this artifact when `DOMAIN.md` says the interaction gate is required. It connects people to domain objects before requirements and roadmap decomposition.

<template>

```markdown
# Use Cases: [Project Name]

**Defined:** [date]
**Depends on:** `.planning/DOMAIN.md`
**Interaction Gate:** [Required / Not required]

## Actors and Roles

| Actor / Role | Description | Primary Goal | Notes |
|--------------|-------------|--------------|--------------|
| [Role] | [Who this is in the user's words] | [What they are trying to accomplish] | [Relationship to the domain, not pre-designed access] |

## Role Relationships

| Relationship | Meaning | Notes |
|--------------|---------|-------|
| [Role A -> Role B] | [How these roles relate] | [Ownership, supervision, collaboration, delegation] |

## Use Case Matrix

| Use Case ID | Actor / Role | Domain Concept(s) | Goal / Operation | Outcome | Requirement IDs |
|-------------|--------------|-------------------|------------------|---------|-----------------|
| UC-001 | [Role] | [Concept] | [Action] | [Observable result] | [REQ-___] |

## Derived Access Rules

Do not design access rules first. Derive them from the use-case matrix.

| Status | Domain Concept | Operation | Actor(s) | Source / Reason |
|--------|----------------|-----------|----------|-----------------|
| allowed | [Concept] | [Operation] | [Roles that have a confirmed use case] | [UC-___] |
| denied | [Concept] | [Operation] | [Roles explicitly excluded] | [User-confirmed boundary / requirement] |
| unconfirmed | [Concept] | [Operation] | [Roles not yet discussed] | [Open question / future scope] |

## Use Case Details

### UC-001: [Use Case Name]

**Actor:** [Role]
**Domain concepts:** [Concepts from DOMAIN.md]
**Goal:** [What the actor wants]
**Preconditions:**
- [Condition that must already be true]

**Main flow:**
1. [Actor does something]
2. [System responds]
3. [Domain object changes or information is shown]

**Alternative / edge flows:**
- [What happens when the common case differs]

**Derived access boundary:**
- [What this actor can do because this use case exists]
- [What is explicitly denied]
- [What remains unconfirmed and must not be silently implemented]

**Acceptance signal:**
- [How we know this use case works]

## Out-of-Scope Actors / Use Cases

| Actor / Use Case | Reason |
|------------------|--------|
| [Excluded actor/action] | [Why excluded now] |

## Open Use-Case Questions

- [ ] [Question that changes roles, derived access rules, or workflows]

---
*Use cases defined: [date]*
*Last updated: [date] after [trigger]*
```

</template>

<guidelines>

**Actor rule:**
Avoid generic "user" when roles differ. Name the actor by their relationship to the system: student, parent, teacher, visitor, workspace owner, reviewer, operator, admin.

**Use-case rule:**
A use case is a role performing an operation on one or more domain concepts to get an outcome. It is not a screen, component, endpoint, or database table.

**Derived access rule:**
Access rules are not invented as a separate permission design. They fall out of actor-operation pairs and must use one of three statuses: `allowed`, `denied`, or `unconfirmed`. If Parent has "set deck scope" and Student does not, Student scope-setting is `unconfirmed` unless the user explicitly excludes it; do not expose or implement unconfirmed behavior. If the user later says Student can, add or update a use case first, then update requirements.

**Requirement handoff rule:**
Every user-facing v1 requirement should trace to at least one use case. If a requirement has no actor and no domain concept, it may be an implementation task rather than a product requirement.

**Continuity rule:**
Each use case should flow into requirements, roadmap success criteria, PLAN must_haves, and UAT. Do not rewrite the same behavior as an unrelated feature later.

</guidelines>

<example>

```markdown
# Use Cases: Word Memory Cards

**Defined:** 2026-07-08
**Depends on:** `.planning/DOMAIN.md`
**Interaction Gate:** Required

## Actors and Roles

| Actor / Role | Description | Primary Goal | Notes |
|--------------|-------------|--------------|--------------|
| Student | Learner reviewing vocabulary | Practice cards and track memory state | Learner under a parent-managed setup |
| Parent | Guardian supporting a learner | Manage decks and view learning records | Owns learner setup decisions |
| Visitor | Unauthenticated evaluator | Try a sample deck | No persisted learner data |

## Use Case Matrix

| Use Case ID | Actor / Role | Domain Concept(s) | Goal / Operation | Outcome | Requirement IDs |
|-------------|--------------|-------------------|------------------|---------|-----------------|
| UC-001 | Parent | Deck, Word Card | Create or edit a deck | Student has cards to review | CARD-01, DECK-01 |
| UC-002 | Parent | Deck, Word Card | Set card review scope | Student reviews only the selected range | DECK-02 |
| UC-003 | Student | Review Session, Word Card, Memory State | Review cards | Memory states update | REVW-01 |
| UC-004 | Parent | Review Session, Memory State | View learning records | Parent sees progress and difficult cards | REPT-01 |
| UC-005 | Visitor | Deck, Word Card | Try sample cards | Visitor experiences the product without account data | DEMO-01 |

## Derived Access Rules

| Status | Domain Concept | Operation | Actor(s) | Source / Reason |
|--------|----------------|-----------|----------|-----------------|
| allowed | Deck / Word Card | Set review scope | Parent | UC-002 |
| unconfirmed | Deck / Word Card | Set review scope | Student | Not requested for v1 |
| denied | Deck / Word Card | Set review scope | Visitor | Guest sample mode has no persisted setup |
| allowed | Word Card | Review | Student, Visitor for sample only | UC-003, UC-005 |
| unconfirmed | Word Card | Review as learner | Parent | Not requested for v1 |
| allowed | Memory State | View learning records | Parent | UC-004 |
| denied | Memory State | View learning records | Visitor | No persisted learner data |
```

</example>
