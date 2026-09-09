> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get busy times

> Get busy times from a calendar. Example request URL is `https://api.cal.com/v2/calendars/busy-times?timeZone=Europe%2FMadrid&dateFrom=2024-12-18&dateTo=2024-12-18&calendarsToLoad[0][credentialId]=135&calendarsToLoad[0][externalId]=skrauciz%40gmail.com`. Note: loggedInUsersTz is deprecated, use timeZone instead. If accessed using an OAuth access token, the `APPS_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/calendars/busy-times
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
  /v2/calendars/busy-times:
    get:
      tags:
        - Calendars
      summary: Get busy times
      description: >-
        Get busy times from a calendar. Example request URL is
        `https://api.cal.com/v2/calendars/busy-times?timeZone=Europe%2FMadrid&dateFrom=2024-12-18&dateTo=2024-12-18&calendarsToLoad[0][credentialId]=135&calendarsToLoad[0][externalId]=skrauciz%40gmail.com`.
        Note: loggedInUsersTz is deprecated, use timeZone instead. If accessed
        using an OAuth access token, the `APPS_READ` scope is required.
      operationId: CalendarsController_getBusyTimes
      parameters:
        - name: loggedInUsersTz
          required: false
          in: query
          deprecated: true
          description: >-
            Deprecated: Use timeZone instead. The timezone of the user
            represented as a string
          schema:
            type: string
            example: America/New_York
        - name: timeZone
          required: false
          in: query
          description: The timezone for the busy times query represented as a string
          schema:
            type: string
            example: America/New_York
        - name: dateFrom
          required: true
          in: query
          description: The starting date for the busy times query
          schema:
            example: '2023-10-01'
            type: string
        - name: dateTo
          required: true
          in: query
          description: The ending date for the busy times query
          schema:
            example: '2023-10-31'
            type: string
        - name: calendarsToLoad
          required: true
          in: query
          description: >-
            An array of Calendar objects representing the calendars to be
            loaded. Use bracket notation in the URL, e.g.:
            calendarsToLoad[0][credentialId]=135&calendarsToLoad[0][externalId]=email@example.com
          schema:
            type: array
            items:
              type: object
              properties:
                credentialId:
                  type: number
                  example: 135
                externalId:
                  type: string
                  example: email@example.com
              required:
                - credentialId
                - externalId
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
                $ref: '#/components/schemas/GetBusyTimesOutput'
components:
  schemas:
    GetBusyTimesOutput:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          type: array
          items:
            $ref: '#/components/schemas/BusyTimesOutput'
      required:
        - status
        - data
    BusyTimesOutput:
      type: object
      properties:
        start:
          format: date-time
          type: string
        end:
          format: date-time
          type: string
        source:
          type: string
          nullable: true
      required:
        - start
        - end

````