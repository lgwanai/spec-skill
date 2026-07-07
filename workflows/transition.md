# Phase Transition Workflow

Workflow for transitioning between phases — completing the current phase and preparing for the next.

> Internal workflow, invoked by `/spec-execute` after verification or by the orchestrator inline. Users drive phase progression via `/spec-plan`, `/spec-execute`, `/spec-verify`, `/spec-next`.

**Required reading before transition:**
1. `.planning/STATE.md`
2. `.planning/PROJECT.md`
3. `.planning/ROADMAP.md`
4. Current phase's plan files (`*-PLAN.md`)
5. Current phase's summary files (`*-SUMMARY.md`)

---

## Transition Steps

### 1. Verify Current Phase Completion

**Check plan summaries:**
- Count `*-PLAN.md` files in the current phase directory
- Count `*-SUMMARY.md` files in the same directory
- If counts match → all plans complete
- If counts don't match → incomplete (see partial_completion below)

Confirm:
- [ ] Verification has passed (`VERIFICATION.md` exists and shows passing status)
- [ ] UAT completed (`UAT.md` exists, if applicable)
- [ ] No critical unresolved issues
- [ ] All task commits are clean and pushed

**Check for verification debt in this phase:**

Scan the current phase's `*-UAT.md` and `*-VERIFICATION.md` for outstanding items:

```bash
OUTSTANDING=""
for f in .planning/phases/XX-current/*-UAT.md .planning/phases/XX-current/*-VERIFICATION.md; do
  [ -f "$f" ] || continue
  grep -q "result: pending\|result: blocked\|status: partial\|status: human_needed\|status: diagnosed" "$f" \
    && OUTSTANDING="$OUTSTANDING\n$(basename $f)"
done
```

If `OUTSTANDING` is not empty, append to the completion confirmation message (regardless of mode):

```
Outstanding verification items in this phase:
{list filenames}

These will carry forward as debt. Review them before the next phase.
```

This does NOT block transition — it ensures the user sees the debt before confirming.

**Partial completion (incomplete plans):**

SAFETY RAIL: Skipping incomplete plans is a destructive action — ALWAYS prompt for confirmation regardless of mode.

Present:

```
Phase [X] has incomplete plans:
- {phase}-01-SUMMARY.md ✓ Complete
- {phase}-02-SUMMARY.md ✗ Missing
- {phase}-03-SUMMARY.md ✗ Missing

⚠️ Safety rail: Skipping plans requires confirmation (destructive action)

Options:
1. Continue current phase (execute remaining plans)
2. Mark complete anyway (skip remaining plans)
3. Review what's left
```

Respect user judgment — they know if the work matters.

**If marking complete with skipped plans:**
- Update ROADMAP with the real count, e.g. "2/3 plans complete" (not "3/3")
- Note in the transition message which plans were skipped

**Cleanup stale handoffs:**

```bash
ls .planning/phases/XX-current/.continue-here*.md 2>/dev/null || true
```

If found, delete them — the phase is complete, so handoffs are stale.

### 2. Update PROJECT.md

Evolve PROJECT.md to reflect learnings from the completed phase. Read the phase `*-SUMMARY.md` files and assess:

**Requirements — Validated:**
- Any Active requirements shipped in this phase? Move to Validated with phase reference.
- Format: `- ✓ [Requirement] — shipped in Phase [N]`

**Requirements — Active:**
- Remove completed requirements
- Add any new requirements discovered during the phase (emerged requirements): `- [ ] [New requirement]`

**Requirements — Out of Scope:**
- Move any invalidated requirements here with reason: `- [Requirement] — [why invalidated]`
- Review existing exclusions — are reasons still valid?

**Key Decisions:**
- Extract decisions from `SUMMARY.md` files
- Add to Key Decisions with rationale and outcome (where known)

**Context:**
- Update with new information (user feedback, metrics, technical discoveries)

**"What This Is":**
- Review: Does the product description still match reality?
- Update if the phase meaningfully changed the product
- Keep it current and accurate

Update the "Last updated" footer:
```markdown
---
*Last updated: [date] after Phase [X]*
```

