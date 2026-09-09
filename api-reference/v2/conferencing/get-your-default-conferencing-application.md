> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get your default conferencing application

> If accessed using an OAuth access token, the `APPS_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/conferencing/default
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
  /v2/conferencing/default:
    get:
      tags:
        - Conferencing
      summary: Get your default conferencing application
      description: >-
        If accessed using an OAuth access token, the `APPS_READ` scope is
        required.
      operationId: ConferencingController_getDefault
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
                $ref: >-
                  #/components/schemas/GetDefaultConferencingAppOutputResponseDto
components:
  schemas:
    GetDefaultConferencingAppOutputResponseDto:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/DefaultConferencingAppsOutputDto'
      required:
        - status
    DefaultConferencingAppsOutputDto:
      type: object
      properties:
        appSlug:
          type: string
        appLink:
          type: string

````