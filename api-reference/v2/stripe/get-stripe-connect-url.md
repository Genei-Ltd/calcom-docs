> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Stripe connect URL



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/stripe/connect
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
  /v2/stripe/connect:
    get:
      tags:
        - Stripe
      summary: Get Stripe connect URL
      operationId: StripeController_redirect
      parameters:
        - name: Authorization
          required: true
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_ or managed user access token
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/StripConnectOutputResponseDto'
components:
  schemas:
    StripConnectOutputResponseDto:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/StripConnectOutputDto'
      required:
        - status
        - data
    StripConnectOutputDto:
      type: object
      properties:
        authUrl:
          type: string
      required:
        - authUrl

````