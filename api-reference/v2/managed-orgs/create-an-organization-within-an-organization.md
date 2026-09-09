> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create an organization within an organization

> For platform, the plan must be 'SCALE' or higher to access this endpoint. Required membership role: `org admin`. PBAC permission: `organization.create`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/organizations/{orgId}/organizations
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
  /v2/organizations/{orgId}/organizations:
    post:
      tags:
        - Managed Orgs
      summary: Create an organization within an organization
      description: >-
        For platform, the plan must be 'SCALE' or higher to access this
        endpoint. Required membership role: `org admin`. PBAC permission:
        `organization.create`. Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control
      operationId: OrganizationsOrganizationsController_createOrganization
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
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateOrganizationInput'
      responses:
        '201':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateManagedOrganizationOutput'
components:
  schemas:
    CreateOrganizationInput:
      type: object
      properties:
        apiKeyDaysValid:
          type: number
          minimum: 1
          description: >-
            For how many days is managed organization api key valid. Defaults to
            30 days.
          example: 60
          default: 30
        apiKeyNeverExpires:
          type: boolean
          description: If true, organization api key never expires.
          example: true
        name:
          type: string
          minLength: 1
          description: >-
            Name of the organization. Maximum 155 characters. Cannot contain
            links or URLs.
          example: CalTeam
          maxLength: 155
        slug:
          type: string
          description: >-
            Organization slug in kebab-case - if not provided will be generated
            automatically based on name.
          example: cal-tel
        metadata:
          type: object
          description: |-
            You can store any additional data you want here.
            Metadata must have at most 50 keys, each key up to 40 characters.
            Values can be strings (up to 500 characters), numbers, or booleans.
          example:
            key: value
      required:
        - name
    CreateManagedOrganizationOutput:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          $ref: '#/components/schemas/ManagedOrganizationWithApiKeyOutput'
      required:
        - status
        - data
    ManagedOrganizationWithApiKeyOutput:
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
        apiKey:
          type: string
      required:
        - id
        - name
        - apiKey

````