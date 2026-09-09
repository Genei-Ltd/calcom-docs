> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get team default conferencing application

> Required membership role: `team admin`. PBAC permission: `team.read`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control. If accessed using an OAuth access token, the `TEAM_APPS_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/organizations/{orgId}/teams/{teamId}/conferencing/default
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
  /v2/organizations/{orgId}/teams/{teamId}/conferencing/default:
    get:
      tags:
        - Orgs / Teams / Conferencing
      summary: Get team default conferencing application
      description: >-
        Required membership role: `team admin`. PBAC permission: `team.read`.
        Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control. If accessed using
        an OAuth access token, the `TEAM_APPS_READ` scope is required.
      operationId: OrganizationsConferencingController_getTeamDefaultApp
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
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/GetDefaultConferencingAppOutputResponseDto
components:
  schemas:
    GetDefaultConferencingAppOutputResponseDto:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          $ref: '#/components/schemas/DefaultConferencingAppsOutputDto'
      required:
        - status
    DefaultConferencingAppsOutputDto:
      type: object
      properties:
        appSlug:
          type: string
        appLink:
          type: string

````