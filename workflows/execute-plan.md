# Execute Plan Workflow

Step-by-step workflow for executing a phase plan. This document guides the AI through plan execution with verification and state updates.

---

## Close-Out Invariant

For each executed plan, the only complete close-out order is:
`production-code commit(s) → SUMMARY commit → STATE/ROADMAP update`.

The only legal half-state is mid-production-commits while still actively working. Once production commits for a plan exist, returning without a committed SUMMARY.md is an illegal partial-plan state. The next execute must detect that condition before starting another plan.

---

## Pre-Execution

### 1. Load Context
- Read `.planning/STATE.md` for current position
- Read `.planning/PROJECT.md` for project context
- Read `.planning/DOMAIN.md` and `.planning/USE_CASES.md` when they exist
- Read `.planning/REQUIREMENTS.md` for requirement-to-use-case traceability
- Read the phase's `PLAN.md` file
- Read any dependency SUMMARY files referenced in the plan's `<context>` section

**If the plan contains an `<interfaces>` block:** These are pre-extracted type definitions and contracts. Use them directly — do NOT re-read the source files to discover types. The planner already extracted what you need.

### 2. Validate Readiness
- [ ] STATE.md shows correct phase and plan
- [ ] All dependency plans have completed SUMMARY files
- [ ] Plan has `requirements` in frontmatter
- [ ] Plan has `must_haves` defined in frontmatter
- [ ] If `scripts/validate_trace.py` exists, it passes before code edits
- [ ] For human-interaction plans, plan has `domain_trace.interaction_gate: required`
- [ ] For human-interaction plans, `domain_trace.use_cases`, `domain_trace.actors`, and `domain_trace.concepts` are not empty
- [ ] For human-interaction plans, `domain_trace.derived_access_rules` is present when roles perform different operations on the same concept
- [ ] No blockers listed in STATE.md for this phase
- [ ] No half-state for this plan: if production commits for this plan exist but SUMMARY.md is uncommitted, finalize the SUMMARY first before starting new work

**Domain-trace hard gate:** If a plan implements UI/app/CLI/business behavior but lacks actor/use-case/concept trace, STOP before editing code. Revise the plan or ask for clarification. Do not generate generic CRUD, generic screens, or broad role systems to fill the gap.

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
- For human-interaction tasks, read the task's `<domain_trace>` and the matching entries in DOMAIN.md, USE_CASES.md, and REQUIREMENTS.md
- Understand current state before making changes
- **MANDATORY gate:** If the task has a `<read_first>` field, you MUST read every listed file BEFORE making any edits. This is not optional. Do not skip files because you "already know" what's in them — read them. The read_first files establish ground truth for the task.

**Step 2: Implement**
- Follow the `<action>` instructions precisely
- Use concrete values specified in the action
- Write tests first if this is a TDD plan (type: tdd)
- For human-interaction/business work, translate the domain trace into real code:
  - Domain concepts become data models, types, schemas, services, commands, components, or state names that match existing project conventions.
  - Use cases become end-to-end behavior across UI/CLI/API/service/data as appropriate.
  - Actor names and outcomes guide screen states, API contracts, command behavior, validation, and copy where relevant.
  - Derived access rules become concrete checks or intentionally absent affordances. Allowed operations must work; denied operations must be blocked, hidden, or unavailable; unconfirmed operations must not be silently implemented.
  - Tests must prove at least the primary allowed path and any derived denied path that protects data or behavior.
- If implementing the action would require inventing a new role, concept, or access rule not present in DOMAIN.md/USE_CASES.md, STOP and update the planning artifacts before continuing.

**TDD commit format (for `type: tdd` plans — RED-GREEN-REFACTOR):**
- RED: Write failing test(s), run (MUST fail), commit: `test({phase}-{plan}): add failing test for [feature]`
- GREEN: Write minimal implementation, run (MUST pass), commit: `feat({phase}-{plan}): implement [feature]`
- REFACTOR: Clean up, tests MUST still pass, commit: `refactor({phase}-{plan}): clean up [feature]`

Errors: RED doesn't fail → investigate test/existing feature. GREEN doesn't pass → debug, iterate. REFACTOR breaks → undo.

**Step 3: Verify**
- Run the `<verify>` command or check
- **HARD GATE — acceptance_criteria verification:** After completing each task, if it has `<acceptance_criteria>`, you MUST run a verification loop before proceeding:
  1. For each criterion: execute the grep, file check, or CLI command that proves it passes
  2. Log each result as PASS or FAIL with the command output
  3. If ANY criterion fails: fix the implementation immediately, then re-run ALL criteria
  4. Repeat until all criteria pass — you are BLOCKED from starting the next task until this gate clears
  5. If a criterion cannot be satisfied after 2 fix attempts, log it as a deviation with reason — do NOT silently skip it
