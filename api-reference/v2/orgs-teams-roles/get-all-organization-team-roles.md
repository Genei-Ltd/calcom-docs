> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all organization team roles

> Required membership role: `org admin`. PBAC permission: `role.readTeamRoles`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/organizations/{orgId}/teams/{teamId}/roles
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
  /v2/organizations/{orgId}/teams/{teamId}/roles:
    get:
      tags:
        - Orgs / Teams / Roles
      summary: Get all organization team roles
      description: >-
        Required membership role: `org admin`. PBAC permission:
        `role.readTeamRoles`. Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control
      operationId: OrganizationsTeamsRolesController_getAllRoles
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
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetAllTeamRolesOutput'
components:
  schemas:
    GetAllTeamRolesOutput:
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
            $ref: '#/components/schemas/TeamRoleOutput'
      required:
        - status
        - data
    TeamRoleOutput:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for the role
        name:
          type: string
          description: Name of the role
        color:
          type: string
          nullable: true
          description: Color for the role (hex code)
        description:
          type: string
          nullable: true
          description: Description of the role
        teamId:
          type: number
          nullable: true
          description: Team ID this role belongs to
        type:
          enum:
            - SYSTEM
            - CUSTOM
          type: string
          description: Type of role
        permissions:
          type: array
          description: Permissions assigned to this role in 'resource.action' format.
          example:
            - booking.read
            - eventType.create
          items:
            type: string
            enum:
              - role.create
              - role.read
              - role.readTeamRoles
              - role.update
              - role.delete
              - eventType.create
              - eventType.read
              - eventType.readTeamEventTypes
              - eventType.update
              - eventType.delete
              - team.read
              - team.readTeamSettings
              - team.readConferencing
              - team.readVerifiedResources
              - team.readMemberships
              - team.update
              - team.delete
              - team.invite
              - team.remove
              - team.listMembers
              - team.listMembersPrivate
              - team.changeMemberRole
              - team.impersonate
              - booking.read
              - booking.readTeamBookings
              - booking.readRecordings
              - booking.update
              - booking.updateTeamBookings
              - booking.reassignTeamPastBookings
              - booking.readTeamAuditLogs
              - insights.read
              - workflow.create
              - workflow.read
              - workflow.readTeamWorkflows
              - workflow.update
              - workflow.delete
              - routingForm.create
              - routingForm.read
              - routingForm.readTeamRoutingForms
              - routingForm.update
              - routingForm.delete
              - routingForm.readTeamAuditLogs
              - routingForm.readResponsePii
              - webhook.create
              - webhook.read
              - webhook.update
              - webhook.delete
              - availability.readTeamAvailability
              - featureOptIn.read
              - featureOptIn.update
              - tag.create
              - tag.update
              - tag.delete
        createdAt:
          type: string
          description: When the role was created
        updatedAt:
          type: string
          description: When the role was last updated
      required:
        - id
        - name
        - type
        - permissions
        - createdAt
        - updatedAt

````