> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all the recordings for the booking

> Fetches all the recordings for the booking `:bookingUid`. Requires authentication and proper authorization. Access is granted if you are the booking organizer, team admin or org admin/owner.

    <Note>cal-api-version: `2026-02-25` is required in the request header.</Note>

If accessed using an OAuth access token, the `BOOKING_READ` scope is required.
    



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/bookings/{bookingUid}/recordings
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
  /v2/bookings/{bookingUid}/recordings:
    get:
      tags:
        - Bookings
      summary: Get all the recordings for the booking
      description: >-
        Fetches all the recordings for the booking `:bookingUid`. Requires
        authentication and proper authorization. Access is granted if you are
        the booking organizer, team admin or org admin/owner.

            <Note>cal-api-version: `2026-02-25` is required in the request header.</Note>

        If accessed using an OAuth access token, the `BOOKING_READ` scope is
        required.
            
      operationId: BookingsController_2026_02_25_getBookingRecordings
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
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetBookingRecordingsOutput'
components:
  schemas:
    GetBookingRecordingsOutput:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          type: array
          items:
            $ref: '#/components/schemas/RecordingItem'
      required:
        - status
        - data
    RecordingItem:
      type: object
      properties:
        id:
          type: string
          example: '1234567890'
        roomName:
          type: string
          example: daily-video-room-123
        startTs:
          type: number
          example: 1678901234
        status:
          type: string
          example: completed
        maxParticipants:
          type: number
          example: 10
        duration:
          type: number
          example: 3600
        shareToken:
          type: string
          example: share-token-123
        downloadLink:
          type: string
          nullable: true
          example: https://cal-video-recordings.s3.us-east-2.amazonaws.com/meetco/123s
        error:
          type: string
          nullable: true
          example: Error message
      required:
        - id
        - roomName
        - startTs
        - status
        - duration
        - shareToken

````