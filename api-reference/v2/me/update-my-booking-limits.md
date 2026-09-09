> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update my booking limits

> Partially updates the authenticated user's global booking limits. Only fields present in the request body are changed; omit a field to leave it untouched, or set it to null to remove that limit. Only available to organization members — non-org accounts receive a 403. If accessed using an OAuth access token, the `PROFILE_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json patch /v2/me/booking-limits
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
  /v2/me/booking-limits:
    patch:
      tags:
        - Me
      summary: Update my booking limits
      description: >-
        Partially updates the authenticated user's global booking limits. Only
        fields present in the request body are changed; omit a field to leave it
        untouched, or set it to null to remove that limit. Only available to
        organization members — non-org accounts receive a 403. If accessed using
        an OAuth access token, the `PROFILE_WRITE` scope is required.
      operationId: MeController_updateMyBookingLimits
      parameters:
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
              $ref: '#/components/schemas/UpdateBookingLimitsInput'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UpdateBookingLimitsOutput'
components:
  schemas:
    UpdateBookingLimitsInput:
      type: object
      properties:
        perDay:
          type: number
          nullable: true
          minimum: 1
          description: Maximum number of bookings per day. Pass null to remove this limit.
          example: 4
        perWeek:
          type: number
          nullable: true
          minimum: 1
          description: Maximum number of bookings per week. Pass null to remove this limit.
          example: 20
        perMonth:
          type: number
          nullable: true
          minimum: 1
          description: >-
            Maximum number of bookings per month. Pass null to remove this
            limit.
          example: 60
        perYear:
          type: number
          nullable: true
          minimum: 1
          description: Maximum number of bookings per year. Pass null to remove this limit.
          example: 500
    UpdateBookingLimitsOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/BookingLimitsOutput'
      required:
        - status
        - data
    BookingLimitsOutput:
      type: object
      properties:
        perDay:
          type: number
          nullable: true
          example: 4
        perWeek:
          type: number
          nullable: true
          example: 20
        perMonth:
          type: number
          example: 60
          nullable: true
        perYear:
          type: number
          nullable: true
          example: 500
      required:
        - perDay
        - perWeek
        - perMonth
        - perYear

````