> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Refresh API Key

> Generate a new API key and delete the current one. Provide API key to refresh as a Bearer token in the Authorization header (e.g. "Authorization: Bearer <apiKey>").



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/api-keys/refresh
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
  /v2/api-keys/refresh:
    post:
      tags:
        - Api Keys
      summary: Refresh API Key
      description: >-
        Generate a new API key and delete the current one. Provide API key to
        refresh as a Bearer token in the Authorization header (e.g.
        "Authorization: Bearer <apiKey>").
      operationId: ApiKeysController_refresh
      parameters:
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
              $ref: '#/components/schemas/RefreshApiKeyInput'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RefreshApiKeyOutput'
components:
  schemas:
    RefreshApiKeyInput:
      type: object
      properties:
        apiKeyDaysValid:
          type: number
          minimum: 1
          description: >-
            For how many days is managed organization api key valid. Defaults to
            30 days.
          example: 60
          default: 30
        apiKeyNeverExpires:
          type: boolean
          description: If true, organization api key never expires.
          example: true
    RefreshApiKeyOutput:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          $ref: '#/components/schemas/ApiKeyOutput'
      required:
        - status
        - data
    ApiKeyOutput:
      type: object
      properties:
        apiKey:
          type: string
      required:
        - apiKey

````