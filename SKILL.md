---
name: spec-skill
description: "Comprehensive specification-driven development system for structured project planning and execution. Slash commands: /new-project, /plan, /execute, /verify, /health, /help, /next, /quick, /transition, /map-codebase. Use when starting new projects, managing complex tasks, or ensuring code quality. ENFORCES a strict 'Ask-Plan-Execute' workflow where user confirmation is REQUIRED before code generation."
---

# Specification Driven Development

TRIGGER when: starting a new project from scratch; managing complex multi-phase work that needs structured plan→execute→verify loops; ensuring a verification closure (must_haves + UAT) before marking work done; onboarding a brownfield codebase (`/spec-map-codebase`); running an ad-hoc task that still wants atomic commits and optional verification (`/spec-quick`).

## Overview

Spec-driven-dev is a structured development system that transforms vague ideas into executable plans through systematic questioning, domain/use-case discovery when humans interact with the system, research, planning, and verification. Inspired by get-shit-done (GSD), it provides templates and workflows for managing software projects from conception to completion.

**CRITICAL RULE**: You must **STOP and WAIT** for user confirmation at specific checkpoints. Do not rush from planning to execution in a single turn.

## Commands

All commands are invoked as `/spec-<name>` (e.g., `/spec-new`, `/spec-plan 1`). Commands automatically load the relevant workflow docs.

### Core Workflow Commands

| Command | Alias | What it does |
|---------|-------|--------------|
| `/spec-new` | `/new-project` | Full initialization: questions → domain/use cases when needed → requirements → roadmap. Creates `.planning/` structure |
| `/spec-plan <N>` | `/plan`, `/plan-phase` | Research + create executable PLAN.md for phase N. Flags: `--prd <file>` (PRD-driven, skip Discuss), `--mvp` (vertical slices + SKELETON.md), `--gaps` (close gaps from VERIFICATION.md) |
| `/spec-execute <N>` | `/execute`, `/execute-phase` | Execute all plans for phase N in parallel waves. Flags: `--wave N` (run only wave N), `--gaps-only` (only gap-closure plans), `--interactive` (checkpoint between every task) |
| `/spec-verify <N>` | `/verify`, `/verify-work` | Verify phase N completion: must_haves check, UAT, gap analysis |
| `/spec-transition` | `/transition` | Complete current phase, update context, prepare next phase |
| `/spec-next` | `/next` | Auto-detect current state and run the next logical step |

### Utility Commands

| Command | What it does |
|---------|--------------|
| `/spec-health [--repair] [--context]` | Validate `.planning/` directory integrity. `--repair` auto-fixes missing files; `--context` adds a read-only context-utilization diagnostic (healthy/warning/critical) |
| `/spec-help` | Show all commands and usage guide |
| `/spec-quick <task>` | Execute ad-hoc task with atomic commits, skip full planning. Flags: `--discuss`/`--full`/`--validate`/`--research` (composable quality gates). Subcommands: `list`, `status <slug>`, `resume <slug>` |
| `/spec-map-codebase [area]` | Analyze existing codebase for brownfield projects |
| `/spec-config` | Show or update `.planning/config.json` settings |

### Command Workflow Mapping

| Command | Loads Workflow | Produces |
|---------|---------------|----------|
| `/spec-new` | `workflows/health.md` (init check) | PROJECT.md, DOMAIN.md, USE_CASES.md, REQUIREMENTS.md, ROADMAP.md, STATE.md, config.json |
| `/spec-plan <N>` | `references/questioning.md` | `NN-CONTEXT.md`, `NN-RESEARCH.md`, `NN-MM-PLAN.md` |
| `/spec-execute <N>` | `workflows/execute-plan.md` | Code changes, atomic commits, `NN-MM-SUMMARY.md` |
| `/spec-verify <N>` | `workflows/verify-work.md` | `NN-VERIFICATION.md`, `NN-UAT.md`, fix plans if needed |
| `/spec-transition` | `workflows/transition.md` | Updated PROJECT.md, ROADMAP.md, STATE.md |
| `/spec-health` | `workflows/health.md` | Health report, auto-repairs if `--repair` |
| `/spec-quick` | *(inline lightweight)* | Quick plan + summary in `.planning/quick/` |
| `/spec-map-codebase` | `templates/codebase/*.md` | `.planning/codebase/*.md` analysis documents |

