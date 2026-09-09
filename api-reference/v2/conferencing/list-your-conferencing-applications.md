> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List your conferencing applications

> If accessed using an OAuth access token, the `APPS_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/conferencing
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
  /v2/conferencing:
    get:
      tags:
        - Conferencing
      summary: List your conferencing applications
      description: >-
        If accessed using an OAuth access token, the `APPS_READ` scope is
        required.
      operationId: ConferencingController_listInstalledConferencingApps
      parameters:
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
                $ref: '#/components/schemas/ConferencingAppsOutputResponseDto'
components:
  schemas:
    ConferencingAppsOutputResponseDto:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
        data:
          type: array
          items:
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