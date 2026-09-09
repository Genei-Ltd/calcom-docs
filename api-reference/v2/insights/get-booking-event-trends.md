> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get booking event trends

> Get booking trend stats for user, team, or organization insights.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/insights/bookings/event-trends
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
  /v2/insights/bookings/event-trends:
    post:
      tags:
        - Insights
      summary: Get booking event trends
      description: Get booking trend stats for user, team, or organization insights.
      operationId: InsightsController_getBookingEventTrends
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
                $ref: '#/components/schemas/GetBookingEventTrendsOutput'
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
    GetBookingEventTrendsOutput:
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
          description: Array of daily event trend data points
          type: array
          items:
            $ref: '#/components/schemas/BookingInsightsEventTrendDto'
      required:
        - status
        - data
    BookingInsightsEventTrendDto:
      type: object
      properties:
        formattedDateFull:
          type: string
          description: Full formatted date label for the data point
          example: Jan 1, 2024
        isToday:
          type: boolean
          description: Whether this data point represents the current day
          example: false
        Month:
          type: string
          description: Abbreviated month-day label for chart display
          example: Jan 1
        Created:
          type: number
          description: Number of bookings created on this date
          example: 12
        Completed:
          type: number
          description: Number of bookings completed on this date
          example: 8
        Rescheduled:
          type: number
          description: Number of bookings rescheduled on this date
          example: 2
        Cancelled:
          type: number
          description: Number of bookings cancelled on this date
          example: 1
        No-Show (Host):
          type: number
          description: Number of host no-shows on this date
          example: 0
        No-Show (Guest):
          type: number
          description: Number of guest no-shows on this date
          example: 1
      required:
        - formattedDateFull
        - isToday
        - Month
        - Created
        - Completed
        - Rescheduled
        - Cancelled
        - No-Show (Host)
        - No-Show (Guest)

````