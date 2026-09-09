> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Save delegation credentials for your organization

> Required membership role: `org admin`. PBAC permission: `organization.update`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/organizations/{orgId}/delegation-credentials
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
    post:
      tags:
        - Orgs / Delegation Credentials
      summary: Save delegation credentials for your organization
      description: >-
        Required membership role: `org admin`. PBAC permission:
        `organization.update`. Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control
      operationId: OrganizationsDelegationCredentialController_createDelegationCredential
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
          schema:
            type: number
      requestBody:
        required: true
        content:
          application/json:
            schema:
              anyOf:
                - $ref: '#/components/schemas/CreateGoogleDelegationCredentialInput'
                - $ref: >-
                    #/components/schemas/CreateMicrosoftDelegationCredentialInput
      responses:
        '201':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateDelegationCredentialOutput'
components:
  schemas:
    CreateGoogleDelegationCredentialInput:
      type: object
      properties:
        domain:
          type: string
        workspacePlatformSlug:
          type: string
          enum:
            - google
        serviceAccountKey:
          $ref: '#/components/schemas/GoogleServiceAccountKeyInput'
      required:
        - domain
        - workspacePlatformSlug
        - serviceAccountKey
    CreateMicrosoftDelegationCredentialInput:
      type: object
      properties:
        domain:
          type: string
        workspacePlatformSlug:
          type: string
          enum:
            - office365
        serviceAccountKey:
          $ref: '#/components/schemas/MicrosoftServiceAccountKeyInput'
        optOutAutoSecretRotation:
          type: boolean
          description: >-
            When true, Cal.com will not mint or promote managed Microsoft 365
            client secrets for this delegation credential. Use this when the
            credential owner wants to rotate the active secret outside Cal.com.
      required:
        - domain
        - workspacePlatformSlug
        - serviceAccountKey
    CreateDelegationCredentialOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          oneOf:
            - $ref: '#/components/schemas/GoogleDelegationCredentialOutput'
              title: Google Service Account
            - $ref: '#/components/schemas/MicrosoftDelegationCredentialOutput'
              title: Microsoft Service Account
      required:
        - status
        - data
    GoogleServiceAccountKeyInput:
      type: object
      properties:
        private_key:
          type: string
        client_email:
          type: string
        client_id:
          type: string
      required:
        - private_key
        - client_email
        - client_id
    MicrosoftServiceAccountKeyInput:
      type: object
      properties:
        private_key:
          type: string
        tenant_id:
          type: string
        client_id:
          type: string
      required:
        - private_key
        - tenant_id
        - client_id
    GoogleDelegationCredentialOutput:
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
      required:
        - id
        - enabled
        - domain
        - organizationId
        - workspacePlatform
        - createdAt
        - updatedAt
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
        secret:
          description: >-
            State of the current active managed secret. `expiresAt` is null if
            not yet known.
          allOf:
            - $ref: '#/components/schemas/SecretDto'
        pendingSecret:
          description: >-
            State of a replacement secret minted and pending
            validation/promotion. `createdAt` and `expiresAt` are null when
            there is no pending secret in flight.
          allOf:
            - $ref: '#/components/schemas/PendingSecretDto'
        secretRotationErrorCode:
          nullable: true
          enum:
            - missing_permission
            - tenant_lifetime_policy
            - transient
            - unknown
            - pending_secret_mint_failed
            - pending_secret_promotion_failed
          type: string
          description: >-
            Why the most recent secret rotation attempt failed, or which stage
            terminally failed, or null if rotation has not failed. This enum is
            open — new values may be added over time, so treat any value you
            don't recognize as `unknown`. See the Cal.com docs' 'Microsoft 365
            (Azure) Secret Auto-Rotation' section for per-code remediation
            guidance.
          example: missing_permission
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
        - secret
        - pendingSecret
        - secretRotationErrorCode
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
    SecretDto:
      type: object
      properties:
        expiresAt:
          format: date-time
          type: string
          nullable: true
          description: >-
            The date and time the current active managed secret expires. Null if
            not yet known.
          example: '2024-10-01T00:00:00.000Z'
      required:
        - expiresAt
    PendingSecretDto:
      type: object
      properties:
        createdAt:
          format: date-time
          type: string
          nullable: true
          description: >-
            The date and time a replacement secret was minted and is pending
            validation/promotion. Null when there is no pending secret in
            flight.
          example: '2024-10-01T00:00:00.000Z'
        expiresAt:
          format: date-time
          type: string
          nullable: true
          description: >-
            The date and time the pending (not-yet-active) managed secret
            expires. Null when there is no pending secret in flight.
          example: '2024-10-01T00:00:00.000Z'
      required:
        - createdAt
        - expiresAt

````