> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update an organization team event type

> <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>

Omit `bookingFields` to keep the existing booking fields. If provided, the array replaces them, and any omitted default fields are restored with their default settings. Required membership role: `team admin`. PBAC permission: `eventType.update`. Learn more about API access control at https://cal.com/docs/api-reference/v2/access-control. If accessed using an OAuth access token, the `TEAM_EVENT_TYPE_WRITE` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json patch /v2/organizations/{orgId}/teams/{teamId}/event-types/{eventTypeId}
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
  /v2/organizations/{orgId}/teams/{teamId}/event-types/{eventTypeId}:
    patch:
      tags:
        - Organization Event Types
      summary: Update an organization team event type
      description: >-
        <Note>Please make sure to pass in the cal-api-version header value as
        mentioned in the Headers section. Not passing the correct value will
        default to an older version of this endpoint.</Note>


        Omit `bookingFields` to keep the existing booking fields. If provided,
        the array replaces them, and any omitted default fields are restored
        with their default settings. Required membership role: `team admin`.
        PBAC permission: `eventType.update`. Learn more about API access control
        at https://cal.com/docs/api-reference/v2/access-control. If accessed
        using an OAuth access token, the `TEAM_EVENT_TYPE_WRITE` scope is
        required.
      operationId: OrganizationsEventTypesController_2026_06_12_updateTeamEventType
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
              $ref: '#/components/schemas/UpdateTeamEventTypeInput_2026_06_12'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UpdateTeamEventTypeOutput_2026_06_12'
