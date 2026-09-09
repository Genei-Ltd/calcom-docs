> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Add a selected calendar

> If accessed using an OAuth access token, the `APPS_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/selected-calendars
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
  /v2/selected-calendars:
    post:
      tags:
        - Selected Calendars
      summary: Add a selected calendar
      description: >-
        If accessed using an OAuth access token, the `APPS_WRITE` scope is
        required.
      operationId: SelectedCalendarsController_addSelectedCalendar
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
              $ref: '#/components/schemas/SelectedCalendarsInputDto'
      responses:
        '201':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SelectedCalendarOutputResponseDto'
components:
  schemas:
    SelectedCalendarsInputDto:
      type: object
      properties:
        integration:
          type: string
        externalId:
          type: string
        credentialId:
          type: number
        delegationCredentialId:
          type: string
      required:
        - integration
        - externalId
        - credentialId
    SelectedCalendarOutputResponseDto:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          $ref: '#/components/schemas/SelectedCalendarOutputDto'
      required:
        - status
        - data
    SelectedCalendarOutputDto:
      type: object
      properties:
        userId:
          type: number
        integration:
          type: string
        externalId:
          type: string
        credentialId:
          type: number
          nullable: true
      required:
        - userId
        - integration
        - externalId
        - credentialId

````