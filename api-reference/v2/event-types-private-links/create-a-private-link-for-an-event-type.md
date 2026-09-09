> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a private link for an event type

> If accessed using an OAuth access token, the `EVENT_TYPE_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/event-types/{eventTypeId}/private-links
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
  /v2/event-types/{eventTypeId}/private-links:
    post:
      tags:
        - Event Types Private Links
      summary: Create a private link for an event type
      description: >-
        If accessed using an OAuth access token, the `EVENT_TYPE_WRITE` scope is
        required.
      operationId: EventTypesPrivateLinksController_2024_09_04_createPrivateLink
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
              $ref: '#/components/schemas/CreatePrivateLinkInput'
      responses:
        '201':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreatePrivateLinkOutput'
components:
  schemas:
    CreatePrivateLinkInput:
      type: object
      properties:
        expiresAt:
          type: string
          description: Expiration date for time-based links
          format: date-time
          example: '2024-12-31T23:59:59.000Z'
        maxUsageCount:
          type: number
          description: >-
            Maximum number of times the link can be used. Pass `-1` to opt out
            of the count cap (the link is then gated only by `expiresAt`, or
            unbounded if that is also unset). If omitted and expiresAt is not
            provided, defaults to 1 (one time use).
          example: 10
          default: 1
    CreatePrivateLinkOutput:
      type: object
      properties:
        status:
          type: string
          description: Response status
          example: success
        data:
          description: Created private link data (either time-based or usage-based)
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