# GIG Cymru NHS Wales - DHCW Software Engineering Handbook
# ==========================================================
#
# This justfile provides command automation for building and maintaining
# the DHCW Software Engineering Handbook documentation.
#
# Quick Start:
#   just --list          # Show all available commands
#   just                 # Run the complete workflow (install, sync, build, serve)
#   just run             # Start the development server quickly
#
# Common Workflows:
#   Development:  just run
#   Clean Build:  just build
#   Deploy:       just deploy

# Variables
local_url := "http://127.0.0.1:8000"
prod_url := "https://gigcymru.github.io/dhcw-software-engineering-handbook/"

# Default recipe - runs the complete development workflow
default: install sync build run

# Display this help message with all available commands
help:
    @just --list

# ============================================================
# Setup & Dependencies
# ============================================================

# Install uv package manager (required for Python dependency management)
# Run this first if you don't have uv installed on your system
install:
    @echo "📦 Installing uv package manager..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    @echo "✅ Installation complete! The 'uv' command is now available."
    @echo "💡 Next step: Run 'just sync' to install project dependencies"

# Synchronize and install all project dependencies
# This ensures your Python environment matches the project requirements
sync:
    @echo "🔄 Synchronizing project dependencies..."
    uv sync
    @echo "✅ Dependencies synchronized successfully!"
    @echo "💡 Your environment is now configured and ready to use"

# ============================================================
# Documentation Building & Serving
# ============================================================

# Build the documentation site from scratch (clean build)
# This removes any previous build artifacts and creates a fresh build
build:
    @echo "🏗️  Building documentation from clean slate..."
    uv run zensical build --clean
    @echo "✅ Documentation built successfully!"
    @echo "📂 Output location: ./site/"
    @echo "💡 Run 'just run' to preview the site locally"

# Start the local development server
# Access the documentation at {{ local_url }}
# The server will automatically reload when you make changes
run:
    @echo "🚀 Starting development server..."
    @echo "📄 Documentation will be available at: {{ local_url }}"
    @echo "💡 Press Ctrl+C to stop the server"
    @echo ""
    uv run zensical serve

# ============================================================
# Deployment
# ============================================================

# Build and deploy documentation to GitHub Pages
# This pushes the built site to the gh-pages branch
# Requires appropriate Git permissions
deploy:
    @echo "🏗️  Building documentation for deployment..."
    uv run zensical build
    @echo "🚀 Deploying to GitHub Pages..."
    uv run ghp-import -n -p -f -m "Update documentation" site
    @echo "✅ Deployment complete!"
    @echo "🌐 Documentation available at: {{ prod_url }}"
    @echo "💡 Note: It may take a few minutes for changes to appear"


# ============================================================================
# Quality Assurance
# ============================================================================

# Run markdown linter on all documentation files (requires npm install)
lint:
    @echo "🔍 Linting markdown files with markdownlint-cli2..."
    npx markdownlint-cli2 "doc/**/*.md" --config .markdownlint-cli2.jsonc
    @echo "✅ Markdown linting complete - no issues found!"
