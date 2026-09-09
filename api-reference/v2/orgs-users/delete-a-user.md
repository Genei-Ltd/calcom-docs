> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a user

> Required membership role: `org admin`. PBAC permission: `organization.remove`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control. If accessed using an OAuth access token, the `ORG_MEMBERSHIP_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json delete /v2/organizations/{orgId}/users/{userId}
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
  /v2/organizations/{orgId}/users/{userId}:
    delete:
      tags:
        - Orgs / Users
      summary: Delete a user
      description: >-
        Required membership role: `org admin`. PBAC permission:
        `organization.remove`. Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control. If accessed using
        an OAuth access token, the `ORG_MEMBERSHIP_WRITE` scope is required.
      operationId: OrganizationsUsersController_deleteOrganizationUser
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
                $ref: '#/components/schemas/GetOrganizationUserOutput'
components:
  schemas:
    GetOrganizationUserOutput:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          $ref: '#/components/schemas/GetOrgUsersWithProfileOutput'
      required:
        - status
        - data
    GetOrgUsersWithProfileOutput:
      type: object
      properties:
        id:
          type: number
          description: The ID of the user
          example: 1
        username:
          type: string
          nullable: true
          description: The username of the user
          example: john_doe
        name:
          type: string
          nullable: true
          description: The name of the user
          example: John Doe
        email:
          type: string
          description: The email of the user
          example: john@example.com
        emailVerified:
          format: date-time
          type: string
          nullable: true
          description: The date when the email was verified
          example: '2022-01-01T00:00:00Z'
        bio:
          type: string
          nullable: true
          description: The bio of the user
          example: I am a software developer
        avatarUrl:
          type: string
          nullable: true
          description: The URL of the user's avatar
          example: https://example.com/avatar.jpg
        timeZone:
          type: string
          description: The time zone of the user
          example: America/New_York
        weekStart:
          type: string
          description: The week start day of the user
          example: Monday
        appTheme:
          type: string
          nullable: true
          description: The app theme of the user
          example: light
        theme:
          type: string
          nullable: true
          description: The theme of the user
          example: default
        defaultScheduleId:
          type: number
          nullable: true
          description: The ID of the default schedule for the user
          example: 1
        locale:
          type: string
          nullable: true
          description: The locale of the user
          example: en-US
        timeFormat:
          type: number
          nullable: true
          description: The time format of the user
          example: 12
        hideBranding:
          type: boolean
          description: Whether to hide branding for the user
          example: false
        brandColor:
          type: string
          nullable: true
          description: The brand color of the user
          example: '#ffffff'
        darkBrandColor:
          type: string
          nullable: true
          description: The dark brand color of the user
          example: '#000000'
        allowDynamicBooking:
          type: boolean
          nullable: true
          description: Whether dynamic booking is allowed for the user
          example: true
        createdDate:
          format: date-time
          type: string
          description: The date when the user was created
          example: '2022-01-01T00:00:00Z'
        verified:
          type: boolean
          nullable: true
          description: Whether the user is verified
          example: true
        invitedTo:
          type: number
          nullable: true
          description: The ID of the user who invited this user
          example: 1
        metadata:
          type: object
          example:
            key: value
        profile:
          description: >-
            organization user profile, contains user data within the organizaton
            context
          allOf:
            - $ref: '#/components/schemas/ProfileOutput'
      required:
        - id
        - email
        - timeZone
        - weekStart
        - hideBranding
        - createdDate
        - profile
    ProfileOutput:
      type: object
      properties:
        id:
          type: number
          description: The ID of the profile of user
          example: 1
        organizationId:
          type: number
          description: The ID of the organization of user
          example: 1
        userId:
          type: number
          description: The IDof the user
          example: 1
        username:
          type: string
          nullable: true
          description: The username of the user within the organization context
          example: john_doe
      required:
        - id
        - organizationId
        - userId

````