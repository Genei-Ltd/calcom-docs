> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Check team Stripe connection

> Required membership role: `team admin`. PBAC permission: `organization.manageBilling`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/organizations/{orgId}/teams/{teamId}/stripe/check
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
  /v2/organizations/{orgId}/teams/{teamId}/stripe/check:
    get:
      tags:
        - Orgs / Teams / Stripe
      summary: Check team Stripe connection
      description: >-
        Required membership role: `team admin`. PBAC permission:
        `organization.manageBilling`. Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control
      operationId: OrganizationsStripeController_checkTeamStripeConnection
      parameters:
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
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/StripCredentialsCheckOutputResponseDto'
components:
  schemas:
    StripCredentialsCheckOutputResponseDto:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
      required:
        - status

````