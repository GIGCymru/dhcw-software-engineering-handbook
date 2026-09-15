# Recommended solution sub-folders

## Create a source folder

You **SHOULD** store all projects that have a definable output release
(for example, web, desktop, mobile or general library projects) in a
source folder, named *src* (`./<rootfoldername>/src`).

## Use additional sub-folders for dependency layers

You **SHOULD** create immediate sub-folders (`/src/<dependencylayer>`) to
separate the dependency layers of your solution, such as data access, user
interface, domain logic or service layers. This reminds you that the layers
exist and to test them.

Including the parent's name in the sub folder name may appear
repetitive, but it adds context. And it can prove useful when
referencing it from another location or when searching for a file or
folder.

We leave naming the sub folders underneath ***src*** and **test** to
your discretion but you **SHOULD :-**

- use Pascal casing when naming folders.

- Follow [Microsoft's naming advice](https://docs.microsoft.com/en-gb/windows/desktop/fileio/naming-a-file)
    when developing for Windows systems.

You **SHOULD NOT** use special characters or abbreviations longer than
two letters in folder names.

!!! example "Examples of good practice"
    > {IMAGE PLACEHOLDER}
    Figure 1 An example.NET Solution with dependency layers

!!! info "Further reading and information"
    [Naming Files, Paths, and Namespaces - Win32 apps \| Microsoft Learn](https://learn.microsoft.com/en-gb/windows/win32/fileio/naming-a-file)

## Create a specification folder

You **SHOULD** store test projects and any specifications you consider
valuable in a specification ('specs') folder (`./<rootfoldername>/specs`).
Keeping them together helps link your documentation to tests.

You **SHOULD** clearly indicate the expected behaviours, functionality
and actual integration with consumers of the code. This may include data
extracts from other systems or software.

## Provide a test folder

As the name suggests, this is where you **SHOULD** store your tests
(`./<rootfoldername>/specs/test`). As with the *src* folder, you **SHOULD**
place test projects in sub folders, mapping the name of the sub folder to
the name of the project.

Names **SHOULD** correspond to those of your dependency layers, with the
*.Tests* suffix added.

When writing the tests, you **SHOULD:-**

- Prioritise output testing over testing that assures modules.

- Adopt Behavioural Driven Development as your approach.

- Balance the benefits and drawbacks of adding extensive testing to
    your solution.

- Consider You Aren't Gonna Need It (YAGNI) rules when deciding what
    to test.

- Consider the testing requirements described in your Definition of
    Done (DOD).

Consider wider assurance needs when deciding what tests to write. Integration and smoke tests often provide the greatest benefit Consider You Aren't Gonna Need It (YAGNI) and carefully balance the time and effort of an extensive testing approach with the benefit it provides

!!! info "Further reading and information"
    [Selective Unit Testing -- Costs and Benefits (stevensanderson.com)](http://blog.stevensanderson.com/2009/11/04/selective-unit-testing-costs-and-benefits/)

## Provide a documents folder

You **SHOULD** keep documentation you consider valuable (including
diagrams, specifications[^1] and documents relevant to build output) in
a documents ('docs') folder (`./<rootfoldername>/specs/docs`). This is
particularly useful if there's no Solutions Architecture Design document
(SAD) or Software Requirements Specification (SRS).

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

## Include a decision records (ADRs) folder

Architecture Decision Records (ADRs) are stored in a decision records
folder (`./<rootfoldername>/decisions`). They capture the context, the options
you considered, and the reasoning behind a significant decision.
Recording decisions as you make them preserves that context for anyone
who works on the solution later, rather than relying on memory or
scattered conversations.

You **SHOULD** write an ADR whenever your team makes a decision that is
significant to the architecture or design of your solution, would be
costly or difficult to reverse, or that future contributors would
benefit from understanding the reasoning behind. This includes
deliberately accepting technical debt -- see *Use ADRs to record
technical debt decisions* below -- but ADRs are not limited to that use
case.

This guidance builds on DHCW's [Architecture Decision Record process](https://gigcymru.github.io/architecture/design-authority/dhcw/architecture-decision-record-process/),
which describes when and how architecture decisions are recorded and
reviewed across DHCW.

### Store ADRs in a decision records folder

You **SHOULD** keep ADRs as close as possible to the teams and code they
affect, only moving them to a central location when they have wider
organisational impact.

- **Project-specific ADRs** **SHOULD** be stored as markdown files in a
    `decisions` folder in the root of the project's Git repository,
    alongside the code they relate to.

- **Cross-project or cross-team ADRs** **SHOULD** be stored in Git,
    preferably in a single shared location to avoid duplication.

- **Organisation-wide or significant ADRs** **MUST** follow the [DHCW Architecture Decision Record process](https://gigcymru.github.io/architecture/design-authority/dhcw/architecture-decision-record-process/);
    contributions are made in the internal `architecture-internal`
    repository, while `architecture` is a read-only public mirror.

You **SHOULD NOT** number ADR filenames. Instead, give each ADR a
descriptive, human-readable title in Title Case, avoiding acronyms, and
name the file after that title in kebab-case, for example
`use-a-managed-database-service.md` for a decision titled *Use a
Managed Database Service*. This follows DHCW's [Simplify Architecture Decision Records Structure](https://gigcymru.github.io/architecture/decisions/dhcw/meta-decisions/simplify-architecture-decision-records-structure/)
decision, which found that sequential numbering adds administrative
overhead -- keeping numbers unique and in order -- without improving
readability.

### Format ADRs using the DHCW template

You **SHOULD** use the [DHCW Architecture Decision Record template](https://gigcymru.github.io/architecture/design-authority/dhcw/architecture-decision-record-template/)
so ADRs are consistent and easy to review across the organisation.

### Retain and supersede ADRs

You **SHOULD NOT** delete or edit an ADR once it's agreed. If a decision
is superseded, record a new ADR explaining the change, and add a note to
the old ADR stating that it has been superseded, linking to the new one.

### Use ADRs to record technical debt decisions

Technical debt is one common reason to write an ADR. Where your team
knowingly accepts technical debt to meet a deadline, work around a
constraint, or defer a better solution to a later date, you **SHOULD**
record the decision as an ADR, covering the rationale, the trade-offs
considered, and a review point so the debt is revisited rather than
forgotten.

This complements DHCW's [Technical Debt](https://gigcymru.github.io/architecture/design-authority/dhcw/technical-debt/)
guidance and the [Technical debt](https://dhcw-digital-health-and-care-wales.github.io/dhcw-delivery-playbook/technical-debt/)
guidance in the DHCW Product and Service Delivery Playbook, which
describe how teams identify, prioritise and pay down debt as part of
their sprint cycle.

!!! tip "Practical tips"
    - Cross-team and organisation-wide ADRs **SHOULD NOT** be duplicated in project repositories; keep them only in their designated shared or internal repository.

    - Never delete an ADR, even once superseded; it remains a record of what was decided and why at the time.

!!! example "Examples of good practice"
    A team chooses a message queue over direct API calls to integrate
    two services. They record an ADR describing the alternatives
    considered, the reasons for choosing a message queue -- such as
    resilience to downstream outages -- and the trade-offs accepted,
    such as eventual consistency.

!!! warning "Practices to avoid"
    - Do not let significant decisions go undocumented; undocumented
        decisions are easily forgotten and harder to justify later.

    - Do not duplicate the same ADR across multiple repositories; link
        to a single source of truth instead.

!!! info "Further reading and information"
    [DHCW Architecture Decision Record process](https://gigcymru.github.io/architecture/design-authority/dhcw/architecture-decision-record-process/)

    [DHCW Architecture Decision Record template](https://gigcymru.github.io/architecture/design-authority/dhcw/architecture-decision-record-template/)

    [Simplify Architecture Decision Records Structure](https://gigcymru.github.io/architecture/decisions/dhcw/meta-decisions/simplify-architecture-decision-records-structure/)

    [DHCW Technical Debt guidance](https://gigcymru.github.io/architecture/design-authority/dhcw/technical-debt/)

## Provide a build folder

You **SHOULD** store the latest output from publish commands, though not
necessarily each build event, in a build folder (`./<rootfoldername>/build`).

Place your outputs in sub folders, named appropriately, with a suffix to
indicate output type and a prefix for the solution name. And take care
to indicate the last build date.

## Provide a scripts folder

You **SHOULD** store any scripts needed to assist with the build[^2], by
placing them in a '*scripts'* subfolder (`./<rootfoldername>/build/scripts`).
This offers a standard location for any others wishing to build your
solution.

As well as build scripts, use the folder to store artefacts related to
your continuous integration (CI) processes. While some CI systems
require you place build artefacts in the root, placing other supporting
files in the scripts folder avoids excessive cluttering.

When storing scripts, you **SHOULD** keep your scripts clean and with
comments.

You **SHOULD** prefer using scripted solutions over build events
whenever possible.

You **SHOULD NOT** break published conventions without considering how
this impacts others.

!!! example "Examples of good practice"
    > {IMAGE PLACEHOLDER}
    Figure 3 An example.NET Solution with a build and scripts folder

!!! info "Further reading and information"
    [.NET Core Opinion #4 - Increase Productivity with Dev Scripts (odetocode.com)](https://odetocode.com/blogs/scott/archive/2018/09/21/net-core-opinion-4-ndash-increase-productivity-with-dev.aspx)

    [.NET Core Opinion #5 - Deployment Scripts and Templates (odetocode.com)](https://odetocode.com/blogs/scott/archive/2018/10/17/net-core-opinion-5-deployment-scripts-and-templates.aspx)

[^2]: .*exe, .ps1 .sql* and .*cmd* files for example.

## Provide a deploy folder

You **SHOULD** store any infrastructure provisioning scripts in a deploy
folder (`./<rootfoldername>/deploy`). These could be Azure Resource
Management (ARM) templates or Bicep scripts and associated parameter files,
but it is **RECOMMENDED** that you use Terraform scripts.

## Provide an examples folder

It is **RECOMMENDED** that you provide examples (`./<rootfoldername>/examples`)
to show others how to use your published outputs. Developers will thank you
for it!

SQL outputs, scripted languages, or configurations such as yaml, will
likely be single files. For complex outputs, store each demo project in
its own sub-folder.

When doing so you **SHOULD:**

- Make sure examples work as expected.

- Demonstrate typical use cases, capabilities and support queries.

- Consider using automation for each example output.

You **SHOULD NOT** let examples become stale and out-of-date.

!!! example "Examples of good practice"
    > {IMAGE PLACEHOLDER}
    Figure 4 An example.NET Solution with example
