> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all memberships

> Retrieve team memberships with optional filtering by email addresses. Supports pagination. If accessed using an OAuth access token, the `TEAM_MEMBERSHIP_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/teams/{teamId}/memberships
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
  /v2/teams/{teamId}/memberships:
    get:
      tags:
        - Teams / Memberships
      summary: Get all memberships
      description: >-
        Retrieve team memberships with optional filtering by email addresses.
        Supports pagination. If accessed using an OAuth access token, the
        `TEAM_MEMBERSHIP_READ` scope is required.
      operationId: TeamsMembershipsController_getTeamMemberships
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
        - name: emails
          required: false
          in: query
          description: >-
            Filter team memberships by email addresses. If you want to filter by
            multiple emails, separate them with a comma (max 20 emails for
            performance).
          schema:
            example: '?emails=user1@example.com,user2@example.com'
            type: array
            items:
              type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetTeamMembershipsOutput'
components:
  schemas:
    GetTeamMembershipsOutput:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
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
          type: string
          enum:
            - MEMBER
            - OWNER
            - ADMIN
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