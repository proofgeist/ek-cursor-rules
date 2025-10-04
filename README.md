# Cursor Rules - AI Assistant Directives

Hello,
I am sharing my cursor rules by way of illustrating how I work with AI as my development co-pilot. I think it encapsulates a lot of 'good' practices I have come to rely on (and stolen, borrowed, improved) to help me make the most out of my agentic development experience. 

This repository contains `.mdc` files that guide AI coding agents (Cursor, in particular) to follow best practices for development, project management, and code quality. Feel free to mix and match as you see fit. 

Fork away. Or, branch and send me a PR for changes.

- EK

## Quick Start - Import Rules to Your Project

### Choose Your Method

**For Cursor IDE:**
- `import-cursor-rules.sh` (Bash - Unix/Linux/macOS)
- `import-cursor-rules.py` (Python - Cross-platform)

**For Claude Code:**
- `sync-to-claude.py` (Generates single Claude.md file)

#### Basic Usage:
```bash
# Cursor IDE: Copy all rules to a new project
./import-cursor-rules.sh /path/to/my-project

# Cursor IDE: Python version (cross-platform)
./import-cursor-rules.py /path/to/my-project

# Claude Code: Generate Claude.md file
./sync-to-claude.py /path/to/my-project
```

#### Advanced Options:
```bash
# Create symlinks (changes to source rules affect all projects)
./import-cursor-rules.sh -l symlink /path/to/my-project

# Only import specific rule sets
./import-cursor-rules.sh -r general,git /path/to/my-project

# Python project with force overwrite
./import-cursor-rules.sh -r python -f /path/to/python-project

# View all options
./import-cursor-rules.sh --help
```

#### Link Types:
- **`copy`** (default): Independent copies, safe for modification
- **`symlink`**: Links to source rules, updates automatically
- **`hardlink`**: Shared file data, updates with source changes

## Directory Structure

### General Rules (`/rules/000-general-rules/`)
Core directives that apply to all projects:

1. **`001-core-directive.mdc`** - Foundation principles and methodology
2. **`002-pre-work-analysis.mdc`** - Pre-work analysis and alignment
3. **`003-during-work-tracking.mdc`** - Active work progress tracking
4. **`004-post-work-updates.mdc`** - Post-work updates and plan sync
5. **`005-plan-format-standards.mdc`** - Project plan structure standards
6. **`006-conflict-resolution.mdc`** - Conflict detection and resolution
7. **`007-integration-workflow.mdc`** - Development integration workflow
8. **`008-documentation-standards.mdc`** - Comprehensive documentation standards (consolidated)
9. **`011-security-standards.mdc`** - Security best practices and standards

### Git Rules (`/rules/100-git-rules/`)
Version control and collaboration standards:

- **`101-git-standards.mdc`** - Comprehensive Git workflow, commits, branching, PRs, and code review

### Design Rules (`/rules/200-design-rules/`)
Design thinking and user experience standards:

- **`201-design-thinking-personas.mdc`** - User persona requirements and design thinking principles

### Python Projects (`/rules/300-python-projects/`)
Specialized directives for Python development:

- **`301-virtual-environment-setup.mdc`** - Python environment management using `uv`
- **`302-python-code-standards.mdc`** - Python coding standards
- **`303-python-testing-standards.mdc`** - Python testing practices
- **`304-test-organization.mdc`** - Test file organization and structure
- **`305-test-utilities.mdc`** - Test utilities and helper functions

### Versioning Rules (`/rules/400-versioning-rules/`)
Automated versioning and release management:

- **`401-versioning-standards.mdc`** - Semantic versioning with semantic-release (REQUIRED)

### Node.js Projects (`/rules/500-nodejs-projects/`)
Specialized directives for Node.js development:

- **`501-package-management.mdc`** - Package management with pnpm (default)
- **`502-nodejs-code-standards.mdc`** - Node.js coding standards and best practices
- **`503-nodejs-testing-standards.mdc`** - Node.js testing with Vitest
- **`504-express-api-standards.mdc`** - Express.js API development standards
- **`505-nextjs-vercel-standards.mdc`** - Next.js framework and Vercel deployment
- **`506-better-auth-standards.mdc`** - Better-Auth authentication implementation
- **`507-proofkit-standards.mdc`** - ProofKit boilerplate for FileMaker web applications
- **`508-typescript-standards.mdc`** - TypeScript coding standards and best practices

### Database Rules (`/rules/600-database-rules/`)
Database design and management standards:

- **`601-database-standards.mdc`** - PostgreSQL as default, schema design, Prisma, migrations, optimization

## Core Principles

