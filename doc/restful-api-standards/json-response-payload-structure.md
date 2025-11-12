# JSON response payload structure

## Response format

JSON response payloads **SHOULD** adhere to the following structure:

```json
    ├── meta (Object, 0..1)
    ├── data (Object, 0..1)
    ├── links (Object, 0..1)
    │         ├── href (String, 1..1)
    │         └── rel (String, 1..1)
    └── errors (Object, 0..1)
            ├── type (String, 1..1)
            ├── title (String, 1..1)
            ├── status (Number, 1..1)
            ├── detail (String, 1..1)
            ├── instance (String, 0..1)
            └── invalidParams (Array, 0..1)
```

| **ELEMENT** | **TYPE** | **CARDINALITY** | **DESCRIPTION** |
| --- | --- | --- | --- |
| meta | Object | 0..1 | Contains metadata (e.g. pagination details such as offset, pageOffset, pageSize, total) |
| data | Object | 0..1 | Contains the primary resource or a resource collection. When returning a single resource, you **MAY** place the resource directly inside data without nesting. |
| links | Object | 0..1 | Provides links to related resources or partial results. **SHOULD** only identify resources in the same versioned Namespace. |
| errors | Object | 0..1 | Contains error details as per *RFC 7807*. If present no other top-level objects should be returned.. |
| href | String | 1..1 | The URL to a nested resource or the next set of items. |
| rel | String | 1..1 | Relation value. Use a standard Link Relation Type if available. |
| type | 1..1 | String | URL to the API's error documentation. |
| title | 1..1 | String | A short, human-readable summary of the error. |
| status | 1..1 | Number | Status code (e.g. 400 BAD REQUEST). |
| detail | 1..1 | String | Detailed error description for troubleshooting. |
| instance | 0..1 | String | URL or path to the resource that caused the error. |
| invalidParams | 0..1 | Array | Array of objects specifying invalid parameters and reasons. |

## Get operation on an individual resource

For a GET operation on an individual resource, the response **SHOULD**
enclose the primary resource within a data object. The outer property
name uses the singular form of the resource name.

Direct:

!!! example "Examples of good practice"
    ```json
        GET /{base}/patients/9991234566
        // 200 OK
        Content-Type: application/json; charset=utf-8
        {
            "data": {
                "NHSNumber": "9991234566",
                "firstName": "Humphrey",
                "lastName": "Appleby"
            }
        }
    ```

Nested:

!!! example "Examples of good practice"
    ```json
        GET /{base}/patients/9991234566
        // 200 OK
        Content-Type: application/json; charset=utf-8
        {
            "data": {
                "patient": {
                "NHSNumber": "9991234566",
                "firstName": "Humphrey",
                "lastName": "Appleby",
                // ... other patient details ...
                }
            }
        }
    ```

## Get operation on a collection of resources

For a collection of resources, the response **SHOULD** enclose the
resource collection within a data object, using the plural form of the
resource name.

A collection with 0 items **SHOULD** return HTTP 200 OK rather than 404
NOT FOUND

Non-empty collection example:

!!! example "Examples of good practice"
    ```json
        GET /{base}/patients
        // 200 OK
        Content-Type: application/json; charset=utf-8
        {
            "data": {
                "patients": [
                {
                    "NHSNumber": "9991234566",
                    "firstName": "Humphrey",
                    "lastName": "Appleby",
                    // ... other patient details ...
                },
                {
                    "NHSNumber": "9991234567",
                    "firstName": "Jim",
                    "lastName": "Hacker",
                    // ... other patient details ...
                },
                // ... more patients ...
                ]
            }
        }
    ```

Empty collection - valid example:

!!! example "Examples of good practice"
    ```json
        GET /{base}/patients
        // 200 OK
        Content-Type: application/json; charset=utf-8
        {
            "data": []
        }
    ```

Empty collection - invalid example:

!!! danger "Examples of practices to avoid"
    ```json
        GET /{base}/patients
        // 404 NOT FOUND
        Content-Type: application/json; charset=utf-8
        {
            "data": []
        }
    ```

## Get operation on nested resources

