> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a reserved slot

> <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>



## OpenAPI

````yaml /api-reference/v2/openapi.json patch /v2/slots/reservations/{uid}
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
  /v2/slots/reservations/{uid}:
    patch:
      tags:
        - Slots
      summary: Update a reserved slot
      description: >-
        <Note>Please make sure to pass in the cal-api-version header value as
        mentioned in the Headers section. Not passing the correct value will
        default to an older version of this endpoint.</Note>
      operationId: SlotsController_2024_09_04_updateReservedSlot
      parameters:
        - name: cal-api-version
          in: header
          description: >-
            Must be set to 2024-09-04. If not set to this value, the endpoint
            will default to an older version.
          required: true
          schema:
            type: string
            default: '2024-09-04'
        - name: uid
          required: true
          in: path
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ReserveSlotInput_2024_09_04'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ReserveSlotOutputResponse_2024_09_04'
components:
  schemas:
    ReserveSlotInput_2024_09_04:
      type: object
      properties:
        eventTypeId:
          type: number
          example: 1
          description: The ID of the event type for which slot should be reserved.
        slotStart:
          type: string
          example: '2024-09-04T09:00:00Z'
          description: ISO 8601 datestring in UTC timezone representing available slot.
          format: date-time
        slotDuration:
          type: number
          example: 30
          description: >-
            By default slot duration is equal to event type length, but if you
            want to reserve a slot for an event type that has a variable length
            you can specify it here as a number in minutes. If you don't have
            this set explicitly that event type can have one of many lengths you
            can omit this.
        reservationDuration:
          type: number
          example: 5
          description: >-
            ONLY for authenticated requests with api key, access token or OAuth
            credentials (ID + secret).
                  
                  For how many minutes the slot should be reserved - for this long time noone else can book this event type at `start` time. If not provided, defaults to 5 minutes.
      required:
        - eventTypeId
        - slotStart
    ReserveSlotOutputResponse_2024_09_04:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          $ref: '#/components/schemas/ReserveSlotOutput_2024_09_04'
      required:
        - status
        - data
    ReserveSlotOutput_2024_09_04:
      type: object
      properties:
        eventTypeId:
          type: number
          example: 1
          description: The ID of the event type for which slot was reserved.
        slotStart:
          type: string
          example: '2024-09-04T09:00:00Z'
          description: ISO 8601 datestring in UTC timezone representing available slot.
          format: date-time
        slotEnd:
          type: string
          example: '2024-09-04T10:00:00Z'
          description: ISO 8601 datestring in UTC timezone representing slot end.
          format: date-time
        slotDuration:
          type: number
          example: 30
          description: >-
            By default slot duration is equal to event type length, but if you
            want to reserve a slot for an event type that has a variable length
            you can specify it here. If you don't have this set explicitly that
            event type can have one of many lengths you can omit this.
        reservationUid:
          type: string
          example: e84be5a3-4696-49e3-acc7-b2f3999c3b94
          description: >-
            The unique identifier of the reservation. Use it to update, get or
            delete the reservation.
        reservationDuration:
          type: number
          example: 5
          description: >-
            For how many minutes the slot is reserved - for this long time noone
            else can book this event type at `start` time.
        reservationUntil:
          type: string
          example: '2023-09-04T10:00:00Z'
          description: >-
            ISO 8601 datestring in UTC timezone representing time until which
            the slot is reserved.
          format: date-time
      required:
        - eventTypeId
        - slotStart
        - slotEnd
        - slotDuration
        - reservationUid
        - reservationDuration
        - reservationUntil

````