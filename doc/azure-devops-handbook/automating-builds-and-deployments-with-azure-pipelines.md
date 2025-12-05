# Automating builds and deployments with Azure pipelines

You **SHOULD** use Azure Pipelines to automate build, test, and
deployment processes, enabling Continuous Integration (CI) & Continuous
Deployment (CD).

## How do you organise your code?

Follow *[How to Organise Your Software Solution](../organising-your-solution/introduction.md)* to maintain a
clean, modular codebase and keep build and deployment scripts separate
to reduce clutter.

!!! tip "Practical tips"
    Place pipeline YAML files in the build/scripts/ folder unless operational needs require a different location.

!!! info "Further reading and information"
    [How to Organise Your Software Solution](../organising-your-solution/introduction.md)

## Core pipeline characteristics

Follow [Microsoft's baseline architecture](https://learn.microsoft.com/en-gb/azure/devops/pipelines/architectures/devops-pipelines-baseline-architecture?view=azure-devops)
to build repeatable, scalable Azure pipelines.

Key considerations:

- **Use YAML:** Prefer YAML pipelines for version control and sharing
    configurations.

- **Modular Design:** Create reusable templates & separate stages
    (e.g. Build, Test, Deploy).

- **Gradual Deployment:** Use progressive strategies (e.g. DevTest \>
    UAT \> Prod).

- **Integrate Security:** Include code analysis and vulnerability
    scanning.

- **Automated Testing:** Run automated tests with coverage reporting.

- **Approvals**

  - Pre-approval checks are **RECOMMENDED** for DevTest and UAT.

  - Pre-approval checks **SHOULD** be in place before deploying to
        Prod.

- **Secure Secrets:** Use tools like Azure Key Vault to manage
    secrets.

- **Store Artifacts:** Retain build outputs for traceability.

!!! tip "Practical tips"
    Not all pipelines need every feature; apply those relevant to the pipeline's purpose.

!!! info "Further reading and information"
    [Azure Pipelines baseline architecture - Azure Pipelines \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/pipelines/architectures/devops-pipelines-baseline-architecture?view=azure-devops)

    [Azure Pipelines documentation - Azure DevOps \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/pipelines/?view=azure-devops)

## Prefer YAML over classic release pipelines

Use YAML pipelines for improved version control, tracking, and auditing.

While Classic Release pipelines can still be useful, YAML deployment
jobs and Azure DevOps Environments are preferred for greater flexibility
and scalability.

Deployment groups may suit VM-based deployments but offer less control
than YAML.

## Naming conventions

| **COMPONENT** | **NAMING CONVENTION** | **example** |
| --- | --- | --- |
| **pipeline** | <repository-name\>-<purpose\> (*purpose* = pr, ci, cd) | `wis-api-pr welshpas-web-ci wcp -integration-services-cd` |
| **Pipeline Run** **(YAML name)** | \$ (Build.DefinitionName)\_ \$(SourceBranchName)\_ \$( Date:yyyyMMdd).\$(Rev:r) | `welshpas-web-ci_main_20241203.1` |
| **STAGE** | PascalCase, descriptive | Build, Test, DeployToProd |
| **JOB** | PascalCase, descriptive | RunUnitTests, BuildDockerImage, DeployToProd |
| **ENVIRONMENT** | <DevTest \| UAT \| PROD\> | DevTest, UAT, Prod |
| **DEPLOYMENT** | DeployTo<Environment\> | DeployToDevTest, DeployToUAT, DeployToProd |
| **VARIABLES** | PascalCase, descriptive | KeyVaultName |
| **LIBRARY VARIABLES** | *Lib-<name\>* | Lib-ApiEndpoint |
| **LIBRARY VARIABLES** **(LINKED TO KEY VAULT)** | *Kv-<name\>* | Kv-APIKey |

!!! tip "Practical tips"
    Use clear, descriptive displayName values to clarify purpose and enhance readability.

    When building Nuget packages, using version numbers as pipeline run names is **RECOMMENDED**. 
    See [Versioning conventions](sharing-code-with-azure-artifacts.md).

## Link work items to builds

**Automatically link work items included:** In Pipeline settings choose
to connect work items with each build result.
