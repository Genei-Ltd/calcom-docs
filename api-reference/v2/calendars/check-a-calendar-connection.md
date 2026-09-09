> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Check a calendar connection

> If accessed using an OAuth access token, the `APPS_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/calendars/{calendar}/check
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
  /v2/calendars/{calendar}/check:
    get:
      tags:
        - Calendars
      summary: Check a calendar connection
      description: >-
        If accessed using an OAuth access token, the `APPS_READ` scope is
        required.
      operationId: CalendarsController_check
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
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object

````