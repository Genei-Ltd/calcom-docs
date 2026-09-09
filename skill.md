---
name: Calcom
description: Use when building integrations with Cal.com's scheduling platform, managing bookings and event types, automating workflows with webhooks, or building AI agents that interact with scheduling infrastructure. Agents should reach for this skill when handling booking creation, availability checks, rescheduling, calendar integrations, team management, or event type configuration.
metadata:
    mintlify-proj: calcom
    version: "1.0"
---

# Cal.com API v2 Skill

## Product summary

Cal.com API v2 is a REST API for managing scheduling, bookings, event types, calendars, and team workflows. Agents use it to create bookings, check availability, manage schedules, configure event types, and automate scheduling workflows. The API supports three authentication methods: OAuth (recommended for integrations), API keys (for direct access), and Platform credentials (deprecated). All requests require the `cal-api-version: 2024-08-13` header. Primary documentation: https://cal.com/docs/api-reference/v2/introduction

Key endpoints:
- `POST /v2/bookings` — Create a booking
- `GET /v2/slots` — Check available time slots
- `GET /v2/event-types` — List event types
- `POST /v2/bookings/{uid}/reschedule` — Reschedule a booking
- `POST /v2/webhooks` — Configure webhooks for automation

## When to use

Reach for this skill when:
- **Creating or managing bookings** — Schedule meetings, reschedule, or cancel existing bookings
- **Checking availability** — Query available time slots for users or teams
- **Building AI agents** — Agents that extract scheduling intent from natural language and execute booking operations
- **Configuring event types** — Create, update, or delete meeting types with custom fields
- **Automating workflows** — Set up webhooks to trigger actions on booking events (created, cancelled, rescheduled)
- **Managing calendars** — Connect external calendars (Google, Outlook, Apple), check busy times, or sync meeting details
- **Team operations** — Create teams, manage memberships, configure team-level event types and schedules
- **Organization management** — Manage users, roles, permissions, and team structures in multi-user environments
- **Tracking usage** — Check and charge credits for agent interactions

Do not use this skill for: UI/dashboard operations, account creation, authentication setup, or pricing/billing queries.

## Quick reference

### Authentication methods

| Method | Use case | Header format |
|--------|----------|---------------|
| API Key | Direct access, agents, scripts | `Authorization: Bearer cal_live_xxxx` |
| OAuth | Integrations, third-party apps | `Authorization: Bearer <access_token>` |
| Platform (deprecated) | Legacy managed users only | `x-cal-client-id` + `x-cal-secret-key` |

### Required headers for all requests

```
cal-api-version: 2024-08-13
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json
```

### Core API endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/v2/slots` | GET | Get available time slots (public, no auth required) |
| `/v2/bookings` | POST | Create a booking (public) |
| `/v2/bookings` | GET | List all bookings (requires `BOOKING_READ` scope) |
| `/v2/bookings/{uid}` | GET | Get a specific booking |
| `/v2/bookings/{uid}/reschedule` | POST | Reschedule a booking |
| `/v2/bookings/{uid}/cancel` | POST | Cancel a booking |
| `/v2/event-types` | GET | List event types |
| `/v2/event-types` | POST | Create an event type |
| `/v2/schedules` | GET | Get user schedules |
| `/v2/schedules` | POST | Create a schedule |
| `/v2/webhooks` | POST | Create a webhook |
| `/v2/credits/available` | GET | Check available credits |
| `/v2/credits/charge` | POST | Charge credits for usage |

### OAuth scopes (most common)

| Scope | Access |
|-------|--------|
| `BOOKING_READ` | View bookings |
| `BOOKING_WRITE` | Create, edit, delete bookings |
| `EVENT_TYPE_READ` | View event types |
| `EVENT_TYPE_WRITE` | Create, edit, delete event types |
| `SCHEDULE_READ` | View availability |
| `SCHEDULE_WRITE` | Create, edit, delete schedules |
| `APPS_READ` | View connected apps |
| `APPS_WRITE` | Connect/disconnect apps |
| `WEBHOOK_READ` | View webhooks |
| `WEBHOOK_WRITE` | Create, edit, delete webhooks |

