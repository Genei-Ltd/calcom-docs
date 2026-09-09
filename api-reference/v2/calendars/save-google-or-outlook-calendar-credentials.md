> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Save Google or Outlook calendar credentials



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/calendars/{calendar}/save
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
  /v2/calendars/{calendar}/save:
    get:
      tags:
        - Calendars
      summary: Save Google or Outlook calendar credentials
      operationId: CalendarsController_save
      parameters:
        - name: state
          required: true
          in: query
          schema:
            type: string
        - name: code
          required: true
          in: query
          schema:
            type: string
        - name: calendar
          required: true
          in: path
          schema:
            enum:
              - office365
              - google
            type: string
      responses:
        '200':
          description: ''

````