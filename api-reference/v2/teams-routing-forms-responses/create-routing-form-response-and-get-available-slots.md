> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create routing form response and get available slots

> Only available for teams that are not part of an organization - for a team within an organization use the organization team endpoint instead. Required membership role: `team member`. PBAC permission: `routingForm.create`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control. If accessed using an OAuth access token, the `TEAM_ROUTING_FORM_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/teams/{teamId}/routing-forms/{routingFormId}/responses
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
  /v2/teams/{teamId}/routing-forms/{routingFormId}/responses:
    post:
      tags:
        - Teams / Routing forms / Responses
      summary: Create routing form response and get available slots
      description: >-
        Only available for teams that are not part of an organization - for a
        team within an organization use the organization team endpoint instead.
        Required membership role: `team member`. PBAC permission:
        `routingForm.create`. Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control. If accessed using
        an OAuth access token, the `TEAM_ROUTING_FORM_WRITE` scope is required.
      operationId: TeamsRoutingFormsResponsesController_createRoutingFormResponse
      parameters:
        - name: Authorization
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_
          required: true
          schema:
            type: string
        - name: routingFormId
          required: true
          in: path
          schema:
            type: string
        - name: start
          required: true
          in: query
          description: |2-

                  Time starting from which available slots should be checked.
                
                  Must be in UTC timezone as ISO 8601 datestring.
                  
                  You can pass date without hours which defaults to start of day or specify hours:
                  2024-08-13 (will have hours 00:00:00 aka at very beginning of the date) or you can specify hours manually like 2024-08-13T09:00:00Z
                  
          schema:
            example: '2050-09-05'
            type: string
        - name: end
          required: true
          in: query
          description: |2-

                  Time until which available slots should be checked.
                  
                  Must be in UTC timezone as ISO 8601 datestring.
                  
                  You can pass date without hours which defaults to end of day or specify hours:
                  2024-08-20 (will have hours 23:59:59 aka at the very end of the date) or you can specify hours manually like 2024-08-20T18:00:00Z
          schema:
            example: '2050-09-06'
            type: string
        - name: timeZone
          required: false
          in: query
          description: >-
            Time zone in which the available slots should be returned. Defaults
            to UTC.
          schema:
            type: string
            example: Europe/Rome
        - name: duration
          required: false
          in: query
          description: >-
            If event type has multiple possible durations then you can specify
            the desired duration here. Also, if you are fetching slots for a
            dynamic event then you can specify the duration her which defaults
            to 30, meaning that returned slots will be each 30 minutes long.
          schema:
            example: '60'
            type: number
        - name: format
          required: false
          in: query
          description: >-
            Format of slot times in response. Use 'range' to get start and end
            times.
          schema:
            example: range
            type: string
            enum:
              - range
              - time
        - name: bookingUidToReschedule
          required: false
          in: query
          description: >-
            The unique identifier of the booking being rescheduled. When
            provided will ensure that the original booking time appears within
            the returned available slots when rescheduling.
          schema:
            type: string
            example: abc123def456
        - name: rescheduleWithSameHost
          required: false
          in: query
          description: >-
            Only for round robin event types that allow the person rescheduling
            to choose the host. True returns slots of the original host, false
            returns slots of any available host. Ignored for other event types.
          schema:
            type: boolean
            example: true
        - name: queueResponse
          required: false
          in: query
          description: Whether to queue the form response.
          schema:
            type: boolean
            example: true
        - name: teamId
          required: true
          in: path
          schema:
            type: number
      responses:
        '201':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateRoutingFormResponseOutput'
components:
  schemas:
    CreateRoutingFormResponseOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/CreateRoutingFormResponseOutputData'
      required:
        - status
        - data
    CreateRoutingFormResponseOutputData:
      type: object
      properties:
        eventTypeId:
          type: number
          description: The ID of the event type that was routed to.
          example: 123
        routing:
          description: >-
            The routing information that could be passed as is to the booking
            API.
          example:
            eventTypeId: 123
            routing:
              teamMemberIds:
                - 101
                - 102
              teamMemberEmail: john.doe@example.com
              skipContactOwner: true
              crmRecordOwnerFallbackTeamMemberIds:
                - 103
                - 104
              crmRecordOwnerFallbackMode: attributeRules
          allOf:
            - $ref: '#/components/schemas/Routing'
        routingCustomMessage:
          type: string
          description: >-
            A custom message to be displayed to the user in case of routing to a
            custom page.
          example: This is a custom message.
        routingExternalRedirectUrl:
          type: string
          description: >-
            The external redirect URL to be used in case of routing to a non
            cal.com event type URL.
          example: https://example.com/
        slots:
          additionalProperties: true
          oneOf:
            - $ref: '#/components/schemas/SlotsOutput_2024_09_04'
              title: Time Slots
            - $ref: '#/components/schemas/RangeSlotsOutput_2024_09_04'
              title: Slot Ranges
    Routing:
      type: object
      properties:
        queuedResponseId:
          type: string
          nullable: true
          description: >-
            The ID of the queued form response. Only present if the form
            response was queued.
          example: '123'
        responseId:
          type: number
          nullable: true
          description: The ID of the routing form response.
          example: 123
        teamMemberIds:
          description: Array of team member IDs that were routed to handle this booking.
          example:
            - 101
            - 102
          type: array
          items:
            type: number
        teamMemberEmail:
          type: string
          description: The email of the team member assigned to handle this booking.
          example: john.doe@example.com
        skipContactOwner:
          type: boolean
          description: Whether to skip contact owner assignment from CRM integration.
          example: true
        crmAppSlug:
          type: string
          description: The CRM application slug for integration.
          example: salesforce
        crmOwnerRecordType:
          type: string
          description: The CRM owner record type for contact assignment.
          example: Account
        crmRecordOwnerFallbackTeamMemberIds:
          description: >-
            Eligible CRM owner fallback team member IDs to pass to the booking
            API.
          example:
            - 103
            - 104
          type: array
          items:
            type: number
        crmRecordOwnerFallbackMode:
          enum:
            - relationship
            - attributeRules
          type: string
          description: The CRM owner fallback strategy used for this routing result.
          example: relationship
      required:
        - teamMemberIds
    SlotsOutput_2024_09_04:
      type: object
      properties: {}
    RangeSlotsOutput_2024_09_04:
      type: object
      properties: {}

````