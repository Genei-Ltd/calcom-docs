> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete an organization role

> Required membership role: `org admin`. PBAC permission: `role.delete`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control



## OpenAPI

````yaml /api-reference/v2/openapi.json delete /v2/organizations/{orgId}/roles/{roleId}
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
  /v2/organizations/{orgId}/roles/{roleId}:
    delete:
      tags:
        - Orgs / Roles
      summary: Delete an organization role
      description: >-
        Required membership role: `org admin`. PBAC permission: `role.delete`.
        Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control
      operationId: OrganizationsRolesController_deleteRole
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
        - name: roleId
          required: true
          in: path
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeleteOrgRoleOutput'
components:
  schemas:
    DeleteOrgRoleOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/OrgRoleOutput'
      required:
        - status
        - data
    OrgRoleOutput:
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
        organizationId:
          type: number
          nullable: true
          description: Organization ID this role belongs to
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
              - '*.*'
              - role.create
              - role.read
              - role.readTeamRoles
              - role.readOrgRoles
              - role.update
              - role.delete
              - eventType.create
              - eventType.read
              - eventType.readTeamEventTypes
              - eventType.readOrgEventTypes
              - eventType.update
              - eventType.delete
              - team.create
              - team.read
              - team.readOrgTeams
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
              - organization.create
              - organization.read
              - organization.readMemberships
              - organization.readManagedOrganizations
              - organization.readDelegationCredentials
              - organization.listMembers
              - organization.listMembersPrivate
              - organization.invite
              - organization.remove
              - organization.manageBilling
              - organization.changeMemberRole
              - organization.impersonate
              - organization.passwordReset
              - organization.editUsers
              - organization.update
              - organization.delete
              - booking.read
              - booking.readOrgBookings
              - booking.readRecordings
              - booking.update
              - booking.updateOrgBookings
              - booking.reassignOrgPastBookings
              - booking.readOrgAuditLogs
              - insights.read
              - workflow.create
              - workflow.read
              - workflow.readTeamWorkflows
              - workflow.update
              - workflow.delete
              - organization.attributes.read
              - organization.attributes.update
              - organization.attributes.delete
              - organization.attributes.create
              - organization.attributes.readSyncHistory
              - organization.attributes.editUsers
              - organization.attributes.readAuditLogs
              - routingForm.create
              - routingForm.read
              - routingForm.readTeamRoutingForms
              - routingForm.readOrgRoutingForms
              - routingForm.update
              - routingForm.delete
              - routingForm.readOrgAuditLogs
              - routingForm.readResponsePii
              - webhook.create
              - webhook.read
              - webhook.readOrgWebhooks
              - webhook.update
              - webhook.delete
              - availability.readTeamAvailability
              - availability.readOrgAvailability
              - availability.updateOrgAvailability
              - ooo.readOrgOoo
              - watchlist.create
              - watchlist.read
              - watchlist.update
              - watchlist.delete
              - featureOptIn.read
              - featureOptIn.update
              - organization.customDomain.create
              - organization.customDomain.read
              - organization.customDomain.update
              - organization.customDomain.delete
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