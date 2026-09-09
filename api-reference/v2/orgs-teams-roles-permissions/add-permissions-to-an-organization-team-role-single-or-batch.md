> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Add permissions to an organization team role (single or batch)



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/organizations/{orgId}/teams/{teamId}/roles/{roleId}/permissions
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
  /v2/organizations/{orgId}/teams/{teamId}/roles/{roleId}/permissions:
    post:
      tags:
        - Orgs / Teams / Roles / Permissions
      summary: Add permissions to an organization team role (single or batch)
      operationId: OrganizationsTeamsRolesPermissionsController_addPermissions
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
              $ref: '#/components/schemas/CreateTeamRolePermissionsInput'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetTeamRolePermissionsOutput'
components:
  schemas:
    CreateTeamRolePermissionsInput:
      type: object
      properties:
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
          description: 'Permissions to add (format: resource.action)'
          example:
            - eventType.read
            - booking.read
      required:
        - permissions
    GetTeamRolePermissionsOutput:
      type: object
      properties:
        status:
          type: string
          enum:
            - success
          example: success
        data:
          type: array
          items:
            type: string
      required:
        - status
        - data

````