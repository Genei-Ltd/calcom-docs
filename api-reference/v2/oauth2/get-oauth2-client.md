> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get OAuth2 client

> Returns the OAuth2 client information for the given client ID



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/auth/oauth2/clients/{clientId}
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
  /v2/auth/oauth2/clients/{clientId}:
    get:
      tags:
        - OAuth2
      summary: Get OAuth2 client
      description: Returns the OAuth2 client information for the given client ID
      operationId: OAuth2Controller_getClient
      parameters:
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
                $ref: '#/components/schemas/OAuth2ClientResponseDto'
components:
  schemas:
    OAuth2ClientResponseDto:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/OAuth2ClientDto'
      required:
        - status
        - data
    OAuth2ClientDto:
      type: object
      properties:
        client_id:
          type: string
          description: The OAuth client ID
          example: clxxxxxxxxxxxxxxxx
        redirect_uris:
          description: The redirect URIs for the OAuth client
          example:
            - https://example.com/callback
          type: array
          items:
            type: string
        name:
          type: string
          description: The name of the OAuth client
          example: My App
        logo:
          type: string
          nullable: true
          description: The logo URL of the OAuth client
        is_trusted:
          type: boolean
          description: Whether the OAuth client is trusted
          example: false
        client_type:
          enum:
            - CONFIDENTIAL
            - PUBLIC
          type: string
          description: The type of OAuth client (CONFIDENTIAL or PUBLIC)
          example: CONFIDENTIAL
      required:
        - client_id
        - redirect_uris
        - name
        - is_trusted
        - client_type

````