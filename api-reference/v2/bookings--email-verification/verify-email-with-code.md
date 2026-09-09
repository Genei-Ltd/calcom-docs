> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Verify email with code

> Verifies an email address using the one-time code that was previously sent.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/bookings/verification/email/verify-code
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
  /v2/bookings/verification/email/verify-code:
    post:
      tags:
        - Bookings - Email Verification
      summary: Verify email with code
      description: >-
        Verifies an email address using the one-time code that was previously
        sent.
      operationId: BookingsVerificationController_verifyEmailCode
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/VerifyEmailCodeInput'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/VerifyEmailCodeOutput'
components:
  schemas:
    VerifyEmailCodeInput:
      type: object
      properties:
        email:
          type: string
          example: user@example.com
        code:
          type: string
          example: '123456'
      required:
        - email
        - code
    VerifyEmailCodeOutput:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          $ref: '#/components/schemas/VerifyEmailCodeData'
      required:
        - status
        - data
    VerifyEmailCodeData:
      type: object
      properties:
        verified:
          type: boolean
          example: true
      required:
        - verified

````