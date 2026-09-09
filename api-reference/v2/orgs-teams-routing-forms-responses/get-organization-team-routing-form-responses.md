> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get organization team routing form responses

> Required membership role: `team admin`. PBAC permission: `routingForm.readResponsePii`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control. If accessed using an OAuth access token, the `TEAM_ROUTING_FORM_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/organizations/{orgId}/teams/{teamId}/routing-forms/{routingFormId}/responses
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
  /v2/organizations/{orgId}/teams/{teamId}/routing-forms/{routingFormId}/responses:
    get:
      tags:
        - Orgs / Teams / Routing forms / Responses
      summary: Get organization team routing form responses
      description: >-
        Required membership role: `team admin`. PBAC permission:
        `routingForm.readResponsePii`. Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control. If accessed using
        an OAuth access token, the `TEAM_ROUTING_FORM_READ` scope is required.
      operationId: >-
        OrganizationsTeamsRoutingFormsResponsesController_getRoutingFormResponses
      parameters:
        - name: Authorization
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_
          required: true
          schema:
            type: string
        - name: routingFormId
          required: true
          in: path
          schema:
            type: string
        - name: orgId
          required: true
          in: path
          schema:
            type: number
        - name: teamId
          required: true
          in: path
          schema:
            type: number
        - name: skip
          required: false
          in: query
          description: Number of responses to skip
          schema:
            type: number
        - name: take
          required: false
          in: query
          description: Number of responses to take
          schema:
            type: number
        - name: sortCreatedAt
          required: false
          in: query
          description: Sort by creation time
          schema:
            type: string
            enum:
              - asc
              - desc
        - name: sortUpdatedAt
          required: false
          in: query
          description: Sort by update time
          schema:
            type: string
            enum:
              - asc
              - desc
        - name: afterCreatedAt
          required: false
          in: query
          description: Filter by responses created after this date
          schema:
            format: date-time
            type: string
        - name: beforeCreatedAt
          required: false
          in: query
          description: Filter by responses created before this date
          schema:
            format: date-time
            type: string
        - name: afterUpdatedAt
          required: false
          in: query
          description: Filter by responses created after this date
          schema:
            format: date-time
            type: string
        - name: beforeUpdatedAt
          required: false
          in: query
          description: Filter by responses updated before this date
          schema:
            format: date-time
            type: string
        - name: routedToBookingUid
          required: false
          in: query
          description: Filter by responses routed to a specific booking
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetRoutingFormResponsesOutput'
components:
  schemas:
    GetRoutingFormResponsesOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          type: array
          items:
            $ref: '#/components/schemas/RoutingFormResponseOutput'
      required:
        - status
        - data
    RoutingFormResponseOutput:
      type: object
      properties:
        id:
          type: number
        formId:
          type: string
        formFillerId:
          type: string
        routedToBookingUid:
          type: string
        response:
          type: object
          additionalProperties: true
          example:
            f00b26df-f54b-4985-8d98-17c5482c6a24:
              label: participant
              value: mamut
        createdAt:
          format: date-time
          type: string
      required:
        - id
        - formId
        - formFillerId
        - routedToBookingUid
        - response
        - createdAt

````