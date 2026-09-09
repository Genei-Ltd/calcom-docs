> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all calendars

> If accessed using an OAuth access token, the `APPS_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/calendars
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
  /v2/calendars:
    get:
      tags:
        - Calendars
      summary: Get all calendars
      description: >-
        If accessed using an OAuth access token, the `APPS_READ` scope is
        required.
      operationId: CalendarsController_getCalendars
      parameters:
        - name: Authorization
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_, managed user access token, or OAuth access token
          required: true
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ConnectedCalendarsOutput'
components:
  schemas:
    ConnectedCalendarsOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/ConnectedCalendarsData'
      required:
        - status
        - data
    ConnectedCalendarsData:
      type: object
      properties:
        connectedCalendars:
          type: array
          items:
            $ref: '#/components/schemas/ConnectedCalendar'
        destinationCalendar:
          $ref: '#/components/schemas/DestinationCalendar'
      required:
        - connectedCalendars
        - destinationCalendar
    ConnectedCalendar:
      type: object
      properties:
        integration:
          $ref: '#/components/schemas/Integration'
        credentialId:
          type: number
        delegationCredentialId:
          type: string
          nullable: true
        primary:
          $ref: '#/components/schemas/Primary'
        calendars:
          type: array
          items:
            $ref: '#/components/schemas/Calendar'
      required:
        - integration
        - credentialId
    DestinationCalendar:
      type: object
      properties:
        id:
          type: number
        integration:
          type: string
        externalId:
          type: string
        primaryEmail:
          type: string
          nullable: true
        userId:
          type: number
          nullable: true
        eventTypeId:
          type: number
          nullable: true
        credentialId:
          type: number
          nullable: true
        delegationCredentialId:
          type: string
          nullable: true
        name:
          type: string
          nullable: true
        primary:
          type: boolean
        readOnly:
          type: boolean
        email:
          type: string
        integrationTitle:
          type: string
      required:
        - id
        - integration
        - externalId
        - primaryEmail
        - userId
        - eventTypeId
        - credentialId
    Integration:
      type: object
      properties:
        appData:
          type: object
          nullable: true
        dirName:
          type: string
        __template:
          type: string
        name:
          type: string
        description:
          type: string
        installed:
          type: boolean
        type:
          type: string
        title:
          type: string
        variant:
          type: string
        category:
          type: string
        categories:
          type: array
          items:
            type: string
        logo:
          type: string
        publisher:
          type: string
        slug:
          type: string
        url:
          type: string
        email:
          type: string
        locationOption:
          nullable: true
          description: Location option for this integration
          type: object
          allOf:
            - $ref: '#/components/schemas/LocationOption'
      required:
        - name
        - description
        - type
        - variant
        - categories
        - logo
        - publisher
        - slug
        - url
        - email
        - locationOption
    Primary:
      type: object
      properties:
        externalId:
          type: string
        integration:
          type: string
        name:
          type: string
        primary:
          type: boolean
          nullable: true
        readOnly:
          type: boolean
        email:
          type: string
        isSelected:
          type: boolean
        credentialId:
          type: number
        delegationCredentialId:
          type: string
          nullable: true
      required:
        - externalId
        - primary
        - readOnly
        - isSelected
        - credentialId
    Calendar:
      type: object
      properties:
        externalId:
          type: string
          format: email
        integration:
          type: string
        name:
          type: string
          format: email
        primary:
          type: boolean
          nullable: true
        readOnly:
          type: boolean
        email:
          type: string
          format: email
        isSelected:
          type: boolean
        credentialId:
          type: number
        delegationCredentialId:
          type: string
          nullable: true
      required:
        - externalId
        - readOnly
        - isSelected
        - credentialId
    LocationOption:
      type: object
      properties:
        label:
          type: string
          description: Display label for this location option
          example: Google Meet
        value:
          type: string
          description: Location type identifier
          example: integrations:google:meet
        icon:
          type: string
          description: Icon identifier for this location option
        disabled:
          type: boolean
          description: Whether this location option is disabled
          default: false
      required:
        - label
        - value

````