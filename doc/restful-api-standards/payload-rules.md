# Payload rules

Some rules in this section align with JSON API, while others differ. You
**MAY** follow the complete JSON API specification, but you **MUST**
carefully consider its impact.

## Encoding and content negotiation

For encoding, you **SHOULD** use "UTF-8".

Unicode **MUST** be used as the standard encoding for all text
representations of dates in APIs, and it is the default for JSON.

The server **SHOULD** represent resources in JSON (RFC 8259/ECMA-404) by
default, defined as application/json in the OpenAPI specification.

You **MAY** add extra media types, but they **MUST** be described in the
OpenAPI definition.

If your API can return multiple media types, it **SHOULD** return the
first supported type indicated in the HTTP Request's Accept header.

If the requested media types are unsupported, the server **SHOULD**
return an HTTP response with status 415 UNSUPPORTED MEDIA TYPE.

## Date formats

HTTP headers containing datetime values **MUST** use the RFC 5322
format:

- `ddd, dd MMM yyyy HH:mm:ss Z`

Dates or timestamps in the JSON payload of the response **MUST** conform to
the RFC 3339 format:

- `YYYY-MM-DDTHH:mm:ssZ`

## Payload size

For performance reasons, the server **SHOULD** use [paging](paging.md) for
large datasets or binary objects.

The server **SHOULD** keep the total payload size below 2 MB and
**MUST** ensure that it does not exceed 10 MB, as this is a hard limit
for some platforms.

!!! info "Further reading and information"
    [JSON:API --- A specification for building APIs in JSON](https://jsonapi.org/)

    [RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259)

    [ECMA-404 - Ecma International](https://ecma-international.org/publications-and-standards/standards/ecma-404/)

    [RFC 5322 - Internet Message Format](https://datatracker.ietf.org/doc/html/rfc5322)

    [RFC 3339 - Date and Time on the Internet: Timestamps](https://datatracker.ietf.org/doc/html/rfc3339)