### Quick Usage Examples

```
/spec-new                          # Start fresh project
/spec-plan 1                       # Plan phase 1
/spec-execute 1                    # Execute phase 1
/spec-verify 1                     # Verify phase 1
/spec-transition                   # Move to phase 2
/spec-health --repair              # Fix missing planning files
/spec-quick "Add dark mode toggle" # Ad-hoc task
/spec-map-codebase api             # Analyze API layer
```

## Configuration

Project settings are stored in `.planning/config.json`. Key settings:

| Setting | Options | Default | Purpose |
|---------|---------|---------|---------|
| `mode` | `interactive`, `yolo` | `interactive` | Confirm vs auto-approve at each step |
| `granularity` | `coarse`, `standard`, `fine` | `standard` | Phase granularity (3-5 / 5-8 / 8-12 phases) |
| `workflow.discuss_mode` | `discuss`, `assumptions` | `discuss` | Interview vs codebase-first discovery |
| `workflow.research` | boolean | `true` | Research domain before planning |
| `parallelization.enabled` | boolean | `true` | Run independent plans simultaneously |

See `templates/config.json` for the full schema with all workflow toggles, gates, safety settings, and parallelization controls.

## Core Workflow

### 1. Project Initialization
Start by creating the foundational project context:

```bash
# Create project planning structure
mkdir -p .planning/phases
```

**Key documents created:**
- `.planning/PROJECT.md` - Project vision and context
- `.planning/DOMAIN.md` - Business vocabulary and domain concepts when people interact with the system
- `.planning/USE_CASES.md` - Actors, roles, and role-to-domain operations when people interact with the system
- `.planning/REQUIREMENTS.md` - Scoped feature requirements
- `.planning/ROADMAP.md` - Phase decomposition
- `.planning/STATE.md` - Project memory and decisions
- `.planning/config.json` - Workflow preferences

### 2. Discovery Discussion (Interactive - BLOCKING)
**Goal**: Fully understand the user's intent before generating any files. **You MUST engage in a dialogue.**

**Resources**:
- Refer to `references/questioning.md` for questioning strategies and mental models.

**Actions**:
1. **Start Open**: Ask "Tell me about what you want to build."
2. **Loop (Ask -> Wait -> Ask)**:
   - Ask clarifying questions about goals, constraints, domain boundaries, actors, and tech stack.
   - **WAIT** for the user's answer.
   - Challenge vagueness and clarify boundaries based on the answer.
   - **REPEAT** until you have a clear mental model.
3. **Summarize**: Present a summary of requirements and scope.
4. **STOP**: Ask "Do we have enough details to proceed to planning? Or should we discuss more?"
5. **WAIT**: Do not generate any Roadmap or Plan files until the user explicitly says "Proceed to Plan".

### 3. Domain & Use-Case Gate
**Only proceed here after user confirmation.**

Before writing REQUIREMENTS.md or ROADMAP.md, decide whether humans interact with the system.

**The gate is REQUIRED when:**
- The system has a UI, app, dashboard, form, human-facing CLI, chat flow, or workflow.
- The user asks to "build a system/app/tool/page/feature" where a person will create, view, edit, review, configure, approve, learn, buy, search, or operate something.
- Different people may use the product differently.
- There are roles, derived access differences, ownership, collaboration, review, approval, learning, commerce, or administration.
- The project has business objects whose meaning, state, ownership, or lifecycle affects behavior.

