> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get OAuth conferencing app auth URL

> If accessed using an OAuth access token, the `APPS_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/conferencing/{app}/oauth/auth-url
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
  /v2/conferencing/{app}/oauth/auth-url:
    get:
      tags:
        - Conferencing
      summary: Get OAuth conferencing app auth URL
      description: >-
        If accessed using an OAuth access token, the `APPS_WRITE` scope is
        required.
      operationId: ConferencingController_redirect
      parameters:
        - name: Authorization
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_, managed user access token, or OAuth access token
          required: true
          schema:
            type: string
        - name: app
          required: true
          in: path
          description: Conferencing application type
          schema:
            enum:
              - zoom
              - msteams
            type: string
        - name: returnTo
          required: true
          in: query
          schema:
            type: string
        - name: onErrorReturnTo
          required: true
          in: query
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetConferencingAppsOauthUrlResponseDto'
components:
  schemas:
    GetConferencingAppsOauthUrlResponseDto:
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