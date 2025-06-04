# Cursor Rules - AI Assistant Directives

This repository contains comprehensive `.mdc` files that guide AI assistants to follow best practices for development, project management, and code quality.

## Quick Start - Import Rules to Your Project

### Using the Import Script

Two import scripts are available:
- `import-cursor-rules.sh` (Bash - Unix/Linux/macOS)
- `import-cursor-rules.py` (Python - Cross-platform)

#### Basic Usage:
```bash
# Copy all rules to a new project
./import-cursor-rules.sh /path/to/my-project

# Python version (cross-platform)
./import-cursor-rules.py /path/to/my-project
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

1. **`01-core-directive.mdc`** - Foundation principles and methodology
   - Functional and modular design principles
   - Approval-based workflow
   - Project plan management
   - Critical checkpoints

2. **`02-pre-work-analysis.mdc`** - Before starting work
   - Plan context review
   - Request alignment checking
   - Conflict detection and resolution

3. **`03-during-work-tracking.mdc`** - Active work monitoring
   - Progress tracking
   - Decision documentation
   - Discovery logging

4. **`04-post-work-updates.mdc`** - After completing work
   - Status updates
   - Plan synchronization
   - Completion tracking

5. **`06-conflict-resolution.mdc`** - Handling conflicts
   - Conflict detection
   - Resolution protocols
   - Communication guidelines

6. **`07-integration-workflow.mdc`** - Development integration
   - Code workflow integration
   - Documentation synchronization
   - Testing and CI/CD alignment

### Git Rules (`/rules/100-git-rules/`)
Version control and collaboration standards:

- **`101-commit-message-standards.mdc`** - Commit message formatting
- **`102-branch-naming-conventions.mdc`** - Branch naming rules
- **`103-git-workflow-standards.mdc`** - Git workflow practices

### Design Rules (`/rules/200-design-rules/`)
UI/UX and design system standards:

- **`201-design-system-standards.mdc`** - Design system guidelines
- **`202-ui-component-standards.mdc`** - UI component standards
- **`203-accessibility-standards.mdc`** - Accessibility requirements

### Python Projects (`/rules/300-python-projects/`)
Specialized directives for Python development:

- **`301-virtual-environment-setup.mdc`** - Python environment management using `uv`
- **`302-python-code-standards.mdc`** - Python coding standards
- **`303-python-testing-standards.mdc`** - Python testing practices

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
1. `PROJECT_PLAN.md` (root directory)
2. `docs/PROJECT_PLAN.md`
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

#### 🔄 **Continuous Integration**
- Commit message standards
- Branch naming conventions
- Documentation synchronization

## Language-Specific Features

### Python Projects
- **Package Management**: Uses `uv` as default for Python projects
- **Virtual Environment**: Automated setup and management
- **Best Practices**: Following Python-specific conventions

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