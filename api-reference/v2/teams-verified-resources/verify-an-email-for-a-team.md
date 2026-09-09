> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Verify an email for a team

> Use code to verify an email. If accessed using an OAuth access token, the `TEAM_VERIFIED_RESOURCES_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/teams/{teamId}/verified-resources/emails/verification-code/verify
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
  /v2/teams/{teamId}/verified-resources/emails/verification-code/verify:
    post:
      tags:
        - Teams Verified Resources
      summary: Verify an email for a team
      description: >-
        Use code to verify an email. If accessed using an OAuth access token,
        the `TEAM_VERIFIED_RESOURCES_WRITE` scope is required.
      operationId: TeamsVerifiedResourcesController_verifyEmail
      parameters:
        - name: teamId
          required: true
          in: path
          schema:
            type: number
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
                $ref: '#/components/schemas/TeamVerifiedEmailOutput'
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
    TeamVerifiedEmailOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/TeamVerifiedEmailOutputData'
      required:
        - status
        - data
    TeamVerifiedEmailOutputData:
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
        teamId:
          type: number
          description: The ID of the associated team, if applicable.
          example: 89
        userId:
          type: number
          nullable: true
          description: The ID of the associated user, if applicable.
          example: 45
      required:
        - id
        - email
        - teamId

````