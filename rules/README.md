# Project Plan Management - MDC Files

This directory contains a comprehensive set of `.mdc` files that instruct AI assistants to actively manage and maintain project plans throughout the development process.

## File Organization

### Core Files (Execute in Order)

1. **`01-project-plan-core.mdc`** - Foundation directive
   - Primary rule: Always consult and update project plan
   - Plan location hierarchy
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

### Supporting Files

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

## How It Works

### Priority System
Files are numbered with priority levels (1-7) to ensure proper execution order:
- **Priority 1**: Core directive (always executed first)
- **Priority 2-4**: Workflow phases (pre, during, post work)
- **Priority 5-7**: Supporting standards and integration

### Workflow Integration
The files create a complete workflow:
```
User Request → Pre-Work Analysis → Active Work → Post-Work Updates
     ↓              ↓                 ↓              ↓
Plan Check → Conflict Resolution → Progress Track → Plan Update
```

### Key Features

#### 🎯 **Always-On Plan Management**
- Every AI interaction checks the project plan
- No work proceeds without plan consultation
- Automatic plan updates after completion

#### 🔍 **Conflict Prevention**
- Early detection of scope/priority conflicts
- Clear resolution protocols
- User decision points for plan changes

#### 📊 **Progress Tracking**
- Real-time status updates
- Discovery documentation
- Decision logging

#### 🔄 **Workflow Integration**
- Commit message standards
- Branch naming conventions
- Documentation synchronization

## Expected Project Plan Location

The system looks for project plans in this order:
1. `PROJECT_PLAN.md` (root directory)
2. `docs/PROJECT_PLAN.md`
3. Any file containing "project plan", "roadmap", or "milestones"

## Benefits

### For Developers
- Never lose track of project direction
- Automatic progress documentation
- Clear conflict resolution process
- Integrated development workflow

### For Project Management
- Always current project status
- Documented decisions and changes
- Clear milestone tracking
- Stakeholder communication support

### For AI Assistants
- Clear, actionable instructions
- Structured workflow to follow
- Consistent plan format requirements
- Integration with development tools

## Usage

These `.mdc` files work automatically with AI assistants that support the format. No manual intervention required - the assistant will:

1. **Check** the project plan before any work
2. **Analyze** requests for conflicts or alignment issues
3. **Track** progress during active work
4. **Update** the plan after completing tasks
5. **Maintain** plan quality and consistency

The result is a living, accurate project plan that serves as the single source of truth for project direction and progress.

---

**Note**: These files ensure your project plan becomes an active, maintained document rather than a forgotten artifact. 