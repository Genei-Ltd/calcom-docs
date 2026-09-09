> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete all webhooks

> If accessed using an OAuth access token, the `EVENT_TYPE_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json delete /v2/event-types/{eventTypeId}/webhooks
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
    delete:
      tags:
        - Event Types / Webhooks
      summary: Delete all webhooks
      description: >-
        If accessed using an OAuth access token, the `EVENT_TYPE_WRITE` scope is
        required.
      operationId: EventTypeWebhooksController_deleteAllEventTypeWebhooks
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
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeleteManyWebhooksOutputResponseDto'
components:
  schemas:
    DeleteManyWebhooksOutputResponseDto:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          type: string
      required:
        - status
        - data

````