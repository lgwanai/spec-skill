# Codebase Architecture Template

Template for `.planning/codebase/architecture.md` — design patterns and component relationships.

---

## Template

```markdown
# Architecture Analysis

## Architectural Style

[Overall architecture: monolith, microservices, serverless, layered, hexagonal, etc.]

## Design Patterns Used

| Pattern | Where Used | Purpose |
|---------|------------|---------|
| Repository | `src/lib/repositories/` | Data access abstraction |
| Factory | `src/lib/factories/` | Object creation |
| Observer | `src/lib/events/` | Event-driven communication |
| Middleware | `src/middleware/` | Request processing pipeline |

## Data Flow

```
[User] → [Browser] → [Next.js App Router] → [API Routes] → [Service Layer] → [Database]
                                                            → [External APIs]
```

## Component Relationships

### Frontend
```
Layout → Pages → Feature Components → Shared Components → UI Library
```

### Backend
```
Route Handler → Service → Repository → Prisma Client → PostgreSQL
             → Auth Middleware → Session Validation
```

## State Management

[How state is managed: React Context, Zustand, Redux, server state via React Query/SWR?]

## Key Architectural Decisions

1. **[Decision]:** [What was chosen and why]
2. **[Decision]:** [What was chosen and why]
3. **[Decision]:** [What was chosen and why]

## Notes

[Architectural observations: coupling, cohesion, separation of concerns, dependency direction.]
```

---

## Guidelines

**Purpose:** Document the "big picture" architecture so decisions about new features align with existing patterns.

**What to capture:**
- Architectural style and why
- Design patterns in use
- Data flow from user to database
- Component/service relationships
- State management approach

**What to infer (don't require confirmation):**
- Patterns visible in the code
- Obvious architectural choices (e.g., Next.js App Router implies server components)
- Consistency or inconsistency in patterns
