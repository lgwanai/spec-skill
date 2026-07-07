# Requirements Template

Template for `.planning/REQUIREMENTS.md` — checkable requirements that define "done."

<template>

```markdown
# Requirements: [Project Name]

**Defined:** [date]
**Core Value:** [from PROJECT.md]
**Interaction Gate:** [Required / Not required]
**Domain Model:** `.planning/DOMAIN.md`
**Use Cases:** `.planning/USE_CASES.md`

## v1 Requirements

Requirements for initial release. Each maps to roadmap phases.
For human-interaction systems, each user-facing requirement continues a use case. Preserve Actor / Operation / Domain Concept / Outcome instead of rewriting it as an unrelated feature.

### Authentication

- [ ] **AUTH-01**: [Actor] can sign up with email and password so that [outcome]. (Use case: UC-___; Concepts: [Account, Session])
- [ ] **AUTH-02**: [Actor] receives email verification after signup so that [outcome]. (Use case: UC-___; Concepts: [Account])
- [ ] **AUTH-03**: [Actor] can reset password via email link so that [outcome]. (Use case: UC-___; Concepts: [Account])
- [ ] **AUTH-04**: [Actor] session persists across browser refresh so that [outcome]. (Use case: UC-___; Concepts: [Session])

### [Category 2]

- [ ] **[CAT]-01**: [Requirement description]
- [ ] **[CAT]-02**: [Requirement description]
- [ ] **[CAT]-03**: [Requirement description]

### [Category 3]

- [ ] **[CAT]-01**: [Requirement description]
- [ ] **[CAT]-02**: [Requirement description]

## v2 Requirements

Deferred to future release. Tracked but not in current roadmap.

### [Category]

- **[CAT]-01**: [Requirement description]
- **[CAT]-02**: [Requirement description]

## Out of Scope

Explicitly excluded. Documented to prevent scope creep.

| Feature | Reason |
|---------|--------|
| [Feature] | [Why excluded] |
| [Feature] | [Why excluded] |

## Traceability

Which phases cover which requirements. Updated during roadmap creation.

| Requirement | Actor / Role | Use Case | Domain Concept(s) | Phase | Status |
|-------------|--------------|----------|-------------------|-------|--------|
| AUTH-01 | [Role] | UC-___ | [Concepts] | Phase 1 | Pending |
| AUTH-02 | [Role] | UC-___ | [Concepts] | Phase 1 | Pending |
| AUTH-03 | [Role] | UC-___ | [Concepts] | Phase 1 | Pending |
| AUTH-04 | [Role] | UC-___ | [Concepts] | Phase 1 | Pending |
| [REQ-ID] | [Role / N/A] | [UC-___ / N/A] | [Concepts / N/A] | Phase [N] | Pending |

## Derived Access Notes

Access is inferred from use cases and explicit boundaries. Use three statuses: `allowed`, `denied`, and `unconfirmed`. Unconfirmed operations must not be silently implemented.

| Status | Operation | Role(s) | Source Use Case(s) / Reason | Requirement(s) |
|--------|-----------|---------|-----------------------------|----------------|
| allowed | [Operation] | [Role(s)] | [UC-___] | [REQ-___] |
| denied | [Operation] | [Role(s)] | [Explicit boundary] | [REQ-___] |
| unconfirmed | [Operation] | [Role(s)] | [Open question / future scope] | [REQ-___ / N/A] |

**Coverage:**
- v1 requirements: [X] total
- Mapped to phases: [Y]
- Unmapped: [Z] ⚠️

---
*Requirements defined: [date]*
*Last updated: [date] after [trigger]*
```

</template>

<guidelines>

**Requirement Format:**
- ID: `[CATEGORY]-[NUMBER]` (AUTH-01, CONTENT-02, SOCIAL-03)
- Description: User-centric, testable, atomic
- Checkbox: Only for v1 requirements (v2 are not yet actionable)
- For human-interaction systems: `[Actor/Role] can [operation] [domain concept] so that [outcome]. (Use case: UC-___; Concepts: [...])`
- For implementation-only requirements: mark Actor/Use Case as `N/A` in Traceability and explain why in the category notes

**Categories:**
- Derive from research FEATURES.md categories
- Keep consistent with domain conventions
- Typical: Authentication, Content, Social, Notifications, Moderation, Payments, Admin

**v1 vs v2:**
- v1: Committed scope, will be in roadmap phases
- v2: Acknowledged but deferred, not in current roadmap
- Moving v2 → v1 requires roadmap update

**Out of Scope:**
- Explicit exclusions with reasoning
- Prevents "why didn't you include X?" later
- Anti-features from research belong here with warnings

**Traceability:**
- Empty initially, populated during roadmap creation
- Each requirement maps to exactly one phase
- Unmapped requirements = roadmap gap
- If the interaction gate is required, every user-facing v1 requirement maps to at least one actor/role, use case, and domain concept
- Avoid generic "User" when roles differ; use the role name from USE_CASES.md
- Derived access notes should be copied from USE_CASES.md and refined only when requirements add detail. Do not add permissions that have no source use case or explicit boundary; leave them `unconfirmed`.

