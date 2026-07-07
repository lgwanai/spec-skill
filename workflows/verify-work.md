# Verify Work Workflow

Workflow for verifying phase completion — checking that the codebase delivers what the phase goal promised.

---

## Verification Steps

### 1. Load Verification Context
- Read `.planning/STATE.md`
- Read `.planning/PROJECT.md` (for core value and requirements)
- Read `.planning/DOMAIN.md` and `.planning/USE_CASES.md` when present
- Read `.planning/REQUIREMENTS.md` for actor/use-case/domain traceability
- Read all `PLAN.md` files for the current phase
- Collect all `must_haves` from all plan frontmatters
- Collect all `domain_trace` blocks from all plan frontmatters
- Read all `SUMMARY.md` files for the current phase
- Read `.planning/phases/{phase}/{phase}-VALIDATION.md` if it exists

### 2. Run Automated Checks

**Trace lint:**
```bash
python scripts/validate_trace.py .  # if available
```
- [ ] Trace references are consistent
- [ ] Human-interaction plans carry actor/use-case/domain trace
- [ ] Derived access rules use `allowed:`, `denied:`, or `unconfirmed:`

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
2. If the plan has `domain_trace.interaction_gate: required`, map the truth to actor, use case, domain concept, and outcome
3. Determine how to verify it (manual test, automated check, code inspection)
4. Perform the check
5. Record: Pass / Fail with evidence

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

### 4a. Verify Domain Trace (if applicable)

For every plan with `domain_trace.interaction_gate: required`:
- [ ] Each referenced use case is implemented as behavior, not just labels, placeholders, or unused types
- [ ] Each referenced domain concept is represented consistently in code artifacts (models/types/schema/state/API/CLI/UI/tests as appropriate)
- [ ] Each derived access rule is enforced:
  - allowed actor-operation pairs succeed
  - denied actor-operation pairs fail, are hidden, or are unavailable
  - unconfirmed actor-operation pairs are not silently implemented or exposed
- [ ] No broad role/permission system was introduced without a source use case
- [ ] Tests or UAT cover the primary actor outcome and any derived denied path that protects data or behavior

Record evidence in the verification report. A failed domain trace is a real gap even if build/tests pass.

### 5. Generate Verification Report

Create `.planning/phases/{phase}/{phase}-VERIFICATION.md` (see `templates/verification-report.md`):
- Must-haves verification results table
- Automated test results
- Build/lint results
- Issues found (with severity)
- Gap analysis (gaps requiring fixes vs accepted gaps)
- Phase completion status

### 6. Handle Gaps

**If critical gaps found:**
1. Document each gap with severity and root cause (analyze inline as the main agent — no sub-agent)
2. Prompt the user to run `/spec-plan` (with `--gaps` if supported) to create a fix plan for the diagnosed gaps
3. Execute the fix plan via `/spec-execute`
4. Re-run verification from Step 2

**If non-critical gaps found:**
1. Document as accepted gaps with rationale
2. Add to STATE.md blockers/concerns for future phases
3. Proceed with transition

### 7. Generate UAT (if applicable)

If this phase has user-facing features, run a conversational UAT session. Claude presents what SHOULD happen; the user confirms or describes what's different.

**UAT philosophy:** Show expected, ask if reality matches.
- "yes" / "y" / "next" / empty → pass
- Anything else → logged as issue, severity inferred
- No Pass/Fail buttons. No severity questions. Just: "Here's what should happen. Does it?"

**Optional Playwright-MCP automation:** When `mcp__playwright__*` (or `mcp__puppeteer__*`) tools are available in the session AND the phase has UI components (a `*-UI-SPEC.md` exists, or UI checkpoints are inferred from `SUMMARY.md`):

For each UI checkpoint:
1. Use `mcp__playwright__browser_navigate` to open the component's URL
2. Use `mcp__playwright__browser_take_screenshot` to capture a screenshot
3. Compare the screenshot visually against the spec's stated requirements (dimensions, color, layout, spacing)
4. Auto-mark checkpoints that clearly match as passed; flag items needing human judgment (subjective aesthetics, content accuracy) for manual UAT questions

