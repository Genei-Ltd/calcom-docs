> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get team bookings

> If accessed using an OAuth access token, the `TEAM_BOOKING_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/teams/{teamId}/bookings
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
  /v2/teams/{teamId}/bookings:
    get:
      tags:
        - Teams / Bookings
      summary: Get team bookings
      description: >-
        If accessed using an OAuth access token, the `TEAM_BOOKING_READ` scope
        is required.
      operationId: TeamsBookingsController_getAllTeamBookings
      parameters:
        - name: Authorization
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_
          required: true
          schema:
            type: string
        - name: status
          required: false
          in: query
          description: >-
            Filter bookings by status. If you want to filter by multiple
            statuses, separate them with a comma.
          schema:
            minItems: 1
            example: '?status=upcoming,past'
            type: array
            items:
              type: string
              enum:
                - upcoming
                - recurring
                - past
                - cancelled
                - unconfirmed
        - name: attendeeEmail
          required: false
          in: query
          description: Filter bookings by the attendee's email address.
          schema:
            example: example@domain.com
            type: string
        - name: attendeeName
          required: false
          in: query
          description: Filter bookings by the attendee's name.
          schema:
            type: string
            example: John Doe
        - name: bookingUid
          required: false
          in: query
          description: Filter bookings by the booking Uid.
          schema:
            example: 2NtaeaVcKfpmSZ4CthFdfk
            type: string
        - name: eventTypeIds
          required: false
          in: query
          description: >-
            Filter bookings by event type ids. Event type ids must be separated
            by a comma.
          schema:
            minItems: 1
            example: '?eventTypeIds=100,200'
            type: string
        - name: eventTypeId
          required: false
          in: query
          description: Filter bookings by event type id.
          schema:
            example: '?eventTypeId=100'
            type: string
        - name: afterStart
          required: false
          in: query
          description: Filter bookings with start after this date string.
          schema:
            example: '?afterStart=2025-03-07T10:00:00.000Z'
            type: string
        - name: beforeEnd
          required: false
          in: query
          description: Filter bookings with end before this date string.
          schema:
            example: '?beforeEnd=2025-03-07T11:00:00.000Z'
            type: string
        - name: afterCreatedAt
          required: false
          in: query
          description: Filter bookings that have been created after this date string.
          schema:
            example: '?afterCreatedAt=2025-03-07T10:00:00.000Z'
            type: string
        - name: beforeCreatedAt
          required: false
          in: query
          description: Filter bookings that have been created before this date string.
          schema:
            example: '?beforeCreatedAt=2025-03-14T11:00:00.000Z'
            type: string
        - name: afterUpdatedAt
          required: false
          in: query
          description: Filter bookings that have been updated after this date string.
          schema:
            example: '?afterUpdatedAt=2025-03-07T10:00:00.000Z'
            type: string
        - name: beforeUpdatedAt
          required: false
          in: query
          description: Filter bookings that have been updated before this date string.
          schema:
            example: '?beforeUpdatedAt=2025-03-14T11:00:00.000Z'
            type: string
        - name: sortStart
          required: false
          in: query
          description: Sort results by their start time in ascending or descending order.
          schema:
            example: '?sortStart=asc OR ?sortStart=desc'
            type: string
            enum:
              - asc
              - desc
        - name: sortEnd
          required: false
          in: query
          description: Sort results by their end time in ascending or descending order.
          schema:
            example: '?sortEnd=asc OR ?sortEnd=desc'
            type: string
            enum:
              - asc
              - desc
        - name: sortCreated
          required: false
          in: query
          description: >-
            Sort results by their creation time (when booking was made) in
            ascending or descending order.
          schema:
            example: '?sortCreated=asc OR ?sortCreated=desc'
            type: string
            enum:
              - asc
              - desc
        - name: sortUpdatedAt
          required: false
          in: query
          description: >-
            Sort results by their updated time (for example when booking status
            changes) in ascending or descending order.
          schema:
            example: '?sortUpdatedAt=asc OR ?sortUpdatedAt=desc'
            type: string
            enum:
              - asc
              - desc
        - name: take
          required: false
          in: query
          description: The number of items to return
          schema:
            minimum: 1
            maximum: 250
            default: 100
            example: 10
            type: number
        - name: skip
          required: false
          in: query
          description: The number of items to skip
          schema:
            minimum: 0
            default: 0
            example: 0
            type: number
        - name: teamId
          required: true
          in: path
          schema:
            type: number
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetBookingsOutput_2024_08_13'
components:
  schemas:
    GetBookingsOutput_2024_08_13:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          type: array
          items:
            oneOf:
              - $ref: '#/components/schemas/BookingOutput_2024_08_13'
                title: Booking
              - $ref: '#/components/schemas/RecurringBookingOutput_2024_08_13'
                title: Recurring Booking
              - $ref: '#/components/schemas/GetSeatedBookingOutput_2024_08_13'
                title: Seated Booking
              - $ref: >-
                  #/components/schemas/GetRecurringSeatedBookingOutput_2024_08_13
                title: Recurring Seated Booking
          description: >-
            Array of booking data, which can contain either BookingOutput
            objects or RecurringBookingOutput objects
        pagination:
          $ref: '#/components/schemas/PaginationMetaDto'
      required:
        - status
        - data
        - pagination
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
    PaginationMetaDto:
      type: object
      properties:
        totalItems:
          type: number
          minimum: 0
          description: >-
            The total number of items available across all pages, matching the
            query criteria.
          example: 123
        remainingItems:
          type: number
          minimum: 0
          description: >-
            The number of items remaining to be fetched *after* the current
            page. Calculated as: `totalItems - (skip + itemsPerPage)`.
          example: 103
        returnedItems:
          type: number
          minimum: 0
          description: The number of items returned in the current page.
          example: 10
        itemsPerPage:
          type: number
          minimum: 1
          description: The maximum number of items requested per page.
          example: 10
        currentPage:
          type: number
          minimum: 1
          description: The current page number being returned.
          example: 2
        totalPages:
          type: number
          minimum: 0
          description: The total number of pages available.
          example: 13
        hasNextPage:
          type: boolean
          description: >-
            Indicates if there is a subsequent page available after the current
            one.
          example: true
        hasPreviousPage:
          type: boolean
          description: >-
            Indicates if there is a preceding page available before the current
            one.
          example: true
      required:
        - totalItems
        - remainingItems
        - returnedItems
        - itemsPerPage
        - currentPage
        - totalPages
        - hasNextPage
        - hasPreviousPage
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