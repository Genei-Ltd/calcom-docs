> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Save Stripe credentials

> Required membership role: `team admin`. PBAC permission: `organization.manageBilling`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/organizations/{orgId}/teams/{teamId}/stripe/save
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
  /v2/organizations/{orgId}/teams/{teamId}/stripe/save:
    get:
      tags:
        - Orgs / Teams / Stripe
      summary: Save Stripe credentials
      description: >-
        Required membership role: `team admin`. PBAC permission:
        `organization.manageBilling`. Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control
      operationId: OrganizationsStripeController_save
      parameters:
        - name: state
          required: true
          in: query
          schema:
            type: string
        - name: code
          required: true
          in: query
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
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/StripCredentialsSaveOutputResponseDto'
components:
  schemas:
    StripCredentialsSaveOutputResponseDto:
      type: object
      properties:
        url:
          type: string
      required:
        - url

````