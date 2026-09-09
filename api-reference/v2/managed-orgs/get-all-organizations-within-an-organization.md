> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all organizations within an organization

> For platform, the plan must be 'SCALE' or higher to access this endpoint. Required membership role: `org admin`. PBAC permission: `organization.read`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/organizations/{orgId}/organizations
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
    get:
      tags:
        - Managed Orgs
      summary: Get all organizations within an organization
      description: >-
        For platform, the plan must be 'SCALE' or higher to access this
        endpoint. Required membership role: `org admin`. PBAC permission:
        `organization.read`. Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control
      operationId: OrganizationsOrganizationsController_getOrganizations
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
        - name: take
          required: false
          in: query
          description: Maximum number of items to return
          schema:
            minimum: 1
            maximum: 250
            default: 250
            example: 25
            type: number
        - name: skip
          required: false
          in: query
          description: Number of items to skip
          schema:
            minimum: 0
            default: 0
            example: 0
            type: number
        - name: slug
          required: false
          in: query
          description: The slug of the managed organization
          schema:
            example: organization-slug
            type: string
        - name: metadataKey
          required: false
          in: query
          description: >-
            The key of the metadata - it is case sensitive so provide exactly as
            stored. If you provide it then you must also provide metadataValue
          schema:
            example: metadata-key
            type: string
        - name: metadataValue
          required: false
          in: query
          description: >-
            The value of the metadata - it is case sensitive so provide exactly
            as stored. If you provide it then you must also provide metadataKey
          schema:
            example: metadata-value
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetManagedOrganizationsOutput'
components:
  schemas:
    GetManagedOrganizationsOutput:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          type: array
          items:
            $ref: '#/components/schemas/ManagedOrganizationOutput'
        pagination:
          $ref: '#/components/schemas/PaginationMetaDto'
      required:
        - status
        - data
        - pagination
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
    PaginationMetaDto:
      type: object
      properties:
        totalItems:
          type: number
          minimum: 0
          description: >-
            The total number of items available across all pages, matching the
            query criteria.
          example: 123
        remainingItems:
          type: number
          minimum: 0
          description: >-
            The number of items remaining to be fetched *after* the current
            page. Calculated as: `totalItems - (skip + itemsPerPage)`.
          example: 103
        returnedItems:
          type: number
          minimum: 0
          description: The number of items returned in the current page.
          example: 10
        itemsPerPage:
          type: number
          minimum: 1
          description: The maximum number of items requested per page.
          example: 10
        currentPage:
          type: number
          minimum: 1
          description: The current page number being returned.
          example: 2
        totalPages:
          type: number
          minimum: 0
          description: The total number of pages available.
          example: 13
        hasNextPage:
          type: boolean
          description: >-
            Indicates if there is a subsequent page available after the current
            one.
          example: true
        hasPreviousPage:
          type: boolean
          description: >-
            Indicates if there is a preceding page available before the current
            one.
          example: true
      required:
        - totalItems
        - remainingItems
        - returnedItems
        - itemsPerPage
        - currentPage
        - totalPages
        - hasNextPage
        - hasPreviousPage

````