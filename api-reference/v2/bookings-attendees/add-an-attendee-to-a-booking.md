> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Add an attendee to a booking

> Add a new attendee to an existing booking by its UID.

      **Seated Events:**
      This endpoint does not support seated event bookings. For seated events, each attendee must be added by creating a new booking for the same event type and time slot via `POST /v2/bookings`. Attempting to add an attendee to a seated event booking will return a 400 error.

      **Side effects:**
      - The booking's attendee list is updated in the database
      - The calendar event is updated on connected calendars (Google Calendar, Outlook, etc.) to include the new attendee
      - An email notification is sent to the new attendee with the booking details

      **Permissions:**
      - The authenticated user must be either the booking organizer, an existing attendee, or have the `booking.update` permission for the team

      <Note>The cal-api-version header is required for this endpoint. Without it, the request will fail with a 404 error.</Note>

If accessed using an OAuth access token, the `BOOKING_WRITE` scope is required.
      



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/bookings/{bookingUid}/attendees
openapi: 3.0.0
info:
  title: Cal.com API v2
  description: ''
  version: 1.0.0
  contact: {}
servers: []
security: []
tags: []
paths:
  /v2/bookings/{bookingUid}/attendees:
    post:
      tags:
        - Bookings / Attendees
      summary: Add an attendee to a booking
      description: >-
        Add a new attendee to an existing booking by its UID.

              **Seated Events:**
              This endpoint does not support seated event bookings. For seated events, each attendee must be added by creating a new booking for the same event type and time slot via `POST /v2/bookings`. Attempting to add an attendee to a seated event booking will return a 400 error.

              **Side effects:**
              - The booking's attendee list is updated in the database
              - The calendar event is updated on connected calendars (Google Calendar, Outlook, etc.) to include the new attendee
              - An email notification is sent to the new attendee with the booking details

              **Permissions:**
              - The authenticated user must be either the booking organizer, an existing attendee, or have the `booking.update` permission for the team

              <Note>The cal-api-version header is required for this endpoint. Without it, the request will fail with a 404 error.</Note>

        If accessed using an OAuth access token, the `BOOKING_WRITE` scope is
        required.
              
      operationId: BookingAttendeesController_2024_08_13_addAttendee
      parameters:
        - name: cal-api-version
          in: header
          description: >-
            Must be set to 2024-08-13. This header is required as this endpoint
            does not exist in older API versions.
          required: true
          schema:
            type: string
            example: '2024-08-13'
        - name: bookingUid
          required: true
          in: path
          schema:
            type: string
        - name: Authorization
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_, managed user access token, or OAuth access token
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AddAttendeeInput_2024_08_13'
      responses:
        '201':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AddAttendeeOutput_2024_08_13'
components:
  schemas:
    AddAttendeeInput_2024_08_13:
      type: object
      properties:
        name:
          type: string
          description: The name of the attendee.
          example: John Doe
        timeZone:
          type: string
          description: The time zone of the attendee.
          example: America/New_York
        phoneNumber:
          type: string
          description: The phone number of the attendee in international format.
          example: '+919876543210'
        language:
          enum:
            - ar
            - ca
            - de
            - es
            - eu
            - he
            - id
            - ja
            - lv
            - pl
            - ro
            - sr
            - th
            - vi
            - az
            - cs
            - el
            - es-419
            - fi
            - hr
            - it
            - km
            - nl
            - pt
            - ru
            - sv
            - tr
            - zh-CN
            - bg
            - da
            - en
            - et
            - fr
            - hu
            - iw
            - ko
            - 'no'
            - pt-BR
            - sk
            - ta
            - uk
            - zh-TW
            - bn
          type: string
          description: >-
            The preferred language of the attendee. Used for booking
            confirmation.
          example: it
          default: en
        email:
          type: string
          format: email
          description: The email of the attendee.
          example: john.doe@example.com
      required:
        - name
        - timeZone
        - email
    AddAttendeeOutput_2024_08_13:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/BookingAttendeeOutput_2024_08_13'
      required:
        - status
        - data
    BookingAttendeeOutput_2024_08_13:
      type: object
      properties:
        name:
          type: string
          example: John Doe
        email:
          type: string
          example: john@example.com
        displayEmail:
          type: string
          example: john@example.com
          description: Clean email for display purposes
        timeZone:
          type: string
          example: America/New_York
        language:
          enum:
            - ar
            - ca
            - de
            - es
            - eu
            - he
            - id
            - ja
            - lv
            - pl
            - ro
            - sr
            - th
            - vi
            - az
            - cs
            - el
            - es-419
            - fi
            - hr
            - it
            - km
            - nl
            - pt
            - ru
            - sv
            - tr
            - zh-CN
            - bg
            - da
            - en
            - et
            - fr
            - hu
            - iw
            - ko
            - 'no'
            - pt-BR
            - sk
            - ta
            - uk
            - zh-TW
            - bn
          type: string
          example: en
        absent:
          type: boolean
          example: false
        phoneNumber:
          type: string
          example: '+1234567890'
        id:
          type: number
          example: 251
        bookingId:
          type: number
          example: 313
      required:
        - name
        - email
        - displayEmail
        - timeZone
        - absent
        - id
        - bookingId

````