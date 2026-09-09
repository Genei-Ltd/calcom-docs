> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get booking KPI stats

> Get booking KPI stats for user, team, or organization insights.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/insights/bookings/kpi-stats
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
  /v2/insights/bookings/kpi-stats:
    post:
      tags:
        - Insights
      summary: Get booking KPI stats
      description: Get booking KPI stats for user, team, or organization insights.
      operationId: InsightsController_getBookingKpiStats
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/BookingInsightsInput'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetBookingKpiStatsOutput'
components:
  schemas:
    BookingInsightsInput:
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
          description: Team ID for team-scoped insights
          example: 12
        timeZone:
          type: string
          description: IANA timezone used to group time-series insights
          example: America/New_York
        columnFilters:
          type: array
          description: >-
            Data-table column filters (discriminated union by type: ss, ms, t,
            n, dr). Date range filters use id=startTime or id=createdAt.
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
                description: Column identifier
              value:
                type: object
                description: Filter value discriminated by type field
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
      required:
        - scope
        - timeZone
    GetBookingKpiStatsOutput:
      type: object
      properties:
        status:
          type: string
          description: Response status
          example: success
          enum:
            - success
            - error
        data:
          description: KPI statistics data
          allOf:
            - $ref: '#/components/schemas/BookingInsightsKpiStatsDataOutput'
      required:
        - status
        - data
    BookingInsightsKpiStatsDataOutput:
      type: object
      properties:
        empty:
          type: boolean
          description: Whether no data exists for the selected period
          example: false
        created:
          description: Total bookings created in the period
          allOf:
            - $ref: '#/components/schemas/BookingInsightsMetricOutput'
        scheduled:
          description: Total bookings scheduled (upcoming) in the period
          allOf:
            - $ref: '#/components/schemas/BookingInsightsMetricOutput'
        completed:
          description: Total bookings completed in the period
          allOf:
            - $ref: '#/components/schemas/BookingInsightsMetricOutput'
        rescheduled:
          description: Total bookings rescheduled in the period
          allOf:
            - $ref: '#/components/schemas/BookingInsightsMetricOutput'
        cancelled:
          description: Total bookings cancelled in the period
          allOf:
            - $ref: '#/components/schemas/BookingInsightsMetricOutput'
        no_show:
          description: Total host no-shows in the period
          allOf:
            - $ref: '#/components/schemas/BookingInsightsMetricOutput'
        no_show_guest:
          description: Total guest no-shows in the period
          allOf:
            - $ref: '#/components/schemas/BookingInsightsMetricOutput'
        rating:
          description: Average rating score in the period
          allOf:
            - $ref: '#/components/schemas/BookingInsightsMetricOutput'
        csat:
          description: Customer satisfaction percentage (0-100) in the period
          allOf:
            - $ref: '#/components/schemas/BookingInsightsMetricOutput'
        previousRange:
          description: Date range of the previous comparison period
          allOf:
            - $ref: '#/components/schemas/BookingInsightsPreviousRangeOutput'
      required:
        - empty
        - created
        - scheduled
        - completed
        - rescheduled
        - cancelled
        - no_show
        - no_show_guest
        - rating
        - csat
        - previousRange
    BookingInsightsMetricOutput:
      type: object
      properties:
        count:
          type: number
          description: Metric value for the current period
          example: 10
        deltaPrevious:
          type: number
          description: Percentage change compared to the previous period
          example: 12.5
      required:
        - count
        - deltaPrevious
    BookingInsightsPreviousRangeOutput:
      type: object
      properties:
        startDate:
          type: string
          description: Start date of the previous comparison period
          example: Dec 1, 2023
        endDate:
          type: string
          description: End date of the previous comparison period
          example: Dec 31, 2023
      required:
        - startDate
        - endDate

````