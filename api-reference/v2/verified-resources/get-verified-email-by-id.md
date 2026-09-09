> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get verified email by id

> If accessed using an OAuth access token, the `VERIFIED_RESOURCES_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/verified-resources/emails/{id}
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
  /v2/verified-resources/emails/{id}:
    get:
      tags:
        - Verified Resources
      summary: Get verified email by id
      description: >-
        If accessed using an OAuth access token, the `VERIFIED_RESOURCES_READ`
        scope is required.
      operationId: UserVerifiedResourcesController_getVerifiedEmailById
      parameters:
        - name: id
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
                $ref: '#/components/schemas/UserVerifiedEmailOutput'
components:
  schemas:
    UserVerifiedEmailOutput:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          $ref: '#/components/schemas/UserVerifiedEmailOutputData'
      required:
        - status
        - data
    UserVerifiedEmailOutputData:
      type: object
      properties:
        id:
          type: number
          description: The unique identifier for the verified email.
          example: 789
        email:
          type: string
          description: The verified email address.
          example: user@example.com
          format: email
        userId:
          type: number
          description: The ID of the associated user, if applicable.
          example: 45
      required:
        - id
        - email
        - userId

````