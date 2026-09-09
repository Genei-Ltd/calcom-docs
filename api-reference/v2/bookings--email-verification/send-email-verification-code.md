> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send email verification code

> Sends a one-time verification code to the specified email address.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/bookings/verification/email/send-code
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
  /v2/bookings/verification/email/send-code:
    post:
      tags:
        - Bookings - Email Verification
      summary: Send email verification code
      description: Sends a one-time verification code to the specified email address.
      operationId: BookingsVerificationController_sendEmailVerificationCode
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SendVerificationEmailInput'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SendVerificationEmailOutput'
components:
  schemas:
    SendVerificationEmailInput:
      type: object
      properties:
        email:
          type: string
          format: email
          example: user@example.com
        username:
          type: string
          example: johndoe
        language:
          type: string
          example: en
        isVerifyingEmail:
          type: boolean
          example: true
      required:
        - email
    SendVerificationEmailOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/SendVerificationEmailData'
      required:
        - status
        - data
    SendVerificationEmailData:
      type: object
      properties:
        sent:
          type: boolean
          example: true
      required:
        - sent

````