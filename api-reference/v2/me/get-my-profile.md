> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get my profile

> If accessed using an OAuth access token, the `PROFILE_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/me
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
    get:
      tags:
        - Me
      summary: Get my profile
      description: >-
        If accessed using an OAuth access token, the `PROFILE_READ` scope is
        required.
      operationId: MeController_getMe
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
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetMeOutput'
components:
  schemas:
    GetMeOutput:
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