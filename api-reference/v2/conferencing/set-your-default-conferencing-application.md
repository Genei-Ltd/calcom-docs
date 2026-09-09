> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Set your default conferencing application

> If accessed using an OAuth access token, the `APPS_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/conferencing/{app}/default
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
  /v2/conferencing/{app}/default:
    post:
      tags:
        - Conferencing
      summary: Set your default conferencing application
      description: >-
        If accessed using an OAuth access token, the `APPS_WRITE` scope is
        required.
      operationId: ConferencingController_default
      parameters:
        - name: app
          required: true
          in: path
          description: Conferencing application type
          schema:
            enum:
              - google-meet
              - zoom
              - msteams
              - daily-video
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
                $ref: >-
                  #/components/schemas/SetDefaultConferencingAppOutputResponseDto
components:
  schemas:
    SetDefaultConferencingAppOutputResponseDto:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
      required:
        - status

````