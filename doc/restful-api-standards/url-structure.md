# Url structure

You **SHOULD** follow the structure below to ensure API endpoints are
predictable & hierarchical.

| **HEADER** | **DESCRIPTION** |
| --- | --- |
| Scheme / Protocol | **MUST** always be https://. |
| Host / Domain | The platform team manages the domain structure, which **MAY** include a global API context in the fully qualified domain name (FQDN), followed by an environment and subdomain. |
| Base path / Context | Represents a grouping of resource endpoints. Sometimes referred to as a Namespace. |
| Version | Versioning requirements and URL rules are described in [Versioning](api-management.md). |
| Resource / Resource collection | Represents the primary resource or resource collection exposed by the API. |
| Resource identifier | A placeholder for the unique identifier of a resource within a collection. |
| ?\[*Query parameters*\] | Used to filter and modify requests. Refer to the [Query Parameters](naming.md) section for reserved names. |

!!! example "Examples of good practice"
    `https://api.test.wales.nhs.uk/appointmentsService/patients?sort=firstName`

    `https://api.test.wales.nhs.uk/appointmentsService/patients/{id}/conditions`

    `https://api.test.wales.nhs.uk/appointmentsService/GPPractices/{id}/slots/{id}`

    `https://api.test.wales.nhs.uk/referenceData/v2/GPPractices/{id}/Practitioners/{id}`

    `https://api.test.wales.nhs.uk/appointmentsService/patients?sort=firstName`

!!! tip "Practical tips"
    Further examples in this document shorten the full URL structure for brevity.
