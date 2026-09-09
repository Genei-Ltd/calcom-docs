> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a schedule

> <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>

If accessed using an OAuth access token, the `SCHEDULE_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json delete /v2/schedules/{scheduleId}
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
    delete:
      tags:
        - Schedules
      summary: Delete a schedule
      description: >-
        <Note>Please make sure to pass in the cal-api-version header value as
        mentioned in the Headers section. Not passing the correct value will
        default to an older version of this endpoint.</Note>


        If accessed using an OAuth access token, the `SCHEDULE_WRITE` scope is
        required.
      operationId: SchedulesController_2024_06_11_deleteSchedule
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
            type: number
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeleteScheduleOutput_2024_06_11'
components:
  schemas:
    DeleteScheduleOutput_2024_06_11:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
      required:
        - status

````