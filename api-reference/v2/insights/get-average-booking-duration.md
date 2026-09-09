> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get average booking duration

> Get average booking duration for user, team, or organization insights.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/insights/bookings/average-duration
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
  /v2/insights/bookings/average-duration:
    post:
      tags:
        - Insights
      summary: Get average booking duration
      description: Get average booking duration for user, team, or organization insights.
      operationId: InsightsController_getBookingAverageDuration
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
                $ref: '#/components/schemas/GetBookingAverageDurationOutput'
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
    GetBookingAverageDurationOutput:
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
          description: Array of daily average duration data points
          type: array
          items:
            $ref: '#/components/schemas/BookingInsightsAverageDurationDto'
      required:
        - status
        - data
    BookingInsightsAverageDurationDto:
      type: object
      properties:
        Date:
          type: string
          description: Abbreviated date label for chart display
          example: Jan 1
        formattedDateFull:
          type: string
          description: Full formatted date label for the data point
          example: Jan 1, 2024
        isToday:
          type: boolean
          description: Whether this data point represents the current day
          example: false
        Average:
          type: number
          description: Average booking duration in minutes for this date
          example: 30
      required:
        - Date
        - formattedDateFull
        - isToday
        - Average

````