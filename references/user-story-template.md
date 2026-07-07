# User Story Template

Defines the canonical "As a / I want to / So that" format for capturing user needs.

## Canonical format

```
As a [user role], I want to [capability], so that [outcome].
```

Three required components:

| Slot | Question | Examples |
|---|---|---|
| `[user role]` | Who is the actor? | "new user", "admin", "signed-in customer", "API consumer" |
| `[capability]` | What can they do? | "register and log in", "upload a CSV", "see my dashboard" |
| `[outcome]` | Why does it matter? | "I can access my account", "I can bulk-import contacts", "I can see at a glance what needs attention" |

All three must be present. Refuse to assemble a partial story.

## Structural Rules

1. **Keep it on a single line** — the full user story should read as one continuous sentence (no line breaks inside the story). If it grows beyond ~120 chars, the scope is too large for one unit of work and should be split into multiple stories.
2. **Bold the keywords when emitting into a plan** — format as `**As a** ..., **I want to** ..., **so that** ...` so the three slots are visually scannable in plan documents. In prose contexts (e.g. a goal line), keep the keywords unbolded.

## Anti-Patterns

- **Missing outcome** — "As a user, I want to upload a CSV." The "so that" is missing; without it the value is unclear and the acceptance criteria become ambiguous.
- **Vague role** — "As a user..." is too generic. Name the actor ("new user", "admin", "API consumer") so the story targets a real need.
- **Solution disguised as capability** — "As a user, I want a dropdown..." describes implementation, not capability. Reframe as the capability the dropdown enables.
- **Multiple capabilities in one story** — "As a user, I want to register, log in, and reset my password..." bundles three units of work. Split into separate stories.
- **Outcome that restates the capability** — "As a user, I want to upload a CSV so that I can upload a CSV." The outcome must state the *value*, not echo the capability.
