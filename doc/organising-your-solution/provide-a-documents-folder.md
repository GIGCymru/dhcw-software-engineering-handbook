# Provide a documents folder (.*/<rootfoldername\>/*specs*/*docs)

You **SHOULD** keep documentation you consider valuable (including
diagrams, specifications[^1] and documents relevant to build output) in
a documents ('docs') folder. This is particularly useful if there's no
Solutions Architecture Design document (SAD) or Software Requirements
Specification (SRS).

While most documents **MAY** be stored in our document management
system, not all will reflect the current state of the solution. For
example, a SAD or SRS may include planned work or perhaps even obsolete
design decisions. Maintaining a *docs* folder is an important step in
addressing any drift between design and build.

You **SHOULD NOT** let documentation become stale or out-of-step with
the build output or use the docs folder as a replacement for the
corporate document management system.

!!! tip "Practical tips"
    - Use automation. For example, generate .pdf files from the repo's markdown files and include OpenAPI documentation.

    - Take care when linking to other documents. Links are only relevant while they are maintained and may be resolvable only from within our domain.

    - Encourage testers and business analysts to use. feature files to record changes to requirements. Link your docs folder to those*. feature* files

    - Use a tool like [Grammarly: Free Online Writing Assistant](https://www.grammarly.com/) to help you make your content clear

Writing good documentation is a skill. Use these links to help you write
high quality documentation.

!!! info "Further reading and information"
    [Doing Visual Studio and .NET Code Documentation Right \-- Visual Studio Magazine](https://visualstudiomagazine.com/articles/2017/02/21/vs-dotnet-code-documentation-tools-roundup.aspx)

    [How to write plain English](https://www.plainenglish.co.uk/)

    [Writing checklist (sharepoint.com)](https://nhswales365.sharepoint.com/sites/DHC_ENG/SitePages/Writing-guidelines.aspx)

[^1]: For example, if you are building on published specs -- such HL7 FHIR.