Team and organization scopes use `TEAM_` and `ORG_` prefixes (e.g., `TEAM_BOOKING_READ`, `ORG_PROFILE_WRITE`).

### Rate limits

- **API Key**: 120 requests per minute (can be increased via support)
- **OAuth**: Same as API key
- **No auth**: 120 requests per minute default

## Decision guidance

### When to use API key vs OAuth

| Scenario | Use API Key | Use OAuth |
|----------|------------|----------|
| Building an integration for third-party apps | ❌ | ✅ |
| Direct agent access to your own Cal.com account | ✅ | ❌ |
| Accessing user's Cal.com account with permission | ❌ | ✅ |
| Server-to-server automation | ✅ | ❌ |
| Public booking creation (no auth needed) | N/A | N/A |

### When to use public endpoints vs authenticated

| Endpoint | Public | Authenticated | Notes |
|----------|--------|---------------|-------|
| `POST /v2/bookings` (create) | ✅ | ✅ | No auth required; token accepted but optional |
| `GET /v2/slots` | ✅ | ✅ | No auth required; query by username/eventSlug |
| `GET /v2/bookings` | ❌ | ✅ | Requires `BOOKING_READ` scope |
| `POST /v2/bookings/{uid}/cancel` | ✅ | ✅ | Public; token optional |
| `POST /v2/bookings/{uid}/reschedule` | ✅ | ✅ | Public; token optional |

### When to use instant bookings

Use `"instant": true` in booking creation when:
- Handling urgent support requests that need immediate routing
- Event type is configured for instant meetings
- You want to bypass normal scheduling and ring available team members immediately

## Workflow

### 1. Check availability before booking

```bash
# Query available slots by username and event slug
curl -X GET "https://api.cal.com/v2/slots?username=bailey&eventSlug=15min&startTime=2024-01-15T00:00:00Z&endTime=2024-01-16T23:59:59Z" \
  -H "cal-api-version: 2024-08-13"
```

### 2. Create a booking

```bash
curl -X POST "https://api.cal.com/v2/bookings" \
  -H "Content-Type: application/json" \
  -H "cal-api-version: 2024-08-13" \
  -d '{
    "eventTypeSlug": "15min",
    "username": "bailey",
    "start": "2024-01-15T09:00:00Z",
    "attendee": {
      "name": "John Doe",
      "email": "john@example.com",
      "timeZone": "America/New_York"
    }
  }'
```

### 3. Handle custom booking fields

If the event type has required custom questions, include them in `bookingFieldsResponses`:

```bash
curl -X POST "https://api.cal.com/v2/bookings" \
  -H "Content-Type: application/json" \
  -H "cal-api-version: 2024-08-13" \
  -d '{
    "eventTypeSlug": "consultation",
    "username": "bailey",
    "start": "2024-01-15T09:00:00Z",
    "attendee": {
      "name": "John Doe",
      "email": "john@example.com",
      "timeZone": "America/New_York"
    },
    "bookingFieldsResponses": {
      "notes": "Discussing the new AI integration",
      "company_size": "10-50"
    }
  }'
```

### 4. Reschedule a booking

```bash
curl -X POST "https://api.cal.com/v2/bookings/{bookingUid}/reschedule" \
  -H "Content-Type: application/json" \
  -H "cal-api-version: 2024-08-13" \
  -d '{
    "start": "2024-01-16T10:00:00Z",
    "rescheduleReason": "Attendee requested different time"
  }'
```

### 5. Cancel a booking

```bash
curl -X POST "https://api.cal.com/v2/bookings/{bookingUid}/cancel" \
  -H "Content-Type: application/json" \
  -H "cal-api-version: 2024-08-13" \
  -d '{
    "cancellationReason": "Meeting no longer needed"
  }'
```

### 6. Set up a webhook for automation

