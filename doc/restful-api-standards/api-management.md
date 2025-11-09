# API management

## Generating an API proxy

To publish an API, generate a proxy from your [Open API
specification](open-api-specification.md) early in the development
process. Contact the platform team (see their process map below) for
details.

## Ping and service status

APIs **SHOULD** implement ping and status endpoints that return an HTTP
200 OK response. These endpoints allow the platform team to connect the
API platform to them.

## API lifecycle

The stability of your API and the support you provide depend on its
[lifecycle status](appendix-a-classifications.md). You **MUST** classify your API
using the [lifecycle status](appendix-a-classifications.md) definitions described in
Appendix A.

### Deprecation and retirement

You **MAY** deprecate and retire an API endpoint if it is:

- Replaced by a new endpoint that provides equivalent or enhanced
    capabilities.

- Not fit for purpose, for example it is insecure.

- Unused or of limited usage.

### Retirement timeline

At the end of the deprecation period, the API endpoints reach
end-of-life and are taken out of service. At this point, the API
endpoint **MUST** no longer be available for use.

### Deprecation policy

To deprecate an API endpoint you **MUST**:

- Add a deprecation notice to your documentation stating the
    deprecation date.

- Add a deprecation header with the deprecation date.

- Email subscribed users with the deprecation date - as the date
    approaches, emails **SHOULD** be sent more frequently.

- Keep the endpoint available for use and maintain normal service
    levels.

- Permit no further integrations, although you **MAY** allow consumers
    in the latter stages of onboarding to complete sign-up.

You **SHOULD** make no further updates unless necessary.

### Retirement policy

To retire an API endpoint, you **MUST**:

- Add a retirement notice to your documentation stating the retirement
    date, giving no less than **6 months'** notice.

- Add a sunset header with the retirement date.

- Provide a migration guide where applicable.

- Keep the endpoint available for use and maintain normal service
    levels.

- Permit no further integrations.

You **SHOULD** make no further updates unless necessary.

!!! info "Further reading and information"
    [RFC 8594 - The Sunset HTTP Header Field](https://datatracker.ietf.org/doc/html/rfc8594)

## Deployment

API deployment **SHOULD** follow DevOps best practices and use
continuous integration and deployment (CI/CD). For more information see
our coding standards.

!!! info "Further reading and information"
    [Software development handbook](../software-development-handbook/introduction.md)

    [Using Source Control](../using-source-control/introduction.md)

!!! tip "Practical tips"
    **API Platform Starter Project**

    Developers can use the platform team's SDK --that comes with pre-set ping and status policies and ready-made pipelines. These pipelines automatically package your API proxy and deploy it to Apigee once approved.

## Versioning

### Semantic versioning

APIs **MUST** follow the Semantic Versioning Specification 2.0.0. It
helps API consumers avoid using new versions with breaking changes. You
**SHOULD** avoid breaking changes where possible.

If you never apply a *breaking change*, simply use semantic versioning
to differentiate *minor* releases (with added functionality) from
*patch* releases.

!!! info "Further reading and information"
    [Semantic Versioning 2.0.0 \| Semantic Versioning](https://semver.org/)

### Versioning urls for release versions

You **MUST** indicate *release* versions with *breaking changes* by
adding a higher *major version number*, preceded by a lowercase *v* to
the URL. Exclude version 1.x.x. and *minor* and *patch* version numbers.

!!! example "Examples of good practice"
    ```sh
        /{base}/patients

        {*base}*/v2/patients

        /{base}/v1/patients

        /{base}/v2.1.3/patients
    ```

### Versioning urls for pre-release versions (alpha and beta)

Follow the same method for pre-release versions but include versions 0
and 1 and add the pre-release type (i.e. *alpha* or *beta*), preceded by
a dash.

Semantic versioning states that major version 0 is always pre-release;
therefore alpha/beta labels are not necessarily needed but they help
clarify API status. Here are some examples:

Version "0.1.3-alpha" published for pre-release testing to:

!!! example "Examples of good practice"
    `/{base}/v0-alpha/patients`

And then version "1.0.0" published to:

!!! example "Examples of good practice"
    `/{base}/patients`

Followed by version "1.1.0-beta" published for pre-release testing to:

!!! example "Examples of good practice"
    `/{base}/v1.1-beta/patients`

Finally, release version "1.1.0" (with no breaking changes) published to
the original URL:

!!! example "Examples of good practice"
    `/{base}/patients`

!!! tip "Practical tips"
    When deploying breaking changes to *beta* versions (i.e. versions used by early adopters), increment the minor version and notify users who might be affected.

## Cataloguing

You **MUST** publish any release version *Open* API to the NHS Wales API
external product catalogue.

You **MAY** publish an *Open* API, not yet marked as a release, version
to the NHS Wales API external product catalogue.

You **SHOULD** publish a release version *inner* API to DHCW's internal
product catalogue.

You **MAY** publish an *inner* API, not yet marked as a release version,
to DHCW's internal product catalogue.

The catalogue entry **MUST** include the [lifecycle
status](appendix-a-classifications.md). This makes it clear to consumers where each
version of your API is in its lifecycle.

!!! tip "Practical tips"
    Uncatalogued APIs run the risk of being forgotten and not monitored or protected by security tools. See also the [OWASP TOP 10](owasp-top-10.md) section.

## Auditing, tracing and monitoring

If your API deals with [confidential or sensitive data](appendix-a-classifications.md), you
**MUST** maintain a log that records details about access.

This log **SHOULD** be sent to our Security information and event
management system (SIEM) and National Intelligent Integrated Audit
Solution (NIIAS) via an [API gateway](api-gateway-pattern.md).

To ensure compliance and for guidance on the log format and the minimum
standard fields, consult with the platform team or Cyber security team.

!!! info "Further reading and information"
    [National Intelligent Integrated Audit Solution (NIIAS) - Home](https://nhswales365.sharepoint.com/sites/DHC_IGNI)

## Rate limiting and throttling

All APIs **SHOULD** set client usage quotas and rate limits. For
critical systems, this is a **MUST**. Speak to the platform team and
Cyber Security team for help.

### Spike arrests

The platform team will help you handle sudden traffic spikes and keep
you API stable. Rate limiting, a key feature in Apigee, sets thresholds
on the number of requests within a specific period.

This ensures a controlled flow of traffic, preventing overloads and
optimising performance. No manual configuration is required; the API
platform team oversees Apigee, guaranteeing effective rate limiting for
a reliable and responsive API experience.
