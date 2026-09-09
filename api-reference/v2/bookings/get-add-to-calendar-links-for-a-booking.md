> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get 'Add to Calendar' links for a booking

> Retrieve calendar links for a booking that can be used to add the event to various calendar services. Returns links for Google Calendar, Microsoft Office, Microsoft Outlook, and a downloadable ICS file.

      <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>

If accessed using an OAuth access token, the `BOOKING_READ` scope is required.
      



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/bookings/{bookingUid}/calendar-links
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
  /v2/bookings/{bookingUid}/calendar-links:
    get:
      tags:
        - Bookings
      summary: Get 'Add to Calendar' links for a booking
      description: >-
        Retrieve calendar links for a booking that can be used to add the event
        to various calendar services. Returns links for Google Calendar,
        Microsoft Office, Microsoft Outlook, and a downloadable ICS file.

              <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>

        If accessed using an OAuth access token, the `BOOKING_READ` scope is
        required.
              
      operationId: BookingsController_2026_02_25_getCalendarLinks
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
                $ref: '#/components/schemas/CalendarLinksOutput_2024_08_13'
components:
  schemas:
    CalendarLinksOutput_2024_08_13:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          description: The status of the request, always 'success' for successful responses
          example: success
        data:
          description: Calendar links for the booking
          type: array
          items:
            $ref: '#/components/schemas/CalendarLink'
      required:
        - status
        - data
    CalendarLink:
      type: object
      properties:
        label:
          type: string
          description: The label of the calendar link
        link:
          type: string
          description: The link to the calendar
      required:
        - label
        - link

````