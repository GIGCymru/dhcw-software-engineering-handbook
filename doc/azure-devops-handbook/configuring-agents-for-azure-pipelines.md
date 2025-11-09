# Configuring agents for Azure pipelines

Agents execute tasks in an Azure Pipeline and are available in two
types:

- **Self-Hosted Agents**: Managed on your infrastructure.

- **Microsoft-Hosted Agents**: Fully managed by Microsoft and
    available on demand.

## Choose an agent type

Choosing the right agent type depends on your needs -- see below.

| **COMPONENT** | **SELF-HOSTED** | **MICROSOFT-HOSTED** |
| --- | --- | --- |
| **COST** | Pay for VMs; build minutes/parallel jobs covered by Visual Studio Enterprise subscriptions. | Pay per minute beyond free-tier usage. |
| **MANAGEMENT** | Manual setup and maintenance required. | Fully managed; no setup needed. |
| **FLEXIBILITY** | Full control over tools and network configuration. | Preconfigured environments; limited customisation. |
| **SCALABILITY** | Limited by VM capacity and no. of available Visual Studio Enterprise subscriptions. | Scales on demand; no infrastructure limits. |
| **AVAILABILITY** | Restricted to DevTest VM uptime: Mon--Fri: 7 PM--7 AM. Sat & Sun: Unavailable. | Available without downtime. |

## Our recommendation

Use **Self-Hosted Agents** for cost-effective scaling with multiple
parallel jobs under our Visual Studio agreement.

Use **Microsoft-Hosted Agents** for occasional tasks or to avoid
management overheads and VM costs.

!!! info "Further reading and information"
    [Azure Pipelines Agents - Azure Pipelines \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/pipelines/agents/agents?view=azure-devops&tabs=yaml%2Cbrowser)

## Setting up a self-hosted agent

To configure a self-hosted agent:

- Provision an Azure Virtual Machine.

- Add the agent to an existing pool (create a new pool if needed).

- Install and configure the agent software from Azure DevOps.

- Run the agent as a service for automatic restarts.

## Securing a self-hosted agent

To ensure agent security:

- Use separate pools for different projects to reduce risk.

- Assign a dedicated pool for production deployments.

- Restrict access to the agent folder to authorised personnel.

- Clean temporary files in the agent's build folder regularly.

- Keep the agent software updated.

- Run the agent under a service account (e.g., Network Service or
    Local Service).

- Avoid using admin or high-privilege accounts.

## Recommended naming conventions

Use clear, descriptive names for agents and pools to improve
readability.

| **COMPONENT** | **NAMING CONVENTION** | **example** |
| --- | --- | --- |
| **AGENT** | <team or project name\>-<agent type\> | wis-api-self-hosted, welshpas-web-ms-hosted |
| **AGENT POOL** | <team or project name\>-<purpose\> | wis-api-build, welshpas-web-deploy |

!!! tip "Practical tips"
    When using [GitHub Advanced Security](enabling-github-advanced-security.md) allow additional URLs for the self-hosted agent to access data for *Dependency Scanning*.

!!! info "Further reading and information"
    [Deploy an Azure Pipelines agent on Windows - Azure Pipelines \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/pipelines/agents/windows-agent?view=azure-devops)

    [Enable TLS 1.2 on clients -- Configuration Manager \| Microsoft Learn](https://learn.microsoft.com/en-gb/mem/configmgr/core/plan-design/security/enable-tls-1-2-client)

    [Allowed address lists and network connections - Azure DevOps \| Microsoft Le arn](https://learn.microsoft.com/en-gb/azure/devops/organizations/security/allow-list-ip-url?view=azure-devops&tabs=IP-V4)

    [Configure GitHub Advanced Security for Azure DevOps -- Azure Repos \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/repos/security/configure-github-advanced-security-features?view=azure-devops&tabs=yaml)
