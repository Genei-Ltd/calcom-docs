> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a schedule

> <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>

If accessed using an OAuth access token, the `SCHEDULE_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json patch /v2/schedules/{scheduleId}
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
  /v2/schedules/{scheduleId}:
    patch:
      tags:
        - Schedules
      summary: Update a schedule
      description: >-
        <Note>Please make sure to pass in the cal-api-version header value as
        mentioned in the Headers section. Not passing the correct value will
        default to an older version of this endpoint.</Note>


        If accessed using an OAuth access token, the `SCHEDULE_WRITE` scope is
        required.
      operationId: SchedulesController_2024_06_11_updateSchedule
      parameters:
        - name: Authorization
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_, managed user access token, or OAuth access token
          required: true
          schema:
            type: string
        - name: cal-api-version
          in: header
          description: >-
            Must be set to 2024-06-11. If not set to this value, the endpoint
            will default to an older version.
          required: true
          schema:
            type: string
            default: '2024-06-11'
        - name: scheduleId
          required: true
          in: path
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateScheduleInput_2024_06_11'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UpdateScheduleOutput_2024_06_11'
components:
  schemas:
    UpdateScheduleInput_2024_06_11:
      type: object
      properties:
        name:
          type: string
          example: One-on-one coaching
        timeZone:
          type: string
          example: Europe/Rome
        availability:
          example:
            - days:
                - Monday
                - Tuesday
              startTime: '09:00'
              endTime: '10:00'
          type: array
          items:
            $ref: '#/components/schemas/ScheduleAvailabilityInput_2024_06_11'
        isDefault:
          type: boolean
          example: true
        overrides:
          example:
            - date: '2024-05-20'
              startTime: '12:00'
              endTime: '14:00'
          type: array
          items:
            $ref: '#/components/schemas/ScheduleOverrideInput_2024_06_11'
    UpdateScheduleOutput_2024_06_11:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          $ref: '#/components/schemas/ScheduleOutput_2024_06_11'
      required:
        - status
        - data
    ScheduleAvailabilityInput_2024_06_11:
      type: object
      properties:
        days:
          type: array
          example:
            - Monday
            - Tuesday
          description: Array of days when schedule is active.
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
        startTime:
          type: string
          pattern: TIME_FORMAT_HH_MM
          example: '08:00'
          description: startTime must be a valid time in format HH:MM e.g. 08:00
        endTime:
          type: string
          pattern: TIME_FORMAT_HH_MM
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
          pattern: TIME_FORMAT_HH_MM
          example: '12:00'
          description: startTime must be a valid time in format HH:MM e.g. 12:00
        endTime:
          type: string
          pattern: TIME_FORMAT_HH_MM
          example: '13:00'
          description: endTime must be a valid time in format HH:MM e.g. 13:00
      required:
        - date
        - startTime
        - endTime
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

````