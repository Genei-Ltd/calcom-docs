> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a schedule

> Required membership role: `org admin`. PBAC permission: `availability.readOrgAvailability`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control. If accessed using an OAuth access token, the `ORG_SCHEDULE_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/organizations/{orgId}/users/{userId}/schedules/{scheduleId}
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
  /v2/organizations/{orgId}/users/{userId}/schedules/{scheduleId}:
    get:
      tags:
        - Orgs / Users / Schedules
      summary: Get a schedule
      description: >-
        Required membership role: `org admin`. PBAC permission:
        `availability.readOrgAvailability`. Learn more about API access control
        at https://cal.com/docs/api-reference/v2/access-control. If accessed
        using an OAuth access token, the `ORG_SCHEDULE_READ` scope is required.
      operationId: OrganizationsSchedulesController_getUserSchedule
      parameters:
        - name: Authorization
          in: header
          description: >-
            For non-platform customers - value must be `Bearer <token>` where
            `<token>` is api key prefixed with cal_
          required: false
          schema:
            type: string
        - name: x-cal-secret-key
          in: header
          description: For platform customers - OAuth client secret key
          required: false
          schema:
            type: string
        - name: x-cal-client-id
          in: header
          description: For platform customers - OAuth client ID
          required: false
          schema:
            type: string
        - name: userId
          required: true
          in: path
          schema:
            type: number
        - name: scheduleId
          required: true
          in: path
          schema:
            type: number
        - name: orgId
          required: true
          in: path
          schema:
            type: number
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetScheduleOutput_2024_06_11'
components:
  schemas:
    GetScheduleOutput_2024_06_11:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          nullable: true
          type: object
          allOf:
            - $ref: '#/components/schemas/ScheduleOutput_2024_06_11'
      required:
        - status
        - data
    ScheduleOutput_2024_06_11:
      type: object
      properties:
        id:
          type: number
          example: 254
        ownerId:
          type: number
          example: 478
        name:
          type: string
          example: Catch up hours
        timeZone:
          type: string
          example: Europe/Rome
        availability:
          example:
            - days:
                - Monday
                - Tuesday
              startTime: '17:00'
              endTime: '19:00'
            - days:
                - Wednesday
                - Thursday
              startTime: '16:00'
              endTime: '20:00'
          type: array
          items:
            $ref: '#/components/schemas/ScheduleAvailabilityInput_2024_06_11'
        isDefault:
          type: boolean
          example: true
        overrides:
          example:
            - date: '2024-05-20'
              startTime: '18:00'
              endTime: '21:00'
          type: array
          items:
            $ref: '#/components/schemas/ScheduleOverrideInput_2024_06_11'
      required:
        - id
        - ownerId
        - name
        - timeZone
        - availability
        - isDefault
        - overrides
    ScheduleAvailabilityInput_2024_06_11:
      type: object
      properties:
        days:
          type: array
          items:
            type: string
            enum:
              - Monday
              - Tuesday
              - Wednesday
              - Thursday
              - Friday
              - Saturday
              - Sunday
          example:
            - Monday
            - Tuesday
          description: Array of days when schedule is active.
        startTime:
          type: string
          example: '08:00'
          description: startTime must be a valid time in format HH:MM e.g. 08:00
        endTime:
          type: string
          example: '15:00'
          description: endTime must be a valid time in format HH:MM e.g. 15:00
      required:
        - days
        - startTime
        - endTime
    ScheduleOverrideInput_2024_06_11:
      type: object
      properties:
        date:
          type: string
          example: '2024-05-20'
        startTime:
          type: string
          example: '12:00'
          description: startTime must be a valid time in format HH:MM e.g. 12:00
        endTime:
          type: string
          example: '13:00'
          description: endTime must be a valid time in format HH:MM e.g. 13:00
      required:
        - date
        - startTime
        - endTime

````