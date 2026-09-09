> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get organization bookings (cursor pagination)

> Cursor-paginated org bookings listing. Pass the `pagination.nextCursor` from the previous response as the `cursor` query parameter to fetch the next page. Omit `cursor` to fetch the first page. `pagination.hasMore` is `false` and `pagination.nextCursor` is `null` when you've reached the last page.

<Note>Must pass `cal-api-version: 2026-05-01` header.</Note>

**`status` filters to a single status.** Pass one (e.g. `?status=upcoming`) or omit to walk all statuses. To list bookings across multiple statuses, issue parallel requests — one per status — and merge client-side.

Required membership role: `org admin`. PBAC permission: `booking.readOrgBookings`. If accessed using an OAuth access token, the `ORG_BOOKING_READ` scope is required.

For managed organizations, bookings where the managed organization owner is the organizer or an attendee are excluded from the result.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/organizations/{orgId}/bookings
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
  /v2/organizations/{orgId}/bookings:
    get:
      tags:
        - Orgs / Bookings
      summary: Get organization bookings (cursor pagination)
      description: >-
        Cursor-paginated org bookings listing. Pass the `pagination.nextCursor`
        from the previous response as the `cursor` query parameter to fetch the
        next page. Omit `cursor` to fetch the first page. `pagination.hasMore`
        is `false` and `pagination.nextCursor` is `null` when you've reached the
        last page.


        <Note>Must pass `cal-api-version: 2026-05-01` header.</Note>


        **`status` filters to a single status.** Pass one (e.g.
        `?status=upcoming`) or omit to walk all statuses. To list bookings
        across multiple statuses, issue parallel requests — one per status — and
        merge client-side.


        Required membership role: `org admin`. PBAC permission:
        `booking.readOrgBookings`. If accessed using an OAuth access token, the
        `ORG_BOOKING_READ` scope is required.


        For managed organizations, bookings where the managed organization owner
        is the organizer or an attendee are excluded from the result.
      operationId: OrganizationsBookingsController_getAllOrgTeamBookingsCursor
      parameters:
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
        - name: status
          required: false
          in: query
          description: >-
            Filter bookings by a single status. Pass one (e.g.
            `?status=upcoming`) or omit to walk all statuses ordered by
            `Booking.uuid DESC`. To list bookings across multiple statuses,
            issue parallel requests, one per status.
          schema:
            example: upcoming
            enum:
              - upcoming
              - recurring
              - past
              - cancelled
              - unconfirmed
            type: string
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
            example: '?eventTypeIds=100,200'
            type: string
        - name: eventTypeId
          required: false
          in: query
          description: Filter bookings by event type id.
          schema:
            example: '?eventTypeId=100'
            type: string
        - name: teamsIds
          required: false
          in: query
          description: >-
            Filter bookings by team ids that user is part of. Team ids must be
            separated by a comma.
          schema:
            example: '?teamIds=50,60'
            type: string
        - name: teamId
          required: false
          in: query
          description: Filter bookings by team id that user is part of
          schema:
            example: '?teamId=50'
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
            enum:
              - asc
              - desc
            type: string
        - name: sortEnd
          required: false
          in: query
          description: Sort results by their end time in ascending or descending order.
          schema:
            example: '?sortEnd=asc OR ?sortEnd=desc'
            enum:
              - asc
              - desc
            type: string
        - name: sortCreated
          required: false
          in: query
          description: >-
            Sort results by their creation time (when booking was made) in
            ascending or descending order.
          schema:
            example: '?sortCreated=asc OR ?sortCreated=desc'
            enum:
              - asc
              - desc
            type: string
        - name: sortUpdatedAt
          required: false
          in: query
          description: >-
            Sort results by their updated time (for example when booking status
            changes) in ascending or descending order.
          schema:
            example: '?sortUpdatedAt=asc OR ?sortUpdatedAt=desc'
            enum:
              - asc
              - desc
            type: string
        - name: cursor
          required: false
          in: query
          description: >-
            Opaque cursor for cursor-based pagination. Pass the
            `pagination.nextCursor` value from a previous response to fetch the
            next page. Omit to fetch the first page.
          schema:
            example: >-
              eyJ2IjoxLCJzb3J0VXVpZCI6IjAxOGY0YzJlLTNmMWEtN2FiYy05ZGVmLTAxMjM0NTY3ODlhYiJ9
            type: string
        - name: limit
          required: false
          in: query
          description: The number of items to return
          schema:
            minimum: 1
            maximum: 100
            default: 50
            example: 50
            type: number
        - name: userIds
          required: false
          in: query
          description: Filter bookings by ids of users within your organization.
          schema:
            example: '?userIds=100,200'
            type: string
        - name: orgId
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
                $ref: '#/components/schemas/GetBookingsOutput_2026_05_01'
components:
  schemas:
    GetBookingsOutput_2026_05_01:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          type: array
          items:
            oneOf:
              - $ref: '#/components/schemas/BookingOutput_2024_08_13'
              - $ref: '#/components/schemas/RecurringBookingOutput_2024_08_13'
              - $ref: '#/components/schemas/GetSeatedBookingOutput_2024_08_13'
              - $ref: >-
                  #/components/schemas/GetRecurringSeatedBookingOutput_2024_08_13
          description: >-
            Array of booking data, which can contain either BookingOutput
            objects or RecurringBookingOutput objects
        pagination:
          $ref: '#/components/schemas/CursorPaginationMeta_2026_05_01'
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
    CursorPaginationMeta_2026_05_01:
      type: object
      properties:
        nextCursor:
          type: string
          nullable: true
          description: >-
            Opaque cursor to fetch the next page. Pass this value as the
            `cursor` query parameter on the next request. `null` when `hasMore`
            is `false`.
          example: >-
            eyJ2IjoxLCJzb3J0VXVpZCI6IjAxOGY0YzJlLTNmMWEtN2FiYy05ZGVmLTAxMjM0NTY3ODlhYiJ9
        hasMore:
          type: boolean
          description: Whether more pages are available after this one.
          example: true
      required:
        - nextCursor
        - hasMore
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