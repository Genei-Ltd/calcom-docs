> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get reserved slot

> <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/slots/reservations/{uid}
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
    get:
      tags:
        - Slots
      summary: Get reserved slot
      description: >-
        <Note>Please make sure to pass in the cal-api-version header value as
        mentioned in the Headers section. Not passing the correct value will
        default to an older version of this endpoint.</Note>
      operationId: SlotsController_2024_09_04_getReservedSlot
      parameters:
        - name: cal-api-version
          in: header
          description: >-
            Must be set to 2024-09-04. If not set to this value, the endpoint
            will default to an older version.
          required: true
          schema:
            type: string
            example: '2024-09-04'
            default: '2024-09-04'
        - name: uid
          required: true
          in: path
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetReservedSlotOutput_2024_09_04'
components:
  schemas:
    GetReservedSlotOutput_2024_09_04:
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
            - $ref: '#/components/schemas/GetReservedSlotOutput_2024_09_04'
      required:
        - status
        - data

````