> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Reassign a booking to auto-selected host

> Currently only supports reassigning host for round robin bookings. The provided authorization header refers to the owner of the booking.

       <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>

If accessed using an OAuth access token, the `BOOKING_WRITE` scope is required.
      



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/bookings/{bookingUid}/reassign
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
  /v2/bookings/{bookingUid}/reassign:
    post:
      tags:
        - Bookings
      summary: Reassign a booking to auto-selected host
      description: >-
        Currently only supports reassigning host for round robin bookings. The
        provided authorization header refers to the owner of the booking.

               <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>

        If accessed using an OAuth access token, the `BOOKING_WRITE` scope is
        required.
              
      operationId: BookingsController_2026_02_25_reassignBooking
      parameters:
        - name: cal-api-version
          in: header
          description: Must be set to 2026-02-25.
          required: true
          schema:
            type: string
            example: '2026-02-25'
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
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ReassignBookingOutput_2024_08_13'
components:
  schemas:
    ReassignBookingOutput_2024_08_13:
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
            - $ref: '#/components/schemas/ReassignBookingOutput_2024_08_13'
              title: Reassigned Booking
          description: >-
            Booking data, which can be either a ReassignAutoBookingOutput object
            or a ReassignManualBookingOutput object
          allOf:
            - $ref: '#/components/schemas/ReassignBookingOutput_2024_08_13'
      required:
        - status
        - data

````