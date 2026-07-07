# Verification Report Template

Template for `NN-VERIFICATION.md` — post-execution verification report for a phase.

---

## File Template

```markdown
---
phase: [N]
verified: [YYYY-MM-DDTHH:MM:SSZ]
status: [passed | gaps_found | human_needed]
score: [N/M] must-haves verified
---

# Phase [N]: [Name] — Verification Report

**Phase Goal:** [goal from ROADMAP.md]
**Verified:** [timestamp]
**Status:** [passed | gaps_found | human_needed]

## Must-Haves Verification

### Truths (Observable Behaviors)

| # | Truth | Status | Evidence |
|---|-------|--------|----------|
| 1 | [Observable behavior] | ✓ VERIFIED | [what confirmed it] |
| 2 | [Observable behavior] | ✗ FAILED | [what's wrong] |
| 3 | [Observable behavior] | ? UNCERTAIN | [why can't verify] |

**Score:** [N/M] truths verified

### Artifacts (Required Files)

| # | Artifact | Expected | Status | Evidence |
|---|----------|----------|--------|----------|
| 1 | `path/to/file.ts` | [provides / contains / exports] | ✓ EXISTS + SUBSTANTIVE | [N lines, exports X] |
| 2 | `path/to/file.ts` | [provides / contains / exports] | ✗ STUB | [File exists but returns placeholder] |

**Artifacts:** [N/M] verified

### Key Links (Artifact Connections)

| # | From | To | Via | Status | Evidence |
|---|------|----|-----|--------|----------|
| 1 | `from/file.ts` | `to/endpoint` | [regex/handler] | ✓ WIRED | [Line N: `fetch('/api/...')`] |
| 2 | `from/file.ts` | `to/module` | [regex/handler] | ✗ NOT WIRED | [handler only logs, no fetch] |

**Wiring:** [N/M] connections verified

## Requirements Coverage

| Requirement | Status | Blocking Issue |
|-------------|--------|----------------|
| [REQ-01]: [description] | ✓ SATISFIED | - |
| [REQ-02]: [description] | ✗ BLOCKED | [issue] |
| [REQ-03]: [description] | ? NEEDS HUMAN | [why can't verify programmatically] |

**Coverage:** [N/M] requirements satisfied

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

## Anti-Patterns Found

| File | Line | Pattern | Severity | Impact |
|------|------|---------|----------|--------|
| `path/to/file.ts` | [N] | `// TODO: implement` | ⚠️ Warning | [Indicates incomplete] |
| `path/to/file.ts` | [N] | `return <div>Placeholder</div>` | 🛑 Blocker | [Renders no content] |
| `path/to/file.ts` | - | File missing | 🛑 Blocker | [Expected file doesn't exist] |

**Anti-patterns:** [N] found ([blockers] blockers, [warnings] warnings)

## Human Verification Required

[If no human verification needed:]
None — all verifiable items checked programmatically.

[If human verification needed:]

### 1. [Test Name]
**Test:** [What to do]
**Expected:** [What should happen]
**Why human:** [Why can't verify programmatically]

## Issues Found

### Issue 1: [Title]
- **Severity:** [🛑 Blocker / ⚠️ Warning / ℹ️ Info]
- **Found during:** [Which verification step]
- **Description:** [What failed]
- **Root cause:** [Why it failed]
- **Resolution:** [How fixed or "Deferred to fix plan [N]-[next]"]

## Gap Analysis

### Gaps Requiring Fix Plans
- [Gap 1]: [What's missing — reference the must_have it violates]
- [Gap 2]: [What's missing — reference the must_have it violates]

### Accepted Gaps
- [Gap 1]: [Why it's acceptable to defer]
- [Gap 2]: [Why it's acceptable to defer]

## Recommended Fix Plans

[If gaps found, generate fix plan recommendations:]

### [N]-[next]-PLAN.md: [Fix Name]
**Objective:** [What this fixes]
**Tasks:**
1. [Task to fix gap]
2. [Verification task]

**Estimated scope:** [Small / Medium]

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

## Verification Metadata

**Verification approach:** Goal-backward (derived from phase goal)
**Must-haves source:** [PLAN.md frontmatter | derived from ROADMAP.md goal]
**Automated checks:** [N] passed, [M] failed
**Human checks required:** [N]
**Total verification time:** [duration]

---
*Verified: [timestamp]*
*Verifier: Claude*
```

---

## Guidelines

**Status values:**
- `passed` — All must-haves verified, no blockers
- `gaps_found` — One or more critical gaps found
- `human_needed` — Automated checks pass but human verification required

**When to run verification:**
- After all phase plans execute
- Before transitioning to next phase
- After fix plans execute (re-verify)

**Must-haves verification:**
- Truths: Manually verify each observable behavior — ✓ VERIFIED / ✗ FAILED / ? UNCERTAIN
- Artifacts: Check files exist with real content (not placeholders) — ✓ EXISTS + SUBSTANTIVE / ✗ STUB
- Key links: Grep for the specified patterns — ✓ WIRED / ✗ NOT WIRED

**Evidence types:**
- For EXISTS: "File at path, exports X"
- For SUBSTANTIVE: "N lines, has patterns X, Y, Z"
- For WIRED: "Line N: code that connects A to B"
- For FAILED: "Missing because X" or "Stub because Y"

**Severity levels:**
- 🛑 Blocker: Prevents goal achievement, must fix
- ⚠️ Warning: Indicates incomplete but doesn't block
- ℹ️ Info: Notable but not problematic

**Gap handling:**
- Critical gaps: Create fix plans immediately
- Non-critical gaps: Document, create fix plans if time permits
- Accepted gaps: Document rationale, track for future phases

**Fix plan generation:**
- Only generate if gaps_found
- Group related fixes into single plans
- Keep to 2-3 tasks per plan
- Include verification task in each plan

**Verification is goal-backward:**
Don't just check "did tasks complete?" — check "does the system behave as the phase goal requires?" Task completion ≠ Goal achievement. This verification catches that gap.
