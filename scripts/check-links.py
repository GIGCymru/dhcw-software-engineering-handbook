#!/usr/bin/env python3
"""Check for broken internal markdown links in the documentation."""

import argparse
import os
import re
import sys
from pathlib import Path

def check_links(search_path: Path, verbose: bool = False) -> int:
    """
    Scan for broken internal markdown links.
    
    Args:
        search_path: The directory or file to search for markdown files.
        verbose: Whether to output details about every link checked.
        
    Returns:
        int: 0 if all links are valid, 1 if broken links are found.
    """
    md_files = []
    
    if search_path.is_file():
        if search_path.suffix == '.md':
            md_files.append(search_path)
    else:
        # Common large directories to skip during traversal to improve performance
        ignore_dirs = {"node_modules", "vendor", "dist", "build"}
        for root, dirs, files in os.walk(search_path):
            # Ignore hidden directories like .git or .venv and known large dependency/build folders
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ignore_dirs]
            for file in files:
                if file.endswith('.md'):
                    md_files.append(Path(root) / file)

    if not md_files:
        print(f"ℹ️ No markdown files found in {search_path}")
        return 0

    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    code_block_pattern = re.compile(r'```.*?```', re.DOTALL)
    errors = []

    print(f"🔍 Checking internal links in {len(md_files)} file(s) under {search_path}...")

    for md_file in md_files:
        try:
            content = md_file.read_text(encoding='utf-8')
        except Exception as e:
            print(f"❌ Error reading {md_file}: {e}", file=sys.stderr)
            continue
        
        # Remove code blocks before searching for links to avoid false positives in examples
        content_no_code = code_block_pattern.sub('', content)
        
        links = link_pattern.findall(content_no_code)
        
        for text, link in links:
            # Skip external links
            if any(link.startswith(s) for s in ['http://', 'https://', 'mailto:', 'tel:']):
                if verbose:
                    print(f"⏭️  Ignored external link in {md_file}: {link}")
                continue
            
            # Remove anchors (e.g., #section-name)
            link_path = link.split('#')[0]
            if not link_path:
                if verbose:
                    print(f"⏭️  Ignored anchor-only link in {md_file}: {link}")
                continue
            
            # Resolve relative path
            # target_path is relative to the directory containing the markdown file
            target_path = (md_file.parent / link_path).resolve()
            
            # Check if target exists
            target_exists = target_path.exists()

            if not target_exists and link_path.startswith('/'):
                # If it looks like an absolute path from the repo root
                repo_root = Path.cwd()
                target_path = (repo_root / link_path.lstrip('/')).resolve()
                target_exists = target_path.exists()
            
            if target_exists:
                if verbose:
                    print(f"✅ Found valid link in {md_file}: '{text}' -> {target_path}")
            else:
                errors.append(f"{md_file}: Broken link '[{text}]({link})'")

    if errors:
        print(f"❌ Found {len(errors)} broken link(s):")
        for error in errors:
            print(f"  - {error}")
        return 1
    else:
        print("✅ All internal links resolved successfully!")
        return 0

def main():
    parser = argparse.ArgumentParser(description="Check for broken internal links in markdown files.")
    parser.add_argument(
        "path", 
        type=Path, 
        nargs='?', 
        default=Path("doc"), 
        help="The directory or file to check (default: doc)"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output showing all checked links"
    )
    args = parser.parse_args()

    if not args.path.exists():
        print(f"❌ Error: Path '{args.path}' does not exist.", file=sys.stderr)
        return 1

    return check_links(args.path, verbose=args.verbose)

if __name__ == "__main__":
    sys.exit(main())