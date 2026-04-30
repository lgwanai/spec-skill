# Codebase Testing Template

Template for `.planning/codebase/testing.md` — testing approach and patterns.

---

## Template

```markdown
# Testing Approach

## Test Frameworks

| Type | Framework | Config File | Command |
|------|-----------|-------------|---------|
| Unit / Integration | Vitest / Jest | `vitest.config.ts` | `npm test` |
| E2E | Playwright / Cypress | `playwright.config.ts` | `npm run test:e2e` |
| Component | Testing Library | *(in vitest)* | `npm test` |

## Test Organization

```
src/
├── components/
│   ├── UserProfile/
│   │   ├── UserProfile.tsx
│   │   └── UserProfile.test.tsx    # Co-located
├── lib/
│   ├── auth.ts
│   └── auth.test.ts                # Co-located
tests/
├── integration/
│   └── api/
│       └── users.test.ts           # API integration tests
└── e2e/
    └── auth-flow.spec.ts           # E2E tests
```

## Test Patterns

### Unit Test Example
```typescript
import { describe, it, expect } from 'vitest';
import { formatUserName } from './user';

describe('formatUserName', () => {
  it('returns full name when both names provided', () => {
    expect(formatUserName({ first: 'John', last: 'Doe' })).toBe('John Doe');
  });

  it('returns first name only when last name missing', () => {
    expect(formatUserName({ first: 'John' })).toBe('John');
  });

  it('throws when no name provided', () => {
    expect(() => formatUserName({})).toThrow('Name required');
  });
});
```

### Integration Test Example
```typescript
import { describe, it, expect } from 'vitest';
import { createUser, getUser } from '@/lib/user';
import { db } from '@/lib/db';

describe('User API', () => {
  it('creates and retrieves a user', async () => {
    const user = await createUser({ email: 'test@example.com', name: 'Test' });
    expect(user.id).toBeDefined();

    const found = await getUser(user.id);
    expect(found.email).toBe('test@example.com');
  });
});
```

## Coverage Requirements

- **Unit tests:** [XX]% minimum
- **Integration tests:** Key API endpoints covered
- **E2E tests:** Critical user flows covered
- **Files excluded:** Generated code, configuration, type definitions

## CI/CD Integration

- Tests run on: [every push / PR to main / scheduled]
- Required checks: [Which tests must pass for merge]
- Test reports: [Where to find them]

## Test Data

- **Fixtures:** [Location and format]
- **Factories:** [Library or pattern used]
- **Database:** [In-memory / test database / Docker container]
- **Seeding:** [How test data is created]

## Notes

[Testing gaps, known flaky tests, areas needing better coverage.]
```

---

## Guidelines

**Purpose:** Document testing practices so new tests are consistent and valuable.

**What to capture:**
- Test frameworks and their configuration
- Test organization (co-located vs separate directory)
- Test patterns with examples
- Coverage requirements and CI integration
- Test data management

**Patterns to document:**
- How to write a good unit test
- How to mock external dependencies
- How to set up integration tests with database
- How to handle async operations in tests
- Table-driven / parameterized test patterns

**Coverage targets:**
- Core business logic: 80%+
- UI components: Focus on behavior, not implementation
- API routes: Cover success + error cases
- E2E: Cover primary user flows, not every edge case