**The gate can be LIGHTWEIGHT/SKIPPED when:**
- The work is a pure library, internal refactor, infrastructure change, CI/build task, or machine-only integration.
- The phase changes implementation only and does not introduce or alter human-facing behavior.

**Actions when required:**
1. **Define top-level concepts first**: Create `.planning/DOMAIN.md` from `templates/DOMAIN.md`. Start with the largest meaningful modules/entities, then recursively decompose only as far as requirements, data, behavior, and verification need.
2. **Keep domain discovery continuous**: Do not treat DOMAIN.md/USE_CASES.md as a separate detour. Their concepts and use cases must flow directly into REQUIREMENTS.md, ROADMAP.md, phase CONTEXT.md, PLAN.md must_haves, and UAT.
3. **Define actors/roles**: Create `.planning/USE_CASES.md` from `templates/USE_CASES.md`. Identify roles and their goals.
4. **Map role operations**: For each role, map what they can do to domain concepts and what outcome results.
5. **Derive access rules from behavior**: Do not invent permissions as a separate design layer. If only Parent can set word-card scope and Student is not given that use case, then scope-setting is Parent-only until the user says otherwise.
6. **Resolve unstable terms**: If a term like "card", "project", "account", "record", or "workspace" is ambiguous, clarify it before requirements.
7. **STOP if unstable**: Do not decompose roadmap while core concepts, actors, or actor-to-concept operations remain ambiguous.

**Actions when not required:**
1. Record `Interaction Gate: Not required` and the reason in DOMAIN.md/USE_CASES.md if the files are being generated.
2. Proceed directly to requirements and roadmap.

### 4. Requirements Extraction
Convert confirmed discovery into scoped, traceable requirements.

**Rules:**
- For human-interaction systems, every v1 user-facing requirement must trace to at least one use case and at least one domain concept.
- Avoid generic "User can..." when roles differ. Prefer "[Role] can [operation] [domain concept] so that [outcome]."
- Access control is derived from the use-case matrix and explicit boundaries. Missing role-operation pairs are `unconfirmed`: do not implement or expose them silently, and ask or defer until the user expands the use case.
- Requirements are the continuation of the use-case model, not a new feature list. Preserve actor, operation, domain concept, and outcome through requirement IDs.
- Implementation-only work can still be tracked as technical requirements, but must not replace the role/use-case model for product behavior.

### 5. Roadmap Planning
**Only proceed here after user confirmation.**
Decompose the confirmed requirements into a phased roadmap:

**Phase structure:**
- **Integer phases** (1, 2, 3): Planned milestone work
- **Decimal phases** (2.1, 2.2): Urgent insertions
- **Dependency tracking**: Clear phase dependencies
- **Success criteria**: Observable behaviors for verification

### 6. Per-Phase Analysis & Discussion (BLOCKING)
Before planning **every phase**, re-analyze context and run a focused discussion loop.

**Resources**:
- Refer to `references/questioning.md` for phase-level clarification patterns.

**Actions**:
1. **Analyze Phase Context**: Review `.planning/PROJECT.md`, `.planning/DOMAIN.md`, `.planning/USE_CASES.md`, `.planning/ROADMAP.md`, `.planning/STATE.md`, and dependency phases.
2. **Loop (Ask -> Wait -> Ask)**:
   - Ask phase-specific clarifying questions about scope, constraints, interfaces, and acceptance criteria.
   - If the phase introduces or changes human interaction, roles, derived access rules, or domain operations, update DOMAIN.md/USE_CASES.md before PLAN.md.
   - If the phase only implements previously modeled behavior, keep the use-case trace and continue into implementation planning without redoing discovery.
   - **WAIT** for the user's answer.
   - Refine unclear assumptions and identify missing decisions.
   - **REPEAT** until phase boundaries are unambiguous.
3. **Summarize**: Present phase scope, risks, decisions, and success criteria.
4. **STOP**: Ask "Do we have enough details for this phase plan?"
5. **WAIT**: Do not create/update this phase's `PLAN.md` until the user explicitly says "Proceed to Phase Plan".

