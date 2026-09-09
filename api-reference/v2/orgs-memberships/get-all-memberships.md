> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all memberships

> Required membership role: `org admin`. PBAC permission: `organization.readMemberships`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control. If accessed using an OAuth access token, the `ORG_MEMBERSHIP_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/organizations/{orgId}/memberships
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
  /v2/organizations/{orgId}/memberships:
    get:
      tags:
        - Orgs / Memberships
      summary: Get all memberships
      description: >-
        Required membership role: `org admin`. PBAC permission:
        `organization.readMemberships`. Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control. If accessed using
        an OAuth access token, the `ORG_MEMBERSHIP_READ` scope is required.
      operationId: OrganizationsMembershipsController_getAllMemberships
      parameters:
        - name: Authorization
          in: header
          description: >-
            For non-platform customers - value must be `Bearer <token>` where
            `<token>` is api key prefixed with cal_
          required: false
          schema:
            type: string
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
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetAllOrgMemberships'
components:
  schemas:
    GetAllOrgMemberships:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/OrganizationMembershipOutput'
      required:
        - status
        - data
    OrganizationMembershipOutput:
      type: object
      properties:
        id:
          type: number
        userId:
          type: number
        teamId:
          type: number
        accepted:
          type: boolean
        role:
          enum:
            - MEMBER
            - OWNER
            - ADMIN
          type: string
        disableImpersonation:
          type: boolean
        user:
          $ref: '#/components/schemas/MembershipUserOutputDto'
        attributes:
          type: array
          items:
            oneOf:
              - $ref: '#/components/schemas/TextAttribute'
                title: Text
              - $ref: '#/components/schemas/NumberAttribute'
                title: Number
              - $ref: '#/components/schemas/SingleSelectAttribute'
                title: Single Select
              - $ref: '#/components/schemas/MultiSelectAttribute'
                title: Multi-Select
      required:
        - id
        - userId
        - teamId
        - accepted
        - role
        - user
        - attributes
    MembershipUserOutputDto:
      type: object
      properties:
        avatarUrl:
          type: string
        username:
          type: string
        name:
          type: string
        email:
          type: string
        bio:
          type: string
        metadata:
          type: object
          example:
            key: value
      required:
        - email
    TextAttribute:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        type:
          type: string
        option:
          type: string
        optionId:
          type: string
      required:
        - id
        - name
        - type
        - option
        - optionId
    NumberAttribute:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        type:
          type: string
        option:
          type: number
        optionId:
          type: string
      required:
        - id
        - name
        - type
        - option
        - optionId
    SingleSelectAttribute:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        type:
          type: string
        option:
          type: string
        optionId:
          type: string
      required:
        - id
        - name
        - type
        - option
        - optionId
    MultiSelectAttribute:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        type:
          type: string
        options:
          type: array
          items:
            $ref: '#/components/schemas/MultiSelectAttributeOption'
      required:
        - id
        - name
        - type
        - options
    MultiSelectAttributeOption:
      type: object
      properties:
        optionId:
          type: string
        option:
          type: string
      required:
        - optionId
        - option

````