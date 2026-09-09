> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all bookings for an organization user

> If accessed using an OAuth access token, the `ORG_BOOKING_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/organizations/{orgId}/users/{userId}/bookings
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
  /v2/organizations/{orgId}/users/{userId}/bookings:
    get:
      tags:
        - Orgs / Users / Bookings
      summary: Get all bookings for an organization user
      description: >-
        If accessed using an OAuth access token, the `ORG_BOOKING_READ` scope is
        required.
      operationId: OrganizationsUsersBookingsController_getOrganizationUserBookings
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
        - name: orgId
          required: true
          in: path
          schema:
            type: number
        - name: userId
          required: true
          in: path
          schema:
            type: number
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
        - name: teamsIds
          required: false
          in: query
          description: >-
            Filter bookings by team ids that user is part of. Team ids must be
            separated by a comma.
          schema:
            minItems: 1
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
      responses:
        '200':
          description: ''

````