### 7. Phase Planning & Review (BLOCKING)
Create the detailed execution plan for the current phase, but **do not execute yet**. This step repeats for each phase.

**Resources**:
- Refer to `references/verification-patterns.md` to define goal-backward verification criteria.

**Actions**:
1. Create/Update `.planning/phases/XX-phase/XX-PLAN.md`.
2. **Define Verification (must_haves)**: In the YAML frontmatter, define `must_haves` (`truths`, `artifacts`, `key_links`) based on the phase goal.
3. **Carry Domain Trace Into Codegen**: For human-interaction/business plans, define `domain_trace` in frontmatter and task-level `<domain_trace>` blocks. Include use cases, actors, domain concepts/modules/entities, and derived access rules that implementation must satisfy.
4. **Plan Tasks**: Break down implementation steps to satisfy verification criteria. For business systems, each task must explain how the use case becomes concrete code: data/entity shape, UI/CLI/API/service behavior, derived access checks, tests, and UAT evidence. Use `<read_first>` tags in tasks to define files that must be read before execution, and `<acceptance_criteria>` for grep-verifiable conditions.
5. **Review**: Check plan against the "Plan Verification Checklist".
6. **STOP**: Present the full plan content to the user.
7. **ASK**: "Here is the detailed plan. Does this look correct? Shall I proceed with execution?"
8. **WAIT**: Do not write any code until the user explicitly says "Yes" or "Proceed".

### 8. Phase Execution
**Only proceed here after user confirmation of the PLAN.**
Execute the **approved** plan step-by-step.

**Resources**:
- Refer to `workflows/execute-plan.md` for the complete execution workflow including pre-execution checks, task execution order, verification rules, atomic commit strategy, and error recovery.
- Refer to `templates/continue-here.md` for session handoff when pausing mid-execution.

**Plan components:**
- **Tasks**: Specific, actionable implementation steps with concrete values
- **Dependencies**: Plan-to-plan dependency graphs managed via wave groups
- **Waves**: Parallel execution groups — independent plans run together
- **Verification**: Executing the defined verification and acceptance criteria
- **Checkpoints**: User interaction points (decisions, visual verification)
- **user_setup**: External service configuration the user must complete

### 9. Verification & Summary
Ensure quality and document outcomes:

**Resources**:
- Refer to `workflows/verify-work.md` for the complete verification workflow: automated checks, must-haves verification, UAT generation, and gap handling.
- Refer to `workflows/transition.md` for phase completion and transition to the next phase.
- Refer to `workflows/health.md` for planning directory integrity checks and auto-repair.
- Refer to `references/verification-patterns.md` for verification types and workflows.
- Refer to `templates/verification-report.md` for the verification report template.
- Refer to `templates/UAT.md` for user acceptance testing documentation.

**Verification types:**
- **Automated**: Tests, linting, build checks
- **Manual**: User verification of UI/UX via checkpoint tasks
- **Must-Haves**: Goal-backward verification (truths, artifacts, key_links)
- **Integration**: System integration testing
- **Documentation**: Update project context

After verification, refer to `workflows/transition.md` for the phase completion checklist and preparation for the next phase.

## Templates & Patterns

All templates are in the `templates/` directory. See `templates/README.md` for the canonical artifact registry — the authoritative index of all `.planning/` artifacts.

### Core Planning Templates
- `templates/PROJECT.md` — Project vision, requirements, constraints, key decisions
- `templates/DOMAIN.md` — Domain concepts, attributes, relationships, lifecycles, invariants; required when humans interact with the system
- `templates/USE_CASES.md` — Actors/roles, role relationships, use-case matrix, role-to-domain operations
- `templates/ROADMAP.md` — Phase decomposition with success criteria and progress tracking
- `templates/STATE.md` — Cross-session memory: position, decisions, blockers, performance, Deferred Items
- `templates/REQUIREMENTS.md` — Scoped functional requirements with traceability
- `templates/config.json` — Workflow configuration (gates, parallelization, quality, `ship.pr_body_sections`, `git.create_tag`)

