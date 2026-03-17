# Requirements Template

Template for `.planning/REQUIREMENTS.md` - scoped project requirements.

---

## File Template

```markdown
# Requirements: [Project Name]

## Overview

[Brief summary of what requirements cover]

## Requirement Format

Each requirement follows this structure:
- **ID**: REQ-XXX (auto-incrementing)
- **Description**: What needs to be built
- **Acceptance Criteria**: How we know it's done
- **Priority**: P0 (must have), P1 (should have), P2 (nice to have)
- **Phase**: Which phase addresses this requirement

## Core Requirements (P0)

### REQ-001: [Core functionality name]
**Description**: [What this requirement entails]
**Acceptance Criteria**:
1. [Specific, testable condition]
2. [Specific, testable condition]
3. [Specific, testable condition]
**Priority**: P0
**Phase**: [Phase number]

### REQ-002: [Another core functionality]
**Description**: [What this requirement entails]
**Acceptance Criteria**:
1. [Specific, testable condition]
2. [Specific, testable condition]
**Priority**: P0
**Phase**: [Phase number]

## Important Requirements (P1)

### REQ-003: [Important functionality]
**Description**: [What this requirement entails]
**Acceptance Criteria**:
1. [Specific, testable condition]
2. [Specific, testable condition]
**Priority**: P1
**Phase**: [Phase number]

### REQ-004: [Another important functionality]
**Description**: [What this requirement entails]
**Acceptance Criteria**:
1. [Specific, testable condition]
**Priority**: P1
**Phase**: [Phase number]

## Enhancement Requirements (P2)

### REQ-005: [Enhancement functionality]
**Description**: [What this requirement entails]
**Acceptance Criteria**:
1. [Specific, testable condition]
**Priority**: P2
**Phase**: [Phase number]

## Non-Functional Requirements

### NFR-001: Performance
**Description**: System performance expectations
**Acceptance Criteria**:
- Page load time < 2 seconds
- API response time < 200ms for 95% of requests
- Support 100 concurrent users

### NFR-002: Security
**Description**: Security requirements
**Acceptance Criteria**:
- All user data encrypted at rest
- HTTPS enforced for all connections
- Authentication required for sensitive operations

### NFR-003: Reliability
**Description**: System reliability expectations
**Acceptance Criteria**:
- 99.9% uptime
- Automated backup system
- Graceful error handling

## Out of Scope

### Explicitly Excluded
- [Feature 1] - [Reason for exclusion]
- [Feature 2] - [Reason for exclusion]
- [Feature 3] - [Reason for exclusion]

### Future Considerations
- [Feature that may be added later]
- [Enhancement for future versions]
- [Integration with other systems]

## Requirement Dependencies

### Dependency Graph
```
REQ-001 → REQ-002 → REQ-003
    ↓
REQ-004 → REQ-005
```

### Implementation Order
1. REQ-001 (Foundation)
2. REQ-002 (Builds on foundation)
3. REQ-004 (Parallel work)
4. REQ-003 (Requires REQ-002)
5. REQ-005 (Requires REQ-004)

## Change Log

### YYYY-MM-DD: Initial Requirements
- Created initial requirement set
- Prioritized P0 requirements
- Defined acceptance criteria

### YYYY-MM-DD: Updated Requirements
- [Change description]
- [Reason for change]
```