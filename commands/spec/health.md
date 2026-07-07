---
name: spec-health
description: "Validate .planning/ directory integrity. Check required files, config schema, phase directory structure, trace consistency, and artifact naming conventions. Auto-repair with --repair, context utilization diagnostic with --context."
argument-hint: "[--repair] [--context]"
---

# /spec-health — Health Check

Trigger the `spec-skill` skill and run the `.planning/` directory health check.

See `workflows/health.md` for the complete health check procedure.

## Workflow

1. **Directory Validation** — Check `.planning/`, `.planning/phases/` exist
2. **Required Files** — Verify PROJECT.md, ROADMAP.md, STATE.md, config.json present
3. **Config Schema** — Validate config.json structure and field types
4. **Phase Integrity** — Check naming conventions, cross-reference with ROADMAP
5. **Artifact Naming** — Verify PLAN.md, SUMMARY.md follow `NN-MM-NAME.md` convention
6. **Cross-Reference** — ROADMAP ↔ Phases, ROADMAP ↔ Requirements, Plans ↔ Requirements
7. **Trace Validation** — Run `scripts/validate_trace.py` when available to validate DOMAIN/USE_CASES/REQUIREMENTS → PLAN domain_trace consistency

## Auto-Repair (`--repair`)

- Missing required files → Create from `templates/` directory
- Invalid config values → Reset to template defaults
- Missing directories → Create
- Corrupted content → Report for manual fix

## Context Utilization (`--context`)

Orthogonal check independent of directory health. Diagnoses the running session's context utilization to catch reasoning-quality degradation before it happens.

**How to measure (self-contained — no SDK):** Ask the user to run Claude Code's built-in `/context` command (or read the context-window indicator shown in the UI) and report the utilization percentage. Then render one of three states:

| Utilization | State    | Action                                                                       |
|-------------|----------|------------------------------------------------------------------------------|
| < 60%       | healthy  | no action — context is comfortable                                           |
| 60% – 70%   | warning  | recommend starting a fresh thread for any remaining work                     |
| ≥ 70%       | critical | reasoning quality may degrade past the fracture point — open a new thread before continuing |

`--context` may be combined with `--repair` or run alone. When combined, run the context check as the final step and include its state in the output report. `--context` never mutates files — it is a read-only diagnostic.

## Output

Health report with:
- Summary (files present, phases found, warnings, errors)
- Errors requiring immediate fix
- Warnings to review
- Auto-repairs applied
- Context utilization state (when `--context` passed)
- Recommendations

## Key Rules

- Template-created files include `<!-- AUTO-GENERATED -->` header
- Phase directories with no plans or summaries → warning only
- config.json with invalid types → reset to defaults
- Trace validation errors block human-interaction plan execution
- `--context` is read-only; it never writes or repairs files
