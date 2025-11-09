# Securing your projects

You **MUST** follow these essential practices to ensure robust security:

- Review permissions **monthly**, ensuring access follows the
    *least-privilege principle*.

- Remove permissions **as soon as** users no longer need access.

- Use fine-grained permissions to restrict access to what's necessary.

- Prefer *Federated Identity* over *Service Connections* when
    possible.

- Avoid *Personal Access Tokens (PATs)* but if used, recycle them
    every ***90 days***.

- Limit access to the minimum required for each user.

!!! info "Further reading and information"
    [Security best practices - Azure DevOps \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/organizations/security/security-best-practices?view=azure-devops)

    [Other security considerations for Azure Pipelines - Azure Pipelines \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/pipelines/security/misc?view=azure-devops)

    [Delete, remove users from team, project, organisation - Azure DevOps \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/organizations/accounts/delete-organization-users?view=azure-devops&tabs=browser)
