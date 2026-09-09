> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Request email verification code

> Sends a verification code to the Email. If accessed using an OAuth access token, the `TEAM_VERIFIED_RESOURCES_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/teams/{teamId}/verified-resources/emails/verification-code/request
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
  /v2/teams/{teamId}/verified-resources/emails/verification-code/request:
    post:
      tags:
        - Teams Verified Resources
      summary: Request email verification code
      description: >-
        Sends a verification code to the Email. If accessed using an OAuth
        access token, the `TEAM_VERIFIED_RESOURCES_WRITE` scope is required.
      operationId: TeamsVerifiedResourcesController_requestEmailVerificationCode
      parameters:
        - name: Authorization
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_, managed user access token, or OAuth access token
          required: true
          schema:
            type: string
        - name: teamId
          required: true
          in: path
          schema:
            type: number
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RequestEmailVerificationInput'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RequestEmailVerificationOutput'
components:
  schemas:
    RequestEmailVerificationInput:
      type: object
      properties:
        email:
          type: string
          format: email
          description: Email to verify.
          example: acme@example.com
      required:
        - email
    RequestEmailVerificationOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
      required:
        - status

````