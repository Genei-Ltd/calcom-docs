> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a membership

> Required membership role: `org admin`. PBAC permission: `organization.remove`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control. If accessed using an OAuth access token, the `ORG_MEMBERSHIP_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json delete /v2/organizations/{orgId}/memberships/{membershipId}
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
  /v2/organizations/{orgId}/memberships/{membershipId}:
    delete:
      tags:
        - Orgs / Memberships
      summary: Delete a membership
      description: >-
        Required membership role: `org admin`. PBAC permission:
        `organization.remove`. Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control. If accessed using
        an OAuth access token, the `ORG_MEMBERSHIP_WRITE` scope is required.
      operationId: OrganizationsMembershipsController_deleteMembership
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
        - name: membershipId
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
                $ref: '#/components/schemas/DeleteOrgMembership'
components:
  schemas:
    DeleteOrgMembership:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
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
          type: string
          enum:
            - MEMBER
            - OWNER
            - ADMIN
        disableImpersonation:
          type: boolean
        user:
          $ref: '#/components/schemas/MembershipUserOutputDto'
        attributes:
          type: array
          items:
            oneOf:
              - $ref: '#/components/schemas/TextAttribute'
              - $ref: '#/components/schemas/NumberAttribute'
              - $ref: '#/components/schemas/SingleSelectAttribute'
              - $ref: '#/components/schemas/MultiSelectAttribute'
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