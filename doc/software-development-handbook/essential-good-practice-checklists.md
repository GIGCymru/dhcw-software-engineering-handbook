# Essential good practice checklists

Use these checklists to help follow our Principles & Standards. We
cross-reference each item to a relevant section in our standards or
guides. Exceptions are noted where they may apply.

## Requirements gathering, analysis and specifications

| **Item** |  |  | **Guide or standard** | **Exceptions** |
| --- | --- | --- | --- | --- |
| 1 | You have a Product Owner. | ☐ | [Cross-functional Scrum Teams](agile-delivery-using-scrum.md) | *Only applies if you follow Scrum* |
| 2 | You record user needs in *User Stories* or other Requirements Specifications. | ☐ | [Agile Practices for requirements gathering](agile-delivery-using-scrum.md) |  |
| 3 | You record non-functional & other requirements in *User Stories* or Requirements Specifications. | ☐ | [Agile Practices for requirements gathering](agile-delivery-using-scrum.md) |  |
| 4 | *User Stories* have clear acceptance criteria. | ☐ | [Agile Practices for requirements gathering](agile-delivery-using-scrum.md) |  |
| 5 | You prefix a Service request Ids to the title of the *User Story* | ☐ | [Agile Practices for requirements gathering](agile-delivery-using-scrum.md) |  |
| 6 | You link the service request in the User Story. | ☐ | [Agile Practices for requirements gathering](agile-delivery-using-scrum.md) |  |
| 7 | You plan your approach to mitigating security risks at the start of the project. | ☐ | [Security](security.md) |  |

### Planning, estimation and work tracking

| **Item** |  |  | **Guide or standard** | **Exceptions** |
| --- | --- | --- | --- | --- |
| 8 | *Scrum* events are used to plan and track work. | ☐ | [Agile delivery using Scrum](agile-delivery-using-scrum.md) | *Only applies if you follow Scrum* |
| 9 | You have a *Scrum* Master. | ☐ | [Cross-functional Scrum Teams](agile-delivery-using-scrum.md) | *Only applies if you follow Scrum* |
| 10 | Your *Scrum* team is multi-disciplinary. | ☐ | [Cross-functional Scrum Teams](agile-delivery-using-scrum.md) | *Only applies if you follow Scrum* |
| 11 | You record work items and defects using the Azure DevOps *Agile process template*. | ☐ | [Agile Planning with Azure DevOps](agile-delivery-using-scrum.md) |  |
| 12 | You associate *Tasks* with *User Stories*. | ☐ | [Agile Planning with Azure DevOps](agile-delivery-using-scrum.md) |  |
| 13 | You do **not** store Personal Identifiable Information (PII) in Azure DevOps. | ☐ | [Agile Planning with Azure DevOps](agile-delivery-using-scrum.md) |  |
| 14 | You publish test, build quality, code coverage & burn down metrics in Azure DevOps dashboards. | ☐ | [Agile Planning with Azure DevOps](agile-delivery-using-scrum.md) |  |

### Source control

| **Item** |  |  | **Guide or standard** | **Exceptions** |
| --- | --- | --- | --- | --- |
| 15 | Everything needed to build your project, including databases, is under source control. | ☐ | [Use Version Control](development-principles.md) |  |
| 16 | Sensitive data, such as API keys and passwords are stored in vaults & secrets and not in source control. | ☐ | [Use Version Control](development-principles.md) |  |
| 17 | You follow the *Conventional Commits* specification. | ☐ | [Use Version Control](development-principles.md) |  |
| 18 | Source code is peer reviewed. | ☐ | [Use Version Control](development-principles.md) | *May not be feasible for small teams. Nor always practical for bigger teams to peer review every code change.* |
| 19 | You specify a minimum number of reviewers for code reviews. | ☐ | [Use Version Control](development-principles.md) |  |
| 20 | You publish code review rules to a *README* or *CONTRIBUTING* markdown file. | ☐ | [Use Version Control](development-principles.md) |  |
| 21 | You publish your approach to branching and merging in a *README* or *CONTRIBUTING* markdown file. | ☐ | [Use Version Control](development-principles.md) |  |
| 22 | You store 3rd party dependencies in a common package feed. | ☐ | [Use Version Control](development-principles.md) |  |
| 23 | You check open-source packages for licence compliance and known vulnerabilities. | ☐ | [Use Version Control](development-principles.md) |  |

### Software design and maintainability

| **Item** |  |  | **Guide or standard** | **Exceptions** |
| --- | --- | --- | --- | --- |
| 24 | You record your approach to maintainability and reusability in a Solutions Design. | ☐ | [Adhere to a Solutions Architecture Design](development-principles.md) |  |
| 25 | You submit software designs for approval by the Technical Design Assurance Group. | ☐ | [Adhere to a Solutions Architecture Design](development-principles.md) |  |
| 26 | You link to specifications and the Solutions Architecture Document in the User Story's 'All Links' tab. | ☐ | [Adhere to a Solutions Architecture Design](development-principles.md) |  |
| 27 | You use design patterns to solve common problems. | ☐ | [Adhere to a Solutions Architecture Design](development-principles.md) |  |
| 28 | You deploy APIs via an API Management solution. | ☐ | [Adhere to a Solutions Architecture Design](development-principles.md) |  |
| 29 | You keep Software frameworks are kept up to date with long-term support. | ☐ | [Keep frameworks up-to-date](development-tools.md) |  |

