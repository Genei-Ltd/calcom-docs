> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Remove a Telegram push subscription



## OpenAPI

````yaml /api-reference/v2/openapi.json delete /v2/notifications/subscriptions/telegram
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
  /v2/notifications/subscriptions/telegram:
    delete:
      tags:
        - Notifications
      summary: Remove a Telegram push subscription
      operationId: NotificationsChatSubscriptionsController_removeTelegram
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
              $ref: '#/components/schemas/RemoveChatSubscriptionInput'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RemoveTelegramSubscriptionResponseDto'
components:
  schemas:
    RemoveChatSubscriptionInput:
      type: object
      properties:
        identifier:
          type: string
          description: Chat platform identifier to remove
          example: U0123456789
      required:
        - identifier
    RemoveTelegramSubscriptionResponseDto:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        message:
          type: string
          example: Telegram subscription removed successfully
      required:
        - status
        - message

````