# UAT Template

Template for `NN-UAT.md` — User Acceptance Testing results for a phase.

---

## File Template

```markdown
---
status: [testing | partial | complete]
phase: [N]
source: [list of SUMMARY.md files tested]
started: [ISO timestamp]
updated: [ISO timestamp]
---

# Phase [N]: [Name] — User Acceptance Test Results

**Status:** [Passed / Failed / Partial]

## Current Test
<!-- OVERWRITE each test - shows where we are -->

number: [N]
name: [test name]
expected: |
  [what user should observe]
awaiting: user response

## Tests

### 1. [Test Name]
expected: [observable behavior - what user should see]
trace: [Actor] / [UC-___] / [Domain Concept] / [REQ-___]
result: [pending]

### 2. [Test Name]
expected: [observable behavior]
trace: [Actor] / [UC-___] / [Domain Concept] / [REQ-___]
result: pass

### 3. [Test Name]
expected: [observable behavior]
result: issue
reported: "[verbatim user response]"
severity: major

### 4. [Test Name]
expected: [observable behavior]
result: skipped
reason: [why skipped]

### 5. [Test Name]
expected: [observable behavior]
result: blocked
blocked_by: [server | physical-device | release-build | third-party | prior-phase]
reason: [why blocked]

## Summary

- **Total deliverables:** [N]
- **Passed:** [N]
- **Issues:** [N]
- **Pending:** [N]
- **Skipped:** [N]
- **Blocked:** [N]

## Issues Found

### Issue 1: [Title]
- **Severity:** [blocker | major | minor | cosmetic]
- **Test:** [Which test]
- **Description:** [What's wrong]
- **Expected:** [What should happen]
- **Actual:** [What happens — verbatim user response]
- **Fix plan:** [Reference to fix plan or "N/A — acceptable"]

## Gaps

<!-- YAML format for /spec-plan --gaps consumption -->
- truth: "[expected behavior from test]"
  status: failed
  reason: "User reported: [verbatim response]"
  severity: [blocker | major | minor | cosmetic]
  test: [N]
  root_cause: ""     # Filled by analysis
  artifacts: []      # Filled by analysis
  missing: []        # Filled by analysis

## Next Steps

- [ ] Fix critical issues (plan: [reference])
- [ ] Re-test failed deliverables
- [ ] Approve accepted issues
- [ ] Proceed to next phase after all criticals resolved

---
*UAT completed: [date]*
```

---

## Guidelines

**When to perform UAT:**
- After all phase plans have been executed
- After automated verification passes
- Before declaring the phase complete

**Human-interaction source of truth:**
- Build UAT tests from USE_CASES.md, REQUIREMENTS.md, and PLAN `domain_trace`, not only from SUMMARY.md prose.
- Each user-facing test should name the actor, use case, domain concept, and expected outcome.
- Include derived access checks when they affect user-visible behavior: allowed actor can complete the operation; denied actor is blocked; unconfirmed operation is not exposed or silently implemented.

**Test result values:**
- `pending` — Not yet tested
- `pass` — Works as expected
- `issue` — Problem found (add `reported` verbatim + `severity` inferred)
- `skipped` — Not applicable (add `reason`)
- `blocked` — Cannot test (add `blocked_by` tag + `reason`)

**Severity inference:**
Severity is INFERRED from user's natural language, never asked directly.

| User describes | Infer |
|----------------|-------|
| Crash, error, exception, fails completely, unusable | blocker |
| Doesn't work, nothing happens, wrong behavior, missing | major |
| Works but..., slow, weird, minor, small issue | minor |
| Color, font, spacing, alignment, visual, looks off | cosmetic |

Default: **major** (safe default, user can clarify if wrong)

**`blocked_by` tags:**
- `server` — Server/backend issue prevents testing
- `physical-device` — Needs hardware (camera, sensors)
- `release-build` — Only reproducible in production build
- `third-party` — External service dependency
- `prior-phase` — Depends on incomplete earlier phase

**UAT philosophy:**
Show expected behavior, ask if reality matches. "yes"/"y"/"next"/empty → pass; anything else → issue. Don't ask Pass/Fail buttons; don't ask severity — infer it from the user's words.

For business systems, show the expected behavior in role language: "Parent can set the selected word-card range; Student scope-setting is unconfirmed and is not exposed in v1." Avoid generic "feature works" tests.

**Fix plans:**
- Critical and High issues should generate new fix plans
- Add fix plans to the current phase or create a decimal phase (e.g., N.1)
- Re-execute and re-test after fixes
- Gaps section (YAML) feeds directly into `/spec-plan --gaps`

**Acceptable failures:**
- Known limitations documented in Requirements
- Issues deferred to future phases
- Edge cases that don't affect core functionality
