# Write clear commit messages

Commit messages are essential for understanding the history, context,
and purpose of code changes. Following these standards will:

- Improve collaboration and communication across teams.

- Make it easier to debug, trace changes and manage the codebase
    effectively.

- Ensure consistency and professionalism in your projects.

You **MUST** write a commit message for every change.

Commit messages **MUST** be clear, concise, and follow a consistent
format.

You **SHOULD:**

- Use the Conventional Commits specification to structure your
    messages.

- Link commits to work items, bugs, or tasks using identifiers.

!!! tip "Practical tips"
    In Visual Studio, include the work item ID, e.g., #123 , in your commit message. Visual Studio will automatically link the commit to the corresponding work item.

Additional **RECOMMENDATIONS**:

- Consider tools like VsCommitizen or commitlint to help enforce
    standards.

- Use branch policies to ensure commit messages comply with
    requirements.

- Use "because" in your message to clarify the reasoning behind
    changes.

!!! info "Further reading and information"
    [Conventional Commits](https://www.conventionalcommits.org)

    [VsCommitizen - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=mrluje.vs-commitizen&ssr=false#qna)

## Commit message standard

Each commit message **MUST** follow this template:

!!! example "Examples of good practice"
    *<type**\>\[optional scope\]: description*

    *\[optional body\]*

    *\[optional footers\]*

*<type\>:* describes the purpose of the commit. You **MUST** append a !
to *<type\>* if the commit introduces a breaking change (e.g. `feat`!).

| **TYPE** | **DESCRIPTION** |
| --- | --- |
| `feat`: | A new feature. |
| `fix`: | A bug fix. |
| `build`: | Changes to the build system or dependencies. |
| `chore`: | Maintenance tasks that do not affect application functionality. |
| `ci`: | Changes to CI/CD pipelines or configuration. |
| `docs`: | Documentation updates. |
| `style`: | Code formatting changes (e.g., indentation, spacing) without functional impact. |
| `refactor`: | Code changes that improve structure & clarity without changing behaviour. |
| `perf`: | Performance improvements. |
| `test`: | Adding or modifying tests |

The *<summary\>* **MUST**:

- Be 50 characters or fewer.

- Use the imperative mood (e.g. "Add login validation").

The *<body\>* **SHOULD**:

- Provide additional context (e.g. **why** a change was made).

- Be wrapped at 72 characters per line for readability.

Additional **RECOMMENDATIONS**:

- Avoid ending with punctuation.

!!! example "Examples of good practice"
    *feat: Add support for user authentication*

    *Introduced OAuth-based login for secure access. Closes Task#1234*

!!! example "Examples of good practice"
    *fix: Resolve API timeout issue on large datasets*

    *Adjusted query execution to improve performance. Resolves Bug#5678*

!!! example "Examples of good practice"  
    *docs: Update README with deployment instructions*

    *Added steps for configuring environment variables and services*

!!! warning "Practices to avoid"
    *Changeset 12345*

    *The best version EVER again!*

    *Second update*

!!! info "Further reading and information"
    [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)

    [commitlint/@commitlint/config-conventional at master · conventional-changelog/commitlint · GitHub](https://github.com/conventional-changelog/commitlint/tree/master/%40commitlint/config-conventional)

    [A Note About Git Commit Messages](https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)

    [How to Write a Git Commit Message (cbea.ms)](https://cbea.ms/git-commit/)

    [How to Write Good Commit Messages: A Practical Git Guide (freecodecamp.org)](https://www.freecodecamp.org/news/writing-good-commit-messages-a-practical-guide/)

    [Writing Meaningful Commit Messages --- Beanstalk (beanstalkapp.com)](https://blog.beanstalkapp.com/post/134929320564/detailed-commit-messages-are-an-essential-part-of)
