> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a membership

> Required membership role: `org admin`. PBAC permission: `organization.invite`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control. If accessed using an OAuth access token, the `ORG_MEMBERSHIP_WRITE` scope is required.

Two identifier modes are accepted in the request body:

1. **`userId`** — attach an existing user (by id) directly. Use when the caller already knows the Cal.com user id and just needs the membership row created/updated. No notification email is sent.

2. **`email`** — invite an existing Cal.com user (by email). Runs the same invite flow the dashboard uses; the user must already exist (if not, the request returns `404` — create them first via `POST /v2/organizations/{orgId}/users`). What happens next depends on the organization's settings:

   - **Auto-attach path.** When the organization is verified by Cal.com and the invitee's email domain matches the organization's configured auto-accept domain (both set by Cal.com during organization verification — not editable by the organization's own admins), the user is added as an accepted member: their organization profile is created, the membership is created with `accepted: true`, and they receive a "you've been added to the organization" notification email.

   - **Pending-invite path.** If either condition is not met, the user receives an "accept your invite" notification email and the membership is created with `accepted: false` until they accept it via the dashboard. No organization profile is created until acceptance.

   Either way the response's `accepted` value reflects the outcome, seat addition is recorded, and the new seat count is pushed to the billing provider.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/organizations/{orgId}/memberships
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
    post:
      tags:
        - Orgs / Memberships
      summary: Create a membership
      description: >-
        Required membership role: `org admin`. PBAC permission:
        `organization.invite`. Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control. If accessed using
        an OAuth access token, the `ORG_MEMBERSHIP_WRITE` scope is required.


        Two identifier modes are accepted in the request body:


        1. **`userId`** — attach an existing user (by id) directly. Use when the
        caller already knows the Cal.com user id and just needs the membership
        row created/updated. No notification email is sent.


        2. **`email`** — invite an existing Cal.com user (by email). Runs the
        same invite flow the dashboard uses; the user must already exist (if
        not, the request returns `404` — create them first via `POST
        /v2/organizations/{orgId}/users`). What happens next depends on the
        organization's settings:

           - **Auto-attach path.** When the organization is verified by Cal.com and the invitee's email domain matches the organization's configured auto-accept domain (both set by Cal.com during organization verification — not editable by the organization's own admins), the user is added as an accepted member: their organization profile is created, the membership is created with `accepted: true`, and they receive a "you've been added to the organization" notification email.

           - **Pending-invite path.** If either condition is not met, the user receives an "accept your invite" notification email and the membership is created with `accepted: false` until they accept it via the dashboard. No organization profile is created until acceptance.

           Either way the response's `accepted` value reflects the outcome, seat addition is recorded, and the new seat count is pushed to the billing provider.
      operationId: OrganizationsMembershipsController_createMembership
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
      requestBody:
        required: true
        description: >-
          Either `userId` to attach an existing org user directly, or `email` to
          invite an existing Cal.com user via the dashboard's invite flow.
        content:
          application/json:
            schema:
              oneOf:
                - $ref: '#/components/schemas/CreateOrgMembershipDto'
                  title: Member by User ID
                - $ref: '#/components/schemas/CreateOrgMembershipByEmailDto'
                  title: Member by Email
      responses:
        '201':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateOrgMembershipOutput'
components:
  schemas:
    CreateOrgMembershipDto:
      type: object
      properties:
        userId:
          type: number
        accepted:
          type: boolean
          default: false
        role:
          default: MEMBER
          enum:
            - MEMBER
            - OWNER
            - ADMIN
          type: string
          description: >-
            If you are platform customer then managed users should only have
            MEMBER role.
        disableImpersonation:
          type: boolean
          default: false
      required:
        - userId
        - role
    CreateOrgMembershipByEmailDto:
      type: object
      properties:
        email:
          type: string
          format: email
          description: Email of an existing Cal.com user to invite to the organization.
        role:
          default: MEMBER
          enum:
            - MEMBER
            - OWNER
            - ADMIN
          type: string
          description: >-
            Role to assign to the invited user. If you are platform customer
            then managed users should only have MEMBER role.
      required:
        - email
        - role
    CreateOrgMembershipOutput:
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