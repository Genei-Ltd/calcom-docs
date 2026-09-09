> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect your conferencing application to a team

> Only `google-meet` can be connected this way, and only for a team that already has a valid Google Calendar connection. Zoom and Microsoft Teams require an OAuth handshake - start it with `GET /v2/organizations/{orgId}/teams/{teamId}/conferencing/{app}/oauth/auth-url` instead. Walkthrough: https://cal.com/docs/api-reference/v2/conferencing-apps. Required membership role: `team admin`. PBAC permission: `team.update`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control. If accessed using an OAuth access token, the `TEAM_APPS_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/organizations/{orgId}/teams/{teamId}/conferencing/{app}/connect
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
  /v2/organizations/{orgId}/teams/{teamId}/conferencing/{app}/connect:
    post:
      tags:
        - Orgs / Teams / Conferencing
      summary: Connect your conferencing application to a team
      description: >-
        Only `google-meet` can be connected this way, and only for a team that
        already has a valid Google Calendar connection. Zoom and Microsoft Teams
        require an OAuth handshake - start it with `GET
        /v2/organizations/{orgId}/teams/{teamId}/conferencing/{app}/oauth/auth-url`
        instead. Walkthrough:
        https://cal.com/docs/api-reference/v2/conferencing-apps. Required
        membership role: `team admin`. PBAC permission: `team.update`. Learn
        more about API access control at
        https://cal.com/docs/api-reference/v2/access-control. If accessed using
        an OAuth access token, the `TEAM_APPS_WRITE` scope is required.
      operationId: OrganizationsConferencingController_connectTeamApp
      parameters:
        - name: teamId
          required: true
          in: path
          schema:
            type: number
        - name: orgId
          required: true
          in: path
          schema:
            type: number
        - name: app
          required: true
          in: path
          description: Conferencing application type
          schema:
            enum:
              - google-meet
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ConferencingAppOutputResponseDto'
components:
  schemas:
    ConferencingAppOutputResponseDto:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
        data:
          $ref: '#/components/schemas/ConferencingAppsOutputDto'
      required:
        - status
        - data
    ConferencingAppsOutputDto:
      type: object
      properties:
        id:
          type: number
          description: Id of the conferencing app credentials
        type:
          type: string
          example: google_video
          description: Type of conferencing app
        userId:
          type: number
          description: Id of the user associated to the conferencing app
        invalid:
          type: boolean
          nullable: true
          example: true
          description: Whether if the connection is working or not.
      required:
        - id
        - type
        - userId

````