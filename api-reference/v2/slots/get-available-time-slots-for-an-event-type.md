> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get available time slots for an event type

> 
      There are 4 ways to get available slots for event type of an individual user:

      1. By event type id. Example '/v2/slots?eventTypeId=10&start=2050-09-05&end=2050-09-06&timeZone=Europe/Rome'

      2. By event type slug + username. Example '/v2/slots?eventTypeSlug=intro&username=bob&start=2050-09-05&end=2050-09-06'

      3. By event type slug + username + organization slug when searching within an organization. Example '/v2/slots?organizationSlug=org-slug&eventTypeSlug=intro&username=bob&start=2050-09-05&end=2050-09-06'

      4. By usernames only (used for dynamic event type - there is no specific event but you want to know when 2 or more people are available). Example '/v2/slots?usernames=alice,bob&username=bob&organizationSlug=org-slug&start=2050-09-05&end=2050-09-06'. As you see you also need to provide the slug of the organization to which each user in the 'usernames' array belongs.

      And 3 ways to get available slots for team event type:

      1. By team event type id. Example '/v2/slots?eventTypeId=10&start=2050-09-05&end=2050-09-06&timeZone=Europe/Rome'.
         **Note for managed event types**: Managed event types are templates that create individual child event types for each team member. You cannot fetch slots for the parent managed event type directly. Instead, you must:
         - Find the child event type IDs (the ones assigned to specific users)
         - Use those child event type IDs to fetch slots as individual user event types using as described in the individual user section above.

      2. By team event type slug + team slug. Example '/v2/slots?eventTypeSlug=intro&teamSlug=team-slug&start=2050-09-05&end=2050-09-06'

      3. By team event type slug + team slug + organization slug when searching within an organization. Example '/v2/slots?organizationSlug=org-slug&eventTypeSlug=intro&teamSlug=team-slug&start=2050-09-05&end=2050-09-06'

      All of them require "start" and "end" query parameters which define the time range for which available slots should be checked.
      Optional parameters are:
      - timeZone: Time zone in which the available slots should be returned. Defaults to UTC.
      - duration: Only use for event types that allow multiple durations or for dynamic event types. If not passed for multiple duration event types defaults to default duration. For dynamic event types defaults to 30 aka each returned slot is 30 minutes long. So duration=60 means that returned slots will be each 60 minutes long.
      - format: Format of the slots. By default return is an object where each key is date and value is array of slots as string. If you want to get start and end of each slot use "range" as value.
      - bookingUidToReschedule: When rescheduling an existing booking, provide the booking's unique identifier to exclude its time slot from busy time calculations. This ensures the original booking time appears as available for rescheduling.

       <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>
      



## OpenAPI

