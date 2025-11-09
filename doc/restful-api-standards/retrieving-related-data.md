# Retrieving related data

## Using separate urls for related resources

Endpoints **SHOULD** return only primary resources by default.

To prevent overloading clients, the server **MAY** offer alternative
endpoints to fetch related data.

URLs **SHOULD NOT** exceed two levels of nesting to maintain readability
and usability.

If a resource can be independently accessed without its parent, it
**SHOULD** have its own top-level endpoint.

!!! example "Examples of good practice"
    `{base}/appointmentsService/patients`

    `{base}/appointmentsService/patients/{id}`

    `{base}/appointmentsService/patients/{id}/conditions`

    `{base}/appointmentsService/patients/{id}/conditions/{id}`

    `{base}*/appointmentsService/patients/*{id}*/encounters/*{id}*/observations/*{id}`

## Returning related resources using query parameters

The server **MAY** support include and expand query parameters to
optimise data retrieval.

include **MUST** return navigation links for the specified related
resources.

expand **MUST** embed related data directly within the response.

!!! example "Examples of good practice"
    `{base}/appointmentsService/patients/{id}?include=conditions`

    `{base}/appointmentsService/patients/{id}?expand=practitioners,conditions`

Additional **RECOMMENDATIONS**:

- **Separate URLs vs Query Parameters**: Use query parameters only
    when they add value. For complex data retrieval, consider GraphQL.

- **Balance Performance and Usability**: Overuse of expand can degrade
    performance, while excessive nesting complicates API navigation.

!!! info "Further reading and information"
    [REST Modelling: designing a future-friendly AP \| LinkedIn](https://www.linkedin.com/pulse/rest-modeling-designing-future-friendly-api-david-hickey/)

    [Use links, not keys, to represent relationships in APIs \| Google Cloud Blog](https://cloud.google.com/blog/products/application-development/api-design-why-you-should-use-links-not-keys-to-represent-relationships-in-apis)

    [Organise the API design around resources \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/architecture/best-practices/api-design#organize-the-api-design-around-resources)

    [Extraneous Fetching antipattern - Azure Architecture Center \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/architecture/antipatterns/extraneous-fetching/)

    [Chatty I/O antipattern - Performance antipatterns for cloud apps \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/architecture/antipatterns/chatty-io/)