components:
  schemas:
    UpdateTeamEventTypeInput_2026_06_12:
      type: object
      properties:
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
            Discover the culinary wonders of the Argentina by making the best
            flan ever!
        slotInterval:
          type: number
          description: >-
            Number representing length of each slot when event is booked. By
            default it equal length of the event type.
                  If event length is 60 minutes then we would have slots 9AM, 10AM, 11AM etc. but if it was changed to 30 minutes then
                  we would have slots 9AM, 9:30AM, 10AM, 10:30AM etc. as the available times to book the 60 minute event.
        minimumBookingNotice:
          type: number
          description: >-
            Minimum number of minutes before the event that a booking can be
            made.
        beforeEventBuffer:
          type: number
          description: >-
            Extra time automatically blocked on your calendar before a meeting
            starts. This gives you time to prepare, review notes, or transition
            from your previous activity.
        afterEventBuffer:
          type: number
          description: >-
            Extra time automatically blocked on your calendar after a meeting
            ends. This gives you time to wrap up, add notes, or decompress
            before your next commitment.
        scheduleId:
          type: number
          description: >-
            If you want that this event has different schedule than user's
            default one you can specify it here.
        bookingLimitsCount:
          description: Limit how many times this event can be booked
          oneOf:
            - $ref: '#/components/schemas/BaseBookingLimitsCount_2024_06_14'
              title: Booking Count Limit
            - $ref: '#/components/schemas/Disabled_2024_06_14'
              title: Disabled
        bookerActiveBookingsLimit:
          description: >-
            Limit the number of active bookings a booker can make for this event
            type.
          oneOf:
            - $ref: '#/components/schemas/BookerActiveBookingsLimit_2024_06_14'
              title: Active Booking Limit
            - $ref: '#/components/schemas/Disabled_2024_06_14'
              title: Disabled
        onlyShowFirstAvailableSlot:
          type: boolean
          description: >-
            This will limit your availability for this event type to one slot
            per day, scheduled at the earliest available time.
        bookingLimitsDuration:
          description: Limit total amount of time that this event can be booked
          oneOf:
            - $ref: '#/components/schemas/BaseBookingLimitsDuration_2024_06_14'
              title: Booking Duration Limit
            - $ref: '#/components/schemas/Disabled_2024_06_14'
              title: Disabled
        bookingWindow:
          description: Limit how far in the future this event can be booked
          oneOf:
            - $ref: '#/components/schemas/BusinessDaysWindow_2024_06_14'
              title: Business Days
            - $ref: '#/components/schemas/CalendarDaysWindow_2024_06_14'
              title: Calendar Days
            - $ref: '#/components/schemas/RangeWindow_2024_06_14'
              title: Date Range
            - $ref: '#/components/schemas/Disabled_2024_06_14'
              title: Disabled
        offsetStart:
          type: number
          description: Offset timeslots shown to bookers by a specified number of minutes
        bookerLayouts:
          description: >-
            Should booker have week, month or column view. Specify default
            layout and enabled layouts user can pick.
          allOf:
            - $ref: '#/components/schemas/BookerLayouts_2024_06_14'
        confirmationPolicy:
          description: >-
            Specify how the booking needs to be manually confirmed before it is
            pushed to the integrations and a confirmation mail is sent.
          oneOf:
            - $ref: '#/components/schemas/BaseConfirmationPolicy_2024_06_14'
              title: Confirmation Required
            - $ref: '#/components/schemas/Disabled_2024_06_14'
              title: Disabled
        bookingProposalCount:
          type: number
          nullable: true
          description: >-
            Exact number of timeslots an attendee must propose for this event
            type. Set to null to use the default single-slot booking flow.
        recurrence:
          description: Create a recurring event type.
          oneOf:
            - $ref: '#/components/schemas/Recurrence_2024_06_14'
              title: Recurring Event
            - $ref: '#/components/schemas/Disabled_2024_06_14'
              title: Disabled
        requiresBookerEmailVerification:
          type: boolean
        skipAttendeeEmailDeliverabilityCheck:
          type: boolean
          description: >-
            When true, skips the MX deliverability check for attendee emails on
            booking. Format validation and watchlist still apply. Requires the
            editor to belong to an organization (including platform orgs).
        emailSettings:
          description: >-
            Email settings for this event type. Personal event types require an
            accepted organization membership; team event types require an
            organization team. This does not include emails sent by custom email
            workflows.
          allOf:
            - $ref: '#/components/schemas/EmailSettings_2024_06_14'
        hideCalendarNotes:
          type: boolean
        lockTimeZoneToggleOnBookingPage:
          type: boolean
        color:
          $ref: '#/components/schemas/EventTypeColor_2024_06_14'
        seats:
          description: Create an event type with multiple seats.
          oneOf:
            - $ref: '#/components/schemas/Seats_2024_06_14'
              title: Seated Event
            - $ref: '#/components/schemas/Disabled_2024_06_14'
              title: Disabled
        customName:
          type: string
          description: |-
            Customizable event name with valid variables:
                  {Link title}, {Event type title} (legacy), {Organiser}, {Scheduler}, {Location}, {Organiser first name},
                  {Scheduler first name}, {Scheduler last name}, {Event duration}, {LOCATION},
                  {HOST/ATTENDEE}, {HOST}, {ATTENDEE}, {USER}
          example: '{Link title} between {Organiser} and {Scheduler}'
        destinationCalendar:
          $ref: '#/components/schemas/DestinationCalendar_2024_06_14'
        useDestinationCalendarEmail:
          type: boolean
        hideCalendarEventDetails:
          type: boolean
        successRedirectUrl:
          type: string
          description: >-
            A valid URL where the booker will redirect to, once the booking is
            completed successfully
          example: https://masterchief.com/argentina/flan/video/9129412
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
          default: false
          description: >-
            Boolean to require authentication for booking this event type via
            api. If true, only authenticated users who are the event-type owner
            or org/team admin/owner can book this event type.
        disableCancelling:
          description: Settings for disabling cancelling of this event type.
          example:
            disabled: true
          allOf:
            - $ref: '#/components/schemas/DisableCancelling_2024_06_14'
        disableRescheduling:
          description: >-
            Settings for disabling rescheduling of this event type. Can be
            always disabled or disabled when less than X minutes before the
            meeting.
          example:
            disabled: false
            minutesBefore: 60
          allOf:
            - $ref: '#/components/schemas/DisableRescheduling_2024_06_14'
        interfaceLanguage:
          type: string
          description: >-
            Set preferred language for the booking interface. Use empty string
            for visitor's browser language (default).
          enum:
            - ''
            - en
            - ar
            - az
            - bg
            - bn
            - ca
            - cs
            - da
            - de
            - el
            - es
            - es-419
            - eu
            - et
            - fi
            - fr
            - he
            - hu
            - it
            - ja
            - km
            - ko
            - nl
            - 'no'
            - pl
            - pt-BR
            - pt
            - ro
            - ru
            - sk-SK
            - sr
            - sv
            - tr
            - uk
            - vi
            - zh-CN
            - zh-TW
        allowReschedulingPastBookings:
          type: boolean
          description: Enabling this option allows for past events to be rescheduled.
          default: false
        allowReschedulingCancelledBookings:
          type: boolean
          description: >-
            When enabled, users will be able to create a new booking when trying
            to reschedule a cancelled booking.
          default: false
        showOptimizedSlots:
          type: boolean
          description: Arrange time slots to optimize availability.
          default: false
        privateNoteEnabled:
          type: boolean
          description: >-
            When enabled, a private note calendar event is created alongside the
            booking with the resolved template as its description. Only visible
            to the host.
          default: false
        privateNoteMode:
          description: >-
            How private notes are delivered: as an additional host event or by
            sending separate host and guest invites.
          example: duplicate_event
          allOf:
            - $ref: '#/components/schemas/PrivateNoteMode'
        privateNoteTemplate:
          type: string
          description: >-
            Template for the private note content. Supports variables like
            {Attendee name}, {Link title}, {Event type title} (legacy),
            {Location}, {Host name}, {Event duration}, and custom booking field
            names.
          example: Meeting with {Attendee name} for {Link title}
        schedulingType:
          enum:
            - collective
            - roundRobin
          type: string
          example: collective
          description: >-
            The scheduling type for the team event - collective or roundRobin.
            ❗If you change scheduling type you must also provide `hosts` or
            `assignAllTeamMembers` in the request body, otherwise the event type
            will have no hosts - this is required because
                  in case of collective event type all hosts are mandatory but in case of round robin some or non can be mandatory so we can't predict how you want the hosts to be setup which is why you must provide that information.  If you want to convert round robin or collective into managed or managed into round robin or collective then you will have to create a new team event type and delete old one.
        hosts:
          description: >-
            Hosts contain specific team members you want to assign to this event
            type. To assign every current and future team member use
            `assignAllTeamMembers: true` and omit this field. As an exception,
            round robin event types accept `hosts` together with
            `assignAllTeamMembers: true` to mark specific team members as fixed
            hosts (entries with `mandatory: true`); non-mandatory entries are
            silently ignored in that combination because they would be added to
            the round robin pool by `assignAllTeamMembers` anyway. For platform
            customers the hosts can include userIds only of managed users.
          type: array
          items:
            $ref: '#/components/schemas/Host'
        assignAllTeamMembers:
          type: boolean
          description: >-
            If true, all current and future team members will be assigned to
            this event type. Mutually exclusive with `hosts` for collective and
            managed event types. For round robin event types, `hosts` may be
            provided alongside `assignAllTeamMembers: true` solely to designate
            fixed hosts via `mandatory: true` entries.
        locations:
          type: array
          description: >-
            Locations where the event will take place. If not provided, cal
            video link will be used as the location. Note: Setting a location to
            a conferencing app does not install the app - the app must already
            be installed. Via API, only Google Meet (google-meet), Microsoft
            Teams (office365-video), and Zoom (zoom) can be installed. Cal Video
            (cal-video) is installed by default. All other conferencing apps
            must be connected via the Cal.com web app and are not available for
            Platform plan customers. You can only set an event type location to
            an app that has already been installed or connected.
          items:
            oneOf:
              - $ref: '#/components/schemas/InputAddressLocation_2024_06_14'
                title: Address
              - $ref: '#/components/schemas/InputLinkLocation_2024_06_14'
                title: Link
              - $ref: '#/components/schemas/InputIntegrationLocation_2024_06_14'
                title: Integration
              - $ref: '#/components/schemas/InputPhoneLocation_2024_06_14'
                title: Phone
              - $ref: '#/components/schemas/InputAttendeeAddressLocation_2024_06_14'
                title: Attendee Address
              - $ref: '#/components/schemas/InputAttendeePhoneLocation_2024_06_14'
                title: Attendee Phone
              - $ref: '#/components/schemas/InputAttendeeDefinedLocation_2024_06_14'
                title: Attendee Defined
              - $ref: '#/components/schemas/InputOrganizersDefaultApp_2024_06_14'
                title: Organizer Default App
        rescheduleWithSameRoundRobinHost:
          type: boolean
          description: >-
            Rescheduled events will be assigned to the same host as initially
            scheduled.
        allowRRHostChoiceOnReschedule:
          type: boolean
          description: >-
            Let the person rescheduling choose between keeping the original host
            and letting round robin pick from the whole team. Requires
            rescheduleWithSameRoundRobinHost to be enabled.
        bookingFields:
          type: array
          description: >-
            Booking fields for the event type. Omit this property to keep the
            current fields. Provide an array to replace them, customize default
            fields, or add custom booking fields. At least one of `email` or
            `attendeePhoneNumber` must be visible and required. The array cannot
            be empty, contain duplicate default fields or custom slugs, or use a
            default field's slug for a custom field. Omitted default fields are
            restored with their default settings. Workflow-added fields are
            read-only and ignored.
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
    UpdateTeamEventTypeOutput_2026_06_12:
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
            - $ref: '#/components/schemas/TeamEventTypeOutput_2026_06_12'
              title: Team Event Type
            - title: Team Event Types (array)
              type: array
              items:
                $ref: '#/components/schemas/TeamEventTypeOutput_2026_06_12'
      required:
        - status
        - data
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
    BookerActiveBookingsLimit_2024_06_14:
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
        disabled:
          type: boolean
          default: false
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
          minItems: 1
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
    EventTypeColor_2024_06_14:
      type: object
      properties:
        lightThemeHex:
          type: string
          pattern: ^#?([0-9A-F]{3}|[0-9A-F]{4}|[0-9A-F]{6}|[0-9A-F]{8})$
          description: Color used for event types in light theme
          example: '#292929'
        darkThemeHex:
          type: string
          pattern: ^#?([0-9A-F]{3}|[0-9A-F]{4}|[0-9A-F]{6}|[0-9A-F]{8})$
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
          default: false
        disableRecordingForGuests:
          type: boolean
          description: If true, the guests will not be able to record the meeting
          default: false
        redirectUrlOnExit:
          type: string
          nullable: true
          format: uri
          description: URL to which participants are redirected when they exit the call
        enableAutomaticRecordingForOrganizer:
          type: boolean
          description: >-
            If true, enables the automatic recording for the event when
            organizer joins the call
          default: false
        enableAutomaticTranscription:
          type: boolean
          description: >-
            If true, enables the automatic transcription for the event whenever
            someone joins the call
          default: false
        disableTranscriptionForGuests:
          type: boolean
          description: >-
            If true, the guests will not be able to receive transcription of the
            meeting
          default: false
        disableTranscriptionForOrganizer:
          type: boolean
          description: >-
            If true, the organizer will not be able to receive transcription of
            the meeting
          default: false
        hideTranscriptionForGuests:
          type: boolean
          description: >-
            If true, guests will not see live transcription captions during the
            meeting
          default: false
        hideTranscriptionForOrganizer:
          type: boolean
          description: >-
            If true, organizers will not see live transcription captions during
            the meeting
          default: false
        sendTranscriptionEmails:
          type: boolean
          description: >-
            Send emails with the transcription of the Cal Video after the
            meeting ends.
          default: true
        disableAttendeeRecordingDownloadEmail:
          type: boolean
          description: >-
            If true, attendees will not receive the Cal Video recording download
            email for this event type. Defaults to false. Organization guest
            notifications can still prevent this email from sending.
          default: false
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
    DisableCancelling_2024_06_14:
      type: object
      properties:
        disabled:
          type: boolean
          description: If true, cancelling is always disabled for this event type.
          example: true
    DisableRescheduling_2024_06_14:
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
            Disable rescheduling when less than the specified number of minutes
            before the meeting. If set, `disabled` should be false or undefined.
          example: 60
    PrivateNoteMode:
      type: string
      enum:
        - duplicate_event
        - separate_events
      description: >-
        How private notes are delivered: as an additional host event or by
        sending separate host and guest invites.
    Host:
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
          default: medium
          enum:
            - lowest
            - low
            - medium
            - high
            - highest
          type: string
      required:
        - userId
    InputAddressLocation_2024_06_14:
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
    InputLinkLocation_2024_06_14:
      type: object
      properties:
        type:
          type: string
          example: link
          description: only allowed value for type is `link`
        link:
          type: string
          format: uri
          example: https://customvideo.com/join/123456
        public:
          type: boolean
      required:
        - type
        - link
        - public
    InputIntegrationLocation_2024_06_14:
      type: object
      properties:
        type:
          type: string
          example: integration
          description: only allowed value for type is `integration`
        integration:
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
          type: string
          example: cal-video
      required:
        - type
        - integration
    InputPhoneLocation_2024_06_14:
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
    InputAttendeeAddressLocation_2024_06_14:
      type: object
      properties:
        type:
          type: string
          example: attendeeAddress
          description: only allowed value for type is `attendeeAddress`
      required:
        - type
    InputAttendeePhoneLocation_2024_06_14:
      type: object
      properties:
        type:
          type: string
          example: attendeePhone
          description: only allowed value for type is `attendeePhone`
      required:
        - type
    InputAttendeeDefinedLocation_2024_06_14:
      type: object
      properties:
        type:
          type: string
          example: attendeeDefined
          description: only allowed value for type is `attendeeDefined`
      required:
        - type
    InputOrganizersDefaultApp_2024_06_14:
      type: object
      properties:
        type:
          type: string
          example: organizersDefaultApp
          description: only allowed value for type is `organizersDefaultApp`
      required:
        - type
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
    TeamEventTypeOutput_2026_06_12:
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
                title: Address
              - $ref: '#/components/schemas/OutputLinkLocation_2024_06_14'
                title: Link
              - $ref: '#/components/schemas/OutputIntegrationLocation_2024_06_14'
                title: Integration
              - $ref: '#/components/schemas/OutputPhoneLocation_2024_06_14'
                title: Phone
              - $ref: >-
                  #/components/schemas/OutputOrganizersDefaultAppLocation_2024_06_14
                title: Organizer Default App
              - $ref: '#/components/schemas/OutputUnknownLocation_2024_06_14'
                title: Unknown
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
          type: object
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
              title: Booking Count Limit
            - $ref: '#/components/schemas/Disabled_2024_06_14'
              title: Disabled
        bookerActiveBookingsLimit:
          $ref: '#/components/schemas/BookerActiveBookingsLimitOutput_2024_06_14'
        onlyShowFirstAvailableSlot:
          type: boolean
        bookingLimitsDuration:
          oneOf:
            - $ref: '#/components/schemas/BaseBookingLimitsDuration_2024_06_14'
              title: Booking Duration Limit
            - $ref: '#/components/schemas/Disabled_2024_06_14'
              title: Disabled
        bookingWindow:
          type: array
          description: Limit how far in the future this event can be booked
          items:
            oneOf:
              - $ref: '#/components/schemas/BusinessDaysWindow_2024_06_14'
                title: Business Days
              - $ref: '#/components/schemas/CalendarDaysWindow_2024_06_14'
                title: Calendar Days
              - $ref: '#/components/schemas/RangeWindow_2024_06_14'
                title: Date Range
        bookerLayouts:
          $ref: '#/components/schemas/BookerLayouts_2024_06_14'
        confirmationPolicy:
          oneOf:
            - $ref: '#/components/schemas/BaseConfirmationPolicy_2024_06_14'
              title: Confirmation Required
            - $ref: '#/components/schemas/Disabled_2024_06_14'
              title: Disabled
        bookingProposalCount:
          type: number
          nullable: true
          description: >-
            Exact number of timeslots an attendee must propose for this event
            type. Null uses the default single-slot booking flow.
        requiresBookerEmailVerification:
          type: boolean
        skipAttendeeEmailDeliverabilityCheck:
          type: boolean
          description: >-
            When true, the MX deliverability check for attendee emails is
            skipped on booking. Format validation and watchlist still apply.
            Org-only (including platform orgs).
        emailSettings:
          description: >-
            Email settings for this event type. Personal event types require an
            accepted organization membership; team event types require an
            organization team. This does not include emails sent by custom email
            workflows.
          allOf:
            - $ref: '#/components/schemas/EmailSettings_2024_06_14'
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
          nullable: true
          description: >-
            How private notes are delivered: as an additional host event or by
            sending separate host and guest invites.
          allOf:
            - $ref: '#/components/schemas/PrivateNoteMode'
        privateNoteTemplate:
          type: string
          nullable: true
          description: >-
            Template for the private note content. Supports variables like
            {Attendee name}, {Link title}, {Event type title} (legacy),
            {Location}, {Host name}, {Event duration}, and custom booking field
            names.
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
          nullable: true
          enum:
            - roundRobin
            - collective
            - managed
          type: string
        team:
          $ref: '#/components/schemas/EventTypeTeam'
        rescheduleWithSameRoundRobinHost:
          type: boolean
          description: >-
            Rescheduled events will be assigned to the same host as initially
            scheduled.
        allowRRHostChoiceOnReschedule:
          type: boolean
          description: >-
            Let the person rescheduling choose between keeping the original host
            and letting round robin pick from the whole team.
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
        - id
        - lengthInMinutes
        - title
        - slug
        - description
        - locations
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
        - bookingFields
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
          format: uri
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
          type: string
          example: cal-video
        link:
          type: string
          format: uri
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
          default: medium
          enum:
            - lowest
            - low
            - medium
            - high
            - highest
          type: string
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