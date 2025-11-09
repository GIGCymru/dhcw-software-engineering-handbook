# Implement a versioning strategy

A versioning strategy **MUST** define how you assign, increment, and
publish version numbers. It **SHOULD** integrate with your branching
strategy to streamline builds and deployments.

## Use semantic versioning

The Semantic Versioning (SemVer 2.0.0) specification is **RECOMMENDED**
and **MUST** be used for public APIs and NuGet packages. SemVer makes it
easier for consumers to understand breaking, additive, or patch-level
changes.

## Automate version numbering

Use tools like **Nerdbank.GitVersioning** to generate SemVer compliant
versions during builds.

!!! tip "Practical tips"
    For .NET projects, NuGet 4.3.0+ supports SemVer 2.0.0.

    For APIs, include version numbers only if updates are expected; omit them for static APIs.

    For C# projects, use the obsolete attribute to warn about upcoming deprecations.

    Don't confuse semantic versioning, which reflects technical compatibility, with product versions which often align with release schedules.

!!! info "Further reading and information"
    [RESTful API Design and Build Standards](../restful-api-standards/introduction.md)

    [Azure DevOps handbook](../azure-devops-handbook/introduction.md)

    [Semantic Versioning 2.0.0 \| Semantic Versioning](https://semver.org/)

    [NuGet Package Version Reference \| Microsoft Learn](https://learn.microsoft.com/en-gb/nuget/concepts/package-versioning?tabs=semver20sort)

    [Versioning and .NET libraries - .NET \| Microsoft Learn](https://learn.microsoft.com/en-gb/dotnet/standard/library-guidance/versioning)

    [API Versioning Options · dotnet/aspnet-api-versioning Wiki](https://github.com/dotnet/aspnet-api-versioning/wiki/API-Versioning-Options)

    [API versioning misconceptions: When you need it and when you don't \| Google Cloud Blog](https://cloud.google.com/blog/products/api-management/common-misconceptions-about-api-versioning)

    [apigee-web-api- design-the-missing-link-ebook.pdf](https://cloud.google.com/files/apigee/apigee-web-api-design-the-missing-link-ebook.pdf) (page 56)

    [Breaking changes and .NET libraries - .NET \| Microsoft Learn](https://learn.microsoft.com/en-gb/dotnet/standard/library-guidance/breaking-changes)

    [Attributes interpreted by the compiler: Miscellaneous - C# reference \| Microsoft Learn](https://learn.microsoft.com/en-gb/dotnet/csharp/language-reference/attributes/general#obsolete-attribute)

    <https://github.com/dotnet/Nerdbank.GitVersioning>

    [Versioning limitations in .NET \| Jon Skeet's coding blog](https://codeblog.jonskeet.uk/2019/06/30/versioning-limitations-in-net/)

    [Semantic Versioning and Patch 2.1.2 \| Alan Kent's Blog](https://alankent.me/2016/09/20/semantic-versioning-and-patch-2-1-2/)

    [API Versioning Explained \| Lightboard Series](https://www.youtube.com/watch?v=_WWr_eFRDeM)
