# Questioning Guide

**Use during Step 2: Requirements Discussion.**

Project initialization is dream extraction, not requirements gathering. You're helping the user discover and articulate what they want to build.

## Philosophy

**You are a thinking partner, not an interviewer.**

The user often has a fuzzy idea. Your job is to help them sharpen it. Ask questions that make them think "oh, I hadn't considered that" or "yes, that's exactly what I mean."

Don't interrogate. Collaborate. Don't follow a script. Follow the thread.

## The Goal

By the end of questioning, you need enough clarity to write a PROJECT.md that downstream phases can act on:

- **Research needs**: what domain to research, what the user already knows, what unknowns exist
- **Requirements needs**: clear enough vision to scope v1 features
- **Roadmap needs**: clear enough vision to decompose into phases, what "done" looks like
- **plan-phase needs**: specific requirements to break into tasks, context for implementation choices
- **execute-phase needs**: success criteria to verify against, the "why" behind requirements

A vague PROJECT.md forces every downstream phase to guess. The cost compounds.

## How to Question

**Start open.** Let them dump their mental model. Don't interrupt with structure.

**Follow energy.** Whatever they emphasized, dig into that. What excited them? What problem sparked this?

**Challenge vagueness.** Never accept fuzzy answers. "Good" means what? "Users" means who? "Simple" means how?

**Make the abstract concrete.** "Walk me through using this." "What does that actually look like?"

**Clarify ambiguity.** "When you say Z, do you mean A or B?" "You mentioned X — tell me more."

**Know when to stop.** When you understand what they want, why they want it, who it's for, and what done looks like — offer to proceed.

## Question Types

Use these as inspiration, not a checklist. Pick what's relevant to the thread.

### Motivation — why this exists:
- "What prompted this?"
- "What problem are you solving?"
- "Why now?"
- "What happens if this doesn't exist?"

### Users — who it's for:
- "Who will use this?"
- "What do they currently do instead?"
- "What's frustrating about their current solution?"
- "How technically savvy are they?"

### Core value — the one thing that matters:
- "If everything else fails, what must work?"
- "What's the primary benefit users get?"
- "What would make them recommend this to others?"

### Scope — what's in and out:
- "What's absolutely necessary for v1?"
- "What can wait for later?"
- "What's explicitly out of scope and why?"
- "What similar things exist, and how is this different?"

### Success — how we know it's working:
- "How will users know it's working?"
- "What metrics would indicate success?"
- "What does 'done' look like?"
- "What would make you say 'this is exactly what I wanted'?"

### Technical context — implementation considerations:
- "Any technical constraints or preferences?"
- "Existing systems to integrate with?"
- "Performance or scale requirements?"
- "Security or compliance needs?"

## Common Patterns

### The Overly Ambitious User
**Symptoms**: Long feature lists, no prioritization, unrealistic timelines.
**Approach**: "Let's focus on what absolutely must work first. We can build the rest later."

### The Vague Visionary
**Symptoms**: Abstract descriptions, no concrete examples.
**Approach**: "Walk me through a specific user doing a specific thing."

### The Technical Perfectionist
**Symptoms**: Focus on implementation details before problem definition.
**Approach**: "Let's first agree on what we're building, then we can discuss how."

### The "Just Like X But Better"
**Symptoms**: References to existing products without clear differentiation.
**Approach**: "What specifically about X doesn't work for you? What would 'better' mean here?"

## Questioning Flow

### Phase 1: Exploration (5-10 minutes)
- Open-ended: "Tell me about what you want to build."
- Follow-up: "What excites you most about this?"
- Clarification: "When you say [vague term], what do you mean?"

### Phase 2: Definition (5-10 minutes)
- Concrete: "Walk me through a user's first experience."
- Boundaries: "What's absolutely necessary vs. nice to have?"
- Success: "How will we know it's working?"

### Phase 3: Validation (2-5 minutes)
- Summary: "So if I understand correctly, you want to build [summary]"
- Confirmation: "Is that right? What am I missing?"
- Next steps: "Ready to document this and start planning?"

## Red Flags

### Vague Answers
- "It should be good" → "What does 'good' mean specifically?"
- "Users will love it" → "Which users? What will they love about it?"
- "It needs to be fast" → "Fast compared to what? What's the target?"

### Contradictions
- "Simple but with all these features" → "Which features are truly essential?"
- "For everyone but also specialized" → "Who's the primary user?"

### Unrealistic Expectations
- "Build Facebook in a weekend" → "What's the minimal version that delivers value?"
- "No budget but enterprise scale" → "What constraints are we working with?"

## Success Indicators

You have enough clarity when:
1. You can write a clear PROJECT.md description
2. You can identify 3-5 core requirements
3. You understand the primary user and their needs
4. You know what "done" looks like for v1
5. You have clear boundaries (in scope/out of scope)

## Transition to Documentation

Once questioning is complete:
1. Summarize key points back to the user
2. Confirm understanding
3. Proceed to create PROJECT.md
4. Move to requirements gathering

Remember: Good questioning saves hours of rework later. Invest time upfront to get clarity.