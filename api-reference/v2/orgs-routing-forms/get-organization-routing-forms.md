> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get organization routing forms

> Required membership role: `org admin`. PBAC permission: `routingForm.readOrgRoutingForms`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control. If accessed using an OAuth access token, the `ORG_ROUTING_FORM_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/organizations/{orgId}/routing-forms
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
  /v2/organizations/{orgId}/routing-forms:
    get:
      tags:
        - Orgs / Routing forms
      summary: Get organization routing forms
      description: >-
        Required membership role: `org admin`. PBAC permission:
        `routingForm.readOrgRoutingForms`. Learn more about API access control
        at https://cal.com/docs/api-reference/v2/access-control. If accessed
        using an OAuth access token, the `ORG_ROUTING_FORM_READ` scope is
        required.
      operationId: OrganizationsRoutingFormsController_getOrganizationRoutingForms
      parameters:
        - name: Authorization
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_
          required: true
          schema:
            type: string
        - name: orgId
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
        - name: teamIds
          required: false
          in: query
          description: Filter by teamIds. Team ids must be separated by a comma.
          schema:
            minItems: 1
            example: '?teamIds=100,200'
            type: array
            items:
              type: number
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetRoutingFormsOutput'
components:
  schemas:
    GetRoutingFormsOutput:
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
            $ref: '#/components/schemas/RoutingFormOutput'
      required:
        - status
        - data
    RoutingFormOutput:
      type: object
      properties:
        name:
          type: string
          example: My Form
        description:
          type: string
          nullable: true
          example: This is the description.
        position:
          type: number
          example: 0
        routes:
          type: object
          additionalProperties: true
          nullable: true
          description: Routing form routes configuration
        createdAt:
          type: string
          example: '2024-03-28T10:00:00.000Z'
          format: date-time
        updatedAt:
          type: string
          example: '2024-03-28T10:00:00.000Z'
          format: date-time
        fields:
          type: object
          additionalProperties: true
          nullable: true
          description: Routing form fields configuration
        userId:
          type: number
          example: 2313
        teamId:
          type: number
          nullable: true
          example: 4214321
        disabled:
          type: boolean
          example: false
        settings:
          type: object
          additionalProperties: true
          nullable: true
          description: Routing form settings
        id:
          type: string
      required:
        - name
        - description
        - position
        - createdAt
        - updatedAt
        - userId
        - teamId
        - disabled
        - id

````