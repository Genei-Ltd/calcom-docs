> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Video Meeting Sessions. Only supported for Cal Video

> Requires authentication and proper authorization. Access is granted if you are the booking organizer, team admin or org admin/owner.

    <Note>cal-api-version: `2026-02-25` is required in the request header.</Note>

    <Note>This endpoint is rate-limited to 60 requests per minute per caller (per API key, access token, OAuth client, or IP). Exceeding the limit returns a 429 response and blocks further calls for 60 seconds.</Note>

    <Note>If the upstream conferencing provider rate-limits the request, this endpoint responds with HTTP 429 and a `Retry-After` header carrying the number of seconds to wait before retrying. Clients should honor this hint.</Note>

If accessed using an OAuth access token, the `BOOKING_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/bookings/{bookingUid}/conferencing-sessions
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
  /v2/bookings/{bookingUid}/conferencing-sessions:
    get:
      tags:
        - Bookings
      summary: Get Video Meeting Sessions. Only supported for Cal Video
      description: >-
        Requires authentication and proper authorization. Access is granted if
        you are the booking organizer, team admin or org admin/owner.

            <Note>cal-api-version: `2026-02-25` is required in the request header.</Note>

            <Note>This endpoint is rate-limited to 60 requests per minute per caller (per API key, access token, OAuth client, or IP). Exceeding the limit returns a 429 response and blocks further calls for 60 seconds.</Note>

            <Note>If the upstream conferencing provider rate-limits the request, this endpoint responds with HTTP 429 and a `Retry-After` header carrying the number of seconds to wait before retrying. Clients should honor this hint.</Note>

        If accessed using an OAuth access token, the `BOOKING_READ` scope is
        required.
      operationId: BookingsController_2026_02_25_getVideoSessions
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
                $ref: '#/components/schemas/GetBookingVideoSessionsOutput'
        '429':
          description: >-
            Rate limit exceeded — either the per-caller throttle or the upstream
            conferencing provider. The `Retry-After` response header carries the
            number of seconds to wait before retrying.
components:
  schemas:
    GetBookingVideoSessionsOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          type: array
          items:
            $ref: '#/components/schemas/CalMeetingSession'
      required:
        - status
        - data
    CalMeetingSession:
      type: object
      properties:
        id:
          type: string
          example: session123
        room:
          type: string
          example: daily-video-room-123
        startTime:
          type: number
          example: 1678901234
        duration:
          type: number
          example: 3600
        ongoing:
          type: boolean
          example: false
        maxParticipants:
          type: number
          example: 10
        participants:
          type: array
          items:
            $ref: '#/components/schemas/CalMeetingParticipant'
      required:
        - id
        - room
        - startTime
        - duration
        - ongoing
        - maxParticipants
        - participants
    CalMeetingParticipant:
      type: object
      properties:
        userId:
          type: string
          nullable: true
          example: user123
        userName:
          type: string
          nullable: true
          example: John Doe
        joinTime:
          type: number
          example: 1678901234
        duration:
          type: number
          example: 3600
      required:
        - userId
        - userName
        - joinTime
        - duration

````