> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete your workflow

> Delete an event-type workflow owned by the authenticated user. Not available to third-party OAuth access tokens.



## OpenAPI

````yaml /api-reference/v2/openapi.json delete /v2/workflows/{workflowId}
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
  /v2/workflows/{workflowId}:
    delete:
      tags:
        - Workflows
      summary: Delete your workflow
      description: >-
        Delete an event-type workflow owned by the authenticated user. Not
        available to third-party OAuth access tokens.
      operationId: UserWorkflowsController_deleteWorkflow
      parameters:
        - name: Authorization
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_, managed user access token, or OAuth access token
          required: true
          schema:
            type: string
        - name: workflowId
          required: true
          in: path
          schema:
            type: number
      responses:
        '200':
          description: ''

````