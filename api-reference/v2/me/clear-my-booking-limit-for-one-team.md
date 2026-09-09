> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Clear my booking limit for one team

> Drops your own numbers for this team so the team default applies to you again. This does not lift the team's limit. If accessed using an OAuth access token, the `PROFILE_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json delete /v2/me/team-booking-limits/{teamId}
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
  /v2/me/team-booking-limits/{teamId}:
    delete:
      tags:
        - Me
      summary: Clear my booking limit for one team
      description: >-
        Drops your own numbers for this team so the team default applies to you
        again. This does not lift the team's limit. If accessed using an OAuth
        access token, the `PROFILE_WRITE` scope is required.
      operationId: MeController_clearMyTeamBookingLimit
      parameters:
        - name: Authorization
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_, managed user access token, or OAuth access token
          required: true
          schema:
            type: string
        - name: teamId
          required: true
          in: path
          schema:
            type: number
      responses:
        '204':
          description: ''

````