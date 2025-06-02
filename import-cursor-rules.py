#!/usr/bin/env python3

"""
Cursor Rules Import Script
Imports cursor rules into a new project with various options.
"""

import argparse
import os
import shutil
import sys
from pathlib import Path
from typing import List, Optional


class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    NC = '\033[0m'  # No Color


def print_colored(message: str, color: str = Colors.NC):
    """Print a colored message."""
    print(f"{color}{message}{Colors.NC}")


def create_symlink(source: Path, target: Path):
    """Create a symlink, handling cross-platform differences."""
    try:
        target.symlink_to(source.resolve())
    except OSError as e:
        print_colored(f"Warning: Could not create symlink {target}: {e}", Colors.YELLOW)
        # Fall back to copying if symlinks aren't supported
        shutil.copy2(source, target)


def create_hardlink(source: Path, target: Path):
    """Create a hardlink."""
    try:
        target.hardlink_to(source)
    except OSError as e:
        print_colored(f"Warning: Could not create hardlink {target}: {e}", Colors.YELLOW)
        # Fall back to copying if hardlinks aren't supported
        shutil.copy2(source, target)


def import_rule_set(rule_set: str, rules_source: Path, cursor_dir: Path, link_type: str, force: bool = False):
    """Import a specific rule set."""
    source_dir = rules_source / rule_set
    target_subdir = cursor_dir / "rules" / rule_set
    
    if not source_dir.is_dir():
        print_colored(f"Warning: Rule set '{rule_set}' not found, skipping...", Colors.YELLOW)
        return
    
    print_colored(f"Importing {rule_set} rules...", Colors.GREEN)
    target_subdir.mkdir(parents=True, exist_ok=True)
    
    # Import files based on link type
    for source_file in source_dir.rglob('*'):
        if source_file.is_file():
            # Calculate relative path to maintain structure
            rel_path = source_file.relative_to(source_dir)
            target_file = target_subdir / rel_path
            
            # Ensure parent directory exists
            target_file.parent.mkdir(parents=True, exist_ok=True)
            
            # Check if file exists and handle accordingly
            if target_file.exists() and not force:
                print(f"  Skipped (exists): {rel_path}")
                continue
            
            # Remove existing file if force is enabled
            if target_file.exists() and force:
                target_file.unlink()
            
            # Create the link/copy based on type
            try:
                if link_type == "copy":
                    shutil.copy2(source_file, target_file)
                    print(f"  Copied: {rel_path}")
                elif link_type == "symlink":
                    create_symlink(source_file, target_file)
                    print(f"  Symlinked: {rel_path}")
                elif link_type == "hardlink":
                    create_hardlink(source_file, target_file)
                    print(f"  Hardlinked: {rel_path}")
            except Exception as e:
                print_colored(f"  Error processing {rel_path}: {e}", Colors.YELLOW)


