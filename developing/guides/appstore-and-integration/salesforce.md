> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Salesforce integration

> Configure how Cal.com syncs booking data with Salesforce contacts, leads, and events.

The Salesforce integration lets you automatically sync booking data to your Salesforce CRM. When connected, Cal.com creates Salesforce events linked to contacts or leads, and can write custom field values at different stages of the booking lifecycle.

## Prerequisites

* A Salesforce account with API access
* The Salesforce app installed and connected in your Cal.com instance

## Event type settings

After connecting Salesforce, you can configure per-event-type settings by navigating to the event type's **Apps** tab and expanding the Salesforce section.

### Attendee record type

Choose how Cal.com identifies attendees in Salesforce:

* **Contact** — Look up or create a Contact record for the attendee
* **Lead** — Look up or create a Lead record for the attendee
* **Contact under Account** — Look up the Contact under their Account

### Write to event record on booking

Enable **On booking, write to the event object** to set custom field values on the Salesforce event whenever a booking is created. Add field name and value pairs to configure which event fields are updated.

### Write to contact or lead record on booking

Enable **On booking, write to a custom field on the attendee record** to update fields on the attendee's Contact or Lead record whenever a booking is created. For each field you configure, you can set:

* **Field name** — The Salesforce API name of the field to write to
* **Field type** — The data type (text, date, datetime, phone, checkbox, picklist, textarea, or custom)
* **Value** — The value to write. Date fields support dynamic values like `booking_start_date`, `booking_created_date`, or `booking_cancel_date`. Text values can also embed booking context tokens — see [Context tokens in field values](#context-tokens-in-field-values)
* **When to write** — Choose between writing on every booking or only when the field is empty

### Write to event record on cancellation

Enable **On cancelled booking, write to event record instead of deleting event** to preserve the Salesforce event when a booking is cancelled. Instead of deleting the event, Cal.com writes your configured field values to it. This is useful when you want to keep a record of cancelled meetings in Salesforce.

For each field, configure the field name, type, value, and write condition, the same as for booking-time writes.

<Note>
  When this option is disabled, Cal.com deletes the Salesforce event on cancellation.
</Note>

### Write to contact or lead record on cancellation

Enable **On cancelled booking, write to a custom field on the attendee record** to update fields on the attendee's Contact or Lead record when a booking is cancelled. This lets you track cancellation status directly on the person record in Salesforce.

Cal.com identifies the correct contact or lead using the Salesforce event's `WhoId` field, which links back to the person originally assigned when the booking was created.

<Note>
  This feature works alongside the "write to record on booking" option. You can configure both independently — for example, writing a booking date on creation and a cancellation status on cancellation.
</Note>

#### Enable write-to-record on cancellation

<Steps>
  <Step title="Open event type settings">
    Go to **Event Types**, select the event type you want to configure, and open the **Apps** tab.
  </Step>

  <Step title="Open Salesforce settings">
    Find the Salesforce app card and expand its settings.
  </Step>

  <Step title="Enable the cancellation toggle">
    Turn on **On cancelled booking, write to a custom field on the attendee contact/lead record**.
  </Step>

  <Step title="Configure fields">
    Add one or more field mappings. For each field, specify:

    * **Field name** — The Salesforce API name of the field on the contact or lead object (for example, `Last_Booking_Status__c`)
    * **Field type** — The data type (text, date, datetime, phone, checkbox, picklist, textarea, or custom)
    * **Value** — The value to write when a booking is cancelled. For date fields, you can use dynamic values like `booking_cancel_date` to automatically populate the cancellation date
    * **When to write** — Choose between writing on every cancellation or only when the field is empty
  </Step>

  <Step title="Save">
    Save your event type. The configured fields update on the attendee's Salesforce record whenever a booking of this type is cancelled.
  </Step>
</Steps>

#### Example: tracking cancellation status and date

A sales team wants to track when prospects cancel discovery calls:

1. In Salesforce, add custom fields to the Contact object (e.g., `Last_Booking_Status__c` and `Last_Cancel_Date__c`)
2. In Cal.com, open the "Discovery Call" event type's Salesforce settings
3. Enable **On cancelled booking, write to a custom field on the attendee contact/lead record**
4. Add a first field mapping:
   * Field name: `Last_Booking_Status__c`
   * Field type: Text
   * Value: `Cancelled`
   * When to write: Every cancellation
5. Add a second field mapping:
   * Field name: `Last_Cancel_Date__c`
   * Field type: Date
   * Value: `booking_cancel_date`
   * When to write: Every cancellation

When a prospect cancels, their Salesforce contact record automatically updates with the cancellation status and date.

### Create records on lead or contact owner fallback

When a round-robin event type is configured to **Book directly with attendee owner**, Cal.com looks up the matched Contact, Lead, or Account owner and routes the booking to that host. If no owner is found, the fallback path runs and standard round-robin assignment takes over. You can also configure Cal.com to **create Salesforce records on this fallback**, so a new Lead, Contact, or custom object is created for the attendee whenever the owner lookup misses.

Use this when you want every booking to leave a paper trail in Salesforce — even when the attendee has no existing owner mapping — without needing your reps to create records manually after the fact.

<Steps>
  <Step title="Open Salesforce settings">
    Navigate to the event type's **Apps** tab and expand the Salesforce section.
  </Step>

  <Step title="Enable the fallback record toggle">
    Turn on **On lead or contact owner fallback, create records in Salesforce**.
  </Step>

  <Step title="Add one or more fallback records">
    For each record you want created, select the Salesforce object (for example, Lead, Contact, or a custom object) and configure the field mappings that populate it. You can add multiple records — for example, create a Lead and a related custom object in a single fallback.
  </Step>

  <Step title="Configure field mappings">
    For each field on the fallback record, specify:

    * **Field name** — The Salesforce API name of the field
    * **Field type** — The data type. In addition to the standard types (text, date, datetime, phone, checkbox, picklist, textarea, custom), fallback records support **Account lookup** for fields that reference the resolved Salesforce Account
    * **Value** — A literal value, a dynamic booking value, or a string with [context tokens](#context-tokens-in-field-values). For **Account lookup** fields, Cal.com writes the id of the Account resolved from the attendee's email domain
  </Step>

  <Step title="Optionally skip when the booking is already with the account owner">
    Enable **Skip if booking with account owner** on any record to suppress creation when the resolved host is already the account owner. This avoids duplicate records for bookings that were routed to the "right" rep to begin with.
  </Step>

  <Step title="Save">
    Save your event type. On future bookings that fall through owner lookup, Cal.com creates each configured record and links Account lookup fields to the matched Account.
  </Step>
</Steps>

<Note>
  If Salesforce returns an error while resolving the Account or its ownership, Cal.com treats the booking as "not owned by the host" and continues creating the fallback records. Salesforce failures never block booking creation.
</Note>

### Context tokens in field values

Text-based field values in write-to-record and fallback-record configurations can embed context tokens that Cal.com replaces at booking time. Tokens use curly braces and can appear anywhere in the string, including alongside literal text.

| Token                 | Replaced with                                          |
| --------------------- | ------------------------------------------------------ |
| `{account_id}`        | Salesforce id of the Account resolved for the attendee |
| `{organizer_user_id}` | Cal.com user id of the booking's organizer (host)      |
| `{booking_uid}`       | Cal.com booking uid                                    |

```text Value examples theme={null}
Booked via Cal.com — organizer {organizer_user_id}
https://app.cal.com/booking/{booking_uid}
Account: {account_id} / Rep: {organizer_user_id}
```

<Note>
  Values that contain only a brace-only literal (for example, `{}`) are treated as static text. Any other token — including hyphenated identifiers from routing form questions such as `{my-question}` — is resolved at booking time.
</Note>

### Record type filtering

Salesforce objects can have multiple Record Types — for example, Contacts may include both "Business Contact" and "Person Account" types. You can exclude specific Record Types so that Cal.com only looks up or creates records of the types you want.

<Steps>
  <Step title="Open Salesforce settings">
    Navigate to the event type's **Apps** tab and expand the Salesforce section.
  </Step>

  <Step title="Find the record type exclusion section">
    Below the attendee record type selector, look for the **Exclude Record Types** setting.
  </Step>

  <Step title="Select record types to exclude">
    Cal.com fetches the available Record Types from your Salesforce org. Select any Record Types you want to skip during contact or lead lookups. Records matching excluded types are filtered out of query results.
  </Step>

  <Step title="Save">
    Save your event type. Future bookings will only match records whose Record Type is not in the exclusion list.
  </Step>
</Steps>

<Note>
  Record type matching is case-insensitive. This setting applies to both lookups and record creation — Cal.com will not create records with an excluded Record Type.
</Note>

### Field mapping validation

Cal.com validates your field mappings when you save event type settings, catching configuration errors before they affect live bookings. Validation checks include:

* **Checkbox fields** must map to a boolean value
* **Date fields** must reference a valid date source (for example, `booking_start_date`, `booking_created_date`, or `booking_cancel_date`)
* **Text, phone, picklist, and custom fields** must have a non-empty string value

If a mapping is invalid, an inline error appears next to the field so you can correct it before saving.

### Sync error notifications

When a Salesforce sync fails at booking time — for example, due to a permission error or an invalid field — Cal.com stores the error and displays a diagnostic notification on the Salesforce settings tab. The notification includes:

* The error code and message
* Which fields were dropped from the sync
* A timestamp of when the error occurred

This helps you identify and fix integration issues without needing to check Salesforce logs.

### Fuzzy domain matching

By default, Cal.com matches attendee email domains to Salesforce Account `Website` fields using exact domain matching. When fuzzy domain matching is enabled, Cal.com also matches across top-level domain variants — for example, an attendee with an `@acme.com` email will match a Salesforce Account whose website is `acme.co.uk`.

This is useful when your Salesforce Accounts use regional domains (`.co.uk`, `.de`, `.com.au`) but your contacts book meetings using a different TLD.

Fuzzy domain matching is a per-credential toggle — enable it in your Salesforce connection settings, and it applies to all event types using that credential.

<Note>
  The fuzzy matching resolution follows a waterfall: exact domain match first, then normalized website comparison, then contact email domain lookup. This ensures precise matches are always preferred over fuzzy ones.
</Note>

### Show CRM contact owner banner on booking page

Enable **Show banner with CRM contact owner on booking page** to display a banner on the booking page identifying the Salesforce contact owner assigned to the attendee. Use this to reassure attendees that they are booking with the account owner already on file, or to make internal handoffs more transparent.

The banner only appears when Cal.com resolves a Salesforce contact owner for the attendee — for example, on round-robin event types where **Book directly with attendee owner** matches a Contact, Lead, or Account owner. If no owner is resolved, no banner is shown.

You can also opt into the banner from a routed URL by appending `cal.showCrmOwnerBanner=true` to the booking link, which is useful when driving traffic from a routing form or external system that already knows the attendee's CRM owner.

### Additional settings

| Setting                                                | Description                                                                                           |
| ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| **Ignore guests**                                      | Only process the primary attendee, not additional guests                                              |
| **Skip contact creation**                              | Do not create a new Contact if one doesn't exist (Contact mode only)                                  |
| **Check for existing contact**                         | When using Lead mode, also check if a Contact exists before creating a Lead                           |
| **Create contact under account**                       | When creating contacts, link them to the matching Account                                             |
| **Change record owner on booking**                     | Reassign the Contact or Lead owner to a specified user when a booking is made                         |
| **Send no-show attendee data**                         | Write attendee no-show status to a field on the Salesforce event object                               |
| **Book directly with attendee owner**                  | For round-robin event types, skip round-robin logic and route directly to the Salesforce record owner |
| **Show banner with CRM contact owner on booking page** | Show a banner on the booking page identifying the resolved Salesforce contact owner                   |

## Routing form options

When you add a route to a Cal.com routing form, the Salesforce app exposes routing options that decide which host receives the booking based on Salesforce data. Configure them from the route's settings panel under the Salesforce section.

### Route to a user that matches a lookup field on an account

Use this option when the correct host is stored as a user reference on the booker's Salesforce Account (or on a related object), rather than as the Account owner. Cal.com resolves the Account for the booker, reads the configured user lookup field, and routes to the matching Cal.com user.

Enter the Salesforce API name of the user lookup field in **Lookup field name**. Two formats are supported:

* A field directly on the Account, for example `Owner_Lookup__c`
* A dot-notation path that traverses a relationship on the Account to reach a user lookup field on a connected object, for example `Region__r.Owner__c`

Dot-notation lets you point at a user field that lives on another object linked to the Account — for example a regional territory record with its own owner — without duplicating that field onto the Account itself. Salesforce resolves the relationship server-side, so any depth supported by SOQL relationship queries works.

```text Lookup field name examples theme={null}
Owner_Lookup__c
Region__r.Owner__c
Territory__r.Regional_Manager__c
```

<Note>
  The lookup field name must contain only letters, numbers, and underscores, with dots separating segments for connected objects. Invalid names are flagged inline in the routing form builder. At routing time, an unrecognized field or relationship causes Cal.com to fall through to the form's fallback route.
</Note>

## Routing trace on booking details

When a booking is routed through a CRM integration such as Salesforce, Cal.com records a routing trace that shows how the booking was assigned. You can view this trace directly on the booking detail page and in the booking list actions dropdown.

Previously, routing trace information was only visible for bookings created through a routing form. Now, any booking that has a routing trace — including direct bookings routed via CRM owner assignment — displays the trace in the UI.

### What the routing trace shows

The routing trace includes information about how and why a booking was assigned to a specific host. For CRM-routed bookings, this typically reflects the Salesforce record owner assignment or account resolution logic that determined the host.

### Where to find it

* **Booking list** — Open the actions dropdown on any booking row. If the booking has a routing trace, you see an option to view it.
* **Booking detail page** — A routing trace badge appears on the detail page for bookings that were routed through CRM, even if no routing form was used.

<Note>
  Routing trace is only available for bookings that have trace data recorded by Cal.com. Bookings created without CRM routing or a routing form do not show a trace.
</Note>

## Cross-TLD fuzzy domain matching

When using the **Contact under Account** attendee record type, Cal.com resolves the attendee's Salesforce Account by matching their email domain against Account `Website` fields. By default, this lookup requires an exact domain match — `acme.com` only matches Accounts whose website is on `acme.com`.

With **cross-TLD fuzzy domain matching** enabled, Cal.com also matches across different top-level domains. An attendee with an `@acme.co.uk` email can be matched to a Salesforce Account whose website is `acme.com`, `acme.de`, or any other TLD variant sharing the same base domain.

### How account resolution works

Cal.com resolves the attendee's Salesforce Account using a multi-step waterfall:

1. **Exact match** — Look for an Account whose `Website` exactly matches the attendee's email domain (for example, `acme.com`)
2. **Normalized match** — Strip URL prefixes like `www.`, `http://`, and trailing paths, then retry the exact match
3. **Contact email match** — Search for existing Contacts whose email domain matches, and use their linked Account
4. **Fuzzy cross-TLD match** — Extract the base domain (for example, `acme` from `acme.co.uk`) and match it against all Account websites regardless of TLD

Cal.com uses the first match found. If multiple Accounts match at any step, the [tiebreaker waterfall](#tiebreaker-waterfall) runs to select the best candidate. If no Account is resolved at any step, the integration falls back to the behavior configured in your event type settings.

### Tiebreaker waterfall

When multiple Salesforce Accounts match a domain during account resolution, Cal.com runs a tiebreaker waterfall to select the best candidate. This is especially relevant for round-robin event types where the resolved Account owner determines which host receives the booking.

The tiebreaker evaluates candidates in priority order. The first criterion that produces a single winner ends the waterfall.

#### Default tiebreaker rules

The following rules are available. By default, they run in the order shown:

| Priority | Criterion            | Category     | Description                                                                                                 |
| -------- | -------------------- | ------------ | ----------------------------------------------------------------------------------------------------------- |
| P1       | Country match        | Geo          | Account whose `BillingCountry` matches the booker's country                                                 |
| P2       | State/region match   | Geo          | Account whose `BillingState` matches the booker's state or region                                           |
| P3       | Sub-region match     | Geo          | Account whose configured sub-region field matches the booker's location (optional, requires a custom field) |
| P4       | *(Reserved)*         | —            | —                                                                                                           |
| P5       | Most child accounts  | Relationship | Account with the highest number of child Accounts in its hierarchy                                          |
| P6       | Most opportunities   | Relationship | Account with the highest number of related Opportunities                                                    |
| P7       | Most contacts        | Relationship | Account with the most related Contact records                                                               |
| P8       | Most recent activity | Activity     | Account with the most recent `LastActivityDate`                                                             |
| P9       | Earliest created     | Activity     | Account with the oldest `CreatedDate` (longest-standing relationship)                                       |

Priorities P1–P3 are **geo tiebreakers** — they use the booker's geographic location (derived from their IP address) to prefer Accounts in the same region. If geo data is unavailable or no geo criterion produces a winner, the waterfall continues to P5.

If all criteria result in a tie, the last-resort rule (P9) selects the Account that was created first.

#### Configuring tiebreaker rules

You can customize which tiebreaker rules are active and their priority order from the event type settings. This lets you tailor account resolution to match your team's routing strategy — for example, prioritizing opportunity count over geographic proximity, or removing rules that are not relevant to your Salesforce data.

To configure tiebreaker rules, navigate to the event type's **Apps** tab, expand the Salesforce section, and find the **Tiebreaker rules** setting.

<Steps>
  <Step title="Enable the tiebreaker waterfall">
    Toggle the tiebreaker waterfall **on**. When disabled, Cal.com does not run tiebreaker logic and selects a matching Account arbitrarily.
  </Step>

  <Step title="Review the default rules">
    The rule list shows each active tiebreaker rule with its priority number, description, and category (Geo, Relationship, or Activity). Rules run in the order they appear, from top to bottom.
  </Step>

  <Step title="Reorder rules">
    Use the arrow buttons to move a rule up or down in the priority list. Rules higher in the list are evaluated first. Move your most important criteria to the top.
  </Step>

  <Step title="Remove a rule">
    Click the delete icon on any rule to remove it from the waterfall. Removed rules no longer participate in account resolution.
  </Step>

  <Step title="Add a rule">
    Use the **Add rule** dropdown to add a previously removed rule back to the waterfall. The dropdown shows each rule's description so you can make an informed selection.
  </Step>

  <Step title="Save">
    Save your event type to apply the updated tiebreaker configuration. The customized order applies to all future bookings for this event type.
  </Step>
</Steps>

<Note>
  The tiebreaker configuration is per event type. Each event type can have its own set of active rules and ordering. If you remove all rules or disable the tiebreaker waterfall, Cal.com skips tiebreaker logic entirely and uses the first Account match from the resolution waterfall.
</Note>

#### Geo tiebreakers

Geo tiebreakers route bookings to the Salesforce Account that is geographically closest to the person booking. Cal.com reads the booker's country and region from IP-based geo-location headers and compares them against the Account's `BillingCountry` and `BillingState` fields in Salesforce.

You can configure geo tiebreakers in the Salesforce section of your routing form settings. When enabled, the tiebreaker waterfall checks geography before falling back to the standard relationship-based criteria (child accounts, opportunities, contacts, etc.).

##### When to use geo tiebreakers

Geo tiebreakers are useful when:

* Your team has regional Account owners and you want bookings routed to the owner nearest the booker
* You have multiple Accounts for the same company across different regions (for example, "Acme US" and "Acme EMEA")
* You want to improve lead-to-rep matching by factoring in geographic proximity

##### Sub-region matching

For more granular geographic routing, you can specify a custom Salesforce field for sub-region matching. This field is checked at P3 in the waterfall, after country and state matching. Use this when your Accounts are segmented by territories smaller than a state — for example, a custom `Sales_Territory__c` field.

<Note>
  Geo tiebreakers require the booker's IP geo-location data, which is derived from request headers set by your infrastructure (for example, Cloudflare or Vercel geo headers). If geo data is not available, these steps are skipped and the waterfall starts at P5.
</Note>

#### Host filtering

For round-robin event types, candidates are filtered before the tiebreaker runs. Only Account owners who are hosts on the event type are eligible. If this filter removes all candidates, Cal.com falls back to standard round-robin assignment.

### Record type filtering

You can exclude specific Salesforce record types from account resolution. When record type filtering is enabled, Accounts with excluded record types are skipped during the resolution waterfall. This prevents Cal.com from matching against Accounts that are not relevant to booking routing, such as partner or vendor accounts.

Configure record type filtering in the Salesforce section of your event type's **Apps** tab.

### When to use fuzzy matching

Fuzzy domain matching is useful when:

* Your Salesforce Accounts have websites on a single TLD (for example, `acme.com`) but attendees book from regional email domains (for example, `@acme.co.uk`, `@acme.de`)
* You want to automatically link international attendees to the correct parent Account without creating duplicate records
* Your organization operates across multiple country domains under the same brand

<Note>
  Fuzzy matching only applies to the **Contact under Account** attendee record type. It does not affect Contact-only or Lead-only lookups.
</Note>

## Field mapping validation

Cal.com validates your Salesforce field mappings when you save event type settings. If a field mapping has a type mismatch — for example, a non-boolean value mapped to a checkbox field, or an empty value for a required text field — Cal.com displays an inline error and prevents the save.

If a sync error occurs at runtime (for example, a field was deleted in Salesforce after configuration), Cal.com stores the error and displays a diagnostic notification on the Salesforce settings tab. The notification includes the error code, message, any dropped fields, and a timestamp to help you troubleshoot.

### Validated field types

| Field type                      | Validation rule                                                        |
| ------------------------------- | ---------------------------------------------------------------------- |
| Checkbox                        | Value must be a boolean (`true` or `false`)                            |
| Date                            | Must reference a valid dynamic date value (e.g., `booking_start_date`) |
| Text, phone, picklist, textarea | Value must be a non-empty string                                       |
| Custom                          | No automatic validation — values are passed through as-is              |
