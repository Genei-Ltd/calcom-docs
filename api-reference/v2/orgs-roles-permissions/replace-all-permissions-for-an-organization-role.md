> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Replace all permissions for an organization role

> Required membership role: `org admin`. PBAC permission: `role.update`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control



## OpenAPI

````yaml /api-reference/v2/openapi.json put /v2/organizations/{orgId}/roles/{roleId}/permissions
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
  /v2/organizations/{orgId}/roles/{roleId}/permissions:
    put:
      tags:
        - Orgs / Roles / Permissions
      summary: Replace all permissions for an organization role
      description: >-
        Required membership role: `org admin`. PBAC permission: `role.update`.
        Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control
      operationId: OrganizationsRolesPermissionsController_setPermissions
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
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateOrgRolePermissionsInput'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetOrgRolePermissionsOutput'
components:
  schemas:
    CreateOrgRolePermissionsInput:
      type: object
      properties:
        permissions:
          type: array
          description: 'Permissions to add (format: resource.action)'
          example:
            - eventType.read
            - booking.read
          items:
            type: string
            enum:
              - '*.*'
              - role.create
              - role.read
              - role.update
              - role.delete
              - eventType.create
              - eventType.read
              - eventType.update
              - eventType.delete
              - team.create
              - team.read
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
              - booking.readOrgAuditLogs
              - insights.read
              - workflow.create
              - workflow.read
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
              - routingForm.update
              - routingForm.delete
              - routingForm.readOrgAuditLogs
              - routingForm.readResponsePii
              - webhook.create
              - webhook.read
              - webhook.update
              - webhook.delete
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
      required:
        - permissions
    GetOrgRolePermissionsOutput:
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