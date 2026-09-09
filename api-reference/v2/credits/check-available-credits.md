> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Check available credits

> Check if the authenticated user (or their org/team) has available credits and return the current balance. Third-party OAuth tokens require the `CREDITS_READ` scope.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/credits/available
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
  /v2/credits/available:
    get:
      tags:
        - Credits
      summary: Check available credits
      description: >-
        Check if the authenticated user (or their org/team) has available
        credits and return the current balance. Third-party OAuth tokens require
        the `CREDITS_READ` scope.
      operationId: CreditsController_getAvailableCredits
      parameters: []
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object

````