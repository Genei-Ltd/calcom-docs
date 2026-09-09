> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get failed bookings by routing field

> Get failed booking counts grouped by routing form field for user, team, or organization insights.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/insights/routings/failed-bookings-by-field
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
  /v2/insights/routings/failed-bookings-by-field:
    post:
      tags:
        - Insights
      summary: Get failed bookings by routing field
      description: >-
        Get failed booking counts grouped by routing form field for user, team,
        or organization insights.
      operationId: InsightsController_getFailedBookingsByField
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RoutingInsightsBaseInput'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/GetInsightsRoutingFailedBookingsByFieldOutput
components:
  schemas:
    RoutingInsightsBaseInput:
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
      required:
        - scope
        - startDate
        - endDate
    GetInsightsRoutingFailedBookingsByFieldOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          type: object
          example:
            Contact Sales:
              Company size:
                - optionId: option_1
                  optionLabel: Enterprise
                  count: 5
      required:
        - status
        - data

````