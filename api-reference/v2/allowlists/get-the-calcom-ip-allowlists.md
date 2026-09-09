> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get the Cal.com IP allowlists

> Returns the IPv4 ranges Cal.com sends traffic from and receives traffic on, keyed by service. Poll this endpoint instead of hard-coding addresses, because they can change.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/allowlists
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
  /v2/allowlists:
    get:
      tags:
        - Allowlists
      summary: Get the Cal.com IP allowlists
      description: >-
        Returns the IPv4 ranges Cal.com sends traffic from and receives traffic
        on, keyed by service. Poll this endpoint instead of hard-coding
        addresses, because they can change.
      operationId: AllowlistsController_getAllowlists
      parameters: []
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetAllowlistsOutput'
components:
  schemas:
    GetAllowlistsOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/AllowlistServicesData'
      required:
        - status
        - data
    AllowlistServicesData:
      type: object
      properties:
        metadata:
          $ref: '#/components/schemas/AllowlistMetadataOutput'
        services:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/AllowlistServiceOutput'
          description: Allowlists keyed by service name.
      required:
        - metadata
        - services
    AllowlistMetadataOutput:
      type: object
      properties:
        schemaVersion:
          type: string
          example: v1
      required:
        - schemaVersion
    AllowlistServiceOutput:
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
      required:
        - direction
        - ipv4

````