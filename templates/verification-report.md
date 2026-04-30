# Verification Report Template

Template for `NN-VERIFICATION.md` — post-execution verification report for a phase.

---

## File Template

```markdown
# Phase [N]: [Name] — Verification Report

**Date:** [YYYY-MM-DD]
**Verification type:** [Automated / Manual / Hybrid]
**Status:** [Passed / Failed / Partial]

## Must-Haves Verification

### Truths (Observable Behaviors)

| # | Truth | Status | Evidence |
|---|-------|--------|----------|
| 1 | [Observable behavior] | [Pass / Fail] | [How verified] |
| 2 | [Observable behavior] | [Pass / Fail] | [How verified] |
| 3 | [Observable behavior] | [Pass / Fail] | [How verified] |

### Artifacts (Required Files)

| # | Artifact | Expected | Status | Evidence |
|---|----------|----------|--------|----------|
| 1 | `path/to/file.ts` | [provides / contains / exports] | [Pass / Fail] | [How checked] |
| 2 | `path/to/file.ts` | [provides / contains / exports] | [Pass / Fail] | [How checked] |

### Key Links (Artifact Connections)

| # | From | To | Pattern | Status | Evidence |
|---|------|----|---------|--------|----------|
| 1 | `from/file.ts` | `to/endpoint` | [regex] | [Pass / Fail] | [How checked] |
| 2 | `from/file.ts` | `to/module` | [regex] | [Pass / Fail] | [How checked] |

## Automated Tests

| Test Suite | Tests Run | Passed | Failed | Coverage |
|------------|-----------|--------|--------|----------|
| Unit | [N] | [N] | [N] | [XX]% |
| Integration | [N] | [N] | [N] | [XX]% |
| E2E | [N] | [N] | [N] | [XX]% |

**Command:** `[test command that was run]`

## Build & Lint

- **Build:** [Pass / Fail] — `[build command]`
- **Type check:** [Pass / Fail] — `[type check command]`
- **Lint:** [Pass / Fail] — `[lint command]`
- **Format:** [Pass / Fail] — `[format check command]`

## Issues Found

### Issue 1: [Title]
- **Severity:** [Critical / High / Medium / Low]
- **Found during:** [Which verification step]
- **Description:** [What failed]
- **Root cause:** [Why it failed]
- **Resolution:** [How fixed or "Deferred to fix plan XX"]

### Issue 2: [Title]
- **Severity:** [Critical / High / Medium / Low]
- **Found during:** [Which verification step]
- **Description:** [What failed]
- **Root cause:** [Why it failed]
- **Resolution:** [How fixed or "Deferred to fix plan XX"]

## Gap Analysis

### Gaps Requiring Fix Plans
- [Gap 1]: [What's missing — reference the must_have it violates]
- [Gap 2]: [What's missing — reference the must_have it violates]

### Accepted Gaps
- [Gap 1]: [Why it's acceptable to defer]
- [Gap 2]: [Why it's acceptable to defer]

## Phase Completion Status

- [ ] All must_have truths verified
- [ ] All must_have artifacts exist and are substantive
- [ ] All key_links confirmed present
- [ ] Automated tests pass
- [ ] Build and lint pass
- [ ] No critical issues unresolved
- [ ] UAT completed (if applicable)

**Phase status:** [Ready for transition / Needs fixes / Blocked]

## Fix Plans Created

- [ ] [Fix plan 1 reference]: [What it fixes]
- [ ] [Fix plan 2 reference]: [What it fixes]

---

*Verification completed: [date]*
```

---

## Guidelines

**When to run verification:**
- After all phase plans execute
- Before transitioning to next phase
- After fix plans execute (re-verify)

**Must-haves verification:**
- Truths: Manually verify each observable behavior
- Artifacts: Check files exist with real content (not placeholders)
- Key links: Grep for the specified patterns

**Gap handling:**
- Critical gaps: Create fix plans immediately
- Non-critical gaps: Document, create fix plans if time permits
- Accepted gaps: Document rationale, track for future milestones

**Verification is goal-backward:**
Don't just check "did tasks complete?" — check "does the system behave as the phase goal requires?" Task completion ≠ Goal achievement. This verification catches that gap.
