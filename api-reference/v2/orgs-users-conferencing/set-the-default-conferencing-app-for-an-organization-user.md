> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Set the default conferencing app for an organization user

> Sets the default conferencing app for a specific user within the organization. If accessed using an OAuth access token, the `APPS_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/organizations/{orgId}/users/{userId}/conferencing/default
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
  /v2/organizations/{orgId}/users/{userId}/conferencing/default:
    post:
      tags:
        - Orgs / Users / Conferencing
      summary: Set the default conferencing app for an organization user
      description: >-
        Sets the default conferencing app for a specific user within the
        organization. If accessed using an OAuth access token, the `APPS_WRITE`
        scope is required.
      operationId: OrganizationsUsersConferencingController_setDefaultConferencingApp
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
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SetDefaultConferencingAppInput'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/SetDefaultConferencingAppOutputResponseDto
components:
  schemas:
    SetDefaultConferencingAppInput:
      type: object
      properties:
        appSlug:
          type: string
          description: The slug of the conferencing app to set as default
          example: google-meet
          enum:
            - google-meet
            - zoom
            - msteams
            - daily-video
      required:
        - appSlug
    SetDefaultConferencingAppOutputResponseDto:
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