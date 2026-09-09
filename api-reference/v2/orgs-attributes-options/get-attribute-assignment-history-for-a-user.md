> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get attribute assignment history for a user

> Required membership role: `org admin`. PBAC permission: `organization.attributes.readAuditLogs`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/organizations/{orgId}/attributes/assignments/{userId}/history
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
  /v2/organizations/{orgId}/attributes/assignments/{userId}/history:
    get:
      tags:
        - Orgs / Attributes / Options
      summary: Get attribute assignment history for a user
      description: >-
        Required membership role: `org admin`. PBAC permission:
        `organization.attributes.readAuditLogs`. Learn more about API access
        control at https://cal.com/docs/api-reference/v2/access-control
      operationId: >-
        OrganizationsAttributesOptionsController_getOrganizationAttributeAssignmentHistory
      parameters:
        - name: Authorization
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_
          required: true
          schema:
            type: string
        - name: orgId
          required: true
          in: path
          schema:
            type: number
        - name: userId
          required: true
          in: path
          schema:
            type: number
        - name: limit
          required: false
          in: query
          description: Maximum number of audit log entries to return.
          schema:
            minimum: 1
            maximum: 50
            default: 25
            type: number
        - name: cursor
          required: false
          in: query
          description: Cursor from the previous response.
          schema:
            format: uuid
            example: 018ff5cd-6dc4-7d57-bcbc-374702ca8b38
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetAttributeAssignmentHistoryOutput'
components:
  schemas:
    GetAttributeAssignmentHistoryOutput:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          description: The attribute assignment history response payload.
          allOf:
            - $ref: '#/components/schemas/AttributeAssignmentHistoryDataOutput'
      required:
        - status
        - data
    AttributeAssignmentHistoryDataOutput:
      type: object
      properties:
        userId:
          type: number
          description: The ID of the user whose attribute assignment history was requested.
          example: 5
        membershipId:
          type: number
          description: The organization membership ID for the requested user.
          example: 42
        auditLogs:
          description: >-
            The paginated audit log entries for the user's attribute
            assignments.
          type: array
          items:
            $ref: '#/components/schemas/AttributeAssignmentHistoryLogOutput'
        nextCursor:
          type: string
          description: >-
            The cursor to pass to the next request when more audit logs are
            available.
          example: 018ff5cd-6dc4-7d57-bcbc-374702ca8b38
        hasMore:
          type: boolean
          description: Whether additional audit log entries are available after this page.
          example: true
      required:
        - userId
        - membershipId
        - auditLogs
        - hasMore
    AttributeAssignmentHistoryLogOutput:
      type: object
      properties:
        id:
          type: string
          description: The unique identifier of the audit log entry.
          example: 018ff5cd-6dc4-7d57-bcbc-374702ca8b38
        timestamp:
          type: string
          description: The ISO timestamp when the assignment change was recorded.
          example: '2026-06-04T10:00:00.000Z'
        source:
          type: string
          description: >-
            The source that emitted the audit event, such as WEBAPP, API_V2,
            WEBHOOK, or SYSTEM.
          example: API_V2
        actor:
          description: Details about the user, app, or system actor that made the change.
          allOf:
            - $ref: '#/components/schemas/AttributeAssignmentHistoryActorOutput'
        sourceContext:
          type: object
          description: >-
            Source-specific context for the audit event, for example API v2, web
            app, DSync, or integration sync metadata.
          example:
            kind: API_V2
        changes:
          description: The attribute assignment changes captured in this audit log entry.
          type: array
          items:
            $ref: '#/components/schemas/AttributeAssignmentHistoryChangeOutput'
        hasError:
          type: boolean
          description: Whether the audit log payload could not be fully parsed.
          example: true
      required:
        - id
        - timestamp
        - source
        - actor
        - sourceContext
        - changes
    AttributeAssignmentHistoryActorOutput:
      type: object
      properties:
        type:
          type: string
          description: The type of actor that made the attribute assignment change.
          example: USER
        displayName:
          type: string
          description: The human-readable name of the actor that made the change.
          example: Alice Admin
        displayEmail:
          type: string
          nullable: true
          description: The email address of the actor when one is available.
          example: alice@example.com
        displayAvatar:
          type: string
          nullable: true
          description: The avatar URL of the actor when one is available.
          example: https://example.com/avatar.png
      required:
        - type
        - displayName
    AttributeAssignmentHistoryChangeOutput:
      type: object
      properties:
        type:
          type: string
          description: >-
            The type of assignment change, such as ASSIGNED, UNASSIGNED,
            VALUE_CHANGED, or WEIGHT_CHANGED.
          example: VALUE_CHANGED
        attribute:
          description: Details for the attribute affected by this change.
          allOf:
            - $ref: '#/components/schemas/AttributeAssignmentHistoryAttributeOutput'
        previous:
          nullable: true
          description: >-
            The previous assignment value before the change, or null when the
            value was newly assigned.
          allOf:
            - $ref: '#/components/schemas/AttributeAssignmentHistoryValueOutput'
        current:
          nullable: true
          description: >-
            The current assignment value after the change, or null when the
            value was unassigned.
          allOf:
            - $ref: '#/components/schemas/AttributeAssignmentHistoryValueOutput'
      required:
        - type
        - attribute
    AttributeAssignmentHistoryAttributeOutput:
      type: object
      properties:
        id:
          type: string
          description: The unique identifier of the attribute that changed.
          example: attr_dept
        slug:
          type: string
          description: The URL-safe slug of the attribute that changed.
          example: department
        name:
          type: string
          description: The display name of the attribute that changed.
          example: Department
        type:
          type: string
          description: >-
            The attribute input type, such as TEXT, NUMBER, SINGLE_SELECT, or
            MULTI_SELECT.
          example: SINGLE_SELECT
      required:
        - id
        - slug
        - name
        - type
    AttributeAssignmentHistoryValueOutput:
      type: object
      properties:
        optionId:
          type: string
          description: The unique identifier of the assigned attribute option.
          example: opt_engineering
        optionSlug:
          type: string
          description: The URL-safe slug of the assigned attribute option.
          example: engineering
        value:
          type: string
          description: The display value of the assigned attribute option.
          example: Engineering
        weight:
          type: number
          nullable: true
          description: >-
            The routing weight for the assigned option, or null when weights are
            not used.
          example: 100
      required:
        - optionId
        - optionSlug
        - value

````