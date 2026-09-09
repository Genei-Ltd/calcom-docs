> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Conferencing app OAuth callback



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/conferencing/{app}/oauth/callback
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
  /v2/conferencing/{app}/oauth/callback:
    get:
      tags:
        - Conferencing
      summary: Conferencing app OAuth callback
      operationId: ConferencingController_save
      parameters:
        - name: state
          required: true
          in: query
          schema:
            type: string
        - name: app
          required: true
          in: path
          description: Conferencing application type
          schema:
            enum:
              - zoom
              - msteams
            type: string
        - name: code
          required: true
          in: query
          schema:
            type: string
      responses:
        '200':
          description: ''

````