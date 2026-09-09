> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a specific attendee for a booking

> Retrieve a specific attendee by their ID for a booking identified by its UID.
        
      <Note>The cal-api-version header is required for this endpoint. Without it, the request will fail with a 404 error.</Note>

If accessed using an OAuth access token, the `BOOKING_READ` scope is required.
      



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/bookings/{bookingUid}/attendees/{attendeeId}
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
  /v2/bookings/{bookingUid}/attendees/{attendeeId}:
    get:
      tags:
        - Bookings / Attendees
      summary: Get a specific attendee for a booking
      description: >-
        Retrieve a specific attendee by their ID for a booking identified by its
        UID.
                
              <Note>The cal-api-version header is required for this endpoint. Without it, the request will fail with a 404 error.</Note>

        If accessed using an OAuth access token, the `BOOKING_READ` scope is
        required.
              
      operationId: BookingAttendeesController_2024_08_13_getBookingAttendee
      parameters:
        - name: cal-api-version
          in: header
          description: >-
            Must be set to 2024-08-13. This header is required as this endpoint
            does not exist in older API versions.
          required: true
          schema:
            type: string
        - name: bookingUid
          required: true
          in: path
          schema:
            type: string
        - name: attendeeId
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
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetBookingAttendeeOutput_2024_08_13'
components:
  schemas:
    GetBookingAttendeeOutput_2024_08_13:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          $ref: '#/components/schemas/BookingAttendeeWithId_2024_08_13'
      required:
        - status
        - data
    BookingAttendeeWithId_2024_08_13:
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
        id:
          type: number
          example: 251
      required:
        - name
        - email
        - displayEmail
        - timeZone
        - absent
        - id

````