> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a managed user

> <Warning>These endpoints are deprecated and will be removed in the future.</Warning>



## OpenAPI

````yaml /api-reference/v2/openapi.json patch /v2/oauth-clients/{clientId}/users/{userId}
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
  /v2/oauth-clients/{clientId}/users/{userId}:
    patch:
      tags:
        - 'Deprecated: Platform / Managed Users'
      summary: Update a managed user
      description: >-
        <Warning>These endpoints are deprecated and will be removed in the
        future.</Warning>
      operationId: OAuthClientUsersController_updateUser
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
        - name: userId
          required: true
          in: path
          schema:
            type: number
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateManagedUserInput'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetManagedUserOutput'
components:
  schemas:
    UpdateManagedUserInput:
      type: object
      properties:
        email:
          type: string
        name:
          type: string
        timeFormat:
          enum:
            - 12
            - 24
          type: number
          example: 12
          description: Must be 12 or 24
        defaultScheduleId:
          type: number
        weekStart:
          enum:
            - Monday
            - Tuesday
            - Wednesday
            - Thursday
            - Friday
            - Saturday
            - Sunday
          type: string
          example: Monday
        timeZone:
          type: string
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
          format: uri
          example: https://cal.com/api/avatar/2b735186-b01b-46d3-87da-019b8f61776b.png
          description: URL of the user's avatar image
        bio:
          type: string
          description: Bio
          example: I am a bio
        metadata:
          type: object
          additionalProperties: true
          description: >-
            You can store any additional data you want here. Metadata must have
            at most 50 keys, each key up to 40 characters, and values up to 500
            characters.
          example:
            key: value
    GetManagedUserOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
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