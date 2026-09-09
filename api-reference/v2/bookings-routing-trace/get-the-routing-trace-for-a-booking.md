> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get the routing trace for a booking

> Retrieve the step-by-step routing trace for a booking identified by its UID. Shows how the booking was routed through routing forms, CRM lookups, and host selection logic.

Returns presented (human-readable) trace steps grouped by routing round, along with the routing form submission if one was used.

If no routing trace exists for the booking, empty steps and groups are returned.

<Note>The cal-api-version header is required for this endpoint.</Note>

If accessed using an OAuth access token, the `BOOKING_READ` scope is required.
    



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/bookings/{bookingUid}/routing-trace
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
  /v2/bookings/{bookingUid}/routing-trace:
    get:
      tags:
        - Bookings / Routing Trace
      summary: Get the routing trace for a booking
      description: >-
        Retrieve the step-by-step routing trace for a booking identified by its
        UID. Shows how the booking was routed through routing forms, CRM
        lookups, and host selection logic.


        Returns presented (human-readable) trace steps grouped by routing round,
        along with the routing form submission if one was used.


        If no routing trace exists for the booking, empty steps and groups are
        returned.


        <Note>The cal-api-version header is required for this endpoint.</Note>


        If accessed using an OAuth access token, the `BOOKING_READ` scope is
        required.
            
      operationId: BookingRoutingTraceController_2024_08_13_getBookingRoutingTrace
      parameters:
        - name: cal-api-version
          in: header
          description: Must be set to `2024-08-13` or later.
          required: true
          schema:
            type: string
            example: '2024-08-13'
        - name: bookingUid
          required: true
          in: path
          schema:
            type: string
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
                $ref: '#/components/schemas/GetBookingRoutingTraceOutput_2024_08_13'
components:
  schemas:
    GetBookingRoutingTraceOutput_2024_08_13:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/RoutingTraceDataOutput_2024_08_13'
      required:
        - status
        - data
    RoutingTraceDataOutput_2024_08_13:
      type: object
      properties:
        steps:
          type: array
          items:
            $ref: '#/components/schemas/RoutingTraceStepOutput_2024_08_13'
        groups:
          type: array
          items:
            $ref: '#/components/schemas/RoutingTraceGroupOutput_2024_08_13'
        formSubmission:
          nullable: true
          type: object
          allOf:
            - $ref: '#/components/schemas/RoutingTraceFormSubmissionOutput_2024_08_13'
      required:
        - steps
        - groups
    RoutingTraceStepOutput_2024_08_13:
      type: object
      properties:
        message:
          type: string
          example: 'Account found by website match: acme.com'
        round:
          type: string
          example: Exact Match
        domain:
          type: string
          example: salesforce
        step:
          type: string
          example: account_found_by_website
        timestamp:
          type: number
          example: 1717000000000
        data:
          type: object
          additionalProperties: true
          description: Step-specific data payload
      required:
        - message
        - round
        - domain
        - step
        - timestamp
        - data
    RoutingTraceGroupOutput_2024_08_13:
      type: object
      properties:
        round:
          type: string
          example: Exact Match
        domain:
          type: string
          example: salesforce
        steps:
          type: array
          items:
            $ref: '#/components/schemas/RoutingTraceStepOutput_2024_08_13'
      required:
        - round
        - domain
        - steps
    RoutingTraceFormSubmissionOutput_2024_08_13:
      type: object
      properties:
        form:
          $ref: '#/components/schemas/RoutingTraceFormOutput_2024_08_13'
        responses:
          type: array
          items:
            $ref: '#/components/schemas/RoutingTraceFormResponseOutput_2024_08_13'
      required:
        - form
        - responses
    RoutingTraceFormOutput_2024_08_13:
      type: object
      properties:
        name:
          type: string
          example: Sales Routing Form
        description:
          type: string
          nullable: true
          example: Routes leads to the right sales rep
      required:
        - name
    RoutingTraceFormResponseOutput_2024_08_13:
      type: object
      properties:
        fieldId:
          type: string
          example: Company Size
        label:
          type: string
          example: Company Size
        displayValue:
          type: string
          example: Enterprise (1000+)
      required:
        - fieldId
        - label
        - displayValue

````