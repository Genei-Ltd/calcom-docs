> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get routing form responses

> Get paginated routing form responses for user, team, or organization insights.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/insights/routings/form-responses
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
  /v2/insights/routings/form-responses:
    post:
      tags:
        - Insights
      summary: Get routing form responses
      description: >-
        Get paginated routing form responses for user, team, or organization
        insights.
      operationId: InsightsController_getRoutingFormResponses
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RoutingInsightsPaginatedInput'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetInsightsRoutingFormResponsesOutput'
components:
  schemas:
    RoutingInsightsPaginatedInput:
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
        sorting:
          type: array
          example:
            - id: createdAt
              desc: true
        offset:
          type: number
          example: 0
        limit:
          type: number
          example: 50
          maximum: 100
      required:
        - scope
        - startDate
        - endDate
        - offset
        - limit
    GetInsightsRoutingFormResponsesOutput:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          $ref: '#/components/schemas/InsightsRoutingFormResponsesDataOutput'
      required:
        - status
        - data
    InsightsRoutingFormResponsesDataOutput:
      type: object
      properties:
        total:
          type: number
          example: 10
        data:
          type: array
          items:
            $ref: '#/components/schemas/InsightsRoutingFormResponseOutput'
      required:
        - total
        - data
    InsightsRoutingFormResponseOutput:
      type: object
      properties:
        id:
          type: number
          example: 1
        uuid:
          type: string
          example: form_123
          nullable: true
        formId:
          type: string
          example: form_123
        formName:
          type: string
          example: Contact Sales
        formTeamId:
          type: number
          example: 10
          nullable: true
        formUserId:
          type: number
          example: 101
        bookingUid:
          type: string
          example: booking_uid
          nullable: true
        bookingId:
          type: number
          example: 1
          nullable: true
        bookingStatus:
          type: string
          example: ACCEPTED
          nullable: true
        bookingStatusOrder:
          type: number
          example: 1
          nullable: true
        bookingCreatedAt:
          type: string
          example: '2024-01-01T00:00:00.000Z'
          nullable: true
          format: date-time
        bookingUserId:
          type: number
          example: 101
          nullable: true
        bookingUserName:
          type: string
          example: Alice Doe
          nullable: true
        bookingUserEmail:
          type: string
          example: alice@example.com
          nullable: true
        bookingUserAvatarUrl:
          type: string
          example: https://example.com/avatar.png
          nullable: true
        bookingAssignmentReason:
          type: string
          example: round_robin
          nullable: true
        bookingStartTime:
          type: string
          example: '2024-01-01T09:00:00.000Z'
          nullable: true
          format: date-time
        bookingEndTime:
          type: string
          example: '2024-01-01T09:30:00.000Z'
          nullable: true
          format: date-time
        eventTypeId:
          type: number
          example: 200
          nullable: true
        eventTypeParentId:
          type: number
          nullable: true
          example: null
        eventTypeSchedulingType:
          type: string
          example: ROUND_ROBIN
          nullable: true
        createdAt:
          format: date-time
          type: string
          example: '2024-01-01T00:00:00.000Z'
        utm_source:
          type: string
          example: google
          nullable: true
        utm_medium:
          type: string
          example: cpc
          nullable: true
        utm_campaign:
          type: string
          example: spring_launch
          nullable: true
        utm_term:
          type: string
          example: calendar scheduling
          nullable: true
        utm_content:
          type: string
          example: hero_cta
          nullable: true
        bookingAttendees:
          type: array
          items:
            $ref: '#/components/schemas/InsightsRoutingBookingAttendeeOutput'
        fields:
          type: array
          items:
            $ref: '#/components/schemas/InsightsRoutingResponseFieldOutput'
      required:
        - id
        - uuid
        - formId
        - formName
        - formTeamId
        - formUserId
        - bookingUid
        - bookingId
        - bookingStatus
        - bookingStatusOrder
        - bookingCreatedAt
        - bookingUserId
        - bookingUserName
        - bookingUserEmail
        - bookingUserAvatarUrl
        - bookingAssignmentReason
        - bookingStartTime
        - bookingEndTime
        - eventTypeId
        - eventTypeParentId
        - eventTypeSchedulingType
        - createdAt
        - utm_source
        - utm_medium
        - utm_campaign
        - utm_term
        - utm_content
        - bookingAttendees
        - fields
    InsightsRoutingBookingAttendeeOutput:
      type: object
      properties:
        name:
          type: string
          example: Jane Doe
        timeZone:
          type: string
          example: Europe/London
        email:
          type: string
          example: jane@example.com
        phoneNumber:
          type: string
          example: null
          nullable: true
      required:
        - name
        - timeZone
        - email
        - phoneNumber
    InsightsRoutingResponseFieldOutput:
      type: object
      properties:
        fieldId:
          type: string
          example: company-size
          nullable: true
        valueString:
          type: string
          example: Enterprise
          nullable: true
        valueNumber:
          type: number
          example: 100
          nullable: true
        valueStringArray:
          example:
            - Enterprise
            - Mid Market
          nullable: true
          type: array
          items:
            type: string
      required:
        - fieldId
        - valueString
        - valueNumber
        - valueStringArray

````