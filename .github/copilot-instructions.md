# GitHub Copilot Instructions

> **⚠️ CRITICAL CONTEXT:** This is the DHCW Software Engineering Handbook for NHS Wales healthcare software engineering guidance. All changes must maintain the highest standards of accuracy, clarity, and professionalism. Healthcare guidance errors can have serious consequences.

## Project Overview

**Project:** DHCW Software Engineering Handbook  
**Organization:** GIG Cymru NHS Wales  
**Purpose:** Comprehensive software engineering guidance for healthcare software development  
**Published Site:** <https://gigcymru.github.io/dhcw-software-engineering-handbook/>  
**Repository:** <https://github.com/GIGCymru/dhcw-software-engineering-handbook/>

### Documentation Scope

This handbook provides comprehensive guidance covering:

- Software development standards and principles
- Source control best practices (Git workflows)
- Solution organization guidelines
- Coding standards (general, T-SQL)
- RESTful API standards (including FHIR)
- Azure DevOps usage
- Testing methodologies
- Security practices (OWASP Top 10)
- Accessibility standards

## Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Site Generator | [Zensical](https://zensical.org/) | Modern static site generator (successor to MkDocs Material) |
| Language | Python 3.13+ | Runtime environment |
| Package Manager | [uv](https://github.com/astral-sh/uv) | Fast Python package/environment management |
| Config File | `zensical.toml` | Site configuration, navigation, theme, plugins |
| Content Location | `/doc` directory | All markdown documentation |
| Linting | markdownlint-cli2 | Markdown quality assurance |
| Spell Checking | cspell | British English spell checking |
| CI/CD | GitHub Actions | Automated build and deployment |
| Hosting | GitHub Pages | Static site hosting |
| Command Runner | [Just](https://github.com/casey/just) | Project-specific commands |

## Quick Start

### Prerequisites

The repository includes multiple setup options:

1. **GitHub Codespaces** (Recommended) - Pre-configured environment via `.devcontainer.json`
2. **Local Development** - Requires Python 3.13+, uv, git, just, npm
3. **Container-based** - Using Podman/Docker with provided Dockerfile

### Common Commands

```bash
just --list    # View all available commands
just           # Full setup + build + serve (default workflow)
just build     # Build the documentation (clean build)
just run       # Start dev server at http://127.0.0.1:8000/
just lint      # Run markdown linting
just spell     # Run spell checking
```

The development server auto-reloads on file changes.

## Project Structure

```text
dhcw-software-engineering-handbook/
├── doc/                          # All documentation content (THIS IS WHERE CONTENT LIVES)
│   ├── index.md                  # Homepage
│   ├── <section-folders>/        # Major handbook sections
│   ├── assets/                   # Images, logos, favicons
│   ├── overrides/                # Theme customizations
│   └── stylesheets/              # Custom CSS
├── .github/                      # GitHub Actions workflows
│   ├── workflows/                # CI/CD workflows
│   └── copilot-instructions.md   # This file
├── .devcontainer.json            # Codespaces configuration
├── .markdownlint-cli2.jsonc      # Markdown linting rules
├── cspell.json                   # Spell checker dictionary (British English)
├── Dockerfile                    # Container image settings
├── justfile                      # Command automation
├── package.json                  # NPM dependencies (linting/spell check tools)
├── pyproject.toml                # Python project configuration
├── zensical.toml                 # Main site configuration
└── README.md                     # Project README
```

## Working with Documentation

### Critical Rules

1. **ALWAYS read files before editing** - Understand current content and structure
2. **All documentation lives in `/doc` directory** - Create new files here
3. **Update navigation** - When adding/removing pages, update `zensical.toml`
4. **Follow existing patterns** - Match formatting, structure, and style
5. **Test locally** - Start dev server to verify changes render correctly
6. **Security & PHI** - NEVER commit patient data (PHI), secrets, or credentials
7. **British English** - Follow NHS Wales language standards

### Standard Workflow

```text
Read file(s) → Make edits → Update navigation (if needed) → Test → Lint/Spell → Commit
```

### Documentation Updates

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

- **[Admonitions](https://zensical.org/docs/authoring/admonitions/)** - Callout boxes (tip, example, warning, info, note, etc.)
- **[Code Blocks](https://zensical.org/docs/authoring/code-blocks/)** - Syntax highlighting with line numbers and annotations
- **Footnotes** - Reference-style footnotes
- **Tables** - Standard markdown tables
- **Tabbed content** - Multi-tab content blocks
- **Mermaid diagrams** - Flowcharts, sequence diagrams, etc.

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

See `doc/software-development-handbook/introduction.md` for live examples.

### Adding New Pages

1. **Create markdown file** in appropriate `/doc` subdirectory
   - Follow naming: lowercase, hyphens for spaces (e.g., `my-new-page.md`)

2. **Update `zensical.toml` navigation:**

   ```toml
   nav = [
      {"Section Name" = [
         {"New Page Title" = "section-name/new-page.md"},
      ]},
   ]
   ```

3. **Test navigation** appears correctly in dev server

### Modifying Navigation

The `zensical.toml` file is organized into sections:

- **`[project]`** - Site metadata (name, description, URLs)
- **`nav`** - Navigation structure (update when adding/removing pages)
- **`[project.markdown_extensions.<..>]`** - Markdown extensions and settings
- **`[project.theme]`** - Theme configuration (logo, features, colors, fonts)

## Quality Assurance

### Pre-Commit Checklist

- [ ] Read files before editing to understand context
- [ ] Follow existing formatting and structure patterns
- [ ] Use correct relative paths for links and images
- [ ] Update `zensical.toml` navigation if adding/removing pages
- [ ] Verify markdown syntax is correct
- [ ] Run `just lint` and fix all issues
- [ ] Run `just spell` and fix all issues
- [ ] Check for secrets/credentials or PHI (DO NOT COMMIT)
- [ ] Test in dev server if possible

### Linting & Validation

**Markdown Linting** (`.markdownlint-cli2.jsonc`):

- Defines deviations from default markdown linting rules
- Lint all changed documents: `just lint`
- Fix all errors before committing

**Spell Checking** (`cspell.json`):

- Custom dictionary includes healthcare/tech terms
- Language: British English (en-GB)
- Check spelling: `just spell`
- Add new terms to the `words` array in `cspell.json` (alphabetically)

### Local Testing

```bash
just run
# Visit http://127.0.0.1:8000/
# Verify: pages load, navigation works, links resolve, images display
```

### Build Testing

```bash
just build
# Check terminal output for errors or warnings
```

## CI/CD Pipeline

GitHub Actions automatically runs on pull requests:

- **Quality Assurance** (`.github/workflows/pr-quality.yml`):
  - Validates markdown files
  - Checks spelling
  - Verifies internal links

- **Documentation** (`.github/workflows/publish.yml`):
  - Builds the site
  - Deploys to GitHub Pages (on main branch only)

- **Copilot Setup Steps** (`.github/workflows/copilot-setup-steps.yml`):
  - Installs dependencies for Copilot agents
  - Ensures environment is ready

Check workflow files in `.github/workflows/` for detailed configuration.

## Common Tasks

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

1. **Read the file first** to understand current content
2. **Make targeted edits** using precise changes
3. **Verify locally** via dev server if possible
4. **Lint and spell check** before committing
5. **Commit changes** with clear message explaining "why"

### Working with Images

- **Location:** All images go in `doc/assets/`
- **Naming:** Use descriptive, lowercase, hyphen-separated names (e.g., `api-workflow-diagram.png`)
- **References in markdown:** `![Descriptive alt text](../assets/image-name.png)`
- **Path notes:** Use relative paths; `../` navigates up one directory

### Adding Code Examples

**Syntax-highlighted code blocks:**

````markdown
```python
def calculate_risk_score(patient_data):
    """Calculate patient risk score for NHS Wales system."""
    return risk_score
```
````

**Supported languages:** python, typescript, javascript, sql, bash, yaml, toml, json, csharp, xml, and more.

### Adding Technical Terms to Spell Checker

If using NHS Wales or healthcare-specific terms:

1. Read `cspell.json`
2. Add term to the `words` array (alphabetically)
3. Commit with clear explanation

Example:

```json
"words": [
    "DHCW",
    "FHIR",
    "mynewterm",
    "WCAG"
]
```

## Troubleshooting

### Build/Server Issues

| Problem | Solution |
|---------|----------|
| Module not found | Run `just sync` to reinstall dependencies |
| Build fails | Check `zensical.toml` syntax; verify all referenced files exist |
| Page not appearing | Verify navigation entry in `zensical.toml` matches file path exactly |
| Broken links | Check relative paths; ensure target files exist |
| Images not loading | Verify path and that image is in `doc/assets/` |
| Markdown not rendering | Check for syntax errors; ensure proper code block fencing |
| Port 8000 in use | Stop existing server or use different port |

### Common Mistakes

- **Forgetting to update navigation** after adding/removing pages
- **Incorrect relative paths** in links (remember `../` to go up a directory)
- **Creating files outside `/doc`** directory
- **Not reading files before editing** (leads to incorrect assumptions)
- **Inconsistent formatting** (not matching existing style)
- **Using American English** instead of British English
- **Committing without testing** locally first

## Git Workflow

### Branch Strategy

- **Main branch:** `main`
- **Feature branches:** Use descriptive names (e.g., `feature/add-python-standards`, `fix/broken-links`, `docs/update-api-standards`)
- **Copilot branches:** Typically start with `copilot/`

### Commit Best Practices

**Commit message format:**

```text
Brief summary (50 chars or less)

- Detailed change 1 explaining why not just what
- Detailed change 2
- Reference issue/PR numbers if applicable
```

**Example good commit:**

```text
Add Python coding standards section

- Include PEP 8 compliance guidelines
- Add examples for common patterns
- Link to Azure DevOps pipeline configuration
- Fixes #123
```

### Standard Git Flow

```bash
git status                    # Verify changes
git diff                      # Review changes
git add [files]               # Stage specific files
git commit -m "message"       # Commit with clear message
git push -u origin [branch]   # Push to remote
```

## Best Practices for AI Agents

### Core Principles

1. **Read First, Edit Second**
   - Always read files before making changes
   - Understand context, structure, and existing patterns
   - Check related files for consistency

2. **Minimize File Creation**
   - Prefer editing existing files over creating new ones
   - Only create files when explicitly required
   - Do not create unnecessary documentation files proactively

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

### Common Pitfalls to Avoid

- ❌ Creating documentation files proactively (README.md, CONTRIBUTING.md, etc.)
- ❌ Making assumptions about file contents without reading them
- ❌ Adding features or improvements beyond what was requested
- ❌ Using placeholder values instead of reading actual content
- ❌ Batch committing multiple unrelated changes
- ❌ Over-engineering solutions or adding unnecessary complexity
- ❌ Ignoring existing conventions in favor of "better" approaches
- ❌ Using American English spelling instead of British English

### Pre-Commit Validation

Before committing, verify:

- [ ] Read all files you edited
- [ ] Changes match existing style and structure
- [ ] Navigation updated if pages added/removed
- [ ] Links use correct relative paths
- [ ] Images referenced are in `doc/assets/`
- [ ] Code blocks have language specifiers
- [ ] Ran `just lint` with no errors
- [ ] Ran `just spell` with no errors
- [ ] Tested in dev server if possible
- [ ] Commit message is clear and explains "why"
- [ ] Only relevant files are staged

## Security Best Practices

### NEVER Commit

- Patient data (PHI - Protected Health Information)
- API keys or access tokens
- Passwords or credentials
- Private keys or certificates
- Any sensitive NHS Wales data

### GitHub Actions Security

- Pin GitHub Actions to full-length commit SHAs instead of tags for supply-chain security
- Example: `actions/checkout@de0fac2e` instead of `actions/checkout@v6`
- Include version comments for maintainability

## Additional Resources

- **For detailed AI agent instructions:** See `AGENTS.md` in the repository root
- **For contributing guidelines:** See `CONTRIBUTING.md`
- **For code of conduct:** See `CODE_OF_CONDUCT.md`
- **Zensical documentation:** <https://zensical.org/>
- **Python Markdown:** <https://python-markdown.github.io/>
- **Just command runner:** <https://github.com/casey/just>

## Summary for Copilot Agents

**Key Takeaways:**

1. ⚕️ **Healthcare context matters** - This is NHS Wales software guidance; accuracy and professionalism are paramount
2. 📖 **Always read before editing** - Understanding context prevents errors
3. 🎯 **Follow existing patterns** - Consistency is critical in professional documentation
4. 📝 **Update navigation** - Keep `zensical.toml` in sync with content changes
5. ✅ **Test your changes** - Use dev server or build to verify before committing
6. 🔧 **Use proper commands** - `just` commands for building, linting, and testing
7. 💭 **Clear commits** - Explain "why" not just "what"
8. 🚫 **Avoid over-engineering** - Make only requested changes, keep it simple
9. 🔍 **British English** - Follow NHS Wales language standards (en-GB)
10. 🤝 **Respect the process** - This documentation helps real healthcare software developers

## Questions or Issues?

If you encounter issues or need clarification:

1. Check this document first
2. Review the `AGENTS.md` file for more detailed instructions
3. Look at existing documentation for patterns
4. Check workflow files in `.github/workflows/`
5. Contact the repository team via GitHub issues

Remember: Quality and accuracy are more important than speed when working with healthcare guidance documentation.
