> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update an organization team role



## OpenAPI

````yaml /api-reference/v2/openapi.json patch /v2/organizations/{orgId}/teams/{teamId}/roles/{roleId}
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
  /v2/organizations/{orgId}/teams/{teamId}/roles/{roleId}:
    patch:
      tags:
        - Orgs / Teams / Roles
      summary: Update an organization team role
      operationId: OrganizationsTeamsRolesController_updateRole
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
        - name: roleId
          required: true
          in: path
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateTeamRoleInput'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UpdateTeamRoleOutput'
components:
  schemas:
    UpdateTeamRoleInput:
      type: object
      properties:
        color:
          type: string
          description: Color for the role (hex code)
        description:
          type: string
          description: Description of the role
        permissions:
          type: array
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
          description: >-
            Permissions for this role (format: resource.action). On update, this
            field replaces the entire permission set for the role (full
            replace). Use granular permission endpoints for one-by-one changes.
          example:
            - eventType.read
            - eventType.create
            - booking.read
        name:
          type: string
          minLength: 1
          description: Name of the role
    UpdateTeamRoleOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
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