> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create an attribute

> Required membership role: `org admin`. PBAC permission: `organization.attributes.create`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/organizations/{orgId}/attributes
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
    post:
      tags:
        - Orgs / Attributes
      summary: Create an attribute
      description: >-
        Required membership role: `org admin`. PBAC permission:
        `organization.attributes.create`. Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control
      operationId: OrganizationsAttributesController_createOrganizationAttribute
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
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateOrganizationAttributeInput'
      responses:
        '201':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateOrganizationAttributesOutput'
components:
  schemas:
    CreateOrganizationAttributeInput:
      type: object
      properties:
        name:
          type: string
        slug:
          type: string
        type:
          enum:
            - TEXT
            - NUMBER
            - SINGLE_SELECT
            - MULTI_SELECT
            - USER_RELATIONSHIP
          type: string
        options:
          type: array
          items:
            $ref: '#/components/schemas/CreateOrganizationAttributeOptionInput'
        enabled:
          type: boolean
      required:
        - name
        - slug
        - type
        - options
    CreateOrganizationAttributesOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/Attribute'
      required:
        - status
        - data
    CreateOrganizationAttributeOptionInput:
      type: object
      properties:
        value:
          type: string
        slug:
          type: string
      required:
        - value
        - slug
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
          enum:
            - TEXT
            - NUMBER
            - SINGLE_SELECT
            - MULTI_SELECT
            - USER_RELATIONSHIP
          type: string
          description: The type of the attribute
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