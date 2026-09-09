> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create team invite link

> Required membership role: `team admin`. PBAC permission: `team.invite`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control. If accessed using an OAuth access token, the `TEAM_MEMBERSHIP_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/organizations/{orgId}/teams/{teamId}/invite
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
  /v2/organizations/{orgId}/teams/{teamId}/invite:
    post:
      tags:
        - Orgs / Teams / Invite
      summary: Create team invite link
      description: >-
        Required membership role: `team admin`. PBAC permission: `team.invite`.
        Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control. If accessed using
        an OAuth access token, the `TEAM_MEMBERSHIP_WRITE` scope is required.
      operationId: OrganizationsTeamsInviteController_createInvite
      parameters:
        - name: Authorization
          in: header
          description: >-
            For non-platform customers - value must be `Bearer <token>` where
            `<token>` is api key prefixed with cal_
          required: false
          schema:
            type: string
        - name: x-cal-secret-key
          in: header
          description: For platform customers - OAuth client secret key
          required: false
          schema:
            type: string
        - name: x-cal-client-id
          in: header
          description: For platform customers - OAuth client ID
          required: false
          schema:
            type: string
        - name: orgId
          required: true
          in: path
          schema:
            type: number
        - name: teamId
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
                $ref: '#/components/schemas/CreateInviteOutputDto'
components:
  schemas:
    CreateInviteOutputDto:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/InviteDataDto'
      required:
        - status
        - data
    InviteDataDto:
      type: object
      properties:
        token:
          type: string
          description: >-
            Unique invitation token for this team. Share this token with
            prospective members to allow them to join the team/organization.
          example: f6a5c8b1d2e34c7f90a1b2c3d4e5f6a5b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2
        inviteLink:
          type: string
          description: >-
            Complete invitation URL that can be shared with prospective members.
            Opens the signup page with the token and redirects to getting
            started after signup.
          example: >-
            http://app.cal.com/signup?token=f6a5c8b1d2e34c7f90a1b2c3d4e5f6a5b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2&callbackUrl=/getting-started
      required:
        - token
        - inviteLink

````