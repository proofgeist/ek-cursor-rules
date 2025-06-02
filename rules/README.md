# Cursor Rules - AI Assistant Directives

This repository contains comprehensive `.mdc` files that guide AI assistants to follow best practices for development, project management, and code quality.

## Directory Structure

### General Rules (`/rules/general-rules/`)
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

5. **`05-plan-format-standards.mdc`** - Plan structure requirements
   - Standard format template
   - Status indicators
   - Quality standards

6. **`06-conflict-resolution.mdc`** - Handling conflicts
   - Conflict detection
   - Resolution protocols
   - Communication guidelines

7. **`07-integration-workflow.mdc`** - Development integration
   - Code workflow integration
   - Documentation synchronization
   - Testing and CI/CD alignment

### Language-Specific Rules (`/rules/python-projects/`)
Specialized directives for specific technologies:

- **`01-virtual-environment-setup.mdc`** - Python environment management using `uv`

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

These `.mdc` files work automatically with AI assistants that support Cursor rules. The assistant will:

1. **Plan** - Start with or create a project plan
2. **Analyze** - Check requests for conflicts or alignment issues
3. **Approve** - Get explicit approval before making changes
4. **Execute** - Make surgical, well-tested modifications
5. **Document** - Update plans and maintain current documentation

---

**The result is a disciplined, quality-focused development process that maintains project direction while ensuring code quality and documentation.** 