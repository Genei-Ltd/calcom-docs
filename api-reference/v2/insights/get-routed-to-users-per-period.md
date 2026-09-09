> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get routed-to users per period

> Get routed-to booking counts by user and period for user, team, or organization insights.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/insights/routings/routed-to-per-period
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
  /v2/insights/routings/routed-to-per-period:
    post:
      tags:
        - Insights
      summary: Get routed-to users per period
      description: >-
        Get routed-to booking counts by user and period for user, team, or
        organization insights.
      operationId: InsightsController_getRoutedToPerPeriod
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RoutedToPerPeriodInput'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetInsightsRoutingRoutedToPerPeriodOutput'
components:
  schemas:
    RoutedToPerPeriodInput:
      type: object
      properties:
        scope:
          type: string
          enum:
            - user
            - team
            - org
          example: user
        selectedTeamId:
          type: number
          description: Team ID for team-scoped routing insights
          example: 12
        startDate:
          type: string
          description: Inclusive start date for routing insights
          example: '2024-01-01'
        endDate:
          type: string
          description: Inclusive end date for routing insights
          example: '2024-01-31'
        columnFilters:
          type: array
          description: >-
            Data-table column filters (discriminated union by type: ss, ms, t,
            n, dr). Date range filters use id=createdAt.
          example:
            - id: createdAt
              value:
                type: dr
                data:
                  startDate: '2024-01-01'
                  endDate: '2024-01-31'
                  preset: custom
          items:
            type: object
            properties:
              id:
                type: string
              value:
                type: object
                properties:
                  type:
                    type: string
                    enum:
                      - ss
                      - ms
                      - t
                      - 'n'
                      - dr
                  data:
                    type: object
        period:
          type: string
          enum:
            - perDay
            - perWeek
            - perMonth
          example: perWeek
        limit:
          type: number
          example: 10
          maximum: 100
        searchQuery:
          type: string
          example: Alice
      required:
        - scope
        - startDate
        - endDate
        - period
        - limit
    GetInsightsRoutingRoutedToPerPeriodOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/InsightsRoutingRoutedToPerPeriodDataOutput'
      required:
        - status
        - data
    InsightsRoutingRoutedToPerPeriodDataOutput:
      type: object
      properties:
        users:
          $ref: '#/components/schemas/InsightsRoutingRoutedToUsersOutput'
        periodStats:
          $ref: '#/components/schemas/InsightsRoutingRoutedToPeriodStatsOutput'
      required:
        - users
        - periodStats
    InsightsRoutingRoutedToUsersOutput:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/InsightsRoutingRoutedToUserOutput'
      required:
        - data
    InsightsRoutingRoutedToPeriodStatsOutput:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/InsightsRoutingRoutedToPeriodStatOutput'
      required:
        - data
    InsightsRoutingRoutedToUserOutput:
      type: object
      properties:
        id:
          type: number
          example: 101
        name:
          type: string
          example: Alice Doe
          nullable: true
        email:
          type: object
          example: alice@example.com
          nullable: true
        avatarUrl:
          type: object
          example: https://example.com/avatar.png
          nullable: true
        performance:
          type: string
          example: above_average
        totalBookings:
          type: number
          example: 12
      required:
        - id
        - name
        - email
        - avatarUrl
        - performance
        - totalBookings
    InsightsRoutingRoutedToPeriodStatOutput:
      type: object
      properties:
        userId:
          type: number
          example: 101
        period_start:
          format: date-time
          type: string
          example: '2024-01-01T00:00:00.000Z'
        total:
          type: number
          example: 3
      required:
        - userId
        - period_start
        - total

````