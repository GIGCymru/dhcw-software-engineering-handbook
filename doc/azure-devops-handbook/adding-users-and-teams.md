# Adding users and Teams

## Add users

When adding users, you **MUST** grant only the minimum access level
necessary. Use built-in [security groups](azure-devops-basics.md) for
easier management, avoiding broad groups unless essential.

!!! info "Further reading and information"
    [Add users or groups to a team or project - Azure DevOps \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/organizations/security/add-users-team-project?view=azure-devops&tabs=preview-page)

## Add additional Teams

Each project has a default team, "*<Project Name\>* Team". You can add
teams for specific areas or products, each with its own backlogs,
sprints, and dashboards.

!!! tip "Practical tips"
    When creating a team, use a clear, descriptive name that reflects its focus (e.g. feature or product), Avoid generic terms like *"Developers".*

!!! example "Examples of good practice"
    **Phoenix Portal Team:** Front-end UI and integration with back-end APIs.

    **Titan Mobile Team:** Mobile app and integration with back-end APIs.

    **Atlas Immunisations API Team:** Backend Immunisation APIs.

    **Helios Appointments Team**: Immunisations appointment scheduler microservice.

    **Developers**

!!! info "Further reading and information"
    [Create or add a team - Azure DevOps \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/organizations/settings/add-teams?view=azure-devops&tabs=preview-page)

## Configure area paths for Teams

Create a new area path for each new Azure DevOps team. This keeps
backlogs, boards, and queries specific to each team while allowing
access to the shared backlog.

!!! info "Further reading and information"
    [Define area paths and assign to a team - Azure Boards \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/organizations/settings/set-area-paths?view=azure-devops&tabs=browser)
