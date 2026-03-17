---
name: spec-skill
description: "Comprehensive specification-driven development system for structured project planning and execution. Use when starting new projects, managing complex tasks, or ensuring code quality. ENFORCES a strict 'Ask-Plan-Execute' workflow where user confirmation is REQUIRED before code generation."
---

# Specification Driven Development

## Overview

Spec-driven-dev is a structured development system that transforms vague ideas into executable plans through systematic questioning, research, planning, and verification. Inspired by get-shit-done, it provides templates and workflows for managing software projects from conception to completion.

**CRITICAL RULE**: You must **STOP and WAIT** for user confirmation at specific checkpoints. Do not rush from planning to execution in a single turn.

## Core Workflow

### 1. Project Initialization
Start by creating the foundational project context:

```bash
# Create project planning structure
mkdir -p .planning/phases
```

**Key documents created:**
- `.planning/PROJECT.md` - Project vision and context
- `.planning/REQUIREMENTS.md` - Scoped feature requirements
- `.planning/ROADMAP.md` - Phase decomposition
- `.planning/STATE.md` - Project memory and decisions
- `.planning/config.json` - Workflow preferences

### 2. Requirements Discussion (Interactive - BLOCKING)
**Goal**: Fully understand the user's intent before generating any files. **You MUST engage in a dialogue.**

**Resources**:
- Refer to `references/questioning.md` for questioning strategies and mental models.

**Actions**:
1. **Start Open**: Ask "Tell me about what you want to build."
2. **Loop (Ask -> Wait -> Ask)**:
   - Ask clarifying questions about features, constraints, and tech stack.
   - **WAIT** for the user's answer.
   - Challenge vagueness and clarify boundaries based on the answer.
   - **REPEAT** until you have a clear mental model.
3. **Summarize**: Present a summary of requirements and scope.
4. **STOP**: Ask "Do we have enough details to proceed to planning? Or should we discuss more?"
5. **WAIT**: Do not generate any Roadmap or Plan files until the user explicitly says "Proceed to Plan".

### 3. Roadmap Planning
**Only proceed here after user confirmation.**
Decompose the confirmed requirements into a phased roadmap:

**Phase structure:**
- **Integer phases** (1, 2, 3): Planned milestone work
- **Decimal phases** (2.1, 2.2): Urgent insertions
- **Dependency tracking**: Clear phase dependencies
- **Success criteria**: Observable behaviors for verification

### 4. Per-Phase Analysis & Discussion (BLOCKING)
Before planning **every phase**, re-analyze context and run a focused discussion loop.

**Resources**:
- Refer to `references/questioning.md` for phase-level clarification patterns.

**Actions**:
1. **Analyze Phase Context**: Review `.planning/PROJECT.md`, `.planning/ROADMAP.md`, `.planning/STATE.md`, and dependency phases.
2. **Loop (Ask -> Wait -> Ask)**:
   - Ask phase-specific clarifying questions about scope, constraints, interfaces, and acceptance criteria.
   - **WAIT** for the user's answer.
   - Refine unclear assumptions and identify missing decisions.
   - **REPEAT** until phase boundaries are unambiguous.
3. **Summarize**: Present phase scope, risks, decisions, and success criteria.
4. **STOP**: Ask "Do we have enough details for this phase plan?"
5. **WAIT**: Do not create/update this phase's `PLAN.md` until the user explicitly says "Proceed to Phase Plan".

### 5. Phase Planning & Review (BLOCKING)
Create the detailed execution plan for the current phase, but **do not execute yet**. This step repeats for each phase.

**Resources**:
- Refer to `references/verification-patterns.md` to define goal-backward verification criteria.

**Actions**:
1. Create/Update `.planning/phases/XX-phase/XX-PLAN.md`.
2. **Define Verification**: For each requirement, define "Must-haves" (Truth, Artifact, Key link, Observable).
3. **Plan Tasks**: Break down implementation steps to satisfy verification criteria.
4. **Review**: Check plan against the "Plan Verification Checklist".
5. **STOP**: Present the full plan content to the user.
6. **ASK**: "Here is the detailed plan. Does this look correct? Shall I proceed with execution?"
7. **WAIT**: Do not write any code until the user explicitly says "Yes" or "Proceed".

### 6. Phase Execution
**Only proceed here after user confirmation of the PLAN.**
Execute the **approved** plan step-by-step:

**Plan components:**
- **Tasks**: Specific, actionable implementation steps
- **Dependencies**: Plan-to-plan dependency graphs
- **Verification**: Executing the defined verification steps
- **Checkpoints**: User interaction points when needed

### 7. Verification & Summary
Ensure quality and document outcomes:

