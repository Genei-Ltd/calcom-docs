> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Verify an email

> Use code to verify an email. If accessed using an OAuth access token, the `VERIFIED_RESOURCES_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/verified-resources/emails/verification-code/verify
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
  /v2/verified-resources/emails/verification-code/verify:
    post:
      tags:
        - Verified Resources
      summary: Verify an email
      description: >-
        Use code to verify an email. If accessed using an OAuth access token,
        the `VERIFIED_RESOURCES_WRITE` scope is required.
      operationId: UserVerifiedResourcesController_verifyEmail
      parameters:
        - name: Authorization
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_, managed user access token, or OAuth access token
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/VerifyEmailInput'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserVerifiedEmailOutput'
components:
  schemas:
    VerifyEmailInput:
      type: object
      properties:
        email:
          type: string
          format: email
          description: Email to verify.
          example: example@acme.com
        code:
          type: string
          description: verification code sent to the email to verify
          example: 1ABG2C
      required:
        - email
        - code
    UserVerifiedEmailOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/UserVerifiedEmailOutputData'
      required:
        - status
        - data
    UserVerifiedEmailOutputData:
      type: object
      properties:
        id:
          type: number
          description: The unique identifier for the verified email.
          example: 789
        email:
          type: string
          description: The verified email address.
          example: user@example.com
          format: email
        userId:
          type: number
          description: The ID of the associated user, if applicable.
          example: 45
      required:
        - id
        - email
        - userId

````