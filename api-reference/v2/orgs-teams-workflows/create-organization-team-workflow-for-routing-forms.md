> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create organization team workflow for routing-forms

> Required membership role: `team admin`. PBAC permission: `workflow.create`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control. If accessed using an OAuth access token, the `TEAM_WORKFLOW_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/organizations/{orgId}/teams/{teamId}/workflows/routing-form
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
  /v2/organizations/{orgId}/teams/{teamId}/workflows/routing-form:
    post:
      tags:
        - Orgs / Teams / Workflows
      summary: Create organization team workflow for routing-forms
      description: >-
        Required membership role: `team admin`. PBAC permission:
        `workflow.create`. Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control. If accessed using
        an OAuth access token, the `TEAM_WORKFLOW_WRITE` scope is required.
      operationId: OrganizationTeamWorkflowsController_createFormWorkflow
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
              $ref: '#/components/schemas/CreateFormWorkflowDto'
      responses:
        '201':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetRoutingFormWorkflowOutput'
components:
  schemas:
    CreateFormWorkflowDto:
      type: object
      properties:
        name:
          type: string
          description: Name of the workflow
          example: Platform Test Workflow
        activation:
          description: Activation settings for the workflow
          allOf:
            - $ref: '#/components/schemas/WorkflowFormActivationDto'
        trigger:
          description: >-
            Trigger configuration for the routing-form workflow, allowed
            triggers are formSubmitted,formSubmittedNoEvent
          oneOf:
            - $ref: '#/components/schemas/OnFormSubmittedTriggerDto'
              title: Form Submitted
            - $ref: '#/components/schemas/OnFormSubmittedNoEventTriggerDto'
              title: Form Submitted Without Event
        steps:
          type: array
          description: >-
            Steps to execute as part of the routing-form workflow, allowed steps
            are email_attendee,email_address,sms_attendee,sms_number
          items:
            oneOf:
              - $ref: '#/components/schemas/WorkflowEmailAddressStepDto'
                title: Email Address
              - $ref: '#/components/schemas/WorkflowEmailAttendeeStepDto'
                title: Email Attendee
              - $ref: '#/components/schemas/WorkflowPhoneAttendeeStepDto'
                title: SMS Attendee
              - $ref: '#/components/schemas/WorkflowPhoneNumberStepDto'
                title: SMS Number
      required:
        - name
        - activation
        - trigger
        - steps
    GetRoutingFormWorkflowOutput:
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
            $ref: '#/components/schemas/RoutingFormWorkflowOutput'
      required:
        - status
        - data
    WorkflowFormActivationDto:
      type: object
      properties:
        isActiveOnAllRoutingForms:
          type: boolean
          description: Whether the workflow is active for all the routing forms
          example: false
        activeOnRoutingFormIds:
          description: List of routing form IDs the workflow applies to
          example:
            - abd1-123edf-a213d-123dfwf
          type: array
          items:
            type: number
      required:
        - isActiveOnAllRoutingForms
    OnFormSubmittedTriggerDto:
      type: object
      properties:
        type:
          type: string
          default: formSubmitted
          enum:
            - formSubmitted
          description: Trigger type for the workflow
          example: formSubmitted
      required:
        - type
    OnFormSubmittedNoEventTriggerDto:
      type: object
      properties:
        offset:
          description: >-
            Offset before/after the trigger time; required for BEFORE_EVENT,
            AFTER_EVENT, and FORM_SUBMITTED_NO_EVENT
          allOf:
            - $ref: '#/components/schemas/WorkflowTriggerOffsetDto'
        type:
          type: string
          default: formSubmittedNoEvent
          enum:
            - formSubmittedNoEvent
          description: Trigger type for the workflow
          example: formSubmittedNoEvent
      required:
        - offset
        - type
    WorkflowEmailAddressStepDto:
      type: object
      properties:
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
          default: email_address
          description: Action to perform, send an email to a specific email address
          example: email_address
        stepNumber:
          type: number
          description: Step number in the workflow sequence
          example: 1
        recipient:
          type: string
          description: Recipient type
          example: attendee
          enum:
            - const
            - attendee
            - email
            - phone_number
        template:
          enum:
            - reminder
            - custom
            - rescheduled
            - completed
            - rating
            - cancelled
          type: string
          description: >-
            Template type for the step. Case-insensitive: uppercase values (e.g.
            `REMINDER`) are normalized to lowercase server-side for backwards
            compat.
          example: reminder
        sender:
          type: string
          description: Displayed sender name.
        autoTranslateEnabled:
          type: boolean
          description: >-
            Whether to enable auto-translation of the workflow step content for
            attendees. Only available for organizations.
          example: false
          default: false
        sourceLocale:
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
            auto-translation (e.g. 'en'). Defaults to the user's locale.
          example: en
        verifiedEmailId:
          type: number
          description: >-
            Email address if recipient is EMAIL, required for action
            EMAIL_ADDRESS
          example: 31214
          externalDocs:
            url: >-
              https://cal.com/docs/api-reference/v2/organization-team-verified-resources/verify-an-email-for-an-org-team
        includeCalendarEvent:
          type: boolean
          default: false
          description: >-
            Whether to include a calendar event in the notification, can be
            included with actions email_host, email_attendee, email_address
          example: true
        message:
          description: Message content for this step
          allOf:
            - $ref: '#/components/schemas/HtmlWorkflowMessageDto'
      required:
        - action
        - stepNumber
        - recipient
        - template
        - sender
        - verifiedEmailId
        - includeCalendarEvent
        - message
    WorkflowEmailAttendeeStepDto:
      type: object
      properties:
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
          default: email_attendee
          description: Action to perform, send an email to the attendees of the event
          example: email_attendee
        stepNumber:
          type: number
          description: Step number in the workflow sequence
          example: 1
        recipient:
          type: string
          description: Recipient type
          example: attendee
          enum:
            - const
            - attendee
            - email
            - phone_number
        template:
          enum:
            - reminder
            - custom
            - rescheduled
            - completed
            - rating
            - cancelled
          type: string
          description: >-
            Template type for the step. Case-insensitive: uppercase values (e.g.
            `REMINDER`) are normalized to lowercase server-side for backwards
            compat.
          example: reminder
        sender:
          type: string
          description: Displayed sender name.
        autoTranslateEnabled:
          type: boolean
          description: >-
            Whether to enable auto-translation of the workflow step content for
            attendees. Only available for organizations.
          example: false
          default: false
        sourceLocale:
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
            auto-translation (e.g. 'en'). Defaults to the user's locale.
          example: en
        includeCalendarEvent:
          type: boolean
          default: false
          description: >-
            Whether to include a calendar event in the notification, can be
            included with actions email_host, email_attendee, email_address
          example: true
        skipNoShowAttendees:
          type: boolean
          default: false
          description: >-
            Whether an after-event rating email should skip attendees currently
            marked as no-show. It has no effect for other workflow triggers or
            templates.
          example: false
        message:
          description: Message content for this step
          allOf:
            - $ref: '#/components/schemas/HtmlWorkflowMessageDto'
      required:
        - action
        - stepNumber
        - recipient
        - template
        - sender
        - includeCalendarEvent
        - message
    WorkflowPhoneAttendeeStepDto:
      type: object
      properties:
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
          default: sms_attendee
          description: >-
            Action to perform, send a text message to the phone numbers of the
            attendees
          example: sms_attendee
        stepNumber:
          type: number
          description: Step number in the workflow sequence
          example: 1
        recipient:
          type: string
          description: Recipient type
          example: attendee
          enum:
            - const
            - attendee
            - email
            - phone_number
        template:
          enum:
            - reminder
            - custom
            - rescheduled
            - completed
            - rating
            - cancelled
          type: string
          description: >-
            Template type for the step. Case-insensitive: uppercase values (e.g.
            `REMINDER`) are normalized to lowercase server-side for backwards
            compat.
          example: reminder
        sender:
          type: string
          description: Displayed sender name.
        autoTranslateEnabled:
          type: boolean
          description: >-
            Whether to enable auto-translation of the workflow step content for
            attendees. Only available for organizations.
          example: false
          default: false
        sourceLocale:
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
            auto-translation (e.g. 'en'). Defaults to the user's locale.
          example: en
        message:
          description: Message content for this step
          allOf:
            - $ref: '#/components/schemas/TextWorkflowMessageDto'
        phoneRequired:
          type: boolean
          description: >-
            whether or not the attendees are required to provide their phone
            numbers when booking
          example: true
          default: false
      required:
        - action
        - stepNumber
        - recipient
        - template
        - sender
        - message
    WorkflowPhoneNumberStepDto:
      type: object
      properties:
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
          default: sms_number
          description: Action to perform, send a text message to a specific phone number
          example: sms_number
        stepNumber:
          type: number
          description: Step number in the workflow sequence
          example: 1
        recipient:
          type: string
          description: Recipient type
          example: attendee
          enum:
            - const
            - attendee
            - email
            - phone_number
        template:
          enum:
            - reminder
            - custom
            - rescheduled
            - completed
            - rating
            - cancelled
          type: string
          description: >-
            Template type for the step. Case-insensitive: uppercase values (e.g.
            `REMINDER`) are normalized to lowercase server-side for backwards
            compat.
          example: reminder
        sender:
          type: string
          description: Displayed sender name.
        autoTranslateEnabled:
          type: boolean
          description: >-
            Whether to enable auto-translation of the workflow step content for
            attendees. Only available for organizations.
          example: false
          default: false
        sourceLocale:
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
            auto-translation (e.g. 'en'). Defaults to the user's locale.
          example: en
        verifiedPhoneId:
          type: number
          description: >-
            Phone number if recipient is PHONE_NUMBER, required for actions
            SMS_NUMBER and WHATSAPP_NUMBER
          example: 3243434
          externalDocs:
            url: >-
              https://cal.com/docs/api-reference/v2/organization-team-verified-resources/verify-a-phone-number-for-an-org-team
        message:
          description: Message content for this step
          allOf:
            - $ref: '#/components/schemas/TextWorkflowMessageDto'
      required:
        - action
        - stepNumber
        - recipient
        - template
        - sender
        - verifiedPhoneId
        - message
    RoutingFormWorkflowOutput:
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
            - routing-form
          description: type of the workflow
          example: routing-form
          default: routing-form
        activation:
          description: Activation settings for the workflow
          allOf:
            - $ref: '#/components/schemas/RoutingFormWorkflowActivationOutputDto'
        trigger:
          description: Trigger configuration
          allOf:
            - $ref: '#/components/schemas/RoutingFormWorkflowTriggerOutputDto'
        steps:
          type: array
          description: >-
            Steps comprising the workflow. A workflow with conditional paths
            contains one paths step listing its branches; steps carrying a
            pathId only run when that path's conditions match.
          items:
            oneOf:
              - $ref: '#/components/schemas/RoutingFormWorkflowStepOutputDto'
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
    WorkflowTriggerOffsetDto:
      type: object
      properties:
        value:
          type: number
          minimum: 1
          description: Time value for offset before/after event trigger
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
    HtmlWorkflowMessageDto:
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
          description: HTML content of the message (used for Emails)
          example: >-
            <p>This is a reminder from {ORGANIZER} of {EVENT_NAME} to {ATTENDEE}
            starting here  {LOCATION} {MEETING_URL} at {START_TIME_h:mma}
            {TIMEZONE}.</p>
      required:
        - subject
        - html
    TextWorkflowMessageDto:
      type: object
      properties:
        subject:
          type: string
          description: Subject of the message
          example: >-
            Reminder: Your Meeting {EVENT_NAME} - {EVENT_DATE_ddd, MMM D, YYYY
            h:mma} with Cal.com
        text:
          type: string
          description: Text content of the message (used for SMS)
          example: >-
            This is a reminder message from {ORGANIZER} of {EVENT_NAME} to
            {ATTENDEE} starting here {LOCATION} {MEETING_URL} at
            {START_TIME_h:mma} {TIMEZONE}.
      required:
        - subject
        - text
    RoutingFormWorkflowActivationOutputDto:
      type: object
      properties:
        isActiveOnAllRoutingForms:
          type: boolean
          default: false
          description: >-
            Whether the workflow is active for all routing forms associated with
            the team/user
          example: false
        activeOnRoutingFormIds:
          description: >-
            List of Event Type IDs the workflow is specifically active on (if
            not active on all)
          example:
            - 5cacdec7-1234-6e1b-78d9-7bcda8a1b332
          type: array
          items:
            type: string
    RoutingFormWorkflowTriggerOutputDto:
      type: object
      properties:
        type:
          enum:
            - formSubmitted
            - formSubmittedNoEvent
          type: string
          description: Trigger type for the workflow
          example: formSubmitted
        offset:
          description: >-
            Offset details (present for
            BEFORE_EVENT/AFTER_EVENT/FORM_SUBMITTED_NO_EVENT)
          allOf:
            - $ref: '#/components/schemas/WorkflowTriggerOffsetOutputDto'
      required:
        - type
    RoutingFormWorkflowStepOutputDto:
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
            - email_attendee
            - email_address
            - sms_attendee
            - sms_number
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