# Filtering

## Field selection

Endpoints **SHOULD** return a default set of fields, but the server
**MAY** allow clients to customise the response, using the `fields` query
parameter. This helps avoid retrieving unnecessary data.

However the server **MUST** always return mandatory fields specified in
the model schema, even if not requested. For example the `conditions`
field is returned even if not specified in the query.

!!! example "Examples of good practice"
    ```json
        GET /{base}/patients/9991234566?fields=NHSNumber,firstName,lastName
        // 200 OK

        Content-Type: application/json; charset=utf-8
        {
            "patient": {
                "NHSNumber": "9991234566",
                "firstName": "Humphrey",
                "lastName":  "Appleby ",
                "conditions": [
                    {
                        "id": "1",
                        "name": "Hypertension"
                    }
                ]
            }
        }
    ```

## Simple filtering

The server **MAY** allow clients to search specific fields by specifying
the field name in the query.

!!! example "Examples of good practice"
    ```json
        GET /{base}/patients?lastName=Appleby&fields=NHSNumber,firstName,lastName
        // 200 OK
        Content-Type: application/json; charset=utf-8
        {
            "patients": [
            {
                "NHSNumber": "9991234566",
                "firstName": "Humphrey",
                "lastName": "Appleby",
                "conditions": [
                    {
                        "id": "1",
                        "name": "Hypertension"
                    },
                    {
                        "id": "2",
                        "name": "Diabetes"
                    }
                ]
            },
            {
                "NHSNumber": "9991234599",
                "firstName": "Lady",
                "lastName": "Appleby",
                "conditions": [
                    {
                        "id": "1",
                        "name": "Hypertension"
                    }
                ]
            }]
        }
    ```

The server **MAY** allow clients to combine search parameters and filter
by relational fields. This allows for advanced searches across related
data.

!!! example "Examples of good practice"
    ```json
        GET /{base}/patients?lastName=Appleby& expand=conditions&condition.name=diabetes
        // 200 OK
        Content-Type: application/json; charset=utf-8
        {
            "patients": [
            {
                "NHSNumber": "9991234566",
                "firstName": "Humphrey",
                "lastName": "Appleby",
                "conditions": [
                    {
                        "id": "1",
                        "name": "Hypertension"
                    },
                    {
                        "id": "2",
                        "name": "Diabetes"
                    }
                ]
            }
        ]
        }
    ```

## Advanced filtering

To enable more advanced filtering logic, the server **MAY** support
OData 4.0-compliant query parameters. These allow clients to specify
filtering expressions that are evaluated for each resource in the
collection, including only items where the expression evaluates to
*true*.

The following operators **MUST** be supported with the *filter* query:

| **OPERATOR GROUP** | **OPERATOR** | **DESCRIPTION** |
| --- | --- | --- |
| **COMPARISON** | `eq` | Equal |
|  | `ne` | Not equal |
|  | `gt` | Greater than |
|  | `ge` | Greater than or equal |
|  | `lt` | Less than |
|  | `le` | Less than or equal |
| **LOGICAL** | `and` | Logical and |
|  | `or` | Logical or |
|  | `not` | Logical negation |
| **GROUPING** | `()` | Precedence grouping |

!!! example "Examples of good practice"
    GET *{base}*/patients?filter=lastName eq Appleby and age ge 53

## Elasticsearch and lucene

When using Elasticsearch, Lucene, or equivalent search products, the
server **SHOULD** align with the syntax of the chosen product.
Alternatively, consider using well-documented, standardised mechanisms
such as OData filter syntax or a GraphQL service.
