> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get organization team workflow

> Required membership role: `team admin`. PBAC permission: `workflow.readTeamWorkflows`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control. If accessed using an OAuth access token, the `TEAM_WORKFLOW_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/organizations/{orgId}/teams/{teamId}/workflows/{workflowId}
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
  /v2/organizations/{orgId}/teams/{teamId}/workflows/{workflowId}:
    get:
      tags:
        - Orgs / Teams / Workflows
      summary: Get organization team workflow
      description: >-
        Required membership role: `team admin`. PBAC permission:
        `workflow.readTeamWorkflows`. Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control. If accessed using
        an OAuth access token, the `TEAM_WORKFLOW_READ` scope is required.
      operationId: OrganizationTeamWorkflowsController_getWorkflowById
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
        - name: teamId
          required: true
          in: path
          schema:
            type: number
        - name: workflowId
          required: true
          in: path
          schema:
            type: number
        - name: orgId
          required: true
          in: path
          schema:
            type: number
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetEventTypeWorkflowOutput'
components:
  schemas:
    GetEventTypeWorkflowOutput:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          description: Indicates the status of the response
          example: success
        data:
          description: workflow
          type: array
          items:
            $ref: '#/components/schemas/EventTypeWorkflowOutput'
      required:
        - status
        - data
    EventTypeWorkflowOutput:
      type: object
      properties:
        id:
          type: number
          description: Unique identifier of the workflow
          example: 101
        name:
          type: string
          description: Name of the workflow
          example: Platform Test Workflow
        userId:
          type: number
          description: ID of the user who owns the workflow (if not team-owned)
          example: 2313
        teamId:
          type: number
          description: ID of the team owning the workflow
          example: 4214321
        createdAt:
          type: string
          description: Timestamp of creation
          example: '2024-05-12T10:00:00.000Z'
          format: date-time
        updatedAt:
          type: string
          description: Timestamp of last update
          example: '2024-05-12T11:30:00.000Z'
          format: date-time
        type:
          type: string
          enum:
            - event-type
          description: type of the workflow
          example: event-type
          default: event-type
        activation:
          description: Activation settings for the workflow
          allOf:
            - $ref: '#/components/schemas/EventTypeWorkflowActivationOutputDto'
        trigger:
          description: Trigger configuration
          allOf:
            - $ref: '#/components/schemas/EventTypeWorkflowTriggerOutputDto'
        steps:
          type: array
          description: >-
            Steps comprising the workflow. A workflow with conditional paths
            contains one paths step listing its branches; steps carrying a
            pathId only run when that path's conditions match.
          items:
            oneOf:
              - $ref: '#/components/schemas/EventTypeWorkflowStepOutputDto'
                title: Step
              - $ref: '#/components/schemas/PathsWorkflowStepOutputDto'
                title: Paths step
      required:
        - id
        - name
        - type
        - activation
        - trigger
        - steps
    EventTypeWorkflowActivationOutputDto:
      type: object
      properties:
        isActiveOnAllEventTypes:
          type: boolean
          default: false
          description: >-
            Whether the workflow is active for all event types associated with
            the team/user
          example: false
        activeOnEventTypeIds:
          description: >-
            List of Event Type IDs the workflow is specifically active on (if
            not active on all)
          example:
            - 698191
            - 698192
          type: array
          items:
            type: number
    EventTypeWorkflowTriggerOutputDto:
      type: object
      properties:
        type:
          enum:
            - beforeEvent
            - eventCancelled
            - newEvent
            - afterEvent
            - rescheduleEvent
            - afterHostsCalVideoNoShow
            - afterGuestsCalVideoNoShow
            - bookingRejected
            - bookingRequested
            - bookingPaymentInitiated
            - bookingPaid
            - bookingNoShowUpdated
          type: string
          description: Trigger type for the workflow
          example: beforeEvent
        offset:
          description: Offset details (present for BEFORE_EVENT/AFTER_EVENT)
          allOf:
            - $ref: '#/components/schemas/WorkflowTriggerOffsetOutputDto'
      required:
        - type
    EventTypeWorkflowStepOutputDto:
      type: object
      properties:
        id:
          type: number
          description: Unique identifier of the step
          example: 67244
        stepNumber:
          type: number
          description: Step number in the workflow sequence
          example: 1
        recipient:
          type: string
          description: Intended recipient type
          example: const
          enum:
            - const
            - attendee
            - email
            - phone_number
        email:
          type: string
          description: Verified email address if action is EMAIL_ADDRESS
          example: notifications@example.com
        phone:
          type: string
          description: Verified Phone if action is SMS_NUMBER or WHATSAPP_NUMBER
        phoneRequired:
          type: boolean
          description: >-
            whether or not the attendees are required to provide their phone
            numbers when booking
          example: true
          default: false
        template:
          enum:
            - reminder
            - custom
            - rescheduled
            - completed
            - rating
            - cancelled
          type: string
          description: Template type used
          example: reminder
        includeCalendarEvent:
          type: boolean
          default: false
          description: Whether a calendar event (.ics) was included (for email actions)
          example: true
        skipNoShowAttendees:
          type: boolean
          default: false
          description: >-
            Whether an after-event attendee rating email skips attendees
            currently marked as no-show.
          example: false
        sender:
          type: string
          description: Displayed sender name used for this step
          example: Cal.com Notifications
        message:
          description: Message content for this step
          allOf:
            - $ref: '#/components/schemas/WorkflowMessageOutputDto'
        autoTranslateEnabled:
          type: boolean
          description: >-
            Whether auto-translation of the workflow step content for attendees
            is enabled. Only available for organizations.
          example: false
          default: false
        sourceLocale:
          nullable: true
          enum:
            - ar
            - ca
            - de
            - es
            - eu
            - he
            - id
            - ja
            - lv
            - pl
            - ro
            - sr
            - th
            - vi
            - az
            - cs
            - el
            - es-419
            - fi
            - hr
            - it
            - km
            - nl
            - pt
            - ru
            - sv
            - tr
            - zh-CN
            - bg
            - da
            - en
            - et
            - fr
            - hu
            - iw
            - ko
            - 'no'
            - pt-BR
            - sk
            - ta
            - uk
            - zh-TW
            - bn
          type: string
          description: >-
            The source locale of the workflow step content used for
            auto-translation (e.g. 'en').
          example: en
        pathId:
          type: string
          description: >-
            Id of the conditional path this step belongs to; the step only runs
            when that path's conditions match. Absent for unconditional steps.
            Read-only — paths and step-to-path membership can only be changed in
            the Cal.com app.
          example: 3f4c11a2-9b7e-4d15-8f0a-2f7de41b6c01
        action:
          enum:
            - email_host
            - email_attendee
            - email_address
            - sms_attendee
            - sms_number
            - whatsapp_attendee
            - whatsapp_number
            - cal_ai_phone_call
          type: string
          description: Action to perform
          example: email_host
      required:
        - id
        - stepNumber
        - recipient
        - template
        - sender
        - message
        - action
    PathsWorkflowStepOutputDto:
      type: object
      properties:
        id:
          type: number
          description: Unique identifier of the step
          example: 67244
        stepNumber:
          type: number
          description: Step number in the workflow sequence
          example: 1
        action:
          type: string
          enum:
            - paths
          description: >-
            The step that splits the workflow into conditional paths. Its paths
            and their conditions are read-only through the API and can only be
            edited in the Cal.com app; include this step by id when updating the
            workflow's steps.
          example: paths
        paths:
          description: The conditional paths this step splits into
          type: array
          items:
            $ref: '#/components/schemas/WorkflowStepPathOutputDto'
      required:
        - id
        - stepNumber
        - action
        - paths
    WorkflowTriggerOffsetOutputDto:
      type: object
      properties:
        value:
          type: number
          description: Time value for offset
          example: 24
        unit:
          enum:
            - hour
            - minute
            - day
          type: string
          description: Unit for the offset time
          example: hour
      required:
        - value
        - unit
    WorkflowMessageOutputDto:
      type: object
      properties:
        subject:
          type: string
          description: Subject of the message
          example: >-
            Reminder: Your Meeting {EVENT_NAME} - {EVENT_DATE_ddd, MMM D, YYYY
            h:mma} with Cal.com
        html:
          type: string
          description: HTML content of the message
          example: <p>Reminder for {EVENT_NAME}.</p>
        text:
          type: string
          description: Text content of the message (used for SMS/WhatsApp)
          example: Reminder for {EVENT_NAME}.
      required:
        - subject
    WorkflowStepPathOutputDto:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier of the path
          example: 3f4c11a2-9b7e-4d15-8f0a-2f7de41b6c01
        name:
          type: string
          description: Name of the path
          example: Enterprise leads
      required:
        - id
        - name

````