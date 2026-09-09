> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get an event type

> <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>
    
    Access control: This endpoint fetches an event type by ID and returns it only if the authenticated user is authorized. Authorization is granted to:
    - System admins
    - The event type owner
    - Hosts of the event type or users assigned to the event type
    - Team admins/owners of the team that owns the team event type
    - Organization admins/owners of the event type owner's organization
    - Organization admins/owners of the team's parent organization

    Note: Update and delete endpoints remain restricted to the event type owner only. If accessed using an OAuth access token, the `EVENT_TYPE_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/event-types/{eventTypeId}
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
  /v2/event-types/{eventTypeId}:
    get:
      tags:
        - Event Types
      summary: Get an event type
      description: >-
        <Note>Please make sure to pass in the cal-api-version header value as
        mentioned in the Headers section. Not passing the correct value will
        default to an older version of this endpoint.</Note>
            
            Access control: This endpoint fetches an event type by ID and returns it only if the authenticated user is authorized. Authorization is granted to:
            - System admins
            - The event type owner
            - Hosts of the event type or users assigned to the event type
            - Team admins/owners of the team that owns the team event type
            - Organization admins/owners of the event type owner's organization
            - Organization admins/owners of the team's parent organization

            Note: Update and delete endpoints remain restricted to the event type owner only. If accessed using an OAuth access token, the `EVENT_TYPE_READ` scope is required.
      operationId: EventTypesController_2024_06_14_getEventTypeById
      parameters:
        - name: cal-api-version
          in: header
          description: >-
            Must be set to 2024-06-14. If not set to this value, the endpoint
            will default to an older version.
          required: true
          schema:
            type: string
            default: '2024-06-14'
        - name: eventTypeId
          required: true
          in: path
          schema:
            type: string
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
                $ref: '#/components/schemas/GetEventTypeOutput_2024_06_14'
components:
  schemas:
    GetEventTypeOutput_2024_06_14:
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
            - $ref: '#/components/schemas/EventTypeOutput_2024_06_14'
            - $ref: '#/components/schemas/TeamEventTypeOutput_2024_06_14'
      required:
        - status
        - data
    EventTypeOutput_2024_06_14:
      type: object
      properties:
        id:
          type: number
          example: 1
        lengthInMinutes:
          type: number
          example: 60
        lengthInMinutesOptions:
          example:
            - 15
            - 30
            - 60
          description: >-
            If you want that user can choose between different lengths of the
            event you can specify them here. Must include the provided
            `lengthInMinutes`.
          type: array
          items:
            type: number
        title:
          type: string
          example: Learn the secrets of masterchief!
        slug:
          type: string
          example: learn-the-secrets-of-masterchief
        description:
          type: string
          example: >-
            Discover the culinary wonders of Argentina by making the best flan
            ever!
        locations:
          type: array
          items:
            oneOf:
              - $ref: '#/components/schemas/OutputAddressLocation_2024_06_14'
              - $ref: '#/components/schemas/OutputLinkLocation_2024_06_14'
              - $ref: '#/components/schemas/OutputIntegrationLocation_2024_06_14'
              - $ref: '#/components/schemas/OutputPhoneLocation_2024_06_14'
              - $ref: >-
                  #/components/schemas/OutputOrganizersDefaultAppLocation_2024_06_14
              - $ref: '#/components/schemas/OutputUnknownLocation_2024_06_14'
        bookingFields:
          type: array
          items:
            oneOf:
              - $ref: '#/components/schemas/NameDefaultFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/EmailDefaultFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/LocationDefaultFieldOutput_2024_06_14'
              - $ref: >-
                  #/components/schemas/RescheduleReasonDefaultFieldOutput_2024_06_14
              - $ref: '#/components/schemas/TitleDefaultFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/NotesDefaultFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/GuestsDefaultFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/PhoneFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/AddressFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/TextFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/NumberFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/TextAreaFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/SelectFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/MultiSelectFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/MultiEmailFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/CheckboxGroupFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/RadioGroupFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/BooleanFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/UrlFieldOutput_2024_06_14'
        disableGuests:
          type: boolean
        slotInterval:
          type: number
          example: 60
          nullable: true
        minimumBookingNotice:
          type: number
          example: 0
        beforeEventBuffer:
          type: number
          example: 0
        afterEventBuffer:
          type: number
          example: 0
        recurrence:
          nullable: true
          allOf:
            - $ref: '#/components/schemas/Recurrence_2024_06_14'
        metadata:
          type: object
        price:
          type: number
        currency:
          type: string
        lockTimeZoneToggleOnBookingPage:
          type: boolean
        seatsPerTimeSlot:
          type: number
          nullable: true
        forwardParamsSuccessRedirect:
          type: boolean
          nullable: true
        successRedirectUrl:
          type: string
          nullable: true
        isInstantEvent:
          type: boolean
        seatsShowAvailabilityCount:
          type: boolean
          nullable: true
        scheduleId:
          type: number
          nullable: true
        bookingLimitsCount:
          oneOf:
            - $ref: '#/components/schemas/BaseBookingLimitsCount_2024_06_14'
            - $ref: '#/components/schemas/Disabled_2024_06_14'
        bookerActiveBookingsLimit:
          $ref: '#/components/schemas/BookerActiveBookingsLimitOutput_2024_06_14'
        onlyShowFirstAvailableSlot:
          type: boolean
        bookingLimitsDuration:
          oneOf:
            - $ref: '#/components/schemas/BaseBookingLimitsDuration_2024_06_14'
            - $ref: '#/components/schemas/Disabled_2024_06_14'
        bookingWindow:
          type: array
          description: Limit how far in the future this event can be booked
          items:
            oneOf:
              - $ref: '#/components/schemas/BusinessDaysWindow_2024_06_14'
              - $ref: '#/components/schemas/CalendarDaysWindow_2024_06_14'
              - $ref: '#/components/schemas/RangeWindow_2024_06_14'
        bookerLayouts:
          $ref: '#/components/schemas/BookerLayouts_2024_06_14'
        confirmationPolicy:
          oneOf:
            - $ref: '#/components/schemas/BaseConfirmationPolicy_2024_06_14'
            - $ref: '#/components/schemas/Disabled_2024_06_14'
        requiresBookerEmailVerification:
          type: boolean
        hideCalendarNotes:
          type: boolean
        color:
          $ref: '#/components/schemas/EventTypeColor_2024_06_14'
        seats:
          $ref: '#/components/schemas/Seats_2024_06_14'
        offsetStart:
          type: number
        customName:
          type: string
        destinationCalendar:
          $ref: '#/components/schemas/DestinationCalendar_2024_06_14'
        useDestinationCalendarEmail:
          type: boolean
        hideCalendarEventDetails:
          type: boolean
        hideOrganizerEmail:
          type: boolean
          description: >-
            Boolean to Hide organizer's email address from the booking screen,
            email notifications, and calendar events
        calVideoSettings:
          description: Cal video settings for the event type
          allOf:
            - $ref: '#/components/schemas/CalVideoSettings'
        hidden:
          type: boolean
        bookingRequiresAuthentication:
          type: boolean
          description: >-
            Boolean to require authentication for booking this event type via
            api. If true, only authenticated users who are the event-type owner
            or org/team admin/owner can book this event type.
        disableCancelling:
          description: Settings for disabling cancelling of this event type.
          allOf:
            - $ref: '#/components/schemas/DisableCancellingOutput_2024_06_14'
        disableRescheduling:
          description: >-
            Settings for disabling rescheduling of this event type. Can be
            always disabled or disabled when less than X minutes before the
            meeting.
          allOf:
            - $ref: '#/components/schemas/DisableReschedulingOutput_2024_06_14'
        interfaceLanguage:
          type: string
          nullable: true
          description: Set preferred language for the booking interface.
        allowReschedulingPastBookings:
          type: boolean
          description: Enabling this option allows for past events to be rescheduled.
        allowReschedulingCancelledBookings:
          type: boolean
          nullable: true
          description: >-
            When enabled, users will be able to create a new booking when trying
            to reschedule a cancelled booking.
        showOptimizedSlots:
          type: boolean
          nullable: true
          description: Arrange time slots to optimize availability.
        privateNoteEnabled:
          type: boolean
          description: >-
            When enabled, a private note calendar event is created alongside the
            booking with the resolved template as its description. Only visible
            to the host.
        privateNoteMode:
          type: string
          nullable: true
          description: >-
            The mode for private notes. Currently only 'duplicate_event' is
            supported.
        privateNoteTemplate:
          type: string
          nullable: true
          description: >-
            Template for the private note content. Supports variables like
            {Attendee name}, {Event type title}, {Location}, {Host name}, {Event
            duration}, and custom booking field names.
        ownerId:
          type: number
          example: 10
        users:
          type: array
          items:
            $ref: '#/components/schemas/User_2024_06_14'
        bookingUrl:
          type: string
          description: Full URL to the booking page for this event type
          example: https://cal.com/john-doe/30min
          format: uri
      required:
        - id
        - lengthInMinutes
        - title
        - slug
        - description
        - locations
        - bookingFields
        - disableGuests
        - recurrence
        - metadata
        - price
        - currency
        - lockTimeZoneToggleOnBookingPage
        - forwardParamsSuccessRedirect
        - successRedirectUrl
        - isInstantEvent
        - scheduleId
        - hidden
        - bookingRequiresAuthentication
        - ownerId
        - users
        - bookingUrl
    TeamEventTypeOutput_2024_06_14:
      type: object
      properties:
        id:
          type: number
          example: 1
        lengthInMinutes:
          type: number
          example: 60
        lengthInMinutesOptions:
          example:
            - 15
            - 30
            - 60
          description: >-
            If you want that user can choose between different lengths of the
            event you can specify them here. Must include the provided
            `lengthInMinutes`.
          type: array
          items:
            type: number
        title:
          type: string
          example: Learn the secrets of masterchief!
        slug:
          type: string
          example: learn-the-secrets-of-masterchief
        description:
          type: string
          example: >-
            Discover the culinary wonders of Argentina by making the best flan
            ever!
        locations:
          type: array
          items:
            oneOf:
              - $ref: '#/components/schemas/OutputAddressLocation_2024_06_14'
              - $ref: '#/components/schemas/OutputLinkLocation_2024_06_14'
              - $ref: '#/components/schemas/OutputIntegrationLocation_2024_06_14'
              - $ref: '#/components/schemas/OutputPhoneLocation_2024_06_14'
              - $ref: >-
                  #/components/schemas/OutputOrganizersDefaultAppLocation_2024_06_14
              - $ref: '#/components/schemas/OutputUnknownLocation_2024_06_14'
        bookingFields:
          type: array
          items:
            oneOf:
              - $ref: '#/components/schemas/NameDefaultFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/EmailDefaultFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/LocationDefaultFieldOutput_2024_06_14'
              - $ref: >-
                  #/components/schemas/RescheduleReasonDefaultFieldOutput_2024_06_14
              - $ref: '#/components/schemas/TitleDefaultFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/NotesDefaultFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/GuestsDefaultFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/PhoneFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/AddressFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/TextFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/NumberFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/TextAreaFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/SelectFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/MultiSelectFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/MultiEmailFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/CheckboxGroupFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/RadioGroupFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/BooleanFieldOutput_2024_06_14'
              - $ref: '#/components/schemas/UrlFieldOutput_2024_06_14'
        disableGuests:
          type: boolean
        slotInterval:
          type: number
          example: 60
          nullable: true
        minimumBookingNotice:
          type: number
          example: 0
        beforeEventBuffer:
          type: number
          example: 0
        afterEventBuffer:
          type: number
          example: 0
        recurrence:
          nullable: true
          allOf:
            - $ref: '#/components/schemas/Recurrence_2024_06_14'
        metadata:
          type: object
        price:
          type: number
        currency:
          type: string
        lockTimeZoneToggleOnBookingPage:
          type: boolean
        seatsPerTimeSlot:
          type: number
          nullable: true
        forwardParamsSuccessRedirect:
          type: boolean
          nullable: true
        successRedirectUrl:
          type: string
          nullable: true
        isInstantEvent:
          type: boolean
        seatsShowAvailabilityCount:
          type: boolean
          nullable: true
        scheduleId:
          type: number
          nullable: true
        bookingLimitsCount:
          oneOf:
            - $ref: '#/components/schemas/BaseBookingLimitsCount_2024_06_14'
            - $ref: '#/components/schemas/Disabled_2024_06_14'
        bookerActiveBookingsLimit:
          $ref: '#/components/schemas/BookerActiveBookingsLimitOutput_2024_06_14'
        onlyShowFirstAvailableSlot:
          type: boolean
        bookingLimitsDuration:
          oneOf:
            - $ref: '#/components/schemas/BaseBookingLimitsDuration_2024_06_14'
            - $ref: '#/components/schemas/Disabled_2024_06_14'
        bookingWindow:
          type: array
          description: Limit how far in the future this event can be booked
          items:
            oneOf:
              - $ref: '#/components/schemas/BusinessDaysWindow_2024_06_14'
              - $ref: '#/components/schemas/CalendarDaysWindow_2024_06_14'
              - $ref: '#/components/schemas/RangeWindow_2024_06_14'
        bookerLayouts:
          $ref: '#/components/schemas/BookerLayouts_2024_06_14'
        confirmationPolicy:
          oneOf:
            - $ref: '#/components/schemas/BaseConfirmationPolicy_2024_06_14'
            - $ref: '#/components/schemas/Disabled_2024_06_14'
        requiresBookerEmailVerification:
          type: boolean
        hideCalendarNotes:
          type: boolean
        color:
          $ref: '#/components/schemas/EventTypeColor_2024_06_14'
        seats:
          $ref: '#/components/schemas/Seats_2024_06_14'
        offsetStart:
          type: number
        customName:
          type: string
        destinationCalendar:
          $ref: '#/components/schemas/DestinationCalendar_2024_06_14'
        useDestinationCalendarEmail:
          type: boolean
        hideCalendarEventDetails:
          type: boolean
        hideOrganizerEmail:
          type: boolean
          description: >-
            Boolean to Hide organizer's email address from the booking screen,
            email notifications, and calendar events
        calVideoSettings:
          description: Cal video settings for the event type
          allOf:
            - $ref: '#/components/schemas/CalVideoSettings'
        hidden:
          type: boolean
        bookingRequiresAuthentication:
          type: boolean
          description: >-
            Boolean to require authentication for booking this event type via
            api. If true, only authenticated users who are the event-type owner
            or org/team admin/owner can book this event type.
        disableCancelling:
          description: Settings for disabling cancelling of this event type.
          allOf:
            - $ref: '#/components/schemas/DisableCancellingOutput_2024_06_14'
        disableRescheduling:
          description: >-
            Settings for disabling rescheduling of this event type. Can be
            always disabled or disabled when less than X minutes before the
            meeting.
          allOf:
            - $ref: '#/components/schemas/DisableReschedulingOutput_2024_06_14'
        interfaceLanguage:
          type: string
          nullable: true
          description: Set preferred language for the booking interface.
        allowReschedulingPastBookings:
          type: boolean
          description: Enabling this option allows for past events to be rescheduled.
        allowReschedulingCancelledBookings:
          type: boolean
          nullable: true
          description: >-
            When enabled, users will be able to create a new booking when trying
            to reschedule a cancelled booking.
        showOptimizedSlots:
          type: boolean
          nullable: true
          description: Arrange time slots to optimize availability.
        privateNoteEnabled:
          type: boolean
          description: >-
            When enabled, a private note calendar event is created alongside the
            booking with the resolved template as its description. Only visible
            to the host.
        privateNoteMode:
          type: string
          nullable: true
          description: >-
            The mode for private notes. Currently only 'duplicate_event' is
            supported.
        privateNoteTemplate:
          type: string
          nullable: true
          description: >-
            Template for the private note content. Supports variables like
            {Attendee name}, {Event type title}, {Location}, {Host name}, {Event
            duration}, and custom booking field names.
        teamId:
          type: number
        bookingUrl:
          type: string
          nullable: true
          description: >-
            Full URL to the booking page for this team event type. Null for
            managed team event types or when the team does not have a slug.
          example: https://cal.com/team/acme/30min
          format: uri
        ownerId:
          type: number
          nullable: true
        parentEventTypeId:
          type: number
          nullable: true
          description: >-
            For managed event types, parent event type is the event type that
            this event type is based on
        hosts:
          type: array
          items:
            $ref: '#/components/schemas/TeamEventTypeResponseHost'
        assignAllTeamMembers:
          type: boolean
        schedulingType:
          type: string
          enum:
            - roundRobin
            - collective
            - managed
        team:
          $ref: '#/components/schemas/EventTypeTeam'
        emailSettings:
          description: >-
            Email settings for this event type. Only available for organization
            team event types.
          allOf:
            - $ref: '#/components/schemas/EmailSettings_2024_06_14'
        rescheduleWithSameRoundRobinHost:
          type: boolean
          description: >-
            Rescheduled events will be assigned to the same host as initially
            scheduled.
      required:
        - id
        - lengthInMinutes
        - title
        - slug
        - description
        - locations
        - bookingFields
        - disableGuests
        - recurrence
        - metadata
        - price
        - currency
        - lockTimeZoneToggleOnBookingPage
        - forwardParamsSuccessRedirect
        - successRedirectUrl
        - isInstantEvent
        - scheduleId
        - hidden
        - bookingRequiresAuthentication
        - teamId
        - bookingUrl
        - hosts
        - schedulingType
        - team
    OutputAddressLocation_2024_06_14:
      type: object
      properties:
        type:
          type: string
          example: address
          description: only allowed value for type is `address`
        address:
          type: string
          minLength: 1
          example: 123 Example St, City, Country
        public:
          type: boolean
      required:
        - type
        - address
        - public
    OutputLinkLocation_2024_06_14:
      type: object
      properties:
        type:
          type: string
          example: link
          description: only allowed value for type is `link`
        link:
          type: string
          example: https://customvideo.com/join/123456
        public:
          type: boolean
      required:
        - type
        - link
        - public
    OutputIntegrationLocation_2024_06_14:
      type: object
      properties:
        type:
          type: string
          example: integration
          description: Only allowed value for type is `integration`
        integration:
          type: string
          example: cal-video
          enum:
            - cal-video
            - google-meet
            - zoom
            - whereby-video
            - whatsapp-video
            - webex-video
            - telegram-video
            - tandem
            - sylaps-video
            - skype-video
            - sirius-video
            - signal-video
            - shimmer-video
            - salesroom-video
            - roam-video
            - riverside-video
            - ping-video
            - office365-video
            - mirotalk-video
            - jitsi
            - jelly-video
            - jelly-conferencing
            - huddle
            - facetime-video
            - element-call-video
            - eightxeight-video
            - discord-video
            - demodesk-video
            - campfire-video
        link:
          type: string
          example: https://example.com
        credentialId:
          type: number
          description: Credential ID associated with the integration
      required:
        - type
        - integration
    OutputPhoneLocation_2024_06_14:
      type: object
      properties:
        type:
          type: string
          example: phone
          description: only allowed value for type is `phone`
        phone:
          type: string
          example: '+37120993151'
        public:
          type: boolean
      required:
        - type
        - phone
        - public
    OutputOrganizersDefaultAppLocation_2024_06_14:
      type: object
      properties:
        type:
          type: string
          example: organizersDefaultApp
          description: only allowed value for type is `organizersDefaultApp`
      required:
        - type
    OutputUnknownLocation_2024_06_14:
      type: object
      properties:
        type:
          type: string
          example: unknown
          description: only allowed value for type is `unknown`
        location:
          type: string
      required:
        - type
        - location
    NameDefaultFieldOutput_2024_06_14:
      type: object
      properties:
        type:
          type: string
          example: name
          description: >-
            only allowed value for type is `name`. Used for having 1 booking
            field for both first name and last name.
          default: name
        label:
          type: string
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.     
            For example, if URL contains query parameter `&name=bob`,      the
            name field will be prefilled with this value and disabled. In case
            of Booker atom need to pass 'name' to defaultFormValues prop with
            the desired value e.g. `defaultFormValues={{name: 'bob'}}`. See
            guide https://cal.com/docs/platform/guides/booking-fields
        isDefault:
          type: boolean
          default: true
          description: This property is always true because it's a default field
          example: true
        slug:
          type: string
          default: name
        required:
          type: boolean
      required:
        - type
        - isDefault
        - slug
        - required
    EmailDefaultFieldOutput_2024_06_14:
      type: object
      properties:
        type:
          type: string
          example: email
          description: only allowed value for type is `email`
          default: email
        label:
          type: string
        required:
          type: boolean
          default: true
          description: >-
            If true show under event type settings but don't show this booking
            field in the Booker. If false show in both.
        hidden:
          type: boolean
          description: >-
            If true show under event type settings but don't show this booking
            field in the Booker. If false show in both.
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.     
            For example, if URL contains query parameter
            `&email=bob@gmail.com`,      the email field will be prefilled with
            this value and disabled. In case of Booker atom need to pass 'email'
            to defaultFormValues prop with the desired value e.g.
            `defaultFormValues={{email: 'bob@gmail.com'}}`. See guide
            https://cal.com/docs/platform/guides/booking-fields
        isDefault:
          type: boolean
          default: true
          description: This property is always true because it's a default field
          example: true
        slug:
          type: string
          default: email
      required:
        - type
        - isDefault
        - slug
    LocationDefaultFieldOutput_2024_06_14:
      type: object
      properties:
        isDefault:
          type: boolean
          default: true
          description: This property is always true because it's a default field
          example: true
        slug:
          type: string
          default: location
          description: >-
            This booking field is returned only if the event type has more than
            one location. The purpose of this field is to allow the user to
            select the location where the event will take place.
        type:
          type: string
          default: radioInput
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            If true show under event type settings but don't show this booking
            field in the Booker. If false show in both.
        label:
          type: string
      required:
        - isDefault
        - slug
        - type
        - required
        - hidden
    RescheduleReasonDefaultFieldOutput_2024_06_14:
      type: object
      properties:
        slug:
          type: string
          example: rescheduleReason
          description: only allowed value for type is `rescheduleReason`
          default: rescheduleReason
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            If true show under event type settings but don't show this booking
            field in the Booker. If false show in both.
        label:
          type: string
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.     
            For example, if URL contains query parameter
            `&rescheduleReason=busy`,      the reschedule reason field will be
            prefilled with this value and disabled.
        isDefault:
          type: boolean
          default: true
          description: This property is always true because it's a default field
          example: true
        type:
          type: string
          default: textarea
      required:
        - slug
        - isDefault
        - type
    TitleDefaultFieldOutput_2024_06_14:
      type: object
      properties:
        slug:
          type: string
          example: title
          description: only allowed value for type is `title`
          default: title
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            If true show under event type settings but don't show this booking
            field in the Booker. If false show in both.
        label:
          type: string
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.     
            For example, if URL contains query parameter
            `&title=masterclass`,      the title field will be prefilled with
            this value and disabled.
        isDefault:
          type: boolean
          default: true
          description: This property is always true because it's a default field
          example: true
        type:
          type: string
          default: text
      required:
        - slug
        - isDefault
        - type
    NotesDefaultFieldOutput_2024_06_14:
      type: object
      properties:
        slug:
          type: string
          example: notes
          description: only allowed value for type is `notes`
          default: notes
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            If true show under event type settings but don't show this booking
            field in the Booker. If false show in both.
        label:
          type: string
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.     
            For example, if URL contains query parameter `&notes=hello`,     
            the notes field will be prefilled with this value and disabled.
        isDefault:
          type: boolean
          default: true
          description: This property is always true because it's a default field
          example: true
        type:
          type: string
          default: textarea
      required:
        - slug
        - isDefault
        - type
    GuestsDefaultFieldOutput_2024_06_14:
      type: object
      properties:
        slug:
          type: string
          example: guests
          description: only allowed value for type is `guests`
          default: guests
        required:
          type: boolean
        hidden:
          type: boolean
          description: >-
            If true show under event type settings but don't show this booking
            field in the Booker. If false show in both.
        label:
          type: string
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.     
            For example, if URL contains query parameter
            `&guests=lauris@cal.com`,      the guests field will be prefilled
            with this value and disabled.
        isDefault:
          type: boolean
          default: true
          description: This property is always true because it's a default field
          example: true
        type:
          type: string
          default: multiemail
      required:
        - slug
        - isDefault
        - type
    PhoneFieldOutput_2024_06_14:
      type: object
      properties:
        type:
          type: string
          example: phone
          description: only allowed value for type is `phone`
        slug:
          type: string
          description: >-
            Unique identifier for the field in format `some-slug`. It is used to
            access response to this booking field during the booking. Special
            slug is `attendeePhoneNumber` - if you create
                  a phone input field with this slug for organization team event type you can create an organization team event type that can be booked using phone without requiring an email by setting {"type": "email", "required": false, "hidden": true} to the email booking field input in the request body.
          example: some-slug
        label:
          type: string
        required:
          type: boolean
        placeholder:
          type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.     
            For example, if the slug is `phone` and the URL contains query
            parameter `&phone=1234567890`,      the phone field will be
            prefilled with this value and disabled. In case of Booker atom need
            to pass slug you used for this booking field to defaultFormValues
            prop with the desired value e.g. `defaultFormValues={{phone:
            '+37122222222'}}`. See guide
            https://cal.com/docs/platform/guides/booking-fields
        hidden:
          type: boolean
          description: >-
            If true show under event type settings but don't show this booking
            field in the Booker. If false show in both.
        isDefault:
          type: boolean
          default: false
          description: >-
            This property is always false because it's not default field but
            custom field
          example: false
      required:
        - type
        - slug
        - label
        - required
        - hidden
        - isDefault
    AddressFieldOutput_2024_06_14:
      type: object
      properties:
        type:
          type: string
          example: address
          description: only allowed value for type is `address`
        slug:
          type: string
          description: >-
            Unique identifier for the field in format `some-slug`. It is used to
            access response to this booking field during the booking
          example: some-slug
        label:
          type: string
          example: Please enter your address
        required:
          type: boolean
        placeholder:
          type: string
          example: e.g., 1234 Main St
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.     
            For example, if the slug is `address` and the URL contains query
            parameter `&address=1234 Main St, London`,      the address field
            will be prefilled with this value and disabled.  In case of Booker
            atom need to pass slug you used for this booking field to
            defaultFormValues prop with the desired value e.g.
            `defaultFormValues={{address: 'mainstreat 10, new york'}}`. See
            guide https://cal.com/docs/platform/guides/booking-fields
        hidden:
          type: boolean
          description: >-
            If true show under event type settings but don't show this booking
            field in the Booker. If false show in both.
        isDefault:
          type: boolean
          default: false
          description: >-
            This property is always false because it's not default field but
            custom field
          example: false
      required:
        - type
        - slug
        - label
        - required
        - hidden
        - isDefault
    TextFieldOutput_2024_06_14:
      type: object
      properties:
        type:
          type: string
          example: text
          description: only allowed value for type is `text`
        slug:
          type: string
          description: >-
            Unique identifier for the field in format `some-slug`. It is used to
            access response to this booking field during the booking
          example: some-slug
        label:
          type: string
          example: Please enter your text
        required:
          type: boolean
        placeholder:
          type: string
          example: e.g., Enter text here
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.     
            For example, if the slug is `friend` and the URL contains query
            parameter `&friend=bob`,      the text field will be prefilled with
            this value and disabled.  In case of Booker atom need to pass slug
            you used for this booking field to defaultFormValues prop with the
            desired value e.g. `defaultFormValues={{friend: 'bob'}}`. See guide
            https://cal.com/docs/platform/guides/booking-fields
        hidden:
          type: boolean
          description: >-
            If true show under event type settings but don't show this booking
            field in the Booker. If false show in both.
        isDefault:
          type: boolean
          default: false
          description: >-
            This property is always false because it's not default field but
            custom field
          example: false
      required:
        - type
        - slug
        - label
        - required
        - hidden
        - isDefault
    NumberFieldOutput_2024_06_14:
      type: object
      properties:
        type:
          type: string
          example: number
          description: only allowed value for type is `number`
        slug:
          type: string
          description: >-
            Unique identifier for the field in format `some-slug`. It is used to
            access response to this booking field during the booking
          example: some-slug
        label:
          type: string
          example: Please enter a number
        required:
          type: boolean
        placeholder:
          type: string
          example: e.g., 100
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.     
            For example, if the slug is `calories` and the URL contains query
            parameter `&calories=3000`,      the number field will be prefilled
            with this value and disabled. In case of Booker atom need to pass
            slug you used for this booking field to defaultFormValues prop with
            the desired value  e.g. `defaultFormValues={{calories: 3000}}`. See
            guide https://cal.com/docs/platform/guides/booking-fields
        hidden:
          type: boolean
          description: >-
            If true show under event type settings but don't show this booking
            field in the Booker. If false show in both.
        isDefault:
          type: boolean
          default: false
          description: >-
            This property is always false because it's not default field but
            custom field
          example: false
      required:
        - type
        - slug
        - label
        - required
        - hidden
        - isDefault
    TextAreaFieldOutput_2024_06_14:
      type: object
      properties:
        type:
          type: string
          example: textarea
          description: only allowed value for type is `textarea`
        slug:
          type: string
          description: >-
            Unique identifier for the field in format `some-slug`. It is used to
            access response to this booking field during the booking
          example: some-slug
        label:
          type: string
          example: Please enter detailed information
        required:
          type: boolean
        placeholder:
          type: string
          example: e.g., Detailed description here...
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.     
            For example, if the slug is `reflection` and the URL contains query
            parameter `&reflection=Today I shipped a feature`,      the text
            area will be prefilled with this value and disabled. In case of
            Booker atom need to pass slug you used for this booking field to
            defaultFormValues prop with the desired value  e.g.
            `defaultFormValues={{reflection: 'Today i shipped a feature'}}`. See
            guide https://cal.com/docs/platform/guides/booking-fields
        hidden:
          type: boolean
          description: >-
            If true show under event type settings but don't show this booking
            field in the Booker. If false show in both.
        isDefault:
          type: boolean
          default: false
          description: >-
            This property is always false because it's not default field but
            custom field
          example: false
      required:
        - type
        - slug
        - label
        - required
        - hidden
        - isDefault
    SelectFieldOutput_2024_06_14:
      type: object
      properties:
        type:
          type: string
          example: select
          description: only allowed value for type is `select`
        slug:
          type: string
          description: >-
            Unique identifier for the field in format `some-slug`. It is used to
            access response to this booking field during the booking
          example: some-slug
        label:
          type: string
          example: Please select an option
        required:
          type: boolean
        placeholder:
          type: string
          example: Select...
        options:
          example:
            - Option 1
            - Option 2
          type: array
          items:
            type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.     
            For example, if the slug is `language` and options of this select
            field are ['english', 'italian'] and the URL contains query
            parameter `&language=italian`,      the 'italian' will be selected
            and the select field will be disabled. In case of Booker atom need
            to pass slug you used for this booking field to defaultFormValues
            prop with the desired value  e.g. `defaultFormValues={{language:
            'italian'}}`. See guide
            https://cal.com/docs/platform/guides/booking-fields
        hidden:
          type: boolean
          description: >-
            If true show under event type settings but don't show this booking
            field in the Booker. If false show in both.
        isDefault:
          type: boolean
          default: false
          description: >-
            This property is always false because it's not default field but
            custom field
          example: false
      required:
        - type
        - slug
        - label
        - required
        - options
        - hidden
        - isDefault
    MultiSelectFieldOutput_2024_06_14:
      type: object
      properties:
        type:
          type: string
          example: multiselect
          description: only allowed value for type is `multiselect`
        slug:
          type: string
          description: >-
            Unique identifier for the field in format `some-slug`. It is used to
            access response to this booking field during the booking
          example: some-slug
        label:
          type: string
          example: Please select multiple options
        required:
          type: boolean
        options:
          example:
            - Option 1
            - Option 2
          type: array
          items:
            type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.     
            For example, if the slug is `language` and the URL contains query
            parameter `&language=en&language=it`,      the 'en' and 'it' will be
            selected and the select field will be disabled. In case of Booker
            atom need to pass slug you used for this booking field to
            defaultFormValues prop with the desired value  e.g.
            `defaultFormValues={{language: ['en', 'it']}}`. See guide
            https://cal.com/docs/platform/guides/booking-fields
        hidden:
          type: boolean
          description: >-
            If true show under event type settings but don't show this booking
            field in the Booker. If false show in both.
        isDefault:
          type: boolean
          default: false
          description: >-
            This property is always false because it's not default field but
            custom field
          example: false
      required:
        - type
        - slug
        - label
        - required
        - options
        - hidden
        - isDefault
    MultiEmailFieldOutput_2024_06_14:
      type: object
      properties:
        type:
          type: string
          example: multiemail
          description: only allowed value for type is `multiemail`
        slug:
          type: string
          description: >-
            Unique identifier for the field in format `some-slug`. It is used to
            access response to this booking field during the booking
          example: some-slug
        label:
          type: string
          example: Please enter multiple emails
        required:
          type: boolean
        placeholder:
          type: string
          example: e.g., example@example.com
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.     
            For example, if the slug is `consultants` and the URL contains query
            parameter
            `&consultants=alice@gmail.com&consultants=bob@gmail.com`,      the
            these emails will be added and none more can be added. In case of
            Booker atom need to pass slug you used for this booking field to
            defaultFormValues prop with the desired value  e.g.
            `defaultFormValues={{consultants: ['alice@gmail.com',
            'bob@gmail.com']}}`. See guide
            https://cal.com/docs/platform/guides/booking-fields
        hidden:
          type: boolean
          description: >-
            If true show under event type settings but don't show this booking
            field in the Booker. If false show in both.
        isDefault:
          type: boolean
          default: false
          description: >-
            This property is always false because it's not default field but
            custom field
          example: false
      required:
        - type
        - slug
        - label
        - required
        - hidden
        - isDefault
    CheckboxGroupFieldOutput_2024_06_14:
      type: object
      properties:
        type:
          type: string
          example: checkbox
          description: only allowed value for type is `checkbox`
        slug:
          type: string
          description: >-
            Unique identifier for the field in format `some-slug`. It is used to
            access response to this booking field during the booking
          example: some-slug
        label:
          type: string
          example: Select all that apply
        required:
          type: boolean
        options:
          example:
            - Checkbox 1
            - Checkbox 2
          type: array
          items:
            type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.     
            For example, if the slug is `notify` and the URL contains query
            parameter `&notify=true`,      the checkbox will be selected and the
            checkbox field will be disabled. In case of Booker atom need to pass
            slug you used for this booking field to defaultFormValues prop with
            the desired value  e.g. `defaultFormValues={{notify: true}}`. See
            guide https://cal.com/docs/platform/guides/booking-fields
        hidden:
          type: boolean
          description: >-
            If true show under event type settings but don't show this booking
            field in the Booker. If false show in both.
        isDefault:
          type: boolean
          default: false
          description: >-
            This property is always false because it's not default field but
            custom field
          example: false
      required:
        - type
        - slug
        - label
        - required
        - options
        - hidden
        - isDefault
    RadioGroupFieldOutput_2024_06_14:
      type: object
      properties:
        type:
          type: string
          example: radio
          description: only allowed value for type is `radio`
        slug:
          type: string
          description: >-
            Unique identifier for the field in format `some-slug`. It is used to
            access response to this booking field during the booking
          example: some-slug
        label:
          type: string
          example: Select one option
        required:
          type: boolean
        options:
          example:
            - Radio 1
            - Radio 2
          type: array
          items:
            type: string
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.     
            For example, if the slug is `language` and options of this select
            field are ['english', 'italian'] and the URL contains query
            parameter `&language=italian`,      the 'italian' radio button will
            be selected and the select field will be disabled. In case of Booker
            atom need to pass slug you used for this booking field to
            defaultFormValues prop with the desired value  e.g.
            `defaultFormValues={{language: 'italian'}}`. See guide
            https://cal.com/docs/platform/guides/booking-fields
        hidden:
          type: boolean
          description: >-
            If true show under event type settings but don't show this booking
            field in the Booker. If false show in both.
        isDefault:
          type: boolean
          default: false
          description: >-
            This property is always false because it's not default field but
            custom field
          example: false
      required:
        - type
        - slug
        - label
        - required
        - options
        - hidden
        - isDefault
    BooleanFieldOutput_2024_06_14:
      type: object
      properties:
        type:
          type: string
          example: boolean
          description: only allowed value for type is `boolean`
        slug:
          type: string
          description: >-
            Unique identifier for the field in format `some-slug`. It is used to
            access response to this booking field during the booking
          example: some-slug
        label:
          type: string
          example: Agree to terms?
        required:
          type: boolean
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.     
            For example, if the slug is `notify` and the URL contains query
            parameter `&notify=true`,      the checkbox will be selected and the
            checkbox field will be disabled. In case of Booker atom need to pass
            slug you used for this booking field to defaultFormValues prop with
            the desired value  e.g. `defaultFormValues={{notify: true}}`. See
            guide https://cal.com/docs/platform/guides/booking-fields
        hidden:
          type: boolean
          description: >-
            If true show under event type settings but don't show this booking
            field in the Booker. If false show in both.
        isDefault:
          type: boolean
          default: false
          description: >-
            This property is always false because it's not default field but
            custom field
          example: false
      required:
        - type
        - slug
        - label
        - required
        - hidden
        - isDefault
    UrlFieldOutput_2024_06_14:
      type: object
      properties:
        type:
          type: string
          example: url
          description: only allowed value for type is `url`
        slug:
          type: string
          description: >-
            Unique identifier for the field in format `some-slug`. It is used to
            access response to this booking field during the booking
          example: some-slug
        label:
          type: string
          example: Please enter your text
        required:
          type: boolean
        placeholder:
          type: string
          example: e.g., Enter url here
        disableOnPrefill:
          type: boolean
          description: >-
            Disable this booking field if the URL contains query parameter with
            key equal to the slug and prefill it with the provided value.     
            For example, if the slug is `videourl` and the URL contains query
            parameter `&videourl=https://youtube.com/abc`the url field will be
            prefilled with this value and disabled.       In case of Booker atom
            need to pass slug you used for this booking field to
            defaultFormValues prop with the desired value  e.g.
            `defaultFormValues={{videourl: 'https://caltube.com/123'}}`. See
            guide https://cal.com/docs/platform/guides/booking-fields
        hidden:
          type: boolean
          description: >-
            If true show under event type settings but don't show this booking
            field in the Booker. If false show in both.
        isDefault:
          type: boolean
          default: false
          description: >-
            This property is always false because it's not default field but
            custom field
          example: false
      required:
        - type
        - slug
        - label
        - required
        - hidden
        - isDefault
    Recurrence_2024_06_14:
      type: object
      properties:
        interval:
          type: number
          example: 10
          description: Repeats every {count} week | month | year
        occurrences:
          type: number
          example: 10
          description: Repeats for a maximum of {count} events
        frequency:
          enum:
            - yearly
            - monthly
            - weekly
          type: string
        disabled:
          type: boolean
          default: false
      required:
        - interval
        - occurrences
        - frequency
    BaseBookingLimitsCount_2024_06_14:
      type: object
      properties:
        day:
          type: number
          minimum: 1
          description: The number of bookings per day
          example: 1
        week:
          type: number
          minimum: 1
          description: The number of bookings per week
          example: 2
        month:
          type: number
          minimum: 1
          description: The number of bookings per month
          example: 3
        year:
          type: number
          minimum: 1
          description: The number of bookings per year
          example: 4
    Disabled_2024_06_14:
      type: object
      properties:
        disabled:
          type: boolean
          description: >-
            Only acceptable value for the `disabled` property is `true`. It is
            used to reset the value of the property for which previously an
            object containing specific settings was passed.
          example: true
      required:
        - disabled
    BookerActiveBookingsLimitOutput_2024_06_14:
      type: object
      properties:
        maximumActiveBookings:
          type: number
          minimum: 1
          description: >-
            The maximum number of active bookings a booker can have for this
            event type.
          example: 3
        offerReschedule:
          type: boolean
          description: >-
            Whether to offer rescheduling the last active booking to the chosen
            time slot when limit is reached.
    BaseBookingLimitsDuration_2024_06_14:
      type: object
      properties:
        day:
          type: number
          minimum: 15
          description: The duration of bookings per day (must be a multiple of 15)
          example: 60
        week:
          type: number
          minimum: 15
          description: The duration of bookings per week (must be a multiple of 15)
          example: 120
        month:
          type: number
          minimum: 15
          description: The duration of bookings per month (must be a multiple of 15)
          example: 180
        year:
          type: number
          minimum: 15
          description: The duration of bookings per year (must be a multiple of 15)
          example: 240
        disabled:
          type: boolean
          default: false
    BusinessDaysWindow_2024_06_14:
      type: object
      properties:
        type:
          type: string
          enum:
            - businessDays
            - calendarDays
            - range
          description: >-
            Whether the window should be business days, calendar days or a range
            of dates
        value:
          type: number
          example: 5
          description: How many business day into the future can this event be booked
        rolling:
          type: boolean
          example: true
          description: |2-

                  Determines the behavior of the booking window:
                  - If **true**, the window is rolling. This means the number of available days will always be equal the specified 'value' 
                    and adjust dynamically as bookings are made. For example, if 'value' is 3 and availability is only on Mondays, 
                    a booker attempting to schedule on November 10 will see slots on November 11, 18, and 25. As one of these days 
                    becomes fully booked, a new day (e.g., December 2) will open up to ensure 3 available days are always visible.
                  - If **false**, the window is fixed. This means the booking window only considers the next 'value' days from the
                    moment someone is trying to book. For example, if 'value' is 3, availability is only on Mondays, and the current 
                    date is November 10, the booker will only see slots on November 11 because the window is restricted to the next 
                    3 calendar days (November 10–12).
                
        disabled:
          type: boolean
          default: false
      required:
        - type
        - value
    CalendarDaysWindow_2024_06_14:
      type: object
      properties:
        type:
          type: string
          enum:
            - businessDays
            - calendarDays
            - range
          description: >-
            Whether the window should be business days, calendar days or a range
            of dates
        value:
          type: number
          example: 5
          description: How many calendar days into the future can this event be booked
        rolling:
          type: boolean
          example: true
          description: |2-

                  Determines the behavior of the booking window:
                  - If **true**, the window is rolling. This means the number of available days will always be equal the specified 'value' 
                    and adjust dynamically as bookings are made. For example, if 'value' is 3 and availability is only on Mondays, 
                    a booker attempting to schedule on November 10 will see slots on November 11, 18, and 25. As one of these days 
                    becomes fully booked, a new day (e.g., December 2) will open up to ensure 3 available days are always visible.
                  - If **false**, the window is fixed. This means the booking window only considers the next 'value' days from the
                    moment someone is trying to book. For example, if 'value' is 3, availability is only on Mondays, and the current 
                    date is November 10, the booker will only see slots on November 11 because the window is restricted to the next 
                    3 calendar days (November 10–12).
                
        disabled:
          type: boolean
          default: false
      required:
        - type
        - value
    RangeWindow_2024_06_14:
      type: object
      properties:
        type:
          type: string
          enum:
            - businessDays
            - calendarDays
            - range
          description: >-
            Whether the window should be business days, calendar days or a range
            of dates
        value:
          example:
            - '2030-09-05'
            - '2030-09-09'
          description: Date range for when this event can be booked.
          type: array
          items:
            type: string
        disabled:
          type: boolean
          default: false
      required:
        - type
        - value
    BookerLayouts_2024_06_14:
      type: object
      properties:
        defaultLayout:
          enum:
            - month
            - week
            - column
          type: string
        enabledLayouts:
          type: array
          items:
            enum:
              - month
              - week
              - column
            type: string
          description: Array of valid layouts - month, week or column
      required:
        - defaultLayout
        - enabledLayouts
    BaseConfirmationPolicy_2024_06_14:
      type: object
      properties:
        type:
          enum:
            - always
            - time
          type: string
          description: The policy that determines when confirmation is required
          example: always
        noticeThreshold:
          description: >-
            The notice threshold required before confirmation is needed.
            Required when type is 'time'.
          allOf:
            - $ref: '#/components/schemas/NoticeThreshold_2024_06_14'
        blockUnconfirmedBookingsInBooker:
          type: boolean
          description: Unconfirmed bookings still block calendar slots.
        disabled:
          type: boolean
          default: false
      required:
        - type
        - blockUnconfirmedBookingsInBooker
    EventTypeColor_2024_06_14:
      type: object
      properties:
        lightThemeHex:
          type: string
          description: Color used for event types in light theme
          example: '#292929'
        darkThemeHex:
          type: string
          description: Color used for event types in dark theme
          example: '#fafafa'
      required:
        - lightThemeHex
        - darkThemeHex
    Seats_2024_06_14:
      type: object
      properties:
        seatsPerTimeSlot:
          type: number
          minimum: 1
          description: Number of seats available per time slot
          example: 4
        showAttendeeInfo:
          type: boolean
          description: Show attendee information to other guests
          example: true
        showAvailabilityCount:
          type: boolean
          description: Display the count of available seats
          example: true
        disabled:
          type: boolean
          default: false
      required:
        - seatsPerTimeSlot
        - showAttendeeInfo
        - showAvailabilityCount
    DestinationCalendar_2024_06_14:
      type: object
      properties:
        integration:
          type: string
          description: >-
            The integration type of the destination calendar. Refer to the
            /api/v2/calendars endpoint to retrieve the integration type of your
            connected calendars.
        externalId:
          type: string
          description: >-
            The external ID of the destination calendar. Refer to the
            /api/v2/calendars endpoint to retrieve the external IDs of your
            connected calendars.
      required:
        - integration
        - externalId
    CalVideoSettings:
      type: object
      properties:
        disableRecordingForOrganizer:
          type: boolean
          description: If true, the organizer will not be able to record the meeting
        disableRecordingForGuests:
          type: boolean
          description: If true, the guests will not be able to record the meeting
        redirectUrlOnExit:
          type: string
          nullable: true
          description: URL to which participants are redirected when they exit the call
        enableAutomaticRecordingForOrganizer:
          type: boolean
          description: >-
            If true, enables the automatic recording for the event when
            organizer joins the call
        enableAutomaticTranscription:
          type: boolean
          description: >-
            If true, enables the automatic transcription for the event whenever
            someone joins the call
        disableTranscriptionForGuests:
          type: boolean
          description: >-
            If true, the guests will not be able to receive transcription of the
            meeting
        disableTranscriptionForOrganizer:
          type: boolean
          description: >-
            If true, the organizer will not be able to receive transcription of
            the meeting
        sendTranscriptionEmails:
          type: boolean
          description: >-
            Send emails with the transcription of the Cal Video after the
            meeting ends.
          default: true
        transcriptionLanguage:
          type: string
          nullable: true
          description: >-
            Deepgram language code for transcription (e.g. 'es', 'fr', 'de',
            'pt-BR', or 'multi' for auto-detect). Defaults to English when not
            set.
          enum:
            - multi
            - ar
            - bg
            - ca
            - zh-HK
            - hr
            - cs
            - da
            - nl
            - nl-BE
            - fi
            - fr
            - fr-CA
            - de
            - de-CH
            - el
            - he
            - hi
            - hu
            - id
            - it
            - ja
            - ko
            - lv
            - lt
            - ms
            - 'no'
            - pl
            - pt
            - pt-BR
            - ro
            - ru
            - sr
            - sk
            - sl
            - es
            - es-419
            - sv
            - th
            - tr
            - uk
            - vi
    DisableCancellingOutput_2024_06_14:
      type: object
      properties:
        disabled:
          type: boolean
          description: If true, cancelling is always disabled for this event type.
          example: true
    DisableReschedulingOutput_2024_06_14:
      type: object
      properties:
        disabled:
          type: boolean
          description: If true, rescheduling is always disabled for this event type.
          example: true
        minutesBefore:
          type: number
          minimum: 1
          description: >-
            Rescheduling is disabled when less than the specified number of
            minutes before the meeting.
          example: 60
    User_2024_06_14:
      type: object
      properties:
        id:
          type: number
        name:
          type: string
          nullable: true
        username:
          type: string
          nullable: true
        avatarUrl:
          type: string
          nullable: true
        weekStart:
          type: string
        brandColor:
          type: string
          nullable: true
        darkBrandColor:
          type: string
          nullable: true
        metadata:
          type: object
      required:
        - id
        - name
        - username
        - avatarUrl
        - weekStart
        - brandColor
        - darkBrandColor
        - metadata
    TeamEventTypeResponseHost:
      type: object
      properties:
        userId:
          type: number
          description: Which user is the host of this event
        mandatory:
          type: boolean
          default: false
          description: >-
            Only relevant for round robin event types. If true then the user
            must attend the round robin event always (fixed host). This may be
            combined with `assignAllTeamMembers: true` on round robin event
            types — entries marked `mandatory: true` become fixed hosts while
            every other team member fills the round robin pool.
        priority:
          type: string
          default: medium
          enum:
            - lowest
            - low
            - medium
            - high
            - highest
        name:
          type: string
          example: John Doe
        username:
          type: string
          example: john-doe
        avatarUrl:
          type: string
          nullable: true
          example: https://cal.com/api/avatar/d95949bc-ccb1-400f-acf6-045c51a16856.png
      required:
        - userId
        - name
        - username
    EventTypeTeam:
      type: object
      properties:
        id:
          type: number
        slug:
          type: string
        bannerUrl:
          type: string
        name:
          type: string
        logoUrl:
          type: string
        weekStart:
          type: string
        brandColor:
          type: string
        darkBrandColor:
          type: string
        theme:
          type: string
      required:
        - id
        - slug
        - bannerUrl
        - name
        - logoUrl
        - weekStart
        - brandColor
        - darkBrandColor
        - theme
    EmailSettings_2024_06_14:
      type: object
      properties:
        disableEmailsToAttendees:
          type: boolean
          description: >-
            Disables all email communication to attendees for this event type,
            including booking confirmations, reminders, and cancellations. This
            DOES NOT include emails sent by custom email workflows.
        disableEmailsToHosts:
          type: boolean
          description: >-
            Disables all email communication to hosts for this event type,
            including booking confirmations, reminders, and cancellations. This
            DOES NOT include emails sent by custom email workflows.
    NoticeThreshold_2024_06_14:
      type: object
      properties:
        unit:
          enum:
            - minutes
            - hours
          type: string
          description: The unit of time for the notice threshold (e.g., minutes, hours)
          example: minutes
        count:
          type: number
          description: The time value for the notice threshold
          example: 30
      required:
        - unit
        - count

````