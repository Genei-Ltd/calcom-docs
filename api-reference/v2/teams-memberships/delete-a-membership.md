> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a membership

> Required membership role: `team admin`. PBAC permission: `team.remove`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control. If accessed using an OAuth access token, the `TEAM_MEMBERSHIP_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json delete /v2/teams/{teamId}/memberships/{membershipId}
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
  /v2/teams/{teamId}/memberships/{membershipId}:
    delete:
      tags:
        - Teams / Memberships
      summary: Delete a membership
      description: >-
        Required membership role: `team admin`. PBAC permission: `team.remove`.
        Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control. If accessed using
        an OAuth access token, the `TEAM_MEMBERSHIP_WRITE` scope is required.
      operationId: TeamsMembershipsController_deleteTeamMembership
      parameters:
        - name: Authorization
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_
          required: true
          schema:
            type: string
        - name: teamId
          required: true
          in: path
          schema:
            type: number
        - name: membershipId
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
                $ref: '#/components/schemas/DeleteTeamMembershipOutput'
components:
  schemas:
    DeleteTeamMembershipOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/TeamMembershipOutput'
      required:
        - status
        - data
    TeamMembershipOutput:
      type: object
      properties:
        id:
          type: number
        userId:
          type: number
        teamId:
          type: number
        accepted:
          type: boolean
        role:
          enum:
            - MEMBER
            - OWNER
            - ADMIN
          type: string
        disableImpersonation:
          type: boolean
        user:
          $ref: '#/components/schemas/MembershipUserOutputDto'
      required:
        - id
        - userId
        - teamId
        - accepted
        - role
        - user
    MembershipUserOutputDto:
      type: object
      properties:
        avatarUrl:
          type: string
        username:
          type: string
        name:
          type: string
        email:
          type: string
        bio:
          type: string
        metadata:
          type: object
          example:
            key: value
      required:
        - email

````