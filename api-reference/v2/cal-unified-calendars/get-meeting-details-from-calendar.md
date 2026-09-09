> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get meeting details from calendar

> Returns detailed information about a meeting including attendance metrics. If accessed using an OAuth access token, the `APPS_READ` scope is required.



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/calendars/{calendar}/event/{eventUid}
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
  /v2/calendars/{calendar}/event/{eventUid}:
    get:
      tags:
        - Cal Unified Calendars
      summary: Get meeting details from calendar
      description: >-
        Returns detailed information about a meeting including attendance
        metrics. If accessed using an OAuth access token, the `APPS_READ` scope
        is required.
      operationId: CalUnifiedCalendarsController_getCalendarEventDetails
      parameters:
        - name: calendar
          required: true
          in: path
          schema:
            type: string
            enum:
              - google
        - name: eventUid
          required: true
          in: path
          description: >-
            The Google Calendar event ID. You can retrieve this by getting
            booking references from the following endpoints:


            - For team events:
            https://cal.com/docs/api-reference/v2/orgs-teams-bookings/get-booking-references-for-a-booking


            - For user events:
            https://cal.com/docs/api-reference/v2/bookings/get-booking-references-for-a-booking
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
                $ref: '#/components/schemas/GetUnifiedCalendarEventOutput'
components:
  schemas:
    GetUnifiedCalendarEventOutput:
      type: object
      properties:
        status:
          type: string
          example: success
          enum:
            - success
            - error
        data:
          $ref: '#/components/schemas/UnifiedCalendarEventOutput'
      required:
        - status
        - data
    UnifiedCalendarEventOutput:
      type: object
      properties:
        start:
          type: object
          properties:
            time:
              format: date-time
              type: string
            timeZone:
              type: string
          description: Start date and time of the calendar event with timezone information
        end:
          type: object
          properties:
            time:
              format: date-time
              type: string
            timeZone:
              type: string
          description: End date and time of the calendar event with timezone information
        id:
          type: string
          description: Unique identifier of the calendar event
        title:
          type: string
          description: Title of the calendar event
        description:
          type: string
          nullable: true
          description: Detailed description of the calendar event
        locations:
          type: array
          items:
            oneOf:
              - $ref: '#/components/schemas/CalendarEventVideoLocation'
              - $ref: '#/components/schemas/CalendarEventPhoneLocation'
              - $ref: '#/components/schemas/CalendarEventSipLocation'
              - $ref: '#/components/schemas/CalendarEventMoreLocation'
            discriminator:
              propertyName: type
          nullable: true
          description: Conference locations with entry points (video, phone, sip, more)
        attendees:
          nullable: true
          description: List of attendees with their response status
          type: array
          items:
            $ref: '#/components/schemas/CalendarEventAttendee'
        status:
          $ref: '#/components/schemas/CalendarEventStatus'
          nullable: true
          example: accepted
        hosts:
          nullable: true
          description: Information about the event hosts (organizers)
          type: array
          items:
            $ref: '#/components/schemas/CalendarEventHost'
        calendarEventOwner:
          nullable: true
          description: >-
            The calendar account that owns this event. This is the primary
            calendar where the event is stored and cannot be modified without
            appropriate permissions. Changing this would require moving the
            event to a different calendar
          allOf:
            - $ref: '#/components/schemas/calendarEventOwner'
        source:
          $ref: '#/components/schemas/CalendarSource'
          example: google
      required:
        - start
        - end
        - id
        - title
        - source
    CalendarEventVideoLocation:
      type: object
      properties:
        type:
          type: string
          default: video
          enum:
            - video
          description: Indicates this is a video conference location
        url:
          type: string
          description: URL for joining the video conference
        label:
          type: string
          nullable: true
          description: Display name for the video conference
        password:
          type: string
          nullable: true
          description: Password required to join the video conference
        meetingCode:
          type: string
          nullable: true
          description: Meeting code or ID required to join the conference
        accessCode:
          type: string
          nullable: true
          description: Access code required to join the conference
      required:
        - type
        - url
    CalendarEventPhoneLocation:
      type: object
      properties:
        type:
          type: string
          default: phone
          enum:
            - phone
          description: Indicates this is a phone conference location
        url:
          type: string
          description: Phone number or URL for dialing into the conference
        label:
          type: string
          nullable: true
          description: Display name for the phone conference
        pin:
          type: string
          nullable: true
          description: PIN number required for the phone conference
        password:
          type: string
          nullable: true
          description: Password required for the phone conference
        accessCode:
          type: string
          nullable: true
          description: Access code required for the phone conference
        regionCode:
          type: string
          nullable: true
          description: Country/region code for the phone number
      required:
        - type
        - url
    CalendarEventSipLocation:
      type: object
      properties:
        type:
          type: string
          default: sip
          enum:
            - sip
          description: >-
            Indicates this is a SIP (Session Initiation Protocol) conference
            location
        url:
          type: string
          description: SIP URL for joining the conference
        label:
          type: string
          nullable: true
          description: Display name for the SIP conference
        pin:
          type: string
          nullable: true
          description: PIN number required for the SIP conference
        password:
          type: string
          nullable: true
          description: Password required for the SIP conference
      required:
        - type
        - url
    CalendarEventMoreLocation:
      type: object
      properties:
        type:
          type: string
          default: more
          enum:
            - more
          description: Indicates this is an additional conference location type
        url:
          type: string
          description: URL for accessing this location
        label:
          type: string
          nullable: true
          description: Display name for this location
      required:
        - type
        - url
    CalendarEventAttendee:
      type: object
      properties:
        email:
          type: string
          description: Email address of the attendee
        name:
          type: string
          description: Display name of the attendee
        responseStatus:
          $ref: '#/components/schemas/CalendarEventResponseStatus'
          nullable: true
          example: accepted
        self:
          type: boolean
          nullable: true
          description: Indicates if this attendee is the current user
        optional:
          type: boolean
          nullable: true
          description: Indicates if this attendee's attendance is optional
        host:
          type: boolean
          nullable: true
          description: Indicates if this attendee is the host
      required:
        - email
    CalendarEventStatus:
      type: string
      description: Status of the event (accepted, pending, declined, cancelled)
      enum:
        - accepted
        - pending
        - declined
        - cancelled
    CalendarEventHost:
      type: object
      properties:
        email:
          type: string
          description: Email address of the event host
        name:
          type: string
          nullable: true
          description: Display name of the event host
        responseStatus:
          $ref: '#/components/schemas/CalendarEventResponseStatus'
          nullable: true
          example: accepted
      required:
        - email
    calendarEventOwner:
      type: object
      properties:
        email:
          type: string
          description: Email address of the event host
        name:
          type: string
          nullable: true
          description: Display name of the event host
      required:
        - email
    CalendarSource:
      type: string
      description: >-
        Calendar integration source (e.g., Google Calendar, Office 365, Apple
        Calendar). Currently only Google Calendar is supported.
      enum:
        - google
        - office365
        - apple
    CalendarEventResponseStatus:
      type: string
      description: Response status of the attendee
      enum:
        - accepted
        - pending
        - declined
        - needsAction

````