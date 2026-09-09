> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all out-of-office entries for a user

> If accessed using an OAuth access token, the `ORG_SCHEDULE_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/organizations/{orgId}/users/{userId}/ooo
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
  /v2/organizations/{orgId}/users/{userId}/ooo:
    get:
      tags:
        - Orgs / Users / OOO
      summary: Get all out-of-office entries for a user
      description: >-
        If accessed using an OAuth access token, the `ORG_SCHEDULE_READ` scope
        is required.
      operationId: OrganizationsUsersOOOController_getOrganizationUserOOO
      parameters:
        - name: Authorization
          in: header
          description: >-
            For non-platform customers - value must be `Bearer <token>` where
            `<token>` is api key prefixed with cal_
          required: false
          schema:
            type: string
        - name: x-cal-secret-key
          in: header
          description: For platform customers - OAuth client secret key
          required: false
          schema:
            type: string
        - name: x-cal-client-id
          in: header
          description: For platform customers - OAuth client ID
          required: false
          schema:
            type: string
        - name: userId
          required: true
          in: path
          schema:
            type: number
        - name: take
          required: false
          in: query
          description: Maximum number of items to return
          schema:
            minimum: 1
            maximum: 250
            default: 250
            example: 25
            type: number
        - name: skip
          required: false
          in: query
          description: Number of items to skip
          schema:
            minimum: 0
            default: 0
            example: 0
            type: number
        - name: sortStart
          required: false
          in: query
          description: Sort results by their start time in ascending or descending order.
          schema:
            example: '?sortStart=asc OR ?sortStart=desc'
            enum:
              - asc
              - desc
            type: string
        - name: sortEnd
          required: false
          in: query
          description: Sort results by their end time in ascending or descending order.
          schema:
            example: '?sortEnd=asc OR ?sortEnd=desc'
            enum:
              - asc
              - desc
            type: string
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
                $ref: '#/components/schemas/UserOoosOutputResponseDto'
components:
  schemas:
    UserOoosOutputResponseDto:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          type: array
          items:
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