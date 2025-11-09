# Commit changes early and often

Committing code early and often provides several benefits:

- It reduces the risk of losing code, e.g., due to local disk failure.

- It encourages building smaller, modular components, simplifying
    rollback.

- It makes integrating changes into the main or master branch easier.

You **MUST** commit changes to your main codebase as soon as possible,
regardless of whether you are using [trunk-based
development](adopt-trunk-based-development-and-continuous-integration.md)
or [feature branches](follow-a-branching-strategy.md).

You **SHOULD** commit related changes together and keep commits as small
as possible. Smaller commits make rollback easier and minimise
disruptions.

You **SHOULD NOT** commit large batches of unrelated work. It
complicates code reviews and rollbacks.
