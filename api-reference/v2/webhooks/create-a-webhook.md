> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a webhook

> If accessed using an OAuth access token, the `WEBHOOK_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/webhooks
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
  /v2/webhooks:
    post:
      tags:
        - Webhooks
      summary: Create a webhook
      description: >-
        If accessed using an OAuth access token, the `WEBHOOK_WRITE` scope is
        required.
      operationId: WebhooksController_createWebhook
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
              $ref: '#/components/schemas/CreateWebhookInputDto'
      responses:
        '201':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserWebhookOutputResponseDto'
components:
  schemas:
    CreateWebhookInputDto:
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
        active:
          type: boolean
        subscriberUrl:
          type: string
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
              - BOOKING_LOCATION_UPDATED
              - BOOKING_REASSIGNED
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
          example:
            - BOOKING_CREATED
            - BOOKING_RESCHEDULED
            - BOOKING_CANCELLED
            - BOOKING_CONFIRMED
            - BOOKING_REJECTED
            - BOOKING_COMPLETED
            - BOOKING_NO_SHOW
            - BOOKING_REOPENED
        secret:
          type: string
        version:
          enum:
            - '2021-10-20'
            - '2026-07-27'
          type: string
          description: >-
            The payload format version of the webhook. Version 2026-07-27 adds
            generated ICS calendar content (`attendeeIcsContent`,
            `organizerIcsContent`) to BOOKING_CREATED, BOOKING_RESCHEDULED,
            BOOKING_CANCELLED, and BOOKING_PAID (when the payment accepted the
            booking) payloads.
          example: '2021-10-20'
        time:
          type: number
          minimum: 1
          description: >-
            How long after the booking start time the no-show triggers are
            evaluated. Required, together with timeUnit, when subscribing to
            AFTER_HOSTS_CAL_VIDEO_NO_SHOW or AFTER_GUESTS_CAL_VIDEO_NO_SHOW
          example: 5
        timeUnit:
          enum:
            - DAY
            - HOUR
            - MINUTE
          type: string
          description: The unit of the no-show time value
          example: MINUTE
      required:
        - active
        - subscriberUrl
        - triggers
    UserWebhookOutputResponseDto:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/UserWebhookOutputDto'
      required:
        - status
        - data
    UserWebhookOutputDto:
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
              - BOOKING_LOCATION_UPDATED
              - BOOKING_REASSIGNED
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
        time:
          type: number
          description: >-
            How long after the booking start time the no-show triggers are
            evaluated
          example: 5
        timeUnit:
          enum:
            - DAY
            - HOUR
            - MINUTE
          type: string
          description: The unit of the no-show time value
          example: MINUTE
        version:
          enum:
            - '2021-10-20'
            - '2026-07-27'
          type: string
          description: >-
            The payload format version of the webhook. Version 2026-07-27 adds
            generated ICS calendar content (`attendeeIcsContent`,
            `organizerIcsContent`) to BOOKING_CREATED, BOOKING_RESCHEDULED,
            BOOKING_CANCELLED, and BOOKING_PAID (when the payment accepted the
            booking) payloads.
          example: '2021-10-20'
        userId:
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
        - version
        - userId
        - id
        - subscriberUrl
        - active

````