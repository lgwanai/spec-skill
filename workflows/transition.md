# Phase Transition Workflow

Workflow for transitioning between phases — completing current phase and preparing for the next.

---

## Transition Steps

### 1. Verify Current Phase Completion

Before transitioning, confirm:
- [ ] All plans in current phase have SUMMARY.md files
- [ ] Verification has passed (VERIFICATION.md exists and shows passing status)
- [ ] UAT completed (UAT.md exists, if applicable)
- [ ] No critical unresolved issues
- [ ] All task commits are clean and pushed

### 2. Update PROJECT.md

**Requirements — Validated:**
- Move completed requirements from Active to Validated
- Format: `- REQ-01: [Description] — shipped in Phase [N]`
- Add checkmark prefix

**Requirements — Active:**
- Remove completed requirements
- Add any new requirements discovered during the phase

**Requirements — Out of Scope:**
- Move any invalidated requirements here with reasoning
- Review existing exclusions — are reasons still valid?

**Key Decisions:**
- Add any significant decisions made during the phase
- Include rationale and outcome (where known)

**Context:**
- Update with new information (user feedback, metrics, technical discoveries)

**"What This Is":**
- Review: Does the product description still match reality?
- Update if the phase significantly changed the product

### 3. Update ROADMAP.md

- Mark current phase as complete in the progress table
- Add completion date
- Update progress indicators

### 4. Update STATE.md

- Update current position: Phase [N+1], Plan 0, Status: "Ready to discuss"
- Update progress bar
- Move resolved blockers from "Blockers/Concerns"
- Add any new blockers or concerns for next phase
- Update performance metrics (phase duration, total plans completed)
- Update accumulated context (new decisions, learnings)
- Set "Last activity" timestamp
- Update "Session Continuity" section

### 5. Context Assembly for Next Phase

**For the next phase's discussion:**
- Summarize what was built in current phase (one paragraph)
- List all new files/modules created
- List all key decisions that affect future phases
- Note any patterns established that future phases should follow
- Flag any known blockers or dependencies for the next phase

### 6. Transition Checkpoint

**Present to user:**
```
Phase [N] Complete.

What was accomplished:
- [Key accomplishment 1]
- [Key accomplishment 2]
- [Key accomplishment 3]

Next phase: Phase [N+1] — [Name]
Goal: [What Phase N+1 delivers]

Ready to proceed to Phase [N+1] discussion?
```

**Wait for user confirmation** before beginning next phase discussion.

---

## Post-Transition

### After user confirms:
1. Begin `/discuss-phase` for Phase N+1
2. Load context: PROJECT.md, STATE.md, ROADMAP.md
3. Present phase goal from ROADMAP
4. Begin discovery questions

### If user wants to pause:
1. Create `.continue-here.md` with:
   - Completed phase reference
   - Next phase ready to discuss
   - All context assembled
2. Update STATE.md with pause position

---

## Transition Checklist

- [ ] All current phase plans completed and summarized
- [ ] Verification passed
- [ ] PROJECT.md updated (requirements, decisions, context)
- [ ] ROADMAP.md updated (progress)
- [ ] STATE.md updated (position, metrics, context)
- [ ] Context assembled for next phase
- [ ] User confirmed transition
- [ ] Next phase discussion ready to begin
