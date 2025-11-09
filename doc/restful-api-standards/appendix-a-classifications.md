# Appendix A: Classifications

## API type

| **TYPE** | **DEFINITION** |
| --- | --- |
| Open | Open APIs are made available to both internal developers within DHCW and external consumers. They are exposed and managed on DHCW's API management platform, Apigee and published on an external catalogue. Examples include *Medicines & Allergies*, *PIX and PDQ APIs* |
| Internal | Internal APIs are accessible only to internal developers within DHCW. They are, typically, exposed and managed on DHCW's API management platform, Apigee and published on an internal catalogue. They are not intended for external use. |
| Client specific | These APIs are restricted to a specific client or team within DHCW. They are usually managed independently through that team's own API management tool. They are not typically published on a central catalogue. |

## Data type

| **TYPE** | **DEFINITION** |
| --- | --- |
| Public | Access restrictions are not required for read-only access. Examples: NHS Wales Data Dictionary items, dummy data in a public test environment. |
| Business confidential | Access restrictions are set by organisational policy, contracts, or license agreements, but not by law. Examples: SNOMED CT, internal URLs, and connection strings. |
| Sensitive | Access restrictions are more stringent and set by laws (e.g. GDPR legislation) Examples: "Personal" data types, as defined in the *Data Protection Impact Assessment Form Template*. |
| Highly sensitive | Access restrictions are specific to the data items and higher than sensitive or business confidential. Examples: "Special category" and "Higher sensitivity" data types, as defined in the *Data Protection Impact Assessment Form Template*. Examples: database passwords, private encryption keys. |

!!! info "Further reading and information"
    IG-TEM-1 Data Protection Impact Assessment Form Template

## Network routing type

| **TYPE** | **DEFINITION** |
| --- | --- |
| Internal | Data stays within NHS Wales Wide Area Network (WAN). |
| Peered | Data stays within Health and Social Care Network (HSCN), Public Sector Broadband Aggregation (PSBA), or another secured link (VPN or mTLS) to NHS Wales WAN. |
| Internet | Data travels across the public internet. |

## Client type

Take care to apply these classifications in context. For example, a
client may be *pre-authorized* to write patient prescription data but
only *licenced* for use in reading patient test results.

| **TYPE** | **DEFINITION** |
| --- | --- |
| Pre-authorised | Authorised to process the data and apply appropriate access controls for end users. Typically, an application managed by an NHS Wales organisation or a contracted supplier. Authorisation requires formal assurance by an NHS Wales assurance group. Examples: Welsh Clinical Portal, GP Systems, Clinical Workstation. |
| Licenced | Licenced ('*Trusted')* to process the data if authorised end users supply or grant access to it. Typically, an application procured or under trial usage by an NHS Wales organisation. Licencing for use may require formal assurance by an NHS Wales assurance group. |
| Open | Has no formal NHS Wales approval or contract licencing its use to process the data. Typically, an application procured, developed, or otherwise obtained by the user. Examples: Postman, SOAP UI |

## Client authentication level

| **LEVEL** | **DEFINITION** |
| --- | --- |
| 0: No Authentication | No authentication. |
| 1: API Key | API Key is provided with each request. *Weak security as the key is both ID and the credential*. |
| 2: Credentials | Basic client credentials (Client ID and Client Secret) are provided with each request. *More secure as the secret can be omitted when the Client ID is written to audit logs.* |
| 3: : Access token (using Credentials) | A time limited access token is first obtained in an initial request, then provided with each further request. To obtain the access token the client supplies basic credentials (Client ID and Client Secret). *More secure as credentials are shared less frequently and only with the token endpoint.* Licenced clients may use level 3. |

## Service level

| **LEVEL** | **DEFINITION** |
| --- | --- |
| Critical | As defined in *DHCW-POL-5 Service Level Target Policy*, extended downtime is highly disruptive. |
| Standard | As defined in *DHCW-POL-5 Service Level Target Policy*, e.g. reporting and analytical systems. |

!!! info "Further reading and information"
    DHCW-POL-5 Service Level Target Policy

## Lifecycle status

| **STATUS** | **DEFINITION** | **RELEASE VERSION** |
| --- | --- | --- |
| **Alpha** | Pre-release version and subject to *breaking changes*. Intended to be used only by those involved with the development. **SHOULD** not be available in a production environment. | No |
| **Beta** | Pre-release version and subject to *breaking changes*. Stable enough for use by early adopters to help you identify bugs and potential improvements. **MAY** be available in a production environment. | No |
| **Stable** | Release version. You **MUST NOT** introduce breaking changes. Breaking changes **MUST** result in a new major version. **SHOULD** be available in a production environment. | Yes |
| **Legacy** | The same as *stable*, available for use but no new integrations given it's planned for *deprecation.* **SHOULD** be available in a production environment for existing users. | Yes |
| **Deprecated** | The same as *stable*, but existing users should switch to a newer version or alternative API. Not intended for new users, given it's planned for *retirement*. **SHOULD** be available in a production environment until retirement. | Yes |
| **Retired** | No longer supported. APIs move into this category when all users have moved to a newer version or no longer subscribe. **MUST** not be available in any environments. | No |
