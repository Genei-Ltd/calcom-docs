> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create team invite link

> If accessed using an OAuth access token, the `TEAM_MEMBERSHIP_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/teams/{teamId}/invite
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
  /v2/teams/{teamId}/invite:
    post:
      tags:
        - Teams / Invite
      summary: Create team invite link
      description: >-
        If accessed using an OAuth access token, the `TEAM_MEMBERSHIP_WRITE`
        scope is required.
      operationId: TeamsInviteController_createInvite
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