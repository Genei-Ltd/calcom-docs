> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get my booking limits

> Returns the authenticated user's global booking limits. Unset bounds are returned as null. Only available to organization members — non-org accounts receive a 403. If accessed using an OAuth access token, the `PROFILE_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/me/booking-limits
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
    get:
      tags:
        - Me
      summary: Get my booking limits
      description: >-
        Returns the authenticated user's global booking limits. Unset bounds are
        returned as null. Only available to organization members — non-org
        accounts receive a 403. If accessed using an OAuth access token, the
        `PROFILE_READ` scope is required.
      operationId: MeController_getMyBookingLimits
      parameters:
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
                $ref: '#/components/schemas/GetBookingLimitsOutput'
components:
  schemas:
    GetBookingLimitsOutput:
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