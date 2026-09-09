> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Disconnect a calendar

> If accessed using an OAuth access token, the `APPS_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/calendars/{calendar}/disconnect
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
  /v2/calendars/{calendar}/disconnect:
    post:
      tags:
        - Calendars
      summary: Disconnect a calendar
      description: >-
        If accessed using an OAuth access token, the `APPS_WRITE` scope is
        required.
      operationId: CalendarsController_deleteCalendarCredentials
      parameters:
        - name: calendar
          required: true
          in: path
          schema:
            enum:
              - apple
              - google
              - office365
            type: string
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
              $ref: '#/components/schemas/DeleteCalendarCredentialsInputBodyDto'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/DeletedCalendarCredentialsOutputResponseDto
components:
  schemas:
    DeleteCalendarCredentialsInputBodyDto:
      type: object
      properties:
        id:
          type: integer
          example: 10
          description: >-
            Credential ID of the calendar to delete, as returned by the
            /calendars endpoint
      required:
        - id
    DeletedCalendarCredentialsOutputResponseDto:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          $ref: '#/components/schemas/DeletedCalendarCredentialsOutputDto'
      required:
        - status
        - data
    DeletedCalendarCredentialsOutputDto:
      type: object
      properties:
        id:
          type: number
        type:
          type: string
        userId:
          type: number
          nullable: true
        teamId:
          type: number
          nullable: true
        appId:
          type: string
          nullable: true
        invalid:
          type: boolean
          nullable: true
      required:
        - id
        - type
        - userId
        - teamId
        - appId
        - invalid

````