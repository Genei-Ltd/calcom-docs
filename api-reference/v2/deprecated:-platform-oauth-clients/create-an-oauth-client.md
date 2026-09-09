> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create an OAuth client

> <Warning>These endpoints are deprecated and will be removed in the future.</Warning>



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/oauth-clients
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
  /v2/oauth-clients:
    post:
      tags:
        - 'Deprecated: Platform OAuth Clients'
      summary: Create an OAuth client
      description: >-
        <Warning>These endpoints are deprecated and will be removed in the
        future.</Warning>
      operationId: OAuthClientsController_createOAuthClient
      parameters:
        - name: Authorization
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateOAuthClientInput'
      responses:
        '201':
          description: Create an OAuth client
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateOAuthClientResponseDto'
components:
  schemas:
    CreateOAuthClientInput:
      type: object
      properties:
        logo:
          type: string
        name:
          type: string
        redirectUris:
          type: array
          items:
            type: string
        permissions:
          type: array
          description: >-
            Array of permission keys like ["BOOKING_READ", "BOOKING_WRITE"]. Use
            ["*"] to grant all permissions.
          items:
            type: string
            enum:
              - EVENT_TYPE_READ
              - EVENT_TYPE_WRITE
              - BOOKING_READ
              - BOOKING_WRITE
              - SCHEDULE_READ
              - SCHEDULE_WRITE
              - APPS_READ
              - APPS_WRITE
              - PROFILE_READ
              - PROFILE_WRITE
              - '*'
        bookingRedirectUri:
          type: string
        bookingCancelRedirectUri:
          type: string
        bookingRescheduleRedirectUri:
          type: string
        areEmailsEnabled:
          type: boolean
        areDefaultEventTypesEnabled:
          type: boolean
          default: false
          description: >-
            If true, when creating a managed user the managed user will have 4
            default event types: 30 and 60 minutes without Cal video, 30 and 60
            minutes with Cal video. Set this as false if you want to create a
            managed user and then manually create event types for the user.
        areCalendarEventsEnabled:
          type: boolean
          default: true
          description: >-
            If true and if managed user has calendar connected, calendar events
            will be created. Disable it if you manually create calendar events.
            Default to true.
      required:
        - name
        - redirectUris
        - permissions
    CreateOAuthClientResponseDto:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          example:
            clientId: clsx38nbl0001vkhlwin9fmt0
            clientSecret: >-
              eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoib2F1dGgtY2xpZW50Iiwi
          allOf:
            - $ref: '#/components/schemas/CreateOAuthClientOutput'
      required:
        - status
        - data
    CreateOAuthClientOutput:
      type: object
      properties:
        clientId:
          type: string
          example: clsx38nbl0001vkhlwin9fmt0
        clientSecret:
          type: string
          example: >-
            eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoib2F1dGgtY2xpZW50Iiwi
      required:
        - clientId
        - clientSecret

````