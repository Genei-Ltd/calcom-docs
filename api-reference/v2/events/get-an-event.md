> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get an Event

> Returns one Event by UUID. The authenticated user must be its owner, one of its hosts, an accepted co-host, or a member of the owning team with permission to read its event types. Events are fixed-date RSVP pages served at cal.com/{slug}; they are not event types (bookable meeting templates) or calendar events.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/events/{uuid}
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
  /v2/events/{uuid}:
    get:
      tags:
        - Events
      summary: Get an Event
      description: >-
        Returns one Event by UUID. The authenticated user must be its owner, one
        of its hosts, an accepted co-host, or a member of the owning team with
        permission to read its event types. Events are fixed-date RSVP pages
        served at cal.com/{slug}; they are not event types (bookable meeting
        templates) or calendar events.
      operationId: EventsController_get
      parameters:
        - name: uuid
          required: true
          in: path
          schema:
            type: string
        - name: Authorization
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_, managed user access token, or OAuth access token
          required: true
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EventOutputResponseDto'
        '400':
          description: Invalid Event UUID
        '401':
          description: Unauthenticated
        '403':
          description: Insufficient permissions
        '404':
          description: Event not found
components:
  schemas:
    EventOutputResponseDto:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/EventOutputDto'
      required:
        - status
        - data
    EventOutputDto:
      type: object
      properties:
        uuid:
          type: string
          description: Unique identifier of the Event.
        slug:
          type: string
        title:
          type: string
        description:
          type: string
          nullable: true
        startTime:
          format: date-time
          type: string
        endTime:
          format: date-time
          type: string
        timeZone:
          type: string
        visibility:
          enum:
            - PUBLIC
            - UNLISTED
          type: string
        hidden:
          type: boolean
        publishedAt:
          format: date-time
          type: string
          nullable: true
        cancelledAt:
          format: date-time
          type: string
          nullable: true
        locations:
          type: array
          items:
            oneOf:
              - $ref: '#/components/schemas/EventAddressLocationOutput'
                title: Address
              - $ref: '#/components/schemas/EventLinkLocationOutput'
                title: Link
              - $ref: '#/components/schemas/EventIntegrationLocationOutput'
                title: Integration
              - $ref: '#/components/schemas/EventOrganizersDefaultAppLocationOutput'
                title: Organizer Default App
        coverImageUrl:
          type: string
          nullable: true
        requiresApproval:
          type: boolean
        waitlistEnabled:
          type: boolean
        confirmedCount:
          type: number
          description: >-
            Confirmed guest count. Returned when listing Events and omitted when
            fetching a single Event by uuid.
      required:
        - uuid
        - slug
        - title
        - startTime
        - endTime
        - timeZone
        - visibility
        - hidden
        - locations
        - requiresApproval
        - waitlistEnabled
    EventAddressLocationOutput:
      type: object
      properties:
        type:
          type: string
          example: address
          enum:
            - address
        address:
          type: string
          example: 123 Event Street
      required:
        - type
        - address
    EventLinkLocationOutput:
      type: object
      properties:
        type:
          type: string
          example: link
          enum:
            - link
        link:
          type: string
          example: https://example.com/event
      required:
        - type
        - link
    EventIntegrationLocationOutput:
      type: object
      properties:
        type:
          type: string
          example: integration
          enum:
            - integration
        integration:
          enum:
            - cal-video
            - google-meet
            - zoom
            - whereby-video
            - whatsapp-video
            - webex-video
            - telegram-video
            - tandem
            - sylaps-video
            - skype-video
            - sirius-video
            - signal-video
            - shimmer-video
            - salesroom-video
            - roam-video
            - riverside-video
            - ping-video
            - office365-video
            - mirotalk-video
            - jitsi
            - jelly-video
            - jelly-conferencing
            - huddle
            - facetime-video
            - element-call-video
            - eightxeight-video
            - discord-video
            - demodesk-video
            - campfire-video
          type: string
          example: cal-video
        credentialId:
          type: number
          description: >-
            Identifies which connected account will host the Event when a host
            has multiple connected accounts.
      required:
        - type
        - integration
    EventOrganizersDefaultAppLocationOutput:
      type: object
      properties:
        type:
          type: string
          example: organizersDefaultApp
          enum:
            - organizersDefaultApp
      required:
        - type

````