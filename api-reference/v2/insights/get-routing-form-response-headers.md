> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get routing form response headers

> Get routing form response headers for user, team, or organization insights.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/insights/routings/form-response-headers
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
  /v2/insights/routings/form-response-headers:
    post:
      tags:
        - Insights
      summary: Get routing form response headers
      description: >-
        Get routing form response headers for user, team, or organization
        insights.
      operationId: InsightsController_getRoutingFormHeaders
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RoutingFormFieldsInput'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetInsightsRoutingFormHeadersOutput'
components:
  schemas:
    RoutingFormFieldsInput:
      type: object
      properties:
        scope:
          type: string
          enum:
            - user
            - team
            - org
          example: user
        selectedTeamId:
          type: number
          description: Team ID for team-scoped routing insights
          example: 12
        routingFormId:
          type: string
          description: Routing form ID to filter fields
          example: form_123
      required:
        - scope
    GetInsightsRoutingFormHeadersOutput:
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
            $ref: '#/components/schemas/InsightsRoutingFormFieldOutput'
      required:
        - status
        - data
    InsightsRoutingFormFieldOutput:
      type: object
      properties:
        id:
          type: string
          example: field_1
        label:
          type: string
          example: Company size
        type:
          type: string
          example: select
        options:
          type: array
          items:
            $ref: '#/components/schemas/InsightsRoutingFormFieldOptionOutput'
      required:
        - id
        - label
    InsightsRoutingFormFieldOptionOutput:
      type: object
      properties:
        id:
          type: string
          example: option_1
          nullable: true
        label:
          type: string
          example: Enterprise
      required:
        - id
        - label

````