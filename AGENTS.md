# AI Agent Instructions

This document provides comprehensive instructions for AI agents (including Claude, GitHub Copilot, Cursor, and other AI assistants) working with the DHCW Software Engineering Handbook project.

> **⚠️ CRITICAL CONTEXT:** This is NHS Wales healthcare software engineering guidance. All changes must maintain the highest standards of accuracy, clarity, and professionalism. Healthcare guidance errors can have serious consequences.

## Project Overview

**Project:** DHCW Software Engineering Handbook
**Organization:** GIG Cymru NHS Wales
**Purpose:** Comprehensive software engineering guidance for healthcare software development
**Published Site:** https://gigcymru.github.io/dhcw-software-engineering-handbook/
**Repository:** https://github.com/GIGCymru/dhcw-software-engineering-handbook/

### Documentation Scope

Comprehensive handbook covering:

- Software development standards and principles
- Source control best practices (Git workflows)
- Solution organization guidelines
- Coding standards (general, T-SQL)
- RESTful API standards (including FHIR)
- Using Azure DevOps
- Testing methodologies
- Security practices (e.g. OWASP Top 10)
- Accessibility standards

## Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Site Generator | [Zensical](https://zensical.org/) | Modern static site generator (successor to MkDocs Material) |
| Language | Python 3.13+ | Runtime environment |
| Package Manager | [uv](https://github.com/astral-sh/uv) | Fast Python package/environment management |
| Config File | `zensical.toml` | Site configuration, navigation, theme, plugins |
| Content Location | `/doc` directory | All markdown documentation |
| Linting | markdownlint + cspell | Quality assurance |
| CI/CD | GitHub Actions | Automated build and deployment |
| Hosting | GitHub Pages | Static site hosting |
| Command Runner | [Just](https://github.com/casey/just) | run project-specific commands. |

## Development Environment Setup

### Standard Setup

The repository includes multiple setup options:

1. **GitHub Codespaces** - Pre-configured environment via `.devcontainer.json`
2. **Local Development** - Requires Python 3.13+, uv, git, just, npm
3. **Container-based** - Using Podman/Docker with provided Dockerfile

### Quick Start

```bash
just --list    # View all available commands
just           # Full setup + build + serve
just build     # Perform a build of the documentation
just run       # Start the dev server (http://127.0.0.1:8000/)
```

The development server auto-reloads on file changes.

## Project Structure

```
dhcw-software-engineering-handbook/
├── doc/                          # All documentation content
│   ├── index.md                  # Homepage
│   ├── <subfolders>/             # Major handbook sections under subfolders
│   ├── assets/                   # Images, logos, favicons
│   ├── overrides/                # Theme customizations
│   └── stylesheets/              # Custom CSS
├── .github/                      # GitHub Actions workflows
├── .devcontainer.json            # Devcontainer configuration
├── .markdownlint-cli2.jsonc      # Markdown Linting rules configuration
├── cspell.json                   # Spell checker dictionary
├── Dockerfile                    # Docker image settings
├── justfile                      # Command automation and workflows
├── package.json                  # NPM project configuration
├── pyproject.toml                # Python project configuration
├── README.md                     # Project README
├── zensical.toml                 # Main configuration file
```

## Workflow for AI Agents

### Critical Rules

1. **ALWAYS read files before editing** - Use Read tool to understand current content and structure
2. **NEVER create unnecessary files** - Prefer editing existing files over creating new ones
3. **Verify navigation changes** - When adding/removing pages, update `zensical.toml`
4. **Follow existing patterns** - Match formatting, structure, and style of existing content
5. **Test locally if possible** - Start dev server to verify changes render correctly
6. **NEVER commit PII or secrets to source control**

### Standard Change Workflow

```
Read file(s) → Make edits → Update navigation (if needed) → Test → Commit → Push
```

### Documentation Updates

**All documentation lives in `/doc` directory as markdown files.**

**Before editing:**

- Read the target file to understand current content
- Check related files for context and patterns
- Review existing formatting and structure

**When editing:**

- Use [Python Markdown](https://zensical.org/docs/authoring/markdown/) with Zensical extensions
- Follow existing heading hierarchy
- Maintain consistent formatting
- Use relative paths for internal links: `[Link text](../section/page.md)`
- Place images in `doc/assets/` and reference: `![Alt text](../assets/image.png)`

**Key Markdown Extensions Available:**

- **[Admonitions](https://zensical.org/docs/authoring/admonitions/)** - Callout boxes for notes, warnings, tips, etc.
- **[Code Blocks](https://zensical.org/docs/authoring/code-blocks/)** - Syntax highlighting with line numbers and annotations
- **Footnotes** - Reference-style footnotes
- **Tables** - Standard markdown tables
- **Tabbed content** - Multi-tab content blocks
- **Mermaid diagrams** - Flowcharts, sequence diagrams, etc.

See the `[project.markdown_extensions.<title>]` sections in `zensical.toml` for the complete list of enabled extensions.

### Adding New Pages

1. **Create markdown file** in appropriate `/doc` subdirectory
2. **Update `zensical.toml` navigation:**

```toml
nav = [
   {"Section Name" = [
      {"New Page Title" = "section-name/new-page.md"},
   ]},
]
```

3. **Follow naming conventions:** lowercase, hyphens for spaces (e.g., `my-new-page.md`)

### Modifying Navigation

The `zensical.toml` file is organized into sections:

- **`[project]`** - Site metadata (name, description, URLs, navigation)
- **`nav`** - Navigation structure (primary area for updates when adding/removing pages)
- **`[project.markdown_extensions.<..>]`** - Markdown extensions and their settings
- **`[project.theme]`** - Theme configuration (logo, features, colors, fonts)

## Git Workflow

### Branch Strategy

- **Main branch:** `main`
- **Feature branches:** Use descriptive names (e.g., `feature/add-python-standards`, `fix/broken-links`, `docs/update-api-standards`)
- **Session branch:** Always use the branch specified in your session context (typically starts with `claude/`)

### Commit and Push

**Standard flow:**

```bash
git status                              # Verify changes
git diff                                # Review changes
git add [files]                         # Stage specific files (or use . for all)
git commit -m "Brief summary

- Detailed change 1
- Detailed change 2"                    # Clear, descriptive commit message
git push -u origin [branch-name]        # Push to remote
```

**Commit message best practices:**

- First line: Brief summary (50 chars or less)
- Blank line
- Bullet points explaining "why" not just "what"
- Reference issue/PR numbers if applicable
- Follow existing repository style (check `git log`)

**Example good commit:**

```
Add Python coding standards section

- Include PEP 8 compliance guidelines
- Add examples for common patterns
- Link to Azure DevOps pipeline configuration
```

## Quality Assurance & Testing

### Pre-Commit Checklist

- [ ] Read files before editing to understand context
- [ ] Follow existing formatting and structure patterns
- [ ] Use correct relative paths for links and images
- [ ] Update `zensical.toml` navigation if adding/removing pages
- [ ] Verify markdown syntax is correct
- [ ] Run markdownlint via `just lint` and fix all issues
- [ ] Run cspell via `just spell` and fix all issues
- [ ] Check spelling, especially technical terms
- [ ] Check for secrets or PII (DO NOT COMMIT THEM TO GIT)

### Linting & Validation

The project uses automated quality checks:

**Markdown Linting** (`.markdownlint-cli2.jsonc`)

- Defines deviations from default markdown linting rules
- Lint all changed documents using `just lint`

**Spell Checking** (`cspell.json`):

- Custom dictionary includes healthcare/tech terms.
- Language: British English (en-GB)
- Add new terms to the `words` or `ignoreWords` arrays as needed
- Check spelling in all docs with `just spell`

### Local Testing

**Development server test:**

```bash
just run
# Visit http://127.0.0.1:8000/
# Verify: pages load, navigation works, links resolve, images display
```

**Build test:**

```bash
just build
# Check terminal output for errors or warnings
```

### CI/CD Pipeline

GitHub Actions automatically:

- Validates markdown
- Checks spelling
- Builds the site
- Deploys to GitHub Pages (on main branch)

Check `.github/workflows/` for pipeline configuration.

## Common Tasks Reference

### Adding a New Documentation Section

1. Create directory: `mkdir -p doc/new-section-name`
2. Create `introduction.md` as the section landing page
3. Add section to `zensical.toml` navigation array
4. Create additional pages as needed
5. Test navigation appears correctly

**Example navigation entry:**

```toml
{"New Section Name" = [
  {"Introduction" = "new-section-name/introduction.md"},
  {"Topic One" = "new-section-name/topic-one.md"},
]},
```

### Updating Existing Content

1. **Read the file first:** `Read /home/user/dhcw-software-engineering-handbook/doc/section/page.md`
2. **Make targeted edits:** Use Edit tool for precise changes
3. **Verify locally:** Check dev server if possible
4. **Commit changes:** Clear message explaining why

### Working with Images

**Location:** All images go in `doc/assets/`

**Naming:** Use descriptive, lowercase, hyphen-separated names (e.g., `api-workflow-diagram.png`)

**References in markdown:**

```markdown
![Descriptive alt text](../assets/image-name.png)
```

**Path notes:** Use relative paths; `../ ` navigates up one directory from current page location.

### Adding Code Examples

**Syntax-highlighted code blocks** ([Zensical Code Blocks](https://zensical.org/docs/authoring/code-blocks/)):

````markdown
```python
def calculate_risk_score(patient_data):
    """Calculate patient risk score for NHS Wales system."""
    return risk_score
```
````

**Supported languages:** python, typescript, javascript, sql, bash, yaml, toml, json, csharp, xml, and more.

**Code blocks support:**
- Syntax highlighting
- Line numbers (configurable)
- Line highlighting
- Annotations
- Copy button

### Using Admonitions

**Admonitions** ([Zensical Admonitions](https://zensical.org/docs/authoring/admonitions/)) create callout boxes for important information.

**Standard admonitions used in this handbook:**

```markdown
!!! tip "Practical tips"
    Use this for practical tips and recommendations

!!! example "Examples of good practice"
    Use this for examples of good practice

!!! warning "Practices to avoid"
    Use this for practices to avoid

!!! info "Further reading and information"
    Use this for links to further guides, information and work instructions
```

**Other available types:** note, abstract, success, question, failure, danger, bug, quote

See `doc/software-development-handbook/introduction.md` for live examples of these admonitions in use.

### Adding Technical Terms to Spell Checker

If using NHS Wales or healthcare-specific terms:

1. Read `cspell.json`
2. Add term to the `words` array (alphabetically)
3. Commit with clear explanation

## Troubleshooting

### Build/Server Issues

| Problem | Solution |
|---------|----------|
| Module not found | Run `just install` to reinstall dependencies |
| Build fails | Check `zensical.toml` syntax; verify all referenced files exist |
| Page not appearing | Verify navigation entry in `zensical.toml` and file path match |
| Broken links | Check relative paths; ensure target files exist |
| Images not loading | Verify path and that image is in `doc/assets/` |
| Markdown not rendering | Check for syntax errors; ensure proper fencing for code blocks |

### Common Mistakes

- **Forgetting to update navigation** after adding/removing pages
- **Incorrect relative paths** in links (remember `../` to go up a directory)
- **Creating files outside `/doc`** directory
- **Not reading files before editing** (leads to incorrect assumptions)
- **Inconsistent formatting** (not matching existing style)

## Best Practices for AI Agents

### 🎯 Core Principles

1. **Read First, Edit Second**
   - Always use Read tool before making changes
   - Understand context, structure, and existing patterns
   - Check related files for consistency

2. **Minimize File Creation**
   - Prefer editing existing files over creating new ones
   - Only create files when explicitly required
   - Never create README files unless specifically requested

3. **Follow Existing Patterns**
   - Match heading styles, formatting, and structure
   - Use similar language and tone
   - Check multiple examples before implementing

4. **Verify Navigation**
   - Update `zensical.toml` when adding/removing pages
   - Test that navigation appears correctly
   - Ensure paths match exactly (case-sensitive)

5. **Healthcare Context Awareness**
   - This is NHS Wales guidance - accuracy is critical
   - Healthcare software errors can have serious consequences
   - Maintain professional, clear, precise language
   - Double-check medical/technical terminology

### 🛠️ Tool Usage Guidelines

**For file operations:**

- **Read tool:** For viewing file contents (NOT cat/head/tail)
- **Edit tool:** For targeted changes to existing files (NOT sed/awk)
- **Write tool:** Only for new files when necessary (NOT echo/cat with heredoc)
- **Grep tool:** For searching content (NOT bash grep/rg)
- **Glob tool:** For finding files by pattern (NOT bash find)

**For git operations:**

- Use Bash tool for git commands
- Always check `git status` and `git diff` before committing
- Use heredoc format for multi-line commit messages
- Push with `-u origin [branch]` format

**Parallel operations:**

- Run independent Read operations in parallel
- Run independent Grep/Glob searches in parallel
- Stage, commit, and push sequentially (they depend on each other)

### 📋 Pre-Commit Validation

Before committing, verify:

- [ ] Read all files you edited
- [ ] Changes match existing style and structure
- [ ] Navigation updated if pages added/removed
- [ ] Links use correct relative paths
- [ ] Images referenced are in `doc/assets/`
- [ ] Code blocks have language specifiers
- [ ] Commit message is clear and explains "why"
- [ ] Only relevant files are staged (check `git status`)

### ⚠️ Common AI Agent Pitfalls

**Avoid these common mistakes:**

- ❌ Creating documentation files proactively (README.md, CONTRIBUTING.md, etc.)
- ❌ Using bash commands for file operations instead of dedicated tools
- ❌ Making assumptions about file contents without reading them
- ❌ Adding features or improvements beyond what was requested
- ❌ Creating abstractions or helpers for one-time operations
- ❌ Using placeholder values instead of reading actual content
- ❌ Batch committing multiple unrelated changes
- ❌ Over-engineering solutions or adding unnecessary complexity
- ❌ Ignoring existing conventions in favor of "better" approaches

## Creating Pull Requests

When your changes are complete and pushed:

1. **Verify your changes are pushed:**

   ```bash
   git status  # Should show "Your branch is up to date with 'origin/[branch]'"
   ```

2. **Review your changes:**

   ```bash
   git log origin/main..HEAD    # See commits that will be in PR
   git diff origin/main..HEAD   # See all changes vs main
   ```

3. **Create PR:**
   - GitHub will show a "Compare & pull request" button after pushing
   - Or use the URL provided in the push output
   - Write clear PR title and description
   - Explain what changed and why
   - Reference any related issues

4. **PR description should include:**
   - Summary of changes
   - Why the changes were made
   - What sections/pages were affected
   - Any testing performed

## Summary for AI Agents

**Key Takeaways:**

1. ⚕️ **Healthcare context matters** - This is NHS Wales software guidance; accuracy and professionalism are paramount
2. 📖 **Always read before editing** - Understanding context prevents errors
3. 🎯 **Follow existing patterns** - Consistency is critical in professional documentation
4. 📝 **Update navigation** - Keep `zensical.toml` in sync with content changes
5. ✅ **Test your changes** - Use dev server or build to verify before committing
6. 🔧 **Use proper tools** - Read/Edit/Write tools, not bash commands for file operations
7. 💭 **Clear commits** - Explain "why" not just "what"
8. 🚫 **Avoid over-engineering** - Make only requested changes, keep it simple
9. 🔍 **British English** - Follow NHS Wales language standards
10. 🤝 **Respect the process** - This documentation helps real healthcare software developers
