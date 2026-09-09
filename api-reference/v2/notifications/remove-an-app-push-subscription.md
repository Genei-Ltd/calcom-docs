> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Remove an app push subscription



## OpenAPI

````yaml /api-reference/v2/openapi.json delete /v2/notifications/subscriptions/app-push
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
  /v2/notifications/subscriptions/app-push:
    delete:
      tags:
        - Notifications
      summary: Remove an app push subscription
      operationId: NotificationsSubscriptionsController_remove
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
              $ref: '#/components/schemas/RemoveAppPushSubscriptionInput'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RemoveAppPushSubscriptionResponseDto'
components:
  schemas:
    RemoveAppPushSubscriptionInput:
      type: object
      properties:
        token:
          type: string
          description: Expo Push Token to remove
          example: ExponentPushToken[xxxxxxxxxxxxxxxxxxxxxx]
      required:
        - token
    RemoveAppPushSubscriptionResponseDto:
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
          example: App push subscription removed successfully
      required:
        - status
        - message

````