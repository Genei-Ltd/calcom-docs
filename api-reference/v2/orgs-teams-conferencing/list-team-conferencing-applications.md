> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List team conferencing applications

> Required membership role: `team admin`. PBAC permission: `team.read`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control. If accessed using an OAuth access token, the `TEAM_APPS_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/organizations/{orgId}/teams/{teamId}/conferencing
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
  /v2/organizations/{orgId}/teams/{teamId}/conferencing:
    get:
      tags:
        - Orgs / Teams / Conferencing
      summary: List team conferencing applications
      description: >-
        Required membership role: `team admin`. PBAC permission: `team.read`.
        Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control. If accessed using
        an OAuth access token, the `TEAM_APPS_READ` scope is required.
      operationId: OrganizationsConferencingController_listTeamConferencingApps
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
                $ref: '#/components/schemas/ConferencingAppsOutputResponseDto'
components:
  schemas:
    ConferencingAppsOutputResponseDto:
      type: object
      properties:
        status:
          type: string
          enum:
            - success
            - error
        data:
          type: array
          items:
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