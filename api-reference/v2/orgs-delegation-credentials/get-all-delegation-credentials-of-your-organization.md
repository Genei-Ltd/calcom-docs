> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all delegation credentials of your organization

> Required membership role: `org admin`. PBAC permission: `organization.read`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/organizations/{orgId}/delegation-credentials
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
  /v2/organizations/{orgId}/delegation-credentials:
    get:
      tags:
        - Orgs / Delegation Credentials
      summary: Get all delegation credentials of your organization
      description: >-
        Required membership role: `org admin`. PBAC permission:
        `organization.read`. Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control
      operationId: OrganizationsDelegationCredentialController_getDelegationCredentials
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
            The unique identifier of the organization whose delegation
            credentials are returned
          schema:
            type: number
            example: 123
        - name: take
          required: false
          in: query
          description: Maximum number of items to return
          schema:
            minimum: 1
            maximum: 250
            default: 250
            example: 25
            type: number
        - name: skip
          required: false
          in: query
          description: Number of items to skip
          schema:
            minimum: 0
            default: 0
            example: 0
            type: number
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetDelegationCredentialsOutput'
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
                    example: /v2/organizations/123/delegation-credentials
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
            `organization.read` permission, or the organization is not on the
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
                    example: /v2/organizations/123/delegation-credentials
                  error:
                    type: object
                    properties:
                      code:
                        type: string
                        example: ForbiddenException
                      message:
                        type: string
components:
  schemas:
    GetDelegationCredentialsOutput:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
          description: The status of the request, either `success` or `error`
        data:
          type: array
          items:
            oneOf:
              - $ref: >-
                  #/components/schemas/GoogleDelegationCredentialWithClientIdOutput
              - $ref: >-
                  #/components/schemas/MicrosoftDelegationCredentialWithClientIdOutput
              - $ref: '#/components/schemas/DelegationCredentialWithClientIdOutput'
          description: The list of delegation credentials belonging to the organization
      required:
        - status
        - data
    GoogleDelegationCredentialWithClientIdOutput:
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
        serviceAccountClientId:
          type: string
          nullable: true
          description: >-
            The client id of the service account associated with the delegation
            credential. The service account's private key is never returned.
          example: '1234567890'
      required:
        - id
        - enabled
        - domain
        - organizationId
        - workspacePlatform
        - createdAt
        - updatedAt
        - serviceAccountClientId
    MicrosoftDelegationCredentialWithClientIdOutput:
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
        serviceAccountClientId:
          type: string
          nullable: true
          description: >-
            The client id of the service account associated with the delegation
            credential. The service account's private key is never returned.
          example: '1234567890'
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
        - serviceAccountClientId
    DelegationCredentialWithClientIdOutput:
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
        serviceAccountClientId:
          type: string
          nullable: true
          description: >-
            The client id of the service account associated with the delegation
            credential. The service account's private key is never returned.
          example: '1234567890'
      required:
        - id
        - enabled
        - domain
        - organizationId
        - workspacePlatform
        - createdAt
        - updatedAt
        - serviceAccountClientId
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