# State Template

Template for `.planning/STATE.md` - project memory and decisions.

---

## File Template

```markdown
# State: [Project Name]

## Project Status

**Current Phase**: [Phase number and name]
**Last Updated**: YYYY-MM-DD HH:MM
**Overall Progress**: [X]% complete

## Active Context

### Current Focus
[What we're working on right now]

### Recent Changes
- [Change 1 with timestamp]
- [Change 2 with timestamp]
- [Change 3 with timestamp]

### Next Steps
1. [Immediate next action]
2. [Follow-up action]
3. [Long-term consideration]

## Key Decisions

### Architecture Decisions
#### DEC-001: [Architecture choice]
**Date**: YYYY-MM-DD
**Decision**: [What was decided]
**Alternatives Considered**:
- [Alternative 1] - [Why rejected]
- [Alternative 2] - [Why rejected]
**Rationale**: [Why this decision was made]
**Implications**: [What this decision affects]

#### DEC-002: [Technology choice]
**Date**: YYYY-MM-DD
**Decision**: [What was decided]
**Alternatives Considered**:
- [Alternative 1] - [Why rejected]
- [Alternative 2] - [Why rejected]
**Rationale**: [Why this decision was made]
**Implications**: [What this decision affects]

### Implementation Decisions
#### DEC-003: [Implementation approach]
**Date**: YYYY-MM-DD
**Decision**: [What was decided]
**Context**: [What led to this decision]
**Rationale**: [Why this approach was chosen]

## Learning & Insights

### Technical Insights
- [Insight 1: What we learned about the technology]
- [Insight 2: Performance characteristics discovered]
- [Insight 3: Integration patterns that worked well]

### Process Insights
- [Insight 1: What worked well in our workflow]
- [Insight 2: What could be improved]
- [Insight 3: Team collaboration patterns]

### User Insights
- [Insight 1: User behavior observations]
- [Insight 2: Feature usage patterns]
- [Insight 3: Pain points discovered]

## Dependencies & Blockers

### Active Dependencies
- [Dependency 1]: [Status and owner]
- [Dependency 2]: [Status and owner]
- [Dependency 3]: [Status and owner]

### Current Blockers
- [Blocker 1]: [Description and impact]
- [Blocker 2]: [Description and impact]
- [Resolution plan for each blocker]

### Resolved Blockers
- [Blocker that was resolved]: [How it was resolved]
- [Blocker that was resolved]: [How it was resolved]

## Phase Completion Status

### Completed Phases
#### Phase 1: [Name]
- **Completion Date**: YYYY-MM-DD
- **Summary**: [Brief outcome]
- **Key Deliverables**: [What was delivered]
- **Lessons Learned**: [Key takeaways]

#### Phase 2: [Name]
- **Completion Date**: YYYY-MM-DD
- **Summary**: [Brief outcome]
- **Key Deliverables**: [What was delivered]
- **Lessons Learned**: [Key takeaways]

### In-Progress Phases
#### Phase 3: [Name]
- **Start Date**: YYYY-MM-DD
- **Current Plan**: [Plan number being worked on]
- **Progress**: [X]% of phase complete
- **Next Plan**: [Next plan to execute]
- **Blockers**: [Any current blockers]

### Upcoming Phases
#### Phase 4: [Name]
- **Planned Start**: YYYY-MM-DD
- **Dependencies**: [What this phase depends on]
- **Estimated Duration**: [Time estimate]

## Configuration & Settings

### Project Configuration
```json
{
  "project_name": "[Project Name]",
  "version": "1.0.0",
  "environment": "development",
  "tech_stack": ["technology1", "technology2"],
  "repository": "[Git repository URL]",
  "team": ["team member 1", "team member 2"]
}
```

### Workflow Settings
```json
{
  "auto_commit": true,
  "require_verification": true,
  "test_coverage_threshold": 80,
  "code_quality_checks": ["linting", "type_checking", "formatting"]
}
```

## Change History

### YYYY-MM-DD: Major Update
- [Change description]
- [Reason for change]
- [Impact assessment]

### YYYY-MM-DD: Phase Completion
- [Phase completed]
- [Key outcomes]
- [State updates]

### YYYY-MM-DD: Decision Recorded
- [Decision made]
- [Context and rationale]
- [Implementation status]
```