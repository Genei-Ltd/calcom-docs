> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update an out-of-office entry for a team member

> If accessed using an OAuth access token, the `TEAM_SCHEDULE_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json patch /v2/teams/{teamId}/users/{userId}/ooo/{oooId}
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
  /v2/teams/{teamId}/users/{userId}/ooo/{oooId}:
    patch:
      tags:
        - Teams / Users / OOO
      summary: Update an out-of-office entry for a team member
      description: >-
        If accessed using an OAuth access token, the `TEAM_SCHEDULE_WRITE` scope
        is required.
      operationId: TeamsOOOController_updateTeamMemberOOO
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
        - name: userId
          required: true
          in: path
          schema:
            type: number
        - name: oooId
          required: true
          in: path
          schema:
            type: number
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateOutOfOfficeEntryDto'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserOooOutputResponseDto'
components:
  schemas:
    UpdateOutOfOfficeEntryDto:
      type: object
      properties:
        start:
          format: date-time
          type: string
          description: >-
            The start date and time of the out of office period in ISO 8601
            format in UTC timezone.
          example: '2023-05-01T00:00:00.000Z'
        end:
          format: date-time
          type: string
          description: >-
            The end date and time of the out of office period in ISO 8601 format
            in UTC timezone.
          example: '2023-05-10T23:59:59.999Z'
        notes:
          type: string
          description: Optional notes for the out of office entry.
          example: Vacation in Hawaii
        toUserId:
          type: number
          description: >-
            The ID of the user covering for the out of office period, if
            applicable.
          example: 2
        reason:
          enum:
            - unspecified
            - vacation
            - travel
            - sick
            - public_holiday
          type: string
          description: the reason for the out of office entry, if applicable
          example: vacation
    UserOooOutputResponseDto:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          $ref: '#/components/schemas/UserOooOutputDto'
      required:
        - status
        - data
    UserOooOutputDto:
      type: object
      properties:
        userId:
          type: number
          description: The ID of the user.
          example: 2
        toUserId:
          type: number
          description: >-
            The ID of the user covering for the out of office period, if
            applicable.
          example: 2
        id:
          type: number
          description: The ID of the ooo entry.
          example: 2
        uuid:
          type: string
          description: The UUID of the ooo entry.
          example: e84be5a3-4696-49e3-acc7-b2f3999c3b94
        start:
          format: date-time
          type: string
          description: >-
            The start date and time of the out of office period in ISO 8601
            format in UTC timezone.
          example: '2023-05-01T00:00:00.000Z'
        end:
          format: date-time
          type: string
          description: >-
            The end date and time of the out of office period in ISO 8601 format
            in UTC timezone.
          example: '2023-05-10T23:59:59.999Z'
        notes:
          type: string
          description: Optional notes for the out of office entry.
          example: Vacation in Hawaii
        reason:
          enum:
            - unspecified
            - vacation
            - travel
            - sick
            - public_holiday
          type: string
          description: the reason for the out of office entry, if applicable
          example: vacation
      required:
        - userId
        - id
        - uuid
        - start
        - end

````