```bash
curl -X POST "https://api.cal.com/v2/webhooks" \
  -H "Authorization: Bearer cal_live_xxxx" \
  -H "Content-Type: application/json" \
  -H "cal-api-version: 2024-08-13" \
  -d '{
    "subscriberUrl": "https://your-app.com/webhooks/cal",
    "eventTriggers": ["BOOKING_CREATED", "BOOKING_RESCHEDULED", "BOOKING_CANCELLED"],
    "active": true
  }'
```

### 7. Check and charge credits (for agents)

```bash
# Check available credits
curl -X GET "https://api.cal.com/v2/credits/available" \
  -H "Authorization: Bearer cal_live_xxxx" \
  -H "cal-api-version: 2024-08-13"

# Charge credits after completing agent work
curl -X POST "https://api.cal.com/v2/credits/charge" \
  -H "Authorization: Bearer cal_live_xxxx" \
  -H "Content-Type: application/json" \
  -H "cal-api-version: 2024-08-13" \
  -d '{
    "credits": 5,
    "creditFor": "AI_AGENT",
    "externalRef": "agent-thread-abc-1711432800000"
  }'
```

## Common gotchas

- **Missing `cal-api-version` header** — All v2 requests require `cal-api-version: 2024-08-13`. Omitting it returns 404. Always include this header.
- **Confusing username vs userId** — Use `username` (the handle, e.g., "bailey") in public endpoints like `/v2/slots` and `/v2/bookings`. Use `userId` only in authenticated endpoints that require it.
- **Required booking fields** — If an event type has custom questions marked as required, omitting them in `bookingFieldsResponses` returns a 400 error. Fetch the event type details first to discover required fields.
- **Time zone handling** — Always specify time zones explicitly in attendee objects. Omitting `timeZone` can cause scheduling conflicts. Store user preferences and pass them consistently.
- **Slot availability race condition** — Check slots immediately before booking; availability can change. Implement retry logic if a slot becomes unavailable between check and booking.
- **OAuth token expiration** — Access tokens expire after 60 minutes. Refresh tokens last 1 year. Implement token refresh logic before making requests.
- **Webhook secret verification** — If you set a webhook secret, verify the signature on incoming payloads using the `x-cal-signature` header. Failing to verify allows spoofed webhooks.
- **Seated event types** — For seated events, the webhook `attendees` array contains only the attendee for the specific seat that triggered the webhook, not all attendees.
- **Platform endpoints deprecated** — Platform OAuth and managed user endpoints are deprecated as of December 15, 2025. Use standard OAuth or API keys instead.
- **Rate limit headers** — Check `x-ratelimit-remaining` and `x-ratelimit-reset` headers in responses. Implement exponential backoff when approaching limits.
- **Idempotency for credits** — Always include `externalRef` when charging credits to prevent double-charging on retries.

## Verification checklist

Before submitting work with Cal.com API:

- [ ] All requests include `cal-api-version: 2024-08-13` header
- [ ] Authentication header is correct (`Authorization: Bearer` for API key or OAuth token)
- [ ] Time zones are explicitly specified in attendee objects
- [ ] Required booking fields are included in `bookingFieldsResponses`
- [ ] Availability was checked before attempting to create a booking
- [ ] Webhook payloads are verified using the secret (if configured)
- [ ] Credit charges include `externalRef` for idempotency
- [ ] Retry logic handles rate limits (429 responses)
- [ ] OAuth tokens are refreshed before expiration (60-minute window)
- [ ] Error responses are logged with full request/response bodies for debugging
- [ ] Team/organization endpoints use correct role-based access (owner > admin > member)
- [ ] OAuth scopes match the endpoints being called

## Resources

**Comprehensive navigation**: https://cal.com/docs/llms.txt

**Critical documentation pages**:
1. [API v2 Introduction & Authentication](https://cal.com/docs/api-reference/v2/introduction) — Authentication methods, rate limits, endpoint access by plan
2. [OAuth & Scopes](https://cal.com/docs/api-reference/v2/oauth) — Available scopes, scope hierarchy, OAuth client setup
3. [AI Agents Guide](https://cal.com/docs/agents) — Recommended workflows for agents, credit management, best practices, CLI alternative

---

> For additional documentation and navigation, see: https://cal.com/docs/llms.txt