# Managing source code with Azure repos

Following the practices in this section aligns with *[Using Source Control](../using-source-control/introduction.md)*, improving traceability, linking work items to code
changes, and enhancing code quality.

!!! info "Further reading and information"
    [Using Source Control](../using-source-control/introduction.md)

## How do you branch and release?

You have freedom to choose your branching and release strategies, but
you **SHOULD** follow these key practices to maintain simplicity and
consistency:

- **Use feature branches**: Develop new features and fix bugs in dedicated branches.

- **Merge through pull requests (PRs)**: Integrate changes into the main branch using PRs.

- **Keep the main branch clean**: Ensure the main branch is functional & up to date.

- **Git Tagging:** Tag the release commit to ensure traceability and version identification.

## Recommended naming conventions

Name Git repositories in lowercase with hyphens. Prefixing with the
Azure DevOps project or team name is **RECOMMENDED** but not required.

| **COMPONENT** | **NAMING CONVENTION** | **examples** |
| --- | --- | --- |
| **REPOSITORY** | Lowercase, hyphens-separated\ <project-name\>:<purpose\> | wis-api welshpas-web wcp-integration-services |
| **TAG** | <Major\>.<Minor\>.<Patch\> | 2.0.0 |

Use this convention for branch names. You may not need them all, it
depends on your strategy.

| **BRANCH TYPE** | **NAMING CONVENTION** | **examples** |
| --- | --- | --- |
| **MAIN** | 'main' | main |
| **DEVELOP** | 'develop' | develop |
| **FEATURE** | feature/*<work-item-number\>-<feature-name\>* | feature/450447-add-cors-policy |
| **RELEASE** | release/*<version-number\>* | release/2.0.0 |
| **BUGFIX** | bugfix/*<issue-number\>-<description\>* | bugfix/46627-fix-SMS-Input-Error |
| **HOTFIX** | hotfix/*<issue-number\>-<description\>* | hotfix/67891-critical-patch |

!!! tip "Practical tips"
    - Always link branches to corresponding work items,

    - Delete redundant feature branches.

## Configure repository settings for commit linking

You **SHOULD** ensure these settings are applied across all branches:

- **Enable Commit Mention Linking:** Automatically link commits to
    work items by including the work item ID (e.g., #123) in the commit
    message.

- **Ensure Work Item Resolution:** Automatically update work item
    status based on commit actions.

## Configure repository policies for email validation

- **Commit author email validation**: Block pushes from emails not
    matching .\*@wales\\.nhs\\.uk\$

## Configure branch policies

Enable these settings on main and release branches to support effective
branching and release:

- **Require a minimum number of reviewers:** Ensure pull requests are
    subject to code review.

- **Require linked work items:** Ensure pull requests are linked to
    work items.

- **Require comments resolution:** Address comments before merging
    pull requests.

- **Enable Build Validation**: Trigger a build pipeline on pull
    requests to validate code quality.

- **Add a Code Coverage Status Check:** Ensure coverage targets are
    met before merging.

- **Set Coverage Thresholds:** Define differential (diff) thresholds
    in *azurepipelines-coverage.yml* or *.runsettings* to match your
    *Definition of Done*.

- **Address Insufficient Coverage:** Use the "*Require comments
    resolution*" policy to address any insufficient coverage before
    merging.

- **Review Coverage Thresholds**: Regularly review thresholds to meet
    quality standards.

!!! tip "Practical tips"
    **Don't obsess over Code Coverage!**

    Use it as a guide but focus on meaningful tests that ensure your code works as expected.

!!! tip "Practical tips"
    **Set Up Pipelines for Validation and Coverage**

    Configure a build pipeline for validation and code coverage checks, In the next section, we'll show you how to set up pipelines for testing & deployment.

!!! info "Further reading and information"
    [Set Git repository settings - Azure Repos \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/repos/git/repository-settings?view=azure-devops&tabs=browser)
