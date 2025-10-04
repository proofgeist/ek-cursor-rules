#!/usr/bin/env python3
"""
Sync Cursor rules (.mdc files) to Claude.md format

This script consolidates all .mdc cursor rules into a single Claude.md file
that can be used with Claude projects.

Usage:
    ./sync-to-claude.py [output_path]

    If output_path is not provided, creates Claude.md in the current directory.

Examples:
    ./sync-to-claude.py                          # Creates ./Claude.md
    ./sync-to-claude.py /path/to/project         # Creates /path/to/project/Claude.md
    ./sync-to-claude.py /path/to/custom.md       # Creates custom.md at specified path
"""

import os
import sys
import re
from pathlib import Path
from typing import List, Tuple
from datetime import datetime


def extract_frontmatter_and_content(file_path: Path) -> Tuple[str, str]:
    """Extract frontmatter metadata and actual content from .mdc file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove YAML frontmatter (between --- markers)
    # Handle multiple frontmatter blocks if present
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.MULTILINE | re.DOTALL)
    content = content.strip()

    return content


def get_rule_files(rules_dir: Path) -> List[Tuple[str, Path]]:
    """Get all .mdc files organized by directory"""
    rule_categories = []

    # Define the order of categories
    category_order = [
        '000-general-rules',
        '100-git-rules',
        '200-design-rules',
        '300-python-projects',
        '400-versioning-rules',
        '500-nodejs-projects',
        '600-database-rules'
    ]

    for category in category_order:
        category_path = rules_dir / category
        if not category_path.exists():
            continue

        mdc_files = sorted(category_path.glob('*.mdc'))
        for mdc_file in mdc_files:
            rule_categories.append((category, mdc_file))

    return rule_categories


def get_category_title(category_name: str) -> str:
    """Convert directory name to readable title"""
    category_map = {
        '000-general-rules': 'General Rules',
        '100-git-rules': 'Git & Version Control Rules',
        '200-design-rules': 'Design & UX Rules',
        '300-python-projects': 'Python Project Rules',
        '400-versioning-rules': 'Versioning & Release Rules',
        '500-nodejs-projects': 'Node.js Project Rules',
        '600-database-rules': 'Database Rules'
    }
    return category_map.get(category_name, category_name.replace('-', ' ').title())


def generate_claude_md(rules_dir: Path, output_path: Path) -> None:
    """Generate Claude.md from all cursor rules"""

    rule_files = get_rule_files(rules_dir)

    if not rule_files:
        print(f"❌ No .mdc files found in {rules_dir}")
        sys.exit(1)

    # Start building the Claude.md content
    lines = [
        "# AI Assistant Rules",
        "",
        f"*Generated from cursor rules on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*",
        "",
        "---",
        ""
    ]

    current_category = None

    for category, file_path in rule_files:
        # Add category header if new category
        if category != current_category:
            lines.append("")
            lines.append(f"# {get_category_title(category)}")
            lines.append("")
            current_category = category

        # Extract content and add to Claude.md
        content = extract_frontmatter_and_content(file_path)

        # Add a separator between files in same category
        lines.append(f"<!-- Source: {file_path.name} -->")
        lines.append("")
        lines.append(content)
        lines.append("")
        lines.append("---")
        lines.append("")

    # Add footer
    lines.extend([
        "",
        "---",
        "",
        "*This file is auto-generated from cursor rules. Do not edit directly.*",
        "*To update, modify the source .mdc files and run sync-to-claude.py*",
        ""
    ])

    # Write to output file
    output_content = "\n".join(lines)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output_content)

    print(f"✅ Successfully created {output_path}")
    print(f"📊 Consolidated {len(rule_files)} rule files")
    print(f"📝 Output size: {len(output_content)} characters")


def main():
    # Determine output path
    if len(sys.argv) > 1:
        output_arg = sys.argv[1]
        output_path = Path(output_arg).resolve()

        # If path is a directory, create Claude.md inside it
        if output_path.is_dir():
            output_path = output_path / "Claude.md"
        # If path doesn't have .md extension, add it
        elif not str(output_path).endswith('.md'):
            output_path = Path(str(output_path) + '.md')
    else:
        # Default to current directory
        output_path = Path.cwd() / "Claude.md"

    # Find rules directory (assume script is in project root)
    script_dir = Path(__file__).parent.resolve()
    rules_dir = script_dir / "rules"

    if not rules_dir.exists():
        print(f"❌ Rules directory not found: {rules_dir}")
        print("   Make sure you're running this script from the project root")
        sys.exit(1)

    print(f"📂 Reading rules from: {rules_dir}")
    print(f"📄 Output file: {output_path}")
    print("")

    generate_claude_md(rules_dir, output_path)


if __name__ == "__main__":
    main()
