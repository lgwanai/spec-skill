# UAT Template

Template for `NN-UAT.md` — User Acceptance Testing results for a phase.

---

## File Template

```markdown
# Phase [N]: [Name] — User Acceptance Test Results

**Date:** [YYYY-MM-DD]
**Tester:** [Name or "User"]
**Status:** [Passed / Failed / Partial]

## Deliverables

### Deliverable 1: [Name]

**What to verify:** [Description of deliverable]
**How to verify:** [Steps to test]
**Expected result:** [What should happen]

**Result:** [Pass / Fail]
**Notes:** [Observations, issues, screenshots]

---

### Deliverable 2: [Name]

**What to verify:** [Description of deliverable]
**How to verify:** [Steps to test]
**Expected result:** [What should happen]

**Result:** [Pass / Fail]
**Notes:** [Observations, issues, screenshots]

---

### Deliverable 3: [Name]

**What to verify:** [Description of deliverable]
**How to verify:** [Steps to test]
**Expected result:** [What should happen]

**Result:** [Pass / Fail]
**Notes:** [Observations, issues, screenshots]

---

## Issues Found

### Issue 1: [Title]
- **Severity:** [Critical / High / Medium / Low]
- **Deliverable:** [Which deliverable]
- **Description:** [What's wrong]
- **Expected:** [What should happen]
- **Actual:** [What happens]
- **Fix plan:** [Reference to fix plan or "N/A — acceptable"]

### Issue 2: [Title]
- **Severity:** [Critical / High / Medium / Low]
- **Deliverable:** [Which deliverable]
- **Description:** [What's wrong]
- **Expected:** [What should happen]
- **Actual:** [What happens]
- **Fix plan:** [Reference to fix plan or "N/A — acceptable"]

---

## Summary

- **Total deliverables:** [N]
- **Passed:** [N]
- **Failed:** [N]
- **Issues requiring fixes:** [N]
- **Issues accepted as-is:** [N]

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

**Severity levels:**
- **Critical**: Blocks phase completion, must fix before proceeding
- **High**: Significant issue, should fix before proceeding
- **Medium**: Noticeable issue, can fix in next phase
- **Low**: Minor issue, track but don't block

**Fix plans:**
- Critical and High issues should generate new fix plans
- Add fix plans to the current phase or create a decimal phase (e.g., N.1)
- Re-execute and re-test after fixes

**Acceptable failures:**
- Known limitations documented in Requirements
- Issues deferred to future milestones
- Edge cases that don't affect core functionality
