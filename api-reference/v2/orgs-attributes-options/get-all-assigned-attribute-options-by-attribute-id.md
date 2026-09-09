> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all assigned attribute options by attribute ID

> Required membership role: `org member`. PBAC permission: `organization.attributes.read`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/organizations/{orgId}/attributes/{attributeId}/options/assigned
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
  /v2/organizations/{orgId}/attributes/{attributeId}/options/assigned:
    get:
      tags:
        - Orgs / Attributes / Options
      summary: Get all assigned attribute options by attribute ID
      description: >-
        Required membership role: `org member`. PBAC permission:
        `organization.attributes.read`. Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control
      operationId: >-
        OrganizationsAttributesOptionsController_getOrganizationAttributeAssignedOptions
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
        - name: attributeId
          required: true
          in: path
          schema:
            type: string
        - name: skip
          required: false
          in: query
          description: Number of responses to skip
          schema:
            type: number
        - name: take
          required: false
          in: query
          description: Number of responses to take
          schema:
            type: number
        - name: assignedOptionIds
          required: false
          in: query
          description: >-
            Filter by assigned attribute option ids. ids must be separated by a
            comma.
          schema:
            example: >-
              ?assignedOptionIds=aaaaaaaa-bbbb-cccc-dddd-eeeeee1eee,aaaaaaaa-bbbb-cccc-dddd-eeeeee2eee
            type: array
            items:
              type: string
        - name: teamIds
          required: false
          in: query
          description: Filter by teamIds. Team ids must be separated by a comma.
          schema:
            example: '?teamIds=100,200'
            type: array
            items:
              type: number
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetAllAttributeAssignedOptionOutput'
components:
  schemas:
    GetAllAttributeAssignedOptionOutput:
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
            $ref: '#/components/schemas/AssignedOptionOutput'
      required:
        - status
        - data
    AssignedOptionOutput:
      type: object
      properties:
        id:
          type: string
          description: The ID of the option
          example: attr_option_id
        attributeId:
          type: string
          description: The ID of the attribute
          example: attr_id
        value:
          type: string
          description: The value of the option
          example: option_value
        slug:
          type: string
          description: The slug of the option
          example: option-slug
        assignedUserIds:
          description: Ids of the users assigned to the attribute option.
          example:
            - 124
            - 224
          type: array
          items:
            type: number
      required:
        - id
        - attributeId
        - value
        - slug
        - assignedUserIds

````