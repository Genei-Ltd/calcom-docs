> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get teams

> If accessed using an OAuth access token, the `TEAM_PROFILE_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/teams
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
    get:
      tags:
        - Teams
      summary: Get teams
      description: >-
        If accessed using an OAuth access token, the `TEAM_PROFILE_READ` scope
        is required.
      operationId: TeamsController_getTeams
      parameters:
        - name: Authorization
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_
          required: true
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetTeamsOutput'
components:
  schemas:
    GetTeamsOutput:
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
            $ref: '#/components/schemas/TeamOutputDto'
      required:
        - status
        - data
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