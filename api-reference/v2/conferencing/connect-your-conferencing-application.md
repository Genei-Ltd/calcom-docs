> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect your conferencing application

> If accessed using an OAuth access token, the `APPS_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/conferencing/{app}/connect
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
  /v2/conferencing/{app}/connect:
    post:
      tags:
        - Conferencing
      summary: Connect your conferencing application
      description: >-
        If accessed using an OAuth access token, the `APPS_WRITE` scope is
        required.
      operationId: ConferencingController_connect
      parameters:
        - name: app
          required: true
          in: path
          description: Conferencing application type
          schema:
            enum:
              - google-meet
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
                $ref: '#/components/schemas/ConferencingAppOutputResponseDto'
components:
  schemas:
    ConferencingAppOutputResponseDto:
      type: object
      properties:
        status:
          type: string
          enum:
            - success
            - error
        data:
          $ref: '#/components/schemas/ConferencingAppsOutputDto'
      required:
        - status
        - data
    ConferencingAppsOutputDto:
      type: object
      properties:
        id:
          type: number
          description: Id of the conferencing app credentials
        type:
          type: string
          example: google_video
          description: Type of conferencing app
        userId:
          type: number
          description: Id of the user associated to the conferencing app
        invalid:
          type: boolean
          nullable: true
          example: true
          description: Whether if the connection is working or not.
      required:
        - id
        - type
        - userId

````