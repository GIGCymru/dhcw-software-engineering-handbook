# Error reporting

[HTTP status codes](http-implementation.md) often provide sufficient
error information. But sometimes the client needs additional details.

If your APIs follow the FHIR standard, the server **MUST** return the
OperationOutcome resource.

For non-FHIR APIs, the server **SHOULD** follow RFC7807 or, where
applicable, the JSON API specification.

When returning error information, the server **MUST NOT** include
unnecessary or sensitive data that attackers could exploit. See also the
[OWASP 10](owasp-top-10.md) & [Minimise Information
Disclosure](security-headers.md) sections.

The server **MUST** use [HTTP status codes](http-implementation.md)
in the 5xx range to indicate server errors. For client errors, the
server **SHOULD** return a 4xx status code.

!!! tip "Practical tips"
    ASP.NET Core's ProblemDetails formats errors according to RFC7807.

!!! info "Further reading and information"
    [OperationOutcome - FHIR v4.0.1](https://hl7.org/fhir/R4/operationoutcome.html#operationoutcome)

    [RFC 7807 - Problem Details for HTTP APIs](https://datatracker.ietf.org/doc/html/rfc7807)

    [JSON:API --- A specification for building APIs in JSON](https://jsonapi.org/)
