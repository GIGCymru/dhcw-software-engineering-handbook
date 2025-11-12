# Creating a new project

## Request a new project

Sometimes you may need to create a new project. Do so by making a
request to the Organisation Owner. When creating a new project the
following project property settings are **RECOMMENDED**:

| **PROPERTY** | **VALUE** |
| --- | --- |
| **project name:** | Use the project acronym for shorter URLs. Avoid spaces. |
| **description:** | Provide a clear, searchable project description. |
| **visibility:** | Private |
| **version control:** | Git |
| **work item process:** | Agile |

!!! info "Further reading and information"
    [Find or look up the organisation owner - Azure DevOps \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/organizations/security/look-up-organization-owner?view=azure-devops)

## Assign project admins

Every project **SHOULD** have **two** project administrators. A project
administrator manages access, configures project settings and customises
boards for teams and workflows.

!!! tip "Practical tips"
    **Project Collection Administrator**

    Depending on your requirements, it might be more suitable to also assign *Project Collection Administrators*. Speak to the Organisation Owner for more help.

!!! info "Further reading and information"
    [Find a project administrator - Azure DevOps \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/organizations/security/look-up-project-administrators?view=azure-devops&tabs=preview-page)

## Remove unused features

The Project Administrator **SHOULD** disable any features or services
that are not required.

!!! info "Further reading and information"
    [Turn a service on or off - Azure DevOps \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/organizations/settings/set-services?view=azure-devops)

## Choose a project profile image

Use a suitable DHCW sub brand logo If you intend to change the *Project
Profile Image.*

## Disable telemetry and data access

You **SHOULD** disable [extensions](using-azure-devops-extensions.md) that
send telemetry or access repositories automatically in project settings
before using the project.