### Design Philosophy
- **Seek first to understand** - Promote thoughtful analysis before action
- **Small things, loosely coupled** - Be functional and modular; keep mutations isolated, avoid side effects
- **As simple as possible but no simpler** - Balance simplicity with functionality
- **Critical thinking encouraged** - Don't agree automatically; offer helpful critiques

### Methodology
- **Start every project with a plan** - Always begin with a project plan
- **No changes without approval** - Share specific plans and wait for explicit approval
- **Surgical changes only** - Keep modifications minimal and targeted
- **Explain rationale** - Always explain why a change is needed
- **Test thoroughly** - Verify changes work, don't break functionality, test edge cases
- **Documentation first** - Document approach before coding, explain decisions, keep README current

## Project Plan Management

### Location Priority
The system looks for project plans in this order:
1. `docs/PROJECT_PLAN.md`
2. `PROJECT_PLAN.md` (root directory)
3. Any file containing "project plan", "roadmap", or "milestones"

### Workflow Integration
```
User Request → Pre-Work Analysis → Active Work → Post-Work Updates
     ↓              ↓                 ↓              ↓
Plan Check → Conflict Resolution → Progress Track → Plan Update
```

### Critical Checkpoints
- ✅ Read plan before starting any work
- ✅ Verify request aligns with current milestone
- ✅ Update plan after completing tasks
- ✅ Note any scope or priority changes

## Key Features

#### 🎯 **Proactive Planning**
- Every project starts with a comprehensive plan
- AI assistants create plans when missing
- No work proceeds without plan consultation

#### 🔒 **Quality Control**
- Approval-based workflow prevents reckless changes
- Surgical modifications maintain code stability
- Comprehensive testing including edge cases

#### 📚 **Documentation-First Approach**
- Document approach before coding
- Explain all decisions along the way
- Keep project documentation current
- All documentation in `/docs` folder with central home
- Comprehensive linking and cross-referencing standards

#### 🔄 **Continuous Integration**
- Commit message standards
- Branch naming conventions
- Documentation synchronization

#### 📖 **Documentation Standards**
- Structured `/docs` folder organization
- Central documentation home with navigation
- Comprehensive linking and cross-referencing
- Writing standards for clarity and consistency

## Technology Stack Standards

### Python Projects
- **Package Management**: `uv` as default
- **Virtual Environment**: Automated setup and management
- **Test Organization**: Structured test files, scripts, and utilities
- **Best Practices**: Modern Python conventions

### Node.js/TypeScript Projects
- **Package Management**: `pnpm` as default
- **Testing Framework**: Vitest (Jest alternative)
- **API Framework**: Express.js with best practices
- **Web Framework**: Next.js with App Router and Server Components
- **Deployment**: Vercel as default platform
- **Authentication**: Better-Auth for type-safe auth
- **FileMaker Integration**: ProofKit for FileMaker web apps
- **Type Safety**: Comprehensive TypeScript standards

### Database
- **Default**: PostgreSQL
- **ORM**: Prisma (Node.js) or SQLAlchemy (Python)
- **Migrations**: Automated with version control
- **Security**: Parameterized queries, encryption, access control

### Versioning & Releases
- **Version Management**: semantic-release (REQUIRED)
- **Commit Format**: Conventional Commits (enforced)
- **Automation**: GitHub Actions for CI/CD
- **Changelog**: Auto-generated from commits

## Benefits

### For Developers
- Clear development methodology
- Automatic progress documentation
- Integrated quality control
- Consistent project structure

### For Project Management
- Always current project status
- Documented decisions and changes
- Clear milestone tracking
- Proactive conflict resolution

### For AI Assistants
- Clear, actionable instructions
- Structured workflow to follow
- Consistent quality standards
- Technology-specific guidance

## Documentation

For comprehensive guides and detailed information:

📖 **[Full Documentation](/docs/README.md)** - Central documentation hub
- [Getting Started](/docs/getting-started/README.md) - Installation, quick start, configuration
- [User Guide](/docs/user-guide/README.md) - Rule categories, best practices (coming soon)
- [Developer Guide](/docs/developer-guide/README.md) - Contributing, creating rules (coming soon)
- [API Reference](/docs/api/README.md) - Script documentation (coming soon)

## Usage

### Automatic Usage (Recommended)
Use the import scripts to set up rules in your projects. The AI assistant will automatically follow the imported rules.

### Manual Usage
These `.mdc` files work automatically with AI assistants that support Cursor rules. The assistant will:

1. **Plan** - Start with or create a project plan
2. **Analyze** - Check requests for conflicts or alignment issues
3. **Approve** - Get explicit approval before making changes
4. **Execute** - Make surgical, well-tested modifications
5. **Document** - Update plans and maintain current documentation

---

**The result is a disciplined, quality-focused development process that maintains project direction while ensuring code quality and documentation.** 