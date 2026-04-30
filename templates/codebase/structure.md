# Codebase Structure Template

Template for `.planning/codebase/structure.md` — directory organization and key modules.

---

## Template

```markdown
# Codebase Structure

## Directory Layout

```
project-root/
├── src/
│   ├── app/          # Application entry and routing
│   ├── components/   # Shared UI components
│   ├── lib/          # Utility functions and helpers
│   ├── models/       # Data models and types
│   ├── api/          # API route handlers
│   └── config/       # Configuration files
├── tests/            # Test suites
├── docs/             # Documentation
├── scripts/          # Build and utility scripts
├── prisma/           # Database schema (if applicable)
├── public/           # Static assets
├── package.json      # Dependencies and scripts
├── tsconfig.json     # TypeScript configuration
└── README.md         # Project overview
```

## Key Entry Points

| Path | Purpose |
|------|---------|
| `src/app/page.tsx` | Main application page |
| `src/app/layout.tsx` | Root layout with providers |
| `src/app/api/` | API route handlers |
| `package.json` `scripts` | Build, test, dev commands |

## Module Organization

### `src/components/`
[How components are organized: by feature, by type, atomic design?]

### `src/lib/`
[Utility organization: by domain, by function type?]

### `src/models/`
[Data modeling approach: TypeScript interfaces, Zod schemas, ORM models?]

## Key Dependencies Between Modules

```
src/app → src/components → src/lib
src/app/api → src/models → src/lib
src/lib → (external packages)
```

## Notes

[Any structural observations: monorepo patterns, shared packages, workspace configuration.]
```

---

## Guidelines

**Purpose:** Document the physical layout of the codebase so new contributors (including AI agents) can navigate quickly.

**What to capture:**
- Top-level directory purpose (not just listing)
- Entry points (where execution starts)
- Module organization (how code is grouped)
- Key dependencies between modules

**What to skip:**
- Individual file listings (too granular, gets stale)
- Generated directories (node_modules, dist, .next)
- Configuration that's self-documenting
