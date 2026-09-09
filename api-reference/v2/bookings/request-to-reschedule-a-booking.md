> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Request to reschedule a booking

> Request to reschedule a booking. The booking will be cancelled and the attendee will receive an email with a link to reschedule.

    <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>

If accessed using an OAuth access token, the `BOOKING_WRITE` scope is required.
    



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/bookings/{bookingUid}/request-reschedule
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
  /v2/bookings/{bookingUid}/request-reschedule:
    post:
      tags:
        - Bookings
      summary: Request to reschedule a booking
      description: >-
        Request to reschedule a booking. The booking will be cancelled and the
        attendee will receive an email with a link to reschedule.

            <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>

        If accessed using an OAuth access token, the `BOOKING_WRITE` scope is
        required.
            
      operationId: BookingsController_2026_02_25_requestReschedule
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
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RequestRescheduleInput_2024_08_13'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RequestRescheduleOutput_2024_08_13'
components:
  schemas:
    RequestRescheduleInput_2024_08_13:
      type: object
      properties:
        rescheduleReason:
          type: string
          example: I need to reschedule due to a conflict
          description: Reason for requesting to reschedule the booking
    RequestRescheduleOutput_2024_08_13:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
      required:
        - status

````