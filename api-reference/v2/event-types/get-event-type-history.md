> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get event type history

> <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>

If accessed using an OAuth access token, the `EVENT_TYPE_READ` scope is required.

Access control: This endpoint returns audit history using the same owner/admin-style audit-history access policy as the app/tRPC history query. Having general event type read access does not by itself grant access to audit history.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/event-types/{eventTypeId}/history
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
  /v2/event-types/{eventTypeId}/history:
    get:
      tags:
        - Event Types
      summary: Get event type history
      description: >-
        <Note>Please make sure to pass in the cal-api-version header value as
        mentioned in the Headers section. Not passing the correct value will
        default to an older version of this endpoint.</Note>


        If accessed using an OAuth access token, the `EVENT_TYPE_READ` scope is
        required.


        Access control: This endpoint returns audit history using the same
        owner/admin-style audit-history access policy as the app/tRPC history
        query. Having general event type read access does not by itself grant
        access to audit history.
      operationId: EventTypesController_2024_06_14_getEventTypeHistory
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
        - name: limit
          required: false
          in: query
          description: >-
            The number of audit logs to return. Defaults to 25 and cannot exceed
            50.
          schema:
            minimum: 1
            maximum: 50
            example: 25
            type: number
        - name: cursor
          required: false
          in: query
          description: >-
            Cursor from the previous response. Pass `pagination.nextCursor` to
            fetch the next page of audit logs.
          schema:
            maxLength: 2048
            example: >-
              eyJjcmVhdGVkQXQiOiIyMDI2LTAxLTAxVDAwOjAwOjAwLjAwMFoiLCJpZCI6IjAxSFgifQ
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
                $ref: '#/components/schemas/GetEventTypeHistoryOutput_2024_06_14'
