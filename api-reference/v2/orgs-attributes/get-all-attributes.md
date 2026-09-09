> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all attributes

> Required membership role: `org member`. PBAC permission: `organization.attributes.read`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/organizations/{orgId}/attributes
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
  /v2/organizations/{orgId}/attributes:
    get:
      tags:
        - Orgs / Attributes
      summary: Get all attributes
      description: >-
        Required membership role: `org member`. PBAC permission:
        `organization.attributes.read`. Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control
      operationId: OrganizationsAttributesController_getOrganizationAttributes
      parameters:
        - name: Authorization
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_
          required: true
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
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetOrganizationAttributesOutput'
components:
  schemas:
    GetOrganizationAttributesOutput:
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
            $ref: '#/components/schemas/Attribute'
      required:
        - status
        - data
    Attribute:
      type: object
      properties:
        id:
          type: string
          description: The ID of the attribute
          example: attr_123
        teamId:
          type: number
          description: The team ID associated with the attribute
          example: 1
        type:
          type: string
          description: The type of the attribute
          enum:
            - TEXT
            - NUMBER
            - SINGLE_SELECT
            - MULTI_SELECT
            - USER_RELATIONSHIP
        name:
          type: string
          description: The name of the attribute
          example: Attribute Name
        slug:
          type: string
          description: The slug of the attribute
          example: attribute-name
        enabled:
          type: boolean
          description: Whether the attribute is enabled and displayed on their profile
          example: true
        usersCanEditRelation:
          type: boolean
          description: Whether users can edit the relation
          example: true
      required:
        - id
        - teamId
        - type
        - name
        - slug
        - enabled

````