### Phase Execution Templates
- `templates/PLAN.md` — Executable phase plan with XML task structure, must_haves, user_setup
- `templates/SUMMARY.md` — Post-execution summary with frontmatter for context assembly
- `templates/discovery.md` — Phase discussion decisions and context capture
- `templates/research.md` — Phase ecosystem research (NN-RESEARCH.md): libraries, patterns, expert approaches, locked constraints from discovery
- `templates/VALIDATION.md` — Validation architecture with Given/When/Then scenarios
- `templates/UAT.md` — User acceptance testing results with issue tracking (five-state model: pass/skipped/blocked + severity inference)
- `templates/verification-report.md` — Post-execution verification against must_haves (three-state: passed/gaps_found/human_needed + Anti-Patterns Found)
- `templates/user-setup.md` — USER-SETUP.md: human-required external config (API keys, dashboards) Claude cannot automate
- `templates/continue-here.md` — Session handoff for paused work

### Brownfield Analysis Templates
- `templates/codebase/structure.md` — Directory organization and key modules
- `templates/codebase/architecture.md` — Design patterns and component relationships
- `templates/codebase/stack.md` — Technology stack with versions
- `templates/codebase/conventions.md` — Coding conventions and patterns
- `templates/codebase/integrations.md` — External services and dependencies
- `templates/codebase/testing.md` — Testing approach and coverage
- `templates/codebase/concerns.md` — Known issues and technical debt

### Quality, Security & Operations Templates
- `templates/SECURITY.md` — Security contract: threat register, trust boundaries, accepted risks, audit trail (ASVS-leveled)
- `templates/DEBUG.md` — Active debug session tracker (`.planning/debug/[slug].md`): hypothesis/test/next-action loop with status state machine
- `templates/retrospective.md` — Living project retrospective: what was built, what worked, inefficiencies, patterns to persist
- `templates/user-profile.md` — Developer profile with behavioral directives and confidence ratings, generated from session analysis

### Workflow Documentation
- `workflows/execute-plan.md` — Step-by-step plan execution with verification and error recovery
- `workflows/verify-work.md` — Phase completion verification including must_haves checking
- `workflows/transition.md` — Phase completion, context updates, and next phase preparation
- `workflows/health.md` — Planning directory integrity validation and auto-repair

### Project Template (PROJECT.md)
See `templates/PROJECT.md` for the full template with guidelines, evolution rules, and brownfield support.

### Phase Plan Template (PLAN.md)
See `templates/PLAN.md` for the full template with frontmatter fields, XML task structure, must_haves verification, user_setup for external services, TDD plans, and parallel execution patterns.

### Roadmap Template (ROADMAP.md)
See `templates/ROADMAP.md` for the full template with phase numbering, decimal insertions, milestone grouping, and progress tracking.

## Implementation Examples

### Example 1: New Web Application
```
User: "I want to build a todo app with user authentication"

Workflow:
1. Initialize project: Create PROJECT.md with core value "Simple, reliable todo management"
2. Domain & Use-Case Gate: Required because people use the app. Define Todo, List, Account, Session; define roles such as Owner or Collaborator if collaboration exists
3. Requirements Discussion: Clarify "user authentication" (Email/Password? OAuth? JWT?) and trace requirements to use cases
4. Roadmap: Phase 1 (Auth), Phase 2 (Todo CRUD), Phase 3 (Advanced features)
5. Per-Phase Discussion (Phase 1): Reconfirm auth boundaries and constraints
6. Plan Review (Phase 1): Present Phase 1 plan for user approval
7. Execution (Phase 1): Implement auth with verification tests
8. Repeat steps 5-7 for each subsequent phase
```

