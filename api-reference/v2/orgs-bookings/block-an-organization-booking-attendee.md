> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Block an organization booking attendee

> Add the email or domain of a booking attendee to the organization blocklist. All matching upcoming bookings in the organization are silently cancelled. If accessed using an OAuth access token, the `ORG_BOOKING_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/organizations/{orgId}/bookings/block
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
  /v2/organizations/{orgId}/bookings/block:
    post:
      tags:
        - Orgs / Bookings
      summary: Block an organization booking attendee
      description: >-
        Add the email or domain of a booking attendee to the organization
        blocklist. All matching upcoming bookings in the organization are
        silently cancelled. If accessed using an OAuth access token, the
        `ORG_BOOKING_WRITE` scope is required.
      operationId: OrganizationsBookingsController_blockOrgBooking
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
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/BlockOrgBookingInput'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BlockOrgBookingOutput'
components:
  schemas:
    BlockOrgBookingInput:
      type: object
      properties:
        bookingUid:
          type: string
          description: The UID of the booking whose attendee should be blocked
          example: booking-uid-123
        blockType:
          enum:
            - EMAIL
            - DOMAIN
          type: string
          description: >-
            Whether to block by email or domain. EMAIL blocks the specific
            booker email. DOMAIN blocks all emails from the same domain.
          example: EMAIL
      required:
        - bookingUid
        - blockType
    BlockOrgBookingOutput:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          $ref: '#/components/schemas/BlockOrgBookingData'
      required:
        - status
        - data
    BlockOrgBookingData:
      type: object
      properties:
        success:
          type: boolean
          description: Whether the operation was successful
          example: true
        message:
          type: string
          description: A human-readable message describing the result
          example: Added to blocklist and 3 bookings cancelled
        bookingUid:
          type: string
          description: The UID of the booking whose attendee was blocked
          example: booking-uid-123
        cancelledCount:
          type: number
          description: The number of bookings cancelled
          example: 3
        blockedValue:
          type: string
          description: The email or domain that was added to the blocklist
          example: spammer@example.com
      required:
        - success
        - message
        - bookingUid
        - cancelledCount
        - blockedValue

````