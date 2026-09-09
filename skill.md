---
name: Calcom
description: Use when building scheduling integrations, managing bookings, creating event types, checking availability, automating workflows, or building AI agents that interact with Cal.com's scheduling infrastructure. Use for tasks like booking meetings, checking time slots, managing teams/organizations, setting up webhooks, and handling calendar integrations.
metadata:
    mintlify-proj: calcom
    version: "1.0"
---

# Cal.com API v2 Skill

## Product summary

Cal.com API v2 is a REST API for managing scheduling, bookings, event types, and team collaboration. Agents use it to create bookings, check availability, manage event types, handle rescheduling, and automate workflows. The API supports three authentication methods: API keys (recommended for agents), OAuth, and platform credentials. All v2 endpoints require the `cal-api-version: 2024-08-13` header. Base URL: `https://api.cal.com/v2`. Primary docs: https://cal.com/docs/api-reference/v2/introduction

Key files and commands:
- **API Key**: Generate in Settings → Developer → API Keys (prefix: `cal_` for test, `cal_live_` for production)
- **CLI**: `npm install -g @calcom/cli` for command-line access (recommended for agents)
- **Rate limits**: 120 requests/minute (API key auth)
- **Token validity**: Access tokens 60 minutes, refresh tokens 1 year

## When to use

Reach for this skill when:
- **Booking operations**: Creating, rescheduling, or canceling meetings on behalf of users
- **Availability queries**: Checking open time slots for users or teams
- **Event type management**: Creating or updating meeting types with custom fields
- **Team/org operations**: Managing teams, users, memberships, and roles
- **Automation**: Setting up webhooks for booking events or creating workflows
- **Calendar integration**: Connecting calendars, checking busy times, managing schedules
- **AI agents**: Building agents that extract scheduling intent and execute bookings
- **Booking field validation**: Understanding required custom questions before booking

## Quick reference

### Authentication headers

```
Authorization: Bearer YOUR_API_KEY
cal-api-version: 2024-08-13
```

### Core endpoints

| Task | Endpoint | Method |
|------|----------|--------|
| Check availability | `GET /v2/slots` | Query params: `username`, `eventSlug`, `startTime`, `endTime` |
| Create booking | `POST /v2/bookings` | Public endpoint (no auth required) |
| Reschedule booking | `POST /v2/bookings/{uid}/reschedule` | Requires booking UID |
| Cancel booking | `POST /v2/bookings/{uid}/cancel` | Requires booking UID |
| List event types | `GET /v2/event-types` | Query: `username`, `eventSlug`, `orgSlug` |
| Get event type | `GET /v2/event-types/{id}` | Returns booking fields and config |
| Create event type | `POST /v2/event-types` | Requires auth |
| Get schedules | `GET /v2/schedules` | User availability windows |
| Create webhook | `POST /v2/webhooks` | Subscribe to booking events |
| Get bookings | `GET /v2/bookings` | Requires auth |

### Slot query patterns

```bash
# By username + event slug (most common for agents)
/v2/slots?username=bailey&eventSlug=15min&startTime=2024-01-15T00:00:00Z&endTime=2024-01-16T23:59:59Z

# By event type ID
/v2/slots?eventTypeId=10&start=2024-01-15&end=2024-01-16&timeZone=Europe/Rome

# For team event types
/v2/slots?eventTypeSlug=intro&teamSlug=team-slug&start=2024-01-15&end=2024-01-16
```

### Booking field types

| Type | Use case | Example |
|------|----------|---------|
| `name` | Attendee name (fullName or splitName) | `{ "field": "name", "variant": "fullName" }` |
| `email` | Attendee email | Required by default |
| `attendeePhoneNumber` | Phone number (for SMS reminders) | Required if SMS workflow enabled |
| `location` | Meeting location picker | Multiple location options |
| `notes` | Additional information | Custom text field |
| `custom` | Custom questions | `{ "field": "custom", "type": "shortText", "slug": "company" }` |

### Webhook triggers

Common triggers for automation:
- `BOOKING_CREATED` — new booking scheduled
- `BOOKING_RESCHEDULED` — booking moved to new time
- `BOOKING_CANCELLED` — booking removed
- `BOOKING_PAID` — payment processed
- `MEETING_STARTED` — meeting began
- `MEETING_ENDED` — meeting concluded
- `RECORDING_READY` — Cal Video recording available

## Decision guidance

### When to use username/slug vs IDs

| Scenario | Use | Example |
|----------|-----|---------|
| Booking for external user | Username + event slug | `username=bailey&eventSlug=15min` |
| Programmatic lookup | Event type ID | `eventTypeId=123` |
| Team bookings | Team slug + event slug | `teamSlug=sales&eventSlug=demo` |
| Within organization | Add `organizationSlug` | `organizationSlug=acme&username=bob` |

### Authentication method choice

