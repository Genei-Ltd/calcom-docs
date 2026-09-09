> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update routing form response

> Required membership role: `team admin`. PBAC permission: `routingForm.update`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control. If accessed using an OAuth access token, the `TEAM_ROUTING_FORM_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json patch /v2/organizations/{orgId}/teams/{teamId}/routing-forms/{routingFormId}/responses/{responseId}
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
  /v2/organizations/{orgId}/teams/{teamId}/routing-forms/{routingFormId}/responses/{responseId}:
    patch:
      tags:
        - Orgs / Teams / Routing forms / Responses
      summary: Update routing form response
      description: >-
        Required membership role: `team admin`. PBAC permission:
        `routingForm.update`. Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control. If accessed using
        an OAuth access token, the `TEAM_ROUTING_FORM_WRITE` scope is required.
      operationId: >-
        OrganizationsTeamsRoutingFormsResponsesController_updateRoutingFormResponse
      parameters:
        - name: Authorization
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_
          required: true
          schema:
            type: string
        - name: teamId
          required: true
          in: path
          schema:
            type: number
        - name: routingFormId
          required: true
          in: path
          schema:
            type: string
        - name: responseId
          required: true
          in: path
          schema:
            type: number
        - name: orgId
          required: true
          in: path
          schema:
            type: number
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateRoutingFormResponseInput'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UpdateRoutingFormResponseOutput'
components:
  schemas:
    UpdateRoutingFormResponseInput:
      type: object
      properties:
        response:
          type: object
          additionalProperties: true
          description: The updated response data
    UpdateRoutingFormResponseOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
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