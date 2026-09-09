> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Unassign an attribute from a user

> Required membership role: `org admin`. PBAC permission: `organization.attributes.editUsers`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control



## OpenAPI

````yaml /api-reference/v2/openapi.json delete /v2/organizations/{orgId}/attributes/options/{userId}/{attributeOptionId}
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
  /v2/organizations/{orgId}/attributes/options/{userId}/{attributeOptionId}:
    delete:
      tags:
        - Orgs / Attributes / Options
      summary: Unassign an attribute from a user
      description: >-
        Required membership role: `org admin`. PBAC permission:
        `organization.attributes.editUsers`. Learn more about API access control
        at https://cal.com/docs/api-reference/v2/access-control
      operationId: >-
        OrganizationsAttributesOptionsController_unassignOrganizationAttributeOptionFromUser
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
        - name: attributeOptionId
          required: true
          in: path
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UnassignOptionUserOutput'
components:
  schemas:
    UnassignOptionUserOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
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