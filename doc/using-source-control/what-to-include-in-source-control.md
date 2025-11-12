# What to include in source control

You **MUST** include:

- Everything needed to build your project, including the database.

- A README.md and CONTRIBUTING.md file. Other documentation **MAY** be
    kept outside source control.

You **MUST NOT** include:

- Sensitive information, such as API keys, passwords, or server names.
    Instead, use environment variables or key stores.

- Personal Identifiable Information (PII).

You **SHOULD** exclude:

- Compilation output and user settings files. Use a .gitignore file
    (e.g., for Visual Studio) to manage exclusions.

Additional **RECOMMENDATIONS**:

- Use Redgate Source Control to manage your database.

- Use package management to avoid storing dependencies in source
    control.

!!! tip "Practical tips"
    **Disaster Recovery**

    In 2017, a disaster recovery test revealed weaknesses in our source control system, risking longer recovery times and data loss. These issues **HAVE** since been resolved.

!!! info "Further reading and information"
    [How to Organise Your Software Solution](../organising-your-solution/introduction.md)

    [gitignore/VisualStudio.gitignore at main · github/gitignore](https://github.com/github/gitignore/blob/main/VisualStudio.gitignore)
