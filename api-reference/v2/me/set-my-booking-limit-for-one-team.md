> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Set my booking limit for one team

> Sets your own numbers for this team's booking limit. Intervals you omit keep what you stored before, an interval sent as `null` goes back to inheriting the team default, and every value is capped at your own overall limit for the same interval. Only teams you are a round-robin host of accept this; the number is enforced on that team's round-robin events only, while collective events and events where you are a fixed host keep the team default. If accessed using an OAuth access token, the `PROFILE_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json patch /v2/me/team-booking-limits/{teamId}
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
  /v2/me/team-booking-limits/{teamId}:
    patch:
      tags:
        - Me
      summary: Set my booking limit for one team
      description: >-
        Sets your own numbers for this team's booking limit. Intervals you omit
        keep what you stored before, an interval sent as `null` goes back to
        inheriting the team default, and every value is capped at your own
        overall limit for the same interval. Only teams you are a round-robin
        host of accept this; the number is enforced on that team's round-robin
        events only, while collective events and events where you are a fixed
        host keep the team default. If accessed using an OAuth access token, the
        `PROFILE_WRITE` scope is required.
      operationId: MeController_updateMyTeamBookingLimit
      parameters:
        - name: Authorization
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_, managed user access token, or OAuth access token
          required: true
          schema:
            type: string
        - name: teamId
          required: true
          in: path
          schema:
            type: number
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateTeamBookingLimitInput'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UpdateTeamBookingLimitOutput'
components:
  schemas:
    UpdateTeamBookingLimitInput:
      type: object
      properties:
        perDay:
          type: number
          nullable: true
          minimum: 1
          description: >-
            Maximum bookings you take per day across this team's round-robin
            events. Pass null to inherit this interval; use DELETE to clear all
            intervals.
          example: 2
        perWeek:
          type: number
          nullable: true
          minimum: 1
          description: >-
            Maximum bookings you take per week across this team's round-robin
            events. Pass null to inherit this interval; use DELETE to clear all
            intervals.
          example: 3
        perMonth:
          type: number
          nullable: true
          minimum: 1
          description: >-
            Maximum bookings you take per month across this team's round-robin
            events. Pass null to inherit this interval; use DELETE to clear all
            intervals.
          example: 12
        perYear:
          type: number
          nullable: true
          minimum: 1
          description: >-
            Maximum bookings you take per year across this team's round-robin
            events. Pass null to inherit this interval; use DELETE to clear all
            intervals.
          example: 100
    UpdateTeamBookingLimitOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/TeamBookingLimitOutput'
      required:
        - status
        - data
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