> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Check Stripe connection



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/stripe/check
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
  /v2/stripe/check:
    get:
      tags:
        - Stripe
      summary: Check Stripe connection
      operationId: StripeController_check
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
                $ref: '#/components/schemas/StripCredentialsCheckOutputResponseDto'
components:
  schemas:
    StripCredentialsCheckOutputResponseDto:
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