- This is not advisory. A task with failing acceptance criteria is an incomplete task.
- **HARD GATE — domain trace verification:** For each human-interaction task:
  1. Confirm every referenced actor/use case/concept appears in the modified code, tests, routes, commands, or UI flow as appropriate.
  2. Confirm allowed operations from derived access rules are implemented.
  3. Confirm denied operations are blocked, hidden, absent, or validated against.
  4. Confirm unconfirmed operations are not silently implemented or exposed.
  5. Confirm at least one automated or manual check proves the use-case outcome.
  6. If any item fails, fix before starting the next task.

**Step 4: Commit**
- Commit with message: `type({phase}-{plan}): {task description}`
- Use conventional commit types: feat, fix, refactor, test, docs
- Each task gets its own atomic commit
- Do NOT squash multiple tasks into one commit

**Pre-commit hook failure handling:** If a commit is BLOCKED by a hook:
1. The `git commit` command fails with hook error output
2. Read the error — it tells you exactly which hook and what failed
3. Fix the issue (type error, lint violation, secret leak, etc.)
4. `git add` the fixed files
5. Retry the commit
6. Budget 1-2 retry cycles per commit

Do NOT use `--no-verify` by default — let hooks run so issues surface at the introducing commit.

**Step 5: Handle Checkpoints**
- If task is type `checkpoint:*`:
  - Pause execution
  - Present checkpoint details to user
  - Wait for user response (explicit approval or decision)
  - Resume only after user responds

### Authentication Gates

Auth errors during execution are NOT failures — they're expected interaction points.

**Indicators:** "Not authenticated", "Unauthorized", 401/403, "Please run {tool} login", "Set {ENV_VAR}"

**Protocol:**
1. Recognize auth gate (not a bug)
2. STOP task execution
3. Create a `checkpoint:human-action` with exact auth steps
4. Wait for user to authenticate
5. Verify credentials work
6. Retry original task
7. Continue normally

Document auth gates in Summary under "Authentication Gates", not as deviations.

### Deviation Rules

Deviations from the plan are normal — handle via these rules:
- **Rules 1-3** (bugs, missing critical items, blockers): auto-fix, test, verify, track as deviations
- **Rule 4** (architectural changes): STOP, present decision to user, await approval
- **Scope boundary:** do not auto-fix pre-existing issues unrelated to current task
- **Fix attempt limit:** max 3 retries per deviation before escalating
- **Priority:** Rule 4 (STOP) > Rules 1-3 (auto) > unsure → Rule 4

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
  - Authentication gates (if any)
  - User setup status (if applicable)
  - Next phase readiness

**Critical ordering — write and commit SUMMARY.md as one atomic block.** Do NOT emit narrative output between the Write tool call and the commit tool call. Truncation at this boundary is a known failure mode.

**Self-Check mechanism:** After writing SUMMARY.md, verify before committing:
- Verify key-files.created exist on disk with `[ -f path ]`
- Check `git log --oneline --all --grep="{phase}-{plan}"` returns at least 1 commit
- Re-run ALL `<acceptance_criteria>` from every task — if any fail, fix before finalizing SUMMARY
- Re-run domain-trace checks for human-interaction plans — actor/use-case/concept/access behavior must still match the plan
- Re-run the plan-level `<verification>` commands — log results in SUMMARY
- Append `## Self-Check: PASSED` or `## Self-Check: FAILED` to SUMMARY

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
- For human-interaction plans, every truth must be checked against its actor, use case, domain concept, and outcome
- Verify `artifacts`: Files exist with real content (not placeholders)
  - Check `min_lines` if specified
  - Check `exports` if specified
  - Check `contains` if specified
- Verify `key_links`: Connections exist and match patterns
  - Grep for `pattern` in the source file
  - Verify the `via` mechanism is present

### Domain Trace Verification
For every plan with `domain_trace.interaction_gate: required`:
- Verify the code implements each referenced use case as behavior, not just files or labels
- Verify domain concepts are represented consistently in data shape, state, API/CLI contracts, UI components, and tests
- Verify derived access rules: allowed role-operation pairs succeed; denied role-operation pairs fail, are hidden, or are unavailable; unconfirmed role-operation pairs are not silently implemented
- Verify no broad, unrequested role/permission framework was introduced without a use-case source
- Record evidence in SUMMARY and VERIFICATION

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
