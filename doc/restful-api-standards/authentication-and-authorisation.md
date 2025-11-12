# Authentication and authorisation

The server **SHOULD** enforce authentication and authorisation using
OAuth 2.0 and OIDC protocols as described below. Typically the API
Platform team will provide this service.

## Client authentication

Authentication is enforced at one of the following levels.

| **LEVEL** | **DESCRIPTION** |
| --- | --- |
| 0 | No Authentication |
| 1 | API Key |
| 2 | Credentials |
| 3 | Access token (using Credentials) |
| 4 | Access token (using Public Key Cryptography) |

Authentication Levels

The server **MUST** enforce the minimum required level as determined by
the type of data accessed, client characteristics and network routing:

|  |  | [**DATA TYPE**](appendix-a-classifications.md) |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| [**CLIENT TYPE**](appendix-a-classifications.md) | [**NETWORK ROUTING TYPE**](appendix-a-classifications.md) | **PUBLIC (READ)** | **PUBLIC (WRITE)** | **BUSINESS CONFIDENTIAL** | **SENSITIVE** | **HIGHLY SENSITIVE** |
| Pre-Authorised | Internal | 0 | 1 | 2 | 2 | 2 |
|  | Peered | 0 | 1 | 3 | 3 | 3 |
|  | Internet | 1 | 1 | 3 | 4 | 4 |
| Licenced | All | 1 | 3 + End User Delegation | 3 + End User Delegation | 4 + End User Delegation | 4 + End User Delegation |
| Open | All | 1 | 3 + End User Delegation | 3 + End User Delegation | *No access* | *No access* |

Minimum Authentication Levels

## End user delegation

*Licenced* and *Open* clients requesting any access beyond reading
[public data](appendix-a-classifications.md) **MUST** require users to delegate
permissions. Users **MUST** be authenticated by the NHS Wales Identity
Provider.

The server **MUST** implement [role-based access
controls](authentication-and-authorisation.md) to verify that end users
are authorised to grant the requested permissions to the client
application.

## Role-based access control (scopes)

APIs **SHOULD** define access controls as *scopes*. Speak to the
platform team for further help.

!!! info "Further reading and information"
    [App Launch: Scopes and Launch Context - SMART App Launch v2.2.0](https://build.fhir.org/ig/HL7/smart-app-launch/scopes-and-launch-context.html#scopes-for-requesting-fhir-resources)

## Authorisation grants

For client authentication level 3 without End User Delegation, the
**RECOMMENDED** method is to use the OAuth 2.0 grant type
client_credentials to obtain a bearer token, as described in RFC 6749,
section 4.4.

For client authentication level 3 with End User Delegation, the
**RECOMMENDED** method is to use the OAuth 2.0 grant type
authorization_code to obtain a token. The client **MUST** use client_id
and client_secret to authenticate with the token endpoint, as described
in RFC 6749, sections 4.1 and 2.3.1.

For level 4 client authentication without End User Delegation, the
**RECOMMENDED** method is to use the OAuth 2.0 grant type
urn:ietf:params:oauth:grant-type:jwt-bearer, as described in RFC 7523,
section 2.1.

For level 4 client authentication with End User Delegation, the
**RECOMMENDED** method is to use the OAuth 2.0 grant type
authorization_code to obtain a token. The client **MUST** use a client
assertion to authenticate with the token endpoint, as described in RFC
7523, section 2.2.

!!! info "Further reading and information"
    [RFC 6749 - The OAuth 2.0 Authorization Framework](https://datatracker.ietf.org/doc/html/rfc6749)

    [RFC 7523 - JSON Web Token (JWT) Profile for OAuth 2.0 Client Authentication and Authorization Grants](https://datatracker.ietf.org/doc/html/rfc7523)

## Access token expiry

When using authentication level 3 or above, access tokens **MUST**
expire within the following time frames:

- For [Business Confidential data](appendix-a-classifications.md): within 1 day.

- For [Sensitive data](appendix-a-classifications.md): within 1 hour.

- For [Highly Sensitive data](appendix-a-classifications.md): tokens **SHOULD** expire
    within 5 minutes but **MUST** expire within 1 hour.

## Restrictions on data use

| **ENVIRONMENT** | **RESTRICTIONS ON DATA SENT TO AND FROM AN API** |
| --- | --- |
| Development | Data **SHOULD** be classified as "[Public](appendix-a-classifications.md)" (e.g., synthetic test data[^1]) Data **MUST NOT** be classified as "[Sensitive](appendix-a-classifications.md)" or "[Highly Sensitive](appendix-a-classifications.md)" Data **MUST NOT** be written to systems in Production |
| Sandbox | Data **MUST** be classified as "[Public](appendix-a-classifications.md)" (e.g., synthetic test data) |
| Systems Integration Testing | Data **SHOULD** be classified as "[Public](appendix-a-classifications.md)" (e.g., synthetic test data) Data **MUST NOT** be classified as "[Sensitive](appendix-a-classifications.md)" or "Highly Sensitive" Data **MUST NOT** be written to systems in Production |
| User Acceptance Testing | Data **MUST NOT** be written to systems in Production |
| Production | No restrictions apply; however, please refer to the [API Security standards](security-headers.md). |

## Input validation

The server **MUST** validate all inputs to prevent code injection,
cross-site scripting (XSS) attacks and other malicious requests such as
overposting and mass assignment.

The server **SHOULD** restrict query parameter string filters to
enumerated values or regular expressions.

## Browser-based access and Cross-Origin Resource Sharing (CORS)

APIs **MUST NOT** be accessed directly from code running in a browser
unless they are limited to reading or writing public data.

If the server permits direct browser access then:

- The outbound HTTP header Access-Control-Allow-Origin **MUST** be set
    to a specific value and **MUST NOT** be a wildcard.

- The inbound HTTP header Origin **MUST** be validated against a list
    of permitted host names for authenticated applications.

[^1]: Note Synthetic data should be useful and reflect the use-case of the API
