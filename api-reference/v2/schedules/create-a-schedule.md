> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a schedule

> 
      Create a schedule for the authenticated user.

      The point of creating schedules is for event types to be available at specific times.

      The first goal of schedules is to have a default schedule. If you are platform customer and created managed users, then it is important to note that each managed user should have a default schedule.
      1. If you passed `timeZone` when creating managed user, then the default schedule from Monday to Friday from 9AM to 5PM will be created with that timezone. The managed user can then change the default schedule via the `AvailabilitySettings` atom.
      2. If you did not, then we assume you want the user to have this specific schedule right away. You should create a default schedule by specifying
      `"isDefault": true` in the request body. Until the user has a default schedule the user can't be booked nor manage their schedule via the AvailabilitySettings atom.

      The second goal of schedules is to create another schedule that event types can point to. This is useful for when an event is booked because availability is not checked against the default schedule but instead against that specific schedule.
      After creating a non-default schedule, you can update an event type to point to that schedule via the PATCH `event-types/{eventTypeId}` endpoint.

      When specifying start time and end time for each day use the 24 hour format e.g. 08:00, 15:00 etc.

      <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>

If accessed using an OAuth access token, the `SCHEDULE_WRITE` scope is required.
      



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/schedules
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
  /v2/schedules:
    post:
      tags:
        - Schedules
      summary: Create a schedule
      description: >2-

              Create a schedule for the authenticated user.

              The point of creating schedules is for event types to be available at specific times.

              The first goal of schedules is to have a default schedule. If you are platform customer and created managed users, then it is important to note that each managed user should have a default schedule.
              1. If you passed `timeZone` when creating managed user, then the default schedule from Monday to Friday from 9AM to 5PM will be created with that timezone. The managed user can then change the default schedule via the `AvailabilitySettings` atom.
              2. If you did not, then we assume you want the user to have this specific schedule right away. You should create a default schedule by specifying
              `"isDefault": true` in the request body. Until the user has a default schedule the user can't be booked nor manage their schedule via the AvailabilitySettings atom.

              The second goal of schedules is to create another schedule that event types can point to. This is useful for when an event is booked because availability is not checked against the default schedule but instead against that specific schedule.
              After creating a non-default schedule, you can update an event type to point to that schedule via the PATCH `event-types/{eventTypeId}` endpoint.

              When specifying start time and end time for each day use the 24 hour format e.g. 08:00, 15:00 etc.

              <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>

        If accessed using an OAuth access token, the `SCHEDULE_WRITE` scope is
        required.
              
      operationId: SchedulesController_2024_06_11_createSchedule
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
            example: '2024-06-11'
            default: '2024-06-11'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateScheduleInput_2024_06_11'
      responses:
        '201':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateScheduleOutput_2024_06_11'
components:
  schemas:
    CreateScheduleInput_2024_06_11:
      type: object
      properties:
        name:
          type: string
          example: Catch up hours
        timeZone:
          type: string
          example: Europe/Rome
          description: >-
            Timezone is used to calculate available times when an event using
            the schedule is booked.
        availability:
          description: >-
            Each object contains days and times when the user is available. If
            not passed, the default availability is Monday to Friday from 09:00
            to 17:00.
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
          description: >-
            Each user should have 1 default schedule. If you specified
            `timeZone` when creating managed user, then the default schedule
            will be created with that timezone.
                Default schedule means that if an event type is not tied to a specific schedule then the default schedule is used.
        overrides:
          description: Need to change availability for a specific date? Add an override.
          example:
            - date: '2024-05-20'
              startTime: '18:00'
              endTime: '21:00'
          type: array
          items:
            $ref: '#/components/schemas/ScheduleOverrideInput_2024_06_11'
      required:
        - name
        - timeZone
        - isDefault
    CreateScheduleOutput_2024_06_11:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
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