````yaml /api-reference/v2/openapi.json get /v2/slots
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
  /v2/slots:
    get:
      tags:
        - Slots
      summary: Get available time slots for an event type
      description: |2-

              There are 4 ways to get available slots for event type of an individual user:

              1. By event type id. Example '/v2/slots?eventTypeId=10&start=2050-09-05&end=2050-09-06&timeZone=Europe/Rome'

              2. By event type slug + username. Example '/v2/slots?eventTypeSlug=intro&username=bob&start=2050-09-05&end=2050-09-06'

              3. By event type slug + username + organization slug when searching within an organization. Example '/v2/slots?organizationSlug=org-slug&eventTypeSlug=intro&username=bob&start=2050-09-05&end=2050-09-06'

              4. By usernames only (used for dynamic event type - there is no specific event but you want to know when 2 or more people are available). Example '/v2/slots?usernames=alice,bob&username=bob&organizationSlug=org-slug&start=2050-09-05&end=2050-09-06'. As you see you also need to provide the slug of the organization to which each user in the 'usernames' array belongs.

              And 3 ways to get available slots for team event type:

              1. By team event type id. Example '/v2/slots?eventTypeId=10&start=2050-09-05&end=2050-09-06&timeZone=Europe/Rome'.
                 **Note for managed event types**: Managed event types are templates that create individual child event types for each team member. You cannot fetch slots for the parent managed event type directly. Instead, you must:
                 - Find the child event type IDs (the ones assigned to specific users)
                 - Use those child event type IDs to fetch slots as individual user event types using as described in the individual user section above.

              2. By team event type slug + team slug. Example '/v2/slots?eventTypeSlug=intro&teamSlug=team-slug&start=2050-09-05&end=2050-09-06'

              3. By team event type slug + team slug + organization slug when searching within an organization. Example '/v2/slots?organizationSlug=org-slug&eventTypeSlug=intro&teamSlug=team-slug&start=2050-09-05&end=2050-09-06'

              All of them require "start" and "end" query parameters which define the time range for which available slots should be checked.
              Optional parameters are:
              - timeZone: Time zone in which the available slots should be returned. Defaults to UTC.
              - duration: Only use for event types that allow multiple durations or for dynamic event types. If not passed for multiple duration event types defaults to default duration. For dynamic event types defaults to 30 aka each returned slot is 30 minutes long. So duration=60 means that returned slots will be each 60 minutes long.
              - format: Format of the slots. By default return is an object where each key is date and value is array of slots as string. If you want to get start and end of each slot use "range" as value.
              - bookingUidToReschedule: When rescheduling an existing booking, provide the booking's unique identifier to exclude its time slot from busy time calculations. This ensures the original booking time appears as available for rescheduling.

               <Note>Please make sure to pass in the cal-api-version header value as mentioned in the Headers section. Not passing the correct value will default to an older version of this endpoint.</Note>
              
      operationId: SlotsController_2024_09_04_getAvailableSlots
      parameters:
        - name: cal-api-version
          in: header
          description: >-
            Must be set to 2024-09-04. If not set to this value, the endpoint
            will default to an older version.
          required: true
          schema:
            type: string
            example: '2024-09-04'
            default: '2024-09-04'
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
        - name: start
          required: true
          in: query
          description: |2-

                  Time starting from which available slots should be checked.

                  Must be in UTC timezone as ISO 8601 datestring.

                  You can pass date without hours which defaults to start of day or specify hours:
                  2024-08-13 (will have hours 00:00:00 aka at very beginning of the date) or you can specify hours manually like 2024-08-13T09:00:00Z.
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
                2024-08-20 (will have hours 23:59:59 aka at the very end of the date) or you can specify hours manually like 2024-08-20T18:00:00Z.
          schema:
            example: '2050-09-06'
            type: string
        - name: organizationSlug
          required: false
          in: query
          description: >-
            The slug of the organization to which user with username belongs or
            team with teamSlug belongs.
          schema:
            example: org-slug
            type: string
        - name: teamSlug
          required: false
          in: query
          description: >-
            The slug of the team who owns event type with eventTypeSlug - used
            when slots are checked for team event type.
          schema:
            example: team-slug
            type: string
        - name: username
          required: false
          in: query
          description: >-
            The username of the user who owns event type with eventTypeSlug -
            used when slots are checked for individual user event type.
          schema:
            example: bob
            type: string
        - name: eventTypeSlug
          required: false
          in: query
          description: >-
            The slug of the event type for which available slots should be
            checked. If slug is provided then username or teamSlug must be
            provided too and if relevant organizationSlug too.
          schema:
            example: event-type-slug
            type: string
        - name: eventTypeId
          required: false
          in: query
          description: >-
            The ID of the event type for which available slots should be
            checked.
          schema:
            example: '100'
            type: number
        - name: usernames
          required: false
          in: query
          description: >-
            The usernames for which available slots should be checked separated
            by a comma.

                Checking slots by usernames is used mainly for dynamic events where there is no specific event but we just want to know when 2 or more people are available.

                Must contain at least 2 usernames.
          schema:
            example: alice,bob
            type: string
        - name: format
          required: false
          in: query
          description: >-
            Format of slot times in response. Use 'range' to get start and end
            times. Use 'time' or omit this query parameter to get only start
            time.
          schema:
            example: range
            type: string
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
        - name: timeZone
          required: false
          in: query
          description: >-
            Time zone in which the available slots should be returned. Defaults
            to UTC.
          schema:
            type: string
            example: Europe/Rome
      responses:
        '200':
          description: >-
            A map of available slots indexed by date, where each date is
            associated with an array of time slots. If format=range is
            specified, each slot will be an object with start and end properties
            denoting start and end of the slot.
                  For seated slots each object will have attendeesCount and bookingUid properties.
                  If no slots are available, the data field will be an empty object {}.
          content:
            application/json:
              schema:
                oneOf:
                  - type: object
                    title: Default format (or with format=time)
                    additionalProperties:
                      type: array
                      items:
                        type: string
                    example:
                      status: success
                      data:
                        '2050-09-05':
                          - start: '2050-09-05T09:00:00.000+02:00'
                          - start: '2050-09-05T10:00:00.000+02:00'
                        '2050-09-06':
                          - start: '2050-09-06T09:00:00.000+02:00'
                          - start: '2050-09-06T10:00:00.000+02:00'
                  - type: object
                    title: Range format (when format=range)
                    additionalProperties:
                      type: array
                      items:
                        type: object
                        properties:
                          start:
                            type: string
                          end:
                            type: string
                    example:
                      status: success
                      data:
                        '2050-09-05':
                          - start: '2050-09-05T09:00:00.000+02:00'
                            end: '2050-09-05T10:00:00.000+02:00'
                          - start: '2050-09-05T10:00:00.000+02:00'
                            end: '2050-09-05T11:00:00.000+02:00'
                        '2050-09-06':
                          - start: '2050-09-06T09:00:00.000+02:00'
                            end: '2050-09-06T10:00:00.000+02:00'
                          - start: '2050-09-06T10:00:00.000+02:00'
                            end: '2050-09-06T11:00:00.000+02:00'

````