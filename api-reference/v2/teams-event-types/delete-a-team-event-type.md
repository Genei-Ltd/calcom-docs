> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a team event type

> If accessed using an OAuth access token, the `TEAM_EVENT_TYPE_WRITE` scope is required.



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
        - Teams / Event Types
      summary: Delete a team event type
      description: >-
        If accessed using an OAuth access token, the `TEAM_EVENT_TYPE_WRITE`
        scope is required.
      operationId: TeamsEventTypesController_deleteTeamEventType
      parameters:
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
            with cal_
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
          type: string
          example: success
          enum:
            - success
            - error
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