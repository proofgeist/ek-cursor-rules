# Installation Guide

Complete guide to installing ek-cursor-rules in your projects.

## Installation Methods

### Method 1: Copy Rules (Recommended)

Copy rules to your project as independent files:

```bash
# Copy all rules
./import-cursor-rules.sh /path/to/project

# Copy specific rule sets only
./import-cursor-rules.sh -r general,git,nodejs /path/to/project

# Python version (cross-platform)
./import-cursor-rules.py /path/to/project
```

**Pros:**
- Rules are independent and can be modified
- No dependency on source repository
- Works offline

**Cons:**
- Updates require re-copying
- Manual sync with upstream changes

### Method 2: Symlinks

Link to source rules for automatic updates:

```bash
./import-cursor-rules.sh -l symlink /path/to/project
```

**Pros:**
- Automatic updates when source changes
- Single source of truth

**Cons:**
- Requires source repository available
- Changes affect all linked projects

### Method 3: Claude.md (Claude Code)

Generate single file for Claude Code:

```bash
./sync-to-claude.py /path/to/project
```

**Pros:**
- Single file, easy to manage
- Works with Claude Code
- Self-contained

**Cons:**
- Large file size (195KB)
- Need to regenerate for updates

## Detailed Setup

### For Cursor IDE

1. **Navigate to cursor rules directory:**
   ```bash
   cd /path/to/ek-cursor-rules
   ```

2. **Import rules:**
   ```bash
   ./import-cursor-rules.sh /path/to/your-project
   ```

3. **Verify installation:**
   ```bash
   ls /path/to/your-project/.cursor/rules/
   ```

4. **Restart Cursor** to load new rules

### For Claude Code

1. **Generate Claude.md:**
   ```bash
   ./sync-to-claude.py /path/to/your-project
   ```

2. **Verify file created:**
   ```bash
   ls -lh /path/to/your-project/Claude.md
   ```

3. **Place in appropriate location:**
   - Project root: `Claude.md`
   - Or: `.claude/Claude.md`

### For Python Projects

Import only Python-relevant rules:

```bash
./import-cursor-rules.sh -r general,git,python,database,versioning /path/to/python-project
```

### For Node.js Projects

Import only Node.js-relevant rules:

```bash
./import-cursor-rules.sh -r general,git,nodejs,database,versioning /path/to/nodejs-project
```

## Import Script Options

### Bash Script (`import-cursor-rules.sh`)

```bash
Usage: ./import-cursor-rules.sh [OPTIONS] TARGET_PATH

Options:
  -l, --link TYPE       Link type: copy (default), symlink, hardlink
  -r, --rules SETS      Comma-separated rule sets to import
  -f, --force           Overwrite existing rules
  -h, --help            Show help message

Examples:
  ./import-cursor-rules.sh /path/to/project
  ./import-cursor-rules.sh -l symlink /path/to/project
  ./import-cursor-rules.sh -r general,git,python /path/to/project
  ./import-cursor-rules.sh -f /path/to/project
```

### Python Script (`import-cursor-rules.py`)

```bash
Usage: python import-cursor-rules.py [OPTIONS] TARGET_PATH

Same options as bash script, cross-platform compatible.
```

### Sync Script (`sync-to-claude.py`)

```bash
Usage: ./sync-to-claude.py [OUTPUT_PATH]

Examples:
  ./sync-to-claude.py                    # Creates ./Claude.md
  ./sync-to-claude.py /path/to/project   # Creates /path/to/project/Claude.md
  ./sync-to-claude.py custom.md          # Creates ./custom.md
```

## Post-Installation

### Verify Installation

1. **Check files exist:**
   ```bash
   # For Cursor
   find .cursor/rules -name "*.mdc"

   # For Claude Code
   ls -lh Claude.md
   ```

2. **Test with AI assistant:**
   - Ask: "What are the core principles?"
   - Should reference: "Seek first to understand" etc.

### Update Rules

```bash
# Pull latest changes
cd /path/to/ek-cursor-rules
git pull origin main

# Re-import to your project
./import-cursor-rules.sh /path/to/your-project

# Or regenerate Claude.md
./sync-to-claude.py /path/to/your-project
```

## Troubleshooting

### Rules Not Loading

**Cursor:**
- Restart Cursor IDE
- Check `.cursor/rules/` directory exists
- Verify `.mdc` file permissions

**Claude Code:**
- Check `Claude.md` in project root or `.claude/`
- Verify file size (should be ~195KB)
- Check file encoding (should be UTF-8)

### Import Script Errors

**Permission denied:**
```bash
chmod +x import-cursor-rules.sh
chmod +x sync-to-claude.py
```

**Python not found:**
```bash
# Use Python 3 explicitly
python3 import-cursor-rules.py /path/to/project
```

**Symlink fails:**
```bash
# Use absolute paths
./import-cursor-rules.sh -l symlink $(pwd)/../my-project
```

## Next Steps

- [Quick Start Tutorial](./quick-start.md)
- [Configuration Guide](./configuration.md)
- [Rule Categories](../user-guide/rule-categories.md)

---

**Navigation**: [← Getting Started](./README.md) | [Quick Start →](./quick-start.md)
