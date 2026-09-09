> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get verified phone number of a team by id

> If accessed using an OAuth access token, the `TEAM_VERIFIED_RESOURCES_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/teams/{teamId}/verified-resources/phones/{id}
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
  /v2/teams/{teamId}/verified-resources/phones/{id}:
    get:
      tags:
        - Teams Verified Resources
      summary: Get verified phone number of a team by id
      description: >-
        If accessed using an OAuth access token, the
        `TEAM_VERIFIED_RESOURCES_READ` scope is required.
      operationId: TeamsVerifiedResourcesController_getVerifiedPhoneById
      parameters:
        - name: teamId
          required: true
          in: path
          schema:
            type: number
        - name: id
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
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TeamVerifiedPhoneOutput'
components:
  schemas:
    TeamVerifiedPhoneOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/TeamVerifiedPhoneOutputData'
      required:
        - status
        - data
    TeamVerifiedPhoneOutputData:
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
          nullable: true
          description: The ID of the associated user, if applicable.
          example: 45
        teamId:
          type: number
          description: The ID of the associated team, if applicable.
          example: 89
      required:
        - id
        - phoneNumber
        - teamId

````