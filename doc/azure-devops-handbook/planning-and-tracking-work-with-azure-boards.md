# Planning and tracking work with Azure boards

Following the practices described in this section aligns with *[Software development handbook](../software-development-handbook/introduction.md)*, helping you deliver incremental changes
in time-boxed sprints.

!!! info "Further reading and information"
    [Software development handbook](../software-development-handbook/introduction.md)

    [Agile Plan and Portfolio Management with Azure Boards - Training \| Microsoft Learn](https://learn.microsoft.com/en-gb/training/modules/plan-agile-github-projects-azure-boards/12-agile-plan-portfolio-management-azure-boards)

## Backlog naming conventions

The backlog is a list of work to complete*.* Prioritise work items based
on business value, using parent-child relationships to maintain a clear
hierarchy.

Name items consistently to minimise misunderstandings and support
automatic release notes generation. The following conventions are
**RECOMMENDED**:

| **WORK ITEM** | **TITLE CONVENTION** | **examples** |
| --- | --- | --- |
| **Epic** | Use action-oriented verbs to describe a high-level business initiative. | *Redesign the Authentication Flow for the NHS Wales Patient Portal.* |
| **FEATURE** | Use outcome-driven language to describe smaller, deliverable functionality. | *Implement Multi-Factor Authentication for the NHS Wales Patient Portal login.* |
| **USER STORY** | "As a \[persona\], I want \[something\] so that \[some reason\]\" | *As a user, I want to enter the SMS code I received so I can complete the authentication.* |
| **TASK** | Use action-oriented verbs to describe work needed for a user story. | *Design UI for SMS code entry.* |
| **BUG** | Focus on user impact and expected behaviour. | *Username field doesn't accept input after clicking, preventing login.* |
| **ISSUE** | Clearly describe a problem or blocker. | *Need approval for UI colours.* |
| **TEST PLAN** | High-level testing objectives, scope and activities. | *Validate Multi-Factor Authentication functionality, including SMS code input and error handling.* |
| **TEST CASE** | A specific scenario to test. | *Verify SMS code input field.* |

!!! info "Further reading and information"
    [Use backlogs to manage projects - Azure Boards \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/boards/backlogs/backlogs-overview?view=azure-devops)

    [Create your product backlog in Azure Boards - Azure Boards \| Microsoft Learn ](https://learn.microsoft.com/en-gb/azure/devops/boards/backlogs/create-your-backlog?view=azure-devops&tabs=agile-process)

## Refine user stories

Capture requirements in User Stories. When doing so:

- Provide a concise description from the user's perspective.

- Include clear acceptance criteria using Gherkin syntax to define 'done.'

> {IMAGE PLACEHOLDER}

!!! info "Further reading and information"
    [Manage requirements, Agile - Azure DevOps \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/cross-service/manage-requirements?view=azure-devops&tabs=agile-process)

## Link service requests

For operational service requests, prefix a work item's title with the
request ID and add a link to the request in the '*All Links'* tab.

Alternatively consider using a custom process template with a *Change
Reference* field. Contact your Organisation Owner for details.

## Match work to the right Azure board

Use *Kanban Boards* (Boards \> Boards) for continuous or unplanned work
and *Task Boards* (Boards \> Sprints) for sprint tracking.

Use tags, custom fields or queries to simplify navigation and reduce
backlog clutter.

!!! info "Further reading and information"
    [Plan and track work in Azure Boards - Azure Boards \| Microsoft Lear n](https://learn.microsoft.com/en-gb/azure/devops/boards/get-started/plan-track-work?view=azure-devops&tabs=agile-process)

    [Manage columns on your board - Azure Boards \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/boards/boards/add-columns?view=azure-devops&tabs=process-administrator#add-the-definition-of-done-to-a-column)

    [Use your board - Azure Boards \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/boards/boards/kanban-quickstart?view=azure-devops)

## Boards naming & style conventions

Use these conventions to maintain consistency in how work items are
represented:

| **COMPONENT** | **CONVENTION / STYLE** | **examples** |
| --- | --- | --- |
| **TAGS** | *Use colours to indicate meaning.* | *Blocked* (Red), *External Dependency* (Blue), *Discovery* (Yellow) |
| **CARD STYLE** | Priority = 1: Highlight high-priority items in Orange. | *Priority=1 (Orange)* |
| **COLUMN NAMING** | Standardise naming across boards. | New, Active, Closed, Test |

!!! info "Further reading and information"
    [Customize cards on a board - Azure Boards \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/boards/boards/customize-cards?view=azure-devops)

## Implement your definition of done

Define shared criteria for each Board column and record it in the
'*Definition of Done*' field.

> {IMAGE PLACEHOLDER}

!!! info "Further reading and information"
    [Add Definition of Done to a column - Azure Boards \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/boards/boards/add-columns?view=azure-devops#add-definition-of-done-to-a-column)

## Set-up delivery plans (optional)

Delivery Plans track work across projects but are **NOT**
**RECOMMENDED** if using tools like Float.

!!! info "Further reading and information"
    [Review team delivery plans in Azure Boards - Azure Boards \| Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/boards/plans/review-team-plans?view=azure-devops)

## Drive development from work items

Link work items to commits, branches, builds, and releases for better
traceability and alignment between code and tasks. See [Link Work items
to Builds](automating-builds-and-deployments-with-azure-pipelines.md) for more details.

## Track progress of builds and releases

Add status badges to a repos' README file to indicate code stability.