For nested resources, the response **SHOULD** either embed the nested
resources or provide navigable links in the links object. See also
[Returning related resources using query
parameters](retrieving-related-data.md).

Embedded resources example (using the expand parameter):

!!! example "Examples of good practice"
    ```json
        GET /{base}/patients/9991234566?expand=practitioners,conditions
        // 200 OK
        Content-Type: application/json; charset=utf-8
        {
            "data": {
                "patient": {
                "NHSNumber": "9991234566",
                "firstName": "Humphrey",
                "lastName": "Appleby",
                // ... other patient details ...
                "practitioner": {
                    "id": "123",
                    "name": "Dr. Liz Asher",
                    // ... other details of the primary care provider ...
                },
                "conditions": [
                    {
                    "id": "1",
                    "name": "Hypertension",
                    // ... other details of the condition ...
                    },
                    {
                    "id": "2",
                    "name": "Diabetes",
                    // ... other details of the condition ...
                    }
                    // ... more condition records ...
                ]
                }
            }
        }
    ```

Linked resources example (using the include parameter):

!!! example "Examples of good practice"
    ```json
        GET /{base}/patients?include=conditions,practitioners
        // 200 OK
        {
            "data": {
                "patient": {
                "NHSNumber": "9991234566",
                "firstName": "Humphrey",
                "lastName": "Appleby",
                // ... other patient details ...
                }
            },
            "links": {
                "practitioner": {
                "href": "/practitioners/123",
                "rel": "practitioner",
                "NHSNumber": "9991234566"
                },
                "conditions": [
                {
                    "href": "/conditions/1",
                    "rel": "condition",
                    "NHSNumber": "9991234566"
                },
                {
                    "href": "/conditions/2",
                    "rel": "condition",
                    "NHSNumber": "9991234566"
                }
                ]
            }
        }
    ```

!!! info "Further reading and information"
    [Link Relations (www.iana.org)](https://www.iana.org/assignments/link-relations/link-relations.xhtml)

## Data operations (POST, PUT & PATCH)

For data operations such as POST, PUT, or PATCH, the request **SHOULD**
include the primary resource data. After a successful POST operation on
a collection, the server **SHOULD** create and return a unique resource
identifier.

Example request:

!!! example "Examples of good practice"
    ```json
        POST /{base}/patients
        Host: //some host
        Content-Type: application/json; charset=utf-8
        {
        "data": {
            "patient": {
            // ... patient details ...
            }
        }
        }
    ```

Example response:

!!! example "Examples of good practice"
    ```json
        201 Created
        Location Header: /{base}/patients/{9991234568}
        Content-Type: application/json; charset=utf-8
        {
            "data": {
                "patient": {
                "NHSNumber": "9991234568",  // The server-generated unique identifier
                // ... other patient details ...
                }
            }
        }
    ```

## Returning an error

When returning an error, the server **SHOULD** follow the *RFC 7807*
format. This ensures that error information is provided in a consistent
and standardised manner. See [Error reporting](error-reporting.md) for
more details.

Example request:

!!! example "Examples of good practice"
    ```json
        POST /{base}/patients
        Host: //some host
        Content-Type: application/json; charset=utf-8
        {
            "data": {
                "patient": {
                "NHSNumber": "9991234568",
                "firstName": "Bernard",
                "lastName": "Woolley",
                "dateOfBirth": "1942-01-06",
                "gender": "Male",
                // ... other patient details ...
                }
            }
        }
    ```

Example response:

!!! example "Examples of good practice"
    ```json
        HTTP/1.1 400 Bad Request
        Content-Type: application/problem+json
        {
            "type": "https://example.com/errors/id-not-allowed",
            "title": "ID Not Allowed",
            "status": 400,
            "detail": "Resource identifiers (IDs) are managed exclusively by the server",
            "instance": "/api/patients",
            "invalidParams": [
                {
                "name": "NHSNumber",
                "reason": "NHSNumber should not be provided in the client request."
                }
            ]
        }
    ```

!!! info "Further reading and information"
    [RFC 7807 - Problem Details for HTTP APIs](https://datatracker.ietf.org/doc/html/rfc7807)
