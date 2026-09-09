> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get verified email of an org team by id

> Required membership role: `team admin`. PBAC permission: `team.readVerifiedResources`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control. If accessed using an OAuth access token, the `TEAM_VERIFIED_RESOURCES_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/organizations/{orgId}/teams/{teamId}/verified-resources/emails/{id}
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
  /v2/organizations/{orgId}/teams/{teamId}/verified-resources/emails/{id}:
    get:
      tags:
        - Organization Team Verified Resources
      summary: Get verified email of an org team by id
      description: >-
        Required membership role: `team admin`. PBAC permission:
        `team.readVerifiedResources`. Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control. If accessed using
        an OAuth access token, the `TEAM_VERIFIED_RESOURCES_READ` scope is
        required.
      operationId: OrgTeamsVerifiedResourcesController_getVerifiedEmailById
      parameters:
        - name: id
          required: true
          in: path
          schema:
            type: number
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
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TeamVerifiedEmailOutput'
components:
  schemas:
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