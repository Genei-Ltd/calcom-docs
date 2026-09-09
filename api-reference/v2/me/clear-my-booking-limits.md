> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Clear my booking limits

> Removes all of the authenticated user's global booking limits. Only available to organization members — non-org accounts receive a 403. If accessed using an OAuth access token, the `PROFILE_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json delete /v2/me/booking-limits
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
  /v2/me/booking-limits:
    delete:
      tags:
        - Me
      summary: Clear my booking limits
      description: >-
        Removes all of the authenticated user's global booking limits. Only
        available to organization members — non-org accounts receive a 403. If
        accessed using an OAuth access token, the `PROFILE_WRITE` scope is
        required.
      operationId: MeController_clearMyBookingLimits
      parameters:
        - name: Authorization
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_, managed user access token, or OAuth access token
          required: true
          schema:
            type: string
      responses:
        '204':
          description: ''

````