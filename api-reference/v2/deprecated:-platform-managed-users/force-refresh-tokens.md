> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Force refresh tokens

> <Warning>These endpoints are deprecated and will be removed in the future.</Warning> If you have lost managed user access or refresh token, then you can get new ones by using OAuth credentials. Access token is valid for 60 minutes and refresh token for 1 year. Make sure to store them in your database, for example, in your User database model `calAccessToken` and `calRefreshToken` fields.
Response also contains `accessTokenExpiresAt` and `refreshTokenExpiresAt` fields, but if you decode the jwt token the payload will contain `clientId` (OAuth client ID), `ownerId` (user to whom token belongs ID), `iat` (issued at time) and `expiresAt` (when does the token expire) fields.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/oauth-clients/{clientId}/users/{userId}/force-refresh
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
  /v2/oauth-clients/{clientId}/users/{userId}/force-refresh:
    post:
      tags:
        - 'Deprecated: Platform / Managed Users'
      summary: Force refresh tokens
      description: >-
        <Warning>These endpoints are deprecated and will be removed in the
        future.</Warning> If you have lost managed user access or refresh token,
        then you can get new ones by using OAuth credentials. Access token is
        valid for 60 minutes and refresh token for 1 year. Make sure to store
        them in your database, for example, in your User database model
        `calAccessToken` and `calRefreshToken` fields.

        Response also contains `accessTokenExpiresAt` and
        `refreshTokenExpiresAt` fields, but if you decode the jwt token the
        payload will contain `clientId` (OAuth client ID), `ownerId` (user to
        whom token belongs ID), `iat` (issued at time) and `expiresAt` (when
        does the token expire) fields.
      operationId: OAuthClientUsersController_forceRefresh
      parameters:
        - name: x-cal-secret-key
          in: header
          description: OAuth client secret key
          required: true
          schema:
            type: string
        - name: userId
          required: true
          in: path
          schema:
            type: number
        - name: clientId
          required: true
          in: path
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/KeysResponseDto'
components:
  schemas:
    KeysResponseDto:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          $ref: '#/components/schemas/KeysDto'
      required:
        - status
        - data
    KeysDto:
      type: object
      properties:
        accessToken:
          type: string
          example: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
        refreshToken:
          type: string
          example: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
        accessTokenExpiresAt:
          type: number
        refreshTokenExpiresAt:
          type: number
      required:
        - accessToken
        - refreshToken
        - accessTokenExpiresAt
        - refreshTokenExpiresAt

````