If Playwright-MCP is not configured, fall back to the standard manual questions unchanged.

Display a summary line before proceeding:
```
UI checkpoints: {N} auto-verified, {M} queued for manual review
```

#### 7a. Check for active UAT sessions

```bash
find .planning/phases -name "*-UAT.md" -type f 2>/dev/null || true
```

**If active sessions exist AND no phase argument provided:**

Read each file's frontmatter (`status`, `phase`) and Current Test section. Display:

```
## Active UAT Sessions

| # | Phase | Status | Current Test | Progress |
|---|-------|--------|--------------|----------|
| 1 | 04-comments | testing | 3. Reply to Comment | 2/6 |
| 2 | 05-auth | testing | 1. Login Form | 0/4 |

Reply with a number to resume, or provide a phase number to start new.
```

- User replies with a number → load that file, go to 7f (resume)
- User replies with a phase number → new session, go to 7c

**If no active sessions AND no phase argument:**

```
No active UAT sessions.
Provide a phase number to start testing (e.g., /spec-verify 4)
```

#### 7b. Extract tests from SUMMARY.md

Read USE_CASES.md, REQUIREMENTS.md, PLAN `domain_trace`, and each `SUMMARY.md`. Parse for:
1. **Accomplishments** — features/functionality added
2. **User-facing changes** — UI, workflows, interactions
3. **Use-case trace** — actor, use case, domain concept, outcome
4. **Derived access rules** — allowed, denied, and unconfirmed operations visible to users

Focus on USER-OBSERVABLE outcomes, not implementation details. For each deliverable, create a test:
- `name`: Brief test name
- `expected`: What the user should see/experience (specific, observable)
- `trace`: Actor / UC ID / Domain Concept / Requirement ID when available

For each derived access rule that affects user-visible behavior, create UAT tests when feasible:
- allowed role can complete the operation
- denied role cannot complete the operation or does not see the affordance
- unconfirmed operation is not exposed or silently implemented

Skip internal/non-observable items (refactors, type changes, etc.).

**Cold-start smoke test injection:**

After extracting tests, scan the SUMMARY files for modified/created file paths. If ANY path matches these patterns:

`server.ts`, `server.js`, `app.ts`, `app.js`, `index.ts`, `index.js`, `main.ts`, `main.js`, `database/*`, `db/*`, `seed/*`, `seeds/*`, `migrations/*`, `startup*`, `docker-compose*`, `Dockerfile*`

Prepend this test to the list:
- `name`: "Cold Start Smoke Test"
- `expected`: "Kill any running server/service. Clear ephemeral state (temp DBs, caches, lock files). Start the application from scratch. Server boots without errors, any seed/migration completes, and a primary query (health check, homepage load, or basic API call) returns live data."

This catches bugs that only manifest on fresh start — race conditions in startup sequences, silent seed failures, missing environment setup — which pass against warm state but break in production.

#### 7c. Create the UAT file

```bash
mkdir -p "$PHASE_DIR"
```

Create `.planning/phases/{phase}/{phase_num}-UAT.md` (see `templates/UAT.md`):

```markdown
---
status: testing
phase: XX-name
source: [list of SUMMARY.md files]
started: [ISO timestamp]
updated: [ISO timestamp]
---

## Current Test
<!-- OVERWRITE each test - shows where we are -->

number: 1
name: [first test name]
expected: |
  [what user should observe]
awaiting: user response

## Tests

### 1. [Test Name]
expected: [observable behavior]
result: [pending]

### 2. [Test Name]
expected: [observable behavior]
result: [pending]

...

## Summary

total: [N]
passed: 0
issues: 0
pending: [N]
skipped: 0

## Gaps

[none yet]
```

#### 7d. Present each test

Render the current checkpoint from the structured UAT file and display it EXACTLY as-is — no commentary before or after. Wait for the user's plain-text response.

#### 7e. Process the response

