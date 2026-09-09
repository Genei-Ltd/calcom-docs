> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a phone call

> If accessed using an OAuth access token, the `TEAM_EVENT_TYPE_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/teams/{teamId}/event-types/{eventTypeId}/create-phone-call
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
  /v2/teams/{teamId}/event-types/{eventTypeId}/create-phone-call:
    post:
      tags:
        - Teams / Event Types
      summary: Create a phone call
      description: >-
        If accessed using an OAuth access token, the `TEAM_EVENT_TYPE_WRITE`
        scope is required.
      operationId: TeamsEventTypesController_createPhoneCall
      parameters:
        - name: teamId
          required: true
          in: path
          schema:
            type: number
        - name: eventTypeId
          required: true
          in: path
          schema:
            type: number
        - name: Authorization
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreatePhoneCallInput'
      responses:
        '201':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreatePhoneCallOutput'
components:
  schemas:
    CreatePhoneCallInput:
      type: object
      properties:
        yourPhoneNumber:
          type: string
          pattern: /^\+[1-9]\d{1,14}$/
          description: Your phone number
        numberToCall:
          type: string
          pattern: /^\+[1-9]\d{1,14}$/
          description: Number to call
        calApiKey:
          type: string
          description: CAL API Key
        enabled:
          type: boolean
          default: true
          description: Enabled status
        templateType:
          default: CUSTOM_TEMPLATE
          enum:
            - CHECK_IN_APPOINTMENT
            - CUSTOM_TEMPLATE
          type: string
          description: Template type
        schedulerName:
          type: string
          description: Scheduler name
        guestName:
          type: string
          description: Guest name
        guestEmail:
          type: string
          description: Guest email
        guestCompany:
          type: string
          description: Guest company
        beginMessage:
          type: string
          description: Begin message
        generalPrompt:
          type: string
          description: General prompt
      required:
        - yourPhoneNumber
        - numberToCall
        - calApiKey
        - enabled
        - templateType
    CreatePhoneCallOutput:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          $ref: '#/components/schemas/Data'
      required:
        - status
        - data
    Data:
      type: object
      properties:
        callId:
          type: string
        agentId:
          type: string
      required:
        - callId

````