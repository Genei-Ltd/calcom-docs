> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Replace booking fields

> <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>

Replaces all booking fields. Omitted custom fields are deleted, while omitted default fields are restored with their default settings. Use `PATCH` to update specific fields. Workflow-added fields are read-only and ignored. If accessed using an OAuth access token, the `EVENT_TYPE_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json put /v2/event-types/{eventTypeId}/booking-fields
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
  /v2/event-types/{eventTypeId}/booking-fields:
    put:
      tags:
        - Event Types
      summary: Replace booking fields
      description: >-
        <Note>Please make sure to pass in the cal-api-version header value as
        mentioned in the Headers section. Not passing the correct value will
        default to an older version of this endpoint.</Note>


        Replaces all booking fields. Omitted custom fields are deleted, while
        omitted default fields are restored with their default settings. Use
        `PATCH` to update specific fields. Workflow-added fields are read-only
        and ignored. If accessed using an OAuth access token, the
        `EVENT_TYPE_WRITE` scope is required.
      operationId: EventTypesController_2026_06_12_replaceBookingFields
      parameters:
        - name: cal-api-version
          in: header
          description: >-
            Must be set to 2026-06-12. If not set to this value, the endpoint
            will default to an older version.
          required: true
          schema:
            type: string
            example: '2026-06-12'
            default: '2026-06-12'
        - name: eventTypeId
          required: true
          in: path
          schema:
            type: number
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
              $ref: '#/components/schemas/BookingFieldsInput_2026_06_12'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BookingFieldsOutput_2026_06_12'
components:
  schemas:
    BookingFieldsInput_2026_06_12:
      type: object
      properties:
        bookingFields:
          type: array
          minItems: 1
          items:
            oneOf:
              - $ref: '#/components/schemas/SystemFullNameFieldInput_2026_06_12'
                title: Default Full Name
              - $ref: '#/components/schemas/SystemSplitNameFieldInput_2026_06_12'
                title: Default Split Name
              - $ref: '#/components/schemas/SystemEmailFieldInput_2026_06_12'
                title: Default Email
              - $ref: '#/components/schemas/SystemLocationFieldInput_2026_06_12'
                title: Default Location
              - $ref: '#/components/schemas/SystemTitleFieldInput_2026_06_12'
                title: Default Title
              - $ref: '#/components/schemas/SystemNotesFieldInput_2026_06_12'
                title: Default Notes
              - $ref: '#/components/schemas/SystemGuestsFieldInput_2026_06_12'
                title: Default Guests
              - $ref: >-
                  #/components/schemas/SystemRescheduleReasonFieldInput_2026_06_12
                title: Default Reschedule Reason
              - $ref: '#/components/schemas/SystemAttendeePhoneFieldInput_2026_06_12'
                title: Default Attendee Phone
              - $ref: '#/components/schemas/SystemSmsReminderFieldInput_2026_06_12'
                title: Workflow-added SMS Reminder
              - $ref: '#/components/schemas/SystemAiAgentPhoneFieldInput_2026_06_12'
                title: Workflow-added AI Agent Phone
              - $ref: '#/components/schemas/CustomEmailFieldInput_2026_06_12'
                title: Custom Email
              - $ref: '#/components/schemas/CustomPhoneFieldInput_2026_06_12'
                title: Custom Phone
              - $ref: '#/components/schemas/CustomAddressFieldInput_2026_06_12'
                title: Custom Address
              - $ref: '#/components/schemas/CustomShortTextFieldInput_2026_06_12'
                title: Custom Short Text
              - $ref: '#/components/schemas/CustomNumberFieldInput_2026_06_12'
                title: Custom Number
              - $ref: '#/components/schemas/CustomLongTextFieldInput_2026_06_12'
                title: Custom Long Text
              - $ref: '#/components/schemas/CustomSelectFieldInput_2026_06_12'
                title: Custom Select
              - $ref: '#/components/schemas/CustomMultiSelectFieldInput_2026_06_12'
                title: Custom Multi-Select
              - $ref: '#/components/schemas/CustomMultiEmailFieldInput_2026_06_12'
                title: Custom Multiple Emails
              - $ref: '#/components/schemas/CustomCheckboxGroupFieldInput_2026_06_12'
                title: Custom Checkbox Group
              - $ref: '#/components/schemas/CustomCheckboxFieldInput_2026_06_12'
                title: Custom Checkbox
              - $ref: '#/components/schemas/CustomRadioGroupFieldInput_2026_06_12'
                title: Custom Radio Group
              - $ref: '#/components/schemas/CustomUrlFieldInput_2026_06_12'
                title: Custom URL
          description: >-
            Booking fields to add or use as a replacement. The array cannot be
            empty, contain duplicate default fields or custom slugs, or use a
            default field's slug for a custom field. When replacing fields, at
            least one of `email` or `attendeePhoneNumber` must remain visible
            and required. Workflow-added fields are read-only and ignored when
            replacing fields.
      required:
        - bookingFields
    BookingFieldsOutput_2026_06_12:
      type: object
      properties:
        status:
          enum:
            - success
            - error
          type: string
          example: success
        data:
          $ref: '#/components/schemas/BookingFieldsOutputData_2026_06_12'
      required:
        - status
        - data
    SystemFullNameFieldInput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: name
          description: Only allowed value is 'name'.
        slug:
          type: string
          example: name
          description: Only allowed value is 'name'.
        variant:
          type: string
          example: fullName
          description: >-
            Only allowed value is 'fullName'. Used for having a single booking
            field for the attendee's full name.
        label:
          type: string
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if URL contains query parameter `&name=bob`,    the name
            field will be prefilled with this value and disabled.
      required:
        - field
        - variant
    SystemSplitNameFieldInput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: name
          description: Only allowed value is 'name'.
        slug:
          type: string
          example: name
          description: Only allowed value is 'name'.
        variant:
          type: string
          example: splitName
          description: >-
            Only allowed value is 'splitName'. Used to have 2 booking fields —
            one for first name and one for last name.
        firstNameLabel:
          type: string
        firstNamePlaceholder:
          type: string
        lastNameLabel:
          type: string
        lastNamePlaceholder:
          type: string
        lastNameRequired:
          type: boolean
          description: >-
            Whether the last name sub-field is required. The first name
            sub-field is always required and cannot be configured.
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if URL contains query parameter `?name=John%20Doe`,    the
            first name and last name fields will be prefilled with these values
            and disabled.    The value may also be a JSON object such as
            `{"firstName":"John","lastName":"Doe"}`.
      required:
        - field
        - variant
    SystemEmailFieldInput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: email
          description: Only allowed value is 'email'.
        slug:
          type: string
          example: email
          description: Only allowed value is 'email'.
        label:
          type: string
        required:
          type: boolean
          description: >-
            To enable phone-only bookings, set this to false and hidden to true,
            then pass an attendeePhoneNumber default booking field with
            required: true and hidden: false.
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if URL contains query parameter `&email=bob@gmail.com`,   
            the email field will be prefilled with this value and disabled.
        excludeEmails:
          description: >-
            Bookers whose email matches an entry cannot book. Entries may be a
            bare domain (`example.com`), a domain with `@` (`@example.com`), or
            an exact address (`person@example.com`). Matching is
            case-insensitive.
          type: array
          items:
            type: string
        requireEmails:
          description: >-
            Only bookers whose email matches an entry can book. Entries may be a
            bare domain (`example.com`), a domain with `@` (`@example.com`), or
            an exact address (`person@example.com`). Matching is
            case-insensitive.
          type: array
          items:
            type: string
      required:
        - field
    SystemLocationFieldInput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: location
          description: >-
            Only allowed value is 'location'. The Booker renders the location
            picker only when the event type has at least 2 location options.
        slug:
          type: string
          example: location
          description: Only allowed value is 'location'.
        label:
          type: string
      required:
        - field
    SystemTitleFieldInput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: title
          description: Only allowed value is 'title'.
        slug:
          type: string
          example: title
          description: Only allowed value is 'title'.
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        label:
          type: string
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if URL contains query parameter `&title=journey`,    the
            title field will be prefilled with this value and disabled.
      required:
        - field
    SystemNotesFieldInput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: notes
          description: Only allowed value is 'notes'.
        slug:
          type: string
          example: notes
          description: Only allowed value is 'notes'.
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        label:
          type: string
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if URL contains query parameter `&notes=bring notebook`,   
            the notes field will be prefilled with this value and disabled.
      required:
        - field
    SystemGuestsFieldInput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: guests
          description: Only allowed value is 'guests'.
        slug:
          type: string
          example: guests
          description: Only allowed value is 'guests'.
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        label:
          type: string
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if URL contains query parameter `&guests=bob@cal.com`,   
            the guests field will be prefilled with this value and disabled.
      required:
        - field
    SystemRescheduleReasonFieldInput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: rescheduleReason
          description: Only allowed value is 'rescheduleReason'.
        slug:
          type: string
          example: rescheduleReason
          description: Only allowed value is 'rescheduleReason'.
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        label:
          type: string
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if URL contains query parameter
            `&rescheduleReason=travel`,    the rescheduleReason field will be
            prefilled with this value and disabled.
      required:
        - field
    SystemAttendeePhoneFieldInput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: attendeePhoneNumber
          description: Only allowed value is 'attendeePhoneNumber'.
        slug:
          type: string
          example: attendeePhoneNumber
          description: Only allowed value is 'attendeePhoneNumber'.
        required:
          type: boolean
          description: >-
            To enable email-only bookings, set this to false and hidden to true,
            then pass an email default booking field with required: true and
            hidden: false.
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        label:
          type: string
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if URL contains query parameter
            `&attendeePhoneNumber=+37122222222`,    the phone field will be
            prefilled with this value and disabled.
      required:
        - field
    SystemSmsReminderFieldInput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: smsReminderNumber
          description: >-
            Only allowed value is 'smsReminderNumber'. This field is added
            automatically by an SMS workflow. It may be echoed from a GET
            response in create, update, or replace bodies, but the API ignores
            it; targeted PATCH and DELETE operations reject it.
        slug:
          type: string
          example: smsReminderNumber
          description: Only allowed value is 'smsReminderNumber'.
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        label:
          type: string
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.
      required:
        - field
    SystemAiAgentPhoneFieldInput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: aiAgentCallPhoneNumber
          description: >-
            Only allowed value is 'aiAgentCallPhoneNumber'. This field is added
            automatically by an AI-agent workflow. It may be echoed from a GET
            response in create, update, or replace bodies, but the API ignores
            it; targeted PATCH and DELETE operations reject it.
        slug:
          type: string
          example: aiAgentCallPhoneNumber
          description: Only allowed value is 'aiAgentCallPhoneNumber'.
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        label:
          type: string
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.
      required:
        - field
    CustomEmailFieldInput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: custom
          description: Must be 'custom' for all custom booking fields.
        slug:
          type: string
          description: >-
            Unique identifier for the field in format `some-slug`. Must start
            with a lowercase letter and contain only lowercase letters, numbers,
            and single hyphens.
          example: some-slug
        label:
          type: string
          example: Your custom field label
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        type:
          type: string
          example: email
          description: Only allowed value is 'email'.
        excludeEmails:
          description: >-
            Bookers whose email matches an entry cannot book. Entries may be a
            bare domain (`example.com`), a domain with `@` (`@example.com`), or
            an exact address (`person@example.com`). Matching is
            case-insensitive.
          type: array
          items:
            type: string
        requireEmails:
          description: >-
            Only bookers whose email matches an entry can book. Entries may be a
            bare domain (`example.com`), a domain with `@` (`@example.com`), or
            an exact address (`person@example.com`). Matching is
            case-insensitive.
          type: array
          items:
            type: string
      required:
        - field
        - slug
        - label
        - type
    CustomPhoneFieldInput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: custom
          description: Must be 'custom' for all custom booking fields.
        slug:
          type: string
          description: >-
            Unique identifier for the field in format `some-slug`. Must start
            with a lowercase letter and contain only lowercase letters, numbers,
            and single hyphens.
          example: some-slug
        label:
          type: string
          example: Your custom field label
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        type:
          type: string
          example: phone
          description: Only allowed value is 'phone'.
      required:
        - field
        - slug
        - label
        - type
    CustomAddressFieldInput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: custom
          description: Must be 'custom' for all custom booking fields.
        slug:
          type: string
          description: >-
            Unique identifier for the field in format `some-slug`. Must start
            with a lowercase letter and contain only lowercase letters, numbers,
            and single hyphens.
          example: some-slug
        label:
          type: string
          example: Your custom field label
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        type:
          type: string
          example: address
          description: Only allowed value is 'address'.
      required:
        - field
        - slug
        - label
        - type
    CustomShortTextFieldInput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: custom
          description: Must be 'custom' for all custom booking fields.
        slug:
          type: string
          description: >-
            Unique identifier for the field in format `some-slug`. Must start
            with a lowercase letter and contain only lowercase letters, numbers,
            and single hyphens.
          example: some-slug
        label:
          type: string
          example: Your custom field label
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        type:
          type: string
          example: shortText
          description: Only allowed value is 'shortText'.
      required:
        - field
        - slug
        - label
        - type
    CustomNumberFieldInput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: custom
          description: Must be 'custom' for all custom booking fields.
        slug:
          type: string
          description: >-
            Unique identifier for the field in format `some-slug`. Must start
            with a lowercase letter and contain only lowercase letters, numbers,
            and single hyphens.
          example: some-slug
        label:
          type: string
          example: Your custom field label
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        type:
          type: string
          example: number
          description: Only allowed value is 'number'.
      required:
        - field
        - slug
        - label
        - type
    CustomLongTextFieldInput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: custom
          description: Must be 'custom' for all custom booking fields.
        slug:
          type: string
          description: >-
            Unique identifier for the field in format `some-slug`. Must start
            with a lowercase letter and contain only lowercase letters, numbers,
            and single hyphens.
          example: some-slug
        label:
          type: string
          example: Your custom field label
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        type:
          type: string
          example: longText
          description: Only allowed value is 'longText'.
        minLength:
          type: number
          minimum: 0
          maximum: 1000
          description: >-
            Minimum character length for the long text field. Defaults to 0 if
            not provided.
        maxLength:
          type: number
          minimum: 0
          maximum: 1000
          description: >-
            Maximum character length for the long text field. Defaults to 1000
            if not provided.
      required:
        - field
        - slug
        - label
        - type
    CustomSelectFieldInput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: custom
          description: Must be 'custom' for all custom booking fields.
        slug:
          type: string
          description: >-
            Unique identifier for the field in format `some-slug`. Must start
            with a lowercase letter and contain only lowercase letters, numbers,
            and single hyphens.
          example: some-slug
        label:
          type: string
          example: Your custom field label
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        options:
          example:
            - Option 1
            - Option 2
          type: array
          items:
            type: string
        type:
          type: string
          example: select
          description: Only allowed value is 'select'.
      required:
        - field
        - slug
        - label
        - options
        - type
    CustomMultiSelectFieldInput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: custom
          description: Must be 'custom' for all custom booking fields.
        slug:
          type: string
          description: >-
            Unique identifier for the field in format `some-slug`. Must start
            with a lowercase letter and contain only lowercase letters, numbers,
            and single hyphens.
          example: some-slug
        label:
          type: string
          example: Your custom field label
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        options:
          example:
            - Option 1
            - Option 2
          type: array
          items:
            type: string
        type:
          type: string
          example: multiSelect
          description: Only allowed value is 'multiSelect'.
      required:
        - field
        - slug
        - label
        - options
        - type
    CustomMultiEmailFieldInput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: custom
          description: Must be 'custom' for all custom booking fields.
        slug:
          type: string
          description: >-
            Unique identifier for the field in format `some-slug`. Must start
            with a lowercase letter and contain only lowercase letters, numbers,
            and single hyphens.
          example: some-slug
        label:
          type: string
          example: Your custom field label
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        type:
          type: string
          example: multiEmail
          description: Only allowed value is 'multiEmail'.
      required:
        - field
        - slug
        - label
        - type
    CustomCheckboxGroupFieldInput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: custom
          description: Must be 'custom' for all custom booking fields.
        slug:
          type: string
          description: >-
            Unique identifier for the field in format `some-slug`. Must start
            with a lowercase letter and contain only lowercase letters, numbers,
            and single hyphens.
          example: some-slug
        label:
          type: string
          example: Your custom field label
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        options:
          example:
            - Option 1
            - Option 2
          type: array
          items:
            type: string
        type:
          type: string
          example: checkboxGroup
          description: Only allowed value is 'checkboxGroup'.
      required:
        - field
        - slug
        - label
        - options
        - type
    CustomCheckboxFieldInput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: custom
          description: Must be 'custom' for all custom booking fields.
        slug:
          type: string
          description: >-
            Unique identifier for the field in format `some-slug`. Must start
            with a lowercase letter and contain only lowercase letters, numbers,
            and single hyphens.
          example: some-slug
        label:
          type: string
          example: Your custom field label
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        type:
          type: string
          example: checkbox
          description: Only allowed value is 'checkbox'.
      required:
        - field
        - slug
        - label
        - type
    CustomRadioGroupFieldInput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: custom
          description: Must be 'custom' for all custom booking fields.
        slug:
          type: string
          description: >-
            Unique identifier for the field in format `some-slug`. Must start
            with a lowercase letter and contain only lowercase letters, numbers,
            and single hyphens.
          example: some-slug
        label:
          type: string
          example: Your custom field label
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        options:
          example:
            - Option 1
            - Option 2
          type: array
          items:
            type: string
        type:
          type: string
          example: radioGroup
          description: Only allowed value is 'radioGroup'.
      required:
        - field
        - slug
        - label
        - options
        - type
    CustomUrlFieldInput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: custom
          description: Must be 'custom' for all custom booking fields.
        slug:
          type: string
          description: >-
            Unique identifier for the field in format `some-slug`. Must start
            with a lowercase letter and contain only lowercase letters, numbers,
            and single hyphens.
          example: some-slug
        label:
          type: string
          example: Your custom field label
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        type:
          type: string
          example: url
          description: Only allowed value is 'url'.
      required:
        - field
        - slug
        - label
        - type
    BookingFieldsOutputData_2026_06_12:
      type: object
      properties:
        bookingFields:
          type: array
          items:
            discriminator:
              propertyName: field
            oneOf:
              - title: Default Name
                discriminator:
                  propertyName: variant
                oneOf:
                  - $ref: '#/components/schemas/SystemFullNameFieldOutput_2026_06_12'
                    title: Default Full Name
                  - $ref: '#/components/schemas/SystemSplitNameFieldOutput_2026_06_12'
                    title: Default Split Name
              - $ref: '#/components/schemas/SystemEmailFieldOutput_2026_06_12'
                title: Default Email
              - $ref: '#/components/schemas/SystemLocationFieldOutput_2026_06_12'
                title: Default Location
              - $ref: '#/components/schemas/SystemTitleFieldOutput_2026_06_12'
                title: Default Title
              - $ref: '#/components/schemas/SystemNotesFieldOutput_2026_06_12'
                title: Default Notes
              - $ref: '#/components/schemas/SystemGuestsFieldOutput_2026_06_12'
                title: Default Guests
              - $ref: >-
                  #/components/schemas/SystemRescheduleReasonFieldOutput_2026_06_12
                title: Default Reschedule Reason
              - $ref: '#/components/schemas/SystemAttendeePhoneFieldOutput_2026_06_12'
                title: Default Attendee Phone
              - $ref: '#/components/schemas/SystemSmsReminderFieldOutput_2026_06_12'
                title: Workflow-added SMS Reminder
              - $ref: '#/components/schemas/SystemAiAgentPhoneFieldOutput_2026_06_12'
                title: Workflow-added AI Agent Phone
              - title: Custom Booking Field
                discriminator:
                  propertyName: type
                oneOf:
                  - $ref: '#/components/schemas/CustomEmailFieldOutput_2026_06_12'
                    title: Custom Email
                  - $ref: '#/components/schemas/CustomPhoneFieldOutput_2026_06_12'
                    title: Custom Phone
                  - $ref: '#/components/schemas/CustomAddressFieldOutput_2026_06_12'
                    title: Custom Address
                  - $ref: '#/components/schemas/CustomShortTextFieldOutput_2026_06_12'
                    title: Custom Short Text
                  - $ref: '#/components/schemas/CustomNumberFieldOutput_2026_06_12'
                    title: Custom Number
                  - $ref: '#/components/schemas/CustomLongTextFieldOutput_2026_06_12'
                    title: Custom Long Text
                  - $ref: '#/components/schemas/CustomSelectFieldOutput_2026_06_12'
                    title: Custom Select
                  - $ref: >-
                      #/components/schemas/CustomMultiSelectFieldOutput_2026_06_12
                    title: Custom Multi-Select
                  - $ref: >-
                      #/components/schemas/CustomMultiEmailFieldOutput_2026_06_12
                    title: Custom Multiple Emails
                  - $ref: >-
                      #/components/schemas/CustomCheckboxGroupFieldOutput_2026_06_12
                    title: Custom Checkbox Group
                  - $ref: >-
                      #/components/schemas/CustomRadioGroupFieldOutput_2026_06_12
                    title: Custom Radio Group
                  - $ref: '#/components/schemas/CustomCheckboxFieldOutput_2026_06_12'
                    title: Custom Checkbox
                  - $ref: '#/components/schemas/CustomUrlFieldOutput_2026_06_12'
                    title: Custom URL
              - $ref: '#/components/schemas/UnknownBookingFieldOutput_2026_06_12'
                title: Unknown Booking Field
          description: The event type's default, custom, and workflow-added booking fields.
      required:
        - bookingFields
    SystemFullNameFieldOutput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: name
          description: Identifies this as the name default booking field.
        slug:
          type: string
          example: name
          description: The default name field always uses `name` as its slug.
        variant:
          type: string
          example: fullName
          enum:
            - fullName
          description: Single full-name input variant.
        label:
          type: string
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
      required:
        - field
        - slug
        - variant
        - disableOnPrefill
    SystemSplitNameFieldOutput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: name
          description: Identifies this as the name default booking field.
        slug:
          type: string
          example: name
          description: The default name field always uses `name` as its slug.
        variant:
          type: string
          example: splitName
          enum:
            - splitName
          description: >-
            The booking page displays separate fields for the attendee's first
            and last names.
        firstNameLabel:
          type: string
        firstNamePlaceholder:
          type: string
        lastNameLabel:
          type: string
        lastNamePlaceholder:
          type: string
        lastNameRequired:
          type: boolean
          description: Whether the last name sub-field is required.
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
      required:
        - field
        - slug
        - variant
        - lastNameRequired
        - disableOnPrefill
    SystemEmailFieldOutput_2026_06_12:
      type: object
      properties:
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        label:
          type: string
          example: Your default field label
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        field:
          type: string
          example: email
          description: Identifies this as the email default booking field.
        slug:
          type: string
          example: email
          description: The default email field always uses `email` as its slug.
        excludeEmails:
          description: >-
            Bookers whose email matches an entry cannot book. Entries may be a
            bare domain (`example.com`), a domain with `@` (`@example.com`), or
            an exact address (`person@example.com`). Matching is
            case-insensitive.
          type: array
          items:
            type: string
        requireEmails:
          description: >-
            Only bookers whose email matches an entry can book. Entries may be a
            bare domain (`example.com`), a domain with `@` (`@example.com`), or
            an exact address (`person@example.com`). Matching is
            case-insensitive.
          type: array
          items:
            type: string
      required:
        - required
        - hidden
        - disableOnPrefill
        - field
        - slug
    SystemLocationFieldOutput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: location
          description: >-
            Identifies this as the location default booking field. The Booker
            renders the location picker only when the event type has at least 2
            location options.
        slug:
          type: string
          example: location
          description: The default location field always uses `location` as its slug.
        label:
          type: string
          example: Your location default field label
      required:
        - field
        - slug
    SystemTitleFieldOutput_2026_06_12:
      type: object
      properties:
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        label:
          type: string
          example: Your default field label
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        field:
          type: string
          example: title
          description: Identifies this as the title default booking field.
        slug:
          type: string
          example: title
          description: The default booking title field always uses `title` as its slug.
      required:
        - required
        - hidden
        - disableOnPrefill
        - field
        - slug
    SystemNotesFieldOutput_2026_06_12:
      type: object
      properties:
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        label:
          type: string
          example: Your default field label
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        field:
          type: string
          example: notes
          description: Identifies this as the notes default booking field.
        slug:
          type: string
          example: notes
          description: The default additional-notes field always uses `notes` as its slug.
      required:
        - required
        - hidden
        - disableOnPrefill
        - field
        - slug
    SystemGuestsFieldOutput_2026_06_12:
      type: object
      properties:
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        label:
          type: string
          example: Your default field label
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        field:
          type: string
          example: guests
          description: Identifies this as the guests default booking field.
        slug:
          type: string
          example: guests
          description: >-
            The default additional-guests field always uses `guests` as its
            slug.
      required:
        - required
        - hidden
        - disableOnPrefill
        - field
        - slug
    SystemRescheduleReasonFieldOutput_2026_06_12:
      type: object
      properties:
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        label:
          type: string
          example: Your default field label
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        field:
          type: string
          example: rescheduleReason
          description: Identifies this as the reschedule reason default booking field.
        slug:
          type: string
          example: rescheduleReason
          description: >-
            The default reschedule-reason field always uses `rescheduleReason`
            as its slug.
      required:
        - required
        - hidden
        - disableOnPrefill
        - field
        - slug
    SystemAttendeePhoneFieldOutput_2026_06_12:
      type: object
      properties:
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        label:
          type: string
          example: Your default field label
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        field:
          type: string
          example: attendeePhoneNumber
          description: Identifies this as the attendee phone number default booking field.
        slug:
          type: string
          example: attendeePhoneNumber
          description: >-
            The default attendee phone field always uses `attendeePhoneNumber`
            as its slug.
      required:
        - required
        - hidden
        - disableOnPrefill
        - field
        - slug
    SystemSmsReminderFieldOutput_2026_06_12:
      type: object
      properties:
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        label:
          type: string
          example: Your default field label
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        field:
          type: string
          example: smsReminderNumber
          description: Phone-number field added automatically by an SMS workflow.
        slug:
          type: string
          example: smsReminderNumber
          description: >-
            This workflow-added field always uses `smsReminderNumber` as its
            slug.
      required:
        - required
        - hidden
        - disableOnPrefill
        - field
        - slug
    SystemAiAgentPhoneFieldOutput_2026_06_12:
      type: object
      properties:
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        label:
          type: string
          example: Your default field label
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        field:
          type: string
          example: aiAgentCallPhoneNumber
          description: Phone-number field added automatically by an AI-agent workflow.
        slug:
          type: string
          example: aiAgentCallPhoneNumber
          description: >-
            This workflow-added field always uses `aiAgentCallPhoneNumber` as
            its slug.
      required:
        - required
        - hidden
        - disableOnPrefill
        - field
        - slug
    CustomEmailFieldOutput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: custom
          description: Identifies this as a custom booking field.
        slug:
          type: string
          description: Unique slug identifier for this custom field.
          example: some-slug
        label:
          type: string
          example: Your custom field label
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        type:
          type: string
          example: email
          enum:
            - email
          description: An email input on the booking page.
        excludeEmails:
          description: >-
            Bookers whose email matches an entry cannot book. Entries may be a
            bare domain (`example.com`), a domain with `@` (`@example.com`), or
            an exact address (`person@example.com`). Matching is
            case-insensitive.
          type: array
          items:
            type: string
        requireEmails:
          description: >-
            Only bookers whose email matches an entry can book. Entries may be a
            bare domain (`example.com`), a domain with `@` (`@example.com`), or
            an exact address (`person@example.com`). Matching is
            case-insensitive.
          type: array
          items:
            type: string
      required:
        - field
        - slug
        - label
        - required
        - hidden
        - disableOnPrefill
        - type
    CustomPhoneFieldOutput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: custom
          description: Identifies this as a custom booking field.
        slug:
          type: string
          description: Unique slug identifier for this custom field.
          example: some-slug
        label:
          type: string
          example: Your custom field label
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        type:
          type: string
          example: phone
          enum:
            - phone
          description: A phone-number input on the booking page.
      required:
        - field
        - slug
        - label
        - required
        - hidden
        - disableOnPrefill
        - type
    CustomAddressFieldOutput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: custom
          description: Identifies this as a custom booking field.
        slug:
          type: string
          description: Unique slug identifier for this custom field.
          example: some-slug
        label:
          type: string
          example: Your custom field label
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        type:
          type: string
          example: address
          enum:
            - address
          description: An address input on the booking page.
      required:
        - field
        - slug
        - label
        - required
        - hidden
        - disableOnPrefill
        - type
    CustomShortTextFieldOutput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: custom
          description: Identifies this as a custom booking field.
        slug:
          type: string
          description: Unique slug identifier for this custom field.
          example: some-slug
        label:
          type: string
          example: Your custom field label
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        type:
          type: string
          example: shortText
          enum:
            - shortText
          description: A single-line text input on the booking page.
      required:
        - field
        - slug
        - label
        - required
        - hidden
        - disableOnPrefill
        - type
    CustomNumberFieldOutput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: custom
          description: Identifies this as a custom booking field.
        slug:
          type: string
          description: Unique slug identifier for this custom field.
          example: some-slug
        label:
          type: string
          example: Your custom field label
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        type:
          type: string
          example: number
          enum:
            - number
          description: A number input on the booking page.
      required:
        - field
        - slug
        - label
        - required
        - hidden
        - disableOnPrefill
        - type
    CustomLongTextFieldOutput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: custom
          description: Identifies this as a custom booking field.
        slug:
          type: string
          description: Unique slug identifier for this custom field.
          example: some-slug
        label:
          type: string
          example: Your custom field label
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        type:
          type: string
          example: longText
          enum:
            - longText
          description: A multi-line text input on the booking page.
        minLength:
          type: number
          description: Minimum character length for the long text field.
        maxLength:
          type: number
          description: Maximum character length for the long text field.
      required:
        - field
        - slug
        - label
        - required
        - hidden
        - disableOnPrefill
        - type
    CustomSelectFieldOutput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: custom
          description: Identifies this as a custom booking field.
        slug:
          type: string
          description: Unique slug identifier for this custom field.
          example: some-slug
        label:
          type: string
          example: Your custom field label
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        options:
          example:
            - Option 1
            - Option 2
          type: array
          items:
            type: string
        type:
          type: string
          example: select
          enum:
            - select
          description: A dropdown that allows one selection.
      required:
        - field
        - slug
        - label
        - required
        - hidden
        - disableOnPrefill
        - options
        - type
    CustomMultiSelectFieldOutput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: custom
          description: Identifies this as a custom booking field.
        slug:
          type: string
          description: Unique slug identifier for this custom field.
          example: some-slug
        label:
          type: string
          example: Your custom field label
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        options:
          example:
            - Option 1
            - Option 2
          type: array
          items:
            type: string
        type:
          type: string
          example: multiSelect
          enum:
            - multiSelect
          description: A list that allows multiple selections.
      required:
        - field
        - slug
        - label
        - required
        - hidden
        - disableOnPrefill
        - options
        - type
    CustomMultiEmailFieldOutput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: custom
          description: Identifies this as a custom booking field.
        slug:
          type: string
          description: Unique slug identifier for this custom field.
          example: some-slug
        label:
          type: string
          example: Your custom field label
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        type:
          type: string
          example: multiEmail
          enum:
            - multiEmail
          description: An input that accepts multiple email addresses.
      required:
        - field
        - slug
        - label
        - required
        - hidden
        - disableOnPrefill
        - type
    CustomCheckboxGroupFieldOutput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: custom
          description: Identifies this as a custom booking field.
        slug:
          type: string
          description: Unique slug identifier for this custom field.
          example: some-slug
        label:
          type: string
          example: Your custom field label
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        options:
          example:
            - Option 1
            - Option 2
          type: array
          items:
            type: string
        type:
          type: string
          example: checkboxGroup
          enum:
            - checkboxGroup
          description: A group of checkboxes that allows multiple selections.
      required:
        - field
        - slug
        - label
        - required
        - hidden
        - disableOnPrefill
        - options
        - type
    CustomRadioGroupFieldOutput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: custom
          description: Identifies this as a custom booking field.
        slug:
          type: string
          description: Unique slug identifier for this custom field.
          example: some-slug
        label:
          type: string
          example: Your custom field label
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        options:
          example:
            - Option 1
            - Option 2
          type: array
          items:
            type: string
        type:
          type: string
          example: radioGroup
          enum:
            - radioGroup
          description: A group of radio buttons that allows one selection.
      required:
        - field
        - slug
        - label
        - required
        - hidden
        - disableOnPrefill
        - options
        - type
    CustomCheckboxFieldOutput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: custom
          description: Identifies this as a custom booking field.
        slug:
          type: string
          description: Unique slug identifier for this custom field.
          example: some-slug
        label:
          type: string
          example: Your custom field label
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        type:
          type: string
          example: checkbox
          enum:
            - checkbox
          description: A single checkbox on the booking page.
      required:
        - field
        - slug
        - label
        - required
        - hidden
        - disableOnPrefill
        - type
    CustomUrlFieldOutput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: custom
          description: Identifies this as a custom booking field.
        slug:
          type: string
          description: Unique slug identifier for this custom field.
          example: some-slug
        label:
          type: string
          example: Your custom field label
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            Hide this booking field from the booking page while keeping it in
            the event type's settings. Hidden fields are only returned to
            callers authorized on the event type.
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.    For
            example, if the slug is `my-field` and the URL contains
            `&my-field=value`,    the field will be prefilled with this value
            and disabled.
        type:
          type: string
          example: url
          enum:
            - url
          description: A URL input on the booking page.
      required:
        - field
        - slug
        - label
        - required
        - hidden
        - disableOnPrefill
        - type
    UnknownBookingFieldOutput_2026_06_12:
      type: object
      properties:
        field:
          type: string
          example: unknown
          enum:
            - unknown
        slug:
          type: string
          example: unknown
          enum:
            - unknown
        bookingField:
          type: string
          description: Raw booking-field data that this API version does not recognize.
      required:
        - field
        - slug
        - bookingField

````