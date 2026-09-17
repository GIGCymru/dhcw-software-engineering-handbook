# Introduction

## Purpose

These standards:

- Specify the requirements for designing and building RESTful APIs.

- Provide guidance for aligning with our API Strategy & Roadmap.

They are intended for API producers but may also assist teams
integrating APIs into client applications.

!!! tip "Practical tips"
    If you have production APIs, you need not introduce breaking changes solely to comply. Contact the author for support.

!!! info "Further reading and information"
    The API Strategy & Roadmap

## Scope

### In-scope

These standards apply to RESTful APIs designed and built for:

- Internal use within the organisation.

- External use by clients, partners, or third parties.

A [good practice checklist](essential-good-practice-checklist.md) is also
included to assist teams in achieving compliance.

### Out-of-scope

These standards do not apply to:

- Non-RESTful APIs, including GraphQL, gRPC, and event-driven APIs
    (e.g. Azure Functions).

- APIs designed primarily to handle large binary data (e.g. image or
    file delivery).

- Topics outside API design and implementation, such as Domain-driven
    design or microservices architecture.

- Infrastructure, networking, or Web Application Firewalls (WAF).

- API publishing pipelines (e.g. via Apigee).

- Telemetry, monitoring, or general software development practices.

## References

1. The API Strategy and Roadmap
1. [Testing for lost updates](../testing-lost-updates/introduction.md)
1. [How to write a Test Summary Report](../test-summary-report/introduction.md)
1. SDS-TEM-5 - Test Summary Report template
1. IG-TEM-1 - Data Protection Impact Assessment Form Template
1. DHCW-POL-5 - Service Level Target Policy

See [how this handbook is organised](../index.md#how-this-handbook-is-organised) for the full list of sections.

## Conventions

This section follows the [handbook-wide conventions](../index.md#conventions)
for RFC 2119 key words and callout boxes.

## The need for guidance

Conforming to these standards helps you build APIs that are consistent,
easy to use, safe and secure.

!!! tip "Practical tips"
    **Integration as a 'war of attrition'**

    Read about Mark Wardle's experience integrating applications with NHS Wales systems. Mark is a Consultant Neurologist and Chair of the Welsh Technical Standards Board.

!!! info "Further reading and information"
    [wardle/concierge: README \> Background](https://github.com/wardle/concierge#readme)
