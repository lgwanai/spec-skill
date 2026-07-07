---
name: spec-help
description: "Show all spec-skill commands and usage guide. Lists available commands, their descriptions, and example usage."
---

# /spec-help — Command Reference

Trigger the `spec-skill` skill and display the full command reference.

## When Invoked

Display all available commands with descriptions and usage patterns. Do NOT start any workflow — this is informational only.

## Output Format

```
# spec-skill Commands

## Core Workflow
/spec-new           Initialize a new spec-driven project
/spec-plan <N>      Research and plan phase N
/spec-execute <N>   Execute all plans for phase N
/spec-verify <N>    Verify phase N completion
/spec-transition    Complete current phase, prepare next
/spec-next          Auto-detect and run next step

## Utilities  
/spec-health [--repair]  Check .planning/ integrity
/spec-quick <task>       Execute ad-hoc task
/spec-map-codebase       Analyze existing codebase
/spec-config             Show/update config.json

## Project Structure
.planning/                All planning documents
templates/                Document templates, including DOMAIN.md and USE_CASES.md for human-interaction systems
workflows/                Workflow step-by-step docs
references/               Questioning and verification guides

Quick start: /spec-new
```

## Key Rules

- Display this output directly — do NOT start any workflow
- If a user invokes a command you don't recognize, suggest `/spec-help`
- Mention `templates/README.md` for the full artifact reference
