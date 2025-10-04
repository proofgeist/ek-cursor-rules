#!/usr/bin/env python3
"""
Sync Cursor rules (.mdc files) to CLAUDE.md format

This script consolidates .mdc cursor rules into a single CLAUDE.md file
that can be used with Claude projects.

Usage:
    ./sync-to-claude.py [--all] [output_path]

    If output_path is not provided, creates CLAUDE.md in the current directory.
    By default, only includes core rules for a lightweight file.

Options:
    --all    Include all rule categories (creates larger file)

Examples:
    ./sync-to-claude.py                          # Creates lightweight ./CLAUDE.md
    ./sync-to-claude.py --all                    # Creates full ./CLAUDE.md with all rules
    ./sync-to-claude.py /path/to/project         # Creates /path/to/project/CLAUDE.md
    ./sync-to-claude.py --all /path/to/custom.md # Creates full custom.md at specified path
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


def get_rule_files(rules_dir: Path, include_all: bool = False) -> List[Tuple[str, Path]]:
    """Get all .mdc files organized by directory"""
    rule_categories = []

    # Define the order of categories
    if include_all:
        category_order = [
            '000-general-rules',
            '100-git-rules',
            '200-design-rules',
            '300-python-projects',
            '400-versioning-rules',
            '500-nodejs-projects',
            '600-database-rules'
        ]
    else:
        # Lightweight version - only essential rules
        category_order = [
            '000-general-rules',  # Core directives only
            '100-git-rules',      # Basic git practices
        ]
        
        # Define essential files within each category for lightweight mode
        essential_files = {
            '000-general-rules': [
                '001-core-directive.mdc',
                '002-pre-work-analysis.mdc', 
                '003-during-work-tracking.mdc',
                '004-post-work-updates.mdc',
                '005-plan-format-standards.mdc'
            ],
            '100-git-rules': [
                '101-using-git'
            ]
        }

    for category in category_order:
        category_path = rules_dir / category
        if not category_path.exists():
            continue

        if include_all:
            mdc_files = sorted(category_path.glob('*.mdc'))
        else:
            # Only include essential files in lightweight mode
            essential_list = essential_files.get(category, [])
            mdc_files = [category_path / f for f in essential_list if (category_path / f).exists()]
            
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


def generate_claude_md(rules_dir: Path, output_path: Path, include_all: bool = False) -> None:
    """Generate Claude.md from all cursor rules"""

    rule_files = get_rule_files(rules_dir, include_all)

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
    # Parse command line arguments
    include_all = '--all' in sys.argv
    if include_all:
        sys.argv.remove('--all')
    
    # Determine output path
    if len(sys.argv) > 1:
        output_arg = sys.argv[1]
        output_path = Path(output_arg).resolve()

        # If path is a directory, create CLAUDE.md inside it
        if output_path.is_dir():
            output_path = output_path / "CLAUDE.md"
        # If path doesn't have .md extension, add it
        elif not str(output_path).endswith('.md'):
            output_path = Path(str(output_path) + '.md')
    else:
        # Default to current directory
        output_path = Path.cwd() / "CLAUDE.md"

    # Find rules directory (assume script is in project root)
    script_dir = Path(__file__).parent.resolve()
    rules_dir = script_dir / "rules"

    if not rules_dir.exists():
        print(f"❌ Rules directory not found: {rules_dir}")
        print("   Make sure you're running this script from the project root")
        sys.exit(1)

    print(f"📂 Reading rules from: {rules_dir}")
    print(f"📄 Output file: {output_path}")
    print(f"🔧 Mode: {'All rules' if include_all else 'Lightweight (core rules only)'}")
    print("")

    generate_claude_md(rules_dir, output_path, include_all)


if __name__ == "__main__":
    main()