### Example 2: API Service
```
User: "Build a REST API for inventory management"

Workflow:
1. Initialize: PROJECT.md with value "Reliable inventory tracking API"
2. Domain & Use-Case Gate: Required if humans/operators/admins use or govern inventory. Define Product, SKU, Stock Movement, Warehouse, Adjustment; define Clerk, Manager, Admin if roles differ
3. Requirements Discussion: Define API surface, database choice, auth strategy, and use-case traceability
4. Roadmap: Phase 1 (Basic CRUD), Phase 2 (Search), Phase 3 (Auth), Phase 4 (Reporting)
5. Per-Phase Discussion (Phase 1): Confirm endpoint scope and data model details
6. Plan Review (Phase 1): Confirm endpoints and data models
7. Execution (Phase 1): Implement endpoints with tests
8. Repeat steps 5-7 for each subsequent phase
```

## Best Practices

### 1. Context Management
- **Discuss before planning**: Ensure alignment on requirements via `workflows/transition.md` and `templates/discovery.md`
- **Model people before features when people interact**: For UI/app/CLI/business workflows, define DOMAIN.md and USE_CASES.md before REQUIREMENTS.md and ROADMAP.md
- **Confirm before executing**: User must approve the plan
- **Keep STATE.md updated** with all key decisions
- **Use SUMMARY.md** for each completed plan with full frontmatter for automatic context assembly
- **Reference dependencies** explicitly in phase plans via `depends_on` and `wave` fields
- **Maintain clean separation** between planning and execution
- **Session continuity**: Use `templates/continue-here.md` when pausing mid-work

### 2. Verification Strategy
- **Goal-backward verification**: Define `must_haves` (truths, artifacts, key_links) in the plan frontmatter before implementation. See `templates/PLAN.md` for the full structure.
- **Task-level verification**: Define grep-verifiable `acceptance_criteria` for each `<task>`
- **Automated checks**: Tests, linting, type checking — see `workflows/verify-work.md`
- **User verification**: Checkpoints for UI/UX validation via `checkpoint:human-verify` tasks
- **Integration testing**: End-to-end workflow validation
- **Verification reporting**: Use `templates/verification-report.md` to document results

### 3. Phase Design
- **Small, focused phases**: 2-3 plans per phase (~50% context max per plan)
- **Clear dependencies**: Explicit phase-to-phase and plan-to-plan dependencies via wave groups
- **Measurable outcomes**: Each phase delivers testable functionality with success criteria
- **Progressive disclosure**: Build complexity gradually
- **Parallel execution**: Independent plans run in same wave — see `templates/PLAN.md` for parallel patterns
- **External services**: Declare in `user_setup` frontmatter — AI can't create API keys or configure dashboards

## Resources

This skill includes resource directories for commands, templates, references, and scripts:

### commands/
Slash command definitions that trigger specific workflows. Each command file describes the workflow, inputs, outputs, and rules for that operation.

**Commands in this skill:**
- `commands/spec/new.md` — `/spec-new`: Initialize a new project
- `commands/spec/plan.md` — `/spec-plan <N>`: Plan a phase (flags: `--prd <file>`, `--mvp`, `--gaps`)
- `commands/spec/execute.md` — `/spec-execute <N>`: Execute a phase (flags: `--wave N`, `--gaps-only`, `--interactive`)
- `commands/spec/verify.md` — `/spec-verify <N>`: Verify phase completion
- `commands/spec/transition.md` — `/spec-transition`: Complete and prepare next phase
- `commands/spec/next.md` — `/spec-next`: Auto-detect next step
- `commands/spec/help.md` — `/spec-help`: Show command reference
- `commands/spec/quick.md` — `/spec-quick`: Ad-hoc task (flags: `--discuss`/`--full`/`--validate`/`--research`; subcmds: `list`/`status`/`resume`)
- `commands/spec/health.md` — `/spec-health [--repair] [--context]`: Check directory integrity
- `commands/spec/map-codebase.md` — `/spec-map-codebase`: Analyze existing codebase
- `commands/spec/config.md` — `/spec-config`: Manage configuration

