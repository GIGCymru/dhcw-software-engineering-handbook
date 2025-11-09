# Essential good practice checklist

| **No.** | **Checklist Item** |  | **Section Heading** | **Exceptions** |
| --- | --- | --- | --- | --- |
| 1 | APIs conform to FHIR R4. | ☐ | FHIR (Fast Healthcare Interoperability Standards) | Suitable FHIR R4 p rofiles may be unava ilable. |
| 2 | You have identified the resource data type. | ☐ | Data Classification |  |
| 3 | You have an OpenAPI specification kept in source control. | ☐ | OpenAPI Specification |  |
| 4 | You structure API endpoints for predictability. | ☐ | URL Structure |  |
| 5 | You use HTTP verbs to define operations. | ☐ | HTTP Implementation |  |
| 6 | APIs return correct HTTP status codes. | ☐ |  |  |
| 7 | You follow FHIR or our JSON payload rules and structure. | ☐ | Payload Rules JSON Response Payload Structure | Unless following the FHIR specification |
| 8 | You apply Paging to collections with an unbounded number of items. | ☐ | Paging |  |
| 9 | You return errors in a common format. | ☐ | Error Reporting |  |
| 1 0 | You publish a transient fault contract.. | ☐ | Handling Transient Faults |  |
| 1 1 | You follow naming conventions and use standard query parameters. | ☐ | Naming |  |
| 1 2 | You define a maximum response time. | ☐ | Performance and Response Times |  |
| 1 3 | You deploy APIs to an API gateway. | ☐ | API Management |  |
| 1 4 | API clients authenticate using OAuth and OIDC. | ☐ | Authentication and Authorisation |  |
| 1 5 | You apply the correct restrictions on data usage. | ☐ | Restrictions on Data Use |  |
| **No.** | **Checklist Item** |  | **Guide or standard** | **Exceptions** |
| 1 6 | APIs implement *ping* and service status endpoints. | ☐ | Ping and Service Status |  |
| 1 7 | You follow our deprecation and retirement policies. | ☐ | Deployment |  |
| 1 8 | API use semantic versioning. | ☐ | Versioning |  |
| 1 9 | You publish APIs to an API catalogue. | ☐ | Cataloguing |  |
| 2 0 | You monitor APIs and apply rate limits where appropriate. | ☐ | Auditing, Tracing and Monitoring |  |
| 2 1 | You deploy API using CI / CD pipelines to an API gateway. | ☐ | Deployment |  |
| 2 2 | You write Test reports for every major, minor and patch version of your API. | ☐ | Test Summary Report |  |
| 2 3 | Test reports include security testing and code coverage metrics. | ☐ |  |  |
| 2 4 | You follow our documentation recommendations. | ☐ | Documentation |  |
