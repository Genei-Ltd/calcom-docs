> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update organization team booking fields

> <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>

Updates the booking fields identified by `slug`. Omitted properties keep their current values. Workflow-added fields are read-only. Required membership role: `team admin`. PBAC permission: `eventType.update`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control. If accessed using an OAuth access token, the `TEAM_EVENT_TYPE_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json patch /v2/organizations/{orgId}/teams/{teamId}/event-types/{eventTypeId}/booking-fields
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
  /v2/organizations/{orgId}/teams/{teamId}/event-types/{eventTypeId}/booking-fields:
    patch:
      tags:
        - Organization Event Types
      summary: Update organization team booking fields
      description: >-
        <Note>Please make sure to pass in the cal-api-version header value as
        mentioned in the Headers section. Not passing the correct value will
        default to an older version of this endpoint.</Note>


        Updates the booking fields identified by `slug`. Omitted properties keep
        their current values. Workflow-added fields are read-only. Required
        membership role: `team admin`. PBAC permission: `eventType.update`.
        Learn more about API access control at
        https://cal.com/docs/api-reference/v2/access-control. If accessed using
        an OAuth access token, the `TEAM_EVENT_TYPE_WRITE` scope is required.
      operationId: OrganizationsEventTypesController_2026_06_12_updateBookingFields
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
              $ref: '#/components/schemas/PatchBookingFieldsInput_2026_06_12'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BookingFieldsOutput_2026_06_12'
components:
  schemas:
    PatchBookingFieldsInput_2026_06_12:
      type: object
      properties:
        bookingFields:
          type: array
          minItems: 1
          items:
            allOf:
              - type: object
                required:
                  - slug
              - anyOf:
                  - $ref: >-
                      #/components/schemas/PartialOmitSystemFullNameFieldInput_2026_06_12Field
                    title: Default Full Name
                  - $ref: >-
                      #/components/schemas/PartialOmitSystemSplitNameFieldInput_2026_06_12Field
                    title: Default Split Name
                  - $ref: >-
                      #/components/schemas/PartialOmitSystemEmailFieldInput_2026_06_12Field
                    title: Default Email
                  - $ref: >-
                      #/components/schemas/PartialOmitSystemLocationFieldInput_2026_06_12Field
                    title: Default Location
                  - $ref: >-
                      #/components/schemas/PartialOmitSystemTitleFieldInput_2026_06_12Field
                    title: Default Title
                  - $ref: >-
                      #/components/schemas/PartialOmitSystemNotesFieldInput_2026_06_12Field
                    title: Default Notes
                  - $ref: >-
                      #/components/schemas/PartialOmitSystemGuestsFieldInput_2026_06_12Field
                    title: Default Guests
                  - $ref: >-
                      #/components/schemas/PartialOmitSystemRescheduleReasonFieldInput_2026_06_12Field
                    title: Default Reschedule Reason
                  - $ref: >-
                      #/components/schemas/PartialOmitSystemAttendeePhoneFieldInput_2026_06_12Field
                    title: Default Attendee Phone
                  - $ref: >-
                      #/components/schemas/PartialOmitCustomEmailFieldInput_2026_06_12Field
                    title: Custom Email
                  - $ref: >-
                      #/components/schemas/PartialOmitCustomPhoneFieldInput_2026_06_12Field
                    title: Custom Phone
                  - $ref: >-
                      #/components/schemas/PartialOmitCustomAddressFieldInput_2026_06_12Field
                    title: Custom Address
                  - $ref: >-
                      #/components/schemas/PartialOmitCustomShortTextFieldInput_2026_06_12Field
                    title: Custom Short Text
                  - $ref: >-
                      #/components/schemas/PartialOmitCustomNumberFieldInput_2026_06_12Field
                    title: Custom Number
                  - $ref: >-
                      #/components/schemas/PartialOmitCustomLongTextFieldInput_2026_06_12Field
                    title: Custom Long Text
                  - $ref: >-
                      #/components/schemas/PartialOmitCustomSelectFieldInput_2026_06_12Field
                    title: Custom Select
                  - $ref: >-
                      #/components/schemas/PartialOmitCustomMultiSelectFieldInput_2026_06_12Field
                    title: Custom Multi-Select
                  - $ref: >-
                      #/components/schemas/PartialOmitCustomMultiEmailFieldInput_2026_06_12Field
                    title: Custom Multiple Emails
                  - $ref: >-
                      #/components/schemas/PartialOmitCustomCheckboxGroupFieldInput_2026_06_12Field
                    title: Custom Checkbox Group
                  - $ref: >-
                      #/components/schemas/PartialOmitCustomCheckboxFieldInput_2026_06_12Field
                    title: Custom Checkbox
                  - $ref: >-
                      #/components/schemas/PartialOmitCustomRadioGroupFieldInput_2026_06_12Field
                    title: Custom Radio Group
                  - $ref: >-
                      #/components/schemas/PartialOmitCustomUrlFieldInput_2026_06_12Field
                    title: Custom URL
          description: >-
            Booking fields to update. Identify each field by `slug` and include
            at least one property to change. `field` and a custom field's `type`
            cannot be changed. Null values and repeated slugs are not allowed.
            Workflow-added fields are read-only.
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
    PartialOmitSystemFullNameFieldInput_2026_06_12Field:
      type: object
      properties:
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
    PartialOmitSystemSplitNameFieldInput_2026_06_12Field:
      type: object
      properties:
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
    PartialOmitSystemEmailFieldInput_2026_06_12Field:
      type: object
      properties:
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
    PartialOmitSystemLocationFieldInput_2026_06_12Field:
      type: object
      properties:
        slug:
          type: string
          example: location
          description: Only allowed value is 'location'.
        label:
          type: string
    PartialOmitSystemTitleFieldInput_2026_06_12Field:
      type: object
      properties:
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
    PartialOmitSystemNotesFieldInput_2026_06_12Field:
      type: object
      properties:
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
    PartialOmitSystemGuestsFieldInput_2026_06_12Field:
      type: object
      properties:
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
    PartialOmitSystemRescheduleReasonFieldInput_2026_06_12Field:
      type: object
      properties:
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
    PartialOmitSystemAttendeePhoneFieldInput_2026_06_12Field:
      type: object
      properties:
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
    PartialOmitCustomEmailFieldInput_2026_06_12Field:
      type: object
      properties:
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
    PartialOmitCustomPhoneFieldInput_2026_06_12Field:
      type: object
      properties:
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
    PartialOmitCustomAddressFieldInput_2026_06_12Field:
      type: object
      properties:
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
    PartialOmitCustomShortTextFieldInput_2026_06_12Field:
      type: object
      properties:
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
    PartialOmitCustomNumberFieldInput_2026_06_12Field:
      type: object
      properties:
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
    PartialOmitCustomLongTextFieldInput_2026_06_12Field:
      type: object
      properties:
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
    PartialOmitCustomSelectFieldInput_2026_06_12Field:
      type: object
      properties:
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
    PartialOmitCustomMultiSelectFieldInput_2026_06_12Field:
      type: object
      properties:
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
    PartialOmitCustomMultiEmailFieldInput_2026_06_12Field:
      type: object
      properties:
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
    PartialOmitCustomCheckboxGroupFieldInput_2026_06_12Field:
      type: object
      properties:
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
    PartialOmitCustomCheckboxFieldInput_2026_06_12Field:
      type: object
      properties:
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
    PartialOmitCustomRadioGroupFieldInput_2026_06_12Field:
      type: object
      properties:
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
    PartialOmitCustomUrlFieldInput_2026_06_12Field:
      type: object
      properties:
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