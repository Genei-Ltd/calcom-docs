> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Reset a blocked delegation credential's secret rotation state

> Clears the terminal secret-rotation failure state so managed secret rotation resumes normally. Use this after fixing whatever external configuration issues caused rotation to reach a terminal state. Required membership role: `org admin`. PBAC permission: `organization.update`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/organizations/{orgId}/delegation-credentials/{credentialId}/reset-rotation
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
  /v2/organizations/{orgId}/delegation-credentials/{credentialId}/reset-rotation:
    post:
      tags:
        - Orgs / Delegation Credentials
      summary: Reset a blocked delegation credential's secret rotation state
      description: >-
        Clears the terminal secret-rotation failure state so managed secret
        rotation resumes normally. Use this after fixing whatever external
        configuration issues caused rotation to reach a terminal state. Required
        membership role: `org admin`. PBAC permission: `organization.update`.
        Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control
      operationId: >-
        OrganizationsDelegationCredentialController_resetDelegationCredentialRotation
      parameters:
        - name: Authorization
          in: header
          description: >-
            For non-platform customers - value must be `Bearer <token>` where
            `<token>` is api key prefixed with cal_
          required: false
          schema:
            type: string
        - name: x-cal-secret-key
          in: header
          description: For platform customers - OAuth client secret key
          required: false
          schema:
            type: string
        - name: x-cal-client-id
          in: header
          description: For platform customers - OAuth client ID
          required: false
          schema:
            type: string
        - name: orgId
          required: true
          in: path
          description: >-
            The unique identifier of the organization the delegation credential
            belongs to
          schema:
            type: number
            example: 123
        - name: credentialId
          required: true
          in: path
          description: The unique identifier of the delegation credential
          schema:
            example: clsx1234567890
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResetDelegationCredentialRotationOutput'
        '400':
          description: >-
            The delegation credential is not a Microsoft/office365 delegation
            credential
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                    example: error
                  timestamp:
                    type: string
                    example: '2024-04-01T00:00:00.000Z'
                  path:
                    type: string
                    example: >-
                      /v2/organizations/123/delegation-credentials/clsx1234567890/reset-rotation
                  error:
                    type: object
                    properties:
                      code:
                        type: string
                        example: BadRequestException
                      message:
                        type: string
        '401':
          description: Authentication is missing or invalid
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                    example: error
                  timestamp:
                    type: string
                    example: '2024-04-01T00:00:00.000Z'
                  path:
                    type: string
                    example: >-
                      /v2/organizations/123/delegation-credentials/clsx1234567890/reset-rotation
                  error:
                    type: object
                    properties:
                      code:
                        type: string
                        example: UnauthorizedException
                      message:
                        type: string
        '403':
          description: >-
            The authenticated user is not an org admin, lacks the
            `organization.update` permission, or the organization is not on the
            required plan
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                    example: error
                  timestamp:
                    type: string
                    example: '2024-04-01T00:00:00.000Z'
                  path:
                    type: string
                    example: >-
                      /v2/organizations/123/delegation-credentials/clsx1234567890/reset-rotation
                  error:
                    type: object
                    properties:
                      code:
                        type: string
                        example: ForbiddenException
                      message:
                        type: string
        '404':
          description: >-
            No delegation credential with the given id exists in the
            organization, or it belongs to a different organization
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                    example: error
                  timestamp:
                    type: string
                    example: '2024-04-01T00:00:00.000Z'
                  path:
                    type: string
                    example: >-
                      /v2/organizations/123/delegation-credentials/clsx1234567890/reset-rotation
                  error:
                    type: object
                    properties:
                      code:
                        type: string
                        example: NotFoundException
                      message:
                        type: string
components:
  schemas:
    ResetDelegationCredentialRotationOutput:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          oneOf:
            - $ref: '#/components/schemas/MicrosoftDelegationCredentialOutput'
          allOf:
            - $ref: '#/components/schemas/MicrosoftDelegationCredentialOutput'
      required:
        - status
        - data
    MicrosoftDelegationCredentialOutput:
      type: object
      properties:
        id:
          type: string
          description: The unique identifier of the delegation credential
          example: clsx1234567890
        enabled:
          type: boolean
          description: Whether the delegation credential is currently enabled
          example: true
        domain:
          type: string
          description: The email domain the delegation credential applies to
          example: example.com
        organizationId:
          type: number
          description: >-
            The unique identifier of the organization the delegation credential
            belongs to
          example: 123
        workspacePlatform:
          $ref: '#/components/schemas/WorkspacePlatformDto'
        createdAt:
          format: date-time
          type: string
          description: The date and time when the delegation credential was created
          example: '2024-04-01T00:00:00.000Z'
        updatedAt:
          format: date-time
          type: string
          description: The date and time when the delegation credential was last updated
          example: '2024-04-01T00:00:00.000Z'
        optOutAutoSecretRotation:
          type: boolean
          description: >-
            Whether Cal.com-managed Microsoft 365 client secret rotation is
            disabled for this delegation credential.
        secretRotationBlocked:
          type: boolean
          description: >-
            Whether managed secret rotation is blocked after repeated failures
            and requires the reset-rotation endpoint before it will resume.
      required:
        - id
        - enabled
        - domain
        - organizationId
        - workspacePlatform
        - createdAt
        - updatedAt
        - optOutAutoSecretRotation
        - secretRotationBlocked
    WorkspacePlatformDto:
      type: object
      properties:
        name:
          type: string
          description: >-
            The name of the workspace platform the delegation credential is
            configured for
          example: Google
        slug:
          type: string
          description: >-
            The slug of the workspace platform the delegation credential is
            configured for
          example: google
      required:
        - name
        - slug

````