**Status Values:**
- Pending: Not started
- In Progress: Phase is active
- Complete: Requirement verified
- Blocked: Waiting on external factor

</guidelines>

<evolution>

**After each phase completes:**
1. Mark covered requirements as Complete
2. Update traceability status
3. Note any requirements that changed scope

**After roadmap updates:**
1. Verify all v1 requirements still mapped
2. Add new requirements if scope expanded
3. Move requirements to v2/out of scope if descoped

**Requirement completion criteria:**
- Requirement is "Complete" when:
  - Feature is implemented
  - Feature is verified (tests pass, manual check done)
  - Feature is committed

</evolution>

<example>

```markdown
# Requirements: CommunityApp

**Defined:** 2025-01-14
**Core Value:** Users can share and discuss content with people who share their interests

## v1 Requirements

### Authentication

- [ ] **AUTH-01**: User can sign up with email and password
- [ ] **AUTH-02**: User receives email verification after signup
- [ ] **AUTH-03**: User can reset password via email link
- [ ] **AUTH-04**: User session persists across browser refresh

### Profiles

- [ ] **PROF-01**: Member can create a profile with display name so that other members can identify them. (Use case: UC-005; Concepts: Profile, Account)
- [ ] **PROF-02**: Member can upload avatar image so that their profile is recognizable. (Use case: UC-005; Concepts: Profile)
- [ ] **PROF-03**: Member can write bio (max 500 chars) so that they can describe themselves. (Use case: UC-005; Concepts: Profile)
- [ ] **PROF-04**: Member can view other members' profiles so that they can understand who posted content. (Use case: UC-006; Concepts: Profile)

### Content

- [ ] **CONT-01**: User can create text post
- [ ] **CONT-02**: User can upload image with post
- [ ] **CONT-03**: User can edit own posts
- [ ] **CONT-04**: User can delete own posts
- [ ] **CONT-05**: User can view feed of posts

### Social

- [ ] **SOCL-01**: User can follow other users
- [ ] **SOCL-02**: User can unfollow users
- [ ] **SOCL-03**: User can like posts
- [ ] **SOCL-04**: User can comment on posts
- [ ] **SOCL-05**: User can view activity feed (followed users' posts)

## v2 Requirements

### Notifications

- **NOTF-01**: User receives in-app notifications
- **NOTF-02**: User receives email for new followers
- **NOTF-03**: User receives email for comments on own posts
- **NOTF-04**: User can configure notification preferences

### Moderation

- **MODR-01**: User can report content
- **MODR-02**: User can block other users
- **MODR-03**: Admin can view reported content
- **MODR-04**: Admin can remove content
- **MODR-05**: Admin can ban users

## Out of Scope

| Feature | Reason |
|---------|--------|
| Real-time chat | High complexity, not core to community value |
| Video posts | Storage/bandwidth costs, defer to v2+ |
| OAuth login | Email/password sufficient for v1 |
| Mobile app | Web-first, mobile later |

## Traceability

| Requirement | Actor / Role | Use Case | Domain Concept(s) | Phase | Status |
|-------------|--------------|----------|-------------------|-------|--------|
| AUTH-01 | Visitor | UC-001 | Account, Session | Phase 1 | Pending |
| AUTH-02 | New Member | UC-001 | Account | Phase 1 | Pending |
| AUTH-03 | Member | UC-002 | Account | Phase 1 | Pending |
| AUTH-04 | Member | UC-003 | Session | Phase 1 | Pending |
| PROF-01 | Member | UC-005 | Profile, Account | Phase 2 | Pending |
| PROF-02 | Member | UC-005 | Profile | Phase 2 | Pending |
| PROF-03 | Member | UC-005 | Profile | Phase 2 | Pending |
| PROF-04 | Member | UC-006 | Profile | Phase 2 | Pending |
| CONT-01 | Member | UC-007 | Post | Phase 3 | Pending |
| CONT-02 | Member | UC-007 | Post, Media | Phase 3 | Pending |
| CONT-03 | Post Author | UC-008 | Post | Phase 3 | Pending |
| CONT-04 | Post Author | UC-009 | Post | Phase 3 | Pending |
| CONT-05 | Member | UC-010 | Feed, Post | Phase 3 | Pending |
| SOCL-01 | Member | UC-011 | Follow Relationship | Phase 4 | Pending |
| SOCL-02 | Member | UC-011 | Follow Relationship | Phase 4 | Pending |
| SOCL-03 | Member | UC-012 | Reaction, Post | Phase 4 | Pending |
| SOCL-04 | Member | UC-013 | Comment, Post | Phase 4 | Pending |
| SOCL-05 | Member | UC-014 | Activity Feed, Post | Phase 4 | Pending |

**Coverage:**
- v1 requirements: 18 total
- Mapped to phases: 18
- Unmapped: 0 ✓

---
*Requirements defined: 2025-01-14*
*Last updated: 2025-01-14 after initial definition*
```

</example>
