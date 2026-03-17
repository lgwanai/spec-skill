# Summary Template

Template for `.planning/phases/XX-name/{phase}-{plan}-SUMMARY.md` - phase completion documentation.

---

## File Template

```markdown
---
phase: XX-name
plan: YY
subsystem: [primary category: auth, payments, ui, api, database, infra, testing, etc.]
tags: [searchable tech: jwt, stripe, react, postgres, prisma]

# Dependency graph
requires:
  - phase: [prior phase this depends on]
    provides: [what that phase built that this uses]
provides:
  - [bullet list of what this phase built/delivered]
affects: [list of phase names or keywords that will need this context]

# Tech tracking
tech-stack:
  added: [libraries/tools added in this phase]
  patterns: [architectural/code patterns established]

key-files:
  created: [important files created]
  modified: [important files modified]

key-decisions:
  - "Decision 1"
  - "Decision 2"

patterns-established:
  - "Pattern 1: description"
  - "Pattern 2: description"

requirements-completed: []  # REQUIRED — Copy ALL requirement IDs from this plan's `requirements` frontmatter.

# Metrics
duration: Xmin
completed: YYYY-MM-DD
---

# Phase [X]: [Name] Summary

**[Substantive one-liner describing outcome - NOT "phase complete" or "implementation finished"]**

## What Was Built

[Detailed description of implementation, 2-3 paragraphs]

## Key Implementation Details

### Technical Decisions
- [Decision 1 with rationale]
- [Decision 2 with rationale]

### Code Patterns Established
- [Pattern 1: description and example]
- [Pattern 2: description and example]

### Files Created/Modified
- `path/to/file1.ext`: [purpose and changes]
- `path/to/file2.ext`: [purpose and changes]

## Verification Results

### Automated Tests
- [Test suite results]
- [Coverage metrics if available]

### Manual Verification
- [User verification results]
- [UI/UX validation]

### Integration Testing
- [End-to-end workflow validation]
- [System integration results]

## Lessons Learned

### What Worked Well
- [Positive outcomes and effective patterns]

### Challenges & Solutions
- [Problems encountered and how they were resolved]

### Recommendations for Future Phases
- [Suggestions based on this implementation experience]

## Next Steps

### Immediate Follow-up
- [Tasks that should be done next]

### Future Considerations
- [Long-term implications or future work needed]
```