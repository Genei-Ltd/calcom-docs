> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get sync history for a specific user

> Returns a paginated list of integration sync runs filtered by user within the organization, including rule evaluations, applied field mappings, and team membership changes per run. Supports cursor-based pagination.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/organizations/{orgId}/attributes/sync-history/user/{userId}
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
  /v2/organizations/{orgId}/attributes/sync-history/user/{userId}:
    get:
      tags:
        - Orgs / Attributes / Sync History
      summary: Get sync history for a specific user
      description: >-
        Returns a paginated list of integration sync runs filtered by user
        within the organization, including rule evaluations, applied field
        mappings, and team membership changes per run. Supports cursor-based
        pagination.
      operationId: OrganizationAttributeSyncHistoryController_getUserSyncHistory
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
          description: Maximum number of items to return (1–100)
          schema:
            minimum: 1
            maximum: 100
            default: 25
            example: 25
            type: number
        - name: cursor
          required: false
          in: query
          description: >-
            Cursor for keyset pagination (UUID of the last item from previous
            page)
          schema:
            format: uuid
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetAttributeSyncHistoryOutput'
components:
  schemas:
    GetAttributeSyncHistoryOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          type: array
          items:
            $ref: '#/components/schemas/IntegrationSyncRunWithChildrenOutput'
        meta:
          $ref: '#/components/schemas/PaginationMeta'
      required:
        - status
        - data
        - meta
    IntegrationSyncRunWithChildrenOutput:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier of the sync run
        provider:
          type: string
          description: Integration provider (e.g. SALESFORCE)
        credentialId:
          type: number
          nullable: true
          description: Credential ID that triggered the sync
        organizationId:
          type: number
          nullable: true
          description: Organization ID
        userId:
          type: number
          nullable: true
          description: Cal.com user ID affected by this sync
        userName:
          type: string
          nullable: true
          description: Display name of the affected user
        externalUserId:
          type: string
          nullable: true
          description: External provider user identifier
        status:
          type: string
          description: Status of the sync run
          enum:
            - APPLIED
            - SKIPPED_BY_RULE
            - NO_RULES_MATCHED
            - FAILED
            - INVALID_SIGNATURE
            - RATE_LIMITED
        signatureVerified:
          type: boolean
          description: Whether the inbound webhook signature was verified
        errorMessage:
          type: string
          nullable: true
          description: Error message if the sync failed
        createdAt:
          type: string
          description: When this sync run was recorded
        ruleEvaluations:
          description: Rules evaluated during this sync run
          type: array
          items:
            $ref: '#/components/schemas/RuleEvaluationOutput'
        appliedFieldMappings:
          description: Field mappings applied during this sync run
          type: array
          items:
            $ref: '#/components/schemas/FieldMappingAppliedOutput'
        teamMembershipChanges:
          description: Team membership changes resulting from this sync run
          type: array
          items:
            $ref: '#/components/schemas/TeamMembershipChangeOutput'
      required:
        - id
        - provider
        - status
        - signatureVerified
        - createdAt
        - ruleEvaluations
        - appliedFieldMappings
        - teamMembershipChanges
    PaginationMeta:
      type: object
      properties:
        hasMore:
          type: boolean
          description: Whether more pages are available
        nextCursor:
          type: string
          description: Cursor for the next page, if available
      required:
        - hasMore
    RuleEvaluationOutput:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier of the rule evaluation
        runId:
          type: string
          description: ID of the parent sync run
        ruleId:
          type: string
          nullable: true
          description: ID of the matching rule, if any
        evaluationOrder:
          type: number
          description: Order in which this rule was evaluated
        attributeKey:
          type: string
          description: Attribute key that was evaluated
        operator:
          type: string
          description: Comparison operator used (e.g. EQUALS, CONTAINS)
        expectedValue:
          type: string
          nullable: true
          description: Value the rule expected to match
        expectedValueType:
          type: string
          description: Data type of the expected value
        actualValue:
          type: string
          nullable: true
          description: Actual value from the external provider
        actualValueType:
          type: string
          description: Data type of the actual value
        passed:
          type: boolean
          description: Whether the rule condition was satisfied
        createdAt:
          type: string
          description: When this evaluation was recorded
      required:
        - id
        - runId
        - evaluationOrder
        - attributeKey
        - operator
        - expectedValueType
        - actualValueType
        - passed
        - createdAt
    FieldMappingAppliedOutput:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier of the field mapping application
        runId:
          type: string
          description: ID of the parent sync run
        fieldMappingId:
          type: string
          nullable: true
          description: ID of the field mapping configuration
        attributeId:
          type: string
          nullable: true
          description: ID of the Cal.com attribute that was updated
        attributeSlug:
          type: string
          description: Slug of the Cal.com attribute
        attributeName:
          type: string
          description: Display name of the Cal.com attribute
        sourceField:
          type: string
          description: Source field name from the external provider
        previousValue:
          type: string
          nullable: true
          description: Attribute value before the sync
        newValue:
          type: string
          nullable: true
          description: Attribute value after the sync
        outcome:
          type: string
          description: Outcome of the mapping (e.g. CREATED, UPDATED, UNCHANGED)
        createdAt:
          type: string
          description: When this mapping was applied
      required:
        - id
        - runId
        - attributeSlug
        - attributeName
        - sourceField
        - outcome
        - createdAt
    TeamMembershipChangeOutput:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier of the membership change
        runId:
          type: string
          description: ID of the parent sync run
        teamId:
          type: number
          nullable: true
          description: Cal.com team ID affected by this change
        teamName:
          type: string
          description: Name of the team
        teamSlug:
          type: string
          nullable: true
          description: Slug of the team
        outcome:
          type: string
          description: Outcome of the change (e.g. ADDED, REMOVED, NO_CHANGE)
        createdAt:
          type: string
          description: When this membership change was recorded
      required:
        - id
        - runId
        - teamName
        - outcome
        - createdAt

````