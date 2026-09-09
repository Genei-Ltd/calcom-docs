> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update an organization within an organization

> For platform, the plan must be 'SCALE' or higher to access this endpoint. Required membership role: `org admin`. PBAC permission: `organization.update`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control



## OpenAPI

````yaml /api-reference/v2/openapi.json patch /v2/organizations/{orgId}/organizations/{managedOrganizationId}
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
    patch:
      tags:
        - Managed Orgs
      summary: Update an organization within an organization
      description: >-
        For platform, the plan must be 'SCALE' or higher to access this
        endpoint. Required membership role: `org admin`. PBAC permission:
        `organization.update`. Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control
      operationId: OrganizationsOrganizationsController_updateOrganization
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
        - name: orgId
          required: true
          in: path
          schema:
            type: number
        - name: managedOrganizationId
          required: true
          in: path
          schema:
            type: number
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateOrganizationInput'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetManagedOrganizationOutput'
components:
  schemas:
    UpdateOrganizationInput:
      type: object
      properties:
        name:
          type: string
          minLength: 1
          description: >-
            Name of the organization. Maximum 155 characters. Cannot contain
            links or URLs.
          example: CalTeam
          maxLength: 155
        metadata:
          type: object
          description: |-
            You can store any additional data you want here.
            Metadata must have at most 50 keys, each key up to 40 characters.
            Values can be strings (up to 500 characters), numbers, or booleans.
          example:
            key: value
    GetManagedOrganizationOutput:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
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
          example:
            key: value
      required:
        - id
        - name

````