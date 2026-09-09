> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a team

> If accessed using an OAuth access token, the `TEAM_PROFILE_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json delete /v2/teams/{teamId}
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
  /v2/teams/{teamId}:
    delete:
      tags:
        - Teams
      summary: Delete a team
      description: >-
        If accessed using an OAuth access token, the `TEAM_PROFILE_WRITE` scope
        is required.
      operationId: TeamsController_deleteTeam
      parameters:
        - name: Authorization
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_
          required: true
          schema:
            type: string
        - name: teamId
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
                $ref: '#/components/schemas/OrgTeamOutputResponseDto'
components:
  schemas:
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