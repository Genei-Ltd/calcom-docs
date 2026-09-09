> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Webhooks

Webhooks offer a great way to automate the flow with other apps when invitees schedule, cancel or reschedule events, or when a meeting starts or ends.

<iframe style={{ width:"100%",maxWidth:"560px" }} height="315" src="https://www.youtube.com/embed/Yy9me5E09LA?si=_2Mz-CKL2ajsFivd" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

The webhook subscription allows you to listen to specific trigger events, such as when a booking has been scheduled, for example. You can always listen to the webhook by providing a custom subscriber URL with your own development work. However, if you wish to trigger automations without any development work, you can use the integration with Zapier which connects Cal.com to your apps.

<Note>
  Please note that the webhooks can be associated with user as well as individual event types, including team event types.
</Note>

### Creating a webhook subscription

To create a new webhook subscription, visit `/settings/developer/webhooks` and proceed to enter the following details:

<Steps>
  <Step title="Subscriber URL">
    This is the listener URL where the payload will be sent when an event trigger is activated.

    The subscriber URL must meet the following requirements:

    * **Cal.com SaaS**: Only HTTPS URLs are accepted. HTTP, private/internal IP addresses (e.g., `10.x.x.x`, `192.168.x.x`, `127.0.0.1`), and `localhost` are blocked.
    * **Self-hosted**: Both HTTP and HTTPS URLs are accepted, and private IP addresses are allowed for internal webhooks.
    * **All environments**: Cloud metadata endpoints (e.g., `169.254.169.254`) and non-HTTP protocols (e.g., `ftp://`, `file://`) are always blocked.

    If your subscriber URL does not meet these requirements, the webhook creation request will be rejected with an error.
  </Step>

  <Step title="Event triggers">
    You can choose which specific triggers to listen to. Currently available triggers include:

    * `Booking Cancelled`
    * `Booking Created`
    * `Booking Rescheduled`
    * `Booking Rejected`
    * `Booking Requested`
    * `Booking Payment Initiated`
    * `Booking Paid`
    * `Meeting Started`
    * `Recording Ready`
    * `Form Submitted`
    * `Meeting Ended`
    * `Instant Meeting Created`
    * `Instant Meeting Accepted`
    * `Booking No-show Updated`
    * `Booking Location Updated`
    * `Booking Reassigned`
    * `After Hosts Didn't Join Cal Video`
    * `After Guests Didn't Join Cal Video`
    * `Wrong Assignment Report`
    * `Delegation Credential Error`
    * `Delegation Credential Secret Rotated`
    * `Delegation Credential Secret Rotation Failed`
    * `Delegation Credential Rotation Required`
  </Step>

  <Step title="Secret">
    You can provide a secret key with this webhook to [verify it](/docs/docs/core-features/webhooks#verifying-the-authenticity-of-the-received-payload) on the subscriber URL when receiving a payload. This helps confirm whether the payload is authentic or has been tampered with. You can leave it blank if you don't wish to secure the webhook with a secret key.
  </Step>

  <Step title="Custom Payload">
    You have the option to [customize the payload](/docs/docs/core-features/webhooks#adding-a-custom-payload-template) that you receive when a subscribed event is triggered.
  </Step>
</Steps>

### Webhook payload reference

Most webhook payloads are wrapped in the following structure:

```json theme={null}
{
  "triggerEvent": "TRIGGER_NAME",
  "createdAt": "2024-01-01T00:00:00.000Z",
  "payload": { ... }
}
```

<Note>
  `MEETING_STARTED` and `MEETING_ENDED` are exceptions — they use a flat payload where booking fields are at the top level alongside `triggerEvent`, with no `payload` wrapper. See [meeting started and meeting ended webhooks](#meeting-started-and-meeting-ended-webhooks) for details.
</Note>

<Note>
  Webhook payloads are versioned. The version of the payload sent is included in the x-cal-webhook-version HTTP header.
  Example: x-cal-webhook-version: 2021-10-20
</Note>

<Note>
  For **seated event types**, the `attendees` array in webhook payloads contains only the attendee associated with the specific seat that triggered the webhook. For example, when a new seat is booked, the webhook includes only that seat's attendee — not all attendees across the entire booking. This applies to all booking-related triggers (`BOOKING_CREATED`, `BOOKING_CANCELLED`, `BOOKING_RESCHEDULED`, etc.).
</Note>

Select a version and trigger event to view the example payload:

<Tabs>
  <Tab title="2021-10-20" id="2021-10-20">
    <AccordionGroup>
      <Accordion title="BOOKING_CREATED">
        ```json theme={null}
        {
          "triggerEvent": "BOOKING_CREATED",
          "createdAt": "2024-01-01T00:00:00.000Z",
          "payload": {
            "bookerUrl": "https://app.example.com",
            "title": "Strategy Session between Organizer and Guest",
            "startTime": "2024-01-01T10:00:00Z",
            "endTime": "2024-01-01T10:15:00Z",
            "additionalNotes": "",
            "type": "standard-event-type",
            "description": "",
            "eventTypeId": 123,
            "hideCalendarNotes": false,
            "hideCalendarEventDetails": false,
            "hideOrganizerEmail": false,
            "schedulingType": null,
            "seatsPerTimeSlot": null,
            "seatsShowAttendees": true,
            "seatsShowAvailabilityCount": true,
            "customReplyToEmail": null,
            "disableRescheduling": false,
            "disableCancelling": false,
            "organizer": {
              "id": 1,
              "name": "Organizer Name",
              "email": "organizer@example.com",
              "username": "organizer-handle",
              "usernameInOrg": "organizer",
              "timeZone": "UTC",
              "language": {
                "locale": "en"
              },
              "timeFormat": "h:mma",
              "utcOffset": 0
            },
            "attendees": [
              {
                "email": "guest@example.com",
                "name": "Guest User",
                "firstName": "Guest",
                "lastName": "User",
                "timeZone": "UTC",
                "language": {
                  "locale": "en"
                },
                "utcOffset": 0
              },
              {
                "email": "additional-guest@example.com",
                "name": "Additional Guest",
                "firstName": "",
                "lastName": "",
                "timeZone": "UTC",
                "language": {
                  "locale": "en"
                },
                "utcOffset": 0
              }
            ],
            "customInputs": {},
            "responses": {
              "name": {
                "label": "your_name",
                "value": "Guest User",
                "isHidden": false
              },
              "email": {
                "label": "email_address",
                "value": "guest@example.com",
                "isHidden": false
              },
              "attendeePhoneNumber": {
                "label": "phone_number",
                "isHidden": true
              },
              "location": {
                "label": "location",
                "value": {
                  "optionValue": "",
                  "value": "integrations:video-provider"
                },
                "isHidden": false
              },
              "title": {
                "label": "what_is_this_meeting_about",
                "isHidden": true
              },
              "notes": {
                "label": "additional_notes",
                "isHidden": false
              },
              "guests": {
                "label": "additional_guests",
                "value": [
                  "additional-guest@example.com"
                ],
                "isHidden": false
              },
              "rescheduleReason": {
                "label": "reason_for_reschedule",
                "isHidden": false
              }
            },
            "userFieldsResponses": {},
            "location": "integrations:video-provider",
            "destinationCalendar": null,
            "iCalUID": "unique-identifier-string@example.com",
            "iCalSequence": 0,
            "requiresConfirmation": false,
            "oneTimePassword": null,
            "organizationId": 1,
            "hashedLink": null,
            "uid": "unique-booking-id",
            "conferenceData": {
              "createRequest": {
                "requestId": "00000000-0000-0000-0000-000000000000"
              }
            },
            "videoCallData": {
              "type": "video_provider",
              "id": "meeting-room-id",
              "password": "redacted_token",
              "url": "https://video.example.com/meeting-room-id"
            },
            "appsStatus": [
              {
                "appName": "video-app",
                "type": "video_provider",
                "success": 1,
                "failures": 0,
                "errors": []
              }
            ],
            "eventTitle": "Strategy Session",
            "eventDescription": "",
            "price": 0,
            "currency": "usd",
            "length": 15,
            "bookingId": 100,
            "metadata": {
              "videoCallUrl": "https://app.example.com/video/unique-booking-id"
            },
            "status": "ACCEPTED"
          }
        }
        ```
      </Accordion>

      <Accordion title="BOOKING_CANCELLED">
        ```json theme={null}
        {
          "triggerEvent": "BOOKING_CANCELLED",
          "createdAt": "2024-01-01T15:00:00.000Z",
          "payload": {
            "bookerUrl": "https://app.example.com",
            "title": "Strategy Session: Organizer & Guest",
            "length": 15,
            "type": "standard-event-type",
            "additionalNotes": "Standard meeting notes placeholder",
            "description": "Standard meeting notes placeholder",
            "customInputs": {},
            "eventTypeId": 100,
            "userFieldsResponses": {},
            "responses": {
              "name": {
                "label": "name",
                "value": "Guest User"
              },
              "email": {
                "label": "email",
                "value": "guest@example.com"
              },
              "notes": {
                "label": "notes",
                "value": "Standard meeting notes placeholder"
              },
              "guests": {
                "label": "guests",
                "value": [
                  "additional-guest@example.com"
                ]
              },
              "rescheduleReason": {
                "label": "rescheduleReason",
                "value": "Original slot no longer works."
              }
            },
            "startTime": "2024-01-04T10:00:00+00:00",
            "endTime": "2024-01-04T10:15:00+00:00",
            "organizer": {
              "id": 1,
              "username": "organizer-handle",
              "usernameInOrg": "organizer",
              "email": "organizer@example.com",
              "name": "Organizer Name",
              "timeZone": "UTC",
              "timeFormat": "h:mma",
              "language": {
                "locale": "en"
              },
              "utcOffset": 0
            },
            "attendees": [
              {
                "name": "Guest User",
                "email": "guest@example.com",
                "timeZone": "UTC",
                "phoneNumber": null,
                "language": {
                  "locale": "en"
                },
                "utcOffset": 0
              },
              {
                "name": "Additional Guest",
                "email": "additional-guest@example.com",
                "timeZone": "UTC",
                "phoneNumber": null,
                "language": {
                  "locale": "en"
                },
                "utcOffset": 0
              }
            ],
            "uid": "unique-booking-identifier",
            "bookingId": 200,
            "location": "integrations:video-provider",
            "destinationCalendar": [],
            "cancellationReason": "I am no longer able to attend this session.",
            "seatsPerTimeSlot": null,
            "seatsShowAttendees": false,
            "iCalUID": "unique-identifier@example.com",
            "iCalSequence": 2,
            "hideOrganizerEmail": false,
            "customReplyToEmail": null,
            "organizationId": 5,
            "eventTitle": "Strategy Session",
            "eventDescription": null,
            "requiresConfirmation": true,
            "price": null,
            "currency": "usd",
            "status": "CANCELLED",
            "requestReschedule": false
          }
        }
        ```
      </Accordion>

      <Accordion title="BOOKING_RESCHEDULED">
        ```json theme={null}
        {
          "triggerEvent": "BOOKING_RESCHEDULED",
          "createdAt": "2024-01-01T10:00:00.000Z",
          "payload": {
            "bookerUrl": "https://app.example.com",
            "title": "Strategy Session: Organizer & Guest",
            "startTime": "2024-01-10T14:30:00Z",
            "endTime": "2024-01-10T14:45:00Z",
            "additionalNotes": "Standard meeting notes placeholder",
            "type": "standard-event-type",
            "description": "Standard meeting notes placeholder",
            "eventTypeId": 100,
            "hideCalendarNotes": false,
            "hideCalendarEventDetails": false,
            "hideOrganizerEmail": false,
            "schedulingType": null,
            "seatsPerTimeSlot": null,
            "seatsShowAttendees": true,
            "seatsShowAvailabilityCount": true,
            "customReplyToEmail": null,
            "disableRescheduling": false,
            "disableCancelling": false,
            "organizer": {
              "id": 1,
              "name": "Organizer Name",
              "email": "organizer@example.com",
              "username": "organizer-handle",
              "usernameInOrg": "organizer",
              "timeZone": "UTC",
              "language": {
                "locale": "en"
              },
              "timeFormat": "h:mma",
              "utcOffset": 0
            },
            "attendees": [
              {
                "email": "guest@example.com",
                "name": "Guest User",
                "firstName": "Guest",
                "lastName": "User",
                "timeZone": "UTC",
                "language": {
                  "locale": "en"
                },
                "utcOffset": 0
              },
              {
                "email": "additional-guest@example.com",
                "name": "Additional Guest",
                "firstName": "",
                "lastName": "",
                "timeZone": "UTC",
                "language": {
                  "locale": "en"
                },
                "utcOffset": 0
              }
            ],
            "customInputs": {},
            "responses": {
              "name": {
                "label": "your_name",
                "value": "Guest User",
                "isHidden": false
              },
              "email": {
                "label": "email_address",
                "value": "guest@example.com",
                "isHidden": false
              },
              "attendeePhoneNumber": {
                "label": "phone_number",
                "isHidden": true
              },
              "location": {
                "label": "location",
                "value": {
                  "value": "integrations:video-provider",
                  "optionValue": ""
                },
                "isHidden": false
              },
              "title": {
                "label": "what_is_this_meeting_about",
                "isHidden": true
              },
              "notes": {
                "label": "additional_notes",
                "value": "Standard meeting notes placeholder",
                "isHidden": false
              },
              "guests": {
                "label": "additional_guests",
                "value": [
                  "additional-guest@example.com"
                ],
                "isHidden": false
              },
              "rescheduleReason": {
                "label": "reason_for_reschedule",
                "isHidden": false
              }
            },
            "userFieldsResponses": {},
            "location": "integrations:video-provider",
            "destinationCalendar": null,
            "iCalSequence": 1,
            "requiresConfirmation": false,
            "oneTimePassword": null,
            "organizationId": 1,
            "hashedLink": null,
            "uid": "new-booking-unique-id",
            "videoCallData": {
              "type": "video_provider",
              "id": "meeting-room-id",
              "password": "redacted_jwt_token",
              "url": "https://video.example.com/meeting-room-id"
            },
            "conferenceData": {
              "createRequest": {
                "requestId": "00000000-0000-0000-0000-000000000000"
              }
            },
            "appsStatus": [
              {
                "appName": "video-app",
                "type": "video_provider",
                "success": 1,
                "failures": 0,
                "errors": []
              }
            ],
            "eventTitle": "Strategy Session",
            "eventDescription": "",
            "price": 0,
            "currency": "usd",
            "length": 15,
            "bookingId": 201,
            "rescheduleId": 200,
            "rescheduleUid": "previous-booking-unique-id",
            "rescheduleStartTime": "2024-01-05T14:30:00Z",
            "rescheduleEndTime": "2024-01-05T14:45:00Z",
            "metadata": {
              "videoCallUrl": "https://app.example.com/video/new-booking-unique-id"
            },
            "status": "ACCEPTED"
          }
        }
        ```
      </Accordion>

      <Accordion title="BOOKING_REQUESTED">
        ```json theme={null}
        {
          "triggerEvent": "BOOKING_REQUESTED",
          "createdAt": "2024-01-01T12:00:00.000Z",
          "payload": {
            "bookerUrl": "https://app.example.com",
            "title": "Strategy Session: Organizer & Guest",
            "startTime": "2024-01-01T13:00:00Z",
            "endTime": "2024-01-01T13:15:00Z",
            "additionalNotes": "Standard meeting notes placeholder",
            "type": "standard-event-type",
            "description": "Standard meeting notes placeholder",
            "eventTypeId": 100,
            "hideCalendarNotes": false,
            "hideCalendarEventDetails": false,
            "hideOrganizerEmail": false,
            "schedulingType": null,
            "seatsPerTimeSlot": null,
            "seatsShowAttendees": true,
            "seatsShowAvailabilityCount": true,
            "customReplyToEmail": null,
            "disableRescheduling": false,
            "disableCancelling": false,
            "organizer": {
              "id": 1,
              "name": "Organizer Name",
              "email": "organizer@example.com",
              "username": "organizer-handle",
              "usernameInOrg": "organizer",
              "timeZone": "UTC",
              "language": {
                "locale": "en"
              },
              "timeFormat": "h:mma",
              "utcOffset": 0
            },
            "attendees": [
              {
                "email": "guest@example.com",
                "name": "Guest User",
                "firstName": "Guest",
                "lastName": "User",
                "timeZone": "UTC",
                "language": {
                  "locale": "en"
                },
                "utcOffset": 0
              },
              {
                "email": "additional-guest@example.com",
                "name": "Additional Guest",
                "firstName": "",
                "lastName": "",
                "timeZone": "UTC",
                "language": {
                  "locale": "en"
                },
                "utcOffset": 0
              }
            ],
            "customInputs": {},
            "responses": {
              "name": {
                "label": "your_name",
                "value": "Guest User",
                "isHidden": false
              },
              "email": {
                "label": "email_address",
                "value": "guest@example.com",
                "isHidden": false
              },
              "attendeePhoneNumber": {
                "label": "phone_number",
                "isHidden": true
              },
              "location": {
                "label": "location",
                "value": {
                  "value": "integrations:video-provider",
                  "optionValue": ""
                },
                "isHidden": false
              },
              "title": {
                "label": "what_is_this_meeting_about",
                "isHidden": true
              },
              "notes": {
                "label": "additional_notes",
                "value": "Standard meeting notes placeholder",
                "isHidden": false
              },
              "guests": {
                "label": "additional_guests",
                "value": [
                  "additional-guest@example.com"
                ],
                "isHidden": false
              },
              "rescheduleReason": {
                "label": "reason_for_reschedule",
                "isHidden": false
              }
            },
            "userFieldsResponses": {},
            "location": "integrations:video-provider",
            "destinationCalendar": null,
            "iCalUID": "unique-booking-id@example.com",
            "iCalSequence": 0,
            "requiresConfirmation": true,
            "oneTimePassword": "00000000-0000-0000-0000-000000000000",
            "organizationId": 1,
            "hashedLink": null,
            "uid": "unique-booking-id",
            "eventTitle": "Strategy Session",
            "eventDescription": "",
            "price": 0,
            "currency": "usd",
            "length": 15,
            "bookingId": 200,
            "metadata": {},
            "status": "PENDING"
          }
        }
        ```
      </Accordion>

      <Accordion title="BOOKING_REJECTED">
        ```json theme={null}
        {
          "triggerEvent": "BOOKING_REJECTED",
          "createdAt": "2024-01-01T14:00:00.000Z",
          "payload": {
            "type": "standard-event-type",
            "title": "Strategy Session: Organizer & Guest",
            "description": "Standard meeting notes placeholder",
            "bookerUrl": "https://app.example.com",
            "userFieldsResponses": {},
            "responses": {
              "name": {
                "label": "name",
                "value": "Guest User"
              },
              "email": {
                "label": "email",
                "value": "guest@example.com"
              },
              "notes": {
                "label": "notes",
                "value": "Standard meeting notes placeholder"
              },
              "guests": {
                "label": "guests",
                "value": [
                  "additional-guest@example.com"
                ]
              }
            },
            "customInputs": {},
            "startTime": "2024-01-01T15:00:00.000Z",
            "endTime": "2024-01-01T15:15:00.000Z",
            "organizer": {
              "id": 1,
              "email": "organizer@example.com",
              "name": "Organizer Name",
              "username": "organizer-handle",
              "usernameInOrg": "organizer",
              "timeZone": "UTC",
              "timeFormat": "h:mma",
              "language": {
                "locale": "en"
              },
              "utcOffset": 0
            },
            "attendees": [
              {
                "name": "Guest User",
                "email": "guest@example.com",
                "timeZone": "UTC",
                "phoneNumber": null,
                "language": {
                  "locale": "en"
                },
                "utcOffset": 0
              },
              {
                "name": "Additional Guest",
                "email": "additional-guest@example.com",
                "timeZone": "UTC",
                "phoneNumber": null,
                "language": {
                  "locale": "en"
                },
                "utcOffset": 0
              }
            ],
            "location": "integrations:video-provider",
            "uid": "unique-booking-identifier",
            "destinationCalendar": [],
            "requiresConfirmation": true,
            "hideOrganizerEmail": false,
            "hideCalendarNotes": false,
            "hideCalendarEventDetails": false,
            "eventTypeId": 100,
            "customReplyToEmail": null,
            "organizationId": 5,
            "additionalNotes": "Standard meeting notes placeholder",
            "rejectionReason": "The organizer is no longer available at this time.",
            "eventTitle": "Strategy Session",
            "eventDescription": "",
            "price": 0,
            "currency": "usd",
            "length": 15,
            "bookingId": 200,
            "status": "REJECTED"
          }
        }
        ```
      </Accordion>

      <Accordion title="BOOKING_PAID">
        ```json theme={null}
        {
          "triggerEvent": "BOOKING_PAID",
          "createdAt": "2024-01-01T12:00:00.000Z",
          "payload": {
            "type": "Consultation Session",
            "title": "Consultation Session: Organizer & Guest",
            "description": "",
            "additionalNotes": "",
            "customInputs": {},
            "startTime": "2024-01-02T10:00:00.000Z",
            "endTime": "2024-01-02T10:30:00.000Z",
            "organizer": {
              "id": 1,
              "name": "Organizer Name",
              "email": "organizer@example.com",
              "username": "organizer-handle",
              "timeZone": "UTC",
              "language": { "locale": "en" },
              "timeFormat": 12
            },
            "attendees": [
              {
                "name": "Guest User",
                "email": "guest@example.com",
                "timeZone": "UTC",
                "language": { "locale": "en" }
              }
            ],
            "location": "integrations:video-provider",
            "destinationCalendar": null,
            "hideCalendarNotes": false,
            "requiresConfirmation": true,
            "eventTypeId": 50,
            "seatsShowAttendees": true,
            "seatsShowAvailabilityCount": true,
            "schedulingType": null,
            "iCalUID": "unique-ical-uid@example.com",
            "iCalSequence": 0,
            "uid": "unique-booking-uid",
            "bookingId": 100,
            "eventTitle": "Consultation Session",
            "eventDescription": "",
            "price": 1000,
            "currency": "USD",
            "length": 30,
            "paymentId": 500,
            "metadata": {
              "identifier": "platform.name",
              "bookingId": 100,
              "eventTypeId": 50,
              "bookerEmail": "guest@example.com",
              "eventTitle": "Consultation Session",
              "externalId": "pi_0000000000000000"
            },
            "status": "ACCEPTED"
          }
        }
        ```
      </Accordion>

      <Accordion title="BOOKING_PAYMENT_INITIATED">
        ```json theme={null}
        {
          "triggerEvent": "BOOKING_PAYMENT_INITIATED",
          "createdAt": "2024-01-01T12:00:00.000Z",
          "payload": {
            "type": "Consultation Session",
            "title": "Consultation Session: Organizer & Guest",
            "description": "",
            "additionalNotes": "",
            "customInputs": {},
            "startTime": "2024-01-02T10:00:00.000Z",
            "endTime": "2024-01-02T10:30:00.000Z",
            "organizer": {
              "id": 1,
              "name": "Organizer Name",
              "email": "organizer@example.com",
              "username": "organizer-handle",
              "timeZone": "UTC",
              "language": { "locale": "en" },
              "timeFormat": 12
            },
            "attendees": [
              {
                "name": "Guest User",
                "email": "guest@example.com",
                "timeZone": "UTC",
                "language": { "locale": "en" }
              }
            ],
            "location": "integrations:video-provider",
            "destinationCalendar": null,
            "hideCalendarNotes": false,
            "requiresConfirmation": false,
            "eventTypeId": 50,
            "seatsShowAttendees": true,
            "seatsShowAvailabilityCount": true,
            "schedulingType": null,
            "iCalUID": "unique-ical-uid@example.com",
            "iCalSequence": 0,
            "uid": "unique-booking-uid",
            "bookingId": 100,
            
            "eventTitle": "Consultation Session",
            "eventDescription": "",
            "requiresConfirmation": false,
            "price": 1000,
            "currency": "USD",
            "length": 30,
            
            "paymentId": 500,
            
            "status": "ACCEPTED",
            "metadata": {}
          }
        }
        ```
      </Accordion>

      <Accordion title="BOOKING_NO_SHOW_UPDATED">
        ```json theme={null}
        {
          "triggerEvent": "BOOKING_NO_SHOW_UPDATED",
          "createdAt": "2024-01-01T12:00:00.000Z",
          "payload": {
            "message": "guest@example.com unmarked as no-show",
            "attendees": [
              {
                "email": "guest@example.com",
                "noShow": false
              }
            ],
            "bookingUid": "unique-booking-identifier",
            "bookingId": 100
          }
        }
        ```
      </Accordion>

      <Accordion title="BOOKING_LOCATION_UPDATED">
        Fires when the location of an existing booking is changed. The payload mirrors the standard booking payload, with one addition: `previousLocation` holds the location before the change and existing `location` holds the new location.

        ```json theme={null}
        {
          "triggerEvent": "BOOKING_LOCATION_UPDATED",
          "createdAt": "2024-01-01T10:00:00.000Z",
          "payload": {
            "bookerUrl": "https://app.example.com",
            "title": "Strategy Session between Organizer and Guest",
            "startTime": "2024-01-01T10:00:00Z",
            "endTime": "2024-01-01T10:15:00Z",
            "additionalNotes": "",
            "type": "standard-event-type",
            "description": "",
            "eventTypeId": 123,
            "hideCalendarNotes": false,
            "hideCalendarEventDetails": false,
            "hideOrganizerEmail": false,
            "schedulingType": null,
            "seatsPerTimeSlot": null,
            "seatsShowAttendees": true,
            "seatsShowAvailabilityCount": true,
            "customReplyToEmail": null,
            "organizer": {
              "id": 1,
              "name": "Organizer Name",
              "email": "organizer@example.com",
              "username": "organizer-handle",
              "usernameInOrg": "organizer",
              "timeZone": "UTC",
              "language": {
                "locale": "en"
              },
              "timeFormat": "h:mma",
              "utcOffset": 0
            },
            "attendees": [
              {
                "email": "guest@example.com",
                "name": "Guest User",
                "firstName": "Guest",
                "lastName": "User",
                "timeZone": "UTC",
                "language": {
                  "locale": "en"
                },
                "utcOffset": 0
              }
            ],
            "customInputs": {},
            "responses": {
              "name": {
                "label": "your_name",
                "value": "Guest User",
                "isHidden": false
              },
              "email": {
                "label": "email_address",
                "value": "guest@example.com",
                "isHidden": false
              },
              "location": {
                "label": "location",
                "value": {
                  "optionValue": "",
                  "value": "https://app.example.com/video/unique-booking-id"
                },
                "isHidden": false
              }
            },
            "userFieldsResponses": {},
            "location": "https://app.example.com/video/unique-booking-id",
            "previousLocation": "https://meet.google.com/abc-defg-hij",
            "destinationCalendar": null,
            "iCalUID": "unique-identifier-string@example.com",
            "iCalSequence": 1,
            "requiresConfirmation": false,
            "organizationId": 1,
            "uid": "unique-booking-id",
            "eventTitle": "Strategy Session",
            "eventDescription": "",
            "price": 0,
            "currency": "usd",
            "length": 15,
            "bookingId": 100,
            "metadata": {
              "videoCallUrl": "https://app.example.com/video/unique-booking-id"
            },
            "status": "ACCEPTED"
          }
        }
        ```
      </Accordion>

      <Accordion title="BOOKING_REASSIGNED">
        Fires when a round-robin booking's host is reassigned (automatic or manual). The payload mirrors the standard booking payload, with two additions: `addedHostUserIds` lists the user IDs of the host(s) newly assigned to the booking and `removedHostUserIds` lists the user IDs of the host(s) removed. `organizer` reflects the new host. Both are IDs only — resolve them via the Cal.com API if you need host names or emails.

        ```json theme={null}
        {
          "triggerEvent": "BOOKING_REASSIGNED",
          "createdAt": "2024-01-01T10:00:00.000Z",
          "payload": {
            "bookerUrl": "https://app.example.com",
            "title": "Strategy Session between Organizer and Guest",
            "startTime": "2024-01-01T10:00:00Z",
            "endTime": "2024-01-01T10:15:00Z",
            "type": "standard-event-type",
            "description": "",
            "eventTypeId": 123,
            "organizer": {
              "id": 2,
              "name": "New Host",
              "email": "new-host@example.com",
              "username": "new-host",
              "timeZone": "UTC",
              "language": {
                "locale": "en"
              },
              "timeFormat": "h:mma",
              "utcOffset": 0
            },
            "attendees": [
              {
                "email": "guest@example.com",
                "name": "Guest User",
                "firstName": "Guest",
                "lastName": "User",
                "timeZone": "UTC",
                "language": {
                  "locale": "en"
                },
                "utcOffset": 0
              }
            ],
            "responses": {
              "name": {
                "label": "your_name",
                "value": "Guest User",
                "isHidden": false
              },
              "email": {
                "label": "email_address",
                "value": "guest@example.com",
                "isHidden": false
              }
            },
            "location": "https://app.example.com/video/unique-booking-id",
            "destinationCalendar": null,
            "iCalUID": "unique-identifier-string@example.com",
            "iCalSequence": 1,
            "uid": "unique-booking-id",
            "eventTitle": "Strategy Session",
            "bookingId": 100,
            "status": "ACCEPTED",
            "addedHostUserIds": [2],
            "removedHostUserIds": [1]
          }
        }
        ```
      </Accordion>

      <Accordion title="MEETING_STARTED">
        Unlike other events, `MEETING_STARTED` uses a flat payload structure — booking fields are at the top level, not nested inside a `payload` object. This webhook fires automatically at the booking's scheduled start time. See [meeting started and meeting ended webhooks](#meeting-started-and-meeting-ended-webhooks) for details.

        ```json theme={null}
        {
          "triggerEvent": "MEETING_STARTED",
          "id": 100,
          "uid": "unique-booking-identifier",
          "idempotencyKey": "00000000-0000-0000-0000-000000000000",
          "userId": 10,
          "userPrimaryEmail": "organizer@example.com",
          "eventTypeId": 50,
          "title": "Strategy Session: Organizer & Guest",
          "description": "",
          "customInputs": {},
          "responses": {
            "name": {
              "label": "your_name",
              "value": "Guest User",
              "isHidden": false
            },
            "email": {
              "label": "email_address",
              "value": "guest@example.com",
              "isHidden": false
            },
            "attendeePhoneNumber": {
              "label": "phone_number",
              "isHidden": true
            },
            "location": {
              "label": "location",
              "value": {
                "optionValue": "",
                "value": "integrations:video-provider"
              },
              "isHidden": false
            },
            "title": {
              "label": "what_is_this_meeting_about",
              "isHidden": true
            },
            "notes": {
              "label": "additional_notes",
              "isHidden": false
            },
            "guests": {
              "label": "additional_guests",
              "value": [
                "additional-guest@example.com"
              ],
              "isHidden": false
            },
            "rescheduleReason": {
              "label": "reason_for_reschedule",
              "isHidden": false
            }
          },
          "startTime": "2024-01-01T10:00:00.000Z",
          "endTime": "2024-01-01T10:15:00.000Z",
          "location": "integrations:video-provider",
          "createdAt": "2024-01-01T09:45:00.000Z",
          "updatedAt": "2024-01-01T09:45:00.000Z",
          "status": "ACCEPTED",
          "paid": false,
          "destinationCalendarId": null,
          "cancellationReason": null,
          "rejectionReason": null,
          "reassignReason": null,
          "reassignById": null,
          "dynamicEventSlugRef": null,
          "dynamicGroupSlugRef": null,
          "rescheduled": null,
          "fromReschedule": null,
          "recurringEventId": null,
          "smsReminderNumber": null,
          "scheduledJobs": [],
          "metadata": {},
          "isRecorded": false,
          "iCalUID": "unique-id@example.com",
          "iCalSequence": 0,
          "rating": null,
          "ratingFeedback": null,
          "noShowHost": false,
          "oneTimePassword": null,
          "cancelledBy": null,
          "rescheduledBy": null,
          "creationSource": "WEBAPP",
          "user": {
            "email": "organizer@example.com",
            "name": "Organizer Name",
            "timeZone": "UTC",
            "username": "organizer-handle"
          },
          "attendees": [
            {
              "id": 101,
              "email": "guest@example.com",
              "name": "Guest User",
              "timeZone": "UTC",
              "phoneNumber": null,
              "locale": "en",
              "bookingId": 100,
              "noShow": false
            },
            {
              "id": 102,
              "email": "additional-guest@example.com",
              "name": "Additional Guest",
              "timeZone": "UTC",
              "phoneNumber": null,
              "locale": "en",
              "bookingId": 100,
              "noShow": false
            }
          ],
          "payment": [],
          "references": [],
          "appsStatus": [
            {
              "appName": "video-app",
              "type": "video_provider",
              "success": 1,
              "failures": 0,
              "errors": []
            }
          ]
        }
        ```
      </Accordion>

      <Accordion title="MEETING_ENDED">
        Unlike other events, `MEETING_ENDED` uses a flat payload structure — booking fields are at the top level, not nested inside a `payload` object. This webhook fires automatically at the booking's scheduled end time. See [meeting started and meeting ended webhooks](#meeting-started-and-meeting-ended-webhooks) for details.

        ```json theme={null}
        {
          "triggerEvent": "MEETING_ENDED",
          "id": 100,
          "uid": "unique-booking-identifier",
          "idempotencyKey": "00000000-0000-0000-0000-000000000000",
          "userId": 10,
          "userPrimaryEmail": "organizer@example.com",
          "eventTypeId": 50,
          "title": "Strategy Session: Organizer & Guest",
          "description": "",
          "customInputs": {},
          "responses": {
            "name": {
              "label": "your_name",
              "value": "Guest User",
              "isHidden": false
            },
            "email": {
              "label": "email_address",
              "value": "guest@example.com",
              "isHidden": false
            },
            "attendeePhoneNumber": {
              "label": "phone_number",
              "isHidden": true
            },
            "location": {
              "label": "location",
              "value": {
                "optionValue": "",
                "value": "integrations:video-provider"
              },
              "isHidden": false
            },
            "title": {
              "label": "what_is_this_meeting_about",
              "isHidden": true
            },
            "notes": {
              "label": "additional_notes",
              "isHidden": false
            },
            "guests": {
              "label": "additional_guests",
              "value": [
                "additional-guest@example.com"
              ],
              "isHidden": false
            },
            "rescheduleReason": {
              "label": "reason_for_reschedule",
              "isHidden": false
            }
          },
          "startTime": "2024-01-01T10:00:00.000Z",
          "endTime": "2024-01-01T10:15:00.000Z",
          "location": "integrations:video-provider",
          "createdAt": "2024-01-01T09:45:00.000Z",
          "updatedAt": "2024-01-01T10:20:00.000Z",
          "status": "ACCEPTED",
          "paid": false,
          "destinationCalendarId": null,
          "cancellationReason": null,
          "rejectionReason": null,
          "reassignReason": null,
          "reassignById": null,
          "dynamicEventSlugRef": null,
          "dynamicGroupSlugRef": null,
          "rescheduled": null,
          "fromReschedule": null,
          "recurringEventId": null,
          "smsReminderNumber": null,
          "scheduledJobs": [],
          "metadata": {},
          "isRecorded": false,
          "iCalUID": "unique-id@example.com",
          "iCalSequence": 0,
          "rating": null,
          "ratingFeedback": null,
          "noShowHost": false,
          "oneTimePassword": null,
          "cancelledBy": null,
          "rescheduledBy": null,
          "creationSource": "WEBAPP",
          "user": {
            "email": "organizer@example.com",
            "name": "Organizer Name",
            "timeZone": "UTC",
            "username": "organizer-handle"
          },
          "attendees": [
            {
              "id": 101,
              "email": "guest@example.com",
              "name": "Guest User",
              "timeZone": "UTC",
              "phoneNumber": null,
              "locale": "en",
              "bookingId": 100,
              "noShow": false
            },
            {
              "id": 102,
              "email": "additional-guest@example.com",
              "name": "Additional Guest",
              "timeZone": "UTC",
              "phoneNumber": null,
              "locale": "en",
              "bookingId": 100,
              "noShow": false
            }
          ],
          "payment": [],
          "references": [],
          "appsStatus": [
            {
              "appName": "video-app",
              "type": "video_provider",
              "success": 1,
              "failures": 0,
              "errors": []
            }
          ]
        }
        ```
      </Accordion>

      <Accordion title="RECORDING_READY">
        ```json theme={null}
        {
          "triggerEvent": "RECORDING_READY",
          "createdAt": "2025-12-22T05:50:04.675Z",
          "payload": {
            "type": "meeting between User_A and User_B",
            "title": "meeting between User_A and User_B",
            "startTime": "2025-12-22T05:50:00.000Z",
            "endTime": "2025-12-22T06:00:00.000Z",
            "organizer": {
              "email": "organizer@example.com",
              "name": "Organizer Name",
              "timeZone": "Asia/Dubai",
              "language": {
                "locale": "en"
              },
              "utcOffset": 240
            },
            "attendees": [
              {
                "id": 00000000,
                "name": "Attendee Name",
                "email": "attendee@example.com",
                "timeZone": "Asia/Dubai",
                "language": {
                  "locale": "en"
                },
                "utcOffset": 240
              }
            ],
            "uid": "REDACTED_UID_STRING",
            "customReplyToEmail": null,
            "downloadLink": "https://app.cal.com/api/video/recording?token=REDACTED_TOKEN"
          }
        }
        ```
      </Accordion>

      <Accordion title="RECORDING_TRANSCRIPTION_GENERATED">
        ```json theme={null}
        {
          "triggerEvent": "RECORDING_TRANSCRIPTION_GENERATED",
          "createdAt": "2025-12-22T05:52:57.101Z",
          "payload": {
            "type": "meeting between User_A and User_B",
            "title": "meeting between User_A and User_B",
            "startTime": "2025-12-22T05:50:00.000Z",
            "endTime": "2025-12-22T06:00:00.000Z",
            "organizer": {
              "email": "organizer@example.com",
              "name": "Organizer Name",
              "timeZone": "Asia/Dubai",
              "language": {
                "locale": "en"
              },
              "utcOffset": 240
            },
            "attendees": [
              {
                "id": 00000000,
                "name": "Attendee Name",
                "email": "attendee@example.com",
                "timeZone": "Asia/Dubai",
                "language": {
                  "locale": "en"
                },
                "utcOffset": 240
              }
            ],
            "uid": "REDACTED_UID",
            "customReplyToEmail": null,
            "downloadLinks": {
              "transcription": [
                {
                  "format": "json",
                  "link": "https://s3.amazonaws.com/path/to/transcript.json?REDACTED_AWS_SIGNATURE"
                },
                {
                  "format": "srt",
                  "link": "https://s3.amazonaws.com/path/to/transcript.srt?REDACTED_AWS_SIGNATURE"
                },
                {
                  "format": "txt",
                  "link": "https://s3.amazonaws.com/path/to/transcript.txt?REDACTED_AWS_SIGNATURE"
                },
                {
                  "format": "vtt",
                  "link": "https://s3.amazonaws.com/path/to/transcript.vtt?REDACTED_AWS_SIGNATURE"
                }
              ],
              "recording": "https://app.cal.com/api/video/recording?token=REDACTED_TOKEN"
            }
          }
        }
        ```
      </Accordion>

      <Accordion title="INSTANT_MEETING">
        ```json theme={null}
        {
          "triggerEvent": "INSTANT_MEETING",
          "createdAt": "2024-01-01T12:00:00.000Z",
          "payload": {
            "triggerEvent": "INSTANT_MEETING",
            "uid": "unique-instant-meeting-id",
            "responses": {
              "name": "Guest User",
              "email": "guest@example.com",
              "notes": "Standard meeting notes placeholder",
              "guests": [
                "additional-guest@example.com"
              ]
            },
            "connectAndJoinUrl": "https://app.example.com/connect-and-join?token=REDACTED_ACCESS_TOKEN",
            "eventTypeId": 100,
            "eventTypeTitle": "Instant Meeting",
            "customInputs": {}
          }
        }
        ```
      </Accordion>

      <Accordion title="INSTANT_MEETING_ACCEPTED">
        Fired when a host accepts an instant meeting and becomes the organizer via the connect-and-join flow. This only triggers for the first host to accept — if the booking has already been accepted by another host, the webhook is not sent.

        ```json theme={null}
        {
          "triggerEvent": "INSTANT_MEETING_ACCEPTED",
          "createdAt": "2024-01-01T12:01:00.000Z",
          "payload": {
            "bookingId": 100,
            "bookingUid": "unique-instant-meeting-id",
            "eventTypeId": 100,
            "status": "ACCEPTED",
            "title": "Instant Meeting between Host and Guest",
            "startTime": "2024-01-01T12:00:00.000Z",
            "endTime": "2024-01-01T12:30:00.000Z",
            "organizer": {
              "id": 1,
              "name": "Host Name",
              "email": "host@example.com",
              "username": "host-handle",
              "timeZone": "UTC",
              "language": {
                "locale": "en"
              },
              "timeFormat": "h:mma",
              "utcOffset": 0
            },
            "attendees": [
              {
                "email": "guest@example.com",
                "name": "Guest User",
                "timeZone": "UTC",
                "language": {
                  "locale": "en"
                },
                "utcOffset": 0
              }
            ],
            "responses": {
              "name": {
                "label": "your_name",
                "value": "Guest User"
              },
              "email": {
                "label": "email_address",
                "value": "guest@example.com"
              }
            },
            "location": "integrations:video-provider",
            "metadata": {
              "videoCallUrl": "https://app.example.com/video/unique-instant-meeting-id"
            }
          }
        }
        ```
      </Accordion>

      <Accordion title="OOO_CREATED">
        `toUser` is the redirect/forwarding user and can be `null` if no redirect is set.

        ```json theme={null}
        {
          "triggerEvent": "OOO_CREATED",
          "createdAt": "2024-01-01T08:00:00.000Z",
          "payload": {
            "oooEntry": {
              "id": 100,
              "start": "2024-01-05T00:00:00+00:00",
              "end": "2024-01-07T23:59:59+00:00",
              "createdAt": "2024-01-01T08:00:00.000Z",
              "updatedAt": "2024-01-01T08:00:00.000Z",
              "notes": "Holiday Leave",
              "reason": {
                "emoji": "🌴",
                "reason": "ooo_reasons_vacation"
              },
              "reasonId": 5,
              "user": {
                "id": 1,
                "name": "Organizer Name",
                "username": "organizer-handle",
                "email": "organizer@example.com",
                "timeZone": "UTC"
              },
              "toUser": null,
              "uuid": "00000000-0000-0000-0000-000000000000"
            }
          }
        }
        ```
      </Accordion>

      <Accordion title="FORM_SUBMITTED">
        Root-level fields (e.g., `name`, `email`, `department`) are duplicated for backward compatibility. The `value` field in responses is deprecated; use `response` instead. For select/multiselect fields, `response` includes both the label and ID.

        ```json theme={null}
        {
          "What Language do you prefer": [
            "Placeholder Language"
          ],
          "Where are you from": [
            "Placeholder Location"
          ],
          "triggerEvent": "FORM_SUBMITTED",
          "createdAt": "2024-01-01T12:00:00.000Z",
          "payload": {
            "formId": "00000000-0000-0000-0000-000000000000",
            "formName": "Customer Intake Form",
            "teamId": null,
            "responses": {
              "What Language do you prefer": {
                "value": [
                  "Placeholder Language"
                ],
                "response": [
                  {
                    "label": "Placeholder Language",
                    "id": "00000000-0000-0000-0000-000000000000"
                  }
                ]
              },
              "Where are you from": {
                "value": [
                  "Placeholder Location"
                ],
                "response": [
                  {
                    "label": "Placeholder Location",
                    "id": "00000000-0000-0000-0000-000000000000"
                  }
                ]
              }
            }
          }
        }
        ```
      </Accordion>

      <Accordion title="FORM_SUBMITTED_NO_EVENT">
        Same structure as `FORM_SUBMITTED`. Triggered 15 minutes after form submission if no booking was made from the routing form.

        ```json theme={null}
        {
          "triggerEvent": "FORM_SUBMITTED_NO_EVENT",
          "createdAt": "2024-01-01T12:00:00.000Z",
          "payload": {
            "formId": "00000000-0000-0000-0000-000000000000",
            "formName": "Customer Inquiry Form",
            "teamId": null,
            "redirect": {
              "type": "customPageMessage",
              "value": "Thank you for your interest! Our team will review your details."
            },
            "responseId": 100,
            "responses": {
              "What Language do you prefer": {
                "value": [
                  "Placeholder Language"
                ],
                "response": [
                  {
                    "label": "Placeholder Language",
                    "id": "00000000-0000-0000-0000-000000000000"
                  }
                ]
              },
              "Where are you from": {
                "value": [
                  "Placeholder Location"
                ],
                "response": [
                  {
                    "label": "Placeholder Location",
                    "id": "00000000-0000-0000-0000-000000000000"
                  }
                ]
              }
            }
          }
        }
        ```
      </Accordion>

      <Accordion title="AFTER_HOSTS_CAL_VIDEO_NO_SHOW">
        ```json theme={null}
        {
          "triggerEvent": "AFTER_HOSTS_CAL_VIDEO_NO_SHOW",
          "createdAt": "2024-01-15T10:05:00.000Z",
          "payload": {
            "title": "30 Minute Meeting",
            "bookingId": 123,
            "bookingUid": "abc123-def456-ghi789",
            "startTime": "2024-01-15T10:00:00.000Z",
            "attendees": [
              {
                "id": 123,
                "email": "jane@example.com",
                "name": "Jane Smith",
                "timeZone": "Europe/London",
                "phoneNumber": null,
                "locale": "en",
                "bookingId": 123,
                "noShow": true
              }
            ],
            "endTime": "2024-01-15T10:30:00.000Z",
            "participants": [],
            "hostEmail": "john@example.com",
            "noShowHost": true,
            "eventType": {
              "id": 789,
              "teamId": null,
              "parentId": null,
              "calVideoSettings": null
            },
            "webhook": {
              "id": "webhook-abc123",
              "subscriberUrl": "https://example.com/webhook",
              "appId": null,
              "time": 5,
              "timeUnit": "MINUTE",
              "eventTriggers": [
                "AFTER_HOSTS_CAL_VIDEO_NO_SHOW",
                "AFTER_GUESTS_CAL_VIDEO_NO_SHOW"
              ],
              "payloadTemplate": null
            },
            "message": "Host with email john@example.com didn't join the call or didn't join before 2024-01-15 10:05:00 +00:00"
          }
        }
        ```
      </Accordion>

      <Accordion title="AFTER_GUESTS_CAL_VIDEO_NO_SHOW">
        ```json theme={null}
        {
          "triggerEvent": "AFTER_GUESTS_CAL_VIDEO_NO_SHOW",
          "createdAt": "2024-01-15T10:05:00.000Z",
          "payload": {
            "title": "30 Minute Meeting",
            "bookingId": 123,
            "bookingUid": "abc123-def456-ghi789",
            "startTime": "2024-01-15T10:00:00.000Z",
            "attendees": [
              {
                "id": 123,
                "email": "jane@example.com",
                "name": "Jane Smith",
                "timeZone": "Europe/London",
                "phoneNumber": null,
                "locale": "en",
                "bookingId": 123,
                "noShow": true
              }
            ],
            "endTime": "2024-01-15T10:30:00.000Z",
            "participants": [],
            "guests": [
              {
                "id": 123,
                "email": "jane@example.com",
                "name": "Jane Smith",
                "timeZone": "Europe/London",
                "phoneNumber": null,
                "locale": "en",
                "bookingId": 123,
                "noShow": true
              }
            ],
            "eventType": {
              "id": 789,
              "teamId": null,
              "parentId": null,
              "calVideoSettings": null
            },
            "webhook": {
              "id": "webhook-abc123",
              "subscriberUrl": "https://example.com/webhook",
              "appId": null,
              "time": 5,
              "timeUnit": "MINUTE",
              "eventTriggers": [
                "AFTER_HOSTS_CAL_VIDEO_NO_SHOW",
                "AFTER_GUESTS_CAL_VIDEO_NO_SHOW"
              ],
              "payloadTemplate": null
            },
            "message": "Guest didn't join the call or didn't join before 2024-01-15 10:05:00 +00:00"
          }
        }
        ```
      </Accordion>

      <Accordion title="DELEGATION_CREDENTIAL_ERROR">
        ```json theme={null}
        {
          "triggerEvent": "DELEGATION_CREDENTIAL_ERROR",
          "createdAt": "2024-01-01T12:00:00.000Z",
          "payload": {
            "error": {
              "type": "CalendarAppDelegationCredentialError",
              "message": "Invalid grant: account has been disabled or password changed"
            },
            "credential": {
              "id": 100,
              "type": "calendar_provider_type",
              "appId": "calendar-app-identifier",
              "delegationCredentialId": "00000000-0000-0000-0000-000000000000"
            },
            "user": {
              "id": 1,
              "email": "user@example.com",
              "organizationId": 500
            }
          }
        }
        ```
      </Accordion>

      <Accordion title="DELEGATION_CREDENTIAL_SECRET_ROTATED">
        Fired when a pending secret has been verified and promoted to active. It does not fire when a replacement secret is only minted and staged as pending.

        ```json theme={null}
        {
          "triggerEvent": "DELEGATION_CREDENTIAL_SECRET_ROTATED",
          "createdAt": "2024-01-01T12:00:00.000Z",
          "payload": {
            "delegationCredential": {
              "id": "00000000-0000-0000-0000-000000000000",
              "workspacePlatform": "office365",
              "domain": "example.com",
              "organizationId": 500,
              "secretExpiresAt": "2024-06-30T00:00:00.000Z"
            }
          }
        }
        ```
      </Accordion>

      <Accordion title="DELEGATION_CREDENTIAL_SECRET_ROTATION_FAILED">
        Fired only when an automatic secret mint or promotion has kept failing continuously for 48+ hours and the credential is marked as blocked (`secretRotationBlocked=true`). Transient failures before that 48-hour terminal window are retried automatically and do not fire a webhook. `error.code` is `SECRET_MINT_FAILED` when minting the replacement secret failed, or `SECRET_PROMOTION_FAILED` when a minted pending secret could not be verified with the workspace platform.

        ```json theme={null}
        {
          "triggerEvent": "DELEGATION_CREDENTIAL_SECRET_ROTATION_FAILED",
          "createdAt": "2024-01-01T12:00:00.000Z",
          "payload": {
            "delegationCredential": {
              "id": "00000000-0000-0000-0000-000000000000",
              "workspacePlatform": "office365",
              "domain": "example.com",
              "organizationId": 500,
              "secretExpiresAt": "2024-01-15T00:00:00.000Z"
            },
            "error": {
              "code": "SECRET_PROMOTION_FAILED",
              "message": "Failed to validate pending secret with workspace platform"
            }
          }
        }
        ```
      </Accordion>

      <Accordion title="DELEGATION_CREDENTIAL_ROTATION_REQUIRED">
        Fired for credentials that have opted out of automatic secret rotation (`optOutAutoSecretRotation=true`) whose active secret is approaching expiry — it is a manual-rotation reminder, not a signal that automatic rotation failed or was blocked. Terminal automatic-rotation failures (including an abandoned pending secret) fire `DELEGATION_CREDENTIAL_SECRET_ROTATION_FAILED` instead. Rotate the secret manually from the delegation credential settings when you receive this event.

        ```json theme={null}
        {
          "triggerEvent": "DELEGATION_CREDENTIAL_ROTATION_REQUIRED",
          "createdAt": "2024-01-01T12:00:00.000Z",
          "payload": {
            "delegationCredential": {
              "id": "00000000-0000-0000-0000-000000000000",
              "workspacePlatform": "office365",
              "domain": "example.com",
              "organizationId": 500,
              "secretExpiresAt": "2024-01-10T00:00:00.000Z"
            }
          }
        }
        ```
      </Accordion>

      <Accordion title="WRONG_ASSIGNMENT_REPORT">
        This webhook is triggered when a team member reports that a booking from a routing form was assigned to the wrong person. This is useful for tracking routing accuracy and improving CRM data quality.

        <Note>
          This webhook only fires for bookings that came through a routing form and have an assignment reason.
        </Note>

        ```json theme={null}
        {
          "triggerEvent": "WRONG_ASSIGNMENT_REPORT",
          "createdAt": "2025-01-15T10:30:00.000Z",
          "payload": {
            "booking": {
              "uid": "abc123def456",
              "id": 12345,
              "title": "Sales Call between Team and Lead",
              "startTime": "2025-01-15T14:00:00.000Z",
              "endTime": "2025-01-15T14:30:00.000Z",
              "status": "ACCEPTED",
              "eventType": {
                "id": 100,
                "title": "Sales Call",
                "slug": "sales-call",
                "teamId": 50
              }
            },
            "report": {
              "reportedBy": {
                "id": 1,
                "email": "reporter@example.com",
                "name": "Reporter Name"
              },
              "routingReason": "Routed based on company size: Enterprise",
              "guest": "lead@company.com",
              "host": {
                "email": "assigned-rep@example.com",
                "name": "Assigned Rep"
              },
              "correctAssignee": "correct-rep@example.com",
              "additionalNotes": "This lead should have been routed to the Enterprise team based on their company size."
            }
          }
        }
        ```
      </Accordion>
    </AccordionGroup>
  </Tab>

  <Tab title="2026-07-27" id="2026-07-27">
    <Note>
      Version `2026-07-27` extends `2021-10-20` — every payload shape and field above is
      unchanged. The only difference: `BOOKING_CREATED`, `BOOKING_RESCHEDULED`,
      `BOOKING_REASSIGNED`, `BOOKING_CANCELLED`, and `BOOKING_PAID` (when the payment accepted the booking) payloads
      additionally carry `attendeeIcsContent` and `organizerIcsContent` — pre-generated `.ics`
      calendar invite strings for a subscriber that sends its own confirmation/cancellation
      emails in place of Cal.com's. Use `attendeeIcsContent` for emails addressed to the attendees
      and `organizerIcsContent` for emails addressed to the organizer. Either field may be absent
      from a payload depending on the booking's calendar and privacy settings — treat both as
      optional.
    </Note>

    <AccordionGroup>
      <Accordion title="BOOKING_CREATED">
        ```json theme={null}
        {
          "triggerEvent": "BOOKING_CREATED",
          "createdAt": "2024-01-01T00:00:00.000Z",
          "payload": {
            "bookerUrl": "https://app.example.com",
            "title": "Strategy Session between Organizer and Guest",
            "startTime": "2024-01-01T10:00:00Z",
            "endTime": "2024-01-01T10:15:00Z",
            "organizer": {
              "id": 1,
              "name": "Organizer Name",
              "email": "organizer@example.com",
              "timeZone": "UTC"
            },
            "attendees": [
              {
                "email": "guest@example.com",
                "name": "Guest User",
                "timeZone": "UTC"
              }
            ],
            "uid": "unique-booking-id",
            "iCalUID": "unique-identifier-string@example.com",
            "iCalSequence": 0,
            "status": "ACCEPTED",
            "attendeeIcsContent": "BEGIN:VCALENDAR\nVERSION:2.0\nMETHOD:REQUEST\nBEGIN:VEVENT\nUID:unique-identifier-string@example.com\nSEQUENCE:0\nORGANIZER;CN=Organizer Name:mailto:organizer@example.com\nATTENDEE;CN=Guest User;ROLE=REQ-PARTICIPANT;PARTSTAT=ACCEPTED;RSVP=TRUE:mailto:guest@example.com\nEND:VEVENT\nEND:VCALENDAR",
            "organizerIcsContent": "BEGIN:VCALENDAR\nVERSION:2.0\nMETHOD:REQUEST\nBEGIN:VEVENT\nUID:unique-identifier-string@example.com\nSEQUENCE:0\nORGANIZER;CN=Organizer Name:mailto:organizer@example.com\nATTENDEE;CN=Organizer Name;ROLE=CHAIR;PARTSTAT=ACCEPTED;RSVP=FALSE:mailto:organizer@example.com\nEND:VEVENT\nEND:VCALENDAR"
          }
        }
        ```

        <Note>
          Payload fields other than `attendeeIcsContent`/`organizerIcsContent` are truncated
          above for brevity — see the `BOOKING_CREATED` example under the `2021-10-20` tab for
          the full field list, all of which are unchanged here.
        </Note>
      </Accordion>

      <Accordion title="BOOKING_RESCHEDULED">
        ```json theme={null}
        {
          "triggerEvent": "BOOKING_RESCHEDULED",
          "createdAt": "2024-01-01T10:00:00.000Z",
          "payload": {
            "title": "Strategy Session: Organizer & Guest",
            "startTime": "2024-01-10T14:30:00Z",
            "endTime": "2024-01-10T14:45:00Z",
            "organizer": {
              "id": 1,
              "name": "Organizer Name",
              "email": "organizer@example.com",
              "timeZone": "UTC"
            },
            "attendees": [
              {
                "email": "guest@example.com",
                "name": "Guest User",
                "timeZone": "UTC"
              }
            ],
            "uid": "new-booking-unique-id",
            "iCalUID": "unique-identifier-string@example.com",
            "iCalSequence": 1,
            "rescheduleUid": "previous-booking-unique-id",
            "rescheduleStartTime": "2024-01-05T14:30:00Z",
            "rescheduleEndTime": "2024-01-05T14:45:00Z",
            "status": "ACCEPTED",
            "attendeeIcsContent": "BEGIN:VCALENDAR\nVERSION:2.0\nMETHOD:REQUEST\nBEGIN:VEVENT\nUID:unique-identifier-string@example.com\nSEQUENCE:1\nORGANIZER;CN=Organizer Name:mailto:organizer@example.com\nATTENDEE;CN=Guest User;ROLE=REQ-PARTICIPANT;PARTSTAT=ACCEPTED;RSVP=TRUE:mailto:guest@example.com\nEND:VEVENT\nEND:VCALENDAR",
            "organizerIcsContent": "BEGIN:VCALENDAR\nVERSION:2.0\nMETHOD:REQUEST\nBEGIN:VEVENT\nUID:unique-identifier-string@example.com\nSEQUENCE:1\nORGANIZER;CN=Organizer Name:mailto:organizer@example.com\nATTENDEE;CN=Organizer Name;ROLE=CHAIR;PARTSTAT=ACCEPTED;RSVP=FALSE:mailto:organizer@example.com\nEND:VEVENT\nEND:VCALENDAR"
          }
        }
        ```

        <Note>
          Payload fields other than `attendeeIcsContent`/`organizerIcsContent` are truncated
          above for brevity — see the `BOOKING_RESCHEDULED` example under the `2021-10-20` tab for
          the full field list, all of which are unchanged here.
        </Note>
      </Accordion>

      <Accordion title="BOOKING_CANCELLED">
        ```json theme={null}
        {
          "triggerEvent": "BOOKING_CANCELLED",
          "createdAt": "2024-01-01T15:00:00.000Z",
          "payload": {
            "title": "Strategy Session: Organizer & Guest",
            "startTime": "2024-01-04T10:00:00+00:00",
            "endTime": "2024-01-04T10:15:00+00:00",
            "organizer": {
              "id": 1,
              "name": "Organizer Name",
              "email": "organizer@example.com",
              "timeZone": "UTC"
            },
            "attendees": [
              {
                "email": "guest@example.com",
                "name": "Guest User",
                "timeZone": "UTC"
              }
            ],
            "uid": "unique-booking-identifier",
            "bookingId": 200,
            "cancellationReason": "I am no longer able to attend this session.",
            "iCalUID": "unique-identifier@example.com",
            "iCalSequence": 2,
            "status": "CANCELLED",
            "attendeeIcsContent": "BEGIN:VCALENDAR\nVERSION:2.0\nMETHOD:CANCEL\nBEGIN:VEVENT\nUID:unique-identifier@example.com\nSEQUENCE:2\nSTATUS:CANCELLED\nORGANIZER;CN=Organizer Name:mailto:organizer@example.com\nATTENDEE;CN=Guest User;ROLE=REQ-PARTICIPANT;PARTSTAT=ACCEPTED;RSVP=TRUE:mailto:guest@example.com\nEND:VEVENT\nEND:VCALENDAR",
            "organizerIcsContent": "BEGIN:VCALENDAR\nVERSION:2.0\nMETHOD:CANCEL\nBEGIN:VEVENT\nUID:unique-identifier@example.com\nSEQUENCE:2\nSTATUS:CANCELLED\nORGANIZER;CN=Organizer Name:mailto:organizer@example.com\nATTENDEE;CN=Organizer Name;ROLE=CHAIR;PARTSTAT=ACCEPTED;RSVP=FALSE:mailto:organizer@example.com\nEND:VEVENT\nEND:VCALENDAR"
          }
        }
        ```

        <Note>
          Payload fields other than `attendeeIcsContent`/`organizerIcsContent` are truncated
          above for brevity — see the `BOOKING_CANCELLED` example under the `2021-10-20` tab for
          the full field list, all of which are unchanged here.
        </Note>
      </Accordion>

      <Accordion title="BOOKING_PAID">
        ```json theme={null}
        {
          "triggerEvent": "BOOKING_PAID",
          "createdAt": "2024-01-01T12:00:00.000Z",
          "payload": {
            "type": "Consultation Session",
            "title": "Consultation Session: Organizer & Guest",
            "startTime": "2024-01-02T10:00:00.000Z",
            "endTime": "2024-01-02T10:30:00.000Z",
            "organizer": {
              "id": 1,
              "name": "Organizer Name",
              "email": "organizer@example.com",
              "timeZone": "UTC"
            },
            "attendees": [
              {
                "name": "Guest User",
                "email": "guest@example.com",
                "timeZone": "UTC"
              }
            ],
            "iCalUID": "unique-ical-uid@example.com",
            "iCalSequence": 0,
            "uid": "unique-booking-uid",
            "bookingId": 100,
            "paymentId": 500,
            "metadata": {
              "identifier": "platform.name",
              "bookingId": 100,
              "eventTypeId": 50,
              "bookerEmail": "guest@example.com",
              "eventTitle": "Consultation Session",
              "externalId": "pi_0000000000000000"
            },
            "status": "ACCEPTED",
            "attendeeIcsContent": "BEGIN:VCALENDAR\nVERSION:2.0\nMETHOD:REQUEST\nBEGIN:VEVENT\nUID:unique-ical-uid@example.com\nSEQUENCE:0\nORGANIZER;CN=Organizer Name:mailto:organizer@example.com\nATTENDEE;CN=Guest User;ROLE=REQ-PARTICIPANT;PARTSTAT=ACCEPTED;RSVP=TRUE:mailto:guest@example.com\nEND:VEVENT\nEND:VCALENDAR",
            "organizerIcsContent": "BEGIN:VCALENDAR\nVERSION:2.0\nMETHOD:REQUEST\nBEGIN:VEVENT\nUID:unique-ical-uid@example.com\nSEQUENCE:0\nORGANIZER;CN=Organizer Name:mailto:organizer@example.com\nATTENDEE;CN=Organizer Name;ROLE=CHAIR;PARTSTAT=ACCEPTED;RSVP=FALSE:mailto:organizer@example.com\nEND:VEVENT\nEND:VCALENDAR"
          }
        }
        ```

        <Note>
          Payload fields other than `attendeeIcsContent`/`organizerIcsContent` are truncated
          above for brevity — see the `BOOKING_PAID` example under the `2021-10-20` tab for the
          full field list, all of which are unchanged here. These fields are present only when
          the payment resulted in an `ACCEPTED` booking; rejected or failed payments carry no ICS.
        </Note>
      </Accordion>
    </AccordionGroup>
  </Tab>
</Tabs>

### Booking No-show Updated webhook payload

This webhook is triggered when an attendee is manually marked or unmarked as no-show on the `/bookings/past` page.

**Example payload when marking an attendee as no-show:**

```json theme={null}
{
  "triggerEvent": "BOOKING_NO_SHOW_UPDATED",
  "createdAt": "2025-12-01T12:34:34.774Z",
  "payload": {
    "message": "test@example.com marked as no-show",
    "attendees": [
      {
        "email": "test@example.com",
        "noShow": true
      }
    ],
    "bookingUid": "5vQFqxDFMjdgKGMijqtqRw",
    "bookingId": 31
  }
}
```

**Example payload when unmarking an attendee as no-show:**

```json theme={null}
{
  "triggerEvent": "BOOKING_NO_SHOW_UPDATED",
  "createdAt": "2025-12-01T12:38:31.663Z",
  "payload": {
    "message": "test@example.com unmarked as no-show",
    "attendees": [
      {
        "email": "test@example.com",
        "noShow": false
      }
    ],
    "bookingUid": "5vQFqxDFMjdgKGMijqtqRw",
    "bookingId": 31
  }
}
```

### Cal Video No-Show Detection webhooks

These webhooks are triggered **automatically** when hosts or guests don't join a Cal Video meeting within the configured time after the booking starts. Unlike `BOOKING_NO_SHOW_UPDATED` which requires manual action, these are detected automatically by checking Cal Video participant data.

<Note>
  These webhooks only work for bookings that use Cal Video as the meeting location.
</Note>

**`Example payload when host didn't join (AFTER_HOSTS_CAL_VIDEO_NO_SHOW):`**

```json theme={null}
{
  "triggerEvent": "AFTER_HOSTS_CAL_VIDEO_NO_SHOW",
  "createdAt": "2025-12-01T15:23:30.320Z",
  "payload": {
    "title": "30min between Owner 1 and test",
    "bookingId": 32,
    "bookingUid": "qVyXscm1ryg2QoQ4K8uHLW",
    "startTime": "2025-12-02T04:00:00.000Z",
    "attendees": [
      {
        "id": 32,
        "email": "test@example.com",
        "name": "test",
        "timeZone": "Asia/Kolkata",
        "phoneNumber": null,
        "locale": "en",
        "bookingId": 32,
        "noShow": false
      }
    ],
    "endTime": "2025-12-02T04:30:00.000Z",
    "participants": [],
    "hostEmail": "owner1-dunder@example.com",
    "eventType": {
      "id": 50,
      "teamId": null,
      "parentId": null,
      "calVideoSettings": null
    },
    "webhook": {
      "id": "2bdfc20b-aa4a-4863-a499-932cb1d4e69a",
      "subscriberUrl": "https://webhook.site/example",
      "appId": null,
      "time": 5,
      "timeUnit": "MINUTE",
      "eventTriggers": [
        "AFTER_HOSTS_CAL_VIDEO_NO_SHOW",
        "AFTER_GUESTS_CAL_VIDEO_NO_SHOW"
      ],
      "payloadTemplate": null
    },
    "message": "Host with email owner1-dunder@example.com didn't join the call or didn't join before 2025-12-02 04:05:00 +00:00"
  }
}
```

**`Example payload when guest didn't join (AFTER_GUESTS_CAL_VIDEO_NO_SHOW):`**

```json theme={null}
{
  "triggerEvent": "AFTER_GUESTS_CAL_VIDEO_NO_SHOW",
  "createdAt": "2025-12-01T15:23:30.323Z",
  "payload": {
    "title": "30min between Owner 1 and test",
    "bookingId": 32,
    "bookingUid": "qVyXscm1ryg2QoQ4K8uHLW",
    "startTime": "2025-12-02T04:00:00.000Z",
    "attendees": [
      {
        "id": 32,
        "email": "test@example.com",
        "name": "test",
        "timeZone": "Asia/Kolkata",
        "phoneNumber": null,
        "locale": "en",
        "bookingId": 32,
        "noShow": false
      }
    ],
    "endTime": "2025-12-02T04:30:00.000Z",
    "participants": [],
    "eventType": {
      "id": 50,
      "teamId": null,
      "parentId": null,
      "calVideoSettings": null
    },
    "webhook": {
      "id": "2bdfc20b-aa4a-4863-a499-932cb1d4e69a",
      "subscriberUrl": "https://webhook.site/example",
      "appId": null,
      "time": 5,
      "timeUnit": "MINUTE",
      "eventTriggers": [
        "AFTER_HOSTS_CAL_VIDEO_NO_SHOW",
        "AFTER_GUESTS_CAL_VIDEO_NO_SHOW"
      ],
      "payloadTemplate": null
    },
    "message": "Guest didn't join the call or didn't join before 2025-12-02 04:05:00 +00:00"
  }
}
```

### Meeting started and meeting ended webhooks

The `MEETING_STARTED` and `MEETING_ENDED` webhooks are **time-delayed** — they fire automatically at the booking's scheduled start time and end time, respectively. You do not need to take any action to trigger them beyond subscribing to these events.

**Key behaviors:**

* **Automatic scheduling**: When a booking is confirmed, Cal.com schedules the `MEETING_STARTED` webhook to fire at the booking's `startTime` and the `MEETING_ENDED` webhook to fire at the booking's `endTime`.
* **Cancellation handling**: If a booking is cancelled or rescheduled, any pending `MEETING_STARTED` and `MEETING_ENDED` webhooks for that booking are automatically cancelled. When a booking is rescheduled, new webhooks are scheduled for the updated times.
* **Flat payload format**: Unlike other webhook events, these two events use a flat payload structure. The booking data is spread at the top level alongside `triggerEvent`, rather than nested inside a `payload` object. See the [example payloads](#webhook-payload-reference) for the exact structure.
* **No custom payload template support**: Custom payload templates are not applied to `MEETING_STARTED` and `MEETING_ENDED` webhooks. The payload is always sent as raw JSON.

<Note>
  If you are migrating from a system that consumes other webhook events, note that the payload shape for `MEETING_STARTED` and `MEETING_ENDED` differs from events like `BOOKING_CREATED`. Ensure your webhook handler accounts for the flat structure.
</Note>

### Delegation credential secret rotation webhooks

Delegation credentials let an organization act on behalf of its members with a workspace platform. Microsoft 365 (Azure Entra ID) delegation credentials authenticate with a client secret that expires, so Cal.com periodically rotates it and emits webhooks so administrators can track rotation health. Google delegation credentials don't have an expiring secret and are not part of this rotation lifecycle.

Subscribe to these events on an organization-scoped webhook to be notified about the delegation credential rotation lifecycle:

* **`DELEGATION_CREDENTIAL_SECRET_ROTATED`** — a pending secret was verified and promoted, and is now active.
* **`DELEGATION_CREDENTIAL_SECRET_ROTATION_FAILED`** — an automatic mint or promotion attempt has kept failing for 48+ hours and rotation is now blocked for that credential (`error.code` is `SECRET_MINT_FAILED` or `SECRET_PROMOTION_FAILED`). Transient failures before that terminal window are retried automatically and do not fire a webhook.
* **`DELEGATION_CREDENTIAL_ROTATION_REQUIRED`** — a reminder for credentials that opted out of automatic rotation (`optOutAutoSecretRotation=true`) whose active secret is nearing expiry. This event does not indicate that automatic rotation failed or was blocked — see `DELEGATION_CREDENTIAL_SECRET_ROTATION_FAILED` for that. In both cases, an administrator must rotate the secret manually from the delegation credential settings.

<Note>
  `DELEGATION_CREDENTIAL_SECRET_ROTATED` and `DELEGATION_CREDENTIAL_SECRET_ROTATION_FAILED` fire only for delegation credentials with automatic secret rotation enabled. `DELEGATION_CREDENTIAL_ROTATION_REQUIRED` fires only for delegation credentials that have opted out of automatic secret rotation. They are delivered asynchronously with retries on transient network errors and HTTP 408, 429, and 5xx responses.
</Note>

### Verifying the authenticity of the received payload

<Steps>
  <Step title="Add a new secret key to your webhook">
    Simply add a new **secret key** to your webhook configuration and save it.
  </Step>

  <Step title="Wait for the webhook to be triggered">
    The webhook will trigger when an event is created, cancelled, rescheduled, or when a meeting ends.
  </Step>

  <Step title="Create an HMAC using the secret key">
    Use the **secret key** to create an HMAC, and update it with the webhook payload received to generate an SHA256 hash.
  </Step>

  <Step title="Verify the payload authenticity">
    Compare the hash received in the header of the webhook `(x-cal-signature-256)` with the one you created using the **secret key** and the body of the payload. If they don't match, the received payload has been adulterated and cannot be trusted.
  </Step>
</Steps>

### Adding a custom payload template

Customizable webhooks are a great way reduce the development effort and in many cases remove the need for a developer to build an additional integration service.

An example of a custom payload template is provided here:

```json theme={null}
{
  "content": "A new event has been scheduled",
  "type": "{{type}}",
  "name": "{{title}}",
  "organizer": "{{organizer.name}}",
  "booker": "{{attendees.0.name}}"
}
```

where `{{type}}` represents the event type slug and `{{title}}` represents the title of the event type. Note that the variables should be added with a double parenthesis as shown above. Here’s a breakdown of the payload that you would receive via an incoming webhook, with an exhaustive list of all the supported variables provided below:

#### Webhook variable list

| Variable           | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| triggerEvent       | String    | The name of the trigger event \[BOOKING\_CREATED, BOOKING\_RESCHEDULED, BOOKING\_CANCELLED, MEETING\_ENDED, BOOKING\_REJECTED, BOOKING\_REQUESTED, BOOKING\_PAYMENT\_INITIATED, BOOKING\_PAID, MEETING\_STARTED, RECORDING\_READY, INSTANT\_MEETING, INSTANT\_MEETING\_ACCEPTED, FORM\_SUBMITTED, BOOKING\_NO\_SHOW\_UPDATED, AFTER\_HOSTS\_CAL\_VIDEO\_NO\_SHOW, AFTER\_GUESTS\_CAL\_VIDEO\_NO\_SHOW, WRONG\_ASSIGNMENT\_REPORT, DELEGATION\_CREDENTIAL\_ERROR, DELEGATION\_CREDENTIAL\_SECRET\_ROTATED, DELEGATION\_CREDENTIAL\_SECRET\_ROTATION\_FAILED, DELEGATION\_CREDENTIAL\_ROTATION\_REQUIRED] |
| createdAt          | Datetime  | The time of the webhook                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| type               | String    | The event type slug                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| title              | String    | The event type name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| startTime          | Datetime  | The event's start time                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| endTime            | Datetime  | The event's end time                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| description        | String    | The event's description as described in the event type settings                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| location           | String    | Location of the event                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| organizer          | Person    | The organizer of the event                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| attendees          | Person\[] | The event booker & any guests. For seated event types, this contains only the attendee for the specific seat that triggered the webhook.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| uid                | String    | The UID of the booking                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| rescheduleUid      | String    | The UID for rescheduling                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| cancellationReason | String    | Reason for cancellation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| rejectionReason    | String    | Reason for rejection                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| team.name          | String    | Name of the team booked                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| team.members       | String\[] | Members of the team booked                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| metadata           | JSON      | Contains metadata of the booking, including the meeting URL (videoCallUrl) in case of Google Meet and Cal Video                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

#### Person Structure

| Variable         | Type   | Description                                                            |
| ---------------- | ------ | ---------------------------------------------------------------------- |
| name             | String | Name of the individual                                                 |
| email            | Email  | Email of the individual                                                |
| timezone         | String | Timezone of the individual (e.g., "America/New\_York", "Asia/Kolkata") |
| language?.locale | String | Locale of the individual (e.g., "en", "fr")                            |
