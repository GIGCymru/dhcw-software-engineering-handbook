# Joining an existing project

Whether you're new to Azure DevOps or arranging access for others, start
with these steps:

## Find your project

First, obtain your project URL. If needed, ask a colleague for help.
Here are some common URLs:

| **PROJECT URL** | **Description** |
| --- | --- |
| <https://dev.azure.com/NHS-Wales-Digital/WCP> | Welsh Clinical Portal |
| <https://dev.azure.com/DHCW-DSPP/> | NHS App |
| [https://dev.azure.com/NHS-Wales/DMTP](https://dev.azure.com/NHS-Wales/DMTP) | Digital Medicines Transformation Portfolio |
| <https://dev.azure.com/NHS-Wales-CoE/> | M365 Centre of Excellence |

!!! tip "Practical tips"
    If you need to begin a project, see [Creating a Project](creating-a-new-project.md).

!!! info "Further reading and information"
    [Connect to your organisation - Azure DevOps Services \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/organizations/accounts/organization-management?view=azure-devops#connect-to-your-organization)

## Check you have the right access level

Next, check your *Access level.* *Access levels* control which **Azure
DevOps** features you can use. If you don't have the right level you may
be blocked from using Repos, Pipelines or Test Plans. Contact the
*Organisation Owner* for more help.

| **ACCESS LEVEL** | **FEATURES** |
| --- | --- |
| **Stakeholder** | Limited features for non-dev roles: create and view work items, basic project management; no access to Repos or Pipelines. |
| **Basic** | Full access to Repos, Pipelines and Artifacts. |
| **Basic + Test Plans** | All Basic features **plus** Azure Test Plans (Test planning, execution and reporting). |

!!! tip "Practical tips"
    **Subscriptions that grant access automatically**

    Visual Studio Professional with GitHub Enterprise → **Basic**.

    GitHub Enterprise Cloud → **Basic.**

    Visual Studio Test Professional → **Basic + Test Plans**.

!!! info "Further reading and information"
    [How to request and manage software subscriptions](../software-subscriptions/introduction.md)

    [Find or look up the organisation owner - Azure DevOps \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/organizations/security/look-up-organization-owner?view=azure-devops)

    [About access levels - Azure DevOps \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/organizations/security/access-levels?view=azure-devops)

    [Azure DevOps Basic usage included with GitHub Enterprise - Azure DevOps Blog](https://devblogs.microsoft.com/devops/azure-devops-basic-usage-included-with-github-enterprise/)

## Verify access

Finally, make sure you have the correct *Access permissions. Access
permissions* control what you can do in a project. Ask a Project
Administrator to update your access if needed.

!!! tip "Practical tips"
    If you click the project URL without the right access, you may be prompted to request access. Your request will be sent to the project administrator.

!!! info "Further reading and information"
    [Find a project administrator - Azure DevOps \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/organizations/security/look-up-project-administrators?view=azure-devops&tabs=preview-page)

    [About permissions and security groups - Azure DevOps \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/organizations/security/about-permissions?view=azure-devops&tabs=preview-page)

    [Troubleshoot access, permission issues - Azure DevOps \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/organizations/security/troubleshoot-permissions?view=azure-devops)

## Additional steps

If you're committing code to Azure Repos you may need to take some extra
steps. See [Support & Troubleshooting](support-and-troubleshooting.md) for
more details.
