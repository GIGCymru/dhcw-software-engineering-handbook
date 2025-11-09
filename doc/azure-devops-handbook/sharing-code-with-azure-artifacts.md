# Sharing code with Azure artifacts

Azure Artifacts provide a reliable way to store, version and distribute
packages, like Nuget, across the organisation. You **SHOULD** follow
these practices when using Artifacts in your Azure DevOps workflows.

!!! info "Further reading and information"
    [What is NuGet and what does it do? \| Microsoft Learn](https://learn.microsoft.com/en-gb/nuget/what-is-nuget)

    [Azure Artifacts documentation \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/artifacts/?view=azure-devops)

    [Omit NuGet Packages in Source Control Systems\| Microsoft Learn](https://learn.microsoft.com/en-gb/nuget/consume-packages/packages-and-source-control)

    [Project-scoped vs Organisation-scoped feeds - Azure Artifacts \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/artifacts/feeds/project-scoped-feeds?view=azure-devops#project-scoped-vs-organization-scoped-feeds)

    [Migrate from file shares - Azure Artifacts \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/artifacts/nuget/move-from-fileshares?view=azure-devops)

    [Configure pipeline permissions - Azure Artifacts \| Microsoft Learn ](https://learn.microsoft.com/en-gb/azure/devops/artifacts/feeds/feed-permissions?view=azure-devops#pipelines-permissions)

## Consuming packages

- **Avoid Public Feeds**: Do not pull packages from public sources
    like nuget.org. Use a secondary feed, *DHCW_Global_Dependencies*,
    for shared or third-party dependencies.

- **Minimise Duplication**: If a package is already in the
    organisation feed, do not duplicate it in your local feed. This
    saves storage costs and reduces redundancy.

- **Keep Dependencies Updated**: Regularly check the
    *DHCW_Global_Dependencies* feed for updates to keep your
    dependencies current.

- **Request Access Permissions**: If you need access to the
    organisation feed, ask the organisation owner to grant the Build
    Service User 'Contributor' permissions. The Build Service User is
    the account running your Azure pipeline.

!!! tip "Practical tips"
    Granting access to an organisation feed is easier than a project feed, as it doesn't require first granting access to the project.

    *DHCW_Global_Dependencies* is hosted in the NHS-Wales-Digital Azure DevOps Organisation but can be used by other Organisations in the same NHS Wales Entra tenant,

!!! info "Further reading and information"
    [Restore NuGet packages in Azure Pipelines - Azure Pipelines \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/pipelines/packages/nuget-restore?view=azure-devops&tabs=yaml#restore-nuget-packages-from-a-feed)

    [Find or lookup the organisation owner - Azure DevOps \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/organizations/security/look-up-organization-owner?view=azure-devops)

## Publishing packages

Publishing packages to Azure Artifacts helps in:

- Sharing secure, maintainable libraries (such as UI components).

- Distributing validated third-party libraries without pulling from public feeds.

!!! info "Further reading and information"
    [Publish NuGet packages with Azure Pipelines - Azure Pipelines \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/pipelines/artifacts/nuget?toc=%2Fazure%2Fdevops%2Fartifacts%2Ftoc.json&bc=%2Fazure%2Fdevops%2Fartifacts%2Fbreadcrumb%2Ftoc.json&view=azure-devops&tabs=yaml)

## How do you version your code?

You **MUST** use Semantic Versioning (SemVer 2.0.0). See the following
for more details:

!!! info "Further reading and information"
    [Using Source Control](../using-source-control/introduction.md)

    [RESTful API Design and Build Standards](../restful-api-standards/introduction.md)

    [Semantic Versioning 2.0.0 \| Semantic Versioning](https://semver.org/)

## Versioning conventions

| **COMPONENT** | **NAMING CONVENTION** | **example** |
| --- | --- | --- |
| **VERSION FORMAT** | <Major\> .<Minor\>.<Patch\>\[-<prerelease tag\>\]\[+<Git commit \>\] | 1.0.0 |
| **MAJOR** | For breaking changes | 2.0.0 |
| **MINOR** | Backward-compatible changes. | 2.1.0 |
| **PATCH** | Bug Fixes | 1.0.1 |
| **PRE-RELEASE TAG** | Optional \[-<alpha \| beta \ rc\>\] | 1.0.0-alpha |
| **ALPHA** | Indicates unstable builds. | 1.0.0-alpha |
| **BETA** | Feature complete but may contain known bugs. | 2.0.0-beta |
| **RC** | Release candidate | 2.1.0-rc |
| **Git Commit** | Short Git hash added after +. Identifies the build's source commit. | 1.0.0-alp ha+26be44c37e 2.0.0- beta+d8164225 |

!!! tip "Practical tips"
    Use the **Nerdbank.GitVersioning** dotnet tool to auto-generate SemVer compliant versions in Azure Pipelines.

    Use extensions like **Generate Release Notes** in YAML Pipeline features to auto-generate package release notes.

!!! info "Further reading and information"
    <https://github.com/dotnet/Nerdbank.GitVersioning>

## Package naming conventions

Follow these naming conventions when publishing a package. Publish
reusable components the organisation shared feed.

| **COMPONENT** | **NAMING CONVENTION** | **example** |
| --- | --- | --- |
| **Organisation feed** | DHCW_Global_Dependencies | DHCW_Global_Dependencies |
| **project feed** | <Project Name\> | NHS Wales Patient Portal |
| **package ID** | \[<DHCW.\>\]<ProjectName\>.<ComponentName\> | DHCW.PortalUI.Validation |
| **Package Version** | See [Publishing Packages: Versioning](#versioning-conventions) | 1.1.0 |
| **AUTHORS** | Team or developer name | Phoenix Portal Team |
| **DESCRIPTION** | A short description for UI display. | Validation library for UI components in the NHS Wales Patient Portal. This library..... |
| **COPYright** | Copyright (c) DHCW <Year\> | Copyright (c) DHCW 2024 |
| **Project URL** | Link to the Azure DevOps project | {base}/\_git/patient-portal |
| **README** | Include a README markdown file | *(overview of what the package does)* |
| **REPOSITORY URL** | A link to the source repository, including a 'type' attribute (e.g., git). | {base}/\_git/patient-portal |
| **TAGS** | Comma-separated list of keywords. | UI, validation, Portal, .Net |
| **RELEASE NOTES** | Description of changes in this release. | New release with added validation for SMS text input. |

## Publishing to shared organisation feeds

*DHCW_Global_Dependencies* (found in the NHS-Wales-Digital) uses only
the \@local feed as the shared repository for stable packages. This
simplifies package management.

Follow these rules When publishing to a shared feed**:**

1. **No Pre-releases:** Packages with pre-release tags (e.g., -alpha,
    -beta, -rc) **MUST NOT** be published to a shared feed. Use
    separate feeds for testing.

2. **Stable Versions Only:** Ensure packages are fully tested,
    reviewed, and stable before publishing.

3. **Follow Conventions:** Adhere to semantic versioning (e.g., 1.0.0
    for stable releases).

!!! tip "Practical tips"
    Automate checks in pipelines to block unstable versions from being published to the shared feed.