### workflows/
Executable code (Python/Bash/etc.) that can be run directly to perform specific operations.

**Scripts in this skill:**
- `scripts/init_project.py` - Initialize a spec-driven project structure from templates.
  - Usage: `python scripts/init_project.py <project_name>`
  - Run when: Starting a new project or reinitializing missing planning scaffolding.
- `scripts/validate_project.py` - Validate required planning files, directory structure, and phase artifacts.
  - Usage: `python scripts/validate_project.py [project_path]`
  - Run when: Before phase execution, after major planning updates, and before handoff.
- `scripts/package_skill.py` - Package this skill into a distributable zip with manifest metadata.
  - Usage: `python scripts/package_skill.py [skill_path]`
  - Run when: Releasing or sharing the skill.

**Appropriate for:** Python scripts, shell scripts, or any executable code that performs automation, data processing, or specific operations.

**Note:** Scripts may be executed without loading into context, but can still be read for patching or environment adjustments.

### workflows/
Step-by-step workflow documentation for each phase of the spec-driven process. Load these into context when executing specific workflows.

**Workflows in this skill:**
- `workflows/execute-plan.md` — Task execution, atomic commits, verification, error recovery
- `workflows/verify-work.md` — Must-haves verification, UAT, gap handling
- `workflows/transition.md` — Phase completion, context updates, next phase preparation
- `workflows/health.md` — Directory integrity validation and auto-repair

### scripts/
Executable code (Python/Bash/etc.) that can be run directly to perform specific operations.

**Scripts in this skill:**
- `scripts/init_project.py` - Initialize a spec-driven project structure from templates
- `scripts/validate_project.py` - Validate required planning files, directory structure, and phase artifacts
- `scripts/package_skill.py` - Package this skill into a distributable zip with manifest metadata

**Appropriate for:** Python scripts, shell scripts, or any executable code that performs automation, data processing, or specific operations.

### references/
Documentation and reference material intended to be loaded into context to inform Claude's process and thinking.

**References in this skill:**
- `references/questioning.md` — Questioning strategies and mental models for requirements and phase-level discovery
- `references/verification-patterns.md` — Verification types, workflows, and goal-backward must_haves patterns
- `references/checkpoints.md` — Checkpoint types (human-verify/decision/action) and golden rules for interaction boundaries
- `references/domain-probes.md` — Domain-aware follow-up probes (auth, real-time, storage, etc.) for requirement gathering
- `references/user-story-template.md` — Canonical "As a / I want to / So that" user story format and structural rules
- `references/tdd.md` — TDD disciplines: red-green-refactor cycle, when TDD improves quality, cycle overhead
- `references/debugger-philosophy.md` — Evergreen debugging disciplines: user=reporter, Claude=investigator
- `references/common-bug-patterns.md` — Frequency-ordered bug checklist (~80% of bugs) to scan before hypothesizing
- `references/thinking-models-debug.md` — Structured reasoning models for debugging (fault tree, hypothesis-driven, Occam's razor)
- `references/ai-evals.md` — AI evaluation reference: model vs product evals, measurement approaches, rubric design

**Appropriate for:** In-depth documentation, API references, database schemas, comprehensive guides, or any detailed information that Claude should reference while working.

### assets/
Files not intended to be loaded into context, but rather used within the output Claude produces.

**Examples from other skills:**
- Brand styling: PowerPoint template files (.pptx), logo files
- Frontend builder: HTML/React boilerplate project directories
- Typography: Font files (.ttf, .woff2)

**Appropriate for:** Templates, boilerplate code, document templates, images, icons, fonts, or any files meant to be copied or used in the final output.

---

**Any unneeded directories can be deleted.** Not every skill requires all three types of resources.
