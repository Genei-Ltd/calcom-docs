> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get OAuth conferencing app's auth URL for a team

> Returns the URL to send a team admin to so they can authorize Zoom or Microsoft Teams for the team. Redirect their browser to it - the provider then returns them to a callback already registered by Cal.com, which stores the credential against the team rather than against the admin who authorized it. `returnTo` and `onErrorReturnTo` must each be a relative path or an absolute http(s) URL. The returned URL expires 10 minutes after this call, so redirect immediately rather than caching it. Walkthrough: https://cal.com/docs/api-reference/v2/conferencing-apps. Required membership role: `team admin`. PBAC permission: `team.update`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control. If accessed using an OAuth access token, the `TEAM_APPS_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/organizations/{orgId}/teams/{teamId}/conferencing/{app}/oauth/auth-url
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
  /v2/organizations/{orgId}/teams/{teamId}/conferencing/{app}/oauth/auth-url:
    get:
      tags:
        - Orgs / Teams / Conferencing
      summary: Get OAuth conferencing app's auth URL for a team
      description: >-
        Returns the URL to send a team admin to so they can authorize Zoom or
        Microsoft Teams for the team. Redirect their browser to it - the
        provider then returns them to a callback already registered by Cal.com,
        which stores the credential against the team rather than against the
        admin who authorized it. `returnTo` and `onErrorReturnTo` must each be a
        relative path or an absolute http(s) URL. The returned URL expires 10
        minutes after this call, so redirect immediately rather than caching it.
        Walkthrough: https://cal.com/docs/api-reference/v2/conferencing-apps.
        Required membership role: `team admin`. PBAC permission: `team.update`.
        Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control. If accessed using
        an OAuth access token, the `TEAM_APPS_WRITE` scope is required.
      operationId: OrganizationsConferencingController_getTeamOAuthUrl
      parameters:
        - name: Authorization
          required: true
          in: header
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
          description: Conferencing application type
          schema:
            enum:
              - zoom
              - msteams
            type: string
        - name: returnTo
          required: true
          in: query
          schema:
            type: string
        - name: onErrorReturnTo
          required: true
          in: query
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetConferencingAppsOauthUrlResponseDto'
components:
  schemas:
    GetConferencingAppsOauthUrlResponseDto:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
      required:
        - status

````