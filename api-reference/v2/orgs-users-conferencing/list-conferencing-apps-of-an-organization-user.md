> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List conferencing apps of an organization user

> Lists all connected conferencing apps for a specific user within the organization, including which one is set as default. If accessed using an OAuth access token, the `APPS_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/organizations/{orgId}/users/{userId}/conferencing
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
  /v2/organizations/{orgId}/users/{userId}/conferencing:
    get:
      tags:
        - Orgs / Users / Conferencing
      summary: List conferencing apps of an organization user
      description: >-
        Lists all connected conferencing apps for a specific user within the
        organization, including which one is set as default. If accessed using
        an OAuth access token, the `APPS_READ` scope is required.
      operationId: OrganizationsUsersConferencingController_listConferencingApps
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
        - name: userId
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
                  #/components/schemas/ConferencingAppsWithDefaultOutputResponseDto
components:
  schemas:
    ConferencingAppsWithDefaultOutputResponseDto:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
        data:
          type: array
          items:
            $ref: '#/components/schemas/ConferencingAppsWithDefaultOutputDto'
      required:
        - status
        - data
    ConferencingAppsWithDefaultOutputDto:
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
        appSlug:
          type: string
          example: google-meet
          description: Slug of the conferencing app
        isDefault:
          type: boolean
          example: false
          description: Whether this app is the user's default conferencing app
      required:
        - id
        - type
        - userId
        - appSlug
        - isDefault

````