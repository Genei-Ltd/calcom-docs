> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all managed users

> <Warning>These endpoints are deprecated and will be removed in the future.</Warning>



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/oauth-clients/{clientId}/users
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
  /v2/oauth-clients/{clientId}/users:
    get:
      tags:
        - 'Deprecated: Platform / Managed Users'
      summary: Get all managed users
      description: >-
        <Warning>These endpoints are deprecated and will be removed in the
        future.</Warning>
      operationId: OAuthClientUsersController_getManagedUsers
      parameters:
        - name: x-cal-secret-key
          in: header
          description: OAuth client secret key
          required: true
          schema:
            type: string
        - name: clientId
          required: true
          in: path
          schema:
            type: string
        - name: limit
          required: false
          in: query
          description: The number of items to return
          schema:
            minimum: 1
            maximum: 250
            example: 10
            type: number
        - name: offset
          required: false
          in: query
          description: The number of items to skip
          schema:
            minimum: 0
            maximum: 250
            example: 0
            type: number
        - name: emails
          required: false
          in: query
          description: >-
            Filter managed users by email. If you want to filter by multiple
            emails, separate them with a comma.
          schema:
            minItems: 1
            example: '?emails=email1@example.com,email2@example.com'
            type: array
            items:
              type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetManagedUsersOutput'
components:
  schemas:
    GetManagedUsersOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          type: array
          items:
            $ref: '#/components/schemas/ManagedUserOutput'
      required:
        - status
        - data
    ManagedUserOutput:
      type: object
      properties:
        id:
          type: number
          example: 1
        email:
          type: string
          example: alice+cluo37fwd0001khkzqqynkpj3@example.com
        username:
          type: string
          nullable: true
          example: alice
        name:
          type: string
          nullable: true
          example: alice
        bio:
          type: string
          nullable: true
          example: bio
        timeZone:
          type: string
          example: America/New_York
        weekStart:
          type: string
          example: Sunday
        createdDate:
          type: string
          example: '2024-04-01T00:00:00.000Z'
          format: date-time
        timeFormat:
          type: number
          nullable: true
          example: 12
        defaultScheduleId:
          type: number
          nullable: true
          example: null
        locale:
          enum:
            - ar
            - ca
            - de
            - es
            - eu
            - he
            - id
            - ja
            - lv
            - pl
            - ro
            - sr
            - th
            - vi
            - az
            - cs
            - el
            - es-419
            - fi
            - hr
            - it
            - km
            - nl
            - pt
            - ru
            - sv
            - tr
            - zh-CN
            - bg
            - da
            - en
            - et
            - fr
            - hu
            - iw
            - ko
            - 'no'
            - pt-BR
            - sk
            - ta
            - uk
            - zh-TW
            - bn
          type: string
          example: en
        avatarUrl:
          type: string
          nullable: true
          format: uri
          example: https://cal.com/api/avatar/2b735186-b01b-46d3-87da-019b8f61776b.png
          description: URL of the user's avatar image
        metadata:
          type: object
          additionalProperties: true
          example:
            key: value
      required:
        - id
        - email
        - username
        - name
        - bio
        - timeZone
        - weekStart
        - createdDate
        - timeFormat
        - defaultScheduleId

````