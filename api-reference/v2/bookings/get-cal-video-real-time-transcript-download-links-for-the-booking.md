> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Cal Video real time transcript download links for the booking

> Fetches all the transcript download links for the booking `:bookingUid`

    <Note>
    Transcripts are generated when clicking "Transcribe" during a Cal Video meeting. Download links are valid for 1 hour only - make a new request to generate fresh links after expiration.

    Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.
    </Note>

If accessed using an OAuth access token, the `BOOKING_READ` scope is required.
    



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/bookings/{bookingUid}/transcripts
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
  /v2/bookings/{bookingUid}/transcripts:
    get:
      tags:
        - Bookings
      summary: Get Cal Video real time transcript download links for the booking
      description: >-
        Fetches all the transcript download links for the booking `:bookingUid`

            <Note>
            Transcripts are generated when clicking "Transcribe" during a Cal Video meeting. Download links are valid for 1 hour only - make a new request to generate fresh links after expiration.

            Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.
            </Note>

        If accessed using an OAuth access token, the `BOOKING_READ` scope is
        required.
            
      operationId: BookingsController_2026_02_25_getBookingTranscripts
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
                $ref: '#/components/schemas/GetBookingTranscriptsOutput'
        '429':
          description: >-
            Conferencing provider rate limit exceeded. Try again later. The
            `Retry-After` response header carries the number of seconds to wait
            before retrying.
components:
  schemas:
    GetBookingTranscriptsOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          example:
            - https://transcript1.com
            - https://transcript2.com
          type: array
          items:
            type: string
      required:
        - status
        - data

````