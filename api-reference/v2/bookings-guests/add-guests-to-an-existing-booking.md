> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Add guests to an existing booking

> Add one or more guests to an existing booking. Maximum 10 guests per request, with a limit of 30 total guests per booking.
    
    **Rate Limiting:**
    This endpoint is rate limited to 5 requests per minute to prevent abuse.
    
    **Seated Events:**
    This endpoint does not support seated event bookings. For seated events, each guest must be added by creating a new booking for the same event type and time slot via `POST /v2/bookings`. Attempting to add guests to a seated event booking will return a 400 error.
    
    **Email Notifications:**
    When guests are added, the following notifications are sent (unless disabled by event type settings):
    
    - **Organizer & Team Members:** Receive an "Add Guests" notification email informing them that new guests have been added to the booking.
    
    - **New Guests:** Receive a "Scheduled Event" email with full booking details and calendar invite. If they have a phone number, they also receive an SMS notification.
    
    - **Existing Guests:** Receive an "Add Guests" notification email informing them that additional guests have been added to the booking.
    
    <Note>The cal-api-version header is required for this endpoint. Without it, the request will fail with a 404 error.</Note>

If accessed using an OAuth access token, the `BOOKING_WRITE` scope is required.
    



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/bookings/{bookingUid}/guests
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
  /v2/bookings/{bookingUid}/guests:
    post:
      tags:
        - Bookings / Guests
      summary: Add guests to an existing booking
      description: >-
        Add one or more guests to an existing booking. Maximum 10 guests per
        request, with a limit of 30 total guests per booking.
            
            **Rate Limiting:**
            This endpoint is rate limited to 5 requests per minute to prevent abuse.
            
            **Seated Events:**
            This endpoint does not support seated event bookings. For seated events, each guest must be added by creating a new booking for the same event type and time slot via `POST /v2/bookings`. Attempting to add guests to a seated event booking will return a 400 error.
            
            **Email Notifications:**
            When guests are added, the following notifications are sent (unless disabled by event type settings):
            
            - **Organizer & Team Members:** Receive an "Add Guests" notification email informing them that new guests have been added to the booking.
            
            - **New Guests:** Receive a "Scheduled Event" email with full booking details and calendar invite. If they have a phone number, they also receive an SMS notification.
            
            - **Existing Guests:** Receive an "Add Guests" notification email informing them that additional guests have been added to the booking.
            
            <Note>The cal-api-version header is required for this endpoint. Without it, the request will fail with a 404 error.</Note>

        If accessed using an OAuth access token, the `BOOKING_WRITE` scope is
        required.
            
      operationId: BookingGuestsController_2024_08_13_addGuests
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
              $ref: '#/components/schemas/AddGuestsInput_2024_08_13'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AddGuestsOutput_2024_08_13'