**Pass** — empty response, "yes", "y", "ok", "pass", "next", "approved", "✓":
```
### {N}. {name}
expected: {expected}
result: pass
```

**Skip** — "skip", "can't test", "n/a":
```
### {N}. {name}
expected: {expected}
result: skipped
reason: [user's reason if provided]
```

**Blocked** — "blocked", "can't test - server not running", "need physical device", "need release build", or any response containing: server / blocked / not running / physical device / release build. Infer `blocked_by`:
- Contains: server, not running, gateway, API → `server`
- Contains: physical, device, hardware, real phone → `physical-device`
- Contains: release, preview, build, EAS → `release-build`
- Contains: stripe, twilio, third-party, configure → `third-party`
- Contains: depends on, prior phase, prerequisite → `prior-phase`
- Default: `other`

```
### {N}. {name}
expected: {expected}
result: blocked
blocked_by: {inferred tag}
reason: "{verbatim user response}"
```

Blocked tests do NOT go into the Gaps section (they're prerequisite gates, not code issues).

**Issue** — anything else. Infer severity from the description:

| User says | Infer |
|-----------|-------|
| crash, error, exception, fails, broken, unusable | blocker |
| doesn't work, wrong, missing, can't, nothing happens | major |
| slow, weird, off, minor, small | minor |
| color, font, spacing, alignment, visual, looks off | cosmetic |

Default to **major** if unclear. Never ask "how severe is this?" — just infer and move on; the user can correct.

```
### {N}. {name}
expected: {expected}
result: issue
reported: "{verbatim user response}"
severity: {inferred}
```

Append to the Gaps section (structured YAML for `/spec-plan --gaps`):
```yaml
- truth: "{expected behavior from test}"
  status: failed
  reason: "User reported: {verbatim user response}"
  severity: {inferred}
  test: {N}
  artifacts: []  # Filled by diagnosis
  missing: []    # Filled by diagnosis
```

**After any response:** update Summary counts and the frontmatter `updated` timestamp. If more tests remain → update Current Test and present the next one. If no more tests → go to 7g.

#### 7f. Resume from file

Read the full UAT file. Find the first test with `result: [pending]`. Announce:
```
Resuming: Phase {phase} UAT
Progress: {passed + issues + skipped}/{total}
Issues found so far: {issues count}

Continuing from Test {N}...
```
Update the Current Test section with the pending test, then present it.

#### 7g. Complete the session

**Determine final status:**
- `pending_count`: tests with `result: [pending]`
- `blocked_count`: tests with `result: blocked`
- `skipped_no_reason`: tests with `result: skipped` and no `reason` field

```
if pending_count > 0 OR blocked_count > 0 OR skipped_no_reason > 0:
  status: partial
else:
  status: complete
```

Update frontmatter (`status`, `updated`), clear Current Test (`[testing complete]`), commit the UAT file, and present a summary:

```
## UAT Complete: Phase {phase}

| Result | Count |
|--------|-------|
| Passed | {N}   |
| Issues | {N}   |
| Skipped| {N}   |

[If issues > 0:]
### Issues Found
[List from Gaps section]
```

**If issues > 0:** proceed to Step 6 (Handle Gaps) with the diagnosed gaps.

**If issues == 0:** the phase is verified. Run the transition workflow (`workflows/transition.md`) inline, then present next-step options (`/spec-plan {next}`, `/spec-execute {next}`).

#### Batched writes

Keep results in memory; write to the file only when:
1. **Issue found** — preserve the problem immediately
2. **Checkpoint** — every 5 passed tests (safety net)
3. **Session complete** — final write before commit

| Section | Rule | When written |
|---------|------|--------------|
| Frontmatter.status | OVERWRITE | Start, complete |
| Frontmatter.updated | OVERWRITE | On any file write |
| Current Test | OVERWRITE | On any file write |
| Tests.{N}.result | OVERWRITE | On any file write |
| Summary | OVERWRITE | On any file write |
| Gaps | APPEND | When issue found |

On context reset, the file shows the last checkpoint; resume from there.

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
