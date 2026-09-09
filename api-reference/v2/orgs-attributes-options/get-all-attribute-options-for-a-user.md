> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all attribute options for a user

> Required membership role: `org member`. PBAC permission: `organization.attributes.read`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/organizations/{orgId}/attributes/options/{userId}
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
  /v2/organizations/{orgId}/attributes/options/{userId}:
    get:
      tags:
        - Orgs / Attributes / Options
      summary: Get all attribute options for a user
      description: >-
        Required membership role: `org member`. PBAC permission:
        `organization.attributes.read`. Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control
      operationId: >-
        OrganizationsAttributesOptionsController_getOrganizationAttributeOptionsForUser
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
        - name: userId
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
                $ref: '#/components/schemas/GetOptionUserOutput'
components:
  schemas:
    GetOptionUserOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          type: array
          items:
            $ref: '#/components/schemas/GetOptionUserOutputData'
      required:
        - status
        - data
    GetOptionUserOutputData:
      type: object
      properties:
        id:
          type: string
          description: The ID of the option assigned to the user
        attributeId:
          type: string
          description: The ID of the attribute
        value:
          type: string
          description: The value of the option
        slug:
          type: string
          description: The slug of the option
      required:
        - id
        - attributeId
        - value
        - slug

````