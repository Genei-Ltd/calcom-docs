> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a team

> If accessed using an OAuth access token, the `TEAM_PROFILE_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/teams
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
  /v2/teams:
    post:
      tags:
        - Teams
      summary: Create a team
      description: >-
        If accessed using an OAuth access token, the `TEAM_PROFILE_WRITE` scope
        is required.
      operationId: TeamsController_createTeam
      parameters:
        - name: Authorization
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateTeamInput'
      responses:
        '201':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateTeamOutput'
components:
  schemas:
    CreateTeamInput:
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
          additionalProperties: true
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
      required:
        - name
    CreateTeamOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          oneOf:
            - $ref: '#/components/schemas/CreateTeamOutputData'
              title: Pending Team
            - $ref: '#/components/schemas/TeamOutputDto'
              title: Team
          description: Either an Output object or a TeamOutputDto.
      required:
        - status
        - data
    CreateTeamOutputData:
      type: object
      properties:
        message:
          type: string
        paymentLink:
          type: string
          format: uri
        pendingTeam:
          $ref: '#/components/schemas/TeamOutputDto'
      required:
        - message
        - paymentLink
        - pendingTeam
    TeamOutputDto:
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
          format: uri
        calVideoLogo:
          type: string
          format: uri
        appLogo:
          type: string
          format: uri
        appIconLogo:
          type: string
          format: uri
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
          additionalProperties: true
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
          format: uri
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