> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get list of verified phone numbers of an org team

> Required membership role: `team admin`. PBAC permission: `team.readVerifiedResources`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control. If accessed using an OAuth access token, the `TEAM_VERIFIED_RESOURCES_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/organizations/{orgId}/teams/{teamId}/verified-resources/phones
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
  /v2/organizations/{orgId}/teams/{teamId}/verified-resources/phones:
    get:
      tags:
        - Organization Team Verified Resources
      summary: Get list of verified phone numbers of an org team
      description: >-
        Required membership role: `team admin`. PBAC permission:
        `team.readVerifiedResources`. Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control. If accessed using
        an OAuth access token, the `TEAM_VERIFIED_RESOURCES_READ` scope is
        required.
      operationId: OrgTeamsVerifiedResourcesController_getVerifiedPhoneNumbers
      parameters:
        - name: teamId
          required: true
          in: path
          schema:
            type: number
        - name: take
          required: false
          in: query
          description: Maximum number of items to return
          schema:
            minimum: 1
            maximum: 250
            default: 250
            example: 25
            type: number
        - name: skip
          required: false
          in: query
          description: Number of items to skip
          schema:
            minimum: 0
            default: 0
            example: 0
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
                $ref: '#/components/schemas/TeamVerifiedPhonesOutput'
components:
  schemas:
    TeamVerifiedPhonesOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          type: array
          items:
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