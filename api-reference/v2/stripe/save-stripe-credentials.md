> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Save Stripe credentials



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/stripe/save
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
  /v2/stripe/save:
    get:
      tags:
        - Stripe
      summary: Save Stripe credentials
      operationId: StripeController_save
      parameters:
        - name: state
          required: true
          in: query
          schema:
            type: string
        - name: code
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
                $ref: '#/components/schemas/StripCredentialsSaveOutputResponseDto'
components:
  schemas:
    StripCredentialsSaveOutputResponseDto:
      type: object
      properties:
        url:
          type: string
      required:
        - url

````