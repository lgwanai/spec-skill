# Continue-Here Template

Template for session handoff — enables seamless resumption of paused work.

---

## File Template

```markdown
# Continue Here

**Created:** [YYYY-MM-DD HH:MM]
**Session paused at:** [Phase, Plan, Task]

## Current Position

- **Phase:** [N] of [M] — [Phase name]
- **Plan:** [NN] — [Brief description]
- **Task:** [Task N] — [Task name]
- **Status:** [In progress / Completed / Blocked]

## What Was Just Completed

[Brief description of the last completed action or task. Include any relevant output or results.]

## What To Do Next

1. [Next step with specific action]
2. [Following step]
3. [Following step]

## Files Currently Being Worked On

- `path/to/file.ts` — [Status: modified / created / in progress]
- `path/to/another.ts` — [Status: modified / created / in progress]

## Decisions Pending

- [Decision 1]: [Context — what needs deciding and why]
- [Decision 2]: [Context — what needs deciding and why]

## Context Needed to Resume

**Key files to read:**
- `.planning/STATE.md` — Current project position
- `.planning/PROJECT.md` — Project vision and context
- `.planning/phases/XX-name/XX-YY-PLAN.md` — Current plan
- `[specific source files]` — Files being worked on

**Key context:**
- [Important context that isn't captured in files]
- [State of any running servers or processes]

## Blockers

- [Blocker 1]: [Description and what's needed to resolve]
- [Blocker 2]: [Description and what's needed to resolve]

## Notes

[Any additional notes that will help resume smoothly.]
```

---

## Guidelines

**When to create:**
- When pausing work mid-phase or mid-plan
- When handing off work to another developer or session
- When context window is filling up and you need a clean restart

**Location:**
- Write to project root as `.continue-here.md`
- STATE.md should reference it in the Session Continuity section

**What makes a good continue-here:**
- **Specific:** Not "work on phase 3" but "Task 2 of Plan 03-02: implement password reset endpoint"
- **Actionable:** The next person should know exactly what command to run or file to edit
- **Self-contained:** Include or reference all context needed to resume

**After resuming:**
- Read `.continue-here.md` first
- Read referenced files
- Delete or archive the file after successfully resuming
- Update STATE.md with new position

**Anti-patterns:**
- "Continue working on the project" — too vague
- Missing file references — resume will waste time re-discovering context
- Not updating STATE.md — next session won't know where to start
