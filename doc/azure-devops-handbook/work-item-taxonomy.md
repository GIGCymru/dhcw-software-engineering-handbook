# Work Item Taxonomy

A standardised taxonomy for categorising work items ensures consistent classification, accurate metrics, and effective prioritisation across teams.

## The problem with classification drift

Without a shared language for work items, teams experience "classification drift" which leads to several problems:

- **Feature requests** logged as **Defects** artificially inflating bug counts and creating a false perception of low software quality.
- **Stakeholder preferences** (UI/UX polish) confused with **Bugs**, making it difficult for engineers to prioritise actual breaks over subjective improvements.
- **Risks** confused with **Impediments**; for example, a stakeholder might raise a "Risk" for something that is already broken (a bug) or a "Bug" for a potential future problem (a risk).

This ambiguity impacts velocity tracking, DORA metrics, and sprint reporting, leading to inefficient overhead and unnecessary stakeholder involvement.

## Benefits of standardisation

- **Accurate Quality Metrics:** Distinguish between technical debt, regressions, and new value.
- **Streamlined Triage:** Items can be easily classified based on agreed taxonomy and definitions.
- **Objective Prioritisation:** Helps the business understand the trade-off between fixing known issues versus building new features.
- **Improved Reporting:** Allows leadership to see exactly where engineering effort is being spent (e.g., "We spent 40% of the sprint on Chores versus 20% on Features").

## Standard work item categories

Use these definitions when categorising work in Azure DevOps to ensure consistency across all teams and projects.

| Category | Definition | Key Question to Ask |
| --- | --- | --- |
| **Defect (Bug)** | A failure to meet existing, agreed-upon requirements. The system is behaving in a way it was explicitly built NOT to behave. | "Is this a regression or a failure of existing logic?" |
| **New Feature** | Functionality that does not currently exist. It introduces new capabilities or solves a new user problem. | "Does this add new value that wasn't there before?" |
| **Improvement (Enhancement)** | An update to an existing feature to make it better, faster, or easier to use, without changing the original core requirement. | "Is the feature working, but could be more efficient/usable?" |
| **Task (Chore / Tech Debt)** | Necessary technical work that provides no direct user-facing value but maintains system health. | "Is this for the developer's benefit or system stability?" |
| **Risk** | A potential future event that may negatively impact the project or product. It has not happened yet. | "Is this something that might go wrong later?" |
| **Issue (Impediment)** | A non-technical blocker or a current problem that is stopping progress but isn't a code bug. | "Is something outside the codebase stopping us from moving?" |
| **Spike** | A time-boxed research task to investigate a technical approach or reduce uncertainty before implementation. | "Do we need to learn more before we can estimate the work?" |

!!! tip "Practical tips"
    When in doubt, ask yourself the key question for each category. This helps ensure items are classified correctly from the start.

!!! example "Examples of good practice"
    - A login button that doesn't respond when clicked → **Defect (Bug)**
    - Adding two-factor authentication to the login flow → **New Feature**
    - Making the login button larger and more visible → **Improvement (Enhancement)**
    - Upgrading a library dependency to patch a security vulnerability → **Task (Chore / Tech Debt)**
    - The authentication service might not scale to handle peak load → **Risk**
    - Waiting for legal approval to proceed with data processing → **Issue (Impediment)**
    - Investigating which authentication library best suits our needs → **Spike**

## Mapping to Azure DevOps work item types

Azure DevOps provides several work item types. Map the taxonomy categories to Azure DevOps as follows:

| Taxonomy Category | Azure DevOps Work Item Type | Notes |
| --- | --- | --- |
| **Defect (Bug)** | Bug | Use the built-in Bug work item type |
| **New Feature** | Feature or User Story | Use Feature for large initiatives, User Story for smaller deliverables |
| **Improvement (Enhancement)** | User Story | Tag with "Enhancement" or use a custom field |
| **Task (Chore / Tech Debt)** | Task | Tag with "Tech Debt" or "Chore" for reporting purposes |
| **Risk** | Issue | Use the Issue work item type, or consider using a separate Risk Register |
| **Issue (Impediment)** | Issue or Impediment | Use the Issue work item type and tag with "Impediment" |
| **Spike** | Task or Spike | Use Task and tag with "Spike", or create a custom Spike work item type |

!!! tip "Practical tips"
    Use tags consistently to enable better filtering and reporting. For example, tag all technical debt items with "TechDebt" to track the proportion of sprint effort spent on maintenance.

## Alignment with backlog naming conventions

The taxonomy definitions complement the [Backlog naming conventions](planning-and-tracking-work-with-azure-boards.md#backlog-naming-conventions) already in use. When creating work items:

1. **Choose the correct category** using the taxonomy definitions above.
2. **Apply the naming convention** for that work item type.
3. **Add clear descriptions** and acceptance criteria.

!!! info "Further reading and information"
    [Planning and tracking work with Azure boards](planning-and-tracking-work-with-azure-boards.md)

    [Work Item Triage Guide](work-item-triage-guide.md) - Guidance for non-technical stakeholders

    [Use agile process template artifacts - Azure Boards | Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/boards/work-items/guidance/agile-process?view=azure-devops)

    [About work item types - Azure Boards | Microsoft Learn](https://learn.microsoft.com/en-gb/azure/devops/boards/work-items/about-work-items?view=azure-devops)

## Implementing the taxonomy in your project

To adopt this taxonomy in your Azure DevOps project:

1. **Review existing work items:** Identify any misclassified items and update them according to the taxonomy.
2. **Update project templates:** Configure work item templates to include taxonomy guidance.
3. **Train team members:** Conduct a walkthrough during a Sprint Planning or All-Hands meeting to ensure everyone understands the definitions.
4. **Update dashboards:** Configure reporting dashboards to reflect the taxonomy categories for better visibility of where effort is being spent.
5. **Refine continuously:** Review classification during Sprint Retrospectives and adjust as needed.

!!! warning "Practices to avoid"
    - Don't create work items without first determining the correct category.
    - Avoid mixing multiple categories in a single work item (e.g., a Bug that also introduces a New Feature).
    - Don't reclassify items arbitrarily to manipulate metrics.

## Success criteria

You'll know the taxonomy is working effectively when:

- Teams consistently classify work items correctly with minimal debate.
- Reporting dashboards provide clear insights into where engineering effort is focused.
- Stakeholders can differentiate between bugs, features, and other work types.
- Quality metrics accurately reflect the true state of the software.

!!! info "Further reading and information"
    [Software development handbook](../software-development-handbook/introduction.md)

    [Agile delivery using Scrum](../software-development-handbook/agile-delivery-using-scrum.md)
