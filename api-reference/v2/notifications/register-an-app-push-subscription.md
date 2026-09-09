> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Register an app push subscription



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/notifications/subscriptions/app-push
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
    post:
      tags:
        - Notifications
      summary: Register an app push subscription
      operationId: NotificationsSubscriptionsController_register
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
              $ref: '#/components/schemas/RegisterAppPushSubscriptionInput'
      responses:
        '201':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AppPushSubscriptionResponseDto'
components:
  schemas:
    RegisterAppPushSubscriptionInput:
      type: object
      properties:
        token:
          type: string
          description: Expo Push Token
          example: ExponentPushToken[xxxxxxxxxxxxxxxxxxxxxx]
        platform:
          enum:
            - IOS
            - ANDROID
          type: string
          description: Mobile platform
          example: IOS
        deviceId:
          type: string
          description: Unique device identifier
          example: device-uuid-123
      required:
        - token
        - platform
        - deviceId
    AppPushSubscriptionResponseDto:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/AppPushSubscriptionOutputDto'
      required:
        - status
        - data
    AppPushSubscriptionOutputDto:
      type: object
      properties:
        id:
          type: number
        userId:
          type: number
        type:
          type: string
        platform:
          type: string
        identifier:
          type: string
        deviceId:
          type: string
          nullable: true
        createdAt:
          format: date-time
          type: string
        updatedAt:
          format: date-time
          type: string
      required:
        - id
        - userId
        - type
        - platform
        - identifier
        - deviceId
        - createdAt
        - updatedAt

````