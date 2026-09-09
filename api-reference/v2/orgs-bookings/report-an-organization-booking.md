> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Report an organization booking

> Report a booking within the organization. A booking report is created and the reported booking along with other matching upcoming bookings are silently cancelled. If accessed using an OAuth access token, the `ORG_BOOKING_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/organizations/{orgId}/bookings/report
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
  /v2/organizations/{orgId}/bookings/report:
    post:
      tags:
        - Orgs / Bookings
      summary: Report an organization booking
      description: >-
        Report a booking within the organization. A booking report is created
        and the reported booking along with other matching upcoming bookings are
        silently cancelled. If accessed using an OAuth access token, the
        `ORG_BOOKING_WRITE` scope is required.
      operationId: OrganizationsBookingsController_reportOrgBooking
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
              $ref: '#/components/schemas/ReportOrgBookingInput'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ReportOrgBookingOutput'
components:
  schemas:
    ReportOrgBookingInput:
      type: object
      properties:
        bookingUid:
          type: string
          description: The UID of the booking to report
          example: booking-uid-123
        reason:
          enum:
            - SPAM
            - UNWANTED
            - DONT_KNOW_PERSON
            - OTHER
          type: string
          description: The reason for reporting the booking
          example: SPAM
        description:
          type: string
          description: Additional description for the report
        reportType:
          enum:
            - EMAIL
            - DOMAIN
          type: string
          description: >-
            Whether to report by email or domain. EMAIL targets the specific
            booker email. DOMAIN targets all emails from the same domain.
          example: EMAIL
      required:
        - bookingUid
        - reason
        - reportType
    ReportOrgBookingOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/ReportOrgBookingData'
      required:
        - status
        - data
    ReportOrgBookingData:
      type: object
      properties:
        success:
          type: boolean
          description: Whether the operation was successful
          example: true
        message:
          type: string
          description: A human-readable message describing the result
          example: Booking reported and cancelled successfully
        bookingUid:
          type: string
          description: The UID of the reported booking
          example: booking-uid-123
        reportedCount:
          type: number
          description: The number of booking reports created
          example: 1
        cancelledCount:
          type: number
          description: The number of bookings cancelled
          example: 3
      required:
        - success
        - message
        - bookingUid
        - reportedCount
        - cancelledCount

````