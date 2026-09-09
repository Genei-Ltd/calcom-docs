> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a selected calendar

> If accessed using an OAuth access token, the `APPS_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json delete /v2/selected-calendars
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
    delete:
      tags:
        - Selected Calendars
      summary: Delete a selected calendar
      description: >-
        If accessed using an OAuth access token, the `APPS_WRITE` scope is
        required.
      operationId: SelectedCalendarsController_deleteSelectedCalendar
      parameters:
        - name: Authorization
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_, managed user access token, or OAuth access token
          required: true
          schema:
            type: string
        - name: integration
          required: true
          in: query
          schema:
            type: string
        - name: externalId
          required: true
          in: query
          schema:
            type: string
        - name: credentialId
          required: true
          in: query
          schema:
            type: string
        - name: delegationCredentialId
          required: false
          in: query
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SelectedCalendarOutputResponseDto'
components:
  schemas:
    SelectedCalendarOutputResponseDto:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
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