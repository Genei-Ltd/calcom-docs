# Cal.com Docs: API v2 Reference

## API v2 Reference

- [API v2 Reference / ORGANIZATIONS (143 pages)](https://cal.com/docs/_llms/api-v2-reference/organizations.md): Documentation for API v2 Reference / ORGANIZATIONS.

### Getting Started

- [Introduction to API v2](https://cal.com/docs/api-reference/v2/introduction.md): Introduction to Cal.com API v2 endpoints
- [OAuth](https://cal.com/docs/api-reference/v2/oauth.md): Authorize apps with Cal.com accounts using OAuth
- [Access Control](https://cal.com/docs/api-reference/v2/access-control.md): Roles, permissions, and OAuth scopes for organizations and teams API v2 endpoints
- [Migrating from API v1 to v2](https://cal.com/docs/api-reference/v2/v1-v2-differences.md): Complete guide for migrating your Cal.com integration from v1 to v2
- [MCP server](https://cal.com/docs/mcp-server.md): Connect AI clients to Cal.com scheduling through the Model Context Protocol using the hosted server at mcp.cal.com or a local instance.
- [User booking limits](https://cal.com/docs/api-reference/v2/user-booking-limits.md): Cap the total number of bookings a user can accept across all event types per day, week, month, or year.
- [AI agents](https://cal.com/docs/agents.md): How AI agents can use the Cal.com API v2 to manage scheduling

### CORE

#### Me

- [Get my profile](https://cal.com/docs/api-reference/v2/me/get-my-profile.md): If accessed using an OAuth access token, the `PROFILE_READ` scope is required.
- [Update my profile](https://cal.com/docs/api-reference/v2/me/update-my-profile.md): Updates the authenticated user's profile. Email changes require verification and the primary email stays unchanged until verification completes, unless the new email is already a verified secondary email or the user is platform-managed. If accessed using an OAuth access token, the `PROFILE_WRITE` sc…
- [Get my booking limits](https://cal.com/docs/api-reference/v2/me/get-my-booking-limits.md): Returns the authenticated user's global booking limits. Unset bounds are returned as null. Only available to organization members — non-org accounts receive a 403. If accessed using an OAuth access token, the `PROFILE_READ` scope is required.
- [Update my booking limits](https://cal.com/docs/api-reference/v2/me/update-my-booking-limits.md): Partially updates the authenticated user's global booking limits. Only fields present in the request body are changed; omit a field to leave it untouched, or set it to null to remove that limit. Only available to organization members — non-org accounts receive a 403. If accessed using an OAuth acces…
- [Clear my booking limits](https://cal.com/docs/api-reference/v2/me/clear-my-booking-limits.md): Removes all of the authenticated user's global booking limits. Only available to organization members — non-org accounts receive a 403. If accessed using an OAuth access token, the `PROFILE_WRITE` scope is required.
- [Get my team booking limits](https://cal.com/docs/api-reference/v2/me/get-my-team-booking-limits.md): Returns every team whose booking limit applies to you as a round-robin host, with the team's default, your own number where you set one, and what is enforced. Teams you host for that set no limit are omitted. Your own number only applies where you are a round-robin host: on collective events and eve…
- [Set my booking limit for one team](https://cal.com/docs/api-reference/v2/me/set-my-booking-limit-for-one-team.md): Sets your own numbers for this team's booking limit. Intervals you omit keep what you stored before, an interval sent as `null` goes back to inheriting the team default, and every value is capped at your own overall limit for the same interval. Only teams you are a round-robin host of accept this; t…
- [Clear my booking limit for one team](https://cal.com/docs/api-reference/v2/me/clear-my-booking-limit-for-one-team.md): Drops your own numbers for this team so the team default applies to you again. This does not lift the team's limit. If accessed using an OAuth access token, the `PROFILE_WRITE` scope is required.

#### Bookings

- [Create a booking](https://cal.com/docs/api-reference/v2/bookings/create-a-booking.md): POST /v2/bookings is used to create regular bookings, recurring bookings and instant bookings. The request bodies for all 3 are almost the same except:       If eventTypeId in the request body is id of a regular event, then regular booking is created.
- [Get all bookings](https://cal.com/docs/api-reference/v2/bookings/get-all-bookings.md): Cursor-based pagination. Pass the `pagination.nextCursor` from the previous response as the `cursor` query parameter to fetch the next page. Omit `cursor` to fetch the first page. `pagination.hasMore` is `false` and `pagination.nextCursor` is `null` when you've reached the last page.
- [Get a booking by seat UID](https://cal.com/docs/api-reference/v2/bookings/get-a-booking-by-seat-uid.md): Get a seated booking by its seat reference UID. This is useful when you have a seatUid from a seated booking and want to retrieve the full booking details.
- [Get a booking](https://cal.com/docs/api-reference/v2/bookings/get-a-booking.md): `:bookingUid` can be
- [Get all the recordings for the booking](https://cal.com/docs/api-reference/v2/bookings/get-all-the-recordings-for-the-booking.md): Fetches all the recordings for the booking `:bookingUid`. Requires authentication and proper authorization. Access is granted if you are the booking organizer, team admin or org admin/owner.
- [Get Cal Video real time transcript download links for the booking](https://cal.com/docs/api-reference/v2/bookings/get-cal-video-real-time-transcript-download-links-for-the-booking.md): Fetches all the transcript download links for the booking `:bookingUid`
- [Reschedule a booking](https://cal.com/docs/api-reference/v2/bookings/reschedule-a-booking.md): Reschedule a booking or seated booking.
- [Request to reschedule a booking](https://cal.com/docs/api-reference/v2/bookings/request-to-reschedule-a-booking.md): Request to reschedule a booking. The booking will be cancelled and the attendee will receive an email with a link to reschedule.
- [Cancel a booking](https://cal.com/docs/api-reference/v2/bookings/cancel-a-booking.md): :bookingUid can be :bookingUid of an usual booking, individual recurrence or recurring booking to cancel all recurrences.
- [Mark a booking absence](https://cal.com/docs/api-reference/v2/bookings/mark-a-booking-absence.md): The provided authorization header refers to the owner of the booking.
- [Reassign a booking to auto-selected host](https://cal.com/docs/api-reference/v2/bookings/reassign-a-booking-to-auto-selected-host.md): Currently only supports reassigning host for round robin bookings. The provided authorization header refers to the owner of the booking.
- [Reassign a booking to a specific host](https://cal.com/docs/api-reference/v2/bookings/reassign-a-booking-to-a-specific-host.md): Currently only supports reassigning host for round robin bookings. The provided authorization header refers to the owner of the booking.
- [Confirm a booking](https://cal.com/docs/api-reference/v2/bookings/confirm-a-booking.md): The provided authorization header refers to the owner of the booking.
- [Decline a booking](https://cal.com/docs/api-reference/v2/bookings/decline-a-booking.md): The provided authorization header refers to the owner of the booking.
- [Get 'Add to Calendar' links for a booking](https://cal.com/docs/api-reference/v2/bookings/get-add-to-calendar-links-for-a-booking.md): Retrieve calendar links for a booking that can be used to add the event to various calendar services. Returns links for Google Calendar, Microsoft Office, Microsoft Outlook, and a downloadable ICS file.
- [Get booking references](https://cal.com/docs/api-reference/v2/bookings/get-booking-references.md): <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>
- [Get Video Meeting Sessions. Only supported for Cal Video](https://cal.com/docs/api-reference/v2/bookings/get-video-meeting-sessions-only-supported-for-cal-video.md): Requires authentication and proper authorization. Access is granted if you are the booking organizer, team admin or org admin/owner.
- [Get the routing trace for a booking](https://cal.com/docs/api-reference/v2/bookings-routing-trace/get-the-routing-trace-for-a-booking.md): Retrieve the step-by-step routing trace for a booking identified by its UID. Shows how the booking was routed through routing forms, CRM lookups, and host selection logic.
- [Update booking location for an existing booking](https://cal.com/docs/api-reference/v2/bookings/update-booking-location-for-an-existing-booking.md): Updates the booking location in Cal.com and updates the corresponding calendar event via the organizer's connected credentials. For integration locations (e.g. Zoom, Google Meet, Cal Video), the endpoint also provisions a conference link. Attendees are notified of the location change by email.…

##### Attendees

- [Get all attendees for a booking](https://cal.com/docs/api-reference/v2/bookings-attendees/get-all-attendees-for-a-booking.md): Retrieve all attendees for a specific booking by its UID.          <Note>The cal-api-version header is required for this endpoint. Without it, the request will fail with a 404 error.</Note>
- [Add an attendee to a booking](https://cal.com/docs/api-reference/v2/bookings-attendees/add-an-attendee-to-a-booking.md): Add a new attendee to an existing booking by its UID.
- [Get a specific attendee for a booking](https://cal.com/docs/api-reference/v2/bookings-attendees/get-a-specific-attendee-for-a-booking.md): Retrieve a specific attendee by their ID for a booking identified by its UID.                <Note>The cal-api-version header is required for this endpoint. Without it, the request will fail with a 404 error.</Note>

##### Guests

- [Add guests to an existing booking](https://cal.com/docs/api-reference/v2/bookings-guests/add-guests-to-an-existing-booking.md): Add one or more guests to an existing booking. Maximum 10 guests per request, with a limit of 30 total guests per booking.          **Rate Limiting:**     This endpoint is rate limited to 5 requests per minute to prevent abuse.          **Seated Events:**     This endpoint does not support seated ev…

##### Email Verification

- [Check if email verification is required](https://cal.com/docs/api-reference/v2/bookings--email-verification/check-if-email-verification-is-required.md): Checks whether email verification is required for the given email. Returns true if verification is needed.
- [Send email verification code](https://cal.com/docs/api-reference/v2/bookings--email-verification/send-email-verification-code.md): Sends a one-time verification code to the specified email address.
- [Verify email with code](https://cal.com/docs/api-reference/v2/bookings--email-verification/verify-email-with-code.md): Verifies an email address using the one-time code that was previously sent.

#### Schedules

- [Create a schedule](https://cal.com/docs/api-reference/v2/schedules/create-a-schedule.md): Create a schedule for the authenticated user.
- [Get all schedules](https://cal.com/docs/api-reference/v2/schedules/get-all-schedules.md): Get all schedules of the authenticated user.           <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>
- [Get default schedule](https://cal.com/docs/api-reference/v2/schedules/get-default-schedule.md): Get the default schedule of the authenticated user.          <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>
- [Get a schedule](https://cal.com/docs/api-reference/v2/schedules/get-a-schedule.md): <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>
- [Update a schedule](https://cal.com/docs/api-reference/v2/schedules/update-a-schedule.md): <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>
- [Delete a schedule](https://cal.com/docs/api-reference/v2/schedules/delete-a-schedule.md): <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>

#### Slots

- [Get available time slots for an event type](https://cal.com/docs/api-reference/v2/slots/get-available-time-slots-for-an-event-type.md): There are 4 ways to get available slots for event type of an individual user:
- [Reserve a slot](https://cal.com/docs/api-reference/v2/slots/reserve-a-slot.md): Make a slot not available for others to book for a certain period of time. If you authenticate using oAuth credentials, api key or access token     then you can also specify custom duration for how long the slot should be reserved for (defaults to 5 minutes).          <Note>Please make sure to pass…
- [Get reserved slot](https://cal.com/docs/api-reference/v2/slots/get-reserved-slot.md): <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>
- [Update a reserved slot](https://cal.com/docs/api-reference/v2/slots/update-a-reserved-slot.md): If you specify a custom reservation duration, you must authenticate using oAuth credentials, api key or access token.
- [Delete a reserved slot](https://cal.com/docs/api-reference/v2/slots/delete-a-reserved-slot.md): <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>

#### Out of Office

- [Get all out-of-office entries for the authenticated user](https://cal.com/docs/api-reference/v2/out-of-office/get-all-out-of-office-entries-for-the-authenticated-user.md): If accessed using an OAuth access token, the `SCHEDULE_READ` scope is required.
- [Create an out-of-office entry for the authenticated user](https://cal.com/docs/api-reference/v2/out-of-office/create-an-out-of-office-entry-for-the-authenticated-user.md): If accessed using an OAuth access token, the `SCHEDULE_WRITE` scope is required.
- [Update an out-of-office entry for the authenticated user](https://cal.com/docs/api-reference/v2/out-of-office/update-an-out-of-office-entry-for-the-authenticated-user.md): If accessed using an OAuth access token, the `SCHEDULE_WRITE` scope is required.
- [Delete an out-of-office entry for the authenticated user](https://cal.com/docs/api-reference/v2/out-of-office/delete-an-out-of-office-entry-for-the-authenticated-user.md): If accessed using an OAuth access token, the `SCHEDULE_WRITE` scope is required.

#### Notifications

- [Register an app push subscription](https://cal.com/docs/api-reference/v2/notifications/register-an-app-push-subscription.md)
- [Remove an app push subscription](https://cal.com/docs/api-reference/v2/notifications/remove-an-app-push-subscription.md)
- [Create a Slack push linking intent](https://cal.com/docs/api-reference/v2/notifications/create-a-slack-push-linking-intent.md)
- [Remove a Slack push subscription](https://cal.com/docs/api-reference/v2/notifications/remove-a-slack-push-subscription.md)
- [Create a Telegram push linking intent](https://cal.com/docs/api-reference/v2/notifications/create-a-telegram-push-linking-intent.md)
- [Remove a Telegram push subscription](https://cal.com/docs/api-reference/v2/notifications/remove-a-telegram-push-subscription.md)

#### Credits

- [Check available credits](https://cal.com/docs/api-reference/v2/credits/check-available-credits.md): Check if the authenticated user (or their org/team) has available credits and return the current balance. Third-party OAuth tokens require the `CREDITS_READ` scope.
- [Charge credits](https://cal.com/docs/api-reference/v2/credits/charge-credits.md): Charge credits for an authenticated user. Uses externalRef for idempotency to prevent double-charging. Third-party OAuth tokens require the `CREDITS_WRITE` scope.

#### Insights

- [Get average booking duration](https://cal.com/docs/api-reference/v2/insights/get-average-booking-duration.md): Get average booking duration for user, team, or organization insights.
- [Get booking event trends](https://cal.com/docs/api-reference/v2/insights/get-booking-event-trends.md): Get booking trend stats for user, team, or organization insights.
- [Get booking KPI stats](https://cal.com/docs/api-reference/v2/insights/get-booking-kpi-stats.md): Get booking KPI stats for user, team, or organization insights.
- [Get booking member stats](https://cal.com/docs/api-reference/v2/insights/get-booking-member-stats.md): Get booking member stats for user, team, or organization insights.
- [Get failed bookings by routing field](https://cal.com/docs/api-reference/v2/insights/get-failed-bookings-by-routing-field.md): Get failed booking counts grouped by routing form field for user, team, or organization insights.
- [Get routing form field options](https://cal.com/docs/api-reference/v2/insights/get-routing-form-field-options.md): Get routing form fields and options for user, team, or organization insights.
- [Get routing form response headers](https://cal.com/docs/api-reference/v2/insights/get-routing-form-response-headers.md): Get routing form response headers for user, team, or organization insights.
- [Get routing form responses](https://cal.com/docs/api-reference/v2/insights/get-routing-form-responses.md): Get paginated routing form responses for user, team, or organization insights.
- [Get routing forms by status](https://cal.com/docs/api-reference/v2/insights/get-routing-forms-by-status.md): Get routing form response counts by booking status for user, team, or organization insights.
- [Get routed-to users per period](https://cal.com/docs/api-reference/v2/insights/get-routed-to-users-per-period.md): Get routed-to booking counts by user and period for user, team, or organization insights.

#### Allowlists

- [Get the Cal.com IP allowlists](https://cal.com/docs/api-reference/v2/allowlists/get-the-calcom-ip-allowlists.md): Returns the IPv4 ranges Cal.com sends traffic from and receives traffic on, keyed by service. Poll this endpoint instead of hard-coding addresses, because they can change.
- [Get the Cal.com IP allowlist of one service](https://cal.com/docs/api-reference/v2/allowlists/get-the-calcom-ip-allowlist-of-one-service.md)

### CALENDARS

#### Calendars

- [Save an ICS feed](https://cal.com/docs/api-reference/v2/calendars/save-an-ics-feed.md): If accessed using an OAuth access token, the `APPS_WRITE` scope is required.
- [Check an ICS feed](https://cal.com/docs/api-reference/v2/calendars/check-an-ics-feed.md): If accessed using an OAuth access token, the `APPS_READ` scope is required.
- [Get busy times](https://cal.com/docs/api-reference/v2/calendars/get-busy-times.md): Get busy times from a calendar. Example request URL is `https://api.cal.com/v2/calendars/busy-times?timeZone=Europe%2FMadrid&dateFrom=2024-12-18&dateTo=2024-12-18&calendarsToLoad[0][credentialId]=135&calendarsToLoad[0][externalId]=skrauciz%40gmail.com`. Note: loggedInUsersTz is deprecated, use timeZ…
- [Get all calendars](https://cal.com/docs/api-reference/v2/calendars/get-all-calendars.md): If accessed using an OAuth access token, the `APPS_READ` scope is required.
- [Get OAuth connect URL](https://cal.com/docs/api-reference/v2/calendars/get-oauth-connect-url.md): If accessed using an OAuth access token, the `APPS_WRITE` scope is required.
- [Save Google or Outlook calendar credentials](https://cal.com/docs/api-reference/v2/calendars/save-google-or-outlook-calendar-credentials.md)
- [Save Apple calendar credentials](https://cal.com/docs/api-reference/v2/calendars/save-apple-calendar-credentials.md): If accessed using an OAuth access token, the `APPS_WRITE` scope is required.
- [Check a calendar connection](https://cal.com/docs/api-reference/v2/calendars/check-a-calendar-connection.md): If accessed using an OAuth access token, the `APPS_READ` scope is required.
- [Disconnect a calendar](https://cal.com/docs/api-reference/v2/calendars/disconnect-a-calendar.md): If accessed using an OAuth access token, the `APPS_WRITE` scope is required.

#### Cal Unified Calendars

- [Get meeting details from calendar](https://cal.com/docs/api-reference/v2/cal-unified-calendars/get-meeting-details-from-calendar.md): Returns detailed information about a meeting including attendance metrics. If accessed using an OAuth access token, the `APPS_READ` scope is required.
- [Update meeting details in calendar](https://cal.com/docs/api-reference/v2/cal-unified-calendars/update-meeting-details-in-calendar.md): Updates event information in the specified calendar provider. If accessed using an OAuth access token, the `APPS_WRITE` scope is required.

#### Selected Calendars

- [Add a selected calendar](https://cal.com/docs/api-reference/v2/selected-calendars/add-a-selected-calendar.md): If accessed using an OAuth access token, the `APPS_WRITE` scope is required.
- [Delete a selected calendar](https://cal.com/docs/api-reference/v2/selected-calendars/delete-a-selected-calendar.md): If accessed using an OAuth access token, the `APPS_WRITE` scope is required.

#### Destination Calendars

- [Update destination calendars](https://cal.com/docs/api-reference/v2/destination-calendars/update-destination-calendars.md): If accessed using an OAuth access token, the `APPS_WRITE` scope is required.

#### Conferencing

- [Conferencing Apps](https://cal.com/docs/api-reference/v2/conferencing-apps.md): Connect Zoom, Microsoft Teams or Google Meet to a user or a team
- [Connect your conferencing application](https://cal.com/docs/api-reference/v2/conferencing/connect-your-conferencing-application.md): Only `google-meet` can be connected this way, and only for a user who already has a valid Google Calendar connection. Zoom and Microsoft Teams require an OAuth handshake - start it with `GET /v2/conferencing/{app}/oauth/auth-url` instead. Walkthrough: https://cal.com/docs/api-reference/v2/conferenci…
- [Get OAuth conferencing app auth URL](https://cal.com/docs/api-reference/v2/conferencing/get-oauth-conferencing-app-auth-url.md): Returns the URL to send the user to so they can authorize Zoom or Microsoft Teams. Redirect the user's browser to it - the provider then returns them to a callback already registered by Cal.com, which stores the credential against the owner of the access token that started the flow. `returnTo` and `…
- [Conferencing app OAuth callback](https://cal.com/docs/api-reference/v2/conferencing/conferencing-app-oauth-callback.md)
- [List your conferencing applications](https://cal.com/docs/api-reference/v2/conferencing/list-your-conferencing-applications.md): If accessed using an OAuth access token, the `APPS_READ` scope is required.
- [Set your default conferencing application](https://cal.com/docs/api-reference/v2/conferencing/set-your-default-conferencing-application.md): If accessed using an OAuth access token, the `APPS_WRITE` scope is required.
- [Get your default conferencing application](https://cal.com/docs/api-reference/v2/conferencing/get-your-default-conferencing-application.md): If accessed using an OAuth access token, the `APPS_READ` scope is required.
- [Disconnect your conferencing application](https://cal.com/docs/api-reference/v2/conferencing/disconnect-your-conferencing-application.md): If accessed using an OAuth access token, the `APPS_WRITE` scope is required.

### EVENT TYPES & AUTOMATION

#### Event Types

- [Create an event type](https://cal.com/docs/api-reference/v2/event-types/create-an-event-type.md): <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section.</Note>
- [List event types](https://cal.com/docs/api-reference/v2/event-types/list-event-types.md): <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>
- [Get an event type](https://cal.com/docs/api-reference/v2/event-types/get-an-event-type.md): <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>
- [Update an event type](https://cal.com/docs/api-reference/v2/event-types/update-an-event-type.md): <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>
- [Delete an event type](https://cal.com/docs/api-reference/v2/event-types/delete-an-event-type.md): <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>
- [Get event type history](https://cal.com/docs/api-reference/v2/event-types/get-event-type-history.md): <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>
- [Get scheduling configuration](https://cal.com/docs/api-reference/v2/event-types/get-scheduling-configuration.md): <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>
- [List CRM sync errors for an event type](https://cal.com/docs/api-reference/v2/event-types/list-crm-sync-errors-for-an-event-type.md): <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>

##### Booking Fields

- [Get booking fields](https://cal.com/docs/api-reference/v2/event-types/get-booking-fields.md): <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>
- [Replace booking fields](https://cal.com/docs/api-reference/v2/event-types/replace-booking-fields.md): <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>
- [Add custom booking fields](https://cal.com/docs/api-reference/v2/event-types/add-custom-booking-fields.md): <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>
- [Update booking fields](https://cal.com/docs/api-reference/v2/event-types/update-booking-fields.md): <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>
- [Delete a custom booking field](https://cal.com/docs/api-reference/v2/event-types/delete-a-custom-booking-field.md): <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>

##### Webhooks

- [Create a webhook](https://cal.com/docs/api-reference/v2/event-types-webhooks/create-a-webhook.md): If accessed using an OAuth access token, the `EVENT_TYPE_WRITE` scope is required.
- [Get all webhooks](https://cal.com/docs/api-reference/v2/event-types-webhooks/get-all-webhooks.md): If accessed using an OAuth access token, the `EVENT_TYPE_READ` scope is required.
- [Delete all webhooks](https://cal.com/docs/api-reference/v2/event-types-webhooks/delete-all-webhooks.md): If accessed using an OAuth access token, the `EVENT_TYPE_WRITE` scope is required.
- [Update a webhook](https://cal.com/docs/api-reference/v2/event-types-webhooks/update-a-webhook.md): If accessed using an OAuth access token, the `EVENT_TYPE_WRITE` scope is required.
- [Get a webhook](https://cal.com/docs/api-reference/v2/event-types-webhooks/get-a-webhook.md): If accessed using an OAuth access token, the `EVENT_TYPE_READ` scope is required.
- [Delete a webhook](https://cal.com/docs/api-reference/v2/event-types-webhooks/delete-a-webhook.md): If accessed using an OAuth access token, the `EVENT_TYPE_WRITE` scope is required.

#### Events

- [List Events](https://cal.com/docs/api-reference/v2/events/list-events.md): Returns the Events the authenticated user hosts: Events they own, plus Events they have accepted a co-host invitation to. A co-hosted Event may be owned by a team, so a team-owned Event can appear here — but team-owned Events the user neither hosts nor co-hosts are not returned by this endpoint. Eve…
- [Get an Event](https://cal.com/docs/api-reference/v2/events/get-an-event.md): Returns one Event by UUID. The authenticated user must be its owner, one of its hosts, an accepted co-host, or a member of the owning team with permission to read its event types. Events are fixed-date RSVP pages served at cal.com/{slug}; they are not event types (bookable meeting templates) or cale…

#### Event Types Private Links

- [Create a private link for an event type](https://cal.com/docs/api-reference/v2/event-types-private-links/create-a-private-link-for-an-event-type.md): If accessed using an OAuth access token, the `EVENT_TYPE_WRITE` scope is required.
- [Get all private links for an event type](https://cal.com/docs/api-reference/v2/event-types-private-links/get-all-private-links-for-an-event-type.md): If accessed using an OAuth access token, the `EVENT_TYPE_READ` scope is required.
- [Update a private link for an event type](https://cal.com/docs/api-reference/v2/event-types-private-links/update-a-private-link-for-an-event-type.md): If accessed using an OAuth access token, the `EVENT_TYPE_WRITE` scope is required.
- [Delete a private link for an event type](https://cal.com/docs/api-reference/v2/event-types-private-links/delete-a-private-link-for-an-event-type.md): If accessed using an OAuth access token, the `EVENT_TYPE_WRITE` scope is required.

#### Routing Forms

- [Calculate slots based on routing form response](https://cal.com/docs/api-reference/v2/routing-forms/calculate-slots-based-on-routing-form-response.md): It will not actually save the response just return the routed event type and slots when it can be booked.

#### Workflows

- [Create a workflow](https://cal.com/docs/api-reference/v2/workflows/create-a-workflow.md): Create an event-type workflow owned by the authenticated user. Not available to third-party OAuth access tokens.
- [Get your workflows](https://cal.com/docs/api-reference/v2/workflows/get-your-workflows.md): Get the event-type workflows owned by the authenticated user. Routing form workflows are not returned. Not available to third-party OAuth access tokens.
- [Get your workflow](https://cal.com/docs/api-reference/v2/workflows/get-your-workflow.md): Get an event-type workflow owned by the authenticated user. Routing form workflows are not addressable through this endpoint. Not available to third-party OAuth access tokens.
- [Update your workflow](https://cal.com/docs/api-reference/v2/workflows/update-your-workflow.md): Update an event-type workflow owned by the authenticated user. Not available to third-party OAuth access tokens.
- [Delete your workflow](https://cal.com/docs/api-reference/v2/workflows/delete-your-workflow.md): Delete an event-type workflow owned by the authenticated user. Not available to third-party OAuth access tokens.

#### Webhooks

- [Create a webhook](https://cal.com/docs/api-reference/v2/webhooks/create-a-webhook.md): If accessed using an OAuth access token, the `WEBHOOK_WRITE` scope is required.
- [Get all webhooks](https://cal.com/docs/api-reference/v2/webhooks/get-all-webhooks.md): Gets a paginated list of webhooks for the authenticated user. If accessed using an OAuth access token, the `WEBHOOK_READ` scope is required.
- [Update a webhook](https://cal.com/docs/api-reference/v2/webhooks/update-a-webhook.md): If accessed using an OAuth access token, the `WEBHOOK_WRITE` scope is required.
- [Get a webhook](https://cal.com/docs/api-reference/v2/webhooks/get-a-webhook.md): If accessed using an OAuth access token, the `WEBHOOK_READ` scope is required.
- [Delete a webhook](https://cal.com/docs/api-reference/v2/webhooks/delete-a-webhook.md): If accessed using an OAuth access token, the `WEBHOOK_WRITE` scope is required.

#### Stripe

- [Get Stripe connect URL](https://cal.com/docs/api-reference/v2/stripe/get-stripe-connect-url.md)
- [Save Stripe credentials](https://cal.com/docs/api-reference/v2/stripe/save-stripe-credentials.md)
- [Check Stripe connection](https://cal.com/docs/api-reference/v2/stripe/check-stripe-connection.md)

### TEAMS

#### Teams

- [Create a team](https://cal.com/docs/api-reference/v2/teams/create-a-team.md): If accessed using an OAuth access token, the `TEAM_PROFILE_WRITE` scope is required.
- [Get teams](https://cal.com/docs/api-reference/v2/teams/get-teams.md): If accessed using an OAuth access token, the `TEAM_PROFILE_READ` scope is required.
- [Get a team](https://cal.com/docs/api-reference/v2/teams/get-a-team.md): If accessed using an OAuth access token, the `TEAM_PROFILE_READ` scope is required.
- [Update a team](https://cal.com/docs/api-reference/v2/teams/update-a-team.md): If accessed using an OAuth access token, the `TEAM_PROFILE_WRITE` scope is required.
- [Delete a team](https://cal.com/docs/api-reference/v2/teams/delete-a-team.md): If accessed using an OAuth access token, the `TEAM_PROFILE_WRITE` scope is required.
- [Get team bookings](https://cal.com/docs/api-reference/v2/teams-bookings/get-team-bookings.md): If accessed using an OAuth access token, the `TEAM_BOOKING_READ` scope is required.
- [Get all team member schedules](https://cal.com/docs/api-reference/v2/teams-schedules/get-all-team-member-schedules.md): If accessed using an OAuth access token, the `TEAM_SCHEDULE_READ` scope is required.

##### Event Types

- [Create a team event type](https://cal.com/docs/api-reference/v2/team-event-types/create-a-team-event-type.md): <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>
- [List team event types](https://cal.com/docs/api-reference/v2/team-event-types/list-team-event-types.md): <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>
- [Get a team event type](https://cal.com/docs/api-reference/v2/team-event-types/get-a-team-event-type.md): <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>
- [Update a team event type](https://cal.com/docs/api-reference/v2/team-event-types/update-a-team-event-type.md): <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>
- [Delete a team event type](https://cal.com/docs/api-reference/v2/team-event-types/delete-a-team-event-type.md): <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>
- [Create a phone call for a team event type](https://cal.com/docs/api-reference/v2/team-event-types/create-a-phone-call-for-a-team-event-type.md): <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>

###### Booking Fields

- [Get team booking fields](https://cal.com/docs/api-reference/v2/team-event-types/get-team-booking-fields.md): <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>
- [Replace team booking fields](https://cal.com/docs/api-reference/v2/team-event-types/replace-team-booking-fields.md): <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>
- [Add custom team booking fields](https://cal.com/docs/api-reference/v2/team-event-types/add-custom-team-booking-fields.md): <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>
- [Update team booking fields](https://cal.com/docs/api-reference/v2/team-event-types/update-team-booking-fields.md): <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>
- [Delete a custom team booking field](https://cal.com/docs/api-reference/v2/team-event-types/delete-a-custom-team-booking-field.md): <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>

###### Webhooks

- [Create a webhook for a team event type](https://cal.com/docs/api-reference/v2/teams-event-types-webhooks/create-a-webhook-for-a-team-event-type.md): If accessed using an OAuth access token, the `TEAM_EVENT_TYPE_WRITE` scope is required.
- [Get all webhooks for a team event type](https://cal.com/docs/api-reference/v2/teams-event-types-webhooks/get-all-webhooks-for-a-team-event-type.md): If accessed using an OAuth access token, the `TEAM_EVENT_TYPE_READ` scope is required.
- [Delete all webhooks for a team event type](https://cal.com/docs/api-reference/v2/teams-event-types-webhooks/delete-all-webhooks-for-a-team-event-type.md): If accessed using an OAuth access token, the `TEAM_EVENT_TYPE_WRITE` scope is required.
- [Update a webhook for a team event type](https://cal.com/docs/api-reference/v2/teams-event-types-webhooks/update-a-webhook-for-a-team-event-type.md): If accessed using an OAuth access token, the `TEAM_EVENT_TYPE_WRITE` scope is required.
- [Get a webhook for a team event type](https://cal.com/docs/api-reference/v2/teams-event-types-webhooks/get-a-webhook-for-a-team-event-type.md): If accessed using an OAuth access token, the `TEAM_EVENT_TYPE_READ` scope is required.
- [Delete a webhook for a team event type](https://cal.com/docs/api-reference/v2/teams-event-types-webhooks/delete-a-webhook-for-a-team-event-type.md): If accessed using an OAuth access token, the `TEAM_EVENT_TYPE_WRITE` scope is required.

##### Invite

- [Create team invite link](https://cal.com/docs/api-reference/v2/teams-invite/create-team-invite-link.md): If accessed using an OAuth access token, the `TEAM_MEMBERSHIP_WRITE` scope is required.

##### Memberships

- [Create a membership](https://cal.com/docs/api-reference/v2/teams-memberships/create-a-membership.md): If accessed using an OAuth access token, the `TEAM_MEMBERSHIP_WRITE` scope is required.
- [Get all memberships](https://cal.com/docs/api-reference/v2/teams-memberships/get-all-memberships.md): Retrieve team memberships with optional filtering by email addresses. Supports pagination. If accessed using an OAuth access token, the `TEAM_MEMBERSHIP_READ` scope is required.
- [Get a membership](https://cal.com/docs/api-reference/v2/teams-memberships/get-a-membership.md): If accessed using an OAuth access token, the `TEAM_MEMBERSHIP_READ` scope is required.
- [Update membership](https://cal.com/docs/api-reference/v2/teams-memberships/update-membership.md): If accessed using an OAuth access token, the `TEAM_MEMBERSHIP_WRITE` scope is required.
- [Delete a membership](https://cal.com/docs/api-reference/v2/teams-memberships/delete-a-membership.md): Required membership role: `team admin`. PBAC permission: `team.remove`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control. If accessed using an OAuth access token, the `TEAM_MEMBERSHIP_WRITE` scope is required.

##### Routing Forms

- [Create routing form response and get available slots](https://cal.com/docs/api-reference/v2/teams-routing-forms-responses/create-routing-form-response-and-get-available-slots.md): Only available for teams that are not part of an organization - for a team within an organization use the organization team endpoint instead. Required membership role: `team member`. PBAC permission: `routingForm.create`. Learn more about API access control at https://cal.com/docs/api-reference/v2/a…

##### Users / OOO

- [Get all out-of-office entries for a team member](https://cal.com/docs/api-reference/v2/teams-users-ooo/get-all-out-of-office-entries-for-a-team-member.md): If accessed using an OAuth access token, the `TEAM_SCHEDULE_READ` scope is required.
- [Create an out-of-office entry for a team member](https://cal.com/docs/api-reference/v2/teams-users-ooo/create-an-out-of-office-entry-for-a-team-member.md): If accessed using an OAuth access token, the `TEAM_SCHEDULE_WRITE` scope is required.
- [Update an out-of-office entry for a team member](https://cal.com/docs/api-reference/v2/teams-users-ooo/update-an-out-of-office-entry-for-a-team-member.md): If accessed using an OAuth access token, the `TEAM_SCHEDULE_WRITE` scope is required.
- [Delete an out-of-office entry for a team member](https://cal.com/docs/api-reference/v2/teams-users-ooo/delete-an-out-of-office-entry-for-a-team-member.md): If accessed using an OAuth access token, the `TEAM_SCHEDULE_WRITE` scope is required.

#### Teams Verified Resources

- [Request email verification code](https://cal.com/docs/api-reference/v2/teams-verified-resources/request-email-verification-code.md): Sends a verification code to the Email. If accessed using an OAuth access token, the `TEAM_VERIFIED_RESOURCES_WRITE` scope is required.
- [Request phone number verification code](https://cal.com/docs/api-reference/v2/teams-verified-resources/request-phone-number-verification-code.md): Sends a verification code to the phone number. If accessed using an OAuth access token, the `TEAM_VERIFIED_RESOURCES_WRITE` scope is required.
- [Verify an email for a team](https://cal.com/docs/api-reference/v2/teams-verified-resources/verify-an-email-for-a-team.md): Use code to verify an email. If accessed using an OAuth access token, the `TEAM_VERIFIED_RESOURCES_WRITE` scope is required.
- [Verify a phone number for an org team](https://cal.com/docs/api-reference/v2/teams-verified-resources/verify-a-phone-number-for-an-org-team.md): Use code to verify a phone number. If accessed using an OAuth access token, the `TEAM_VERIFIED_RESOURCES_WRITE` scope is required.
- [Get list of verified emails of a team](https://cal.com/docs/api-reference/v2/teams-verified-resources/get-list-of-verified-emails-of-a-team.md): If accessed using an OAuth access token, the `TEAM_VERIFIED_RESOURCES_READ` scope is required.
- [Get list of verified phone numbers of a team](https://cal.com/docs/api-reference/v2/teams-verified-resources/get-list-of-verified-phone-numbers-of-a-team.md): If accessed using an OAuth access token, the `TEAM_VERIFIED_RESOURCES_READ` scope is required.
- [Get verified email of a team by id](https://cal.com/docs/api-reference/v2/teams-verified-resources/get-verified-email-of-a-team-by-id.md): If accessed using an OAuth access token, the `TEAM_VERIFIED_RESOURCES_READ` scope is required.
- [Get verified phone number of a team by id](https://cal.com/docs/api-reference/v2/teams-verified-resources/get-verified-phone-number-of-a-team-by-id.md): If accessed using an OAuth access token, the `TEAM_VERIFIED_RESOURCES_READ` scope is required.

### AUTH & ACCESS

#### API Keys

- [Refresh API Key](https://cal.com/docs/api-reference/v2/api-keys/refresh-api-key.md): Generate a new API key and delete the current one. Provide API key to refresh as a Bearer token in the Authorization header (e.g. "Authorization: Bearer <apiKey>").

#### OAuth2

- [Get OAuth2 client](https://cal.com/docs/api-reference/v2/oauth2/get-oauth2-client.md): Returns the OAuth2 client information for the given client ID
- [Exchange authorization code or refresh token for tokens](https://cal.com/docs/api-reference/v2/oauth2/exchange-authorization-code-or-refresh-token-for-tokens.md): RFC 6749-compliant token endpoint. Pass client_id in the request body (Section 2.3.1). Use grant_type 'authorization_code' to exchange an auth code for tokens, or 'refresh_token' to refresh an access token. Accepts both application/x-www-form-urlencoded (standard per RFC 6749 Section 4.1.3) and appl…

#### Verified Resources

- [Request email verification code](https://cal.com/docs/api-reference/v2/verified-resources/request-email-verification-code.md): Sends a verification code to the email. If accessed using an OAuth access token, the `VERIFIED_RESOURCES_WRITE` scope is required.
- [Request phone number verification code](https://cal.com/docs/api-reference/v2/verified-resources/request-phone-number-verification-code.md): Sends a verification code to the phone number. If accessed using an OAuth access token, the `VERIFIED_RESOURCES_WRITE` scope is required.
- [Verify an email](https://cal.com/docs/api-reference/v2/verified-resources/verify-an-email.md): Use code to verify an email. If accessed using an OAuth access token, the `VERIFIED_RESOURCES_WRITE` scope is required.
- [Verify a phone number](https://cal.com/docs/api-reference/v2/verified-resources/verify-a-phone-number.md): Use code to verify a phone number. If accessed using an OAuth access token, the `VERIFIED_RESOURCES_WRITE` scope is required.
- [Get list of verified emails](https://cal.com/docs/api-reference/v2/verified-resources/get-list-of-verified-emails.md): If accessed using an OAuth access token, the `VERIFIED_RESOURCES_READ` scope is required.
- [Get list of verified phone numbers](https://cal.com/docs/api-reference/v2/verified-resources/get-list-of-verified-phone-numbers.md): If accessed using an OAuth access token, the `VERIFIED_RESOURCES_READ` scope is required.
- [Get verified email by id](https://cal.com/docs/api-reference/v2/verified-resources/get-verified-email-by-id.md): If accessed using an OAuth access token, the `VERIFIED_RESOURCES_READ` scope is required.
- [Get verified phone number by id](https://cal.com/docs/api-reference/v2/verified-resources/get-verified-phone-number-by-id.md): If accessed using an OAuth access token, the `VERIFIED_RESOURCES_READ` scope is required.

### DEPRECATED

#### Managed Orgs

- [Create an organization within an organization](https://cal.com/docs/api-reference/v2/managed-orgs/create-an-organization-within-an-organization.md): For platform, the plan must be 'SCALE' or higher to access this endpoint. Required membership role: `org admin`. PBAC permission: `organization.create`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control
- [Get all organizations within an organization](https://cal.com/docs/api-reference/v2/managed-orgs/get-all-organizations-within-an-organization.md): For platform, the plan must be 'SCALE' or higher to access this endpoint. Required membership role: `org admin`. PBAC permission: `organization.readManagedOrganizations`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control
- [Get an organization within an organization](https://cal.com/docs/api-reference/v2/managed-orgs/get-an-organization-within-an-organization.md): For platform, the plan must be 'SCALE' or higher to access this endpoint. Required membership role: `org admin`. PBAC permission: `organization.readManagedOrganizations`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control
- [Update an organization within an organization](https://cal.com/docs/api-reference/v2/managed-orgs/update-an-organization-within-an-organization.md): For platform, the plan must be 'SCALE' or higher to access this endpoint. Required membership role: `org admin`. PBAC permission: `organization.update`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control
- [Delete an organization within an organization](https://cal.com/docs/api-reference/v2/managed-orgs/delete-an-organization-within-an-organization.md): For platform, the plan must be 'SCALE' or higher to access this endpoint. Required membership role: `org admin`. PBAC permission: `organization.delete`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control

#### Platform OAuth Clients

- [Create an OAuth client](https://cal.com/docs/api-reference/v2/deprecated:-platform-oauth-clients/create-an-oauth-client.md): <Warning>These endpoints are deprecated and will be removed in the future.</Warning>
- [Get all OAuth clients](https://cal.com/docs/api-reference/v2/deprecated:-platform-oauth-clients/get-all-oauth-clients.md): <Warning>These endpoints are deprecated and will be removed in the future.</Warning>
- [Get an OAuth client](https://cal.com/docs/api-reference/v2/deprecated:-platform-oauth-clients/get-an-oauth-client.md): <Warning>These endpoints are deprecated and will be removed in the future.</Warning>
- [Update an OAuth client](https://cal.com/docs/api-reference/v2/deprecated:-platform-oauth-clients/update-an-oauth-client.md): <Warning>These endpoints are deprecated and will be removed in the future.</Warning>
- [Delete an OAuth client](https://cal.com/docs/api-reference/v2/deprecated:-platform-oauth-clients/delete-an-oauth-client.md): <Warning>These endpoints are deprecated and will be removed in the future.</Warning>

#### Platform / Managed Users

- [Get all managed users](https://cal.com/docs/api-reference/v2/deprecated:-platform-managed-users/get-all-managed-users.md): <Warning>These endpoints are deprecated and will be removed in the future.</Warning>
- [Create a managed user](https://cal.com/docs/api-reference/v2/deprecated:-platform-managed-users/create-a-managed-user.md): <Warning>These endpoints are deprecated and will be removed in the future.</Warning>
- [Get a managed user](https://cal.com/docs/api-reference/v2/deprecated:-platform-managed-users/get-a-managed-user.md): <Warning>These endpoints are deprecated and will be removed in the future.</Warning>
- [Update a managed user](https://cal.com/docs/api-reference/v2/deprecated:-platform-managed-users/update-a-managed-user.md): <Warning>These endpoints are deprecated and will be removed in the future.</Warning>
- [Delete a managed user](https://cal.com/docs/api-reference/v2/deprecated:-platform-managed-users/delete-a-managed-user.md): <Warning>These endpoints are deprecated and will be removed in the future.</Warning>
- [Force refresh tokens](https://cal.com/docs/api-reference/v2/deprecated:-platform-managed-users/force-refresh-tokens.md): <Warning>These endpoints are deprecated and will be removed in the future.</Warning> If you have lost managed user access or refresh token, then you can get new ones by using OAuth credentials. Access token is valid for 60 minutes and refresh token for 1 year. Make sure to store them in your databas…
- [Refresh managed user tokens](https://cal.com/docs/api-reference/v2/deprecated:-platform-managed-users/refresh-managed-user-tokens.md): <Warning>These endpoints are deprecated and will be removed in the future.</Warning> If managed user access token is expired then get a new one using this endpoint - it will also refresh the refresh token, because we use     "refresh token rotation" mechanism. Access token is valid for 60 minutes an…

#### Platform / Webhooks

- [Create a webhook](https://cal.com/docs/api-reference/v2/deprecated:-platform-webhooks/create-a-webhook.md): <Warning>These endpoints are deprecated and will be removed in the future.</Warning>
- [Get all webhooks](https://cal.com/docs/api-reference/v2/deprecated:-platform-webhooks/get-all-webhooks.md): <Warning>These endpoints are deprecated and will be removed in the future.</Warning>
- [Delete all webhooks](https://cal.com/docs/api-reference/v2/deprecated:-platform-webhooks/delete-all-webhooks.md): <Warning>These endpoints are deprecated and will be removed in the future.</Warning>
- [Update a webhook](https://cal.com/docs/api-reference/v2/deprecated:-platform-webhooks/update-a-webhook.md): <Warning>These endpoints are deprecated and will be removed in the future.</Warning>
- [Get a webhook](https://cal.com/docs/api-reference/v2/deprecated:-platform-webhooks/get-a-webhook.md): <Warning>These endpoints are deprecated and will be removed in the future.</Warning>
- [Delete a webhook](https://cal.com/docs/api-reference/v2/deprecated:-platform-webhooks/delete-a-webhook.md): <Warning>These endpoints are deprecated and will be removed in the future.</Warning>

## OpenAPI Specs

- [openapi](/docs/api-reference/v2/openapi.json)
