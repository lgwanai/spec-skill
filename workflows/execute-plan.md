# Execute Plan Workflow

Step-by-step workflow for executing a phase plan. This document guides the AI through plan execution with verification and state updates.

---

## Pre-Execution

### 1. Load Context
- Read `.planning/STATE.md` for current position
- Read `.planning/PROJECT.md` for project context
- Read the phase's `PLAN.md` file
- Read any dependency SUMMARY files referenced in the plan's `<context>` section

### 2. Validate Readiness
- [ ] STATE.md shows correct phase and plan
- [ ] All dependency plans have completed SUMMARY files
- [ ] Plan has `requirements` in frontmatter
- [ ] Plan has `must_haves` defined in frontmatter
- [ ] No blockers listed in STATE.md for this phase

### 3. Check for User Setup
- Review plan's `user_setup` frontmatter field
- If user_setup has entries:
  - Generate `{phase}-USER-SETUP.md` with checklist
  - Present to user BEFORE executing
  - Wait for user confirmation that setup is complete

---

## Execution

### 4. Execute Tasks Sequentially

For each `<task>` in the plan:

**Step 1: Read First**
- Read all files listed in `<read_first>`
- Read all files listed in `<files>` that will be modified
- Understand current state before making changes

**Step 2: Implement**
- Follow the `<action>` instructions precisely
- Use concrete values specified in the action
- Write tests first if this is a TDD plan (type: tdd)

**Step 3: Verify**
- Run the `<verify>` command or check
- Check all `<acceptance_criteria>`:
  - Grep-verify that expected strings exist in files
  - Run commands that prove behavior works
- If verification fails: fix, re-verify, do not proceed until passing

**Step 4: Commit**
- Commit with message: `type({phase}-{plan}): {task description}`
- Use conventional commit types: feat, fix, refactor, test, docs
- Each task gets its own atomic commit
- Do NOT squash multiple tasks into one commit

**Step 5: Handle Checkpoints**
- If task is type `checkpoint:*`:
  - Pause execution
  - Present checkpoint details to user
  - Wait for user response (explicit approval or decision)
  - Resume only after user responds

---

## Post-Execution

### 5. Create Summary
After all tasks complete:
- Create `.planning/phases/{phase}/{phase}-{plan}-SUMMARY.md`
- Follow the SUMMARY template structure
- Document:
  - Accomplishments (substantive one-liner)
  - Performance metrics (duration, files modified)
  - Task commits with hashes
  - Files created/modified
  - Decisions made
  - Deviations from plan
  - Issues encountered
  - User setup status (if applicable)
  - Next phase readiness

### 6. Update STATE.md
- Update current position (phase, plan, status)
- Note new decisions in accumulated context
- Update performance metrics
- Add any blockers or concerns
- Update progress bar
- Record last activity timestamp

### 7. Update PROJECT.md (if needed)
- Move completed requirements to Validated
- Add new Key Decisions if any
- Update "What This Is" if product evolved

---

## Verification Rules

### Auto-verification (no user needed)
- Build passes: `npm run build` or equivalent
- Type check passes: `tsc --noEmit` or equivalent
- Lint passes: `npm run lint` or equivalent
- Tests pass: `npm test` or equivalent

### Must-Haves Verification
After all plans in a phase complete:
- Verify `truths`: Each observable behavior is actually working
- Verify `artifacts`: Files exist with real content (not placeholders)
  - Check `min_lines` if specified
  - Check `exports` if specified  
  - Check `contains` if specified
- Verify `key_links`: Connections exist and match patterns
  - Grep for `pattern` in the source file
  - Verify the `via` mechanism is present

### Gap Handling
- Gaps found → Create fix plans
- Fix plans execute → Re-verify
- Cycle repeats until all must_haves pass

---

## Error Recovery

### If a Task Fails
1. Read error output carefully
2. Fix the specific issue (do NOT shotgun debug)
3. Re-run verification
4. If same failure 3 times:
   - Document the issue
   - Consult debugging references
   - If unresolved, create a checkpoint:decision task for user input

### If Build/Tests Break
1. Do NOT proceed to next task
2. Fix the breakage immediately
3. Commit the fix
4. Re-run all verification

### If Context Window Fills
1. Complete current task and commit it
2. Create `.continue-here.md` with current position
3. Update STATE.md with session continuity info
4. Pause and resume in fresh context
