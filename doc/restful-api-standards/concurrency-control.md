# Concurrency control

To prevent accidental overwrites of updates, design your concurrency
control model carefully to handle transient faults appropriately.

The server **SHOULD** ensure that clients include an If-Match header
when making changes to resources that might be updated concurrently.

When a client sends an If-Match header with a valid ETag value:

- The server **MUST** check if the provided ETag matches the current
    ETag of the resource.

- If they match, the server processes the request and returns a 2xx
    HTTP status code (for example, 200 OK) indicating success.

- If they do not match, the server **MUST** return a 412 PRECONDITION
    FAILED status code to indicate a conflict.

If a client does not include the If-Match header:

- The server **MUST** respond with a 428 PRECONDITION **REQUIRED** HTTP
    status code, indicating that the If-Match header is required.

- The response **MUST** include a clear message instructing clients to
    include the If-Match header in future requests for the resource.

You **MUST** describe in your API documentation which resources require
the use of the If-Match header.

!!! info "Further reading and information"
    [Testing for lost updates](../testing-lost-updates/introduction.md)
