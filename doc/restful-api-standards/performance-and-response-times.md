# Performance and response times

You **MUST** define a maximum response time and specify any exceptions.

To improve performance and minimise network traffic, you **SHOULD**
consider the following options. Your choice depends on your use-case and
user needs:

- Implement a server-side cache (for example, ASP.NET output caching)
    or a distributed cache (for example, Redis) for more complex
    scenarios.

- Allow clients to cache responses (response caching) while taking
    care to mitigate any potential security risks; see [HTTP Messaging
    caching](http-message-caching.md).

- Avoid blocking calls. For example, ASP.NET web APIs **SHOULD** use
    the async keyword.

- Take advantage of [paging](paging.md) and [filtering](filtering.md) to
    limit the amount of data returned in responses.

- Compress responses and minify JSON payloads.

You **MUST** monitor and analyse API performance and take corrective
actions if your APIs do not meet the performance thresholds defined in
your solutions architecture.

!!! info "Further reading and information"
    [ASP.NET Core Best Practices \| Microsoft Learn](https://learn.microsoft.com/en-gb/aspnet/core/fundamentals/best-practices?view=aspnetcore-7.0)
