# Verify Work Workflow

Workflow for verifying phase completion — checking that the codebase delivers what the phase goal promised.

---

## Verification Steps

### 1. Load Verification Context
- Read `.planning/STATE.md`
- Read `.planning/PROJECT.md` (for core value and requirements)
- Read all PLAN.md files for the current phase
- Collect all `must_haves` from all plan frontmatters
- Read all SUMMARY.md files for the current phase
- Read `.planning/phases/{phase}/{phase}-VALIDATION.md` if it exists

### 2. Run Automated Checks

**Build:**
```bash
npm run build  # or equivalent
```
- [ ] Build exits with code 0
- [ ] No build warnings that indicate issues

**Type Check:**
```bash
tsc --noEmit  # or equivalent
```
- [ ] No type errors

**Lint:**
```bash
npm run lint  # or equivalent
```
- [ ] No lint errors (warnings acceptable if pre-existing)

**Tests:**
```bash
npm test  # or equivalent
```
- [ ] All tests pass
- [ ] Coverage meets threshold (if configured)

### 3. Verify Must-Haves

**Truths (Observable Behaviors):**

For each truth in `must_haves.truths`:
1. Read the truth statement
2. Determine how to verify it (manual test, automated check, code inspection)
3. Perform the check
4. Record: Pass / Fail with evidence

Example:
- Truth: "User can see existing messages"
- Check: Navigate to messages page, verify messages render
- Evidence: Screenshot or "Messages component renders MessageList with 3 test messages"

**Artifacts (Required Files):**

For each artifact in `must_haves.artifacts`:
1. Check file exists at specified path
2. Check `min_lines` — is file substantive? (not a 3-line placeholder)
3. Check `exports` — do specified exports exist?
4. Check `contains` — does pattern exist in file?
5. Record: Pass / Fail with evidence

**Key Links (Artifact Connections):**

For each link in `must_haves.key_links`:
1. Run grep with the specified `pattern` in the source file
2. Verify the connection exists
3. Record: Pass / Fail with evidence

### 4. Manual Verification (if applicable)

For plans with `checkpoint:human-verify` tasks:
- Present each deliverable to the user
- User visits URL, tests functionality
- User reports: Pass / Fail with observations

### 5. Generate Verification Report

Create `.planning/phases/{phase}/{phase}-VERIFICATION.md`:
- Must-haves verification results table
- Automated test results
- Build/lint results
- Issues found (with severity)
- Gap analysis (gaps requiring fixes vs accepted gaps)
- Phase completion status

### 6. Handle Gaps

**If critical gaps found:**
1. Document each gap with severity
2. Create fix plans (add to current phase or create decimal phase)
3. Execute fix plans
4. Re-run verification from Step 2

**If non-critical gaps found:**
1. Document as accepted gaps with rationale
2. Add to STATE.md blockers/concerns for future phases
3. Proceed with transition

### 7. Generate UAT (if applicable)

If this phase has user-facing features:
- Create `.planning/phases/{phase}/{phase}-UAT.md`
- List each deliverable with verification instructions
- User tests each deliverable
- Record pass/fail with observations
- Issues → fix plans → re-execute → re-UAT

---

## Verification Checklist

Before declaring phase complete:
- [ ] All automated checks pass (build, type, lint, tests)
- [ ] All must_have truths verified
- [ ] All must_have artifacts exist and are substantive
- [ ] All must_have key_links confirmed present
- [ ] UAT completed (if applicable)
- [ ] No critical issues unresolved
- [ ] Verification report created
- [ ] STATE.md updated
