# Sorting

The server **MAY** support sorting of result sets by accepting a
comma‐separated list of expressions via the sort query parameter. The
server **SHOULD** honour the client's preferences.

By default the server **SHOULD** sort in ascending order but **MAY**
sort in descending order if the client prefixes an expression with a
dash (-).

NULL values **MUST** be treated as less than non-NULL values.

Items **MUST** be sorted according to the order of expressions provided.
The first expression defines the primary sort order; for items with
identical values in the first expression, the second expression defines
the secondary order, and so on.

!!! example "Examples of good practice"
    ```json
        GET /{base}/patients?sort=-lastName
        // 200 OK
        Content-Type: application/json; charset=utf-8
        "data": {
            "patients": [
            {
                "NHSNumber": "9991234568",
                "firstName": "Bernard",
                "lastName": "Woolley",
                // ... other patient details ...
            },
            {
                "NHSNumber": "9991234567",
                "firstName": "Jim",
                "lastName": "Hacker",
                // ... other patient details ...
            },
            {
                "NHSNumber": "9991234566",
                "firstName": "Humphrey",
                "lastName": "Appleby",
                // ... other patient details ...
            }
            // ... more patients ...
            ]
        }
        }
    ```

## Compound collection operations

When paging, filtering & sorting operations are performed together, the
evaluation order **MUST** be:

1. **Filtering:** All filtering expressions, including range queries,
    **MUST** be applied using an AND operation.

2. **Sorting:** The filtered list **MUST** be sorted according to the
    specified sort criteria.

3. **Paging:** The sorted, filtered list **MUST** then be paged. This
    applies to both token-based and client-driven paging.
