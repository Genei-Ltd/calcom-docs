> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get the Cal.com IP allowlist of one service



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/allowlists/{service}
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
  /v2/allowlists/{service}:
    get:
      tags:
        - Allowlists
      summary: Get the Cal.com IP allowlist of one service
      operationId: AllowlistsController_getAllowlist
      parameters:
        - name: service
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
                $ref: '#/components/schemas/GetAllowlistOutput'
components:
  schemas:
    GetAllowlistOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/AllowlistServiceData'
      required:
        - status
        - data
    AllowlistServiceData:
      type: object
      properties:
        metadata:
          $ref: '#/components/schemas/AllowlistMetadataOutput'
        service:
          $ref: '#/components/schemas/NamedAllowlistServiceOutput'
      required:
        - metadata
        - service
    AllowlistMetadataOutput:
      type: object
      properties:
        schemaVersion:
          type: string
          example: v1
      required:
        - schemaVersion
    NamedAllowlistServiceOutput:
      type: object
      properties:
        direction:
          enum:
            - ingress-to-cal
            - egress-from-cal
          type: string
          description: >-
            `ingress-to-cal` are the addresses your systems connect to when they
            call Cal.com. `egress-from-cal` are the addresses Cal.com connects
            to your systems from, for example when delivering a webhook.
          example: egress-from-cal
        ipv4:
          example:
            - 203.0.113.20/32
            - 203.0.113.21/32
          type: array
          items:
            type: string
        name:
          type: string
          example: webhooks
      required:
        - direction
        - ipv4
        - name

````