> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Disconnect team conferencing application

> Required membership role: `team admin`. PBAC permission: `team.update`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control. If accessed using an OAuth access token, the `TEAM_APPS_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json delete /v2/organizations/{orgId}/teams/{teamId}/conferencing/{app}/disconnect
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
  /v2/organizations/{orgId}/teams/{teamId}/conferencing/{app}/disconnect:
    delete:
      tags:
        - Orgs / Teams / Conferencing
      summary: Disconnect team conferencing application
      description: >-
        Required membership role: `team admin`. PBAC permission: `team.update`.
        Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control. If accessed using
        an OAuth access token, the `TEAM_APPS_WRITE` scope is required.
      operationId: OrganizationsConferencingController_disconnectTeamApp
      parameters:
        - name: teamId
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
              - zoom
              - msteams
            type: string
        - name: orgId
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
                $ref: >-
                  #/components/schemas/DisconnectConferencingAppOutputResponseDto
components:
  schemas:
    DisconnectConferencingAppOutputResponseDto:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
      required:
        - status

````