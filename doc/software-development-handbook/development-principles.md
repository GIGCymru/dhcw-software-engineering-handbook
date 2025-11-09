# Development principles

## Ahdere to a solutions architecture

Software **SHOULD** align with our API-first and Cloud-first strategies.
Follow a Solutions Architecture Design, reviewed by the Technical Design
Assurance Group, to meet these goals.

!!! info "Further reading and information"
    [RESTful API Design and Build Standards](../restful-api-standards/introduction.md)

    [Architectural principles \| Microsoft Learn](https://learn.microsoft.com/en-gb/dotnet/architecture/modern-web-apps-azure/architectural-principles)

## Write modular code

Build modular code using APIs and NuGet packages.

!!! info "Further reading and information"
    [Azure DevOps handbook](../azure-devops-handbook/introduction.md)

!!! tip "Practical tips"
    Sharing validated, trusted code is a principle of secure coding.

## Use version control

Effective source control is essential. Follow our [guide for help](../using-source-control/introduction.md).

!!! note "Using source control"
    - Structure repositories for clarity and scalability.

    - Use consistent branching and merging strategies.

    - Follow versioning conventions to track releases.

    - Write clear, conventional commit messages.

    - Conduct constructive code reviews.

!!! info "Further reading and information"
    [Using Source Control](../using-source-control/introduction.md)

    [RESTful API Design and Build Standards](../restful-api-standards/introduction.md)

    [Azure DevOps handbook](../azure-devops-handbook/introduction.md)

    [What is Git? - Azure DevOps \| Microsoft Learn](https://learn.microsoft.com/en-gb/devops/develop/git/what-is-git)

!!! tip "Practical tips"
    Apply source control to databases and application code.

## Follow coding standards

Deliver reliable, maintainable software by adhering to these guides:

!!! note
    [T-SQL Coding Standard](../t-sql-coding-standard/introduction.md)

    Rules for table design, maintainable queries, procedures, and transaction handling.

!!! note
    [How to Organise Your Software Solution](../organising-your-solution/introduction.md)

    Guidance on project structure, folder conventions, documentation, and dependency layering.

!!! note
    [General Coding Standards](../general-coding-standards/introduction.md)

    Clean code, defensive coding, implementing SOLID principles and Microsoft formatting and naming standards.

!!! info "Further reading and information"
    [T-SQL Coding Standard](../t-sql-coding-standard/introduction.md)

    [How to Organise Your Software Solution](../organising-your-solution/introduction.md)

    [General Coding Standards](../general-coding-standards/introduction.md)

## Adopt Continuous Integration (CI) and Continuous Delivery (CD)

All teams **MUST** use CI/CD to improve quality and accelerate the
frequency of deployment.

!!! info "Further reading and information"
    [Use continuous integration - Azure DevOps \| Microsoft Learn](https://learn.microsoft.com/en-gb/devops/develop/what-is-continuous-integration)

    [What is continuous delivery? - Azure DevOps \| Microsoft Learn](https://learn.microsoft.com/en-gb/devops/deliver/what-is-continuous-delivery)

    [Continuous Delivery vs Continuous Deployment - Continuous Delivery](https://continuousdelivery.com/2010/08/continuous-delivery-vs-continuous-deployment/#:~:text=While%20continuous%20deployment%20implies%20continuous,in%20the%20hands%20of%20IT.&text=That%20means%20no%20more%20testing,you're%20using%20Scrum)

    [What is DevOps? - Azure DevOps \| Microsoft Learn](https://learn.microsoft.com/en-gb/devops/what-is-devops?view=azure-devops)

For full guidance on how to implement CI/CD, refer to the references
below:

!!! info "Further reading and information"
    [Using Source Control](../using-source-control/introduction.md)

    [Azure DevOps handbook](../azure-devops-handbook/introduction.md)

## Publishing as open source

The *Digital Service Standard for Wales* and the *Welsh Technical
Standards Board* encourage making source code open. But this guide does
not cover open-source publishing.

If you plan to make your source code open, you **SHOULD** obtain the
necessary approval and comply with any necessary organisational or legal
requirements.

!!! info "Further reading and information"
    [Digital Service Standards - Digital Public Service Wales (gov.wales)](https://digitalpublicservices.gov.wales/toolbox/digital-service-standards/#work-open)

    [Welsh Technical Standards Board \| A statement of principles](https://standards.cymru/posts/2018-12-01-wtsb/#4-open-by-default-open-technical-standards-and-open-source-code)

    [Public Repos · GIGCymru/GitHub-GIG-Cymru Wiki](https://github.com/GIGCymru/GitHub-GIG-Cymru/wiki/Public-Repos)

!!! tip "Practical tips"
    Access to *github.com/GIGCymru/GitHub-GIG-Cymru/wiki/Public-Repos* requires a DHCW GitHub Enterprise account.