components:
  schemas:
    GetEventTypeHistoryOutput_2024_06_14:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
          description: Indicates whether the request was successful.
        data:
          description: The event type history data including audit log entries.
          allOf:
            - $ref: '#/components/schemas/EventTypeHistoryData_2024_06_14'
        pagination:
          description: Pagination metadata for fetching additional pages.
          allOf:
            - $ref: '#/components/schemas/EventTypeHistoryPagination_2024_06_14'
      required:
        - status
        - data
        - pagination
    EventTypeHistoryData_2024_06_14:
      type: object
      properties:
        eventTypeId:
          type: number
          example: 123
          description: The ID of the event type whose history is being returned.
        auditLogs:
          description: >-
            List of audit log entries for the event type, ordered by most recent
            first.
          type: array
          items:
            $ref: '#/components/schemas/EventTypeHistoryAuditLog_2024_06_14'
      required:
        - eventTypeId
        - auditLogs
    EventTypeHistoryPagination_2024_06_14:
      type: object
      properties:
        nextCursor:
          type: string
          nullable: true
          description: >-
            Opaque cursor to fetch the next page. Pass this value as the
            `cursor` query parameter on the next request. `null` when `hasMore`
            is `false`.
          example: >-
            eyJjcmVhdGVkQXQiOiIyMDI2LTAxLTAxVDAwOjAwOjAwLjAwMFoiLCJpZCI6IjAxSFgifQ
        hasMore:
          type: boolean
          description: Whether more pages are available after this one.
          example: false
      required:
        - nextCursor
        - hasMore
    EventTypeHistoryAuditLog_2024_06_14:
      type: object
      properties:
        id:
          type: string
          example: 018f4c2e-3f1a-7abc-9def-0123456789ab
          description: Unique identifier of the audit log entry.
        action:
          type: string
          enum:
            - EVENT_TYPE_MODIFIED
            - EVENT_TYPE_CREATED
            - EVENT_TYPE_DELETED
          example: EVENT_TYPE_MODIFIED
          description: The type of change that was made to the event type.
        type:
          type: string
          example: RECORD_MODIFIED
          description: The category of audit record.
        timestamp:
          type: string
          example: '2026-01-01T00:00:00.000Z'
          description: ISO 8601 timestamp of when the change occurred.
        source:
          type: string
          example: WEBAPP
          description: The source application or context where the change was made.
        actor:
          description: The user or system that performed the change.
          allOf:
            - $ref: '#/components/schemas/EventTypeHistoryActor_2024_06_14'
        impersonatedBy:
          nullable: true
          description: >-
            Present when the action was performed via user impersonation.
            Contains details of the impersonated user.
          allOf:
            - $ref: '#/components/schemas/EventTypeHistoryImpersonatedBy_2024_06_14'
        actionDisplayTitle:
          type: string
          example: Ada Lovelace modified the event type
          description: Human-readable English summary of who performed the action.
        displayFields:
          description: List of fields that were changed, with their old and new values.
          type: array
          items:
            $ref: '#/components/schemas/EventTypeHistoryDisplayField_2024_06_14'
        displayJson:
          type: object
          nullable: true
          description: >-
            Raw JSON representation of the full change payload, or null if
            unavailable.
        hasError:
          type: boolean
          example: false
          description: Whether an error occurred while parsing the audit log entry.
      required:
        - id
        - action
        - type
        - timestamp
        - source
        - actor
        - actionDisplayTitle
        - displayFields
        - displayJson
    EventTypeHistoryActor_2024_06_14:
      type: object
      properties:
        type:
          type: string
          enum:
            - USER
            - GUEST
            - ATTENDEE
            - SYSTEM
            - APP
          example: USER
          description: The type of actor who performed the action.
        displayName:
          type: string
          nullable: true
          example: Ada Lovelace
          description: Display name of the actor, or null if unavailable.
        displayEmail:
          type: string
          nullable: true
          example: ada@example.com
          description: Email address of the actor, or null if unavailable.
        displayAvatar:
          type: string
          nullable: true
          example: https://example.com/avatar.png
          description: Avatar URL of the actor, or null if unavailable.
      required:
        - type
        - displayName
        - displayEmail
        - displayAvatar
    EventTypeHistoryImpersonatedBy_2024_06_14:
      type: object
      properties:
        displayName:
          type: string
          example: Grace Hopper
          description: Display name of the user who was being impersonated.
        displayEmail:
          type: string
          nullable: true
          example: grace@example.com
          description: Email address of the impersonated user, or null if unavailable.
        displayAvatar:
          type: string
          nullable: true
          example: https://example.com/avatar.png
          description: Avatar URL of the impersonated user, or null if unavailable.
      required:
        - displayName
        - displayEmail
        - displayAvatar
    EventTypeHistoryDisplayField_2024_06_14:
      type: object
      properties:
        label:
          type: string
          example: Duration
          description: Human-readable English label for the changed field.
        fieldValue:
          oneOf:
            - $ref: '#/components/schemas/RawValueFieldValue_2024_06_14'
            - $ref: '#/components/schemas/RawValuesFieldValue_2024_06_14'
            - $ref: '#/components/schemas/ValueChangeFieldValue_2024_06_14'
            - $ref: '#/components/schemas/DiffFieldValue_2024_06_14'
          discriminator:
            propertyName: type
            mapping:
              rawValue:
                $ref: '#/components/schemas/RawValueFieldValue_2024_06_14'
              rawValues:
                $ref: '#/components/schemas/RawValuesFieldValue_2024_06_14'
              valueChange:
                $ref: '#/components/schemas/ValueChangeFieldValue_2024_06_14'
              diff:
                $ref: '#/components/schemas/DiffFieldValue_2024_06_14'
          description: >-
            The field value, discriminated by `type`. Each variant includes only
            its relevant required fields.
      required:
        - label
        - fieldValue
    RawValueFieldValue_2024_06_14:
      type: object
      properties:
        type:
          type: string
          enum:
            - rawValue
          description: Discriminator indicating this field holds a single plain-text value.
        value:
          type: string
          example: enabled
          description: The plain-text value of the field.
      required:
        - type
        - value
    RawValuesFieldValue_2024_06_14:
      type: object
      properties:
        type:
          type: string
          enum:
            - rawValues
          description: >-
            Discriminator indicating this field holds a list of plain-text
            values.
        values:
          example:
            - Google Meet
            - Cal Video
          description: List of plain-text values.
          type: array
          items:
            type: string
      required:
        - type
        - values
    ValueChangeFieldValue_2024_06_14:
      type: object
      properties:
        type:
          type: string
          enum:
            - valueChange
          description: >-
            Discriminator indicating a primitive value changed from one value to
            another.
        previous:
          type: string
          example: '30'
          description: The value before the change.
        next:
          type: string
          example: '60'
          description: The value after the change.
      required:
        - type
        - previous
        - next
    DiffFieldValue_2024_06_14:
      type: object
      properties:
        type:
          type: string
          enum:
            - diff
          description: >-
            Discriminator indicating this field contains a JSON diff of complex
            (object/array) values.
        previous:
          type: string
          example: '{"key": "old"}'
          description: JSON-stringified previous value.
        next:
          type: string
          example: '{"key": "new"}'
          description: JSON-stringified new value.
      required:
        - type
        - previous
        - next

````