# Documentation

Good documentation makes our APIs easier to use. Even without a
technical writer, this guide shows you how to create clear,
well-structured API docs.

!!! info "Further reading and information"
    [Documenting APIs - GOV.UK](https://www.gov.uk/guidance/how-to-document-apis)

    [Documenting APIs: A guide for technical writers and engineers](https://idratherbewriting.com/learnapidoc/)

## Writing style

You **SHOULD** follow DHCW's Writing checklist, ensuring that you:

- Write short sentences.

- Talk directly to your user by using 'you' and active verbs.

- Use the active voice and plain language.

- Avoid using 'home-grown' terms that are not industry standard.

!!! info "Further reading and information"
    [DHCW Writing checklist](https://nhswales365.sharepoint.com/sites/DHCW-Intranet/SitePages/Writing-style-guide.aspx)

## OpenAPI specification

You **SHOULD**:

- Describe your API using the OpenAPI (OAS) definition, version 3. OAS
    is a global standard for describing RESTful APIs in a human and
    machine-readable format.

- Provide OpenAPI definitions in YAML, as described in the next
    section.

- Add a monitored email address to the info object of the OpenAPI
    definition to allow consumers to contact you with issues or
    comments.

- Include the full semantic version number in the info object of the
    OpenAPI definition.\
    Store your OpenAPI specification in source control and keep it up to
    date.

!!! info "Further reading and information"
    [Semantic Versioning 2.0.0 \| Semantic Versioning](https://semver.org/)

## Document structure

You **SHOULD** organise your API documentation. This section provides a
**RECOMMENDED** structure:

!!! example "Examples of good practice"
    ```sh
        ├── system.yml
        ├── {api-id}/
        │   ├── api.yml
        │   ├── spec/
        │   │   ├── open-api.yml or service.wsdl
        │   │   └── example-requests/
        │   └── user-guide/
        │       └── (see the user-guide section for more information)
    ```

### System.yml

`system.yml` describes the underlying service that exposes the API
endpoints. Information that might otherwise be repeated across related
APIs can be added to the description. It contains the following fields:

| **FIELD** | **MAX CHARACTERS** | **DESCRIPTION** |
| --- | --- | --- |
| `short-name` | 10 | Name or abbreviation to be used as a prefix when displayed in the API catalogue. |
| `description` | 150 | What the service does. |

### Api.yml

`api.yml` provides a brief overview of:

- What your API does.

- Whether your API is in the alpha, beta or in production.

- Who can use your API, and any restrictions on using it or its data.

| **FIELD** | **MAX CHARACTERS** | **DESCRIPTION** |
| --- | --- | --- |
| `title` | 80 | Name or abbreviation to be used as a prefix when displayed in the API catalogue. |
| `description` | 150 | What the service does. |
| `overview` | 800 | Provide brief details for each of the following: - ***What the API does***: A more detailed description with specifics about data sources and formats. - ***Who will use it and why***: Provide examples of typical consumers and why they would use the API. - ***Where it's available***: Mention any restrictions on use. |
| `owner` | 30 | Email address for main point of contact for information about the API. |
| `type` | N/A | `FHIR`, `REST` `SOAP`, `HL7v2`, `HL7v3` `Solr` or `GraphQL` |
| `status` | N/A | `Alpha`, `Beta` `Stable`, `Legacy`, `Deprecated` or `Retired` |
| `data type` | N/A | `Public`, `Business Confidential` `Sensitive` or `Highly Sensitive` |

### Spec/open-api.yml

Include an `open-api.yml` file in the `spec` folder. You **SHOULD** format
descriptions in markdown so that the platform team can generate HTML
documentation in the API [catalogue](api-management.md).

You **SHOULD NOT** include the actual endpoint of your API server.
Replace it with *<https://private.url>*.

You **MAY** include examples in the `open-api.yml` file.

### Spec/service.wsdl

If you are publishing a legacy SOAP service, you **SHOULD** provide a
service.wsdl document in the spec/example-requests folder. Contact the
platform team for more information.

### User-guide

Although documentation can be auto generated from the `open-api.yml` or
`service.wsdl`, you **MAY** enhance it by adding a user guide as markdown
files.

!!! example "Examples of good practice"
    ```sh
        user-guide/
        ├── overview.md
        ├── quickstart.md
        ├── how-to/
        │   ├── 1-{description}.md
        │   └── n-{description}.md
        ├── concepts/
        │   ├── {concept}.md
        │   └── {concept}.md
    ```

### Overview.md -- introduce your API

You **SHOULD** start with a brief overview that explains what the API
does and how it works. Focus on technical details suitable for
developers and emphasise any prerequisites or essential concepts.

!!! example "Examples of good practice"
    *'A FHIR API that lets you retrieve ValueSets resources of SNOMED concepts.'*

    *//...how it works*

    *'A SOAP API that triggers a questionnaire to be sent.'*

    *//...how it works*

### Quickstart.md - how to get started

You **SHOULD** create a concise section that guides users through the
quickest and simplest method of obtaining an example response from your
API. Assume the reader is familiar with the necessary technology but
highlight any advanced or unconventional steps, including potential
pitfalls or important considerations.

### How-to -- task-based guides for common scenarios

You **SHOULD** provide task-based examples in a user-friendly style to
help users with common integration tasks. Write them in the same style
as the quickstart; however, these examples can be longer and more
complex. Examples **SHOULD** have the following characteristics:

- Begin with a front-loaded title that starts with a verb.

- Focus on helping users complete one task.

- Tell users what they need to do, not how the system works.

- Use numbered steps for clarity.

- Include example code and descriptions for request parameters and
    response fields.

- Provide links to any subsequent tasks the user needs to complete.

!!! example "Examples of good practice"
    *'**Retrieve ValueSets resources of SNOMED concepts** -- using a FHIR API'*

    *'**Trigger the sending of a questionnaire** -- using a SOAP API'*

!!! tip "Practical tips"
    Avoid duplicating basic info about the API. Link to the Getting started
    section instead.

### Concepts

You **SHOULD** explain any essential concepts, such as document metadata
standards. If a concept refers to an external source you **SHOULD**
provide a link.

### Error response codes

You **SHOULD** place error responses near the endpoint documentation or
at the end of the API reference. Even if you anticipate only standard
responses, such as 400 NOT FOUND or 200 OK, you **MUST** clarify how
they relate to your API.

!!! tip "Practical tips"
    - Store the OpenAPI definition in the docs folder of your code repository.

    - Create custom tasks in your CI/CD pipeline to publish API documentation to Apigee.

## Developer portal

We provide two developer portals for managing and publishing APIs:

| **FEATURE** | **DESCRIPTION** | **URL** |
| --- | --- | --- |
| Internal Developer Portal | Allows developers to browse the internal API catalogue, obtain API keys, and test APIs before external publication. | <https://apim-apigee-test-nhswales.apigee.io/> |
| External Developer Portal | Central hub for publishing and managing API documentation. Provides a user-friendly interface for API consumers. | [Home - NHS Wales Digital Platform](https://digitalplatform.nhs.wales/) |

When you are ready to publish your API documentation, contact the
platform team for guidance.

## Software development kits (sdks)

Creating a client-side SDK takes effort, but it can simplify integration
for your users. If you provide an SDK with your API, you **MUST** test it
thoroughly to ensure reliability.

!!! tip "Practical tips"
    Understand your users' needs. A .NET client might not be useful to a Java developer!

## Exceptions

Standards provide valuable guidance, but there may be rare exceptions.
Principal and Lead Software Developers have discretion in such cases.
