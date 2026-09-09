> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a Telegram push linking intent



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/notifications/subscriptions/telegram/link-intents
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
  /v2/notifications/subscriptions/telegram/link-intents:
    post:
      tags:
        - Notifications
      summary: Create a Telegram push linking intent
      operationId: NotificationsChatSubscriptionsController_createTelegramLinkIntent
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
        '201':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ChatPushLinkIntentResponseDto'
components:
  schemas:
    ChatPushLinkIntentResponseDto:
      type: object
      properties:
        status:
          type: string
          enum:
            - success
          example: success
        data:
          $ref: '#/components/schemas/ChatPushLinkIntentOutputDto'
      required:
        - status
        - data
    ChatPushLinkIntentOutputDto:
      type: object
      properties:
        token:
          type: string
          description: Opaque one-time token for Companion
        expiresAt:
          format: date-time
          type: string
          description: When the one-time token expires
      required:
        - token
        - expiresAt

````