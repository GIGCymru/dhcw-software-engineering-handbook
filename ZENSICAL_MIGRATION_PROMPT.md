# Zensical Migration Prompt

## Task Description

Migrate this repository from mkdocs-material to zensical (https://github.com/zensical/zensical) as the static site generator. Ensure the site builds successfully and resolve any errors and report on any warnings.

## Pre-Migration Checklist

Before starting the migration, identify and document the following from the existing mkdocs.yml:

1. **Custom Features to Preserve:**
   - [ ] Custom theme directories (custom_dir)
   - [ ] Custom CSS files (extra_css)
   - [ ] Custom JavaScript files (extra_javascript)
   - [ ] Theme overrides (especially analytics integrations in overrides/partials/)
   - [ ] Logo and favicon paths
   - [ ] Font configurations
   - [ ] Color schemes (palette settings)

2. **Navigation Structure:**
   - [ ] Document if navigation is auto-generated or explicit
   - [ ] Note any section groupings or hierarchy
   - [ ] Identify any external links in navigation

3. **Plugins in Use:**
   - [ ] List all plugins from mkdocs.yml
   - [ ] Check if they're actually used (search for their features in content)
   - [ ] Note: `table-reader`, `awesome-nav` may not be needed in zensical

4. **Markdown Extensions:**
   - [ ] List all markdown_extensions with their configurations
   - [ ] Document any custom fences (mermaid, etc.)
   - [ ] Note pymdownx extension settings

5. **Extra Configuration:**
   - [ ] Analytics providers and settings
   - [ ] Cookie consent configurations
   - [ ] Copyright notices (especially with HTML links)
   - [ ] Social links
   - [ ] Any other extra: section content

## Migration Steps

### 1. Install Zensical

```bash
uv add zensical
```

### 2. Create zensical.toml Configuration

Key points for configuration:

- **Basic Settings:** site_name, site_description, site_url, repo_url, docs_dir, edit_uri
- **Copyright:** Ensure HTML entities are properly escaped (use \" for quotes in TOML strings)
- **Navigation:** Convert YAML list format to TOML array of dicts
- **Theme:** Specify `variant = "classic"` to match Material for MkDocs appearance
- **Custom Directory:** Set `custom_dir = "doc/overrides"` (or appropriate path)
- **Features Array:** Must be at `[project.theme]` level, NOT nested under features table
- **Markdown Extensions:** Convert to array format, configure pymdownx settings under `[project.pymdownx]`

#### Known Configuration Gotchas:

1. **Cookie Consent Format:**
   ```toml
   # CORRECT:
   [project.extra.consent.cookies]
   analytics = {name = "Simple Analytics", checked = true}

   # INCORRECT (causes "AttributeError: 'list' object has no attribute 'items'"):
   [[project.extra.consent.cookies]]
   name = "analytics"
   checked = true
   ```

2. **Copyright with HTML:**
   ```toml
   copyright = "Copyright &copy; 2025 Org Name – <a href=\"#__consent\">Change cookie settings</a>"
   ```

3. **Features Configuration:**
   ```toml
   [project.theme]
   features = [
     "navigation.footer",
     "content.action.view",
     "content.code.copy",
   ]
   ```

### 3. Update Project Files

- **pyproject.toml:** Replace mkdocs packages with `zensical>=0.0.7`
- **README.md:** Update references from `mkdocs serve` to `zensical serve`
- **Makefile:** Update commands to use zensical instead of mkdocs
- **Dockerfile:** Update ENTRYPOINT to use zensical

### 4. Update Deployment Configuration

#### Makefile Deploy Target:

```makefile
.PHONY: deploy
deploy:
	uv run zensical build
	uv run ghp-import -n -p -f -m "Update documentation" site
	@echo "Documentation deployed"
```

**Important:** Zensical does NOT have a `gh-deploy` command. Use `ghp-import` which is included as a dependency.

#### GitHub Actions Workflow:

Follow the official zensical guidelines (not the mkdocs approach):

```yaml
name: Documentation

on:
  push:
    branches:
      - main

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - uses: actions/configure-pages@v5
      - uses: actions/checkout@v5
      - uses: actions/setup-python@v5
        with:
          python-version: 3.x
      - run: pip install zensical
      - run: zensical build --clean
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v4
        with:
          path: site
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

**Key Differences from mkdocs workflow:**
- Use `actions/configure-pages@v5` first
- Use `pip install zensical` (not uv - simpler for CI)
- Use `zensical build --clean`
- Use `actions/upload-pages-artifact@v4` and `actions/deploy-pages@v4`
- Set proper permissions: `contents: read`, `pages: write`, `id-token: write`
- Configure `github-pages` environment
- **Do NOT use caching** - zensical docs explicitly say "At the moment, we do not recommend using caches on CI systems"

### 5. Build and Test

```bash
# Clean build
rm -rf site
uv run zensical build

# Check for errors and warnings
# Verify output:
ls -la site/
du -sh site/
ls -lh site/search.json site/sitemap.xml

# Test locally
uv run zensical serve
```

### 6. Configuration Audit

After initial migration, compare against original mkdocs.yml:

- [ ] Verify all theme features are enabled
- [ ] Check copyright message includes all original content
- [ ] Confirm custom CSS/JS files are referenced
- [ ] Validate analytics integration works
- [ ] Test navigation structure matches original
- [ ] Verify custom overrides are loaded

### 7. Commit and Deploy

```bash
git add zensical.toml pyproject.toml uv.lock README.md Makefile Dockerfile .github/workflows/
git commit -m "Migrate from mkdocs-material to zensical"
git push
```

## Common Issues and Solutions

### Issue 1: "AttributeError: 'list' object has no attribute 'items'"
**Cause:** Cookie consent configuration using array syntax instead of dict
**Solution:** Use `[project.extra.consent.cookies]` with dict format, not `[[...]]`

### Issue 2: "No such command 'gh-deploy'"
**Cause:** Zensical doesn't have mkdocs's gh-deploy command
**Solution:** Use `ghp-import` directly (already included as dependency)

### Issue 3: Missing analytics template
**Cause:** Custom analytics integration in overrides not being loaded
**Solution:** Add `custom_dir = "doc/overrides"` to `[project.theme]` section

### Issue 4: Navigation footer not showing
**Cause:** Features configured incorrectly
**Solution:** Ensure `features = [...]` is directly under `[project.theme]`, not nested

### Issue 5: Branch push fails with 403
**Cause:** Git restrictions requiring specific branch naming patterns
**Solution:** Push to allowed branch pattern (e.g., `claude/gh_pages-<session-id>`)

## Verification Checklist

After migration is complete:

- [ ] Build completes with 0 errors
- [ ] Build completes with 0 warnings
- [ ] All pages generated (verify count matches original)
- [ ] search.json created
- [ ] sitemap.xml created
- [ ] Custom CSS applied correctly
- [ ] Navigation structure matches original
- [ ] Footer navigation visible
- [ ] Copyright notice displays correctly (including HTML links)
- [ ] Cookie consent appears
- [ ] Analytics integration works
- [ ] Logo and favicon display
- [ ] Theme colors match original
- [ ] Code blocks render with syntax highlighting
- [ ] Mermaid diagrams render (if used)
- [ ] Admonitions display correctly
- [ ] Tabbed content works (if used)

## Relevant Documentation Sources

### Zensical Official Documentation:
- Main Repository: https://github.com/zensical/zensical
- Get Started: https://zensical.org/docs/get-started/
- Create Your Site: https://zensical.org/docs/create-your-site/
- Basic Configuration: https://zensical.org/docs/setup/basics/
- Navigation Setup: https://zensical.org/docs/setup/navigation/
- Publishing/Deployment: https://zensical.org/docs/publish-your-site/
- Compatibility Guide: https://zensical.org/compatibility/

### Key Zensical Features:
- Customization: https://zensical.org/docs/customization/
- Logo and Icons: https://zensical.org/docs/setup/logo-and-icons/
- Footer Setup: https://zensical.org/docs/setup/footer/
- Analytics: https://zensical.org/docs/setup/analytics/

### Reference Documentation:
- ghp-import: https://github.com/c-w/ghp-import (for manual deployment)
- GitHub Actions configure-pages: https://github.com/actions/configure-pages
- GitHub Actions upload-pages-artifact: https://github.com/actions/upload-pages-artifact
- GitHub Actions deploy-pages: https://github.com/actions/deploy-pages

## Expected Outcome

Upon successful migration:
- Site builds in ~3-5 seconds
- All content, navigation, and styling preserved
- GitHub Actions workflow deploys automatically on merge to main
- Site accessible at `<username>.github.io/<repository>`
- No warnings or errors in build output

## Notes

- Zensical is built by the same team as Material for MkDocs
- Uses "classic" variant to maintain Material for MkDocs appearance
- Configuration format is TOML instead of YAML
- Some mkdocs plugins may not be needed (e.g., awesome-nav replaced by explicit nav structure)
- Zensical includes ghp-import as a dependency for deployment
- CI builds should use pip, not uv, for simplicity
- Do not use caching in CI per zensical recommendations
