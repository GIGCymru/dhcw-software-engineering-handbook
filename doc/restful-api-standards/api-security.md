# API security

## OWASP top 10

During assurance, you **MUST** provide evidence of adequate mitigations
against OWASP Top 10 API Security Risks -- 2023 in a Test Summary
report.

!!! info "Further reading and information"
    [OWASP Top 10 API Security Risks -- 2023 - OWASP API Security Top 10](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)

## Secrets and certificate management

You **SHOULD NOT** store secrets in clear-text storage.

Secrets and API keys **MUST** be stored and encrypted in a secrets
manager. Where secrets are injected from a secrets manager into a CI-CD
pipeline, they **MUST NOT** be logged.

## Encryption

The server **MUST** secure communications using at least TLS 1.2
(https).

The server **SHOULD**:

- Use one of the TLS cipher suites recommended in *SOP-OSD-001
    Encryption in Transit* and *SS-OSD-006 Application Programming
    Interfaces (APIs)*

- Use a TLS certificate signed by a chain ending with a trusted
    Certificate Authority (CA)

!!! info "Further reading and information"
    SOP-OSD-001 Encryption in Transit

    SS-OSD-006 Application Programming Interfaces (APIs)

## Security headers

Use [HTTP response headers](http-implementation.md) to specify security
controls in HTTP communications. These serve as an extra layer of
protection against common vulnerabilities and privacy risks.

### Minimise information disclosure

You **SHOULD** remove unnecessary HTTP response headers that expose
details about the server and its underlying technologies. For example,
consider the following response which includes headers that reveal
server information:

!!! danger "Examples of practices to avoid"
    ```sh
        *HTTP/1.1 201 Created*

        *Content-Type: application/json; charset=utf-8*

        *Location: /api/patients/9991234568*

        *Date: 2024-02-17T12:00:00Z*

        *Server: Microsoft-IIS/10.0*

        *X-AspNet-Version: 6.0.0*

        *X-AspNetMvc-Version: 6.0.0*
    ```

You **SHOULD** remove these sensitive headers. A valid response might
look like this:

!!! example "Examples of good practice"
    ```sh
        *HTTP/1.1 201 Created*

        *Content-Type: application/json; charset=utf-8*

        *Location: /api/patients/9991234568*

        *Date: 2024-02-17T12:00:00Z*
    ```

## HTTP message caching

Typically, you **SHOULD NOT** allow sensitive data, returned over an
authenticated (HTTPS) connection, to be cached. But if you do, you
**MUST** make sure there is no risk that network appliances cache data
in clear text. Speak to the Cyber security team for help.

## API gateway pattern

APIs **SHOULD** be deployed behind a gateway. This ensures that the
security policies provided by the gateway are used rather than
implementing them directly in your back-end API.

Typically, deploy to Apigee or your own API gateway if building APIs
exclusively for your app. Consult the API platform and Cyber Security
teams for further advice.

## Data classification

You **MUST** classify resource data types according to the platform
team's data classification framework (see [Appendix
A](appendix-a-classifications.md)).

Based on the classification, you **MUST** apply the appropriate security
controls.

For detailed guidance on implementing security measures, refer to the
[Authentication and Authorisation](authentication-and-authorisation.md)
section.
