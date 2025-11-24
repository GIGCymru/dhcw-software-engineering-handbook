# AI Agent Instructions

This document provides comprehensive instructions for AI agents (including Claude, GitHub Copilot, Cursor, and other AI assistants) working with the DHCW Software Engineering Handbook project.

## Project Overview

**Project Name:** DHCW Software Engineering Handbook
**Organization:** GIG Cymru NHS Wales
**Purpose:** Comprehensive software engineering guidance for healthcare software development
**Tech Stack:** Zensical (static site generator), Python 3.13+, uv package manager
**Site URL:** https://gigcymru.github.io/dhcw-software-engineering-handbook/
**Repository:** https://github.com/GIGCymru/dhcw-software-engineering-handbook/

## What This Project Contains

This is a comprehensive handbook covering:

- Software development standards and principles
- Source control best practices
- Solution organization guidelines
- Coding standards (general, T-SQL)
- RESTful API standards
- Azure DevOps handbook
- Testing methodologies
- Security practices
- Accessibility standards

## Technology Stack

- **Documentation Generator:** [Zensical](https://zensical.org/) - Modern static site generator
- **Language:** Python 3.13+
- **Package Manager:** [uv](https://github.com/astral-sh/uv) - Fast Python package manager
- **Configuration:** `zensical.toml` - Site configuration and navigation
- **Documentation Directory:** `/doc` - All markdown content
- **Build Output:** Static HTML/CSS/JS site

## Development Environment Setup

### Prerequisites Check

Before starting, verify these are available:

```bash
python --version  # Should be 3.13+
uv --version      # Should be installed
git --version     # Required for version control
```

### Initial Setup

1. **Clone the repository** (if not already cloned):

   ```bash
   git clone https://github.com/GIGCymru/dhcw-software-engineering-handbook.git
   cd dhcw-software-engineering-handbook
   ```

2. **Install dependencies:**

   ```bash
   uv sync
   ```

3. **Start the development server:**

   ```bash
   uv run zensical serve
   ```

4. **Access the site:**
   - Local: `http://127.0.0.1:8000/`
   - The server auto-reloads on file changes

## Project Structure

```
dhcw-software-engineering-handbook/
├── doc/                          # All documentation content
│   ├── index.md                  # Homepage
│   ├── software-development-handbook/
│   ├── using-source-control/
│   ├── organising-your-solution/
│   ├── general-coding-standards/
│   ├── t-sql-coding-standard/
│   ├── restful-api-standards/
│   ├── azure-devops-handbook/
│   ├── software-subscriptions/
│   ├── test-summary-report/
│   ├── testing-lost-updates/
│   ├── coding-standard-template/
│   ├── assets/                   # Images, logos, favicons
│   ├── overrides/                # Theme customizations
│   └── stylesheets/              # Custom CSS
├── .github/                      # GitHub Actions workflows
├── zensical.toml                 # Main configuration file
├── pyproject.toml                # Python project configuration
├── uv.lock                       # Dependency lock file
├── README.md                     # Project README
├── CONTRIBUTING.md               # Contribution guidelines
└── CODE_OF_CONDUCT.md           # Code of conduct
```

## Making Changes

### Documentation Updates

1. **Navigate to the appropriate directory:**

   ```bash
   cd doc/[section-name]/
   ```

2. **Edit markdown files:**
   - All content is in markdown (`.md`) files
   - Follow existing formatting conventions
   - Use GitHub-flavored markdown

3. **Preview changes:**
   - Development server auto-reloads
   - Check `http://127.0.0.1:8000/` for live preview

### Adding New Pages

1. **Create the markdown file** in the appropriate directory under `/doc`

2. **Update navigation** in `zensical.toml`:

   ```toml
   nav = [
     {"Section Name" = [
       {"New Page Title" = "section-name/new-page.md"},
     ]},
   ]
   ```

3. **Verify the page appears** in the navigation menu

### Modifying Site Configuration

Edit `zensical.toml` for:

- Site metadata (name, description, URL)
- Navigation structure
- Theme settings
- Markdown extensions
- Plugin configuration

## Git Workflow

### Branch Strategy

- **Main branch:** `main` (or as specified in current context)
- **Feature branches:** Create descriptive branches (e.g., `feature/add-python-standards`, `fix/broken-links`)
- **Work branch:** Use the branch specified in your session context

### Committing Changes

1. **Check status:**

   ```bash
   git status
   ```

2. **View changes:**

   ```bash
   git diff
   ```

3. **Stage changes:**

   ```bash
   git add [file-path]
   # Or stage all changes:
   git add .
   ```

4. **Commit with clear message:**

   ```bash
   git commit -m "Brief description of changes

   - Detailed point 1
   - Detailed point 2"
   ```

5. **Push to remote:**

   ```bash
   git push -u origin [branch-name]
   ```

### Commit Message Guidelines

- Use clear, descriptive messages
- Focus on "why" rather than "what"
- Follow existing commit message style in the repository
- Reference issue numbers if applicable

## Testing Your Changes

### Local Testing Checklist

- [ ] Development server runs without errors
- [ ] All pages load correctly
- [ ] Navigation links work
- [ ] Images and assets display properly
- [ ] Markdown renders correctly
- [ ] Code blocks have proper syntax highlighting
- [ ] Internal links resolve correctly
- [ ] No broken links

### Build Testing

```bash
# Full build (if Makefile is used)
make

# Or manually test build
uv run zensical build
```

## Common Tasks

### Adding a New Section

1. Create directory: `mkdir -p doc/new-section`
2. Add `introduction.md` file
3. Update `zensical.toml` navigation
4. Add additional pages as needed

### Updating Styling

1. Edit files in `doc/stylesheets/extra.css`
2. Or add theme overrides in `doc/overrides/`
3. Changes auto-reload in dev server

### Working with Images

1. Place images in `doc/assets/`
2. Reference in markdown:

   ```markdown
   ![Alt text](../assets/image-name.png)
   ```

### Adding Code Examples

Use fenced code blocks with language specification:

```markdown
```python
def example():
    return "Hello, World!"
```
```

## Troubleshooting

### Development Server Issues

- **Port already in use:** Stop other instances or use different port
- **Module not found:** Run `uv sync` to reinstall dependencies
- **Changes not reflecting:** Hard refresh browser (Ctrl+Shift+R)

### Build Errors

- Check `zensical.toml` syntax
- Verify all referenced files exist
- Ensure markdown is properly formatted
- Check for broken internal links

## Best Practices for AI Agents

1. **Always read before editing:** Use Read tool to understand current content
2. **Preserve formatting:** Match existing markdown style and structure
3. **Verify links:** Ensure all internal references are correct
4. **Test locally:** Start dev server to preview changes
5. **Clear commits:** Write descriptive commit messages
6. **Follow conventions:** Adhere to existing naming and structure patterns
7. **Check navigation:** Update `zensical.toml` when adding/removing pages
8. **Incremental changes:** Make focused, reviewable changes
9. **Documentation first:** If unclear, check existing documentation patterns
10. **Healthcare context:** Remember this is healthcare software guidance - accuracy and clarity are critical

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

For questions or support, contact: Joel Henderson at <joel.henderson@wales.nhs.uk>

## Additional Resources

- [Zensical Documentation](https://zensical.org/)
- [uv Documentation](https://github.com/astral-sh/uv)
- [GitHub Actions Workflows](.github/workflows/)
- [Published Site](https://gigcymru.github.io/dhcw-software-engineering-handbook/)

---

**Note for AI Agents:** This project contains critical healthcare software engineering guidance. Ensure all changes maintain accuracy, clarity, and professional standards appropriate for NHS Wales software development.
