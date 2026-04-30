# Codebase Technology Stack Template

Template for `.planning/codebase/stack.md` — technology stack with versions and rationale.

---

## Template

```markdown
# Technology Stack

## Languages

| Language | Version | Where Used | Notes |
|----------|---------|------------|-------|
| TypeScript | [version] | Frontend + Backend | Strict mode enabled |
| [Language] | [version] | [Where] | [Notes] |

## Frameworks

| Framework | Version | Purpose | Notes |
|-----------|---------|---------|-------|
| Next.js | [version] | Full-stack React framework | App Router |
| [Framework] | [version] | [Purpose] | [Notes] |

## Database

| Technology | Version | Purpose | Notes |
|------------|---------|---------|-------|
| PostgreSQL | [version] | Primary database | Via [ORM/Driver] |
| [Database] | [version] | [Purpose] | [Notes] |

## Key Libraries

| Library | Version | Purpose | Critical? |
|---------|---------|---------|-----------|
| Prisma | [version] | ORM and migrations | Yes |
| NextAuth.js | [version] | Authentication | Yes |
| Tailwind CSS | [version] | Styling | No |
| Zod | [version] | Schema validation | Yes |
| [Library] | [version] | [Purpose] | [Yes/No] |

## Development Tools

| Tool | Purpose |
|------|---------|
| TypeScript | Type checking |
| ESLint | Linting |
| Prettier | Formatting |
| Vitest / Jest | Testing |
| Playwright | E2E testing |

## Deployment

| Platform | Purpose | Notes |
|----------|---------|-------|
| Vercel / [Platform] | Hosting | [Notes] |
| GitHub Actions | CI/CD | [Notes] |

## Why This Stack

[Brief explanation of key technology choices — why these over alternatives.]

## Notes

[Version compatibility issues, upgrade plans, deprecated packages.]
```

---

## Guidelines

**Purpose:** Document the technology stack so new work uses compatible tools and libraries.

**What to capture:**
- All production dependencies with versions
- Development tools and their purpose
- Deployment platform and CI/CD pipeline
- Rationale for key choices

**Critical libraries:**
Mark as Critical if switching would require significant refactoring (ORM, auth, framework).
Mark as Not Critical if it's easily replaceable (styling, utility libraries).

**Version tracking:**
Always include versions. "Latest" is not a version. Check package.json for exact versions.
