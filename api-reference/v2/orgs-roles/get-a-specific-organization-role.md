> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a specific organization role

> Required membership role: `org admin`. PBAC permission: `role.read`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/organizations/{orgId}/roles/{roleId}
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
    get:
      tags:
        - Orgs / Roles
      summary: Get a specific organization role
      description: >-
        Required membership role: `org admin`. PBAC permission: `role.read`.
        Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control
      operationId: OrganizationsRolesController_getRole
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
                $ref: '#/components/schemas/GetOrgRoleOutput'
components:
  schemas:
    GetOrgRoleOutput:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
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
          type: string
          description: Type of role
          enum:
            - SYSTEM
            - CUSTOM
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