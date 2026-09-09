> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get an organization within an organization

> For platform, the plan must be 'SCALE' or higher to access this endpoint. Required membership role: `org admin`. PBAC permission: `organization.readManagedOrganizations`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/organizations/{orgId}/organizations/{managedOrganizationId}
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
  /v2/organizations/{orgId}/organizations/{managedOrganizationId}:
    get:
      tags:
        - Managed Orgs
      summary: Get an organization within an organization
      description: >-
        For platform, the plan must be 'SCALE' or higher to access this
        endpoint. Required membership role: `org admin`. PBAC permission:
        `organization.readManagedOrganizations`. Learn more about API access
        control at https://cal.com/docs/api-reference/v2/access-control
      operationId: OrganizationsOrganizationsController_getOrganization
      parameters:
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
        - name: managedOrganizationId
          required: true
          in: path
          schema:
            type: number
        - name: orgId
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
                $ref: '#/components/schemas/GetManagedOrganizationOutput'
components:
  schemas:
    GetManagedOrganizationOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/ManagedOrganizationOutput'
      required:
        - status
        - data
    ManagedOrganizationOutput:
      type: object
      properties:
        id:
          type: number
        name:
          type: string
          minLength: 1
        slug:
          type: string
        metadata:
          type: object
          additionalProperties: true
          example:
            key: value
      required:
        - id
        - name

````