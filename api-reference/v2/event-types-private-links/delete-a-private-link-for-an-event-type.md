> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a private link for an event type

> If accessed using an OAuth access token, the `EVENT_TYPE_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json delete /v2/event-types/{eventTypeId}/private-links/{linkId}
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
  /v2/event-types/{eventTypeId}/private-links/{linkId}:
    delete:
      tags:
        - Event Types Private Links
      summary: Delete a private link for an event type
      description: >-
        If accessed using an OAuth access token, the `EVENT_TYPE_WRITE` scope is
        required.
      operationId: EventTypesPrivateLinksController_2024_09_04_deletePrivateLink
      parameters:
        - name: cal-api-version
          in: header
          description: >-
            Must be set to `2024-09-04`. Returns the full booking URL including
            org slug and event slug.
          required: true
          schema:
            type: string
            default: '2024-09-04'
        - name: eventTypeId
          required: true
          in: path
          schema:
            type: number
        - name: linkId
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
                $ref: '#/components/schemas/DeletePrivateLinkOutput'
components:
  schemas:
    DeletePrivateLinkOutput:
      type: object
      properties:
        status:
          type: string
          description: Response status
          example: success
        data:
          type: object
          description: Deleted link information
          properties:
            linkId:
              type: string
              example: abc123def456
            message:
              type: string
              example: Private link deleted successfully
      required:
        - status
        - data

````