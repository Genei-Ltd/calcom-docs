> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Reassign a booking to a specific host

> Currently only supports reassigning host for round robin bookings. The provided authorization header refers to the owner of the booking.

      <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>

If accessed using an OAuth access token, the `BOOKING_WRITE` scope is required.
      



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/bookings/{bookingUid}/reassign/{userId}
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
  /v2/bookings/{bookingUid}/reassign/{userId}:
    post:
      tags:
        - Bookings
      summary: Reassign a booking to a specific host
      description: >-
        Currently only supports reassigning host for round robin bookings. The
        provided authorization header refers to the owner of the booking.

              <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>

        If accessed using an OAuth access token, the `BOOKING_WRITE` scope is
        required.
              
      operationId: BookingsController_2026_02_25_reassignBookingToUser
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
        - name: userId
          required: true
          in: path
          schema:
            type: number
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
              $ref: '#/components/schemas/ReassignToUserBookingInput_2024_08_13'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ReassignBookingOutput_2024_08_13'
components:
  schemas:
    ReassignToUserBookingInput_2024_08_13:
      type: object
      properties:
        reason:
          type: string
          example: Host has to take another call
          description: Reason for reassigning the booking
    ReassignBookingOutput_2024_08_13:
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
            - $ref: '#/components/schemas/ReassignBookingOutput_2024_08_13'
          description: >-
            Booking data, which can be either a ReassignAutoBookingOutput object
            or a ReassignManualBookingOutput object
          allOf:
            - $ref: '#/components/schemas/ReassignBookingOutput_2024_08_13'
      required:
        - status
        - data

````