> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a managed user

> <Warning>These endpoints are deprecated and will be removed in the future.</Warning>



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/oauth-clients/{clientId}/users
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
    post:
      tags:
        - 'Deprecated: Platform / Managed Users'
      summary: Create a managed user
      description: >-
        <Warning>These endpoints are deprecated and will be removed in the
        future.</Warning>
      operationId: OAuthClientUsersController_createUser
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
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateManagedUserInput'
      responses:
        '201':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateManagedUserOutput'
components:
  schemas:
    CreateManagedUserInput:
      type: object
      properties:
        email:
          type: string
          example: alice@example.com
        name:
          type: string
          example: Alice Smith
          description: Managed user's name is used in emails
        timeFormat:
          type: number
          example: 12
          enum:
            - 12
            - 24
          description: Must be a number 12 or 24
        weekStart:
          type: string
          example: Monday
          enum:
            - Monday
            - Tuesday
            - Wednesday
            - Thursday
            - Friday
            - Saturday
            - Sunday
        timeZone:
          type: string
          example: America/New_York
          description: >-
            Timezone is used to create user's default schedule from Monday to
            Friday from 9AM to 5PM. If it is not passed then user does not have
                  a default schedule and it must be created manually via the /schedules endpoint. Until the schedule is created, the user can't access availability atom to set his / her availability nor booked.
                  It will default to Europe/London if not passed.
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
          example: https://cal.com/api/avatar/2b735186-b01b-46d3-87da-019b8f61776b.png
          description: URL of the user's avatar image
        bio:
          type: string
          description: Bio
          example: I am a bio
        metadata:
          type: object
          description: >-
            You can store any additional data you want here. Metadata must have
            at most 50 keys, each key up to 40 characters, and values up to 500
            characters.
          example:
            key: value
      required:
        - email
        - name
    CreateManagedUserOutput:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          $ref: '#/components/schemas/CreateManagedUserData'
      required:
        - status
        - data
    CreateManagedUserData:
      type: object
      properties:
        accessToken:
          type: string
          example: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
        refreshToken:
          type: string
          example: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
        user:
          $ref: '#/components/schemas/ManagedUserOutput'
        accessTokenExpiresAt:
          type: number
        refreshTokenExpiresAt:
          type: number
      required:
        - accessToken
        - refreshToken
        - user
        - accessTokenExpiresAt
        - refreshTokenExpiresAt
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
          example: https://cal.com/api/avatar/2b735186-b01b-46d3-87da-019b8f61776b.png
          description: URL of the user's avatar image
        metadata:
          type: object
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