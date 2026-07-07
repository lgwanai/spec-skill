---
name: spec-new
description: "Initialize a new spec-driven project. Full initialization flow: questions → domain/use cases when humans interact → requirements → roadmap. Creates .planning/ directory structure with PROJECT.md, DOMAIN.md, USE_CASES.md, REQUIREMENTS.md, ROADMAP.md, STATE.md, and config.json."
argument-hint: "[project-name]"
---

# /spec-new — New Project Initialization

Trigger the `spec-skill` skill and execute the project initialization workflow.

## Workflow

1. **Questions** — Ask until the user's idea is fully understood (goals, constraints, tech preferences, edge cases)
2. **Interaction Gate** — Decide whether humans interact with the system. Required for web/app/UI/dashboard/form/human-facing CLI/business workflows/roles/derived access/collaboration. Also required when the user says "add/build a feature" and that feature is operated by a person.
3. **Domain Model** — When the gate is required, define top-level concepts/modules first, then recursively decompose only the concepts needed for current system design in DOMAIN.md.
4. **Actors and Use Cases** — When the gate is required, define roles and role-to-domain operations in USE_CASES.md before roadmap planning.
5. **Derived Access Rules** — Derive role capabilities from the use-case matrix. Do not invent a separate permission model before behavior exists.
6. **Requirements** — Extract v1, v2, and out-of-scope items. User-facing v1 requirements must trace to use cases when the gate is required.
7. **Roadmap** — Create phases mapped to requirements and use cases.
8. **Initialize** — Create `.planning/` directory with PROJECT.md, DOMAIN.md, USE_CASES.md, REQUIREMENTS.md, ROADMAP.md, STATE.md, config.json

## What You Produce

- `.planning/PROJECT.md` — Project vision and context
- `.planning/DOMAIN.md` — Domain vocabulary and concept model when humans interact with the system
- `.planning/USE_CASES.md` — Actors, roles, role-to-domain operations, and derived access rules when humans interact with the system
- `.planning/REQUIREMENTS.md` — Scoped requirements with traceability
- `.planning/ROADMAP.md` — Phase decomposition with success criteria
- `.planning/STATE.md` — Project memory and session state
- `.planning/config.json` — Workflow configuration

## Key Rules

- **STOP and WAIT** for user confirmation before creating any files
- Use `references/questioning.md` for questioning strategies
- Follow `templates/PROJECT.md` template structure
- If people interact with the system, do not skip DOMAIN.md and USE_CASES.md
- DOMAIN.md and USE_CASES.md are upstream inputs to REQUIREMENTS.md and ROADMAP.md, not separate side documents
- If people do not interact with the system, record the interaction gate as not required and keep the domain/use-case artifacts lightweight
- Check for existing `.planning/` — if found, offer to reinitialize or merge
