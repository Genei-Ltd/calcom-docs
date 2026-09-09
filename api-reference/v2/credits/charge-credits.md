> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Charge credits

> Charge credits for an authenticated user. Uses externalRef for idempotency to prevent double-charging. Third-party OAuth tokens require the `CREDITS_WRITE` scope.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/credits/charge
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
  /v2/credits/charge:
    post:
      tags:
        - Credits
      summary: Charge credits
      description: >-
        Charge credits for an authenticated user. Uses externalRef for
        idempotency to prevent double-charging. Third-party OAuth tokens require
        the `CREDITS_WRITE` scope.
      operationId: CreditsController_chargeCredits
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ChargeCreditsInput'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
components:
  schemas:
    ChargeCreditsInput:
      type: object
      properties:
        credits:
          type: number
          minimum: 1
          description: Number of credits to charge
          example: 5
        creditFor:
          type: string
          description: What the credits are being charged for
          enum:
            - SMS
            - CAL_AI_PHONE_CALL
            - AI_AGENT
          example: AI_AGENT
        externalRef:
          type: string
          description: Unique external reference for idempotency
          example: agent-thread-123-1711432800000
      required:
        - credits
        - creditFor

````