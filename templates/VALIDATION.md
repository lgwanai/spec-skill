# Validation Template

Template for `NN-VALIDATION.md` — validation architecture for a phase (Nyquist method).

---

## File Template

```markdown
# Phase [N]: [Name] — Validation Architecture

## Validation Strategy

**Automated verification:**
- [Test suite that covers this phase's requirements]
- [Build/lint checks that must pass]

**Manual verification:**
- [UI/UX checks user must perform]
- [Behavior checks that can't be automated]

**Integration verification:**
- [Cross-phase integration checks]
- [External service connectivity]

## Test Scenarios

### Scenario 1: [Name]

**Given** [precondition]
**When** [action]
**Then** [expected outcome]

### Scenario 2: [Name]

**Given** [precondition]
**When** [action]
**Then** [expected outcome]

### Scenario 3: [Name]

**Given** [precondition]
**When** [action]
**Then** [expected outcome]

## Coverage Targets

- Unit test coverage: [XX]%
- Integration test coverage: [XX]%
- Key paths covered: [list of critical user flows]

## Edge Cases

### Boundary Conditions
- [Edge case 1]: [Expected behavior]
- [Edge case 2]: [Expected behavior]

### Error States
- [Error scenario 1]: [Expected handling]
- [Error scenario 2]: [Expected handling]

### Concurrency
- [Concurrent scenario]: [Expected behavior]

## Validation Checklist

- [ ] All Given/When/Then scenarios pass
- [ ] Coverage targets met
- [ ] Edge cases handled correctly
- [ ] Error states produce appropriate responses
- [ ] No regressions in prior phase functionality

## Notes

[Additional validation context, known limitations, or environmental setup required.]
```

---

## Guidelines

**When to create:**
- During research phase for complex phases with many requirements
- When the phase involves security, payments, or data integrity
- Before execution to define what "done and correct" looks like

**Given/When/Then format:**
- **Given**: The initial context or precondition
- **When**: The action or event that occurs
- **Then**: The expected observable outcome

**Coverage targets:**
- Unit: 70-90% depending on phase criticality
- Integration: Cover all API endpoints and data flows
- Key paths: Every primary user flow must be tested

**Edge cases to consider:**
- Empty/null inputs
- Maximum/minimum values
- Network failures
- Concurrent operations
- Authentication/authorization edge cases
