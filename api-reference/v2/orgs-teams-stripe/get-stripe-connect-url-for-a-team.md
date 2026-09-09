> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Stripe connect URL for a team

> Required membership role: `team admin`. PBAC permission: `organization.manageBilling`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/organizations/{orgId}/teams/{teamId}/stripe/connect
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
  /v2/organizations/{orgId}/teams/{teamId}/stripe/connect:
    get:
      tags:
        - Orgs / Teams / Stripe
      summary: Get Stripe connect URL for a team
      description: >-
        Required membership role: `team admin`. PBAC permission:
        `organization.manageBilling`. Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control
      operationId: OrganizationsStripeController_getTeamStripeConnectUrl
      parameters:
        - name: Authorization
          required: true
          in: header
          schema:
            type: string
        - name: teamId
          required: true
          in: path
          schema:
            type: number
        - name: orgId
          required: true
          in: path
          schema:
            type: number
        - name: returnTo
          required: true
          in: query
          schema:
            type: string
        - name: onErrorReturnTo
          required: true
          in: query
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/StripConnectOutputResponseDto'
components:
  schemas:
    StripConnectOutputResponseDto:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/StripConnectOutputDto'
      required:
        - status
        - data
    StripConnectOutputDto:
      type: object
      properties:
        authUrl:
          type: string
      required:
        - authUrl

````