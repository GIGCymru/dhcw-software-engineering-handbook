# HTTP implementation

APIs **MUST** follow standard HTTP semantics to ensure consistency,
predictability and interoperability. This section outlines good
practice, but refer to official specs when needed:

!!! info "Further reading and information"
    [RFC 9110: HTTP Semantics - Status Codes (rfc-editor.org)](https://www.rfc-editor.org/rfc/rfc9110.html#name-status-codes)

    [API design best practices - Conform to HTTP semantics \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/architecture/best-practices/api-design#conform-to-http-semantics)

## Hypermedia (hateos)

A RESTful API **MUST** implement *Hypermedia as the Engine of
Application State (HATEOAS)* to be classified as *Richardson Level 3*.
HATEOAS allows clients to navigate and manipulate resources dynamically
without requiring prior knowledge of specific URIs.

However, *HATEOAS* is NOT required for APIs in this organisation.
But if implemented:

- The API **MUST** provide hypermedia links to guide clients on
    available actions.

- These links **SHOULD** use standard link relations where possible
    (e.g. as defined in RFC 8288) and **MUST** be documented in the
    API's OpenAPI definition.

!!! info "Further reading and information"
    [RFC 8288: Web Linking](https://www.rfc-editor.org/rfc/rfc8288.html)

## HTTP verbs and resource operations

APIs **MUST** use standard HTTP methods correctly to ensure predictable
behaviour.

- APIs **MUST** only expose necessary HTTP methods and **MUST**
    document them in the [OpenAPI definition](documentation.md).

- APIs **SHOULD** return `405 Method Not Allowed` for unsupported HTTP
    methods instead of silently ignoring them.

- APIs **MUST** adhere to the standard HTTP semantics defined in *RFC 9110*,
    including idempotency rules.

- Non-standard HTTP verbs **MUST NOT** be used.

!!! info "Further reading and information"
    [RFC 9110: HTTP Semantics - Status Codes (rfc-editor.org)](https://www.rfc-editor.org/rfc/rfc9110.html#name-status-codes)

## Standard HTTP methods and usage

| **OPERATION** | **HTTP VERB** | **PATH** | **REQUEST BODY** | **RESPONSE BODY** | **IDEMPOTENT** |
| --- | --- | --- | --- | --- | --- |
| **LIST** | `GET` | `/resources` | None | Collection Resource | ✅ Yes |
| **RETRIEVE** | `GET` | `/resources/{id}` | None | Resource | ✅ Yes |
| **CREATE** | `POST` | `/resources` | Resource | Resource | ❌ No |
| **REPLACE** | `PUT` | `/resources/{id}` | Resource | Resource | ✅ Yes |
| **MODIFY** | `PATCH` | `/resources/{id}` | Partial Resource | Resource | ❌ No |
| **DELETE** | `DELETE` | `/resources/{id}` | None | None | ✅ Yes |
| **RETRIEVE HEADERS** | `HEAD` | `/resources/{id}` | None | None | ✅ Yes |
| **QUERY CAPABILITIES** | `OPTIONS` | `/resources` | None | Allowed Methods | ✅ Yes |

- `GET`, `HEAD`, `OPTIONS`, and `DELETE` **MUST NOT** modify resources.

- `PUT` and `DELETE` **MUST** be idempotent to ensure safe retries.

- `PATCH` is `NOT` idempotent unless explicitly designed to be.

- `POST` **MUST** be used for non-idempotent operations such as resource
    creation.

## HTTP request headers

PIs **MUST** support and handle the following request headers:

| **HEADER** | **DESCRIPTION** |
| --- | --- |
| `Authorization` | Used for authentication. APIs **MUST** validate this header and reject malformed requests. |
| `Content-Type` | **MUST** be included in requests with a body. Allowed values: *`application/json`, `application/xml`, `multipart/form-data`, `application/x-www-form-urlencoded`*. |
| `Date` | **MUST** be formatted as per RFC 5322, e.g. Tue, *11 Oct 2022 09:27:30 GMT.* |

!!! info "Further reading and information"
    [RFC 5322 - Internet Message Format](https://datatracker.ietf.org/doc/html/rfc5322)

APIs **SHOULD** support the following request headers:

| **HEADER** | **DESCRIPTION** |
| --- | --- |
| `Accept` | Specifies the response format. Default: *`application/json`*. |
| `Access-Control-Request-Method` | Used in CORS preflight requests to indicate the intended HTTP method. |

APIs **MAY** support additional request headers:

| **HEADER** | **DESCRIPTION** |
| --- | --- |
| `x-api-key` | A legacy authentication method. **MAY** be used only when legacy support is required. Prefer Authorization |
| `X-Audit-Consent` | JSON-encoded FHIR consent resource (base64, max 8KB). |
| `X-Audit-Device` | FHIR identifier for the client device (base64, max 8KB). |
| `X-Au dit-Organisation` | FHIR identifier for the client organisation (base64, max 8KB). |
| `X-Audit-User` | FHIR identifier for the authenticated user (base64, max 8KB). |
| `X-Au thenticated_User` | Identifies the client system for auditing. |
| `Cache-Control` | Controls caching (e.g. *`no-store`*). |
| `Connection` | Manages connection behaviour (e.g. *`keep-alive`*). |
| `If-Match`, `If-None-Match` | Used for optimistic concurrency control with resource updates. |
| `Origin` | If present, APIs **MUST** validate it against a list of allowed origins to ensure security. |
| `X-Request-Id` | A unique identifier for the API request. If not provided by the client, this identifier **MAY** be generated in the API Gateway. |

## HTTP response headers

APIs **SHOULD** return the following response headers:

| **HEADER** | **DESCRIPTION** |
| --- | --- |
| `Cache-Control` | Controls caching (e.g. *`no-store` or `private, max-age=3600`*). |
| `Content-Security-Policy` | Defines security policies to mitigate XSS and injection (e.g. *`frame-ancestors 'none'`*). |
| `Content-Type` | Specifies the response media type (e.g. *`application/json` or `application/xml`*). Used only if a message body is returned. |
| `Location` | On successful resource creation Post, the API **MUST** return a `201 CREATED` status and a Location header with the new resource's relative URL. |
| `Request-Id` | Echoes the unique request identifier provided by the client. |
| `Strict-Transport-Security` | Enforces HTTPS (e.g. *`max-age=31536000; includeSubDomains`*). |
| `WWW-Authenticate` | Specifies the required authentication method (e.g. *`Bearer realm="nhswales365", authorization_uri="..."`*). |
| `X-Content-Type-Options` | Prevents MIME sniffing (e.g. *`nosniff`*). |
| `X-Frame-Options` | Prevents clickjacking (e.g. *`SAMEORIGIN` or `DENY`*). |

The following optional response headers **MAY** apply:

| **HEADER** | **DESCRIPTION** |
| --- | --- |
| `Access-Control-Allow-Origin` | Specifies allowed origins for web access. If used, the value **MUST** be non-wildcard (i.e., *not \**). |
| `Content-Security-Policy` | Restricts content sources (e.g. *`default-src 'none'`*). |
| `Date` | Response timestamp in RFC 5322 format (e.g. *`Tue, 11 Oct 2022 09:27:31 GMT`*). |
| `ETag` | Indicates the resource version. Used with `If-Match` / `If-None-Match` for optimistic concurrency control. |
| `Expires` | The date/time after which the response is considered stale (RFC 5322 format). |
| `Feature-Policy` | Defines permitted client-side features (e.g. *`none`*). |
| `Referrer-Policy` | Specifies the level of referrer information to include (e.g. *`no-referrer`*). |
| `Retry-After` | Indicates when a client should retry a failed request (expressed in seconds or as a date - RFC 5322 format. RFC 5322 is **RECOMMENDED**. |

!!! tip "Practical tips"
    Additional headers **MAY** be added or modified by the API gateway
    to [deprecate or retire](api-management.md) an API or apply
    [rate limiting](api-management.md), for example. Speak to the platform
    team for more help.

!!! info "Further reading and information"
    [RFC 5322 - Internet Message Format](https://datatracker.ietf.org/doc/html/rfc5322)

## Return HTTP status codes

The server **MUST** return the correct HTTP status code for each API
operation, as per RFC 9110. The table below lists common status codes,
but others **MAY** be used if needed.

- "✅ Yes" means the status code applies to that operation.

- An empty cell means the code is not usually used for that operation.

| **HTTP STATUS CODE** | **GET (COLLECTION)** | **GET (RESOURCE)** | **POST (COLLECTION)** | **PUT (RESOURCE)** | **PATCH (RESOURCE)** | **DELETE (RESOURCE)** |
| --- | --- | --- | --- | --- | --- | --- |
| `200 OK`                     | ✅ Yes | ✅ Yes |  | ✅ Yes | See caveats below |  |
| `201 CREATED`                |  |  | ✅ Yes |  |  |  |
| `202 ACCEPTED`               |  |  | ✅ Yes | ✅ Yes | ✅ Yes | ✅ |
| `304 NOT MODIFIED`           | See caveats below |  |  |  |  |  |
| `400 BAD REQUEST`            | ✅ Yes | ✅ Yes |         |        |         |        |
| `401 UNAUTHORIZED`           | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| `403 FORBIDDEN`              | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| `404 NOT FOUND`              | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| `405 METHOD NOT ALLOWED`     | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| `408 REQUEST TIMEOUT`        | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| `409 CONFLICT`               |  |  | ✅ Yes | ✅ Yes |  |  |
| `412 PRECONDITION FAILED`    |  |  | ✅ Yes | ✅ Yes | ✅ Yes | See caveats below |
| `415 UNSUPPORTED MEDIA TYPE` | ✅ Yes | ✅ Yes | ✅ Yes | ✅ | Yes | ✅ Yes |
| `422 UNPROCESSABLE ENTITY`   |  |  | ✅ Yes | ✅ Yes | ✅ Yes |  |
| `428 PRECONDITIONS` **REQUIRED** |  |  | ✅ Yes | ✅ Yes | ✅ Yes | See caveats below |
| `429 TOO MANY REQUESTS`      | See caveats below |  |  |  |  |  |
| `500 INTERNAL SERVER ERROR`  | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| `501 NOT IMPLEMENTED`        | See caveats below |  |  | ✅ Yes | ✅ Yes |  |
| `502 BAD GATEWAY`            | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| `503 SERVICE UNAVAILABLE`    | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| `504 GATEWAY TIMEOUT`        | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |

### Caveats and edge cases

- While `PATCH` can return 200 `OK` with the updated resource, 202
    `ACCEPTED` is preferred for asynchronous processing. But some
    implementations **MAY** choose to return `200 OK` instead.

- `304 NOT MODIFIED` applies only when the API supports caching with
    conditional GET requests. The server **MAY** return `304 NOT MODIFIED`
    if the client's cached version is still valid.

- Use `409 CONFLICT`when there's a conflict with the current state of
    the target resource. Use `422 UNPROCESSABLE ENTITY` when the server
    understands the request but can't process it due to semantic
    errors.

- Use `409 CONFLICT`when there's a conflict with the current state of
    the target resource. Use `422 UNPROCESSABLE ENTITY` when the server
    understands the request but can't process it due to semantic
    errors.

- While `415 UNSUPPORTED MEDIA TYPE` is typically used for `POST`, `PUT` and
    `PATCH`, it **MAY** apply to `GET` if a body is sent with an unsupported
    media type --- although this is rare.

- `412 PRECONDITION FAILED` and `428 PRECONDITIONS` **REQUIRED** are typically
    used for `POST`, `PUT` and `PATCH`. However, some designs **MAY** also
    apply them to `DELETE` if preconditions are enforced.

- Use `428 PRECONDITIONS` **REQUIRED** when the server requires the request to
    be conditional, typically to prevent the "lost update" problem. Use
   `412 PRECONDITION FAILED` when a precondition specified in the request
   isn't met.

- Typically our API platform will apply rate limiting and return
    `429 TOO MANY REQUESTS` when appropriate.

- Some designs **MAY** extend the use of `501 NOT IMPLEMENTED` to other
    methods if a particular method is not supported by the server.

!!! info "Further reading and information"
    [RFC 9110: HTTP Semantics - Status Codes (rfc-editor.org)](https://www.rfc-editor.org/rfc/rfc9110.html#name-status-codes)
