> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Verify a phone number

> Use code to verify a phone number. If accessed using an OAuth access token, the `VERIFIED_RESOURCES_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/verified-resources/phones/verification-code/verify
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
  /v2/verified-resources/phones/verification-code/verify:
    post:
      tags:
        - Verified Resources
      summary: Verify a phone number
      description: >-
        Use code to verify a phone number. If accessed using an OAuth access
        token, the `VERIFIED_RESOURCES_WRITE` scope is required.
      operationId: UserVerifiedResourcesController_verifyPhoneNumber
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
              $ref: '#/components/schemas/VerifyPhoneInput'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserVerifiedPhoneOutput'
components:
  schemas:
    VerifyPhoneInput:
      type: object
      properties:
        phone:
          type: string
          description: phone number to verify.
          example: '+37255556666'
        code:
          type: string
          description: verification code sent to the phone number to verify
          example: 1ABG2C
      required:
        - phone
        - code
    UserVerifiedPhoneOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/UserVerifiedPhoneOutputData'
      required:
        - status
        - data
    UserVerifiedPhoneOutputData:
      type: object
      properties:
        id:
          type: number
          description: The unique identifier for the verified email.
          example: 789
        phoneNumber:
          type: string
          description: The verified phone number.
          example: '+37255556666'
          format: phone
        userId:
          type: number
          description: The ID of the associated user, if applicable.
          example: 45
      required:
        - id
        - phoneNumber
        - userId

````