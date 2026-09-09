> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update destination calendars

> If accessed using an OAuth access token, the `APPS_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json put /v2/destination-calendars
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
  /v2/destination-calendars:
    put:
      tags:
        - Destination Calendars
      summary: Update destination calendars
      description: >-
        If accessed using an OAuth access token, the `APPS_WRITE` scope is
        required.
      operationId: DestinationCalendarsController_updateDestinationCalendars
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
              $ref: '#/components/schemas/DestinationCalendarsInputBodyDto'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DestinationCalendarsOutputResponseDto'
components:
  schemas:
    DestinationCalendarsInputBodyDto:
      type: object
      properties:
        integration:
          enum:
            - apple_calendar
            - google_calendar
            - office365_calendar
          type: string
          example: apple_calendar
          description: >-
            The calendar service you want to integrate, as returned by the
            /calendars endpoint
        externalId:
          type: string
          example: >-
            https://caldav.icloud.com/26962146906/calendars/1644422A-1945-4438-BBC0-4F0Q23A57R7S/
          description: >-
            Unique identifier used to represent the specific calendar, as
            returned by the /calendars endpoint
        delegationCredentialId:
          type: string
      required:
        - integration
        - externalId
    DestinationCalendarsOutputResponseDto:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/DestinationCalendarsOutputDto'
      required:
        - status
        - data
    DestinationCalendarsOutputDto:
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