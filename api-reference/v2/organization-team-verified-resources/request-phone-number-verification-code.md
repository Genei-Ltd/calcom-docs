> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Request phone number verification code

> Sends a verification code to the phone number. Required membership role: `team admin`. PBAC permission: `team.update`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control. If accessed using an OAuth access token, the `TEAM_VERIFIED_RESOURCES_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/organizations/{orgId}/teams/{teamId}/verified-resources/phones/verification-code/request
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
  /v2/organizations/{orgId}/teams/{teamId}/verified-resources/phones/verification-code/request:
    post:
      tags:
        - Organization Team Verified Resources
      summary: Request phone number verification code
      description: >-
        Sends a verification code to the phone number. Required membership role:
        `team admin`. PBAC permission: `team.update`. Learn more about API
        access control at https://cal.com/docs/api-reference/v2/access-control.
        If accessed using an OAuth access token, the
        `TEAM_VERIFIED_RESOURCES_WRITE` scope is required.
      operationId: OrgTeamsVerifiedResourcesController_requestPhoneVerificationCode
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
        - name: orgId
          required: true
          in: path
          schema:
            type: number
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RequestPhoneVerificationInput'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RequestPhoneVerificationOutput'
components:
  schemas:
    RequestPhoneVerificationInput:
      type: object
      properties:
        phone:
          type: string
          description: Phone number to verify.
          example: +372 5555 6666
      required:
        - phone
    RequestPhoneVerificationOutput:
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