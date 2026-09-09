> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Save an ICS feed

> If accessed using an OAuth access token, the `APPS_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/calendars/ics-feed/save
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
  /v2/calendars/ics-feed/save:
    post:
      tags:
        - Calendars
      summary: Save an ICS feed
      description: >-
        If accessed using an OAuth access token, the `APPS_WRITE` scope is
        required.
      operationId: CalendarsController_createIcsFeed
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
              $ref: '#/components/schemas/CreateIcsFeedInputDto'
      responses:
        '201':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateIcsFeedOutputResponseDto'
components:
  schemas:
    CreateIcsFeedInputDto:
      type: object
      properties:
        urls:
          type: array
          minItems: 1
          example:
            - https://cal.com/ics/feed.ics
          description: An array of ICS URLs
          items:
            type: string
            example: https://cal.com/ics/feed.ics
        readOnly:
          type: boolean
          default: true
          example: false
          description: Whether to allowing writing to the calendar or not
      required:
        - urls
    CreateIcsFeedOutputResponseDto:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/CreateIcsFeedOutput'
      required:
        - status
        - data
    CreateIcsFeedOutput:
      type: object
      properties:
        id:
          type: number
          example: 1234567890
          description: The id of the calendar credential
        type:
          type: string
          example: ics-feed_calendar
          description: The type of the calendar
        userId:
          type: integer
          nullable: true
          example: 1234567890
          description: The user id of the user that created the calendar
        teamId:
          type: integer
          nullable: true
          example: 1234567890
          description: The team id of the user that created the calendar
        appId:
          type: string
          nullable: true
          example: ics-feed
          description: The slug of the calendar
        invalid:
          type: boolean
          nullable: true
          example: false
          description: Whether the calendar credentials are valid or not
      required:
        - id
        - type
        - userId
        - teamId
        - appId
        - invalid

````