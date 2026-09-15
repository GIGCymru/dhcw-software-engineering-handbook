# Software Engineering Handbook

This site shares Digital Health and Care Wales' (DHCW) Software Engineering Handbook.
Until now, these have only been available to internal staff.

## Why have a handbook?

When you're building software, especially in healthcare, good guidance really matters. It helps everyone work in a consistent way, so the code is easier to understand, safer, and more reliable.

A handbook brings together all the important know-how: how to write clear, secure code; how to manage changes properly; how to work well across teams; and how to meet the expectations of modern software development.

It's there to help you make good decisions, avoid mistakes, and deliver software that others can trust and build on.

## How this handbook is organised

The handbook is split into the following sections:

- [Software Development Handbook](software-development-handbook/introduction.md) — how to manage software development projects for DHCW.
- [Using Source Control](using-source-control/introduction.md) — good practice for using source control and conducting code reviews.
- [Organising Your Solution](organising-your-solution/introduction.md) — how to structure the folders and files of a software solution.
- [General Coding Standards](general-coding-standards/introduction.md) — general coding standards for software development.
- [T-SQL Coding Standard](t-sql-coding-standard/introduction.md) — the coding standard for writing T-SQL.
- [RESTful API Standards](restful-api-standards/introduction.md) — requirements and guidance for designing and building RESTful APIs.
- [Azure DevOps Handbook](azure-devops-handbook/introduction.md) — how to use Azure DevOps to manage software projects.
- [Software Subscriptions](software-subscriptions/introduction.md) — how to identify, request and manage software subscriptions.
- [Test Summary Report](test-summary-report/introduction.md) — how to write a Test Summary Report.
- [Testing for Lost Updates](testing-lost-updates/introduction.md) — how to test for lost updates and other database concurrency bugs.

There's also a [Coding Standard Template](coding-standard-template/coding-standard-template.md) to use as a starting point when authoring a new coding standard.

## Conventions

This section explains the conventions used throughout the handbook.

!!! rfc-terms "Terminology and Requirements"
    To be clear about what’s expected, we use specific words with defined meanings, as described in [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119):

    | | | |
    | --- | --- | --- |
    | **MUST** | **MUST NOT** | **REQUIRED** |
    | **SHALL** | **SHALL NOT** | **SHOULD** |
    | **SHOULD NOT** | **RECOMMENDED** | **MAY** |
    | **OPTIONAL** | | |

This handbook uses four consistent callout boxes:

!!! tip "Practical tips"
    Practical advice and recommendations.

!!! example "Examples of good practice"
    Worked examples showing the standard applied correctly.

!!! warning "Practices to avoid"
    Practices that don't meet the standard.

!!! info "Further reading and information"
    Links to further guides, information and work instructions. If a hyperlink is missing, search for the document in our Document Management System.

### Exceptions prove the rule

As with most standards, there are occasions when it's unwise to follow
"hard and fast" rules.

Principal and Lead software developers have discretion to do so but this
should be the exception rather than the rule.

## Contributing

We welcome suggestions and improvements from colleagues, partners, and the wider community.

To suggest a change, please open an issue using the issue form on this repository.

Please read:

- [Contributing Guide](https://github.com/GIGCymru/dhcw-software-engineering-handbook/blob/main/CONTRIBUTING.md)
- [Code of Conduct](https://github.com/GIGCymru/dhcw-software-engineering-handbook/blob/main/CODE_OF_CONDUCT.md)

If you're unsure whether your idea is ready, open an issue anyway and a maintainer will help shape it.
