# Establish a clear repo structure

## Before creating your repo

You **MUST** have a clear plan for how to organise your repos. You have
three main options:

| **REPO TYPE** | **Description** |
| --- | --- |
| **MONOREPO** | A single repo for all our organisation's source code. We do not use this approach and it is **NOT RECOMMENDED** to have all teams share one Azure DevOps project. |
| **SINGLE REPO** | Each team stores its code in the same repo. This is the **RECOMMENDED** approach for most cases but requires automation to manage the process effectively. |
| **MULTIREPO** | Each application has its own repo. This may be necessary if you have specific constraints that make this approach better for your team. |

## Managing multiple applications in the same repo

Your repos **MUST NOT** become a confusing mess. To keep them organised
you **MUST**:

- Deploy applications only when code changes are made to that specific
    application.

- Restrict access to distinct parts of your codebase when needed.

For example, the Single Record Product team might face these scenarios:

| **PROBLEM** | **SOLUTION** |
| --- | --- |
| The Welsh Clinical Portal mobile and web apps share common libraries in the same repo, but changes to one app should not trigger deployments of the other. | Set up build pipelines to trigger only when code changes occur in specific directories. |
| Contractors working on the Welsh Nursing Care Record form should not be able to modify the Welsh Clinical Portal apps. | Use branch policies or security settings to limit access. |

## Choosing between single and multirepos?

Using a *Single Repo* is **RECOMMENDED** for apps that share a release
cadence, like a desktop app and its back-end API. This approach is also
good for components that are deployed together.

If you choose a single repo, you **MUST** automate builds and
deployments and follow the folder structure outlined in *How to Organise
Your Software Solution.*

If your apps are each tied to their own Visual Studio .sln file,
*Multirepo* may be a better fit.

!!! tip "Practical tips"
    Even when using a single repo for common libraries, you **SHOULD** use package management to publish binaries.

    Repos and branches serve a different purpose. See the Azure DevOps handbook for details.

!!! info "Further reading and information"
    [How to Organise Your Software Solution](../organising-your-solution/introduction.md)

    [Azure DevOps handbook](../azure-devops-handbook/introduction.md)

    [Structure your Git Repo - Training \| Microsoft Learn](https://learn.microsoft.com/en-gb/training/modules/structure-your-git-repo/)

    [Working with a Monorepo - CSE Developer Blog (microsoft.com)](https://devblogs.microsoft.com/cse/2021/11/23/working-with-a-monorepo/)

    [Monorepos in Git \| Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/monorepos)

    [Misconceptions about Monorepos: Monorepo != Monolith](https://blog.nrwl.io/misconceptions-about-monorepos-monorepo-monolith-df1250d4b03c)

    [The Big Ball of Mud and Other Architectural Disasters (codinghorror.com)](https://blog.codinghorror.com/the-big-ball-of-mud-and-other-architectural-disasters/)
