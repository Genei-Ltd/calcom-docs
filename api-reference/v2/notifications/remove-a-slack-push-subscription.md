> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Remove a Slack push subscription



## OpenAPI

````yaml /api-reference/v2/openapi.json delete /v2/notifications/subscriptions/slack
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
  /v2/notifications/subscriptions/slack:
    delete:
      tags:
        - Notifications
      summary: Remove a Slack push subscription
      operationId: NotificationsChatSubscriptionsController_removeSlack
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
              $ref: '#/components/schemas/RemoveSlackSubscriptionInput'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RemoveSlackSubscriptionResponseDto'
components:
  schemas:
    RemoveSlackSubscriptionInput:
      type: object
      properties:
        identifier:
          type: string
          description: Slack user ID
          example: U0123456789
        teamId:
          type: string
          description: Slack team (workspace) ID
          example: T0123456789
      required:
        - identifier
        - teamId
    RemoveSlackSubscriptionResponseDto:
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
          example: Slack subscription removed successfully
      required:
        - status
        - message

````