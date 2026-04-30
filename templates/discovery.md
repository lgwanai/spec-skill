# Discovery / Context Template

Template for `NN-CONTEXT.md` or `NN-DISCOVERY.md` — phase discussion decisions and context.

---

## File Template

```markdown
# Phase [N]: [Name] — Discovery Context

**Created:** [YYYY-MM-DD]
**Source:** Phase discussion session

## Phase Scope

**What this phase builds:**
[Brief description of what this phase delivers — the user's words and framing.]

**What this phase does NOT build:**
- [Explicit exclusion 1]
- [Explicit exclusion 2]

## Design Decisions

### Decision 1: [Title]
- **Context:** [Why this decision was needed]
- **Options considered:**
  - Option A: [Description] — [Tradeoffs]
  - Option B: [Description] — [Tradeoffs]
- **Decision:** [Chosen option]
- **Rationale:** [Why this was chosen]

### Decision 2: [Title]
- **Context:** [Why this decision was needed]
- **Options considered:**
  - Option A: [Description] — [Tradeoffs]
- **Decision:** [Chosen option]
- **Rationale:** [Why this was chosen]

## User Preferences

- **[Category]:** [Preference captured during discussion]
- **[Category]:** [Preference captured during discussion]

## Assumptions

- [Assumption 1 — what we're assuming without explicit confirmation]
- [Assumption 2]

## Open Questions Resolved

- **Q:** [Question asked during discussion]
  **A:** [Answer provided]

- **Q:** [Question asked during discussion]
  **A:** [Answer provided]

## Constraints

- **[Type]:** [Constraint] — [Reason]
- **[Type]:** [Constraint] — [Reason]

## Technical Notes

[Any technical context, architecture hints, or implementation guidance captured during discussion.]

## References

- `.planning/PROJECT.md`
- `.planning/ROADMAP.md`
- `.planning/STATE.md`
- `.planning/REQUIREMENTS.md`
```

---

## Guidelines

**Purpose:**
This document captures everything decided during the phase discussion step. It feeds directly into:
1. **Research:** Researcher knows what patterns to investigate
2. **Planning:** Planner knows what decisions are locked in

**What belongs here vs PLAN.md:**
- CONTEXT.md: WHAT we decided and WHY
- PLAN.md: HOW we implement those decisions

**Writing good decisions:**
- Always include context (why was this needed?)
- Always include alternatives considered (what else could we have done?)
- Always include rationale (why this choice?)
- This prevents revisiting decisions during implementation

**Assumptions:**
- Be explicit about what you're assuming
- Mark as unconfirmed if the user didn't explicitly agree
- Plan-phase should surface unconfirmed assumptions to the user

**When to create:**
- After every phase discussion step
- Before research and planning
- Update if new decisions are made during planning
