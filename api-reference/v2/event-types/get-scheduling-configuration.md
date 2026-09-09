> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get scheduling configuration

> Returns the scheduling configuration for a team event type. The response shape varies by scheduling type:

    - **roundRobin**: Full configuration including hosts with priority, weight, and group assignment, host groups, and advanced settings (weights toggle, lead threshold, no-show calculations, CRM fallback).
    - **collective**: Hosts with basic info and assignAllTeamMembers. Round-robin-specific fields are omitted.
    - **managed**: Hosts with basic info and assignAllTeamMembers. Round-robin-specific fields are omitted.

    Validates that the event type is a team event type. Returns 422 if the event type is not a team event type.

    If accessed using an OAuth access token, the `EVENT_TYPE_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/event-types/{eventTypeId}/scheduling-config
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
  /v2/event-types/{eventTypeId}/scheduling-config:
    get:
      tags:
        - Event Types
      summary: Get scheduling configuration
      description: >-
        Returns the scheduling configuration for a team event type. The response
        shape varies by scheduling type:

            - **roundRobin**: Full configuration including hosts with priority, weight, and group assignment, host groups, and advanced settings (weights toggle, lead threshold, no-show calculations, CRM fallback).
            - **collective**: Hosts with basic info and assignAllTeamMembers. Round-robin-specific fields are omitted.
            - **managed**: Hosts with basic info and assignAllTeamMembers. Round-robin-specific fields are omitted.

            Validates that the event type is a team event type. Returns 422 if the event type is not a team event type.

            If accessed using an OAuth access token, the `EVENT_TYPE_READ` scope is required.
      operationId: EventTypesController_2024_06_14_getSchedulingConfig
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
                $ref: '#/components/schemas/GetSchedulingConfigOutput'
components:
  schemas:
    GetSchedulingConfigOutput:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          $ref: '#/components/schemas/SchedulingConfigData'
      required:
        - status
        - data
    SchedulingConfigData:
      type: object
      properties:
        eventTypeId:
          type: number
          example: 1
          description: Event type ID
        schedulingType:
          type: string
          enum:
            - roundRobin
            - collective
            - managed
          example: roundRobin
          description: >-
            The scheduling type of this event type. Determines which fields are
            populated.
        hosts:
          description: Array of hosts assigned to this event type
          type: array
          items:
            $ref: '#/components/schemas/SchedulingHost'
        assignAllTeamMembers:
          type: boolean
          example: false
          description: Whether all team members are automatically assigned as hosts
        hostGroups:
          description: >-
            Host groups for organizing round-robin hosts. Only present for
            roundRobin scheduling type.
          type: array
          items:
            $ref: '#/components/schemas/SchedulingHostGroup'
        rescheduleWithSameRoundRobinHost:
          type: boolean
          example: false
          description: >-
            Whether rescheduled events keep the same round-robin host. Only
            present for roundRobin scheduling type.
        isRRWeightsEnabled:
          type: boolean
          example: false
          description: >-
            Whether round-robin weights are enabled for host distribution. Only
            present for roundRobin scheduling type.
        maxLeadThreshold:
          type: number
          nullable: true
          example: 3
          description: >-
            Max lead threshold for load-balanced distribution. null = 'maximize
            availability', number = 'load balancing'. Only present for
            roundRobin scheduling type.
        includeNoShowInRRCalculation:
          type: boolean
          example: false
          description: >-
            Whether no-show bookings are included in round-robin calculations.
            Only present for roundRobin scheduling type.
        crmRecordOwnerFallbackWindowHours:
          type: number
          nullable: true
          example: 24
          description: >-
            CRM record owner fallback window in hours. Only present for
            roundRobin scheduling type.
        crmRecordOwnerFallbackWindowSkipWeekends:
          type: boolean
          example: false
          description: >-
            Whether to exclude weekends from the CRM record owner fallback
            window calculation. Only present for roundRobin scheduling type.
      required:
        - eventTypeId
        - schedulingType
        - hosts
        - assignAllTeamMembers
    SchedulingHost:
      type: object
      properties:
        userId:
          type: number
          example: 1
          description: User ID of the host
        name:
          type: string
          example: John Doe
          description: Display name of the host
        username:
          type: string
          example: john-doe
          description: Username of the host
        mandatory:
          type: boolean
          example: false
          description: >-
            If true, this host is a fixed host who always attends (not in the
            round-robin rotation pool)
        priority:
          type: string
          nullable: true
          enum:
            - lowest
            - low
            - medium
            - high
            - highest
          example: medium
          description: >-
            Priority level for round-robin distribution. Only present for
            roundRobin scheduling type.
        weight:
          type: number
          nullable: true
          example: 100
          description: >-
            Weight for round-robin distribution. Higher weight means more
            bookings assigned. Only present for roundRobin scheduling type.
        avatarUrl:
          type: string
          nullable: true
        groupId:
          type: string
          nullable: true
          description: >-
            ID of the host group this host belongs to. Only present for
            roundRobin scheduling type.
      required:
        - userId
        - name
        - username
        - mandatory
    SchedulingHostGroup:
      type: object
      properties:
        id:
          type: string
          description: Unique ID of the host group
        name:
          type: string
          example: Sales Team
          description: Name of the host group
      required:
        - id
        - name

````