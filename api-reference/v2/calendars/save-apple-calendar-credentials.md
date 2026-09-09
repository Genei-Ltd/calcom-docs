> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Save Apple calendar credentials

> If accessed using an OAuth access token, the `APPS_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/calendars/{calendar}/credentials
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
  /v2/calendars/{calendar}/credentials:
    post:
      tags:
        - Calendars
      summary: Save Apple calendar credentials
      description: >-
        If accessed using an OAuth access token, the `APPS_WRITE` scope is
        required.
      operationId: CalendarsController_syncCredentials
      parameters:
        - name: calendar
          required: true
          in: path
          schema:
            enum:
              - apple
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
              $ref: '#/components/schemas/CreateCalendarCredentialsInput'
      responses:
        '201':
          description: ''
components:
  schemas:
    CreateCalendarCredentialsInput:
      type: object
      properties:
        username:
          type: string
          minLength: 1
        password:
          type: string
          minLength: 1
      required:
        - username
        - password

````