### Coding standards

| **Item** |  |  | **Guide or standard** | **Exceptions** |
| --- | --- | --- | --- | --- |
| 30 | Your software solution is organised according to our conventions. | ☐ | [Follow our coding standards](development-principles.md#follow-coding-standards) | This may not be feasible for some legacy codebases. |
| 31 | You provide a *README.md* file in the root folder. | ☐ | [Follow our coding standards](development-principles.md#follow-coding-standards) |  |
| 32 | You use *SOLID* principles to make your code more testable. | ☐ | [Follow our coding standards](development-principles.md#follow-coding-standards) |  |
| 33 | You follow our conventions for naming unit tests. | ☐ | [Follow our coding standards](development-principles.md#follow-coding-standards) |  |
| 34 | You employ a common approach to logging exceptions. | ☐ | [Follow our coding standards](development-principles.md#follow-coding-standards) |  |
| 35 | You use our common SQL Prompt settings files to format T-SQL. | ☐ | [Follow our coding standards](development-principles.md#follow-coding-standards) |  |
| 36 | Your software meets all relevant accessibility standards. | ☐ | [User interface and accessibility standards](user-interface-and-accessibility-standards.md) |  |
| 37 | You mitigate application vulnerabilities. | ☐ | [Security](security.md) |  |
| 38 | You perform code analysis checks | ☐ | [Security](security.md) |  |

### Observing a definition of done

| **Item** |  |  | **Guide or standard** | **Exceptions** |
| --- | --- | --- | --- | --- |
| 39 | You publish common acceptance criteria in a *Definition of Done*. | ☐ | [Agile Practices for requirements gathering](agile-delivery-using-scrum.md) |  |
| 40 | You automate regression testing. | ☐ | [Adopt Continuous Integration (CI) and Continuous Delivery (CD)](development-principles.md) | *Some frameworks and legacy code may make impractical to write automated unit tests.* |
| 41 | Test Analysts peer review unit tests. | ☐ | [Testing](../restful-api-standards/testing.md) |  |
| 42 | You add a commit message prior to checking code into source control. | ☐ | [Use Version Control](development-principles.md) |  |
| 43 | You test during each *Sprint*. | ☐ | [Testing](../restful-api-standards/testing.md) | *Only applies if you follow Scrum* |
| 44 | You issue a *Test Summary Report* prior to each deployment. | ☐ | [Testing](../restful-api-standards/testing.md) |  |
| 45 | You agree opportunities for improvement at *Sprint* retrospectives. | ☐ | [Agile delivery using Scrum](agile-delivery-using-scrum.md) | *Only applies if you follow Scrum* |
| 46 | You account for security threats and vulnerabilities. For example, by adding security risk mitigations and a corresponding testing strategy to your definition of done. | ☐ | [Security](security.md) |  |

### Deployment

| **Item** |  |  | **Guide or standard** | **Exceptions** |
| --- | --- | --- | --- | --- |
| 47 | You can identify the work items associated with each release. | ☐ | [Use Version Control](development-principles.md) |  |
| 48 | Your branching and merging strategy identifies a release branch. | ☐ | [Use Version Control](development-principles.md) |  |
| 49 | You apply rules or policies to your release branch to prevent improper use. | ☐ | [Use Version Control](development-principles.md) |  |
| 50 | You maintain permissions on your project to prevent improper access. | ☐ | [Use Version Control](development-principles.md) |  |
| 51 | Your deployments are triggered by commits to source control. | ☐ | [Adopt Continuous Integration (CI) and Continuous Delivery (CD)](development-principles.md) | *Only applies if you practice trunk-based development.* |
| 52 | You maintain a deployment checklist or automated build & deployment script. | ☐ | [Adopt Continuous Integration (CI) and Continuous Delivery (CD)](development-principles.md) |  |
| 53 | You publish instructions on how to build and deploy your software in a *README* or *CONTRIBUTING* markdown file. | ☐ | [Follow our coding standards](development-principles.md#follow-coding-standards) |  |
| 54 | You can easily rollback to a previous release when required. | ☐ | [Use Version Control](development-principles.md) |  |

### Governance of technologies

| **Item** |  |  | **Guide or standard** | **Exceptions** |
| --- | --- | --- | --- | --- |
| 55 | You have the appropriate licences or subscriptions for the tools you use. | ☐ | [Activate software subscriptions](development-tools.md) |  |
| 56 | You comply with licencing terms and conditions for any 3rd party software you use, including open-source software. | ☐ | [Activate software subscriptions](development-tools.md) |  |
| 57 | You seek agreement from the Software Development Manager, Lead Developers group or Application & Architecture Assurance group before choosing a new technology. | ☐ | [Evaluating and adopting new tools](development-tools.md) |  |
