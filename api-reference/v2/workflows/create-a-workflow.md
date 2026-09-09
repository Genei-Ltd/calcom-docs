> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a workflow

> Create an event-type workflow owned by the authenticated user. Not available to third-party OAuth access tokens.



## OpenAPI

````yaml /api-reference/v2/openapi.json post /v2/workflows
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
  /v2/workflows:
    post:
      tags:
        - Workflows
      summary: Create a workflow
      description: >-
        Create an event-type workflow owned by the authenticated user. Not
        available to third-party OAuth access tokens.
      operationId: UserWorkflowsController_createWorkflow
      parameters:
        - name: Authorization
          in: header
          description: >-
            value must be `Bearer <token>` where `<token>` is api key prefixed
            with cal_, managed user access token, or OAuth access token
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateEventTypeWorkflowDto'
      responses:
        '201':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetEventTypeWorkflowOutput'
components:
  schemas:
    CreateEventTypeWorkflowDto:
      type: object
      properties:
        name:
          type: string
          description: Name of the workflow
          example: Platform Test Workflow
        activation:
          description: Activation settings for the workflow
          allOf:
            - $ref: '#/components/schemas/WorkflowActivationDto'
        trigger:
          description: >-
            Trigger configuration for the event-type workflow, allowed triggers
            are
            beforeEvent,eventCancelled,newEvent,afterEvent,rescheduleEvent,afterHostsCalVideoNoShow,afterGuestsCalVideoNoShow,bookingRejected,bookingRequested,bookingPaymentInitiated,bookingPaid,bookingNoShowUpdated
          oneOf:
            - $ref: '#/components/schemas/OnBeforeEventTriggerDto'
              title: Before Event
            - $ref: '#/components/schemas/OnAfterEventTriggerDto'
              title: After Event
            - $ref: '#/components/schemas/OnCancelTriggerDto'
              title: Event Cancelled
            - $ref: '#/components/schemas/OnCreationTriggerDto'
              title: New Event
            - $ref: '#/components/schemas/OnRescheduleTriggerDto'
              title: Event Rescheduled
            - $ref: '#/components/schemas/OnAfterCalVideoGuestsNoShowTriggerDto'
              title: After Guest No-Show
            - $ref: '#/components/schemas/OnAfterCalVideoHostsNoShowTriggerDto'
              title: After Host No-Show
            - $ref: '#/components/schemas/OnRejectedTriggerDto'
              title: Booking Rejected
            - $ref: '#/components/schemas/OnRequestedTriggerDto'
              title: Booking Requested
            - $ref: '#/components/schemas/OnPaidTriggerDto'
              title: Booking Paid
            - $ref: '#/components/schemas/OnPaymentInitiatedTriggerDto'
              title: Booking Payment Initiated
            - $ref: '#/components/schemas/OnNoShowUpdateTriggerDto'
              title: Booking No-Show Updated
        steps:
          type: array
          minItems: 1
          description: >-
            Steps to execute as part of the event-type workflow, allowed steps
            are
            email_host,email_attendee,email_address,sms_attendee,sms_number,whatsapp_attendee,whatsapp_number,cal_ai_phone_call
          items:
            oneOf:
              - $ref: '#/components/schemas/WorkflowEmailAddressStepDto'
                title: Email Address
              - $ref: '#/components/schemas/WorkflowEmailAttendeeStepDto'
                title: Email Attendee
              - $ref: '#/components/schemas/WorkflowEmailHostStepDto'
                title: Email Host
              - $ref: '#/components/schemas/WorkflowPhoneWhatsAppAttendeeStepDto'
                title: WhatsApp Attendee
              - $ref: '#/components/schemas/WorkflowPhoneWhatsAppNumberStepDto'
                title: WhatsApp Number
              - $ref: '#/components/schemas/WorkflowPhoneNumberStepDto'
                title: SMS Number
              - $ref: '#/components/schemas/WorkflowPhoneAttendeeStepDto'
                title: SMS Attendee
      required:
        - name
        - activation
        - trigger
        - steps
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
    WorkflowActivationDto:
      type: object
      properties:
        isActiveOnAllEventTypes:
          type: boolean
          default: false
          description: Whether the workflow is active for all the event-types
          example: false
        activeOnEventTypeIds:
          default: []
          description: >-
            List of event-types IDs the workflow applies to, required if
            isActiveOnAllEventTypes is false
          example:
            - 698191
          type: array
          items:
            type: number
      required:
        - isActiveOnAllEventTypes
    OnBeforeEventTriggerDto:
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
          default: beforeEvent
          enum:
            - beforeEvent
          description: Trigger type for the workflow
          example: beforeEvent
      required:
        - offset
        - type
    OnAfterEventTriggerDto:
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
          default: afterEvent
          enum:
            - afterEvent
          description: Trigger type for the workflow
          example: afterEvent
      required:
        - offset
        - type
    OnCancelTriggerDto:
      type: object
      properties:
        type:
          type: string
          default: eventCancelled
          enum:
            - eventCancelled
          description: Trigger type for the workflow
      required:
        - type
    OnCreationTriggerDto:
      type: object
      properties:
        type:
          type: string
          default: newEvent
          enum:
            - newEvent
          description: Trigger type for the workflow
      required:
        - type
    OnRescheduleTriggerDto:
      type: object
      properties:
        type:
          type: string
          default: rescheduleEvent
          enum:
            - rescheduleEvent
          description: Trigger type for the workflow
      required:
        - type
    OnAfterCalVideoGuestsNoShowTriggerDto:
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
          default: afterGuestsCalVideoNoShow
          enum:
            - afterGuestsCalVideoNoShow
          description: Trigger type for the workflow
          example: afterGuestsCalVideoNoShow
      required:
        - offset
        - type
    OnAfterCalVideoHostsNoShowTriggerDto:
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
          default: afterHostsCalVideoNoShow
          enum:
            - afterHostsCalVideoNoShow
          description: Trigger type for the workflow
          example: afterHostsCalVideoNoShow
      required:
        - offset
        - type
    OnRejectedTriggerDto:
      type: object
      properties:
        type:
          type: string
          default: bookingRejected
          enum:
            - bookingRejected
          description: Trigger type for the workflow
      required:
        - type
    OnRequestedTriggerDto:
      type: object
      properties:
        type:
          type: string
          default: bookingRequested
          enum:
            - bookingRequested
          description: Trigger type for the workflow
      required:
        - type
    OnPaidTriggerDto:
      type: object
      properties:
        type:
          type: string
          default: bookingPaid
          enum:
            - bookingPaid
          description: Trigger type for the workflow
      required:
        - type
    OnPaymentInitiatedTriggerDto:
      type: object
      properties:
        type:
          type: string
          default: bookingPaymentInitiated
          enum:
            - bookingPaymentInitiated
          description: Trigger type for the workflow
      required:
        - type
    OnNoShowUpdateTriggerDto:
      type: object
      properties:
        type:
          type: string
          default: bookingNoShowUpdated
          enum:
            - bookingNoShowUpdated
          description: Trigger type for the workflow
      required:
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
    WorkflowEmailHostStepDto:
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
          default: email_host
          description: Action to perform, send an email to the host of the event
          example: email_host
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
    WorkflowPhoneWhatsAppAttendeeStepDto:
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
          default: whatsapp_attendee
          description: Action to perform
          example: whatsapp_attendee
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
          description: >-
            Message content for this step, send a text message via whatsapp to
            the phone numbers of the attendees
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
    WorkflowPhoneWhatsAppNumberStepDto:
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
          default: whatsapp_number
          description: >-
            Action to perform, send a text message via whatsapp to a specific
            phone number
          example: whatsapp_number
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