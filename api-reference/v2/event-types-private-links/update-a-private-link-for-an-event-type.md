> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a private link for an event type

> If accessed using an OAuth access token, the `EVENT_TYPE_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json patch /v2/event-types/{eventTypeId}/private-links/{linkId}
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
    patch:
      tags:
        - Event Types Private Links
      summary: Update a private link for an event type
      description: >-
        If accessed using an OAuth access token, the `EVENT_TYPE_WRITE` scope is
        required.
      operationId: EventTypesPrivateLinksController_2024_09_04_updatePrivateLink
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
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdatePrivateLinkBody'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UpdatePrivateLinkOutput'
components:
  schemas:
    UpdatePrivateLinkBody:
      type: object
      properties:
        expiresAt:
          format: date-time
          type: string
          description: New expiration date for time-based links
          example: '2024-12-31T23:59:59.000Z'
        maxUsageCount:
          type: number
          description: >-
            New maximum number of times the link can be used. Pass `-1` to opt
            out of the count cap.
          example: 10
    UpdatePrivateLinkOutput:
      type: object
      properties:
        status:
          type: string
          description: Response status
          example: success
        data:
          description: Updated private link data (either time-based or usage-based)
          oneOf:
            - $ref: '#/components/schemas/TimeBasedPrivateLinkOutput'
            - $ref: '#/components/schemas/UsageBasedPrivateLinkOutput'
      required:
        - status
        - data
    TimeBasedPrivateLinkOutput:
      type: object
      properties:
        linkId:
          type: string
          description: The private link ID
          example: abc123def456
        eventTypeId:
          type: number
          description: Event type ID this link belongs to
          example: 123
        isExpired:
          type: boolean
          description: Whether the link is currently expired
          example: false
        bookingUrl:
          type: string
          description: >-
            Full booking URL for this private link (deprecated endpoints return
            hash-only URL without event slug)
          format: uri
          example: https://cal.com/d/abc123def456
        expiresAt:
          type: string
          description: Expiration date for this time-based link
          format: date-time
          example: '2025-12-31T23:59:59.000Z'
      required:
        - linkId
        - eventTypeId
        - isExpired
        - bookingUrl
        - expiresAt
    UsageBasedPrivateLinkOutput:
      type: object
      properties:
        linkId:
          type: string
          description: The private link ID
          example: abc123def456
        eventTypeId:
          type: number
          description: Event type ID this link belongs to
          example: 123
        isExpired:
          type: boolean
          description: Whether the link is currently expired
          example: false
        bookingUrl:
          type: string
          description: >-
            Full booking URL for this private link (deprecated endpoints return
            hash-only URL without event slug)
          format: uri
          example: https://cal.com/d/abc123def456
        maxUsageCount:
          type: number
          description: Maximum number of times this link can be used
          example: 10
        usageCount:
          type: number
          description: Current usage count for this link
          example: 3
      required:
        - linkId
        - eventTypeId
        - isExpired
        - bookingUrl
        - maxUsageCount
        - usageCount

````