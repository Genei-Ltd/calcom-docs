> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all OAuth clients

> <Warning>These endpoints are deprecated and will be removed in the future.</Warning>



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/oauth-clients
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
    get:
      tags:
        - 'Deprecated: Platform OAuth Clients'
      summary: Get all OAuth clients
      description: >-
        <Warning>These endpoints are deprecated and will be removed in the
        future.</Warning>
      operationId: OAuthClientsController_getOAuthClients
      parameters:
        - name: Authorization
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_
          required: true
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetOAuthClientsResponseDto'
components:
  schemas:
    GetOAuthClientsResponseDto:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          type: array
          items:
            $ref: '#/components/schemas/PlatformOAuthClientDto'
      required:
        - status
        - data
    PlatformOAuthClientDto:
      type: object
      properties:
        id:
          type: string
          example: clsx38nbl0001vkhlwin9fmt0
        name:
          type: string
          example: MyClient
        secret:
          type: string
          example: secretValue
        permissions:
          type: array
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
          description: Array of permission keys like ["BOOKING_READ", "BOOKING_WRITE"]
          example:
            - BOOKING_READ
            - BOOKING_WRITE
        logo:
          type: string
          nullable: true
          example: https://example.com/logo.png
        redirectUris:
          example:
            - https://example.com/callback
          type: array
          items:
            type: string
        organizationId:
          type: number
          example: 1
        createdAt:
          format: date-time
          type: string
          example: '2024-03-23T08:33:21.851Z'
        areEmailsEnabled:
          type: boolean
          example: true
        areDefaultEventTypesEnabled:
          type: boolean
          example: true
          description: >-
            If enabled, when creating a managed user the managed user will have
            4 default event types: 30 and 60 minutes without Cal video, 30 and
            60 minutes with Cal video. Leave this disabled if you want to create
            a managed user and then manually create event types for the user.
        areCalendarEventsEnabled:
          type: boolean
          example: true
          description: >-
            If true and if managed user has calendar connected, calendar events
            will be created. Disable it if you manually create calendar events.
            Default to true.
        bookingRedirectUri:
          type: string
          format: uri
          example: https://example.com/booking-redirect
        bookingCancelRedirectUri:
          type: string
          format: uri
          example: https://example.com/booking-cancel
        bookingRescheduleRedirectUri:
          type: string
          format: uri
          example: https://example.com/booking-reschedule
      required:
        - id
        - name
        - secret
        - permissions
        - redirectUris
        - organizationId
        - createdAt
        - areEmailsEnabled
        - areDefaultEventTypesEnabled
        - areCalendarEventsEnabled

````