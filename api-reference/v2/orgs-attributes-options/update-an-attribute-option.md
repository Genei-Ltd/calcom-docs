> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update an attribute option

> Required membership role: `org admin`. PBAC permission: `organization.attributes.update`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control



## OpenAPI

````yaml /api-reference/v2/openapi.json patch /v2/organizations/{orgId}/attributes/{attributeId}/options/{optionId}
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
  /v2/organizations/{orgId}/attributes/{attributeId}/options/{optionId}:
    patch:
      tags:
        - Orgs / Attributes / Options
      summary: Update an attribute option
      description: >-
        Required membership role: `org admin`. PBAC permission:
        `organization.attributes.update`. Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control
      operationId: >-
        OrganizationsAttributesOptionsController_updateOrganizationAttributeOption
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
        - name: optionId
          required: true
          in: path
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateOrganizationAttributeOptionInput'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UpdateAttributeOptionOutput'
components:
  schemas:
    UpdateOrganizationAttributeOptionInput:
      type: object
      properties:
        value:
          type: string
        slug:
          type: string
    UpdateAttributeOptionOutput:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          $ref: '#/components/schemas/OptionOutput'
      required:
        - status
        - data
    OptionOutput:
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
      required:
        - id
        - attributeId
        - value
        - slug

````