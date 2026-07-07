---
name: spec-execute
description: "Execute all plans for a phase in waves. Runs tasks with atomic commits, verification after each task, and generates SUMMARY.md. Supports wave filtering, gap-only, and interactive modes."
argument-hint: "<phase-number> [--wave N] [--gaps-only] [--interactive]"
---

# /spec-execute — Execute a Phase

Trigger the `spec-skill` skill and execute the phase execution workflow.

See `workflows/execute-plan.md` for the complete execution procedure.

## Optional Flags

Flags are documentation-only — not automatically active. A flag is active **only when its literal token appears in `$ARGUMENTS`**. If a documented flag is absent from `$ARGUMENTS`, treat it as inactive. Do not infer a flag is active just because it is documented here or mentioned inside a plan file.

- `--wave N` — Execute only Wave `N` in the phase. Use for pacing, quota management, or staged rollout. Phase verification/completion still only happens when no incomplete plans remain after the selected wave finishes.
- `--gaps-only` — Execute only gap-closure plans (plans with `gap_closure: true` in frontmatter). Use after `/spec-verify` creates fix plans.
- `--interactive` — Execute plans sequentially inline with user checkpoints between every task. Lower token usage, pair-programming style. Best for small phases, bug fixes, and verification gaps. (spec-skill is self-contained and runs inline by default; this flag makes the between-task checkpoints explicit rather than only at `checkpoint:*` tasks.)

**Active flags are derived from `$ARGUMENTS`:**

- `--wave N` is active only if the literal `--wave` token is present in `$ARGUMENTS`
- `--gaps-only` is active only if the literal `--gaps-only` token is present in `$ARGUMENTS`
- `--interactive` is active only if the literal `--interactive` token is present in `$ARGUMENTS`
- If none of these tokens appear, run the standard full-phase execution with no flag-specific filtering

## Workflow

1. **Pre-Execution** — Load context (STATE.md, PROJECT.md, PLAN.md), validate readiness, check user_setup
2. **Filter Plans** *(if flags active)*:
   - `--wave N` → select only plans with `wave: N`
   - `--gaps-only` → select only plans with `gap_closure: true` in frontmatter
3. **Execute in Waves** — Group plans by `wave` number. Within a wave, plans are independent and run in flexible order; waves execute sequentially. `--wave N` runs only that wave.
4. **Per-Task** — Read first → implement → verify → atomic commit. In `--interactive`, pause for a user checkpoint between every task.
5. **Checkpoints** — Pause at `checkpoint:*` tasks (and between tasks in `--interactive`), present to user, resume on approval
6. **Post-Execution** — Create SUMMARY.md, update STATE.md, update PROJECT.md if needed. Phase verification/completion only fires when no incomplete plans remain.

## Wave Execution Pattern

```
WAVE 1:   Plan 01, Plan 02     # Independent, no overlap
WAVE 2:   Plan 03, Plan 04     # Depend on wave 1
WAVE 3:   Plan 05              # Depends on plans 03+04

--wave 2      → only Plans 03, 04 (phase not marked complete)
--gaps-only   → only plans with gap_closure: true
--interactive → checkpoints between every task
```

## What You Produce

- Code changes with atomic commits per task
- `.planning/phases/XX-name/XX-YY-SUMMARY.md` — Post-execution summary with frontmatter

## Key Rules

- Build/test must pass after each task before committing
- Do NOT proceed past a failing verification
- 3 consecutive failures → document, consult debugging references, create checkpoint for user
- Context window filling → complete current task, commit, create `.continue-here.md`
- `--wave N` does not mark the phase complete if other waves remain incomplete
- `--gaps-only` is the natural pairing with `/spec-verify` fix plans