components:
  schemas:
    AddGuestsInput_2024_08_13:
      type: object
      properties:
        guests:
          minItems: 1
          description: >-
            Array of guests to add to the booking. Maximum 100 guests per
            request.
          example:
            - email: john.doe@example.com
              name: John Doe
              timeZone: America/New_York
            - email: jane.smith@example.com
              name: Jane Smith
          type: array
          items:
            $ref: '#/components/schemas/Guest'
      required:
        - guests
    AddGuestsOutput_2024_08_13:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          oneOf:
            - $ref: '#/components/schemas/BookingOutput_2024_08_13'
              title: Booking
            - $ref: '#/components/schemas/RecurringBookingOutput_2024_08_13'
              title: Recurring Booking
            - title: Recurring Bookings (array)
              type: array
              items:
                $ref: '#/components/schemas/RecurringBookingOutput_2024_08_13'
            - $ref: '#/components/schemas/GetSeatedBookingOutput_2024_08_13'
              title: Seated Booking
            - $ref: '#/components/schemas/GetRecurringSeatedBookingOutput_2024_08_13'
              title: Recurring Seated Booking
            - title: Recurring Seated Bookings (array)
              type: array
              items:
                $ref: >-
                  #/components/schemas/GetRecurringSeatedBookingOutput_2024_08_13
          description: >-
            Booking data, which can be either a BookingOutput object, a
            RecurringBookingOutput object, or an array of RecurringBookingOutput
            objects
      required:
        - status
        - data
    Guest:
      type: object
      properties:
        email:
          type: string
          description: The email of the guest.
          example: john.doe@example.com
        name:
          type: string
          description: The name of the guest.
          example: John Doe
        timeZone:
          type: string
          description: The time zone of the guest.
          example: America/New_York
        phoneNumber:
          type: string
          description: The phone number of the guest in international format.
          example: '+919876543210'
        language:
          type: string
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
          description: The preferred language of the guest. Used for booking confirmation.
          example: it
          default: en
      required:
        - email
    BookingOutput_2024_08_13:
      type: object
      properties:
        id:
          type: number
          example: 123
        uid:
          type: string
          example: booking_uid_123
        title:
          type: string
          example: Consultation
        description:
          type: string
          example: Learn how to integrate scheduling into marketplace.
        hosts:
          type: array
          items:
            $ref: '#/components/schemas/BookingHost'
        status:
          enum:
            - cancelled
            - accepted
            - rejected
            - pending
          type: string
          example: accepted
        cancellationReason:
          type: string
          example: User requested cancellation
        cancelledByEmail:
          type: string
          format: email
          example: canceller@example.com
        reschedulingReason:
          type: string
          example: User rescheduled the event
        rescheduledByEmail:
          type: string
          format: email
          example: rescheduler@example.com
        rescheduledFromUid:
          type: string
          example: previous_uid_123
          description: UID of the previous booking from which this booking was rescheduled.
        rescheduledToUid:
          type: string
          example: new_uid_456
          description: UID of the new booking to which this booking was rescheduled.
        start:
          type: string
          example: '2024-08-13T15:30:00Z'
          format: date-time
        end:
          type: string
          example: '2024-08-13T16:30:00Z'
          format: date-time
        duration:
          type: number
          example: 60
        eventTypeId:
          type: number
          example: 50
          deprecated: true
          description: Deprecated - rely on 'eventType' object containing the id instead.
        eventType:
          $ref: '#/components/schemas/EventType'
        meetingUrl:
          type: string
          format: uri
          description: Deprecated - rely on 'location' field instead.
          example: https://example.com/recurring-meeting
          deprecated: true
        location:
          type: string
          example: https://example.com/meeting
        absentHost:
          type: boolean
          example: true
        createdAt:
          type: string
          example: '2024-08-13T15:30:00Z'
          format: date-time
        updatedAt:
          type: string
          nullable: true
          example: '2024-08-13T15:30:00Z'
          format: date-time
        metadata:
          type: object
          additionalProperties:
            type: string
          example:
            key: value
        rating:
          type: number
          example: 4
        icsUid:
          type: string
          example: ics_uid_123
          description: UID of ICS event.
        attendees:
          type: array
          items:
            $ref: '#/components/schemas/BookingAttendee'
        guests:
          example:
            - guest1@example.com
            - guest2@example.com
          type: array
          items:
            type: string
        bookingFieldsResponses:
          type: object
          additionalProperties: true
          description: >-
            Booking field responses consisting of an object with booking field
            slug as keys and user response as values.
          example:
            customField: customValue
      required:
        - id
        - uid
        - title
        - description
        - hosts
        - status
        - start
        - end
        - duration
        - eventTypeId
        - eventType
        - location
        - absentHost
        - createdAt
        - updatedAt
        - attendees
        - bookingFieldsResponses
    RecurringBookingOutput_2024_08_13:
      type: object
      properties:
        id:
          type: number
          example: 123
        uid:
          type: string
          example: booking_uid_123
        title:
          type: string
          example: Consultation
        description:
          type: string
          example: Learn how to integrate scheduling into marketplace.
        hosts:
          type: array
          items:
            $ref: '#/components/schemas/BookingHost'
        status:
          enum:
            - cancelled
            - accepted
            - rejected
            - pending
          type: string
          example: accepted
        cancellationReason:
          type: string
          example: User requested cancellation
        cancelledByEmail:
          type: string
          format: email
          example: canceller@example.com
        reschedulingReason:
          type: string
          example: User rescheduled the event
        rescheduledByEmail:
          type: string
          format: email
          example: rescheduler@example.com
        rescheduledFromUid:
          type: string
          example: previous_uid_123
          description: UID of the previous booking from which this booking was rescheduled.
        rescheduledToUid:
          type: string
          example: new_uid_456
          description: UID of the new booking to which this booking was rescheduled.
        start:
          type: string
          example: '2024-08-13T15:30:00Z'
          format: date-time
        end:
          type: string
          example: '2024-08-13T16:30:00Z'
          format: date-time
        duration:
          type: number
          example: 60
        eventTypeId:
          type: number
          example: 50
          deprecated: true
          description: Deprecated - rely on 'eventType' object containing the id instead.
        eventType:
          $ref: '#/components/schemas/EventType'
        meetingUrl:
          type: string
          format: uri
          description: Deprecated - rely on 'location' field instead.
          example: https://example.com/recurring-meeting
          deprecated: true
        location:
          type: string
          example: https://example.com/meeting
        absentHost:
          type: boolean
          example: true
        createdAt:
          type: string
          example: '2024-08-13T15:30:00Z'
          format: date-time
        updatedAt:
          type: string
          nullable: true
          example: '2024-08-13T15:30:00Z'
          format: date-time
        metadata:
          type: object
          additionalProperties:
            type: string
          example:
            key: value
        rating:
          type: number
          example: 4
        icsUid:
          type: string
          example: ics_uid_123
          description: UID of ICS event.
        attendees:
          type: array
          items:
            $ref: '#/components/schemas/BookingAttendee'
        guests:
          example:
            - guest1@example.com
            - guest2@example.com
          type: array
          items:
            type: string
        bookingFieldsResponses:
          type: object
          additionalProperties: true
          description: >-
            Booking field responses consisting of an object with booking field
            slug as keys and user response as values.
          example:
            customField: customValue
        recurringBookingUid:
          type: string
          example: recurring_uid_987
      required:
        - id
        - uid
        - title
        - description
        - hosts
        - status
        - start
        - end
        - duration
        - eventTypeId
        - eventType
        - location
        - absentHost
        - createdAt
        - updatedAt
        - attendees
        - bookingFieldsResponses
        - recurringBookingUid
    GetSeatedBookingOutput_2024_08_13:
      type: object
      properties:
        id:
          type: number
          example: 123
        uid:
          type: string
          example: booking_uid_123
        title:
          type: string
          example: Consultation
        description:
          type: string
          example: Learn how to integrate scheduling into marketplace.
        hosts:
          type: array
          items:
            $ref: '#/components/schemas/BookingHost'
        status:
          enum:
            - cancelled
            - accepted
            - rejected
            - pending
          type: string
          example: accepted
        cancellationReason:
          type: string
          example: User requested cancellation
        cancelledByEmail:
          type: string
          format: email
          example: canceller@example.com
        reschedulingReason:
          type: string
          example: User rescheduled the event
        rescheduledByEmail:
          type: string
          format: email
          example: rescheduler@example.com
        rescheduledFromUid:
          type: string
          example: previous_uid_123
          description: UID of the previous booking from which this booking was rescheduled.
        rescheduledToUid:
          type: string
          example: new_uid_456
          description: UID of the new booking to which this booking was rescheduled.
        start:
          type: string
          example: '2024-08-13T15:30:00Z'
          format: date-time
        end:
          type: string
          example: '2024-08-13T16:30:00Z'
          format: date-time
        duration:
          type: number
          example: 60
        eventTypeId:
          type: number
          example: 50
          deprecated: true
          description: Deprecated - rely on 'eventType' object containing the id instead.
        eventType:
          $ref: '#/components/schemas/EventType'
        meetingUrl:
          type: string
          format: uri
          description: Deprecated - rely on 'location' field instead.
          example: https://example.com/recurring-meeting
          deprecated: true
        location:
          type: string
          example: https://example.com/meeting
        absentHost:
          type: boolean
          example: true
        createdAt:
          type: string
          example: '2024-08-13T15:30:00Z'
          format: date-time
        updatedAt:
          type: string
          nullable: true
          example: '2024-08-13T15:30:00Z'
          format: date-time
        metadata:
          type: object
          additionalProperties:
            type: string
          example:
            key: value
        rating:
          type: number
          example: 4
        icsUid:
          type: string
          example: ics_uid_123
          description: UID of ICS event.
        attendees:
          type: array
          items:
            $ref: '#/components/schemas/SeatedAttendee'
      required:
        - id
        - uid
        - title
        - description
        - hosts
        - status
        - start
        - end
        - duration
        - eventTypeId
        - eventType
        - location
        - absentHost
        - createdAt
        - updatedAt
        - attendees
    GetRecurringSeatedBookingOutput_2024_08_13:
      type: object
      properties:
        id:
          type: number
          example: 123
        uid:
          type: string
          example: booking_uid_123
        title:
          type: string
          example: Consultation
        description:
          type: string
          example: Learn how to integrate scheduling into marketplace.
        hosts:
          type: array
          items:
            $ref: '#/components/schemas/BookingHost'
        status:
          enum:
            - cancelled
            - accepted
            - rejected
            - pending
          type: string
          example: accepted
        cancellationReason:
          type: string
          example: User requested cancellation
        cancelledByEmail:
          type: string
          format: email
          example: canceller@example.com
        reschedulingReason:
          type: string
          example: User rescheduled the event
        rescheduledByEmail:
          type: string
          format: email
          example: rescheduler@example.com
        rescheduledFromUid:
          type: string
          example: previous_uid_123
          description: UID of the previous booking from which this booking was rescheduled.
        rescheduledToUid:
          type: string
          example: new_uid_456
          description: UID of the new booking to which this booking was rescheduled.
        start:
          type: string
          example: '2024-08-13T15:30:00Z'
          format: date-time
        end:
          type: string
          example: '2024-08-13T16:30:00Z'
          format: date-time
        duration:
          type: number
          example: 60
        eventTypeId:
          type: number
          example: 50
          deprecated: true
          description: Deprecated - rely on 'eventType' object containing the id instead.
        eventType:
          $ref: '#/components/schemas/EventType'
        meetingUrl:
          type: string
          format: uri
          description: Deprecated - rely on 'location' field instead.
          example: https://example.com/recurring-meeting
          deprecated: true
        location:
          type: string
          example: https://example.com/meeting
        absentHost:
          type: boolean
          example: true
        createdAt:
          type: string
          example: '2024-08-13T15:30:00Z'
          format: date-time
        updatedAt:
          type: string
          nullable: true
          example: '2024-08-13T15:30:00Z'
          format: date-time
        metadata:
          type: object
          additionalProperties:
            type: string
          example:
            key: value
        rating:
          type: number
          example: 4
        icsUid:
          type: string
          example: ics_uid_123
          description: UID of ICS event.
        attendees:
          type: array
          items:
            $ref: '#/components/schemas/SeatedAttendee'
        recurringBookingUid:
          type: string
          example: recurring_uid_987
      required:
        - id
        - uid
        - title
        - description
        - hosts
        - status
        - start
        - end
        - duration
        - eventTypeId
        - eventType
        - location
        - absentHost
        - createdAt
        - updatedAt
        - attendees
        - recurringBookingUid
    BookingHost:
      type: object
      properties:
        id:
          type: number
          example: 1
        name:
          type: string
          example: Jane Doe
        email:
          type: string
          example: jane100@example.com
        displayEmail:
          type: string
          example: jane100@example.com
          description: Clean email for display purposes
        username:
          type: string
          example: jane100
        timeZone:
          type: string
          example: America/Los_Angeles
      required:
        - id
        - name
        - email
        - displayEmail
        - username
        - timeZone
    EventType:
      type: object
      properties:
        id:
          type: number
          example: 1
        slug:
          type: string
          example: some-event
      required:
        - id
        - slug
    BookingAttendee:
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
      required:
        - name
        - email
        - displayEmail
        - timeZone
        - absent
    SeatedAttendee:
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
        seatUid:
          type: string
          example: 3be561a9-31f1-4b8e-aefc-9d9a085f0dd1
        createdAt:
          type: string
          example: '2024-08-13T15:30:00Z'
          description: The date and time when the attendee joined the seated booking.
        bookingFieldsResponses:
          type: object
          additionalProperties: true
          description: >-
            Booking field responses consisting of an object with booking field
            slug as keys and user response as values.
          example:
            customField: customValue
        metadata:
          type: object
          additionalProperties:
            type: string
          example:
            key: value
      required:
        - name
        - email
        - displayEmail
        - timeZone
        - absent
        - seatUid
        - bookingFieldsResponses

````