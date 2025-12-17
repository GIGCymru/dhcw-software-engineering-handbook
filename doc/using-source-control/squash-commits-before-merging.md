# Squash commits before merging

When working on feature branches or preparing changes for merge to the
trunk (main or master), you **SHOULD** squash related commits into
logical, coherent units before merging. This practice creates a cleaner,
more maintainable commit history.

## Why squash commits?

Squashing commits before merging to the trunk provides several benefits:

- **Cleaner history**: The trunk's commit log remains focused on
    meaningful changes rather than work-in-progress commits.

- **Easier debugging**: Tools like `git bisect` are more effective when
    each commit represents a complete, logical change.

- **Better code archaeology**: Future developers can understand the
    evolution of the codebase by examining meaningful commits rather than
    piecing together fragments.

- **Simplified rollbacks**: Rolling back a feature is straightforward
    when it's represented as a single commit or a small number of logical
    commits.

- **Professional presentation**: A well-curated commit history
    demonstrates care and attention to detail in your work.

## When to squash

You **SHOULD** squash commits in these scenarios:

- Before merging a feature branch into the trunk.

- When multiple commits address the same logical change (e.g., "Add
    feature X", "Fix typo", "Address review comments", "Fix tests").

- When you have work-in-progress commits that were made for backup or
    intermediate check-pointing purposes.

You **SHOULD NOT** squash in these scenarios:

- Commits that represent genuinely distinct logical changes or features.

- Commits that have already been pushed to a shared branch that others
    may have based work on.

- When preserving detailed history is required for compliance, audit, or
    regulatory purposes.

## What to keep vs. what to squash

When preparing your branch for merge, consider the following guidance:

**Keep separate commits for**:

- Distinct features or bug fixes that could be deployed independently.

- Changes that affect different subsystems or components.

- Refactoring commits that should be reviewed separately from functional
    changes.

- Changes that may need to be cherry-picked to other branches
    independently.

**Squash together**:

- The initial implementation and subsequent fixes for the same feature.

- Commits fixing typos, formatting, or linting issues in your own recent
    work.

- "Work in progress" commits made for backup purposes.

- Commits addressing code review feedback for the same logical change.

- Test updates made alongside the code they test.

## How to squash commits

### Interactive rebase

The most flexible approach is using interactive rebase. This allows you
to combine, reorder, edit, or drop commits.

To squash the last N commits (e.g., the last 5 commits):

```bash
git rebase -i HEAD~5
```

To squash all commits on your feature branch since it diverged from main:

```bash
git rebase -i main
```

This opens an editor showing your commits:

```bash
pick abc1234 Add user authentication feature
pick def5678 Fix typo in login form
pick ghi9012 Add tests for authentication
pick jkl3456 Address code review comments
pick mno7890 Fix failing test
```

Change `pick` to `squash` (or `s`) for commits you want to combine with
the previous commit:

```bash
pick abc1234 Add user authentication feature
squash def5678 Fix typo in login form
squash ghi9012 Add tests for authentication
squash jkl3456 Address code review comments
squash mno7890 Fix failing test
```

Save and close the editor. Git will then prompt you to edit the combined
commit message. Remove or combine the individual messages into one
coherent message:

```text
Add user authentication feature

Implement login and registration functionality with form validation,
session management, and comprehensive test coverage.
```

### Squash merge

If your workflow uses pull requests, many platforms offer a "squash and
merge" option. This automatically squashes all commits in the pull
request into a single commit when merging:

- **GitHub**: Select "Squash and merge" when merging a pull request
- **Azure DevOps**: Select "Squash commit" in the merge options
- **GitLab**: Select "Squash commits when merge request is accepted"

This approach is simpler but less flexible than interactive rebase, as
you cannot selectively keep certain commits separate.

### Reset and recommit

For straightforward cases where you want to combine all changes into a
single commit, you can use reset:

```bash
# Ensure you're on your feature branch
git checkout feature-branch

# Soft reset to the point where your branch diverged from main
# This keeps all your changes but uncommits them
git reset --soft main

# Review your changes
git status

# Create a single, well-crafted commit
git commit -m "Add user authentication feature

Implement login and registration functionality with form validation,
session management, and comprehensive test coverage."
```

!!! warning "Important considerations"
    **Rewriting history on shared branches**: If you've already pushed
    your commits to a shared branch that others may have pulled, squashing
    requires a force push (`git push --force-with-lease`). This can
    disrupt collaborators. In team environments, only rewrite history on
    branches you own, or coordinate with your team before force pushing.

    **Backup before squashing**: Before squashing commits, consider
    creating a backup branch:

    ```bash
    git branch backup-feature-branch
    ```

    This allows you to recover if something goes wrong during the rebase.

## Example workflow

Here's a typical workflow incorporating commit squashing:

```bash
# Fetch the latest remote refs first:
git fetch origin

# Create and switch to a feature branch based on origin/main
git checkout -b feature/user-auth origin/main

# Make several commits as you work
git commit -m "WIP: Initial auth structure"
git commit -m "Add login form"
git commit -m "Fix validation bug"
git commit -m "Add tests"
git commit -m "Address PR feedback"

# Before merging, review your commit history
git log --oneline main..HEAD

# Squash all commits into one
git rebase -i origin/main

# In the editor, squash commits as appropriate
# Edit the commit message to be clear and comprehensive

# Push to remote (force push required after rebase)
git push --force-with-lease origin feature/user-auth

# Create pull request for review
# After approval, merge to main
```

## Additional resources

!!! info "Further reading and information"
    [Git Tools - Rewriting History (Official Git Documentation)](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History)

    [About pull request merges - GitHub Docs](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges)

    [Squash your commits - Git Tower](https://www.git-tower.com/learn/git/faq/git-squash)
