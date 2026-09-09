> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Assign an attribute to a user

> Required membership role: `org admin`. PBAC permission: `organization.attributes.editUsers`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/organizations/{orgId}/attributes/options/{userId}
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
    post:
      tags:
        - Orgs / Attributes / Options
      summary: Assign an attribute to a user
      description: >-
        Required membership role: `org admin`. PBAC permission:
        `organization.attributes.editUsers`. Learn more about API access control
        at https://cal.com/docs/api-reference/v2/access-control
      operationId: >-
        OrganizationsAttributesOptionsController_assignOrganizationAttributeOptionToUser
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
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/AssignOrganizationAttributeOptionToUserInput
      responses:
        '201':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AssignOptionUserOutput'
components:
  schemas:
    AssignOrganizationAttributeOptionToUserInput:
      type: object
      properties:
        value:
          type: string
        attributeOptionId:
          type: string
        attributeId:
          type: string
        weight:
          type: number
          minimum: 0
          description: The weight of the attribute for this user
      required:
        - attributeId
    AssignOptionUserOutput:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          $ref: '#/components/schemas/AssignOptionUserOutputData'
      required:
        - status
        - data
    AssignOptionUserOutputData:
      type: object
      properties:
        id:
          type: string
          description: The ID of the option assigned to the user
        memberId:
          type: number
          description: The ID form the org membership for the user
        attributeOptionId:
          type: string
          description: The value of the option
        weight:
          type: number
          nullable: true
          description: The weight of the attribute for this user
      required:
        - id
        - memberId
        - attributeOptionId

````