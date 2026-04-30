# Codebase Integrations Template

Template for `.planning/codebase/integrations.md` — external services and third-party dependencies.

---

## Template

```markdown
# External Integrations

## Authentication

| Service | Purpose | Auth Method | Environment Variables |
|---------|---------|-------------|----------------------|
| NextAuth.js | User authentication | OAuth 2.0 / Credentials | `AUTH_SECRET`, `AUTH_PROVIDER_ID`, `AUTH_PROVIDER_SECRET` |
| [Service] | [Purpose] | [Method] | [Env vars] |

## Database

| Service | Purpose | Connection | Environment Variables |
|---------|---------|------------|----------------------|
| PostgreSQL | Primary database | Direct / Connection pool | `DATABASE_URL` |
| Redis | Session store / Cache | Direct | `REDIS_URL` |

## Storage

| Service | Purpose | Environment Variables |
|---------|---------|----------------------|
| S3 / Cloudflare R2 | File uploads | `STORAGE_ENDPOINT`, `STORAGE_ACCESS_KEY`, `STORAGE_SECRET_KEY` |

## Email

| Service | Purpose | Environment Variables |
|---------|---------|----------------------|
| Resend / SendGrid | Transactional email | `EMAIL_API_KEY`, `EMAIL_FROM` |

## Payments

| Service | Purpose | Environment Variables |
|---------|---------|----------------------|
| Stripe | Payment processing | `STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET` |

## Monitoring & Logging

| Service | Purpose | Environment Variables |
|---------|---------|----------------------|
| Sentry | Error tracking | `SENTRY_DSN` |
| [Service] | [Purpose] | [Env vars] |

## External APIs

| API | Purpose | Base URL | Auth | Environment Variables |
|-----|---------|----------|------|----------------------|
| [API name] | [What it provides] | [URL] | [API Key / OAuth] | [Env vars] |

## Webhook Endpoints

| Endpoint | Service | Purpose |
|----------|---------|---------|
| `/api/webhooks/stripe` | Stripe | Payment events |
| `/api/webhooks/[service]` | [Service] | [Purpose] |

## Environment Configuration

### `.env.example`
```bash
# Auth
AUTH_SECRET=
AUTH_PROVIDER_ID=
AUTH_PROVIDER_SECRET=

# Database
DATABASE_URL=

# Storage
STORAGE_ENDPOINT=
STORAGE_ACCESS_KEY=
STORAGE_SECRET_KEY=

# Email
EMAIL_API_KEY=
EMAIL_FROM=

# Payments
STRIPE_SECRET_KEY=
STRIPE_WEBHOOK_SECRET=

# Monitoring
SENTRY_DSN=
```

## Notes

[Integration-specific notes: rate limits, supported regions, SDK versions, known issues.]
```

---

## Guidelines

**Purpose:** Document all external integrations so new work knows what services are available and how to connect to them.

**What to capture:**
- Every external service the application depends on
- Authentication method and credentials location
- Environment variables required
- Webhook endpoints and their purposes

**Security note:**
- Never document actual secrets or API keys
- Always reference environment variables, not hardcoded values
- Mark services that require user setup (dashboard configuration)

**When adding new integrations:**
- Add to this document
- Add required env vars to `.env.example`
- Document in the phase plan's `user_setup` if human configuration is needed
