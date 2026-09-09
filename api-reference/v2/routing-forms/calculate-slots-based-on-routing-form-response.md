> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Calculate slots based on routing form response

> It will not actually save the response just return the routed event type and slots when it can be booked.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/routing-forms/{routingFormId}/calculate-slots
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
  /v2/routing-forms/{routingFormId}/calculate-slots:
    post:
      tags:
        - Routing forms
      summary: Calculate slots based on routing form response
      description: >-
        It will not actually save the response just return the routed event type
        and slots when it can be booked.
      operationId: RoutingFormsController_calculateSlotsBasedOnRoutingFormResponse
      parameters:
        - name: Authorization
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_, managed user access token, or OAuth access token
          required: true
          schema:
            type: string
        - name: start
          required: true
          in: query
          description: |2-

                  Time starting from which available slots should be checked.
                
                  Must be in UTC timezone as ISO 8601 datestring.
                  
                  You can pass date without hours which defaults to start of day or specify hours:
                  2024-08-13 (will have hours 00:00:00 aka at very beginning of the date) or you can specify hours manually like 2024-08-13T09:00:00Z
                  
          schema:
            example: '2050-09-05'
            type: string
        - name: end
          required: true
          in: query
          description: |2-

                  Time until which available slots should be checked.
                  
                  Must be in UTC timezone as ISO 8601 datestring.
                  
                  You can pass date without hours which defaults to end of day or specify hours:
                  2024-08-20 (will have hours 23:59:59 aka at the very end of the date) or you can specify hours manually like 2024-08-20T18:00:00Z
          schema:
            example: '2050-09-06'
            type: string
        - name: timeZone
          required: false
          in: query
          description: >-
            Time zone in which the available slots should be returned. Defaults
            to UTC.
          schema:
            type: string
            example: Europe/Rome
        - name: duration
          required: false
          in: query
          description: >-
            If event type has multiple possible durations then you can specify
            the desired duration here. Also, if you are fetching slots for a
            dynamic event then you can specify the duration her which defaults
            to 30, meaning that returned slots will be each 30 minutes long.
          schema:
            example: '60'
            type: number
        - name: format
          required: false
          in: query
          description: >-
            Format of slot times in response. Use 'range' to get start and end
            times.
          schema:
            example: range
            type: string
            enum:
              - range
              - time
        - name: bookingUidToReschedule
          required: false
          in: query
          description: >-
            The unique identifier of the booking being rescheduled. When
            provided will ensure that the original booking time appears within
            the returned available slots when rescheduling.
          schema:
            type: string
            example: abc123def456
        - name: rescheduleWithSameHost
          required: false
          in: query
          description: >-
            Only for round robin event types that allow the person rescheduling
            to choose the host. True returns slots of the original host, false
            returns slots of any available host. Ignored for other event types.
          schema:
            type: boolean
            example: true
        - name: routingFormId
          required: true
          in: path
          schema:
            type: string
      requestBody:
        required: true
        description: >-
          The routing form response, as a map of field identifier to answer.
          Answers use the option label, not the option id. Must not be empty -
          without answers no route can match.
        content:
          application/json:
            schema:
              type: object
              additionalProperties:
                type: string
              example:
                email: jane@example.com
                department: sales
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResponseSlotsOutput'
components:
  schemas:
    ResponseSlotsOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/ResponseSlotsOutputData'
      required:
        - status
        - data
    ResponseSlotsOutputData:
      type: object
      properties:
        eventTypeId:
          type: number
        slots:
          additionalProperties: true
          oneOf:
            - $ref: '#/components/schemas/SlotsOutput_2024_09_04'
              title: Time Slots
            - $ref: '#/components/schemas/RangeSlotsOutput_2024_09_04'
              title: Slot Ranges
      required:
        - eventTypeId
        - slots
    SlotsOutput_2024_09_04:
      type: object
      properties: {}
    RangeSlotsOutput_2024_09_04:
      type: object
      properties: {}

````