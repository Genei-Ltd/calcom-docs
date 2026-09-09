> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update my profile

> Updates the authenticated user's profile. Email changes require verification and the primary email stays unchanged until verification completes, unless the new email is already a verified secondary email or the user is platform-managed. If accessed using an OAuth access token, the `PROFILE_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json patch /v2/me
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
  /v2/me:
    patch:
      tags:
        - Me
      summary: Update my profile
      description: >-
        Updates the authenticated user's profile. Email changes require
        verification and the primary email stays unchanged until verification
        completes, unless the new email is already a verified secondary email or
        the user is platform-managed. If accessed using an OAuth access token,
        the `PROFILE_WRITE` scope is required.
      operationId: MeController_updateMe
      parameters:
        - name: Authorization
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_, managed user access token, or OAuth access token
          required: true
          schema:
            type: string
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
                $ref: '#/components/schemas/UpdateMeOutput'
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
    UpdateMeOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/MeOutput'
      required:
        - status
        - data
    MeOutput:
      type: object
      properties:
        id:
          type: number
        username:
          type: string
        email:
          type: string
          format: email
        name:
          type: string
          nullable: true
        avatarUrl:
          type: string
          nullable: true
        bio:
          type: string
          nullable: true
        timeFormat:
          type: number
        defaultScheduleId:
          type: number
          nullable: true
        weekStart:
          type: string
        timeZone:
          type: string
        locale:
          type: string
          nullable: true
          example: en
          description: The user's locale setting
        organizationId:
          type: number
          nullable: true
        organization:
          $ref: '#/components/schemas/MeOrgOutput'
      required:
        - id
        - username
        - email
        - name
        - avatarUrl
        - bio
        - timeFormat
        - defaultScheduleId
        - weekStart
        - timeZone
        - locale
        - organizationId
    MeOrgOutput:
      type: object
      properties:
        isPlatform:
          type: boolean
        id:
          type: number
      required:
        - isPlatform
        - id

````