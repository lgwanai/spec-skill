# Codebase Concerns Template

Template for `.planning/codebase/concerns.md` — known issues, technical debt, and areas needing attention.

---

## Template

```markdown
# Codebase Concerns & Technical Debt

## Critical Issues

### [Issue Title]
- **Location:** [File or module]
- **Severity:** [Critical / High]
- **Description:** [What's wrong]
- **Impact:** [What this affects]
- **Suggested fix:** [How to address]
- **Effort estimate:** [Small / Medium / Large]

## Technical Debt

### [Debt Item Title]
- **Location:** [File or module]
- **Type:** [Duplication / Outdated pattern / Missing tests / Poor abstraction]
- **Description:** [What's suboptimal]
- **Impact:** [How this slows development]
- **Suggested fix:** [How to address]
- **Effort estimate:** [Small / Medium / Large]

## Security Concerns

### [Security Concern Title]
- **Location:** [File or module]
- **Risk:** [High / Medium / Low]
- **Description:** [What's concerning]
- **Mitigation:** [What's currently protecting us]
- **Suggested improvement:** [How to harden]

## Performance Concerns

### [Performance Issue Title]
- **Location:** [File or module]
- **Impact:** [User-facing / Background]
- **Description:** [What's slow or resource-intensive]
- **Metrics:** [Current performance if known]
- **Suggested optimization:** [How to improve]

## Architecture Concerns

### [Architecture Concern Title]
- **Description:** [What architectural decision is problematic]
- **Why it's a concern:** [How it limits future work]
- **Migration path:** [How to move to better architecture]
- **Effort estimate:** [Small / Medium / Large / Epic]

## Dependency Concerns

| Package | Version | Concern | Action |
|---------|---------|---------|--------|
| [package] | [version] | [Deprecated / Vulnerable / Unmaintained] | [Upgrade to / Replace with] |

## Notes

[Any additional context about codebase health, areas to be careful with, or migration plans.]
```

---

## Guidelines

**Purpose:** Document everything that's wrong or could be better. This prevents re-discovering the same issues and helps prioritize improvement work.

**What to capture:**
- Known bugs (critical issues)
- Technical debt (suboptimal but working code)
- Security vulnerabilities or concerns
- Performance bottlenecks
- Architectural problems
- Dependency issues

**Severity levels:**
- **Critical:** Causes data loss, security breach, or complete feature failure
- **High:** Significant user impact, blocks important work
- **Medium:** Degraded experience, slows development
- **Low:** Cosmetic, nice-to-have improvement

**This is NOT a backlog:**
Don't list feature ideas here. This is about codebase health — things that need fixing or improving in the existing code.
