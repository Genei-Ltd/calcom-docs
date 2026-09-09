> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all webhooks

> If accessed using an OAuth access token, the `EVENT_TYPE_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/event-types/{eventTypeId}/webhooks
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
  /v2/event-types/{eventTypeId}/webhooks:
    get:
      tags:
        - Event Types / Webhooks
      summary: Get all webhooks
      description: >-
        If accessed using an OAuth access token, the `EVENT_TYPE_READ` scope is
        required.
      operationId: EventTypeWebhooksController_getEventTypeWebhooks
      parameters:
        - name: Authorization
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_, managed user access token, or OAuth access token
          required: true
          schema:
            type: string
        - name: eventTypeId
          required: true
          in: path
          schema:
            type: number
        - name: take
          required: false
          in: query
          description: Maximum number of items to return
          schema:
            minimum: 1
            maximum: 250
            default: 250
            example: 25
            type: number
        - name: skip
          required: false
          in: query
          description: Number of items to skip
          schema:
            minimum: 0
            default: 0
            example: 0
            type: number
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EventTypeWebhooksOutputResponseDto'
components:
  schemas:
    EventTypeWebhooksOutputResponseDto:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          type: array
          items:
            $ref: '#/components/schemas/EventTypeWebhookOutputDto'
      required:
        - status
        - data
    EventTypeWebhookOutputDto:
      type: object
      properties:
        payloadTemplate:
          type: string
          description: >-
            The template of the payload that will be sent to the subscriberUrl,
            check cal.com/docs/core-features/webhooks for more information
          example: >-
            {"content":"A new event has been
            scheduled","type":"{{type}}","name":"{{title}}","organizer":"{{organizer.name}}","booker":"{{attendees.0.name}}"}
        triggers:
          type: array
          items:
            type: string
            enum:
              - BOOKING_CREATED
              - BOOKING_PAYMENT_INITIATED
              - BOOKING_PAID
              - BOOKING_RESCHEDULED
              - BOOKING_REQUESTED
              - BOOKING_CANCELLED
              - BOOKING_REJECTED
              - BOOKING_NO_SHOW_UPDATED
              - FORM_SUBMITTED
              - MEETING_ENDED
              - MEETING_STARTED
              - RECORDING_READY
              - INSTANT_MEETING
              - INSTANT_MEETING_ACCEPTED
              - RECORDING_TRANSCRIPTION_GENERATED
              - OOO_CREATED
              - AFTER_HOSTS_CAL_VIDEO_NO_SHOW
              - AFTER_GUESTS_CAL_VIDEO_NO_SHOW
              - FORM_SUBMITTED_NO_EVENT
              - ROUTING_FORM_FALLBACK_HIT
              - DELEGATION_CREDENTIAL_ERROR
              - WRONG_ASSIGNMENT_REPORT
              - DELEGATION_CREDENTIAL_SECRET_ROTATION_FAILED
              - DELEGATION_CREDENTIAL_ROTATION_REQUIRED
              - DELEGATION_CREDENTIAL_SECRET_ROTATED
              - CALENDAR_ENTRY_REJECTED
        eventTypeId:
          type: number
        id:
          type: number
        subscriberUrl:
          type: string
        active:
          type: boolean
        secret:
          type: string
      required:
        - payloadTemplate
        - triggers
        - eventTypeId
        - id
        - subscriberUrl
        - active

````