> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Remove a permission from an organization role

> Required membership role: `org admin`. PBAC permission: `role.update`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control



## OpenAPI

````yaml /api-reference/v2/openapi.json delete /v2/organizations/{orgId}/roles/{roleId}/permissions/{permission}
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
  /v2/organizations/{orgId}/roles/{roleId}/permissions/{permission}:
    delete:
      tags:
        - Orgs / Roles / Permissions
      summary: Remove a permission from an organization role
      description: >-
        Required membership role: `org admin`. PBAC permission: `role.update`.
        Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control
      operationId: OrganizationsRolesPermissionsController_removePermission
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
        - name: permission
          required: true
          in: path
          schema:
            type: string
      responses:
        '204':
          description: ''

````