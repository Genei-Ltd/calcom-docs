> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Save conferencing app OAuth credentials

> Required membership role: `team admin`. PBAC permission: `team.update`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control. If accessed using an OAuth access token, the `TEAM_APPS_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/organizations/{orgId}/teams/{teamId}/conferencing/{app}/oauth/callback
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
  /v2/organizations/{orgId}/teams/{teamId}/conferencing/{app}/oauth/callback:
    get:
      tags:
        - Orgs / Teams / Conferencing
      summary: Save conferencing app OAuth credentials
      description: >-
        Required membership role: `team admin`. PBAC permission: `team.update`.
        Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control. If accessed using
        an OAuth access token, the `TEAM_APPS_WRITE` scope is required.
      operationId: OrganizationsConferencingController_saveTeamOauthCredentials
      parameters:
        - name: state
          required: true
          in: query
          schema:
            type: string
        - name: code
          required: true
          in: query
          schema:
            type: string
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
          schema:
            type: string
      responses:
        '200':
          description: ''

````