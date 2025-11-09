# Paging

When performing a **GET** operation on a collection, the server **MAY**
return a partial result. The server **SHOULD** apply paging to
collections with an unbounded number of items.

## Token-based paging (recommended)

Token-based paging, where the server controls the paging sequence, is
**RECOMMENDED**. Common approaches include cursor, keyset, and seek
paging.

The server **SHOULD** supply a continuation token in the href field of
the [navigation link](paging.md) and assign it to a query parameter
named token. This token **MUST** be an encoded string.

If the client omits the token, the server **MUST** return the first
partial result, eliminating the need to include a page token in the URL
of the first link.

!!! example "Examples of good practice"
    ```json
        GET /{base}/patients?pageOffset=2&pageSize=10&total=true
        // 200 OK
        Content-Type: application/json; charset=utf-8
        {
        "meta": {
            "pageOffset": 2,
            "pageSize": 10,
            "total": 40
        },
        "data": {
            "pageOffset": 2,
            "pageSize": 10,
            "patients": [
            {
                "NHSNumber": "9991234566"
                // ... other patient details ...
            },
            {
                "NHSNumber": "9991234567"
                // ... other patient details ...
            }
            // ... 8 more patient records ...
            ]
        },
        "links": [
            {
            "href": "/patients?page=2&pageSize=10",
            "rel": "self"
            },
            {
            "href": "/patients?page=1&pageSize=10",
            "rel": "first"
            },
            {
            "href": "/patients?page=1&pageSize=10",
            "rel": "prev"
            },
            {
            "href": "/patients?page=3&pageSize=10",
            "rel": "next"
            },
            {
            "href": "/patients?page=4&pageSize=10",
            "rel": "last"
            }
        ]
        }
    ```

## Client-driven paging

Allowing clients to control paging provides flexibility but may be less
efficient. The server **MAY** allow clients to supply an offset (or
pageOffset) integer value as the starting point.

If omitted, the server **MUST** use default values of offset=0 or
pageOffset=1. If the value is greater than or equal to the number of
resources, the server **MUST** return an empty collection.

If the value is invalid, the server **SHOULD** return a 400 BAD REQUEST
HTTP status code.

The server **SHOULD** include the offset values in the response ---
whether explicitly provided or not --- to maintain context for the
client.

!!! example "Examples of good practice"
    ```json
        GET /{base}/patients?pageOffset=2&pageSize=10&total=true
        // 200 OK
        Content-Type: application/json; charset=utf-8
        {
        "meta": {
            "pageOffset": 2,
            "pageSize": 10,
            "total": 40
        },
        "data": {
            "pageOffset": 2,
            "pageSize": 10,
            "patients": [
            {
                "NHSNumber": "9991234566",
                // ... other patient details ...
            },
            {
                "NHSNumber": "9991234567",
                // ... other patient details ...
            }
            // ... 8 x more patient records ...
            ]
        },
        "links": {
            "self": {
            "href": "/patients?page=2&pageSize=10",
            "rel": "self"
            },
            "first": {
            "href": "/patients?page=1&pageSize=10",
            "rel": "first"
            },
            "prev": {
            "href": "/patients?page=1&pageSize=10",
            "rel": "prev"
            },
            "next": {
            "href": "/patients?page=3&pageSize=10",
            "rel": "next"
            },
            "last": {
            "href": "/patients?page=4&pageSize=10",
            "rel": "last"
            }
        }
        }
    ```

## Paging stability

When implementing paging, the server **MUST** ensure the following:

- The server **MUST** sort on a unique value. This may require sorting
    on an additional value (typically a primary key) if necessary.

- Sorting and filtering parameters **MUST** be consistent across pages
    to maintain predictability.

- Query options **MUST NOT** be changed while iterating over a partial
    result set.

(See the sections on [Filtering](filtering.md), [Sorting](sorting.md) and
[Compound Collections](compound-collection-operations.md) for more
information.)

## Page links

The server **MUST** indicate a partial result by including navigation
links as JSON objects within the links array. Each JSON object
**SHOULD** contain rel and href  fields.

The rel field **SHOULD** be restricted to the following values: self,
first, prev, next and last.

The absence of a next link indicates that there are no more results.

The absence of a prev link typically indicates the start of the result
set, although it **MAY** be omitted if reverse paging is expensive or
impractical.

Similarly, the server **MAY** omit the last link if providing it is
costly or impractical.

href fields in links **MUST** contain a URL with any appropriate query
parameters.

## Page size

The server **MAY** allow clients to specify the number of items returned
using the pageSize query parameter. It **MUST** either use this value or
apply a default pageSize when none is specified.

The server **MUST** set a default pageSize and an upper limit
(maxPageSize) for each resource collection. These values **SHOULD** be
determined based on reasonable estimates of default and maximum request
times and payload sizes.

Clients **MAY** specify an integer value for pageSize or request the maximum
allowed by setting pageSize to maxPageSize.

If pageSize is not a non-negative integer or exceeds maxPageSize, the
server **SHOULD** return a 400 BAD REQUEST HTTP status code.

The server **MAY** return fewer items than specified by the pageSize
when returning the last page.

The server **SHOULD** include the pageSize value in the links object
within the response, regardless of whether it was explicitly provided or
set by default.

## Total

The server **MAY** allow clients to request the total number of matches
by providing a total query parameter.

If the client specifies total=true, the server **SHOULD** return the
total number of matches in the total field at the root of the JSON
response.

By default, the total parameter **MUST** be set to false.

!!! tip "Practical tips"
    total indicates the overall number of results that match the request, not the number of resources returned in the current response..

## Paging nested resources

The server **MAY** support client paging of nested resources and
**SHOULD** provide the necessary navigation links for such cases.

## Paging implementation

When implementing paging, the server **SHOULD** consider the following
key aspects:

- Establish a method for handling updates to maintain data consistency
    and accuracy.

- Implement efficient data retrieval mechanisms to minimise
    performance impact.

- Ensure secure encoding of continuation tokens to protect client
    privacy and data integrity.
