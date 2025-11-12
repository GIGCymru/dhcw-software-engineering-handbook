# Azure DevOps basics

## Core concepts and terminology

| **Concept** | **Description** |
| --- | --- |
| **Organisation** | The top-level container, representing a server instance. Each organisation has its own configuration and owner. |
| **Project** | A unit within an organisation that includes repositories, planning tools, and Continuous Integration (CI) & Continuous Delivery (CD) capabilities. |
| **Team** | A subset of a project, enabling smaller groups to work on specific features or components. |
| **Access Levels** | These define the available features to a user, There are three access levels: *Stakeholder*, *Basic* and *Basic + Test Plans*. |
| **Access Permissions** | These control specific actions (e.g. read, write, delete) on resources within projects. |
| **Security Groups** | These group users to manage permissions and apply policies consistently. |

## Key features

| **Concept** | **FUNCTION** |
| --- | --- |
| **Boards** | Track and prioritise work using tasks, sprints, and backlogs. |
| **Repos** | Manage and store source code in Git repositories. |
| **Pipelines** | Automate code build, test and deployment processes. |
| **Artifacts** | Store build outputs, like compiled binaries and packages. |
| **Test Plans** | Define and execute test cases to ensure code quality. |

## Common security groups

Azure DevOps organises user permissions into roles. Use the table below
to determine which role best suits your needs.

| **Role** | **Description** |
| --- | --- |
| **Contributor** | Daily users of Azure DevOps. Key tasks: - Cloning, pushing, and pulling code in repositories. - Creating and managing work items, tasks, and bugs. - Participating in sprints and board activities. - Triggering and monitoring CI/CD pipelines. |
| **Project Administrator** | Administers specific projects. Key responsibilities: - Assigning user permissions and configuring project settings. - Setting up repositories, boards, and sprint iterations. - Creating and maintaining CI/CD pipelines and housekeeping tasks. |
| **Project Collection Administrator** | Oversees multiple projects. Key tasks: - Managing shared resources like package feeds and deployment agents. - Setting up pipelines that span projects. |
| **Organisation Owner** | Global administrator for the organisation. Responsibilities include: - Creating projects and configuring global policies. - Managing billing, subscriptions and user accounts. |
