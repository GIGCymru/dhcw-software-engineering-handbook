# Use Architecture Decision Records (ADRs) to manage technical debt

Teams **SHOULD** use Architecture Decision Records (ADRs) to document
deliberate technical debt decisions. Recording these decisions preserves
the context and reasoning behind them, making technical debt easier to
review and manage over time.

This guidance builds on DHCW's [Technical Debt](https://gigcymru.github.io/architecture/design-authority/dhcw/technical-debt/)
guidance, particularly the *Architecture Decision Records (ADRs)* section
under *Relationship to Architecture Governance*, which describes how an
ADR that records a deviation, with its rationale and trade-offs, converts
inadvertent conformance debt into deliberate, managed debt. It
complements the [Technical debt](https://dhcw-digital-health-and-care-wales.github.io/dhcw-delivery-playbook/technical-debt/)
guidance in the DHCW Product and Service Delivery Playbook, which
describes how teams identify, prioritise and pay down debt as part of
their sprint cycle.

## When to write an ADR

You **SHOULD** write an ADR whenever your team knowingly accepts
technical debt to meet a deadline, work around a constraint, or defer a
better solution to a later date.

Each ADR **SHOULD** record:

- The rationale for accepting the debt

- The trade-offs considered, including alternatives that were rejected

- The risks introduced by the decision

- A review point, so the debt is revisited rather than forgotten

## Where to store ADRs

You **SHOULD** keep ADRs as close as possible to the teams and code they
affect, only moving them to a central location when they have wider
organisational impact.

- **Project-specific ADRs** **SHOULD** be stored in the project's Git
    repository, alongside the code they relate to.

- **Cross-project or cross-team ADRs** **SHOULD** be stored in Git,
    preferably in a single shared location to avoid duplication.

- **Organisation-wide or significant ADRs** **MUST** follow the [DHCW Architecture Decision Record process](https://gigcymru.github.io/architecture/design-authority/dhcw/architecture-decision-record-process/); contributions are made in the internal `architecture-internal` repository, while `architecture` is a read-only public mirror.

## Track technical debt in Azure DevOps

The DHCW Product and Service Delivery Playbook's [Technical debt](https://dhcw-digital-health-and-care-wales.github.io/dhcw-delivery-playbook/technical-debt/)
guidance requires every debt item to be captured as a ticket in Azure
DevOps, tagged **Tech Debt**, so it's visible, estimable and can be
prioritised alongside other work.

You **SHOULD** link the ADR to its corresponding Azure DevOps ticket,
and the ticket back to the ADR, so the rationale for the decision stays
connected to the work item used to track and prioritise paying it down.

## How to format ADRs

You **SHOULD** use the [DHCW Architecture Decision Record template](https://gigcymru.github.io/architecture/design-authority/dhcw/architecture-decision-record-template/)
so ADRs are consistent and easy to review across the organisation.

!!! tip "Practical tips"
    - For project-specific ADRs, store them as markdown files in an `adr` or `docs/adr` folder in the repository so they're version controlled alongside the code they describe. Cross-team and organisation-wide ADRs **SHOULD NOT** be duplicated this way; keep them only in their designated shared or internal repository.

    - Never delete them; if a decision is superseded, record a new ADR that supersedes the old one and add a note to the old ADR stating such.

    - Reference related ADRs from your Azure DevOps **Tech Debt** tickets so technical debt remains visible and can be prioritised.

!!! example "Examples of good practice"
    A team accepts a short-term workaround to meet a release deadline.
    They record an ADR explaining why the workaround was chosen, what
    the preferred long-term solution is, and set a review date at the
    next quarterly planning session.

!!! warning "Practices to avoid"
    - Do not let technical debt go undocumented; undocumented debt is
        easily forgotten and harder to justify addressing later.

    - Do not duplicate the same ADR across multiple repositories; link
        to a single source of truth instead.

!!! info "Further reading and information"
    [DHCW Technical Debt guidance](https://gigcymru.github.io/architecture/design-authority/dhcw/technical-debt/)

    [Technical debt - DHCW Product and Service Delivery Playbook](https://dhcw-digital-health-and-care-wales.github.io/dhcw-delivery-playbook/technical-debt/)

    [DHCW Architecture Decision Record template](https://gigcymru.github.io/architecture/design-authority/dhcw/architecture-decision-record-template/)

    [How to start using ADRs with Git](https://github.com/architecture-decision-record/architecture-decision-record#how-to-start-using-adrs-with-git)
