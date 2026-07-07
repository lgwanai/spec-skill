---
name: spec-plan
description: "Research and create an executable PLAN.md for a specific phase. Runs discovery questions, research, and generates atomic task plans with XML structure. Supports PRD-driven planning (--prd), vertical MVP mode (--mvp), and gap-closure mode (--gaps)."
argument-hint: "<phase-number> [--prd <file>] [--mvp] [--gaps]"
---

# /spec-plan — Plan a Phase

Trigger the `spec-skill` skill and execute the phase planning workflow.

## Flags

- `--prd <file>` — PRD-driven mode. Read requirements from the given PRD/acceptance-criteria file instead of running the interactive Discuss step. Parse the file's requirements into `CONTEXT.md` automatically and skip questioning entirely. Use when requirements are already locked externally.
- `--mvp` — Vertical MVP mode. Organize tasks as feature slices (UI → API → DB) instead of horizontal layers. On Phase 1 of a new project, also emit `SKELETON.md` (Walking Skeleton: a minimal end-to-end runnable skeleton built first, then iterated on). Can be persisted on a phase via `**Mode:** mvp` in ROADMAP.md so subsequent plans inherit it.
- `--gaps` — Gap-closure mode. Read `VERIFICATION.md` and extract the recorded gaps (failed verifications, missing must-haves). Generate a targeted fix plan that closes each gap, skipping fresh research. Use after `/spec-verify` surfaces gaps.

`--prd` and `--gaps` are mutually exclusive (both supply requirements from a file instead of the conversation). `--mvp` may combine with either.

## Workflow

1. **Load Context** — Read PROJECT.md, ROADMAP.md, STATE.md, and prior phase summaries. In `--prd` mode, also read the PRD file and parse its requirements into `CONTEXT.md`. In `--gaps` mode, read `VERIFICATION.md` and extract the gap list.
2. **Discuss (BLOCKING)** — Ask phase-specific clarifying questions about scope, constraints, interfaces, and acceptance criteria. Use `references/questioning.md` for patterns. **Skip in `--prd` and `--gaps` modes** — requirements come from the file, not the conversation.
3. **Research** — Investigate implementation approaches, libraries, and patterns for this phase. **Skip in `--gaps` mode** — the gap list already scopes the work.
4. **Create PLAN.md** — Generate the executable plan following `templates/PLAN.md`:
   - Must_haves (truths, artifacts, key_links) for goal-backward verification
   - XML task structure with `<read_first>`, `<acceptance_criteria>`, concrete values
   - Wave assignment for parallel execution
   - User_setup for external services
   - **`--mvp`:** organize tasks as vertical feature slices (UI → API → DB) rather than horizontal layers; on Phase 1 of a new project, also write `SKELETON.md` describing the minimal end-to-end runnable skeleton to build first
   - **`--gaps`:** one task per recorded gap, each with acceptance criteria derived from the corresponding failed verification
5. **Review (BLOCKING)** — Present full plan, **STOP and WAIT** for user confirmation

## What You Produce

- `.planning/phases/XX-name/XX-CONTEXT.md` — Discovery decisions (or PRD-parsed requirements in `--prd` mode)
- `.planning/phases/XX-name/XX-RESEARCH.md` — Technical research (omitted in `--gaps` mode)
- `.planning/phases/XX-name/XX-YY-PLAN.md` — Executable implementation plan
- `.planning/phases/XX-name/SKELETON.md` — Walking Skeleton spec (only in `--mvp` on Phase 1 of a new project)

## Key Rules

- 2-3 tasks per plan, ~50% context max
- Prefer vertical slices over horizontal layers (default in `--mvp`, encouraged otherwise)
- Every task must have grep-verifiable acceptance criteria
- Reference prior SUMMARYs only when genuinely needed (not reflexive chaining)
- External services → declare in `user_setup` frontmatter
- In `--gaps` mode, every task must trace back to a named gap in `VERIFICATION.md`