**Example evolution:**

Before:
```markdown
### Active

- [ ] JWT authentication
- [ ] Real-time sync < 500ms
- [ ] Offline mode

### Out of Scope

- OAuth2 — complexity not needed for v1
```

After (Phase 2 shipped JWT auth, discovered rate limiting needed):
```markdown
### Validated

- ✓ JWT authentication — Phase 2

### Active

- [ ] Real-time sync < 500ms
- [ ] Offline mode
- [ ] Rate limiting on sync endpoint

### Out of Scope

- OAuth2 — complexity not needed for v1
```

### 3. Update ROADMAP.md

- Mark current phase as complete in the progress table (checkbox `[x]` with today's date)
- Add completion date
- Update plan count to final (e.g. "3/3 plans complete", or "2/3 plans complete" if skipped)
- Update progress indicators
- Update the Progress table (Status → Complete, with date)

### 4. Update STATE.md

**Current position:**
- Phase [N+1], Plan 0, Status: "Ready to plan"
- Update progress bar
- Set "Last activity" timestamp

**Accumulated Context — Decisions:**
- Note recent decisions from this phase (3–5 max)
- Full log lives in PROJECT.md Key Decisions table

**Accumulated Context — Blockers/Concerns:**
- Review blockers from the completed phase
- If addressed in this phase → remove from list
- If still relevant for future → keep with phase prefix (e.g. `[Phase 2]`)
- Add any new concerns from the completed phase's summaries

Example:
```
Before:
- ⚠️ [Phase 1] Database schema not indexed for common queries
- ⚠️ [Phase 2] WebSocket reconnection behavior on flaky networks unknown

After (if database indexing was addressed in Phase 2):
- ⚠️ [Phase 2] WebSocket reconnection behavior on flaky networks unknown
```

**Project Reference:**
- Update date and current focus to reflect the transition
```markdown
## Project Reference

See: .planning/PROJECT.md (updated [today])

**Core value:** [Current core value from PROJECT.md]
**Current focus:** [Next phase name]
```

**Performance metrics:**
- Update phase duration, total plans completed

**Session Continuity:**

```markdown
Last session: [today]
Stopped at: Phase [X] complete, ready to plan Phase [X+1]
Resume file: None
```

### 5. Context Assembly for Next Phase

**For the next phase's planning:**
- Summarize what was built in the current phase (one paragraph)
- List all new files/modules created
- List all key decisions that affect future phases
- Note any patterns established that future phases should follow
- Flag any known blockers or dependencies for the next phase

### 6. Transition Checkpoint

**Present to user:**
```
Phase [X] Complete.

What was accomplished:
- [Key accomplishment 1]
- [Key accomplishment 2]
- [Key accomplishment 3]

Next phase: Phase [X+1] — [Name]
Goal: [What Phase N+1 delivers]

Ready to proceed to Phase [X+1] planning?
```

Wait for user confirmation before beginning the next phase.

---

## Post-Transition

### After user confirms:
1. Begin `/spec-plan` for Phase N+1 (spec-skill merges phase discussion into planning; load ROADMAP goal and run discovery questions as part of planning)
2. Load context: PROJECT.md, STATE.md, ROADMAP.md
3. Present phase goal from ROADMAP
4. Begin discovery questions inline

### If user wants to pause:
1. Create `.continue-here.md` (see `templates/continue-here.md`) with:
   - Completed phase reference
   - Next phase ready to plan
   - All context assembled
2. Update STATE.md with the pause position

---

## Transition Checklist

- [ ] All current phase plans completed and summarized (or user chose to skip with confirmation)
- [ ] Verification debt surfaced (outstanding UAT/VERIFICATION items listed)
- [ ] Stale `.continue-here*.md` handoffs deleted
- [ ] PROJECT.md evolved (requirements, decisions, description if needed)
- [ ] ROADMAP.md updated (completion status, plan count, date)
- [ ] STATE.md updated (position, metrics, blockers, context, session continuity)
- [ ] Context assembled for next phase
- [ ] User confirmed transition
- [ ] Next phase planning ready to begin
