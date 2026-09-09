> ## Documentation Index
> Fetch the complete documentation index at: https://cal.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to setup scim with okta

<Note>
  Before provisioning users, your organization must have a **verified domain** configured. Cal.com only provisions users whose email domain matches (or is a subdomain of) your organization's verified domain. Provisioning requests for other domains are rejected to prevent account capture. Verify your domain under `Settings → Organization` before enabling SCIM.
</Note>

<Steps>
  <Step title="Create an application with your OIDC provider">
    For example, in Okta, once you create an account, you can click on Applications on the sidebar menu:

    <img src="https://mintcdn.com/calcom/I5tVBJL5l-pcIYMU/images/i1600x900-oVjaQ0tU3AnO_wrzp85.png?fit=max&auto=format&n=I5tVBJL5l-pcIYMU&q=85&s=9026756e1372c1ef4adfc2b39d8116b1" width="1600" height="900" data-path="images/i1600x900-oVjaQ0tU3AnO_wrzp85.png" />
  </Step>

  <Step title="Click on Create App Integration">
    <img src="https://mintcdn.com/calcom/I5tVBJL5l-pcIYMU/images/i1600x900-wrIlZkLdZ6kL_wf7mxn.png?fit=max&auto=format&n=I5tVBJL5l-pcIYMU&q=85&s=3bd200085a219cb22958a27d70cd6bdf" width="1600" height="900" data-path="images/i1600x900-wrIlZkLdZ6kL_wf7mxn.png" />
  </Step>

  <Step title="Select SAML or OIDC and Web App, then click Next">
    Note you will have to fill in the appropriate fields for the SAML or OIDC setup to continue.

    * [SAML Setup](/docs/developing/guides/auth-and-provision/sso-setup#setting-up-saml-login)
    * [OIDC Setup](/docs/developing/guides/auth-and-provision/sso-setup#setting-up-oidc-login)

    <img src="https://mintcdn.com/calcom/a6KkjhrH4XhVuWk6/images/i1600x900-IfRWYg8XuCMI_tkwyft.png?fit=max&auto=format&n=a6KkjhrH4XhVuWk6&q=85&s=2144b11c135b98c7c6b4fbbbad2be00d" width="1600" height="900" data-path="images/i1600x900-IfRWYg8XuCMI_tkwyft.png" />
  </Step>

  <Step title="Enable SCIM provisioning">
    Once the application is created, under General -> App Settings, click "Edit" and then the checkbox "Enable SCIM provisioning".

    <img src="https://mintcdn.com/calcom/5iwI3KYRn4f5i5y6/images/scim/app-settings-enable-scim.webp?fit=max&auto=format&n=5iwI3KYRn4f5i5y6&q=85&s=e343c8b435acc08307373ddc92f5dc03" width="2400" height="1350" data-path="images/scim/app-settings-enable-scim.webp" />
  </Step>

  <Step title="Go to Directory Sync in Cal.com">
    Next, go to your instance of Cal.com and navigate to `https://app.cal.com/settings/organization/dsync` and click configure.

    <img src="https://mintcdn.com/calcom/5iwI3KYRn4f5i5y6/images/scim/dsync-configure.webp?fit=max&auto=format&n=5iwI3KYRn4f5i5y6&q=85&s=1d3fb362a76567fabfaac07a7bc67ec8" width="2400" height="1350" data-path="images/scim/dsync-configure.webp" />
  </Step>

  <Step title="Configure Directory Sync">
    In the "Configure Directory Sync" form, choose a directory sync name and select "Okta SCIM v2.0" as the "Directory Provider".

    <img src="https://mintcdn.com/calcom/5iwI3KYRn4f5i5y6/images/scim/dsync-configure-provider.webp?fit=max&auto=format&n=5iwI3KYRn4f5i5y6&q=85&s=87b57666fce0719dc72c2579e296f21c" width="2400" height="1350" data-path="images/scim/dsync-configure-provider.webp" />
  </Step>

  <Step title="Take note of SCIM Base URL and SCIM Bearer Token">
    <img src="https://mintcdn.com/calcom/5iwI3KYRn4f5i5y6/images/scim/dsync-configure-info.webp?fit=max&auto=format&n=5iwI3KYRn4f5i5y6&q=85&s=d859f74a2a63a40eb7618209e9ea6822" width="2400" height="1350" data-path="images/scim/dsync-configure-info.webp" />
  </Step>

  <Step title="Setup Provisioning in Okta">
    In Okta, go to your application. Navigate to the "Provisioning" tab and click "Integration" under "Settings".

    <img src="https://mintcdn.com/calcom/5iwI3KYRn4f5i5y6/images/scim/okta-dsync-options.webp?fit=max&auto=format&n=5iwI3KYRn4f5i5y6&q=85&s=2cb99d0f8149c66653f20b7cf22c5ebd" width="2400" height="1350" data-path="images/scim/okta-dsync-options.webp" />

    * Under "SCIM connector base URL" enter the "SCIM Base URL" from Cal.com
    * Under "Unique identifier field for users" enter "email"
    * Under "Supported provisioning actions" enable:
      * "Import New Users and Profile Updates"
      * "Push New Users"
      * "Push Profile Updates"
      * "Push Groups"
    * Under "Authentication Mode" choose "HTTP Header"
    * Under "Authentication" enter the "SCIM Bearer Token" from Cal.com
    * When you hit save, it will make a test call to the "SCIM Base URL"
  </Step>

  <Step title="Go to the 'To App' settings">
    After saving, navigate to the "To App" settings, still under the "Provisioning" tab.
  </Step>

  <Step title="Enable Provisioning to App">
    Under "Provisioning to App", click "Edit" and enable:

    * "Create User"
    * "Update User Attributes"
    * "Deactivate User"
  </Step>

  <Step title="Update Attribute Mapping">
    Under "\{Your application name} Attribute Mapping," remove all fields except for:

    * "username"
    * "givenName"
    * "familyName"
    * "email"
    * "displayName"
  </Step>

  <Step title="Map Attributes from Okta Profile">
    Set each of these properties to "Map from Okta Profile" and the related field. Under "Apply On" select "Create and Update".

    <img src="https://mintcdn.com/calcom/5iwI3KYRn4f5i5y6/images/scim/okta-property-settings.webp?fit=max&auto=format&n=5iwI3KYRn4f5i5y6&q=85&s=cdb70b1b876310295d0d35598898d3a1" width="2400" height="1350" data-path="images/scim/okta-property-settings.webp" />
  </Step>

  <Step title="Assign users and groups to the app">
    You can now assign users and groups to the app.
  </Step>
</Steps>

## Mapping Okta Groups to Cal.com Teams

When provisioning groups to your organization, Okta groups can be mapped to teams within your organization, and users will be auto-assigned to these teams.

On `https://app.cal.com/settings/organization/dsync`, there is a table with the teams under your organization. Click on "Add group name" to map the Okta group to the team.

<Note>
  The group name must be spelled exactly as it is shown on Okta.
</Note>

When you push the group to your organization, those users will automatically be added to the team.

<img src="https://mintcdn.com/calcom/5iwI3KYRn4f5i5y6/images/scim/group-team-mapping.webp?fit=max&auto=format&n=5iwI3KYRn4f5i5y6&q=85&s=50889f4dcd185c0cc420482abb3d33b6" width="2400" height="1350" data-path="images/scim/group-team-mapping.webp" />

## Email domain verification

Cal.com verifies that each SCIM-provisioned email belongs to your organization before force-joining the user. Provisioning succeeds only when all of the following are true:

* Your organization has a **verified domain** set.
* The provisioned user's email domain matches that verified domain exactly, or is a subdomain of it (for example, `eu.acme.com` matches `acme.com`).

If any check fails, the SCIM request is rejected with a `Forbidden` error and the user is not created or joined to your organization. If you see this error in your identity provider, confirm that the organization is verified and that the affected user's email domain matches your verified domain.
