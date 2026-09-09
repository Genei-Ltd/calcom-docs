> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List permissions for an organization team role

> Required membership role: `org admin`. PBAC permission: `role.readTeamRoles`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/organizations/{orgId}/teams/{teamId}/roles/{roleId}/permissions
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
    get:
      tags:
        - Orgs / Teams / Roles / Permissions
      summary: List permissions for an organization team role
      description: >-
        Required membership role: `org admin`. PBAC permission:
        `role.readTeamRoles`. Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control
      operationId: OrganizationsTeamsRolesPermissionsController_listPermissions
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
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetTeamRolePermissionsOutput'
components:
  schemas:
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