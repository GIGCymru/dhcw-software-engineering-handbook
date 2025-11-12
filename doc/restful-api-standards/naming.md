# Naming

## Resource names

Resource names **SHOULD** be clear, descriptive and written in
*lowerCamelCase*. Use plural nouns in URLs and to identify resource
collections in JSON payloads. Use the singular form to identify an
individual resource in a JSON payload.

!!! example "Examples of good practice"
    `/{base}*/patients/{id*}`

    `/{base}*/Patient/{id*}`

    `/{base}*/getPatient/{id*}`

Prefer nouns to verbs, even if the noun is not immediately obvious.

!!! example "Examples of good practice"
    `/{base}*/uk-who/calculation`

    `/{base}*/uk-who/calculate`

## Resource identifiers

Resource identifiers **MUST** serve as unique references for resources.
It is **RECOMMENDED** to use the field name "*id*" or to concatenate
the resource name with "*Id*" when referencing these identifiers.

Resource identifiers **MUST** be URL safe and not expose implementation
details such as database primary keys.

## Resource fields

Resource fields **MUST** be descriptive and use *lowerCamelCase*.

!!! example "Examples of good practice"
    ```json
        {
        "data": {
            "patients": [
            {
                "firstName": "Humphrey",
                // ... other patient details ...
            },
                // ... more patients ...
            ]
        }
    }
    ```

## Query parameters

Query parameters **SHOULD** be written in *lowerCamelCase*.

You **SHOULD NOT** define query parameters with names that differ only
in case.

The server **SHOULD NOT** be case sensitive when processing query
parameters.

When query parameters are treated as strings they present an opportunity
for injection attacks. To minimise risk, the server **SHOULD** constrain
the values of string filters to enumerations or regular expressions.

## Reserved names

You **SHOULD** adhere to the defined behaviour for query parameters as
described in this standard. These names are reserved for their intended
purposes and **MUST NOT** be repurposed.

!!! info "Further reading and information"
    [Microsoft Graph REST API Guidelines](https://github.com/microsoft/api-guidelines/blob/vNext/graph/GuidelinesGraph.md)