def main():
    parser = argparse.ArgumentParser(
        description="Import cursor rules into a new project",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Link Types:
  copy        Independent copies (safe for modification)
  symlink     File-level symlinks (updates with source changes)
  hardlink    File-level hardlinks (shared file data, updates with source)
  dirsymlink  Directory-level symlink to entire rules folder (most efficient)

Examples:
  %(prog)s /path/to/my-project                        # Copy all rules
  %(prog)s -l dirsymlink /path/to/my-project          # Symlink entire rules directory
  %(prog)s -l hardlink /path/to/my-project            # Hardlink all files
  %(prog)s -r general,git /path/to/my-project         # Only general and git rules
  %(prog)s -r python -f /path/to/python-project      # Python rules, force overwrite
        """
    )
    
    parser.add_argument(
        "target_directory",
        help="Target directory to import rules into"
    )
    
    parser.add_argument(
        "-l", "--link-type",
        choices=["copy", "symlink", "hardlink", "dirsymlink"],
        default="copy",
        help="How to import rules (default: copy)"
    )
    
    parser.add_argument(
        "-r", "--rules",
        default="all",
        help="Which rule sets: all, general, python, git, or comma-separated (default: all)"
    )
    
    parser.add_argument(
        "-f", "--force",
        action="store_true",
        help="Overwrite existing .cursor directory"
    )
    
    args = parser.parse_args()
    
    # Determine script directory and rules source
    script_dir = Path(__file__).parent.resolve()
    rules_source = script_dir / "rules"
    
    # Validate source rules exist
    if not rules_source.is_dir():
        print_colored(f"Error: Rules directory not found at {rules_source}", Colors.RED)
        sys.exit(1)
    
    # Set up target directory
    target_dir = Path(args.target_directory).resolve()
    
    # Create target directory if it doesn't exist
    if not target_dir.exists():
        print_colored(f"Target directory doesn't exist. Creating: {target_dir}", Colors.YELLOW)
        target_dir.mkdir(parents=True)
    
    # Check if .cursor already exists
    cursor_dir = target_dir / ".cursor"
    if cursor_dir.exists() and not args.force:
        print_colored(f"Warning: .cursor directory already exists in {target_dir}", Colors.YELLOW)
        print_colored("Will skip existing files. Use --force to overwrite everything.", Colors.YELLOW)

    # Remove existing .cursor if force is enabled
    if cursor_dir.exists() and args.force:
        print_colored("Removing existing .cursor directory...", Colors.YELLOW)
        shutil.rmtree(cursor_dir)

    # Handle directory-level symlink (special case)
    if args.link_type == "dirsymlink":
        print_colored("Creating directory-level symlink to entire rules folder...", Colors.BLUE)
        cursor_dir.mkdir(parents=True, exist_ok=True)
        rules_link = cursor_dir / "rules"
        
        # Check if rules symlink already exists
        if rules_link.is_symlink() and not args.force:
            print_colored("Rules symlink already exists, skipping...", Colors.YELLOW)
        elif rules_link.is_dir() and not args.force:
            print_colored("Rules directory already exists, skipping symlink creation...", Colors.YELLOW)
        else:
            try:
                if rules_link.exists() and args.force:
                    if rules_link.is_dir():
                        shutil.rmtree(rules_link)
                    else:
                        rules_link.unlink()
                rules_link.symlink_to(rules_source.resolve())
                print_colored("Directory symlink created successfully", Colors.GREEN)
            except OSError as e:
                print_colored(f"Error: Could not create directory symlink: {e}", Colors.RED)
                print_colored("Falling back to copy mode...", Colors.YELLOW)
                args.link_type = "copy"
            else:
                # Create .cursorignore file
                cursorignore_file = target_dir / ".cursorignore"
                if not cursorignore_file.exists():
                    print_colored("Creating .cursorignore file...", Colors.BLUE)
                    with open(cursorignore_file, "w") as f:
                        f.write("# Cursor rules directory (symlinked to source)\n")
                        f.write(".cursor/\n\n")
                else:
                    print_colored(".cursorignore already exists, skipping...", Colors.YELLOW)
                
                # Success message
                print()
                print_colored(f"✅ Cursor rules processing completed for {target_dir}", Colors.GREEN)
                print_colored("Link type: directory symlink", Colors.BLUE)
                print_colored("All rule sets included via directory link", Colors.BLUE)
                print()
                print_colored("Next steps:", Colors.YELLOW)
                print(f"1. Navigate to your project: cd {target_dir}")
                print("2. Open the project in Cursor")
                print("3. The rules will be automatically applied")
                print()
                print_colored("Note: Directory symlink means ALL changes to source rules will affect this project", Colors.YELLOW)
                return

    # Create .cursor directory for file-level operations
    print_colored(f"Creating .cursor directory in {target_dir}", Colors.BLUE)
    cursor_dir.mkdir(parents=True, exist_ok=True)
    rules_dir = cursor_dir / "rules"
    rules_dir.mkdir(exist_ok=True)
    
    # Determine which rule sets to import
    if args.rules == "all":
        # Import all available rule sets
        rule_sets = [d.name for d in rules_source.iterdir() if d.is_dir()]
    else:
        # Import specific rule sets
        rule_sets = [rule_set.strip() for rule_set in args.rules.split(",")]
    
    # Import each rule set
    for rule_set in rule_sets:
        import_rule_set(rule_set, rules_source, cursor_dir, args.link_type, args.force)
    
    # Create a .cursorignore file to avoid tracking the rules themselves
    cursorignore_file = target_dir / ".cursorignore"
    if not cursorignore_file.exists():
        print_colored("Creating .cursorignore file...", Colors.BLUE)
        with open(cursorignore_file, "w") as f:
            f.write("# Cursor rules directory (if using symlinks/hardlinks)\n")
            f.write(".cursor/\n\n")
    else:
        print_colored(".cursorignore already exists, skipping...", Colors.YELLOW)
    
    # Success message
    print()
    print_colored(f"✅ Cursor rules processing completed for {target_dir}", Colors.GREEN)
    print_colored(f"Link type: {args.link_type}", Colors.BLUE)
    print_colored(f"Rule sets: {args.rules}", Colors.BLUE)
    print()
    print_colored("Next steps:", Colors.YELLOW)
    print(f"1. Navigate to your project: cd {target_dir}")
    print("2. Open the project in Cursor")
    print("3. The rules will be automatically applied")
    print()
    
    if args.link_type in ["symlink", "hardlink"]:
        print_colored(f"Note: Using {args.link_type} means changes to rules in the source will affect this project", Colors.YELLOW)


if __name__ == "__main__":
    main() 