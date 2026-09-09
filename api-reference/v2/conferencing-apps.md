> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Conferencing Apps

> Connect Zoom, Microsoft Teams or Google Meet to a user or a team

Every Cal.com booking gets a location. By default that is Cal Video, and you can point it at Zoom, Microsoft Teams or Google Meet instead once the app is connected to the user or team that owns the event type.

Which endpoint you use depends on whether the app needs an OAuth handshake:

| App             | `app` slug    | How to connect                                       |
| --------------- | ------------- | ---------------------------------------------------- |
| Cal Video       | `daily-video` | Always available — nothing to connect                |
| Google Meet     | `google-meet` | A single `POST /v2/conferencing/google-meet/connect` |
| Zoom            | `zoom`        | The OAuth redirect flow below                        |
| Microsoft Teams | `msteams`     | The OAuth redirect flow below                        |

<Warning>
  [`POST /v2/conferencing/{app}/connect`](/docs/api-reference/v2/conferencing/connect-your-conferencing-application) only accepts `google-meet`. Sending `zoom` or `msteams` to it returns `400` with `Invalid conferencing app. Available apps: GOOGLE_MEET.` — those apps use the OAuth flow instead.
</Warning>

## Authentication

Every request below takes an `Authorization: Bearer <token>` header, where the token is an API key prefixed with `cal_`, a managed user access token, or an OAuth access token.

**The credential is stored against whoever the token belongs to.** To connect Zoom for one of your managed users, call these endpoints with *that user's* access token, not with your API key. OAuth access tokens additionally need the `APPS_WRITE` scope to connect and `APPS_READ` to read.

## Connecting Zoom

Connecting Zoom is a redirect flow: you ask us for an authorization URL, send the user to it, and Zoom returns them to us so we can store the credential.

<Steps>
  <Step title="Request the authorization URL">
    ```bash theme={null}
    curl -G 'https://api.cal.com/v2/conferencing/zoom/oauth/auth-url' \
      --data-urlencode 'returnTo=https://example.com/settings/conferencing' \
      --data-urlencode 'onErrorReturnTo=https://example.com/settings/conferencing?error=zoom' \
      -H 'Authorization: Bearer <managed user access token>'
    ```

    ```json theme={null}
    {
      "status": "success",
      "data": {
        "url": "https://zoom.us/oauth/authorize?response_type=code&client_id=...&redirect_uri=...&state=..."
      }
    }
    ```

    `returnTo` and `onErrorReturnTo` are where we send the user once Zoom is done. Each must be a relative path (`/settings/conferencing`) or an absolute `http(s)` URL — protocol-relative values like `//example.com` and `javascript:` URLs are rejected.

    <Warning>
      The `state` embedded in that URL is signed and **expires 10 minutes after you request it**. Fetch the URL and redirect immediately — don't cache it, queue it, or email it to the user.
    </Warning>

    See [Get OAuth conferencing app auth URL](/docs/api-reference/v2/conferencing/get-oauth-conferencing-app-auth-url).
  </Step>

  <Step title="Send the user to that URL">
    Navigate the user's browser to `data.url` — a top-level redirect, not a `fetch`. Zoom shows its consent screen and then redirects back to `https://api.cal.com/v2/conferencing/zoom/oauth/callback`.

    On our hosted API that callback URL is already registered on Cal.com's Zoom app, so you do not configure a redirect URI. Either way, you should not call the callback endpoint yourself. Self-hosted instances register their own — see [Self-hosting](#self-hosting).
  </Step>

  <Step title="We store the credential and redirect back">
    The [callback](/docs/api-reference/v2/conferencing/conferencing-app-oauth-callback) exchanges the code with Zoom, resolves the access token carried in `state` back to the user, stores the Zoom credential against them, and `301`s to your `returnTo`. If anything fails — the user denies consent, the state has expired — the user lands on `onErrorReturnTo` instead.

    Reconnecting replaces the user's existing Zoom credential rather than adding a second one.
  </Step>

  <Step title="Make Zoom the default location (optional)">
    Connecting Zoom makes it *available* as a location. To make new bookings use it by default:

    ```bash theme={null}
    curl -X POST 'https://api.cal.com/v2/conferencing/zoom/default' \
      -H 'Authorization: Bearer <managed user access token>'
    ```

    This returns `400` with `zoom not connected.` if the previous steps didn't complete. Pass `daily-video` to switch back to Cal Video.
  </Step>
</Steps>

### Checking and removing the connection

* [`GET /v2/conferencing`](/docs/api-reference/v2/conferencing/list-your-conferencing-applications) lists the user's connected conferencing apps. An entry with `"invalid": true` means the stored credential stopped working and the user has to reconnect.
* [`GET /v2/conferencing/default`](/docs/api-reference/v2/conferencing/get-your-default-conferencing-application) returns the current default.
* [`DELETE /v2/conferencing/zoom/disconnect`](/docs/api-reference/v2/conferencing/disconnect-your-conferencing-application) removes it.

## Connecting Zoom for a team

Team-owned conferencing apps follow exactly the same flow, against the organization endpoints:

```
GET    /v2/organizations/{orgId}/teams/{teamId}/conferencing/zoom/oauth/auth-url
GET    /v2/organizations/{orgId}/teams/{teamId}/conferencing
GET    /v2/organizations/{orgId}/teams/{teamId}/conferencing/default
POST   /v2/organizations/{orgId}/teams/{teamId}/conferencing/zoom/default
DELETE /v2/organizations/{orgId}/teams/{teamId}/conferencing/zoom/disconnect
```

The caller must be a **team admin**. The PBAC permission depends on the endpoint: listing the team's apps and reading its default need `team.read`, while requesting an auth URL, setting a default and disconnecting need `team.update`. For OAuth access tokens the scope is `TEAM_APPS_WRITE` to connect, set a default or disconnect, and `TEAM_APPS_READ` to list the team's apps or read its default. See [Access Control](/docs/api-reference/v2/access-control).

For **platform organizations** these endpoints additionally require the `ESSENTIALS` plan or above; a platform organization on a lower plan — or with no subscription — gets a `403`. Organizations that are not platform organizations are unaffected by the plan check.

Zoom still redirects to the same Cal.com-registered callback. The organization and team ids travel inside the signed `state`, which is how the credential ends up on the team instead of on the admin who authorized it.

## Connecting Google Meet

Google Meet needs no OAuth handshake of its own, because it rides on the user's Google Calendar connection:

```bash theme={null}
curl -X POST 'https://api.cal.com/v2/conferencing/google-meet/connect' \
  -H 'Authorization: Bearer <managed user access token>'
```

The user (or team) must already have a working Google Calendar connection — otherwise this returns `400` with `Google Meet requires a Google Calendar connection.`, or asks for a reconnect if the existing calendar credential has gone invalid. Calling it twice returns `400` with `Google Meet is already connected for this user.`

## Self-hosting

On Cal.com's hosted API the Zoom and Microsoft Teams OAuth apps are ours and nothing needs provisioning. On a self-hosted instance you must configure the app's client id and secret from the admin apps page first — without them the auth-url request returns `404`, with `Zoom app not found` for `zoom` and `Office365 app not found` for `msteams`.

The OAuth callback is built from your API base URL rather than hardcoded, so it is `<API_URL>/v2/conferencing/{app}/oauth/callback` — `https://api.cal.com/v2/conferencing/zoom/oauth/callback` on our hosted API, and your own host elsewhere. Register that exact URL as the redirect URI on the Zoom or Microsoft app you provision, otherwise the handshake fails when the provider redirects back.
