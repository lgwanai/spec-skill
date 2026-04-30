# Codebase Conventions Template

Template for `.planning/codebase/conventions.md` — coding conventions and patterns.

---

## Template

```markdown
# Coding Conventions

## Naming

### Files
- **Components:** PascalCase (`UserProfile.tsx`)
- **Utilities:** camelCase (`formatDate.ts`)
- **Types:** PascalCase or camelCase with `.types.ts` suffix
- **Tests:** `*.test.ts` or `*.spec.ts` next to source
- **API routes:** Next.js route handlers in `route.ts`

### Variables & Functions
- **Variables:** camelCase (`userName`, `isLoading`)
- **Functions:** camelCase with verb prefix (`getUser`, `createSession`)
- **Constants:** UPPER_SNAKE_CASE for true constants (`MAX_RETRY_COUNT`)
- **Types/Interfaces:** PascalCase (`UserProfile`, `CreateUserInput`)
- **Enums:** PascalCase with singular name (`UserRole`)

### Database
- **Tables:** snake_case, plural (`user_profiles`)
- **Columns:** snake_case (`created_at`, `updated_at`)
- **Primary keys:** `id` (UUID or auto-increment)
- **Foreign keys:** `{table}_id` (`user_id`, `post_id`)
- **Timestamps:** `created_at`, `updated_at` (always include)

## File Organization

### Component Structure
```
components/
├── UserProfile/
│   ├── UserProfile.tsx       # Main component
│   ├── UserProfile.test.tsx  # Tests
│   ├── UserProfile.types.ts  # Types (if complex)
│   └── index.ts              # Barrel export
```

### Import Order
1. External packages (React, Next.js, libraries)
2. Internal modules (src/...)
3. Relative imports (./...)
4. Styles and assets

## Error Handling

### API Routes
```typescript
try {
  // Business logic
} catch (error) {
  if (error instanceof ValidationError) {
    return NextResponse.json({ error: error.message }, { status: 400 });
  }
  console.error('Unexpected error:', error);
  return NextResponse.json({ error: 'Internal server error' }, { status: 500 });
}
```

### Expected Patterns
- Never swallow errors silently
- Always log unexpected errors
- Use typed errors (custom Error classes)
- Return appropriate HTTP status codes

## TypeScript Conventions

- Prefer `interface` for object shapes, `type` for unions and utilities
- Use `strict: true` in tsconfig
- Avoid `any` — use `unknown` and type guards
- Use `readonly` for immutable properties
- Use `as const` for literal types
- Export types alongside their implementations

## Git Conventions

### Commit Messages
```
type(scope): description

feat(auth): add password reset flow
fix(api): handle empty response from external service
refactor(models): extract shared user types
test(auth): add password reset integration tests
docs(readme): update installation instructions
```

### Branch Naming
- `feature/description`
- `fix/description`
- `refactor/description`

## Notes

[Project-specific conventions not covered above.]
```

---

## Guidelines

**Purpose:** Document coding patterns so new code is consistent with existing code. 

**What to capture:**
- Naming conventions (files, variables, functions, database)
- File organization patterns
- Error handling patterns
- TypeScript conventions
- Git conventions
- Any project-specific rules

**How to discover conventions:**
- Sample 3-5 representative files in each category
- Look for consistent patterns (not one-off exceptions)
- Note both explicit rules (linter config) and implicit conventions (code patterns)
