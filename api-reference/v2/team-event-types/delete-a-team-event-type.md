> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a team event type

> <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>

Required membership role: `team admin`. PBAC permission: `eventType.delete`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control. If accessed using an OAuth access token, the `TEAM_EVENT_TYPE_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json delete /v2/teams/{teamId}/event-types/{eventTypeId}
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
  /v2/teams/{teamId}/event-types/{eventTypeId}:
    delete:
      tags:
        - Team Event Types
      summary: Delete a team event type
      description: >-
        <Note>Please make sure to pass in the cal-api-version header value as
        mentioned in the Headers section. Not passing the correct value will
        default to an older version of this endpoint.</Note>


        Required membership role: `team admin`. PBAC permission:
        `eventType.delete`. Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control. If accessed using
        an OAuth access token, the `TEAM_EVENT_TYPE_WRITE` scope is required.
      operationId: TeamsEventTypesController_2026_06_12_deleteTeamEventType
      parameters:
        - name: cal-api-version
          in: header
          description: >-
            Must be set to 2026-06-12. If not set to this value, the endpoint
            will default to an older version.
          required: true
          schema:
            type: string
            example: '2026-06-12'
            default: '2026-06-12'
        - name: teamId
          required: true
          in: path
          schema:
            type: number
        - name: eventTypeId
          required: true
          in: path
          schema:
            type: number
        - name: Authorization
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_, managed user access token, or OAuth access token
          required: true
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeleteTeamEventTypeOutput'
components:
  schemas:
    DeleteTeamEventTypeOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/DeletedTeamEventTypeData'
      required:
        - status
        - data
    DeletedTeamEventTypeData:
      type: object
      properties:
        id:
          type: number
          example: 1
        title:
          type: string
          example: Team Meeting
      required:
        - id
        - title

````