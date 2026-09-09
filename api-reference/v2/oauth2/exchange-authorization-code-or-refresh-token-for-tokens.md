> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Exchange authorization code or refresh token for tokens

> RFC 6749-compliant token endpoint. Pass client_id in the request body (Section 2.3.1). Use grant_type 'authorization_code' to exchange an auth code for tokens, or 'refresh_token' to refresh an access token. Accepts both application/x-www-form-urlencoded (standard per RFC 6749 Section 4.1.3) and application/json content types.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/auth/oauth2/token
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
  /v2/auth/oauth2/token:
    post:
      tags:
        - OAuth2
      summary: Exchange authorization code or refresh token for tokens
      description: >-
        RFC 6749-compliant token endpoint. Pass client_id in the request body
        (Section 2.3.1). Use grant_type 'authorization_code' to exchange an auth
        code for tokens, or 'refresh_token' to refresh an access token. Accepts
        both application/x-www-form-urlencoded (standard per RFC 6749 Section
        4.1.3) and application/json content types.
      operationId: OAuth2Controller_token
      parameters: []
      requestBody:
        required: true
        description: >-
          Token request body. client_id is required. Accepts
          application/x-www-form-urlencoded (RFC 6749 standard) or
          application/json. Use grant_type 'authorization_code' with
          client_secret (confidential) or code_verifier (public/PKCE), or
          grant_type 'refresh_token' with client_secret (confidential) or just
          the refresh_token (public).
        content:
          application/json:
            schema:
              oneOf:
                - $ref: '#/components/schemas/OAuth2ExchangeConfidentialInput'
                  title: Exchange - Confidential Client
                - $ref: '#/components/schemas/OAuth2ExchangePublicInput'
                  title: Exchange - Public Client
                - $ref: '#/components/schemas/OAuth2RefreshConfidentialInput'
                  title: Refresh - Confidential Client
                - $ref: '#/components/schemas/OAuth2RefreshPublicInput'
                  title: Refresh - Public Client
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OAuth2TokensDto'
components:
  schemas:
    OAuth2ExchangeConfidentialInput:
      type: object
      properties:
        client_id:
          type: string
          description: The client identifier
          example: my-client-id
        grant_type:
          type: string
          description: The grant type — must be 'authorization_code'
          example: authorization_code
          enum:
            - authorization_code
        code:
          type: string
          description: The authorization code received from the authorize endpoint
          example: abc123
        redirect_uri:
          type: string
          description: The redirect URI used in the authorization request
          example: https://example.com/callback
        client_secret:
          type: string
          description: The client secret for confidential clients
      required:
        - client_id
        - grant_type
        - code
        - redirect_uri
        - client_secret
    OAuth2ExchangePublicInput:
      type: object
      properties:
        client_id:
          type: string
          description: The client identifier
          example: my-client-id
        grant_type:
          type: string
          description: The grant type — must be 'authorization_code'
          example: authorization_code
          enum:
            - authorization_code
        code:
          type: string
          description: The authorization code received from the authorize endpoint
          example: abc123
        redirect_uri:
          type: string
          description: The redirect URI used in the authorization request
          example: https://example.com/callback
        code_verifier:
          type: string
          description: >-
            PKCE code verifier (required for public clients that used
            code_challenge)
      required:
        - client_id
        - grant_type
        - code
        - redirect_uri
        - code_verifier
    OAuth2RefreshConfidentialInput:
      type: object
      properties:
        client_id:
          type: string
          description: The client identifier
          example: my-client-id
        grant_type:
          type: string
          description: The grant type — must be 'refresh_token'
          example: refresh_token
          enum:
            - refresh_token
        refresh_token:
          type: string
          description: The refresh token
          example: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
        client_secret:
          type: string
          description: The client secret for confidential clients
      required:
        - client_id
        - grant_type
        - refresh_token
        - client_secret
    OAuth2RefreshPublicInput:
      type: object
      properties:
        client_id:
          type: string
          description: The client identifier
          example: my-client-id
        grant_type:
          type: string
          description: The grant type — must be 'refresh_token'
          example: refresh_token
          enum:
            - refresh_token
        refresh_token:
          type: string
          description: The refresh token
          example: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
      required:
        - client_id
        - grant_type
        - refresh_token
    OAuth2TokensDto:
      type: object
      properties:
        access_token:
          type: string
          description: The access token
          example: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
        token_type:
          type: string
          description: The token type
          example: bearer
        refresh_token:
          type: string
          description: The refresh token
          example: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
        expires_in:
          type: number
          description: The number of seconds until the access token expires
          example: 1800
        scope:
          type: string
          description: The granted scopes (space-delimited per RFC 6749)
          example: BOOKING_READ BOOKING_WRITE
      required:
        - access_token
        - token_type
        - refresh_token
        - expires_in
        - scope

````