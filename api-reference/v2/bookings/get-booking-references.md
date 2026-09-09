> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get booking references

> <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>

If accessed using an OAuth access token, the `BOOKING_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/bookings/{bookingUid}/references
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
  /v2/bookings/{bookingUid}/references:
    get:
      tags:
        - Bookings
      summary: Get booking references
      description: >-
        <Note>Please make sure to pass in the cal-api-version header value as
        mentioned in the Headers section. Not passing the correct value will
        default to an older version of this endpoint.</Note>


        If accessed using an OAuth access token, the `BOOKING_READ` scope is
        required.
      operationId: BookingsController_2026_02_25_getBookingReferences
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
        - name: type
          required: false
          in: query
          description: Filter booking references by type
          schema:
            example: google_calendar
            enum:
              - google_calendar
              - office365_calendar
              - daily_video
              - google_video
              - office365_video
              - zoom_video
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
                $ref: '#/components/schemas/BookingReferencesOutput_2024_08_13'
components:
  schemas:
    BookingReferencesOutput_2024_08_13:
      type: object
      properties:
        status:
          type: string
          description: The status of the request, always 'success' for successful responses
          example: success
          enum:
            - success
            - error
        data:
          description: Booking References
          type: array
          items:
            $ref: '#/components/schemas/BookingReference'
      required:
        - status
        - data
    BookingReference:
      type: object
      properties:
        type:
          type: string
          description: The type of the booking reference
        eventUid:
          type: string
          description: The event uid of the booking
        destinationCalendarId:
          type: string
          nullable: true
          description: The id of the calendar the event is created in
        id:
          type: number
          description: The id of the booking reference
      required:
        - type
        - eventUid
        - destinationCalendarId
        - id

````