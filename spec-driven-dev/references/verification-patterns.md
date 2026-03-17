# Verification Patterns

Verification ensures that what was built matches what was intended. This document outlines patterns for effective verification in spec-driven development.

## Goal-Backward Verification

### Core Principle
Define success criteria BEFORE implementation, then verify against those criteria AFTER implementation.

### Process
1. **During planning**: Define "must-haves" - observable behaviors that must be true
2. **During execution**: Implement with verification in mind
3. **After completion**: Verify all must-haves are satisfied

### Example
**Plan requirement**: "User can create an account"
**Must-haves**:
- Truth: Registration form accepts valid email/password
- Artifact: `POST /api/register` endpoint exists
- Key link: Form submits to endpoint, endpoint creates user record
- Observable: User receives confirmation email

## Plan Verification (Pre-Implementation)

Before executing any phase, the plan itself must be verified.

### Checklist
- **Completeness**: Does it cover all requirements for this phase?
- **Feasibility**: Are the technical choices realistic?
- **Clarity**: Are the tasks actionable and unambiguous?
- **Verification**: Are the success criteria defined and testable?

### Process
1.  **Review**: Present the `PLAN.md` to the user.
2.  **Discuss**: Address any concerns or missing details.
3.  **Approve**: Get explicit confirmation before proceeding.

## Verification Types

### 1. Automated Verification
**When to use**: Repetitive checks, regression prevention, CI/CD pipelines

**Patterns**:
- **Unit tests**: Individual function/component testing
- **Integration tests**: Component interaction testing
- **End-to-end tests**: Full workflow testing
- **Static analysis**: Code quality, security, type checking

**Examples**:
```bash
# Run test suite
npm test

# Check type safety
npm run typecheck

# Lint code
npm run lint

# Security scan
npm audit
```

### 2. Manual Verification
**When to use**: UI/UX validation, subjective quality, exploratory testing

**Patterns**:
- **Visual inspection**: UI appearance and layout
- **User workflow**: Complete user journey testing
- **Accessibility**: Screen reader compatibility, keyboard navigation
- **Cross-browser**: Different browser testing

**Process**:
1. Create verification checklist
2. Execute each check manually
3. Document results and issues
4. Sign off when all checks pass

### 3. Integration Verification
**When to use**: System interaction, API contracts, data flow

**Patterns**:
- **API contract testing**: Verify request/response formats
- **Data flow testing**: End-to-end data validation
- **System integration**: Multi-service workflow testing

**Examples**:
```bash
# Test API endpoints
curl -X POST http://localhost:3000/api/register

# Verify database state
psql -c "SELECT COUNT(*) FROM users;"

# Check service health
curl http://localhost:3000/health
```

## Verification Workflow

### Pre-Implementation
1. **Define criteria**: What must be true when done
2. **Create tests**: Write test cases that verify criteria
3. **Plan verification**: Decide what to verify and how

### During Implementation
1. **Run tests frequently**: Catch issues early
2. **Verify incrementally**: Don't wait until the end
3. **Document issues**: Track what needs fixing

### Post-Implementation
1. **Run full test suite**: Ensure everything works
2. **Manual verification**: Subjective quality checks
3. **Integration testing**: System-wide validation
4. **Sign-off**: Document successful verification

## Verification Tools

### Testing Frameworks
- **Jest/React Testing Library**: React component testing
- **Pytest**: Python testing
- **JUnit**: Java testing
- **Cypress/Playwright**: End-to-end testing

### Code Quality
- **ESLint/Prettier**: JavaScript/TypeScript linting
- **Black/Flake8**: Python formatting and linting
- **SonarQube**: Code quality analysis

### Security
- **npm audit**: Node.js dependency security
- **Snyk**: Multi-language security scanning
- **OWASP ZAP**: Web application security testing

### Performance
- **Lighthouse**: Web performance testing
- **Apache Bench**: API load testing
- **JMeter**: Load and performance testing

## Best Practices

### 1. Start with Verification
Define how you'll verify success before writing any code.

### 2. Automate What You Can
Automated tests catch regressions and save time.

### 3. Keep Tests Fast
Slow tests discourage frequent running.

### 4. Test User Experience
Don't just test code - test what users actually experience.

### 5. Verify Edge Cases
Test boundary conditions and error scenarios.

### 6. Document Verification
Record what was verified, how, and by whom.

### 7. Continuous Verification
Integrate verification into your development workflow.

## Common Pitfalls

### 1. Incomplete Verification
**Problem**: Not verifying all success criteria
**Solution**: Use verification checklist for each requirement

### 2. Over-Reliance on Automation
**Problem**: Missing subjective quality issues
**Solution**: Include manual verification steps

### 3. Verification Drift
**Problem**: Verification doesn't match actual requirements
**Solution**: Regularly review and update verification criteria

### 4. False Positives
**Problem**: Tests pass but functionality is broken
**Solution**: Include integration and end-to-end testing

### 5. Verification Overhead
**Problem**: Too much time spent on verification
**Solution**: Prioritize critical paths and automate where possible

## Templates

### Verification Checklist Template
```markdown
# Verification Checklist: [Feature Name]

## Automated Tests
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] End-to-end tests pass
- [ ] Code quality checks pass

## Manual Verification
- [ ] UI appears correctly
- [ ] User workflow works end-to-end
- [ ] Error handling works as expected
- [ ] Performance is acceptable

## Integration Verification
- [ ] API contracts are satisfied
- [ ] Data flows correctly through system
- [ ] External dependencies work

## Sign-off
- **Verified by**: [Name]
- **Date**: YYYY-MM-DD
- **Notes**: [Any issues or observations]
```

### Test Case Template
```markdown
# Test Case: [Test Name]

**Requirement**: [Related requirement ID]
**Description**: [What this test verifies]

## Test Steps
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Expected Results
- [Expected outcome 1]
- [Expected outcome 2]

## Actual Results
- [ ] Pass
- [ ] Fail
- [ ] Skipped

**Notes**: [Any observations]
```

## Summary

Effective verification is critical for delivering quality software. By defining success criteria upfront, using appropriate verification methods, and integrating verification into your workflow, you ensure that what you build matches what was intended.

Remember: Verification isn't just about finding bugs - it's about confirming that you've successfully delivered value to users.