> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get my team booking limits

> Returns every team whose booking limit applies to you as a round-robin host, with the team's default, your own number where you set one, and what is enforced. Teams you host for that set no limit are omitted. Your own number only applies where you are a round-robin host: on collective events and events where you are a fixed host the team default keeps applying to you. If accessed using an OAuth access token, the `PROFILE_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/me/team-booking-limits
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
  /v2/me/team-booking-limits:
    get:
      tags:
        - Me
      summary: Get my team booking limits
      description: >-
        Returns every team whose booking limit applies to you as a round-robin
        host, with the team's default, your own number where you set one, and
        what is enforced. Teams you host for that set no limit are omitted. Your
        own number only applies where you are a round-robin host: on collective
        events and events where you are a fixed host the team default keeps
        applying to you. If accessed using an OAuth access token, the
        `PROFILE_READ` scope is required.
      operationId: MeController_getMyTeamBookingLimits
      parameters:
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
                $ref: '#/components/schemas/GetTeamBookingLimitsOutput'
components:
  schemas:
    GetTeamBookingLimitsOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/TeamBookingLimitsData'
      required:
        - status
        - data
    TeamBookingLimitsData:
      type: object
      properties:
        teams:
          type: array
          items:
            $ref: '#/components/schemas/TeamBookingLimitOutput'
        globalLimit:
          nullable: true
          type: object
          allOf:
            - $ref: '#/components/schemas/BookingLimitsOutput'
        isOvercommitted:
          type: boolean
          description: >-
            True when your team numbers add up to more than your overall limit.
            Advisory only — the overall limit still caps you.
      required:
        - teams
        - globalLimit
        - isOvercommitted
    TeamBookingLimitOutput:
      type: object
      properties:
        teamId:
          type: number
          example: 42
        teamName:
          type: string
          example: Engineering
        teamLimit:
          description: What the team set for everyone who has not chosen their own number.
          allOf:
            - $ref: '#/components/schemas/BookingLimitsOutput'
        memberLimit:
          nullable: true
          description: >-
            Only the intervals you set for yourself; null while you inherit the
            team's numbers.
          type: object
          allOf:
            - $ref: '#/components/schemas/BookingLimitsOutput'
        effectiveLimit:
          description: What is enforced for you on this team.
          allOf:
            - $ref: '#/components/schemas/BookingLimitsOutput'
      required:
        - teamId
        - teamName
        - teamLimit
        - memberLimit
        - effectiveLimit
    BookingLimitsOutput:
      type: object
      properties:
        perDay:
          type: number
          nullable: true
          example: 4
        perWeek:
          type: number
          nullable: true
          example: 20
        perMonth:
          type: number
          example: 60
          nullable: true
        perYear:
          type: number
          nullable: true
          example: 500
      required:
        - perDay
        - perWeek
        - perMonth
        - perYear

````