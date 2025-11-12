# Development tools

## Technology stack

In recent years we have expanded our tech stack, adopting tools like
GitHub Enterprise, Google Cloud Platform (GCP) and PostgreSQL and
programming languages like Python. However, teams in Operations and
Primary Care and Mental Health primarily use the following:

| **CATEGORY** | **TOOLS** |
| --- | --- |
| **DEVOPS** | - Azure DevOps |
| **DEV ENVIRONMENT** | - Visual Studio or Visual Studio Code (preferred) - Git - SQL Toolbelt Essentials (mandatory when writing T-SQL) - HL7Edit |
| **SERVER-SIDE DEVELOPMENT** | - .NET / ASP.NET with C# - Microsoft SQL Server with T-SQL - Azure |
| **FRONT-END DEVELOPMENT** | - ASP.NET MVC with C# - .NET MAUI - Blazor - Client-side JavaScript |

!!! tip "Practical tips"
    A common toolset reduces complexity and avoids additional licencing costs.

## Activate software subscriptions

Development tools are not preinstalled on your laptop. Your line manager
typically arranges a software subscription so you can install the tools.
If not, follow our guide to request and manage subscriptions.

!!! info "Further reading and information"
    [How to request and manage software subscriptions](../software-subscriptions/introduction.md)

    [Visual Studio Subscriptions \| Microsoft Learn](https://learn.microsoft.com/en-gb/visualstudio/subscriptions/)

## Setting up the development environment

Our primary tools include Visual Studio, SQL Server Management Studio
and Azure DevOps. Use the links below to set up your environment. Read
our Azure DevOps Handbook to support its use.

!!! info "Further reading and information"
    [Select a development environment - Azure DevOps \| Microsoft Learn](https://learn.microsoft.com/en-gb/devops/develop/selecting-development-environment)

    [Azure DevOps handbook](../azure-devops-handbook/introduction.md)

    [Client version compatibility - Azure DevOps \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/server/compatibility?view=azure-devops)

    [Sign in with work or school account - Visual Studio Subscription \| Microsoft Learn](https://learn.microsoft.com/en-gb/visualstudio/subscriptions/sign-in-work)

    [Download the Visual Studio IDE - Visual Studio Subscription \| Microsoft Learn](https://learn.microsoft.com/en-gb/visualstudio/subscriptions/vs-ide-benefit#download-and-install-the-ide)

    [Install Visual Studio and choose your preferred features \| Microsoft Learn](https://learn.microsoft.com/en-gb/visualstudio/install/install-visual-studio?view=vs-2022)

    [Connect to project from browser/supported client - Azure DevOps \| Microsoft L earn](https://learn.microsoft.com/en-gb/azure/devops/organizations/projects/connect-to-projects?bc=%2Fazure%2Fdevops%2Fget-started%2Fbreadcrumb%2Ftoc.json&toc=%2Fazure%2Fdevops%2Fget-started%2Ftoc.json&view=azure-devops&tabs=visual-studio-2019)

    [Get started with Git and Visual Studio - Azure Repos \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/repos/git/gitquickstart?view=azure-devops&tabs=visual-studio-2022)

    [What is SQL Server? - SQL Server \| Microsoft Learn](https://learn.microsoft.com/en-gb/sql/sql-server/what-is-sql-server?view=sql-server-ver16)

!!! tip "Practical tips"
    - Run Visual Studio as a standard user to follow the principle of least privilege.

    - Use IIS Express instead of IIS.

    - For new projects, consider SQL Server Developer Edition.

## Keep frameworks up to date

You **SHOULD** keep frameworks and dependencies current to minimise
security risks.

!!! tip "Practical tips"
    **CANISC cyber security concerns**

    In 2018, the National Assembly Public Accounts Committee flagged CANISC, the all-Wales Cancer system, as a cyber security risk due to discontinued Microsoft security updates.

!!! info "Further reading and information"
    [Microsoft .NET Framework - Microsoft Lifecycle \| Microsoft Learn](https://learn.microsoft.com/en-gb/lifecycle/products/microsoft-net-framework)

    [.NET Framework official support policy (microsoft.com)](https://dotnet.microsoft.com/platform/support/policy/dotnet-framework)

    [.NET Official Support Policy (microsoft.com)](https://dotnet.microsoft.com/platform/support/policy)

## Evaluating and adopting new tools

If you need to use new or alternative tools you **SHOULD** follow these
rules:

- **Use widely adopted frameworks**: Choose those with dedicated
    support, follow open standards and have good documentation.

- **Check licencing**: Ensure Terms and Conditions are suitable for
    use.

- **Learn from others**: Base decisions on the experience gained by
    other teams.