| Use case | Method | Notes |
|----------|--------|-------|
| AI agents | API key | Simplest, 120 req/min rate limit |
| Third-party apps | OAuth | User grants permission, scoped access |
| Platform customers | Platform credentials | For managing multiple users |

### Slot reservation vs booking

| Action | When | Endpoint |
|--------|------|----------|
| Reserve slot | Pre-book to hold time | `POST /v2/slots/reserve` |
| Create booking | Confirm attendee booking | `POST /v2/bookings` |
| Check availability | Query open times | `GET /v2/slots` |

## Workflow

### Typical booking flow

1. **Understand the request**: Extract scheduling intent (who, when, duration, custom fields)
2. **Fetch event type details**: `GET /v2/event-types?username=X&eventSlug=Y` to see booking fields and requirements
3. **Check availability**: `GET /v2/slots?username=X&eventSlug=Y&startTime=...&endTime=...` to find open slots
4. **Validate required fields**: Review `bookingFields` array in event type response; identify required custom questions
5. **Prepare booking payload**: Build request with attendee info, start time, and all required `bookingFieldsResponses`
6. **Create booking**: `POST /v2/bookings` with complete payload (no auth required for public bookings)
7. **Handle response**: Capture booking UID for future rescheduling/cancellation
8. **Set up automation** (optional): Create webhook to track booking lifecycle events

### Rescheduling flow

1. Obtain booking UID from original booking response or `GET /v2/bookings`
2. Check new availability: `GET /v2/slots?...&bookingUidToReschedule=UID` (excludes original slot from busy time)
3. Call `POST /v2/bookings/{uid}/reschedule` with new start time and optional reason
4. Confirm response includes updated booking details

### Team event type setup

1. Create team: `POST /v2/teams` (requires org admin role)
2. Create team event type: `POST /v2/teams/{teamId}/event-types` with hosts and scheduling type
3. Set scheduling type: `collective` (all hosts attend), `roundRobin` (rotate hosts), or `managed` (template)
4. Assign hosts: Include `hosts` array with user IDs and `mandatory` flag
5. Test booking: Use `teamSlug` + `eventTypeSlug` in slot queries

## Common gotchas

- **Missing `cal-api-version` header**: Requests without this header return 404. Always include `cal-api-version: 2024-08-13`.
- **Required booking fields**: If event type has custom questions marked required, omitting them returns 400 error. Always fetch event type first to see `bookingFields`.
- **Time zones**: Pass times in UTC (no timezone offset). Specify attendee timezone in booking request: `"attendee": { "timeZone": "America/New_York" }`.
- **Slot format**: By default returns object with dates as keys. Use `format=range` query param to get start/end times.
- **Managed event types**: Cannot fetch slots for parent managed event type directly. Use child event type IDs (assigned to specific users).
- **Public booking endpoint**: `POST /v2/bookings` does not require authentication, allowing external bookings. Secure by validating attendee email or using private links.
- **Booking field responses**: Use exact slug names from event type response. Typos in `bookingFieldsResponses` keys are silently ignored.
- **Instant bookings**: Only work for team event types configured for instant meetings. Requires `instant: true` in request.
- **Rescheduling same slot**: Use `bookingUidToReschedule` query param to exclude original booking from busy time calculation.
- **Webhook payload versions**: Default version `2021-10-20` is legacy. Use `version: 2026-07-27` for ICS calendar content in payloads.
- **Rate limits**: 120 requests/minute per API key. Implement exponential backoff for retries.
- **Token expiration**: Access tokens expire after 60 minutes. Refresh using refresh token before expiry.

## Verification checklist

Before submitting booking or event type operations:

- [ ] Include `cal-api-version: 2024-08-13` header in all requests
- [ ] Verify authentication method (API key, OAuth, or public endpoint)
- [ ] Fetch event type and confirm all required `bookingFields` are included in request
- [ ] Check availability before booking to avoid conflicts
- [ ] Validate time zones: attendee timezone in booking, UTC times in API calls
- [ ] For team bookings: confirm team slug and event type slug are correct
- [ ] For rescheduling: include `bookingUidToReschedule` to exclude original slot from busy time
- [ ] Test with a non-production event type first
- [ ] Confirm webhook payload version matches expected format (default `2021-10-20`, use `2026-07-27` for ICS)
- [ ] Check rate limit headers in response: `X-RateLimit-Remaining`

## Resources

**Comprehensive navigation**: https://cal.com/docs/llms.txt

**Critical documentation pages**:
1. [API v2 Introduction & Authentication](https://cal.com/docs/api-reference/v2/introduction) — Auth methods, rate limits, endpoint availability by plan
2. [AI Agents Guide](https://cal.com/docs/agents) — Booking workflows, credit management, best practices for agents
3. [Access Control & Roles](https://cal.com/docs/api-reference/v2/access-control) — PBAC, OAuth scopes, membership roles for teams/orgs

---

> For additional documentation and navigation, see: https://cal.com/docs/llms.txt