**Resources**:
- Refer to `references/verification-patterns.md` for verification types and workflows.

**Verification types:**
- **Automated**: Tests, linting, build checks
- **Manual**: User verification of UI/UX
- **Integration**: System integration testing
- **Documentation**: Update project context

## Templates & Patterns

### Project Template (PROJECT.md)
```markdown
# [Project Name]

## What This Is
[Current accurate description — 2-3 sentences. What does this product do and who is it for?]

## Core Value
[The ONE thing that matters most. If everything else fails, this must work.]

## Requirements
### Validated
(None yet — ship to validate)

### Active
- [ ] [Requirement 1]
- [ ] [Requirement 2]

### Out of Scope
- [Exclusion 1] — [why]
- [Exclusion 2] — [why]

## Context
[Background information that informs implementation]
```

### Phase Plan Template (PLAN.md)
```markdown
---
phase: XX-name
plan: NN
type: execute
wave: N
depends_on: []
files_modified: []
autonomous: true
requirements: []
---

<objective>
[What this plan accomplishes]
Purpose: [Why this matters]
Output: [What artifacts will be created]
</objective>

<tasks>
<task type="auto">
  <name>Task 1: [Action-oriented name]</name>
  <files>path/to/file.ext</files>
  <action>[Specific implementation]</action>
  <verify>[Command or check to prove it worked]</verify>
  <done>[Measurable acceptance criteria]</done>
</task>
</tasks>
```

### Roadmap Template (ROADMAP.md)
```markdown
# Roadmap: [Project Name]

## Phases
- [ ] **Phase 1: [Name]** - [One-line description]
- [ ] **Phase 2: [Name]** - [One-line description]

### Phase 1: [Name]
**Goal**: [What this phase delivers]
**Depends on**: Nothing (first phase)
**Requirements**: [REQ-01, REQ-02]
**Success Criteria**:
  1. [Observable behavior from user perspective]
  2. [Observable behavior from user perspective]
```

## Implementation Examples

### Example 1: New Web Application
```
User: "I want to build a todo app with user authentication"

Workflow:
1. Initialize project: Create PROJECT.md with core value "Simple, reliable todo management"
2. Requirements Discussion: Clarify "user authentication" (Email/Password? OAuth? JWT?)
3. Roadmap: Phase 1 (Auth), Phase 2 (Todo CRUD), Phase 3 (Advanced features)
4. Per-Phase Discussion (Phase 1): Reconfirm auth boundaries and constraints
5. Plan Review (Phase 1): Present Phase 1 plan for user approval
6. Execution (Phase 1): Implement auth with verification tests
7. Repeat steps 4-6 for each subsequent phase
```

### Example 2: API Service
```
User: "Build a REST API for inventory management"

Workflow:
1. Initialize: PROJECT.md with value "Reliable inventory tracking API"
2. Requirements Discussion: Define API surface, database choice, and auth strategy
3. Roadmap: Phase 1 (Basic CRUD), Phase 2 (Search), Phase 3 (Auth), Phase 4 (Reporting)
4. Per-Phase Discussion (Phase 1): Confirm endpoint scope and data model details
5. Plan Review (Phase 1): Confirm endpoints and data models
6. Execution (Phase 1): Implement endpoints with tests
7. Repeat steps 4-6 for each subsequent phase
```

## Best Practices

### 1. Context Management
- **Discuss before planning**: Ensure alignment on requirements
- **Confirm before executing**: User must approve the plan
- **Keep STATE.md updated** with all key decisions
- **Use SUMMARY.md** for each completed plan
- **Reference dependencies** explicitly in phase plans
- **Maintain clean separation** between planning and execution

### 2. Verification Strategy
- **Goal-backward verification**: Define success criteria before implementation
- **Automated checks**: Tests, linting, type checking
- **User verification**: Checkpoints for UI/UX validation
- **Integration testing**: End-to-end workflow validation

### 3. Phase Design
- **Small, focused phases**: 2-3 plans per phase
- **Clear dependencies**: Explicit phase-to-phase dependencies
- **Measurable outcomes**: Each phase delivers testable functionality
- **Progressive disclosure**: Build complexity gradually

## Resources

This skill includes resource directories for templates and references:

### scripts/
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

**Note:** Scripts may be executed without loading into context, but can still be read by Claude for patching or environment adjustments.

### references/
Documentation and reference material intended to be loaded into context to inform Claude's process and thinking.

**Examples from other skills:**
- Product management: `communication.md`, `context_building.md` - detailed workflow guides
- BigQuery: API reference documentation and query examples
- Finance: Schema documentation, company policies

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
