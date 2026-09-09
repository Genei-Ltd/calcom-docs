> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get booking member stats

> Get booking member stats for user, team, or organization insights.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/insights/bookings/members
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
  /v2/insights/bookings/members:
    post:
      tags:
        - Insights
      summary: Get booking member stats
      description: Get booking member stats for user, team, or organization insights.
      operationId: InsightsController_getBookingMemberStats
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
                $ref: '#/components/schemas/GetBookingMemberStatsOutput'
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
    GetBookingMemberStatsOutput:
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
          description: Member statistics grouped by ranking category
          allOf:
            - $ref: '#/components/schemas/BookingInsightsMemberStatsDataOutput'
      required:
        - status
        - data
    BookingInsightsMemberStatsDataOutput:
      type: object
      properties:
        mostBookings:
          description: Members ranked by most total bookings
          type: array
          items:
            $ref: '#/components/schemas/BookingInsightsMemberStatDto'
        leastBookings:
          description: Members ranked by fewest total bookings
          type: array
          items:
            $ref: '#/components/schemas/BookingInsightsMemberStatDto'
        mostCancelled:
          description: Members ranked by most cancellations
          type: array
          items:
            $ref: '#/components/schemas/BookingInsightsMemberStatDto'
        mostCompleted:
          description: Members ranked by most completed bookings
          type: array
          items:
            $ref: '#/components/schemas/BookingInsightsMemberStatDto'
        leastCompleted:
          description: Members ranked by fewest completed bookings
          type: array
          items:
            $ref: '#/components/schemas/BookingInsightsMemberStatDto'
        mostNoShow:
          description: Members ranked by most no-shows
          type: array
          items:
            $ref: '#/components/schemas/BookingInsightsMemberStatDto'
        highestRatings:
          description: Members ranked by highest average rating
          type: array
          items:
            $ref: '#/components/schemas/BookingInsightsMemberStatDto'
        lowestRatings:
          description: Members ranked by lowest average rating
          type: array
          items:
            $ref: '#/components/schemas/BookingInsightsMemberStatDto'
      required:
        - mostBookings
        - leastBookings
        - mostCancelled
        - mostCompleted
        - leastCompleted
        - mostNoShow
        - highestRatings
        - lowestRatings
    BookingInsightsMemberStatDto:
      type: object
      properties:
        userId:
          type: number
          description: User ID of the team member
          example: 101
        user:
          description: Team member profile details
          allOf:
            - $ref: '#/components/schemas/BookingInsightsMemberUserDto'
        emailMd5:
          type: string
          description: MD5 hash of email for Gravatar lookup
          example: c160f8cc69a4f0bf2b0362752353d060
        count:
          type: number
          description: Number of bookings for this ranking category
          example: 8
      required:
        - userId
        - user
        - emailMd5
        - count
    BookingInsightsMemberUserDto:
      type: object
      properties:
        id:
          type: number
          description: User ID of the team member
          example: 101
        username:
          type: string
          nullable: true
          description: Username of the team member
          example: alice
        name:
          type: string
          nullable: true
          description: Display name of the team member
          example: Alice
        email:
          type: string
          description: Email address of the team member
          example: alice@example.com
        avatarUrl:
          type: string
          nullable: true
          description: Avatar image URL
          example: /alice/avatar.png
      required:
        - id
        - email

````