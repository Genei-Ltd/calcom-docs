> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a team

> Required membership role: `org admin`. PBAC permission: `team.create`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control. If accessed using an OAuth access token, the `ORG_PROFILE_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/organizations/{orgId}/teams
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
  /v2/organizations/{orgId}/teams:
    post:
      tags:
        - Orgs / Teams
      summary: Create a team
      description: >-
        Required membership role: `org admin`. PBAC permission: `team.create`.
        Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control. If accessed using
        an OAuth access token, the `ORG_PROFILE_WRITE` scope is required.
      operationId: OrganizationsTeamsController_createTeam
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
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateOrgTeamDto'
      responses:
        '201':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrgTeamOutputResponseDto'
components:
  schemas:
    CreateOrgTeamDto:
      type: object
      properties:
        name:
          type: string
          minLength: 1
          maxLength: 155
          description: >-
            Name of the team. Maximum 155 characters. Cannot contain links or
            URLs.
          example: CalTeam
        slug:
          type: string
          description: >-
            Team slug in kebab-case - if not provided will be generated
            automatically based on name.
          example: caltel
        logoUrl:
          type: string
          example: >-
            https://i.cal.com/api/avatar/b0b58752-68ad-4c0d-8024-4fa382a77752.png
          description: URL of the teams logo image
        calVideoLogo:
          type: string
        appLogo:
          type: string
        appIconLogo:
          type: string
        bio:
          type: string
        hideBranding:
          type: boolean
          default: false
        isPrivate:
          type: boolean
        hideBookATeamMember:
          type: boolean
        metadata:
          type: object
          description: |-
            You can store any additional data you want here.
            Metadata must have at most 50 keys, each key up to 40 characters.
            Values can be strings (up to 500 characters), numbers, or booleans.
          example:
            key: value
        theme:
          type: string
        brandColor:
          type: string
        darkBrandColor:
          type: string
        bannerUrl:
          type: string
          example: >-
            https://i.cal.com/api/avatar/949be534-7a88-4185-967c-c020b0c0bef3.png
          description: URL of the teams banner image which is shown on booker
        timeFormat:
          type: number
        timeZone:
          type: string
          default: Europe/London
          example: America/New_York
          description: >-
            Timezone is used to create teams's default schedule from Monday to
            Friday from 9AM to 5PM. It will default to Europe/London if not
            passed.
        weekStart:
          type: string
          default: Sunday
          example: Monday
        autoAcceptCreator:
          type: boolean
          default: true
          description: >-
            If you are a platform customer, don't pass 'false', because then
            team creator won't be able to create team event types.
        addCreatorAsOwner:
          type: boolean
          default: true
          description: >-
            Whether to create an OWNER membership on the team for the user
            associated with authentication credentials for this request. For
            example, if you authenticate with API key belonging to Bob, then Bob
            will have OWNER membership for the newly created team. Pass false to
            create the team without an OWNER membership for that user - e.g. so
            it isn't included when assignAllTeamMembers is used on round-robin
            events. Org admins/owners can still manage the team and its event
            types without being a team member.
      required:
        - name
    OrgTeamOutputResponseDto:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          $ref: '#/components/schemas/OrgTeamOutputDto'
      required:
        - status
        - data
    OrgTeamOutputDto:
      type: object
      properties:
        id:
          type: number
        parentId:
          type: number
        name:
          type: string
          minLength: 1
        slug:
          type: string
        logoUrl:
          type: string
        calVideoLogo:
          type: string
        appLogo:
          type: string
        appIconLogo:
          type: string
        bio:
          type: string
        hideBranding:
          type: boolean
        isOrganization:
          type: boolean
        isPrivate:
          type: boolean
        hideBookATeamMember:
          type: boolean
          default: false
        metadata:
          type: object
          example:
            key: value
        theme:
          type: string
        brandColor:
          type: string
        darkBrandColor:
          type: string
        bannerUrl:
          type: string
        timeFormat:
          type: number
        timeZone:
          type: string
          default: Europe/London
        weekStart:
          type: string
          default: Sunday
      required:
        - id
        - name
        - isOrganization

````