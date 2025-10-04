# Getting Started

Get up and running with ek-cursor-rules in minutes.

## Quick Navigation

- [Installation Guide](./installation.md) - Import rules into your projects
- [Quick Start](./quick-start.md) - 5-minute setup guide
- [Configuration](./configuration.md) - Customize for your needs

## Overview

ek-cursor-rules provides AI assistant directives that enforce best practices across your development projects. The rules work with both Cursor IDE and Claude Code.

## Prerequisites

- **For Cursor**: Cursor IDE installed
- **For Claude Code**: Claude Code CLI installed
- **For Python scripts**: Python 3.6+
- **For import scripts**: Bash or Python

## Choose Your Path

### 1. Cursor IDE Users

Import rules directly into your Cursor project:

```bash
./import-cursor-rules.sh /path/to/your-project
```

The rules will be copied to `.cursor/rules/` in your project.

### 2. Claude Code Users

Generate a single `Claude.md` file:

```bash
./sync-to-claude.py /path/to/your-project
```

Place the generated `Claude.md` in your project root or `.claude/` directory.

### 3. Quick Start for Any Project

```bash
# Clone this repository
git clone https://github.com/yourusername/ek-cursor-rules.git
cd ek-cursor-rules

# Copy rules to your project
./import-cursor-rules.sh /path/to/your-project

# Or generate Claude.md
./sync-to-claude.py /path/to/your-project
```

## What Gets Installed

When you import the rules, you get:

- **General Rules**: Core directives, documentation, security
- **Git Rules**: Commit conventions, branching, code review
- **Design Rules**: User personas, design thinking
- **Python Rules** (optional): Python-specific standards
- **Node.js Rules** (optional): Node.js/TypeScript standards
- **Database Rules**: PostgreSQL, Prisma standards
- **Versioning Rules**: semantic-release setup

## Next Steps

1. **[Complete Installation](./installation.md)** - Detailed setup guide
2. **[Quick Start Tutorial](./quick-start.md)** - Walk through first project
3. **[Explore Rule Categories](../user-guide/rule-categories.md)** - Understand available rules
4. **[Customize Configuration](./configuration.md)** - Tailor to your needs

---

**Navigation**: [← Documentation Home](../README.md) | [Installation →](./installation.md)
