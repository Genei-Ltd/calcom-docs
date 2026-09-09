> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Check if email verification is required

> Checks whether email verification is required for the given email. Returns true if verification is needed.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/bookings/verification/email/check
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
  /v2/bookings/verification/email/check:
    get:
      tags:
        - Bookings - Email Verification
      summary: Check if email verification is required
      description: >-
        Checks whether email verification is required for the given email.
        Returns true if verification is needed.
      operationId: BookingsVerificationController_checkEmailVerificationRequired
      parameters:
        - name: email
          required: true
          in: query
          schema:
            example: user@example.com
            type: string
        - name: userSessionEmail
          required: false
          in: query
          schema:
            example: user@example.com
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object

````