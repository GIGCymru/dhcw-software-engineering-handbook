# Include a decision records (ADRs) folder (./<rootfoldername\>/decisions)

Architecture Decision Records (ADRs) capture the context, the options
you considered, and the reasoning behind a significant decision.
Recording decisions as you make them preserves that context for anyone
who works on the solution later, rather than relying on memory or
scattered conversations.

You **SHOULD** write an ADR whenever your team makes a decision that is
significant to the architecture or design of your solution, would be
costly or difficult to reverse, or that future contributors would
benefit from understanding the reasoning behind. This includes
deliberately accepting technical debt -- see *Use ADRs to record
technical debt decisions* below -- but ADRs are not limited to that use
case.

This guidance builds on DHCW's [Architecture Decision Record process](https://gigcymru.github.io/architecture/design-authority/dhcw/architecture-decision-record-process/),
which describes when and how architecture decisions are recorded and
reviewed across DHCW.

## Store ADRs in a decision records folder

You **SHOULD** keep ADRs as close as possible to the teams and code they
affect, only moving them to a central location when they have wider
organisational impact.

- **Project-specific ADRs** **SHOULD** be stored as markdown files in a
    `decisions` folder in the root of the project's Git repository,
    alongside the code they relate to.

- **Cross-project or cross-team ADRs** **SHOULD** be stored in Git,
    preferably in a single shared location to avoid duplication.

- **Organisation-wide or significant ADRs** **MUST** follow the [DHCW Architecture Decision Record process](https://gigcymru.github.io/architecture/design-authority/dhcw/architecture-decision-record-process/);
    contributions are made in the internal `architecture-internal`
    repository, while `architecture` is a read-only public mirror.

You **SHOULD NOT** number ADR filenames. Instead, give each ADR a
descriptive, human-readable title in Title Case, avoiding acronyms, and
name the file after that title in kebab-case, for example
`use-a-managed-database-service.md` for a decision titled *Use a
Managed Database Service*. This follows DHCW's [Simplify Architecture Decision Records Structure](https://gigcymru.github.io/architecture/decisions/dhcw/meta-decisions/simplify-architecture-decision-records-structure/)
decision, which found that sequential numbering adds administrative
overhead -- keeping numbers unique and in order -- without improving
readability.

## Format ADRs using the DHCW template

You **SHOULD** use the [DHCW Architecture Decision Record template](https://gigcymru.github.io/architecture/design-authority/dhcw/architecture-decision-record-template/)
so ADRs are consistent and easy to review across the organisation.

## Retain and supersede ADRs

You **SHOULD NOT** delete or edit an ADR once it's agreed. If a decision
is superseded, record a new ADR explaining the change, and add a note to
the old ADR stating that it has been superseded, linking to the new one.

## Use ADRs to record technical debt decisions

Technical debt is one common reason to write an ADR. Where your team
knowingly accepts technical debt to meet a deadline, work around a
constraint, or defer a better solution to a later date, you **SHOULD**
record the decision as an ADR, covering the rationale, the trade-offs
considered, and a review point so the debt is revisited rather than
forgotten.

This complements DHCW's [Technical Debt](https://gigcymru.github.io/architecture/design-authority/dhcw/technical-debt/)
guidance and the [Technical debt](https://dhcw-digital-health-and-care-wales.github.io/dhcw-delivery-playbook/technical-debt/)
guidance in the DHCW Product and Service Delivery Playbook, which
describe how teams identify, prioritise and pay down debt as part of
their sprint cycle.

!!! tip "Practical tips"
    - Cross-team and organisation-wide ADRs **SHOULD NOT** be duplicated in project repositories; keep them only in their designated shared or internal repository.

    - Never delete an ADR, even once superseded; it remains a record of what was decided and why at the time.

!!! example "Examples of good practice"
    A team chooses a message queue over direct API calls to integrate
    two services. They record an ADR describing the alternatives
    considered, the reasons for choosing a message queue -- such as
    resilience to downstream outages -- and the trade-offs accepted,
    such as eventual consistency.

!!! warning "Practices to avoid"
    - Do not let significant decisions go undocumented; undocumented
        decisions are easily forgotten and harder to justify later.

    - Do not duplicate the same ADR across multiple repositories; link
        to a single source of truth instead.

!!! info "Further reading and information"
    [DHCW Architecture Decision Record process](https://gigcymru.github.io/architecture/design-authority/dhcw/architecture-decision-record-process/)

    [DHCW Architecture Decision Record template](https://gigcymru.github.io/architecture/design-authority/dhcw/architecture-decision-record-template/)

    [Simplify Architecture Decision Records Structure](https://gigcymru.github.io/architecture/decisions/dhcw/meta-decisions/simplify-architecture-decision-records-structure/)

    [DHCW Technical Debt guidance](https://gigcymru.github.io/architecture/design-authority/dhcw/technical-debt/)

    [Technical debt - DHCW Product and Service Delivery Playbook](https://dhcw-digital-health-and-care-wales.github.io/dhcw-delivery-playbook/technical-debt/)

    [How to start using ADRs with Git](https://github.com/architecture-decision-record/architecture-decision-record#how-to-start-using-adrs-with-git)
