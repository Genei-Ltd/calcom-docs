> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a booking

> `:bookingUid` can be

      1. uid of a normal booking

      2. uid of one of the recurring booking recurrences

      3. uid of recurring booking which will return an array of all recurring booking recurrences (stored as recurringBookingUid on one of the individual recurrences).

      If you are fetching a seated booking for an event type with 'show attendees' disabled, then to retrieve attendees in the response either set 'show attendees' to true on event type level or
      you have to provide an authentication method of event type owner, host, team admin or owner or org admin or owner.

      <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>
      



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/bookings/{bookingUid}
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
  /v2/bookings/{bookingUid}:
    get:
      tags:
        - Bookings
      summary: Get a booking
      description: |-
        `:bookingUid` can be

              1. uid of a normal booking

              2. uid of one of the recurring booking recurrences

              3. uid of recurring booking which will return an array of all recurring booking recurrences (stored as recurringBookingUid on one of the individual recurrences).

              If you are fetching a seated booking for an event type with 'show attendees' disabled, then to retrieve attendees in the response either set 'show attendees' to true on event type level or
              you have to provide an authentication method of event type owner, host, team admin or owner or org admin or owner.

              <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>
              
      operationId: BookingsController_2026_02_25_getBooking
      parameters:
        - name: cal-api-version
          in: header
          description: Must be set to 2026-02-25.
          required: true
          schema:
            type: string
            default: '2026-02-25'
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
          required: false
          schema:
            type: string
        - name: x-cal-secret-key
          in: header
          description: For platform customers - OAuth client secret key
          required: false
          schema:
            type: string
        - name: x-cal-client-id
          in: header
          description: For platform customers - OAuth client ID
          required: false
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetBookingOutput_2024_08_13'
components:
  schemas:
    GetBookingOutput_2024_08_13:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          oneOf:
            - $ref: '#/components/schemas/BookingOutput_2024_08_13'
            - $ref: '#/components/schemas/RecurringBookingOutput_2024_08_13'
            - type: array
              items:
                $ref: '#/components/schemas/RecurringBookingOutput_2024_08_13'
            - $ref: '#/components/schemas/GetSeatedBookingOutput_2024_08_13'
            - $ref: '#/components/schemas/GetRecurringSeatedBookingOutput_2024_08_13'
            - type: array
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
          type: string
          enum:
            - cancelled
            - accepted
            - rejected
            - pending
          example: accepted
        cancellationReason:
          type: string
          example: User requested cancellation
        cancelledByEmail:
          type: string
          example: canceller@example.com
        reschedulingReason:
          type: string
          example: User rescheduled the event
        rescheduledByEmail:
          type: string
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
          type: string
          enum:
            - cancelled
            - accepted
            - rejected
            - pending
          example: accepted
        cancellationReason:
          type: string
          example: User requested cancellation
        cancelledByEmail:
          type: string
          example: canceller@example.com
        reschedulingReason:
          type: string
          example: User rescheduled the event
        rescheduledByEmail:
          type: string
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
          type: string
          enum:
            - cancelled
            - accepted
            - rejected
            - pending
          example: accepted
        cancellationReason:
          type: string
          example: User requested cancellation
        cancelledByEmail:
          type: string
          example: canceller@example.com
        reschedulingReason:
          type: string
          example: User rescheduled the event
        rescheduledByEmail:
          type: string
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
          type: string
          enum:
            - cancelled
            - accepted
            - rejected
            - pending
          example: accepted
        cancellationReason:
          type: string
          example: User requested cancellation
        cancelledByEmail:
          type: string
          example: canceller@example.com
        reschedulingReason:
          type: string
          example: User rescheduled the event
        rescheduledByEmail:
          type: string
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
          description: >-
            Booking field responses consisting of an object with booking field
            slug as keys and user response as values.
          example:
            customField: customValue
        metadata:
          type: object
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