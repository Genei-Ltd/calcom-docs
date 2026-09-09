> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List CRM sync errors for an event type

> <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>

Returns CRM sync errors scoped to the requested event type and CRM app. By default this endpoint returns only active errors. Pass `includeDismissed=true` to include dismissed historical errors.

If accessed using an OAuth access token, the `EVENT_TYPE_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/event-types/{eventTypeId}/crm-sync-errors
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
  /v2/event-types/{eventTypeId}/crm-sync-errors:
    get:
      tags:
        - Event Types
      summary: List CRM sync errors for an event type
      description: >-
        <Note>Please make sure to pass in the cal-api-version header value as
        mentioned in the Headers section. Not passing the correct value will
        default to an older version of this endpoint.</Note>


        Returns CRM sync errors scoped to the requested event type and CRM app.
        By default this endpoint returns only active errors. Pass
        `includeDismissed=true` to include dismissed historical errors.


        If accessed using an OAuth access token, the `EVENT_TYPE_READ` scope is
        required.
      operationId: EventTypesController_2024_06_14_getCrmSyncErrors
      parameters:
        - name: cal-api-version
          in: header
          description: >-
            Must be set to 2024-06-14. If not set to this value, the endpoint
            will default to an older version.
          required: true
          schema:
            type: string
            default: '2024-06-14'
        - name: eventTypeId
          required: true
          in: path
          schema:
            type: number
        - name: appSlug
          required: true
          in: query
          description: CRM app slug connected to the event type, for example `salesforce`.
          schema:
            type: string
            example: salesforce
        - name: includeDismissed
          required: false
          in: query
          description: >-
            When true, returns dismissed historical errors as well as active
            errors. Defaults to false.
          schema:
            default: false
            example: true
            type: boolean
        - name: cursor
          required: false
          in: query
          description: >-
            Opaque cursor from `pagination.nextCursor`. Omit to fetch the first
            page of CRM sync errors.
          schema:
            example: >-
              eyJ2IjoxLCJzb3J0VXVpZCI6IjAxOWVhODUwLWVmYzctN2E0OC04NTA4LWFlZDMxYjcyY2U2OCJ9
            type: string
        - name: limit
          required: false
          in: query
          description: Maximum number of CRM sync errors to return.
          schema:
            minimum: 1
            maximum: 100
            default: 50
            example: 50
            type: number
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
                $ref: '#/components/schemas/GetCrmSyncErrorsOutput_2024_06_14'
components:
  schemas:
    GetCrmSyncErrorsOutput_2024_06_14:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          description: >-
            CRM sync errors scoped to the requested event type and connected CRM
            app.
          type: array
          items:
            $ref: '#/components/schemas/CrmSyncErrorOutput_2024_06_14'
        pagination:
          $ref: '#/components/schemas/CrmSyncErrorsPaginationOutput_2024_06_14'
      required:
        - status
        - data
        - pagination
    CrmSyncErrorOutput_2024_06_14:
      type: object
      properties:
        id:
          type: string
          description: Unique CRM sync error ID.
          example: 019ea850-efc7-7a48-8508-aed31b72ce68
        credentialId:
          type: number
          description: Credential ID that produced the CRM sync error.
          example: 123
        eventTypeId:
          type: number
          description: Event type ID where the CRM sync error occurred.
          example: 49
        appSlug:
          type: string
          description: CRM app slug that produced the error.
          example: salesforce
        timestamp:
          type: string
          description: Timestamp when the CRM sync error was recorded.
          example: '2026-06-08T17:38:57.107Z'
        errorCode:
          type: string
          description: Provider-specific CRM error code.
          example: FIELD_CUSTOM_VALIDATION_EXCEPTION
        errorMessage:
          type: string
          description: Human-readable CRM error message.
          example: Validation rule blocked this update
        rawMessage:
          type: string
          description: Raw provider error message, when available.
          example: >-
            FIELD_CUSTOM_VALIDATION_EXCEPTION: Validation rule blocked this
            update
        droppedFields:
          description: CRM fields dropped or attempted during sync error handling.
          example:
            - Custom_Field__c
          type: array
          items:
            type: string
        eventCreated:
          type: boolean
          nullable: true
          description: Whether the CRM event was created before the error was recorded.
          example: false
        bookingUid:
          type: string
          description: Booking UID associated with the CRM sync error, when available.
          example: booking_uid_123
        dismissedAt:
          type: string
          nullable: true
          description: >-
            Timestamp when the CRM sync error was dismissed. Null means the
            error is active.
          example: '2026-06-08T17:40:00.000Z'
      required:
        - id
        - credentialId
        - eventTypeId
        - appSlug
        - timestamp
        - errorCode
        - errorMessage
        - droppedFields
        - dismissedAt
    CrmSyncErrorsPaginationOutput_2024_06_14:
      type: object
      properties:
        nextCursor:
          type: string
          nullable: true
          description: >-
            Opaque cursor for the next page, or null when no more rows are
            available.
          example: >-
            eyJ2IjoxLCJzb3J0VXVpZCI6IjAxOWVhODUwLWVmYzctN2E0OC04NTA4LWFlZDMxYjcyY2U2OCJ9
        hasMore:
          type: boolean
          description: Whether more CRM sync error rows are available.
          example: true
      required:
        - nextCursor
        - hasMore

````