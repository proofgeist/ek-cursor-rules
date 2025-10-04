# AI Assistant Rules

*Generated from cursor rules on 2025-10-03 23:55:08*

---


# General Rules

<!-- Source: 001-core-directive.mdc -->

# Core Directive

## Principles

- Seek first to understand
- Design for "small things, loosely coupled" -- be functional and modular; Keep mutations isolated, avoid side effects.
- Make things as simple as possible but no simpler.
- Do not agree with me automatically. Consider my observations critically and offer helpful critiques or refinements to my thought process.

## Methodology
- **Start every project with a plan**: Always begin with a project plan. If none exists, work with me to formuate one.
- **No changes without approval**: Always share a specific plan and wait for explicit approval before making any code modifications
- **Surgical changes only**: Keep modifications minimal and targeted - avoid large refactors
- **Explain rationale**: Always explain why a change is needed and what problem it solves
- **Test thoroughly**: Verify changes work as expected, don't break existing functionality, and test edge cases.
- **Documentation first**: Document the approach before coding, explain all decisions, and keep README current.

## Project Plan Instructions
**ALWAYS consult the project plan before making any changes and update it after completing work.**

1. **Primary**: `PROJECT_PLAN.md` (root directory)
2. **Secondary**: `docs/PROJECT_PLAN.md` 
3. **Fallback**: Any file containing "project plan", "roadmap", or "milestones"

## When Plan is Missing

If no project plan exists:
1. **Alert the user** immediately
2. **Offer to create one** based on current context
3. **Do not proceed** without explicit user direction

## Critical Checkpoints

- ✅ Read plan before starting any work
- ✅ Verify request aligns with current milestone
- ✅ Update plan after completing tasks
- ✅ Note any scope or priority changes

---

**This is the foundation rule - all other project management directives build on this.**

---

<!-- Source: 002-pre-work-analysis.mdc -->

# Pre-Work Analysis Protocol

## Required Analysis Before Starting

### 1. Plan Context Review
Read and understand:
- Current project phase/milestone
- Planned features and priorities  
- Known issues and blockers
- Dependencies and prerequisites

### 2. Request Alignment Check
Verify if the user's request:
- ✅ Fits within the current milestone
- ⚠️ Requires addressing dependencies first
- 🔄 Changes scope or priorities
- 📝 Introduces new features not in plan

### 3. Conflict Resolution
If request conflicts with plan:
1. **Highlight the conflict clearly**
2. **Explain implications** (timeline, dependencies, scope)
3. **Propose resolution options**:
   - Adjust current milestone
   - Defer to future milestone
   - Modify request to fit plan
4. **Wait for explicit user direction**

### 4. Plan Update Proposals
Suggest plan updates when request:
- Introduces new features
- Reveals new dependencies
- Changes technical approach
- Affects timeline estimates

## Communication Template

```
📋 **Project Plan Check**
- Current milestone: [milestone name]
- Request alignment: [✅ aligned / ⚠️ dependency / 🔄 scope change]
- Proposed plan updates: [list any needed updates]
- Recommendation: [proceed / adjust plan / clarify scope]
```

---

**Complete this analysis before any code changes or implementation work.**

---

<!-- Source: 003-during-work-tracking.mdc -->

# During-Work Progress Tracking

## Active Work Guidelines

### 1. Reference Plan for Decisions
- Consult plan when making architectural choices
- Ensure decisions align with project direction
- Consider impact on future milestones

### 2. Discovery Tracking
Note any discoveries that affect:
- Future milestone planning
- Technical dependencies
- Scope or complexity estimates
- Architecture decisions

### 3. Progress Monitoring
Track progress on current milestone items:
- Which tasks are being worked on
- Estimated completion status
- Any blockers encountered
- Changes in approach or scope

### 4. Decision Documentation
Log significant decisions made during work:
- Technical approach choices
- Architecture modifications
- Scope adjustments
- Dependency discoveries

## Real-Time Updates

### Progress Indicators
- 🔄 **In Progress**: Currently working on this item
- ⏸️ **Paused**: Temporarily blocked or deprioritized
- 🔍 **Investigating**: Researching approach or dependencies
- 🛠️ **Implementing**: Active development in progress

### Discovery Notes
Document discoveries in this format:
```
💡 **Discovery**: [Brief description]
- **Impact**: [How this affects the plan]
- **Action**: [What needs to be updated]
- **Timeline**: [Effect on current/future milestones]
```

### Decision Log Format
```
🎯 **Decision**: [What was decided]
- **Context**: [Why this decision was needed]
- **Alternatives**: [Other options considered]
- **Impact**: [Effect on plan/architecture]
- **Date**: [When decided]
```

---

**Keep the project plan current with real-time progress and discoveries.**

---

<!-- Source: 004-post-work-updates.mdc -->

# Post-Work Plan Updates

## Required Updates After Completing Work

### 1. Status Updates
Update the project plan to reflect:
- ✅ **Completed tasks/features**
- 🔄 **Modified scope or approach** 
- 🚫 **Blocked items** with clear reasons
- 📝 **New tasks discovered** during work
- 🎯 **Updated priorities or timelines**

### 2. Progress Tracking
- Mark completed items with ✅
- Update in-progress items with current status
- Add newly discovered tasks to appropriate milestones
- Note any changes to estimates or dependencies

### 3. Documentation Sync
Ensure consistency between:
- Project plan and implementation
- README and current capabilities
- Architecture decisions and code
- Dependencies and actual requirements

## Update Templates

### Completion Update
```
## Work Completed: [Date]
### ✅ Completed
- [Task/feature completed]
- [Another completed item]

### 🔄 Modified
- [Item]: [How it changed and why]

### 📝 New Tasks Discovered
- [New task]: [Why needed, which milestone]

### 🎯 Updated Estimates
- [Task]: [Old estimate] → [New estimate] ([Reason])
```

### Milestone Progress
```
### [Milestone Name] - [Updated Status]
Progress: [X/Y tasks completed] ([percentage]%)
- [x] Completed task
- [🔄] In progress task (current status)
- [ ] Pending task
- [📝] Newly discovered task
- [🚫] Blocked task (reason and impact)
```

## Quality Checks

Before finalizing updates:
- ✅ All completed work is marked
- ✅ New discoveries are captured
- ✅ Blockers are documented with reasons
- ✅ Timeline impacts are noted
- ✅ Next steps are clear

## Integration Notes

### Commit Messages
Reference plan updates in commits:
```
feat: implement feature X

- Completes milestone 1.2 task "Feature X"
- Updates project plan with completion status
- Discovered need for additional validation (added to milestone 1.3)
```

---

**Always update the plan immediately after completing work - don't let it become stale.**

---

<!-- Source: 005-plan-format-standards.mdc -->

# Project Plan Format Standards

## Required Plan Structure

Every project plan must include these sections:

```markdown
# Project Plan - [Project Name]

## Current Status
- **Phase**: [Current development phase]
- **Last Updated**: [Date]
- **Next Milestone**: [Target date and goals]
- **Overall Progress**: [X/Y milestones completed]

## User Personas
### User Persona: [Persona Name]
- **Primary User**: [Brief description of user type and context]
- **Pain Points**: [List 2-4 key problems this user faces]
- **Goals**: [List 2-4 primary objectives this user wants to achieve]
- **Context**: [When/where/how they use the solution - optional]

[Additional personas as needed]

## Milestones
### [Milestone Name] - [Status] - [Target Date]
**Goal**: [Brief description of milestone objective]
**Progress**: [X/Y tasks completed] ([percentage]%)

- [ ] Task 1 - [Brief description]
- [x] Completed task - [Brief description]
- [🔄] In progress task - [Current status]
- [🚫] Blocked task - [Reason for block]
- [📝] New task discovered - [Why needed]

**Dependencies**: [List any dependencies]
**Risks**: [Known risks or concerns]

## Architecture Decisions
- **[Date]**: [Decision] - [Rationale and alternatives considered]

## Known Issues & Blockers
- **[Issue]**: [Description, impact, and resolution plan]

## Future Considerations
- [Items for later milestones or post-MVP]

## Change Log
- **[Date]**: [Summary of changes made to plan]
```

## Status Indicators

### Task Status
- `[ ]` **Planned**: Not yet started
- `[🔄]` **In Progress**: Currently being worked on
- `[x]` **Completed**: Finished and verified
- `[🚫]` **Blocked**: Cannot proceed (include reason)
- `[📝]` **New**: Discovered during work
- `[⏸️]` **Paused**: Temporarily deprioritized
- `[🔍]` **Investigating**: Researching approach

### Milestone Status
- **🎯 Active**: Currently being worked on
- **✅ Complete**: All tasks finished
- **📋 Planned**: Scheduled for future
- **🚫 Blocked**: Cannot proceed
- **🔄 In Progress**: Some tasks completed

## Quality Standards

### Plan Maintenance
- Update **Last Updated** date with every change
- Remove completed items after milestone closure
- Keep future items realistic and well-defined
- Maintain clear, actionable task descriptions

### Consistency Requirements
- Task descriptions should be specific and measurable
- Dependencies must be clearly identified
- Blockers must include resolution plans
- Architecture decisions must include rationale

### Review Triggers
Update plan when:
- Starting new work
- Completing tasks
- Discovering new requirements
- Encountering blockers
- Making architecture decisions
- Changing priorities

---

**Maintain this format consistently to ensure the plan remains useful and actionable.**

---

<!-- Source: 006-conflict-resolution.mdc -->

# Project Plan Conflict Resolution

## Conflict Detection

### Common Conflict Types
- **Scope creep**: Request adds features not in current milestone
- **Priority conflicts**: Request changes established priorities
- **Dependency violations**: Request skips required prerequisites
- **Timeline conflicts**: Request affects milestone deadlines
- **Architecture conflicts**: Request contradicts planned approach

### Early Warning Signs
- Request mentions features not in plan
- User asks to "quickly add" something
- Request requires significant refactoring
- Work would affect multiple milestones
- Request changes core assumptions

## Resolution Protocol

### 1. Immediate Assessment
When conflict detected:
```
🚨 **Plan Conflict Detected**
- **Request**: [Summary of user request]
- **Conflict**: [How it conflicts with current plan]
- **Impact**: [Timeline, scope, or dependency effects]
- **Current Milestone**: [What would be affected]
```

### 2. Impact Analysis
Evaluate:
- **Timeline impact**: How much delay would this cause?
- **Scope impact**: How much additional work is required?
- **Dependency impact**: What other tasks would be affected?
- **Risk impact**: What new risks does this introduce?

### 3. Resolution Options
Present clear options:

#### Option A: Adjust Plan
- Modify current milestone to include request
- Update timeline and dependencies
- Reassess priorities

#### Option B: Defer Request
- Add to future milestone
- Maintain current plan integrity
- Explain rationale for deferral

#### Option C: Compromise Solution
- Implement minimal version now
- Plan full implementation for later
- Identify what can be done within current scope

### 4. User Decision Required
```
📋 **Resolution Required**

**Options:**
1. **Adjust Plan**: [Description and impacts]
2. **Defer Request**: [When it could be addressed]
3. **Compromise**: [What can be done now vs later]

**Recommendation**: [Your suggested approach with rationale]

**Please choose how to proceed before I continue.**
```

## Communication Guidelines

### Be Clear and Direct
- State conflicts explicitly
- Explain implications clearly
- Don't minimize the impact
- Provide specific options

### Stay Solution-Focused
- Always offer multiple options
- Explain trade-offs clearly
- Recommend the best path forward
- Respect user's final decision

### Document Decisions
After resolution:
- Update plan with decision made
- Note rationale for future reference
- Adjust affected milestones
- Update timeline if needed

## Special Cases

### Urgent Requests
If user indicates urgency:
1. Acknowledge the urgency
2. Still explain the conflict
3. Offer expedited options
4. Get explicit approval for plan changes

### Stakeholder Pressure
If request comes from stakeholders:
1. Respect the business context
2. Explain technical implications
3. Offer implementation strategies
4. Document the decision rationale

---

**Never proceed with conflicting work without explicit user direction and plan updates.**

---

<!-- Source: 007-integration-workflow.mdc -->

# Development Workflow Integration

## Code Development Integration

### Commit Message Standards
Reference plan updates in commit messages:
```
feat: implement user authentication

- Completes milestone 1.2 task "User login system"
- Updates project plan with completion status
- Discovered need for password reset flow (added to milestone 1.3)

Plan-Update: Mark auth system as complete, add password reset task
```

### Branch Naming
Include milestone references:
```
feature/milestone-1.2-user-auth
bugfix/milestone-1.1-api-validation
refactor/milestone-2.0-database-schema
```

### Pull Request Templates
Include plan context:
```markdown
## Plan Context
- **Milestone**: [Which milestone this addresses]
- **Tasks Completed**: [List of plan tasks finished]
- **Plan Updates**: [Any changes needed to the plan]
- **Dependencies**: [Any new dependencies discovered]

## Implementation
[Standard PR description]

## Plan Impact
- [ ] Project plan updated with completion status
- [ ] New tasks added if discovered
- [ ] Timeline impacts documented
```

## Documentation Synchronization

### README Alignment
Ensure README reflects:
- Current project status from plan
- Completed features and capabilities
- Known limitations and future plans
- Installation and setup requirements

### Architecture Documentation
Keep synchronized:
- Architecture decisions in plan
- Technical documentation
- Code comments and structure
- API documentation

### Dependency Management
Track in both plan and code:
- External dependencies and versions
- Internal module dependencies
- Development tool requirements
- Deployment dependencies

## Testing Integration

### Test Planning
Align tests with plan:
- Verify completed features match specifications
- Test acceptance criteria from plan tasks
- Validate architecture decisions
- Check dependency integrations

### Test Results Impact
Update plan based on testing:
- Mark tasks as truly complete after testing
- Document any scope changes discovered
- Add bug fixes to appropriate milestones
- Update estimates based on test complexity

## Continuous Integration

### CI/CD Pipeline
Include plan validation:
```yaml
# Example CI step
- name: Validate Plan Sync
  run: |
    # Check if plan is updated
    # Verify completed features are tested
    # Ensure documentation is current
```

### Automated Checks
- Plan freshness (updated within reasonable time)
- Completion status accuracy
- Documentation consistency
- Dependency alignment

## Quality Assurance

### Regular Plan Reviews
Schedule periodic reviews:
- **Weekly**: Progress against current milestone
- **Monthly**: Overall plan accuracy and timeline
- **Per Milestone**: Complete plan validation
- **Major Changes**: Architecture and scope review

### Consistency Audits
Regular checks for:
- Plan vs. implementation alignment
- Documentation currency
- Dependency accuracy
- Timeline realism

### Stakeholder Communication
Use plan for:
- Progress reports
- Timeline updates
- Scope change discussions
- Risk communication

## Tool Integration

### Project Management Tools
Sync with external tools:
- Export milestones to project trackers
- Import external deadlines
- Coordinate with team planning tools
- Maintain single source of truth

### Development Tools
Integrate with:
- IDE project settings
- Linting and formatting rules
- Build system configuration
- Deployment scripts

---

**The project plan should be the central hub that connects all development activities.**

---

<!-- Source: 008-documentation-standards.mdc -->

# Documentation Standards

## Core Principles

1. **Avoid technical jargon** whenever possible
2. **Use active voice** - write "Click the button" not "The button should be clicked"
3. **Use simple language** for complex ideas, not the other way around
4. **Be succinct** - respect the reader's time
5. **Write for the reader** - understand their knowledge level and needs
6. **Provide context** - explain why, not just how
7. **Include examples** - show, don't just tell
8. **Keep it current** - documentation must match actual implementation

## Documentation Structure

### Required Folder Organization

```
project-root/
└── docs/
    ├── README.md              # Central documentation home (REQUIRED)
    ├── getting-started/       # Setup and onboarding
    ├── user-guide/            # End-user documentation
    ├── developer-guide/       # Developer documentation
    ├── api/                   # API documentation
    ├── architecture/          # System design docs
    └── troubleshooting/       # Problem-solving guides
```

### Central Documentation Home (REQUIRED)

**Every project MUST have `/docs/README.md` as the central documentation hub.**

```markdown
# Project Name Documentation

## Quick Links
- [Getting Started](./getting-started/README.md)
- [User Guide](./user-guide/README.md)
- [Developer Guide](./developer-guide/README.md)
- [API Documentation](./api/README.md)

## Documentation Structure
Brief explanation of how documentation is organized.

## Contributing
Link to contribution guidelines.
```

### Document Template

Every documentation file should follow this structure:

```markdown
# [Clear, Descriptive Title]

## Overview
Brief explanation of what this document covers and why it's important.

## Prerequisites
What the reader needs to know or have before reading this document.

## [Main Content Sections]
Organized by logical flow or user journey.

## Examples
Practical examples showing how to use or implement.

## Troubleshooting
Common issues and their solutions.

## Related Documentation
Links to related docs and next steps.
```

## Writing Standards

### Content Guidelines

#### Overview Section
- **Purpose**: What problem does this solve?
- **Scope**: What does this document cover?
- **Audience**: Who should read this?
- **Time estimate**: How long will this take to read/implement?

#### Main Content
- **Start with purpose** - what problem does this solve?
- **Include examples** - code snippets, screenshots, diagrams
- **Provide context** - when/why to use this feature
- **Include troubleshooting** - common issues and solutions

#### Code Examples
- **Complete and runnable** - readers should be able to copy/paste
- **Well-commented** - explain non-obvious parts
- **Show real-world usage** - not just hello world
- **Include expected output** - what should happen

### Style Guidelines

#### Language & Tone
- **Use active voice**: "Click the button" not "The button should be clicked"
- **Write for the target audience**: User vs developer documentation
- **Keep sentences short and clear**: Aim for 15-20 words per sentence
- **Use consistent terminology**: Define terms once, use them consistently
- **Include step-by-step instructions**: For procedures

#### Formatting
- **Use headings** to break up content (h2, h3, h4)
- **Use lists** for items, steps, or options
- **Use code blocks** with language syntax highlighting
- **Use tables** for structured data
- **Use callouts** for important notes, warnings, tips

#### Callout Format
```markdown
> **Note**: Additional information that's helpful but not critical

> **Warning**: Important information about potential issues

> **Tip**: Helpful suggestions or best practices
```

## Linking Standards

### Internal Documentation Links
- **Always use relative paths** from the current document
- **Link to specific sections** when possible (e.g., `../user-guide/features.md#authentication`)
- **Use descriptive link text** (e.g., "See [Authentication Guide](../user-guide/authentication.md)")

### Cross-Reference Requirements
- **Every new document MUST be linked from central home**
- **Related documents should cross-reference each other**
- **Use "See also" sections** for related documentation

### Link Text Guidelines
```markdown
<!-- Good -->
See the [Getting Started Guide](./getting-started.md) for setup instructions.

<!-- Bad -->
Click [here](./getting-started.md) for more information.
```

## Quality Standards

### Content Requirements
- **Accuracy**: All information must be correct and up-to-date
- **Completeness**: Cover all necessary information
- **Clarity**: Easily understood by target audience
- **Examples**: Include practical, working examples
- **Searchability**: Use clear headings and keywords

### Documentation Metrics
Track and maintain:
- **Documentation coverage** (features documented vs implemented)
- **Link health** (broken links percentage)
- **Documentation freshness** (last updated dates)
- **User feedback** on documentation quality

## Enforcement Protocol

### Pre-Documentation Checklist
Before creating any documentation, verify:
- [ ] `/docs` folder exists
- [ ] Central documentation home exists and is current
- [ ] Appropriate subfolder structure is in place
- [ ] Link from central home is planned

### Post-Documentation Requirements
After creating documentation:
- [ ] Add link to central documentation home
- [ ] Update any related documentation with cross-references
- [ ] Verify all internal links work
- [ ] Add/update last_updated date in frontmatter

### Regular Audits
- **Monthly**: Check for broken links
- **Per milestone**: Verify documentation completeness
- **Per release**: Update all last_updated dates
- **Quarterly**: Review documentation structure and organization

## Integration with Workflow

### Project Plan Integration
- **Documentation tasks** must be included in project milestones
- **Documentation review** required before feature completion
- **Documentation updates** tracked in project plan

### Git Workflow Integration
- **Documentation changes** follow same approval process as code
- **Documentation commits** reference related code changes
- **Documentation review** included in pull request process

## Communication Templates

### When Creating New Documentation
```
📚 **Documentation Created**: [Document Name]
- **Location**: `/docs/[subfolder]/[filename].md`
- **Linked from**: [Central home section]
- **Cross-references**: [List of related docs]
- **Next steps**: [Any follow-up documentation needed]
```

### When Updating Documentation Structure
```
🔄 **Documentation Structure Update**
- **Changes**: [What was modified]
- **Impact**: [How this affects existing docs]
- **Links updated**: [List of modified links]
- **Central home updated**: [Yes/No]
```

---

**This rule ensures all documentation is clear, well-organized, and maintainable through consistent standards.**

---

<!-- Source: 011-security-standards.mdc -->

# Security Standards

## Core Security Principles

1. **Defense in Depth** - Multiple layers of security controls
2. **Principle of Least Privilege** - Minimum necessary access
3. **Fail Securely** - Failures should deny access, not grant it
4. **Security by Design** - Security considerations from the start
5. **Keep Security Simple** - Complexity is the enemy of security
6. **Never Trust User Input** - Always validate and sanitize

## Authentication & Authorization

### Authentication Standards

**Password Requirements:**
- Minimum 8 characters (12+ recommended)
- Must include: uppercase, lowercase, numbers, special characters
- No common passwords (check against breach databases)
- Implement rate limiting on login attempts
- Use secure password hashing (bcrypt, argon2, scrypt)

**Session Management:**
- Use secure, httpOnly, sameSite cookies
- Implement session timeout (15-30 minutes idle)
- Regenerate session ID after login
- Implement secure logout (invalidate server-side)
- Use CSRF tokens for state-changing operations

**Multi-Factor Authentication:**
- Require MFA for sensitive operations
- Support TOTP (Time-based One-Time Password)
- Provide backup codes for account recovery
- Never send codes via SMS if possible (use authenticator apps)

### Authorization Standards

**Access Control:**
- Implement Role-Based Access Control (RBAC)
- Check authorization on every request
- Validate on server-side, not client-side
- Log authorization failures
- Use attribute-based access when needed

**API Authorization:**
- Use OAuth 2.0 for third-party access
- Implement proper scope validation
- Use short-lived access tokens (15 min)
- Implement refresh token rotation
- Validate tokens on every request

## Input Validation & Sanitization

### Validation Rules

**Always Validate:**
- Data type and format
- Length and size limits
- Allowed characters/patterns
- Business logic constraints
- File types and content

**Validation Patterns:**
```javascript
// Good - Server-side validation
const userSchema = {
  email: z.string().email().max(255),
  age: z.number().int().min(18).max(120),
  username: z.string().min(3).max(30).regex(/^[a-zA-Z0-9_]+$/)
};

// Bad - Client-side only
<input type="email" required /> // Not enough!
```

### Sanitization Rules

**HTML/XSS Prevention:**
- Escape output based on context (HTML, JavaScript, URL, CSS)
- Use templating engines with auto-escaping
- Sanitize rich text with allowlist-based libraries
- Never use `innerHTML` with user content
- Set Content-Security-Policy headers

**SQL Injection Prevention:**
- Always use parameterized queries/prepared statements
- Never concatenate user input into SQL
- Use ORMs with proper escaping
- Validate input types before queries
- Apply principle of least privilege to database users

**Command Injection Prevention:**
- Never pass user input to system commands
- Use language-specific APIs instead of shell commands
- Whitelist allowed values if commands necessary
- Validate and escape all inputs

## Secret Management

### Secret Storage

**Environment Variables:**
```bash
# .env.local (NEVER commit)
DATABASE_URL="postgresql://user:pass@localhost:5432/db"
API_SECRET_KEY="your-secret-key-here"
ENCRYPTION_KEY="your-encryption-key-here"

# .env.example (safe to commit)
DATABASE_URL="postgresql://user:password@localhost:5432/dbname"
API_SECRET_KEY="your-secret-key"
ENCRYPTION_KEY="your-encryption-key"
```

**Secret Management Tools:**
- Use HashiCorp Vault for production secrets
- Use AWS Secrets Manager / Azure Key Vault for cloud
- Use 1Password / Bitwarden for team secrets
- Rotate secrets regularly (90 days max)
- Never hardcode secrets in code

**Secret Detection:**
- Use git-secrets or similar tools
- Scan commits for exposed secrets
- Set up pre-commit hooks to prevent commits with secrets
- Monitor for leaked secrets (GitHub secret scanning)

### API Keys & Tokens

**Best Practices:**
- Generate cryptographically random keys (32+ bytes)
- Use different keys per environment
- Implement key rotation
- Store hashed versions when possible
- Revoke compromised keys immediately
- Monitor key usage for anomalies

## Data Protection

### Encryption Standards

**At Rest:**
- Encrypt sensitive data in database (PII, passwords, tokens)
- Use AES-256 for symmetric encryption
- Use proper key management (KMS, Vault)
- Encrypt backups
- Encrypt file uploads

**In Transit:**
- Always use HTTPS/TLS 1.2+ in production
- Use HSTS headers (Strict-Transport-Security)
- Implement certificate pinning for mobile apps
- Encrypt WebSocket connections (wss://)
- Validate SSL/TLS certificates

**Encryption Examples:**
```javascript
// Encrypt sensitive data before storage
import crypto from 'crypto';

const algorithm = 'aes-256-gcm';
const key = Buffer.from(process.env.ENCRYPTION_KEY, 'hex');

function encrypt(text) {
  const iv = crypto.randomBytes(16);
  const cipher = crypto.createCipheriv(algorithm, key, iv);
  let encrypted = cipher.update(text, 'utf8', 'hex');
  encrypted += cipher.final('hex');
  const authTag = cipher.getAuthTag();
  return `${iv.toString('hex')}:${authTag.toString('hex')}:${encrypted}`;
}

function decrypt(encryptedData) {
  const [ivHex, authTagHex, encrypted] = encryptedData.split(':');
  const iv = Buffer.from(ivHex, 'hex');
  const authTag = Buffer.from(authTagHex, 'hex');
  const decipher = crypto.createDecipheriv(algorithm, key, iv);
  decipher.setAuthTag(authTag);
  let decrypted = decipher.update(encrypted, 'hex', 'utf8');
  decrypted += decipher.final('utf8');
  return decrypted;
}
```

### Data Privacy

**PII (Personally Identifiable Information):**
- Minimize collection of PII
- Document what PII is collected and why
- Implement data retention policies
- Provide user data export/deletion
- Comply with GDPR/CCPA requirements
- Anonymize data in non-production environments

**Data Minimization:**
- Only collect necessary data
- Delete data when no longer needed
- Avoid logging sensitive information
- Redact PII from logs and errors
- Use data classification (public, internal, confidential, restricted)

## Security Headers

### Required HTTP Headers

```javascript
// Express.js example with Helmet
import helmet from 'helmet';

app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      styleSrc: ["'self'", "'unsafe-inline'"], // Be specific
      scriptSrc: ["'self'"],
      imgSrc: ["'self'", "data:", "https:"],
      connectSrc: ["'self'"],
      fontSrc: ["'self'"],
      objectSrc: ["'none'"],
      mediaSrc: ["'self'"],
      frameSrc: ["'none'"],
    },
  },
  hsts: {
    maxAge: 31536000, // 1 year
    includeSubDomains: true,
    preload: true,
  },
  referrerPolicy: { policy: 'strict-origin-when-cross-origin' },
}));

// Additional headers
app.use((req, res, next) => {
  res.setHeader('X-Content-Type-Options', 'nosniff');
  res.setHeader('X-Frame-Options', 'DENY');
  res.setHeader('X-XSS-Protection', '1; mode=block');
  res.setHeader('Permissions-Policy', 'geolocation=(), microphone=(), camera=()');
  next();
});
```

### CORS Configuration

```javascript
// Restrictive CORS setup
const corsOptions = {
  origin: (origin, callback) => {
    const allowedOrigins = process.env.ALLOWED_ORIGINS?.split(',') || [];
    if (!origin || allowedOrigins.includes(origin)) {
      callback(null, true);
    } else {
      callback(new Error('Not allowed by CORS'));
    }
  },
  credentials: true,
  optionsSuccessStatus: 200,
  maxAge: 86400, // 24 hours
};

app.use(cors(corsOptions));
```

## Rate Limiting & DDoS Protection

### Rate Limiting Implementation

```javascript
import rateLimit from 'express-rate-limit';

// General API rate limit
const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // 100 requests per window
  message: 'Too many requests, please try again later',
  standardHeaders: true,
  legacyHeaders: false,
});

// Strict limit for authentication
const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 5, // 5 attempts per 15 minutes
  skipSuccessfulRequests: true,
  message: 'Too many login attempts, please try again later',
});

app.use('/api/', apiLimiter);
app.use('/api/auth/', authLimiter);
```

### DDoS Protection

- Use CDN with DDoS protection (Cloudflare, AWS Shield)
- Implement rate limiting at multiple layers
- Use connection limits and timeouts
- Monitor for unusual traffic patterns
- Implement CAPTCHA for suspicious activity
- Use Web Application Firewall (WAF)

## Dependency Security

### Dependency Management

**Regular Audits:**
```bash
# Node.js
pnpm audit
pnpm audit fix

# Python
pip-audit
safety check
```

**Automated Scanning:**
- Enable Dependabot/Renovate for automatic updates
- Review security advisories regularly
- Update dependencies promptly
- Pin dependency versions in production
- Use lock files (pnpm-lock.yaml, requirements.txt)

**Supply Chain Security:**
- Verify package integrity (checksums, signatures)
- Review dependencies before adding
- Minimize dependency count
- Use official registries only
- Enable 2FA on package manager accounts

## Logging & Monitoring

### Security Logging

**What to Log:**
- Authentication attempts (success/failure)
- Authorization failures
- Input validation failures
- Security-relevant configuration changes
- API usage patterns
- Error conditions

**What NOT to Log:**
- Passwords or secrets
- Credit card numbers
- Session tokens
- PII without redaction
- Full request/response bodies with sensitive data

**Log Security:**
```javascript
// Good - Redacted logging
logger.info({
  event: 'login_attempt',
  user: user.id,
  ip: redactIP(req.ip),
  success: false,
  reason: 'invalid_password'
});

// Bad - Exposing sensitive data
logger.info({
  event: 'login_attempt',
  email: user.email, // PII
  password: password, // NEVER!
  ip: req.ip // Full IP = PII
});
```

### Security Monitoring

**Implement Monitoring For:**
- Failed authentication attempts (brute force detection)
- Unusual API access patterns
- Privilege escalation attempts
- Data exfiltration patterns
- Error rate spikes
- Geographic anomalies

**Alerting:**
- Set up alerts for security events
- Define incident response procedures
- Implement automated blocking for obvious attacks
- Log all security alerts
- Regular review of security logs

## Secure Development Practices

### Code Review Checklist

**Security Review Points:**
- [ ] No hardcoded secrets or credentials
- [ ] Input validation on all user inputs
- [ ] Output encoding based on context
- [ ] Parameterized queries (no SQL injection)
- [ ] Proper authentication/authorization checks
- [ ] Secure session management
- [ ] No sensitive data in logs
- [ ] Security headers implemented
- [ ] HTTPS enforced
- [ ] Dependencies up to date

### Security Testing

**Required Tests:**
- Static Application Security Testing (SAST)
- Dependency vulnerability scanning
- Authentication/authorization tests
- Input validation tests
- CSRF protection tests
- XSS prevention tests

**Tools to Use:**
- npm audit / pnpm audit
- Snyk / Dependabot
- OWASP ZAP for penetration testing
- SonarQube for code quality
- Git-secrets for secret detection

## Incident Response

### Security Incident Protocol

**When a Security Issue is Discovered:**

1. **Immediate Response** (Within 1 hour)
   - Assess severity and impact
   - Contain the issue (disable feature, revoke keys)
   - Notify security team/lead

2. **Investigation** (Within 4 hours)
   - Identify root cause
   - Determine scope of breach
   - Check logs for exploitation
   - Document findings

3. **Remediation** (Within 24 hours)
   - Deploy fix to production
   - Rotate compromised credentials
   - Notify affected users (if applicable)
   - Update security controls

4. **Post-Incident** (Within 1 week)
   - Conduct post-mortem
   - Update security procedures
   - Implement preventive measures
   - Document lessons learned

### Disclosure Policy

- Report security vulnerabilities privately
- Give security team time to fix (90 days)
- Coordinate disclosure with stakeholders
- Document CVEs for significant issues
- Thank security researchers

## Compliance & Regulations

### Required Compliance

**For All Projects:**
- Secure credential storage
- Encrypted data transmission (HTTPS)
- Access control implementation
- Security logging and monitoring
- Incident response plan

**Based on Data Handled:**
- **GDPR** (EU users): Data privacy, right to deletion, breach notification
- **CCPA** (California users): Data disclosure, opt-out rights
- **HIPAA** (Healthcare): PHI protection, audit trails
- **PCI DSS** (Payment cards): Secure card handling, encryption
- **SOC 2** (B2B SaaS): Security, availability, confidentiality

### Security Documentation

**Required Documents:**
- Security policy and procedures
- Data classification and handling
- Incident response plan
- Access control policy
- Encryption standards
- Third-party security review results

---

**Security is everyone's responsibility. Follow these standards to build secure applications.**

---


# Git & Version Control Rules

<!-- Source: 101-git-standards.mdc -->

# Git Standards

## Gitignore Standards

### Required Entries

Every project `.gitignore` must include:

```gitignore
# Environment variables
.env
.env.local
.env.*.local

# Dependencies
node_modules/
__pycache__/
*.pyc
.Python
venv/
.venv/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Build outputs
dist/
build/
*.egg-info/
.next/
out/

# Logs
*.log
logs/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Testing
.coverage
coverage/
*.cover
.pytest_cache/
.vitest/

# OS
.DS_Store
Thumbs.db
```

## Commit Standards

### Conventional Commits Format

**Use Conventional Commits specification for all commit messages.**

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Commit Types

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Code style changes (formatting, missing semi-colons, etc)
- **refactor**: Code change that neither fixes a bug nor adds a feature
- **perf**: Performance improvements
- **test**: Adding or updating tests
- **build**: Changes to build system or dependencies
- **ci**: Changes to CI configuration files and scripts
- **chore**: Other changes that don't modify src or test files
- **revert**: Reverts a previous commit

### Commit Message Guidelines

#### Subject Line
- Use imperative mood: "add feature" not "added feature"
- Don't capitalize first letter
- No period at the end
- Limit to 50 characters
- Be specific and descriptive

#### Body (Optional)
- Separate from subject with blank line
- Explain what and why, not how
- Wrap at 72 characters
- Use bullet points for multiple changes

#### Footer (Optional)
- Reference issues: `Fixes #123`, `Closes #456`
- Note breaking changes: `BREAKING CHANGE: description`

### Examples

```bash
# Simple feature
feat(auth): add password reset functionality

# Bug fix with details
fix(api): resolve race condition in user creation

Race condition occurred when multiple requests created users
with the same email simultaneously. Added database constraint
and proper error handling.

Fixes #234

# Breaking change
feat(api): change authentication to use OAuth 2.0

BREAKING CHANGE: Previous API key authentication is no longer
supported. All clients must migrate to OAuth 2.0.

# Documentation
docs(readme): update installation instructions

# Multiple changes
chore: update dependencies

- Upgrade React to v18.2.0
- Update Next.js to v14.0.0
- Fix TypeScript errors from upgrades
```

## Branching Strategy

### Branch Naming Convention

```
<type>/<short-description>
```

**Types:**
- `feature/` - New features
- `fix/` - Bug fixes
- `hotfix/` - Urgent production fixes
- `refactor/` - Code refactoring
- `docs/` - Documentation updates
- `test/` - Test additions/updates
- `chore/` - Maintenance tasks

**Examples:**
```
feature/user-authentication
fix/login-validation-error
hotfix/security-vulnerability
refactor/database-queries
docs/api-documentation
```

### Branch Lifecycle

#### Main Branches
- **`main`** (or `master`) - Production-ready code
- **`develop`** - Integration branch for features (if using Git Flow)

#### Feature Development
```bash
# Create feature branch from main
git checkout -b feature/user-profile main

# Work on feature with regular commits
git add .
git commit -m "feat(profile): add user avatar upload"

# Keep branch updated with main
git fetch origin main
git rebase origin/main

# Push to remote
git push origin feature/user-profile
```

#### Hotfix Process
```bash
# Create hotfix from main
git checkout -b hotfix/critical-security-fix main

# Make fix
git add .
git commit -m "fix(security): patch XSS vulnerability"

# Merge to main AND develop
git checkout main
git merge --no-ff hotfix/critical-security-fix
git checkout develop
git merge --no-ff hotfix/critical-security-fix

# Tag the release
git tag -a v1.0.1 -m "Security patch"
```

## Pull Request Standards

### PR Title Format
Use same format as commit messages:
```
<type>(<scope>): <description>
```

### PR Description Template
```markdown
## Description
Brief description of what this PR does.

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Changes Made
- Change 1
- Change 2
- Change 3

## Testing
- [ ] Tests added/updated
- [ ] All tests passing
- [ ] Manual testing completed

## Screenshots (if applicable)
[Add screenshots here]

## Related Issues
Fixes #(issue number)
Relates to #(issue number)

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] No new warnings generated
```

### PR Best Practices

1. **Keep PRs small and focused** - One feature/fix per PR
2. **Update branch before creating PR** - Rebase on latest main
3. **Write clear description** - Explain what and why
4. **Add reviewers** - At least one reviewer required
5. **Respond to feedback** - Address all review comments
6. **Squash commits** (if configured) - Clean history in main

### PR Merge Strategy

**Choose one strategy per project:**

#### Squash and Merge (Recommended)
- Combines all commits into one
- Clean linear history
- Good for feature branches

#### Merge Commit
- Preserves all commits
- Creates merge commit
- Good for complex features

#### Rebase and Merge
- Linear history without merge commits
- Rewrites commit history
- Good for small changes

## Code Review Guidelines

### As a Reviewer

**Required Checks:**
- [ ] Code follows project standards and style guide
- [ ] Changes are well-tested
- [ ] No obvious bugs or security issues
- [ ] Documentation is updated
- [ ] Commit messages follow conventions
- [ ] No unnecessary files committed
- [ ] No secrets or sensitive data in code

**Review Checklist:**
- **Functionality**: Does it work as intended?
- **Code Quality**: Is it readable and maintainable?
- **Performance**: Any performance concerns?
- **Security**: Any security vulnerabilities?
- **Testing**: Are there adequate tests?
- **Documentation**: Is it properly documented?

### As an Author

**Before Requesting Review:**
- [ ] Self-review your own code
- [ ] Run all tests locally
- [ ] Update documentation
- [ ] Check for console logs/debug code
- [ ] Verify no merge conflicts
- [ ] Add descriptive PR description

**Responding to Feedback:**
- Thank reviewers for their time
- Ask questions if feedback is unclear
- Make requested changes promptly
- Mark conversations as resolved when addressed
- Request re-review after changes

## Git Workflow Best Practices

### Daily Workflow

```bash
# Start of day - update main
git checkout main
git pull origin main

# Create feature branch
git checkout -b feature/new-feature

# Regular commits during work
git add <files>
git commit -m "feat(scope): descriptive message"

# Before pushing - rebase on main
git fetch origin main
git rebase origin/main

# Push to remote
git push origin feature/new-feature

# Create pull request
# (Use GitHub/GitLab UI)
```

### Commit Hygiene

**Do:**
- Commit frequently with logical chunks
- Write descriptive commit messages
- Keep commits focused on single change
- Test before committing
- Review diff before committing

**Don't:**
- Commit commented-out code
- Commit debug/console logs
- Commit large binary files
- Commit secrets or credentials
- Mix unrelated changes in one commit

### Stashing Changes

```bash
# Save work in progress
git stash save "WIP: feature description"

# List stashes
git stash list

# Apply most recent stash
git stash apply

# Apply and remove stash
git stash pop

# Apply specific stash
git stash apply stash@{2}
```

## Git Hooks

### Recommended Pre-commit Hooks

```bash
# .git/hooks/pre-commit

#!/bin/sh

# Prevent commits to main
branch="$(git rev-parse --abbrev-ref HEAD)"
if [ "$branch" = "main" ]; then
  echo "Direct commits to main are not allowed"
  exit 1
fi

# Run linter
npm run lint || exit 1

# Run tests
npm test || exit 1
```

### Recommended Commit-msg Hook

```bash
# .git/hooks/commit-msg

#!/bin/sh

# Validate commit message format
commit_msg=$(cat "$1")
pattern="^(feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert)(\(.+\))?: .{1,50}"

if ! echo "$commit_msg" | grep -qE "$pattern"; then
  echo "Invalid commit message format"
  echo "Use: <type>(<scope>): <subject>"
  exit 1
fi
```

## Semantic Versioning Integration

### Version Tags

Follow semantic versioning when tagging releases:

```bash
# Major release (breaking changes)
git tag -a v2.0.0 -m "Major release with breaking changes"

# Minor release (new features)
git tag -a v1.1.0 -m "Add new features"

# Patch release (bug fixes)
git tag -a v1.0.1 -m "Bug fixes and improvements"

# Push tags
git push origin --tags
```

### Automatic Versioning

Use semantic-release or similar tools for automatic versioning based on commit messages (see versioning rules).

---

**Follow these Git standards for consistent, maintainable version control and collaboration.**

---


# Design & UX Rules

<!-- Source: 201-design-thinking-personas.mdc -->

# Design Thinking & User Persona Requirements

## Core Design Thinking Directive

**Every project MUST have at least one user persona defined before any development work begins.**

### User-Centered Approach
- **Empathize first** - Understand user needs before building solutions
- **Define problems clearly** - User personas guide problem definition
- **Validate assumptions** - Test solutions against defined user needs
- **Iterate based on user feedback** - Use personas to evaluate design decisions

## User Persona Requirements

### Mandatory Before Development
1. **Project plan must include user personas** in a dedicated section
2. **Pre-work analysis must verify persona completeness** before starting any milestone
3. **All feature decisions must reference relevant user personas**
4. **Testing and validation should consider persona needs**

### User Persona Template
Use this simplified format for every persona:

```markdown
### User Persona: [Persona Name]
- **Primary User**: [Brief description of user type and context]
- **Pain Points**: [List 2-4 key problems this user faces]
- **Goals**: [List 2-4 primary objectives this user wants to achieve]
- **Context**: [When/where/how they use the solution - optional]
```

## Integration with Project Workflow

### During Project Plan Creation
- **Alert user** if no personas are defined
- **Require at least one persona** before approving any project plan
- **Suggest persona research** if personas seem incomplete

### During Pre-Work Analysis
- **Verify persona alignment** - does the requested work serve defined users?
- **Flag feature requests** that don't align with any existing persona
- **Suggest persona updates** if new user types are discovered

### During Development
- **Reference personas** when making design/architecture decisions
- **Question implementations** that don't clearly benefit defined users
- **Suggest user testing** for features that significantly impact user experience

### During Post-Work Updates
- **Update personas** if new user insights are discovered
- **Note persona validation** results from user testing or feedback
- **Suggest new personas** if gaps in user coverage are identified

## Persona Quality Standards

### Complete Personas Include:
- ✅ **Specific user description** (not just "users" or "people")
- ✅ **Concrete pain points** (real problems, not assumptions)
- ✅ **Clear goals** (what success looks like for this user)
- ✅ **Actionable insights** (can guide design decisions)

### Avoid Generic Personas:
- ❌ "Users want the app to be fast" (too vague)
- ❌ "People need a good experience" (not specific)
- ❌ "Everyone wants it to work" (not actionable)

### Good Persona Examples:
```markdown
### User Persona: Busy Marketing Manager
- **Primary User**: Marketing managers at SMBs juggling multiple campaigns
- **Pain Points**: Context switching between tools, losing track of campaign performance, manual reporting
- **Goals**: Unified dashboard view, automated performance alerts, quick campaign adjustments

### User Persona: Junior Developer
- **Primary User**: Developers with 1-3 years experience learning new frameworks  
- **Pain Points**: Overwhelming documentation, unclear setup instructions, fear of breaking things
- **Goals**: Step-by-step guidance, safe experimentation environment, quick wins to build confidence
```

## Enforcement Protocol

### Missing Personas
If project plan lacks personas:
1. **Stop work immediately**
2. **Alert user to missing personas requirement**
3. **Offer to help create personas** based on project context
4. **Do not proceed** with development until personas are defined

### Incomplete Personas
If personas are too vague or generic:
1. **Flag quality issues** with specific feedback
2. **Suggest improvements** using the template
3. **Request user research** if personas seem assumption-based
4. **Proceed cautiously** while encouraging persona refinement

### Persona-Feature Misalignment
If requested work doesn't serve any defined persona:
1. **Question the value** of the requested feature
2. **Ask which persona** this serves
3. **Suggest persona updates** if new user type discovered
4. **Consider deferring work** until user value is clear

## Communication Templates

### Missing Personas Alert
```
🚨 **Design Thinking Requirement**
- **Issue**: No user personas defined in project plan
- **Impact**: Cannot validate user value of development work  
- **Required**: Define at least one user persona before proceeding
- **Template**: [Provide persona template]
```

### Persona Quality Feedback
```
📋 **Persona Quality Check**
- **Current**: [Quote existing persona]
- **Issues**: [Specific problems - too vague, not actionable, etc.]
- **Suggestions**: [Concrete improvements needed]
- **Template**: [Show improved version]
```

---

**Design thinking starts with understanding users. No development work should begin without clearly defined user personas.**

---


# Python Project Rules

<!-- Source: 301-virtual-environment-setup.mdc -->

1. Environment Setup
   - Use `uv` for all virtual environment operations
   - Create a virtual environment if none exists for the project
   - Use Python version specified in pyproject.toml
   - Keep virtual environment in .venv directory
   - Add .venv to .gitignore
   - Document Python version requirements

2. Package Management
   - Use `uv pip` for package installation
   - Use `uv pip compile` for dependency resolution
   - Use `uv pip sync` for environment synchronization
   - Use `uv pip freeze` for dependency export
   - Use `uv pip uninstall` for package removal
   - Use `uv pip list` for package listing

3. Dependency Management
   - Use pyproject.toml for project metadata
   - Use requirements.txt for deployment
   - Pin all dependencies to specific versions
   - Use dependency groups for development tools
   - Keep development dependencies separate
   - Document dependency update process

4. Environment Variables
   - Use python-dotenv for environment variables
   - Keep .env files out of version control
   - Document required environment variables
   - Use .env.example for documentation
   - Validate environment on startup
   - Use secure defaults

5. Development Tools
   - Install development tools in virtual environment
   - Use pre-commit for git hooks
   - Configure black, isort, flake8
   - Set up pytest configuration
   - Configure coverage reporting
   - Set up debugging tools

6. Best Practices
   - Activate virtual environment in shell
   - Use virtual environment in IDE
   - Keep virtual environment up to date
   - Document setup process
   - Use consistent Python version
   - Follow security best practices

---

<!-- Source: 302-python-code-standards.mdc -->

1. Code Style and Formatting
   - Use Black for code formatting (line length: 88)
   - Use isort for import sorting
   - Use flake8 for linting
   - Follow PEP 8 guidelines
   - Use type hints for all function parameters and return values
   - Use docstrings for all modules, classes, and functions (Google style)

2. Project Structure
   - Use src-layout for all projects:
     ```
     project/
     ├── src/
     │   └── package_name/
     │       ├── __init__.py
     │       └── module.py
     ├── tests/
     │   └── test_module.py
     ├── pyproject.toml
     ├── README.md
     └── .gitignore
     ```
   - Keep package names lowercase with underscores
   - Use absolute imports within the package
   - Separate test files mirror the source structure

3. Package Management
   - Use `uv` for all package management operations
   - Maintain dependencies in pyproject.toml
   - Pin all dependencies to specific versions
   - Use dependency groups for development tools
   - Keep requirements.txt for deployment (generated from pyproject.toml)

4. Code Organization
   - Keep functions small and focused (max 20 lines)
   - Use classes for complex state management
   - Use dataclasses for data containers
   - Use enums for constants
   - Use type aliases for complex types
   - Use pathlib for file operations
   - Use context managers for resource management

5. Error Handling
   - Use custom exceptions for domain-specific errors
   - Include meaningful error messages
   - Use context managers for cleanup
   - Log exceptions with appropriate context
   - Use typing.Optional for nullable values

6. Performance
   - Use list comprehensions over map/filter
   - Use generator expressions for large datasets
   - Use sets for membership testing
   - Use collections.defaultdict for counting
   - Profile code before optimization

7. Security
   - Never store secrets in code
   - Use environment variables for configuration
   - Validate all user input
   - Use parameterized queries for databases
   - Use secure defaults for all operations

8. Documentation
   - Write docstrings for all public APIs
   - Include examples in docstrings
   - Keep README.md up to date
   - Document all configuration options
   - Include type hints in all signatures

9. Best Practices
   - Use dataclasses for data containers
   - Use pathlib for file operations
   - Use typing.Protocol for interfaces
   - Use functools.lru_cache for expensive operations
   - Use asyncio for I/O-bound operations
   - Use multiprocessing for CPU-bound operations

---

<!-- Source: 303-python-testing-standards.mdc -->

1. Test Structure
   - Use pytest as the testing framework
   - Follow AAA pattern (Arrange, Act, Assert)
   - Keep tests independent and isolated
   - Use descriptive test names (test_should_do_something_when_condition)
   - Mirror source directory structure in tests
   - Use conftest.py for shared fixtures

2. Test Organization
   - Group related tests in classes
   - Use meaningful test class names
   - Keep test files focused and small
   - Use test categories (unit, integration, e2e)
   - Separate test data from test logic
   - Use test factories for complex objects

3. Test Coverage
   - Aim for 100% line coverage
   - Focus on branch coverage for critical paths
   - Use coverage.py for coverage reporting
   - Exclude test files from coverage
   - Document why code is excluded from coverage
   - Run coverage in CI/CD pipeline

4. Test Types
   - Unit Tests:
     - Test one thing at a time
     - Mock external dependencies
     - Test edge cases and error conditions
     - Keep tests fast and focused
   - Integration Tests:
     - Test component interactions
     - Use test databases
     - Clean up test data
     - Test real external services in staging
   - End-to-End Tests:
     - Test complete user flows
     - Use realistic test data
     - Test error recovery
     - Keep tests maintainable

5. Test Data
   - Use fixtures for common test data
   - Use factories for complex objects
   - Keep test data minimal
   - Use random data for edge cases
   - Clean up test data after tests
   - Use parameterized tests for multiple cases

6. Mocking and Stubbing
   - Use unittest.mock for mocking
   - Mock external services
   - Use dependency injection
   - Mock time-dependent operations
   - Use context managers for mocking
   - Reset mocks between tests

7. Performance Testing
   - Use pytest-benchmark for benchmarks
   - Test with realistic data volumes
   - Measure memory usage
   - Test concurrent operations
   - Profile slow tests
   - Keep performance tests separate

8. Test Documentation
   - Document test purpose
   - Explain complex test setups
   - Document test data requirements
   - Keep test documentation up to date
   - Use docstrings for test classes
   - Document test categories

9. CI/CD Integration
   - Run tests in CI pipeline
   - Fail on test failures
   - Generate coverage reports
   - Run different test types in parallel
   - Cache test dependencies
   - Use test matrices for different environments

10. Best Practices
    - Keep tests fast
    - Make tests reliable
    - Use meaningful assertions
    - Test error conditions
    - Use appropriate test doubles
    - Follow testing pyramid

---

<!-- Source: 304-test-organization.mdc -->

# Python Test Organization Standards

## Test File Classification

### File Types
- **Runnable Tests**: Standard pytest files that test actual functionality
- **Test Scripts**: Utility scripts that help with testing but aren't tests themselves
- **Test Utilities**: Helper modules and functions for testing
- **Test Data**: Sample data, fixtures, and test resources

### Organization Requirements
- **Runnable tests** go in `tests/` directory with standard naming
- **Test scripts** go in `tests/scripts/` directory
- **Test utilities** go in `tests/utils/` directory
- **Test data** goes in `tests/data/` directory
- **Clear naming conventions** to distinguish between types

## Directory Structure

### Standard Test Layout

```
project-root/
├── src/
│   └── myproject/
│       ├── __init__.py
│       ├── core.py
│       └── api.py
├── tests/
│   ├── __init__.py            # Makes tests a package
│   ├── conftest.py            # Pytest configuration and fixtures
│   ├── test_core.py           # Tests for core functionality
│   ├── test_api.py            # Tests for API endpoints
│   ├── test_integration.py    # Integration tests
│   ├── scripts/               # Test utility scripts
│   │   ├── setup_test_db.py
│   │   ├── generate_test_data.py
│   │   └── cleanup_test_env.py
│   ├── utils/                 # Test helper modules
│   │   ├── __init__.py
│   │   ├── factories.py
│   │   ├── fixtures.py
│   │   └── assertions.py
│   └── data/                  # Test data files
│       ├── sample_data.json
│       └── test_fixtures.yaml
└── pytest.ini
```

## Runnable Tests (`tests/`)

### Naming Convention
- Files: `test_*.py` or `*_test.py`
- Classes: `Test*` (e.g., `TestUserService`)
- Functions: `test_*` (e.g., `test_create_user`)

### Test File Structure

```python
# tests/test_user_service.py
"""Tests for user service functionality."""

import pytest
from myproject.services.user_service import UserService
from tests.utils.factories import UserFactory

class TestUserService:
    """Test suite for UserService."""

    @pytest.fixture
    def user_service(self):
        """Provide a user service instance."""
        return UserService()

    def test_create_user(self, user_service):
        """Test creating a new user."""
        user_data = UserFactory.build()
        user = user_service.create(user_data)

        assert user.id is not None
        assert user.email == user_data.email

    def test_create_user_with_duplicate_email(self, user_service):
        """Test that duplicate emails raise error."""
        user_data = UserFactory.build(email="test@example.com")
        user_service.create(user_data)

        with pytest.raises(ValueError, match="Email already exists"):
            user_service.create(user_data)

    @pytest.mark.parametrize("age,expected", [
        (17, False),
        (18, True),
        (25, True),
    ])
    def test_is_adult(self, age, expected):
        """Test adult age verification."""
        user = UserFactory.build(age=age)
        assert user.is_adult() == expected
```

### Test Organization Patterns

**Arrange-Act-Assert (AAA):**
```python
def test_user_creation():
    # Arrange
    user_data = {"email": "test@example.com", "name": "Test"}
    user_service = UserService()

    # Act
    user = user_service.create(user_data)

    # Assert
    assert user.email == "test@example.com"
    assert user.name == "Test"
```

**Given-When-Then (BDD):**
```python
def test_login_with_valid_credentials():
    # Given a user exists
    user = create_user(email="test@example.com", password="secret123")

    # When they attempt to login
    result = auth_service.login("test@example.com", "secret123")

    # Then login succeeds
    assert result.success is True
    assert result.token is not None
```

## Test Scripts (`tests/scripts/`)

### Purpose
Utility scripts that help with testing but aren't tests themselves:
- Database setup/teardown
- Test data generation
- Environment configuration
- Performance benchmarking
- Result validation

### Naming Convention
- Descriptive names **without** `test_` prefix
- Clear action verbs: `setup_`, `generate_`, `cleanup_`, `validate_`

### Example Scripts

```python
# tests/scripts/setup_test_db.py
"""Script to set up test database."""

import sys
from pathlib import Path
from myproject.database import Database

def setup_test_database():
    """Create and populate test database."""
    db = Database.connect(test_mode=True)
    db.create_tables()
    db.seed_data('tests/data/seed.sql')
    print("✅ Test database set up successfully")

if __name__ == "__main__":
    setup_test_database()
```

```python
# tests/scripts/generate_test_data.py
"""Generate sample test data."""

import json
from faker import Faker
from pathlib import Path

fake = Faker()

def generate_users(count=100):
    """Generate fake user data."""
    users = []
    for _ in range(count):
        users.append({
            "email": fake.email(),
            "name": fake.name(),
            "age": fake.random_int(18, 80),
        })

    output_file = Path("tests/data/users.json")
    output_file.parent.mkdir(exist_ok=True)
    output_file.write_text(json.dumps(users, indent=2))
    print(f"✅ Generated {count} users to {output_file}")

if __name__ == "__main__":
    generate_users(100)
```

## Test Data (`tests/data/`)

### Organization

```
tests/data/
├── fixtures/              # Static test fixtures
│   ├── users.json
│   └── products.json
├── snapshots/             # Snapshot test data
│   └── api_responses/
├── seeds/                 # Database seed files
│   └── test_seed.sql
└── samples/               # Sample files for testing
    ├── sample.pdf
    └── sample.csv
```

### Fixtures

```json
// tests/data/fixtures/users.json
[
  {
    "id": "1",
    "email": "admin@example.com",
    "role": "admin",
    "name": "Admin User"
  },
  {
    "id": "2",
    "email": "user@example.com",
    "role": "user",
    "name": "Regular User"
  }
]
```

```python
# tests/conftest.py - Loading fixtures
import json
import pytest
from pathlib import Path

@pytest.fixture
def user_fixtures():
    """Load user fixtures from JSON."""
    fixture_path = Path("tests/data/fixtures/users.json")
    return json.loads(fixture_path.read_text())

@pytest.fixture
def admin_user(user_fixtures):
    """Get admin user from fixtures."""
    return next(u for u in user_fixtures if u["role"] == "admin")
```

## conftest.py Configuration

### Shared Fixtures

```python
# tests/conftest.py
"""Pytest configuration and shared fixtures."""

import pytest
from myproject.database import Database
from myproject.app import create_app

@pytest.fixture(scope="session")
def app():
    """Create application instance."""
    return create_app(config="testing")

@pytest.fixture(scope="session")
def db():
    """Create database connection."""
    database = Database.connect(test_mode=True)
    database.create_tables()
    yield database
    database.drop_tables()
    database.disconnect()

@pytest.fixture
def client(app):
    """Create test client."""
    return app.test_client()

@pytest.fixture(autouse=True)
def reset_db(db):
    """Reset database before each test."""
    db.truncate_all_tables()
    yield
    db.truncate_all_tables()

# Pytest configuration
def pytest_configure(config):
    """Configure pytest."""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests"
    )
```

## pytest.ini Configuration

```ini
# pytest.ini
[pytest]
testpaths = tests
python_files = test_*.py *_test.py
python_classes = Test*
python_functions = test_*

# Markers
markers =
    unit: Unit tests
    integration: Integration tests
    slow: Slow-running tests
    smoke: Smoke tests

# Coverage
addopts =
    --strict-markers
    --cov=src/myproject
    --cov-report=term-missing
    --cov-report=html
    -v

# Warnings
filterwarnings =
    error
    ignore::DeprecationWarning
```

## Test Execution

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_user_service.py

# Run specific test
pytest tests/test_user_service.py::TestUserService::test_create_user

# Run with markers
pytest -m unit              # Only unit tests
pytest -m "not slow"        # Skip slow tests
pytest -m "integration"     # Only integration tests

# Run with coverage
pytest --cov=src/myproject --cov-report=html

# Run in parallel
pytest -n auto

# Run with verbose output
pytest -vv
```

### Running Scripts

```bash
# Run test setup scripts
python tests/scripts/setup_test_db.py
python tests/scripts/generate_test_data.py

# Run cleanup
python tests/scripts/cleanup_test_env.py
```

## Best Practices

### Test Isolation
- Each test should be independent
- Use fixtures to set up clean state
- Clean up after tests (databases, files, etc.)
- Avoid shared mutable state

### Test Naming
- Use descriptive names that explain what is being tested
- Include the expected outcome
- Follow pattern: `test_<action>_<expected_result>`

### Test Organization
- Group related tests in classes
- Use marks for categorization
- Keep test files focused on single module/feature
- Mirror source code structure

### Performance
- Keep unit tests fast (< 100ms each)
- Mark slow tests with `@pytest.mark.slow`
- Use test parallelization for large suites
- Mock external dependencies

---

**Organize tests systematically for maintainability and clarity.**

---

<!-- Source: 305-test-utilities.mdc -->

# Python Test Utilities Standards

## Test Utilities Directory (`tests/utils/`)

### Purpose
Helper modules and functions that support testing:
- Factory functions for creating test objects
- Custom assertions and matchers
- Test fixtures and mock builders
- Shared test helpers
- Custom pytest plugins

### Organization

```
tests/utils/
├── __init__.py           # Export commonly used utilities
├── factories.py          # Object factories
├── fixtures.py           # Reusable fixtures
├── assertions.py         # Custom assertions
├── mocks.py              # Mock builders
├── helpers.py            # Generic helpers
└── database.py           # Database test utilities
```

## Factory Pattern for Test Data

### Using factory_boy

```python
# tests/utils/factories.py
"""Test data factories."""

import factory
from factory.faker import Faker
from myproject.models import User, Post, Comment

class UserFactory(factory.Factory):
    """Factory for creating test users."""

    class Meta:
        model = User

    id = factory.Sequence(lambda n: n)
    email = Faker("email")
    name = Faker("name")
    age = Faker("random_int", min=18, max=80)
    is_active = True
    role = "user"
    created_at = Faker("date_time_this_year")

    @classmethod
    def admin(cls, **kwargs):
        """Create admin user."""
        return cls(role="admin", **kwargs)

    @classmethod
    def inactive(cls, **kwargs):
        """Create inactive user."""
        return cls(is_active=False, **kwargs)

class PostFactory(factory.Factory):
    """Factory for creating test posts."""

    class Meta:
        model = Post

    id = factory.Sequence(lambda n: n)
    title = Faker("sentence")
    content = Faker("text")
    author = factory.SubFactory(UserFactory)
    published = True
    created_at = Faker("date_time_this_month")

class CommentFactory(factory.Factory):
    """Factory for creating test comments."""

    class Meta:
        model = Comment

    id = factory.Sequence(lambda n: n)
    content = Faker("paragraph")
    post = factory.SubFactory(PostFactory)
    author = factory.SubFactory(UserFactory)
    created_at = Faker("date_time_this_week")
```

### Usage in Tests

```python
# tests/test_user_service.py
from tests.utils.factories import UserFactory, PostFactory

def test_create_user():
    # Build without saving
    user_data = UserFactory.build()
    assert user_data.id is not None

def test_user_posts():
    # Create with specific attributes
    user = UserFactory(email="test@example.com")

    # Create related objects
    posts = PostFactory.create_batch(3, author=user)
    assert len(posts) == 3
    assert all(p.author == user for p in posts)

def test_admin_permissions():
    # Use factory methods
    admin = UserFactory.admin()
    assert admin.role == "admin"

    regular_user = UserFactory()
    assert regular_user.role == "user"
```

### Custom Factory Builders

```python
# tests/utils/builders.py
"""Custom builders for complex test objects."""

from dataclasses import dataclass
from typing import Optional

@dataclass
class TestUserBuilder:
    """Builder for creating test users with fluent interface."""

    email: str = "test@example.com"
    name: str = "Test User"
    age: int = 25
    role: str = "user"
    is_active: bool = True

    def with_email(self, email: str) -> 'TestUserBuilder':
        self.email = email
        return self

    def with_name(self, name: str) -> 'TestUserBuilder':
        self.name = name
        return self

    def as_admin(self) -> 'TestUserBuilder':
        self.role = "admin"
        return self

    def inactive(self) -> 'TestUserBuilder':
        self.is_active = False
        return self

    def build(self) -> dict:
        """Build user data dictionary."""
        return {
            "email": self.email,
            "name": self.name,
            "age": self.age,
            "role": self.role,
            "is_active": self.is_active,
        }

# Usage
user_data = (TestUserBuilder()
    .with_email("admin@example.com")
    .with_name("Admin User")
    .as_admin()
    .build())
```

## Custom Assertions

### Assertion Helpers

```python
# tests/utils/assertions.py
"""Custom assertion helpers."""

from typing import Any, Dict, List
import json

def assert_valid_uuid(value: str) -> None:
    """Assert value is valid UUID."""
    import uuid
    try:
        uuid.UUID(value)
    except ValueError:
        raise AssertionError(f"{value} is not a valid UUID")

def assert_valid_email(email: str) -> None:
    """Assert email format is valid."""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise AssertionError(f"{email} is not a valid email")

def assert_datetime_recent(dt, max_age_seconds=60) -> None:
    """Assert datetime is recent (within max_age_seconds)."""
    from datetime import datetime, timedelta
    now = datetime.utcnow()
    age = (now - dt).total_seconds()
    if age > max_age_seconds:
        raise AssertionError(
            f"Datetime {dt} is {age}s old, expected < {max_age_seconds}s"
        )

def assert_contains_subset(subset: Dict, full: Dict) -> None:
    """Assert dictionary contains all keys/values from subset."""
    for key, value in subset.items():
        if key not in full:
            raise AssertionError(f"Key '{key}' not found in {full}")
        if full[key] != value:
            raise AssertionError(
                f"Key '{key}': expected {value}, got {full[key]}"
            )

def assert_json_equal(actual: str, expected: str) -> None:
    """Assert JSON strings are equal (ignoring formatting)."""
    actual_data = json.loads(actual)
    expected_data = json.loads(expected)
    if actual_data != expected_data:
        raise AssertionError(
            f"JSON mismatch:\nActual: {actual_data}\nExpected: {expected_data}"
        )

def assert_lists_equal_unordered(list1: List, list2: List) -> None:
    """Assert lists contain same elements regardless of order."""
    if sorted(list1) != sorted(list2):
        raise AssertionError(
            f"Lists not equal:\n{list1}\nvs\n{list2}"
        )
```

### Usage

```python
# tests/test_user_service.py
from tests.utils.assertions import (
    assert_valid_uuid,
    assert_valid_email,
    assert_datetime_recent,
    assert_contains_subset
)

def test_create_user():
    user = user_service.create({
        "email": "test@example.com",
        "name": "Test User"
    })

    assert_valid_uuid(user.id)
    assert_valid_email(user.email)
    assert_datetime_recent(user.created_at)
    assert_contains_subset(
        {"email": "test@example.com", "name": "Test User"},
        user.to_dict()
    )
```

## Mock Builders

### Reusable Mocks

```python
# tests/utils/mocks.py
"""Mock builders and helpers."""

from unittest.mock import Mock, MagicMock, AsyncMock
from typing import Any, Dict

class MockDatabaseBuilder:
    """Builder for database mocks."""

    def __init__(self):
        self.mock = Mock()
        self._setup_defaults()

    def _setup_defaults(self):
        """Set up default behaviors."""
        self.mock.connect.return_value = None
        self.mock.disconnect.return_value = None

    def with_query_result(self, result: Any):
        """Set query result."""
        self.mock.query.return_value = result
        return self

    def with_query_error(self, error: Exception):
        """Set query to raise error."""
        self.mock.query.side_effect = error
        return self

    def build(self) -> Mock:
        """Build the mock."""
        return self.mock

class MockApiClientBuilder:
    """Builder for API client mocks."""

    def __init__(self):
        self.mock = Mock()
        self._responses: Dict[str, Any] = {}

    def with_get_response(self, url: str, response: Dict):
        """Set GET response for URL."""
        def get_side_effect(request_url):
            if request_url == url:
                return response
            raise ValueError(f"Unexpected URL: {request_url}")

        self.mock.get.side_effect = get_side_effect
        return self

    def with_post_response(self, url: str, response: Dict):
        """Set POST response for URL."""
        self._responses[url] = response
        self.mock.post.return_value = response
        return self

    def build(self) -> Mock:
        """Build the mock."""
        return self.mock

# Usage
def test_database_query():
    db = (MockDatabaseBuilder()
        .with_query_result([{"id": 1, "name": "Test"}])
        .build())

    result = db.query("SELECT * FROM users")
    assert result == [{"id": 1, "name": "Test"}]
```

## Test Fixtures

### Reusable Fixtures

```python
# tests/utils/fixtures.py
"""Reusable test fixtures."""

import pytest
from typing import Generator
from myproject.database import Database

@pytest.fixture
def temp_file(tmp_path) -> Generator[str, None, None]:
    """Create temporary file."""
    file_path = tmp_path / "test_file.txt"
    file_path.write_text("test content")
    yield str(file_path)
    # Cleanup happens automatically with tmp_path

@pytest.fixture
def mock_time(monkeypatch):
    """Mock time.time() to return fixed value."""
    from datetime import datetime
    fixed_time = datetime(2024, 1, 1, 12, 0, 0)

    class MockDatetime:
        @staticmethod
        def now():
            return fixed_time

        @staticmethod
        def utcnow():
            return fixed_time

    monkeypatch.setattr("datetime.datetime", MockDatetime)
    return fixed_time

@pytest.fixture
def capture_logs():
    """Capture log messages."""
    import logging
    from io import StringIO

    log_stream = StringIO()
    handler = logging.StreamHandler(log_stream)
    handler.setLevel(logging.DEBUG)

    logger = logging.getLogger()
    logger.addHandler(handler)

    yield log_stream

    logger.removeHandler(handler)

@pytest.fixture
def env_vars(monkeypatch):
    """Set environment variables."""
    def set_env(**kwargs):
        for key, value in kwargs.items():
            monkeypatch.setenv(key, value)

    return set_env
```

## Database Test Utilities

### Database Helpers

```python
# tests/utils/database.py
"""Database testing utilities."""

from contextlib import contextmanager
from typing import Generator, Dict, Any
import pytest

class DatabaseTestHelper:
    """Helper for database testing."""

    def __init__(self, db):
        self.db = db

    def seed(self, table: str, data: list[dict]) -> None:
        """Seed table with data."""
        for row in data:
            self.db.insert(table, row)

    def truncate(self, *tables: str) -> None:
        """Truncate tables."""
        for table in tables:
            self.db.execute(f"TRUNCATE TABLE {table} CASCADE")

    def count(self, table: str, where: Dict = None) -> int:
        """Count rows in table."""
        query = f"SELECT COUNT(*) FROM {table}"
        if where:
            conditions = " AND ".join(f"{k} = %s" for k in where.keys())
            query += f" WHERE {conditions}"
            return self.db.query_one(query, tuple(where.values()))[0]
        return self.db.query_one(query)[0]

    @contextmanager
    def transaction(self) -> Generator:
        """Run test in transaction and rollback."""
        self.db.begin()
        try:
            yield
        finally:
            self.db.rollback()

@pytest.fixture
def db_helper(db):
    """Provide database helper."""
    return DatabaseTestHelper(db)

# Usage
def test_user_creation(db_helper):
    with db_helper.transaction():
        db_helper.seed("users", [
            {"email": "test@example.com", "name": "Test"}
        ])
        assert db_helper.count("users") == 1

        # Changes rolled back after test
```

## Test Helpers

### Generic Helpers

```python
# tests/utils/helpers.py
"""Generic test helper functions."""

from typing import Any, Callable
import time
import asyncio

def wait_until(
    condition: Callable[[], bool],
    timeout: float = 5.0,
    interval: float = 0.1
) -> bool:
    """Wait until condition is true or timeout."""
    start = time.time()
    while time.time() - start < timeout:
        if condition():
            return True
        time.sleep(interval)
    return False

async def wait_until_async(
    condition: Callable[[], bool],
    timeout: float = 5.0,
    interval: float = 0.1
) -> bool:
    """Async version of wait_until."""
    start = time.time()
    while time.time() - start < timeout:
        if await condition():
            return True
        await asyncio.sleep(interval)
    return False

def assert_raises_with_message(
    exception_type: type,
    message_substring: str
):
    """Context manager to assert exception with specific message."""
    import pytest
    with pytest.raises(exception_type) as exc_info:
        yield
    assert message_substring in str(exc_info.value)

def deep_merge_dicts(dict1: dict, dict2: dict) -> dict:
    """Deep merge two dictionaries."""
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge_dicts(result[key], value)
        else:
            result[key] = value
    return result

# Usage
def test_async_operation():
    result = None

    async def fetch_result():
        nonlocal result
        result = await some_async_function()

    asyncio.run(fetch_result())

    assert wait_until(lambda: result is not None, timeout=2.0)
    assert result == expected_value
```

## Best Practices

### Reusability
- Create generic utilities that can be used across tests
- Keep utilities focused on single responsibility
- Document expected usage with docstrings
- Export commonly used utilities from `__init__.py`

### Type Safety
- Use type hints for all utility functions
- Return concrete types, avoid `Any` when possible
- Use generics for flexible but type-safe utilities

### Maintainability
- Keep utilities simple and well-tested
- Avoid complex logic in test utilities
- Version control test utilities like production code
- Document breaking changes in utilities

### Performance
- Cache expensive operations
- Use lazy evaluation when appropriate
- Don't create heavy objects in module scope
- Clean up resources in fixtures

---

**Build reusable test utilities for efficient and maintainable testing.**

---


# Versioning & Release Rules

<!-- Source: 401-versioning-standards.mdc -->

# Versioning & Release Standards

## Core Directive

**Every project MUST use semantic-release for automated versioning and releases.**

### Why semantic-release?
- Automated version management based on conventional commits
- Automatic changelog generation
- Consistent release process across projects
- CI/CD integration
- Reduces human error in versioning

## Semantic Versioning (SemVer)

### Version Format
All projects use semantic versioning: `MAJOR.MINOR.PATCH`

- **MAJOR**: Breaking changes (not backward compatible)
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

### Version Numbering Rules
```
- Start with 0.1.0 for initial development
- Bug fix:        1.0.0 → 1.0.1 (PATCH)
- New feature:    1.0.1 → 1.1.0 (MINOR)
- Breaking change: 1.1.0 → 2.0.0 (MAJOR)
```

### Pre-release Labels
```
1.0.0-alpha.1    # Alpha releases
1.0.0-beta.1     # Beta releases
1.0.0-rc.1       # Release candidates
```

## semantic-release Setup (REQUIRED)

### Installation

```bash
# Install semantic-release and plugins
pnpm add -D semantic-release \
  @semantic-release/commit-analyzer \
  @semantic-release/release-notes-generator \
  @semantic-release/changelog \
  @semantic-release/github \
  @semantic-release/git \
  @semantic-release/npm
```

### Configuration

Create `.releaserc.json` in project root:

```json
{
  "branches": ["main"],
  "plugins": [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    [
      "@semantic-release/changelog",
      {
        "changelogFile": "CHANGELOG.md"
      }
    ],
    "@semantic-release/npm",
    [
      "@semantic-release/git",
      {
        "assets": ["CHANGELOG.md", "package.json"],
        "message": "chore(release): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}"
      }
    ],
    "@semantic-release/github"
  ]
}
```

### package.json Scripts

```json
{
  "scripts": {
    "release": "semantic-release",
    "release:dry": "semantic-release --dry-run"
  }
}
```

## Conventional Commits (REQUIRED)

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Commit Types & Version Impact

```
feat:     → MINOR version (new features)
fix:      → PATCH version (bug fixes)
docs:     → PATCH version (documentation)
style:    → PATCH version (formatting)
refactor: → PATCH version (code refactoring)
perf:     → PATCH version (performance)
test:     → PATCH version (tests)
chore:    → PATCH version (maintenance)
ci:       → PATCH version (CI config)
build:    → PATCH version (build system)

BREAKING CHANGE: → MAJOR version
```

### Examples

```bash
# Minor release (new feature)
feat(auth): add password reset functionality

# Patch release (bug fix)
fix(api): resolve race condition in user creation

Added database constraint to prevent duplicate user creation
when multiple requests arrive simultaneously.

Fixes #234

# Major release (breaking change)
feat(api): change authentication to use OAuth 2.0

BREAKING CHANGE: Previous API key authentication is no longer
supported. All clients must migrate to OAuth 2.0.

See migration guide: docs/oauth-migration.md

# Patch release (docs)
docs(readme): update installation instructions
```

## GitHub Actions Integration

### Release Workflow

Create `.github/workflows/release.yml`:

```yaml
name: Release

on:
  push:
    branches: [main]

permissions:
  contents: write
  issues: write
  pull-requests: write

jobs:
  release:
    name: Create Release
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0
          persist-credentials: false

      - name: Setup pnpm
        uses: pnpm/action-setup@v2
        with:
          version: 8

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 18
          cache: 'pnpm'

      - name: Install dependencies
        run: pnpm install --frozen-lockfile

      - name: Run tests
        run: pnpm test

      - name: Build
        run: pnpm build

      - name: Release
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          NPM_TOKEN: ${{ secrets.NPM_TOKEN }}
        run: pnpm release
```

### Environment Variables

**GitHub:**
- `GITHUB_TOKEN`: Automatically provided by GitHub Actions
- Use repository secrets for additional tokens

**NPM (if publishing):**
- `NPM_TOKEN`: Create at npmjs.com → Access Tokens
- Add as repository secret

## Release Process

### Automated Releases

1. **Developer creates feature**
   - Work on feature branch
   - Use conventional commits
   - Create pull request

2. **Code review & merge**
   - Review and approve PR
   - Squash and merge to main
   - Ensure commit message follows conventions

3. **Automatic release**
   - GitHub Actions runs on main push
   - semantic-release analyzes commits
   - Determines version bump
   - Updates CHANGELOG.md
   - Creates Git tag
   - Creates GitHub release
   - Publishes to NPM (if configured)

### Manual Release (Emergency)

```bash
# Dry run to preview release
pnpm release:dry

# Force release (use with caution)
npx semantic-release --no-ci
```

## Branch Strategy

### Main Branch
- **Protected**: Require PR and reviews
- **CI Required**: All checks must pass
- **Release Trigger**: Every push triggers release analysis

### Feature Branches
- Branch from: `main`
- Naming: `feat/feature-name`, `fix/bug-name`
- Merge: Squash and merge to main
- Delete after merge

### Hotfix Process
```bash
# Create hotfix branch from main
git checkout -b fix/critical-bug main

# Fix the issue
git commit -m "fix(critical): resolve security vulnerability"

# Create PR, get approval, merge to main
# semantic-release will handle the patch version
```

## Changelog Management

### Automatic Generation
semantic-release generates CHANGELOG.md from commits:

```markdown
# Changelog

## [2.1.0](https://github.com/user/repo/compare/v2.0.0...v2.1.0) (2024-01-15)

### Features

* **auth**: add password reset functionality ([abc123](https://github.com/user/repo/commit/abc123))

### Bug Fixes

* **api**: resolve race condition in user creation ([def456](https://github.com/user/repo/commit/def456))
```

### Manual Entries (Discouraged)
If necessary, add to CHANGELOG.md before version section:
```markdown
<!-- Manual entries go here, above automatic content -->
```

## Commit Message Enforcement

### Git Hooks (Recommended)

Install commitlint:
```bash
pnpm add -D @commitlint/config-conventional @commitlint/cli husky
```

Configure `.commitlintrc.json`:
```json
{
  "extends": ["@commitlint/config-conventional"],
  "rules": {
    "type-enum": [2, "always", [
      "feat", "fix", "docs", "style", "refactor",
      "perf", "test", "build", "ci", "chore", "revert"
    ]],
    "subject-case": [2, "never", ["upper-case"]],
    "subject-empty": [2, "never"],
    "subject-full-stop": [2, "never", "."],
    "header-max-length": [2, "always", 72]
  }
}
```

Setup husky:
```bash
npx husky-init
echo "npx --no -- commitlint --edit \$1" > .husky/commit-msg
```

### PR Title Validation

GitHub Action to validate PR titles (`.github/workflows/pr-title.yml`):

```yaml
name: PR Title Check

on:
  pull_request:
    types: [opened, edited, synchronize]

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: amannn/action-semantic-pull-request@v5
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## Best Practices

### Commit Discipline
- Write clear, descriptive commit messages
- One logical change per commit
- Use scope to indicate affected area
- Document breaking changes explicitly
- Reference issues in footer

### Version Strategy
- Let semantic-release handle all versioning
- Never manually edit version in package.json
- Use conventional commits consistently
- Review dry-run before important releases

### Release Management
- Monitor releases in GitHub Actions
- Review generated changelogs
- Test releases in staging before production
- Keep dependencies updated

### Troubleshooting
```bash
# Debug release process
pnpm release:dry --debug

# Check what would be released
npx semantic-release --dry-run

# Analyze commits
npx semantic-release-cli --analyze-commits
```

## Migration Guide

### Existing Projects

1. **Install semantic-release**
   ```bash
   pnpm add -D semantic-release @semantic-release/changelog @semantic-release/git
   ```

2. **Create .releaserc.json** with configuration above

3. **Update GitHub Actions** to use release workflow

4. **Tag current version**
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

5. **Enforce conventional commits** with commitlint

6. **Merge with conventional commit** to trigger first automated release

---

**Use semantic-release for all projects to ensure consistent, automated versioning and releases.**

---


# Node.js Project Rules

<!-- Source: 501-package-management.mdc -->

# Node.js Package Management

## Default Package Manager: pnpm

**Always use `pnpm` as the default package manager for Node.js projects.**

### Why pnpm?
- **Disk efficient**: Uses content-addressable storage, saves disk space
- **Fast**: Installs packages faster than npm/yarn
- **Strict**: Better dependency management with isolated node_modules
- **Monorepo support**: Excellent workspace support

## Installation & Setup

### Check if pnpm is installed
```bash
pnpm --version
```

### Install pnpm globally (if needed)
```bash
npm install -g pnpm
# or
curl -fsSL https://get.pnpm.io/install.sh | sh -
```

### Initialize new project
```bash
pnpm init
```

## Package Management Commands

### Installing Dependencies
```bash
# Install all dependencies
pnpm install

# Add a dependency
pnpm add <package>

# Add dev dependency
pnpm add -D <package>

# Add global package
pnpm add -g <package>

# Install specific version
pnpm add <package>@<version>
```

### Removing Dependencies
```bash
# Remove a package
pnpm remove <package>

# Remove dev dependency
pnpm remove -D <package>
```

### Updating Dependencies
```bash
# Update all dependencies
pnpm update

# Update specific package
pnpm update <package>

# Update to latest (including major)
pnpm update <package> --latest

# Interactive update
pnpm update --interactive
```

### Running Scripts
```bash
# Run package.json script
pnpm <script-name>

# Examples:
pnpm start
pnpm dev
pnpm test
pnpm build
```

## Project Configuration

### .npmrc Configuration
Create `.npmrc` in project root for pnpm settings:

```ini
# Use pnpm for this project
engine-strict=true

# Hoist patterns (if needed for compatibility)
shamefully-hoist=false

# Auto install peers
auto-install-peers=true

# Strict peer dependencies
strict-peer-dependencies=true
```

### package.json Engine Specification
Add to `package.json` to enforce pnpm:

```json
{
  "engines": {
    "node": ">=18.0.0",
    "pnpm": ">=8.0.0"
  },
  "packageManager": "pnpm@8.15.0"
}
```

### Add .npmrc to enforce pnpm
```ini
# .npmrc in project root
engine-strict=true
```

## Workspace Management (Monorepos)

### pnpm-workspace.yaml
For monorepo projects, create `pnpm-workspace.yaml`:

```yaml
packages:
  - 'packages/*'
  - 'apps/*'
  - '!**/test/**'
```

### Workspace Commands
```bash
# Install dependencies for all workspaces
pnpm install

# Run script in specific workspace
pnpm --filter <workspace-name> <script>

# Run script in all workspaces
pnpm -r <script>

# Add dependency to specific workspace
pnpm --filter <workspace-name> add <package>
```

## Lock File Management

### pnpm-lock.yaml
- **Always commit** `pnpm-lock.yaml` to version control
- Ensures reproducible installs across environments
- Contains exact dependency tree

### Lock File Operations
```bash
# Generate/update lock file
pnpm install

# Install from lock file only
pnpm install --frozen-lockfile

# Update lock file without installing
pnpm install --lockfile-only
```

## Migration from npm/yarn

### From npm
```bash
# Remove npm files
rm package-lock.json
rm -rf node_modules

# Install with pnpm
pnpm install

# Import from package-lock.json (if needed)
pnpm import
```

### From yarn
```bash
# Remove yarn files
rm yarn.lock
rm -rf node_modules

# Install with pnpm
pnpm install
```

## Best Practices

### 1. Lock File First
- Always run `pnpm install` before starting work
- Keep `pnpm-lock.yaml` up to date
- Use `--frozen-lockfile` in CI/CD

### 2. Dependency Auditing
```bash
# Check for vulnerabilities
pnpm audit

# Fix vulnerabilities
pnpm audit --fix
```

### 3. Clean Installation
```bash
# Remove node_modules and reinstall
rm -rf node_modules
pnpm install
```

### 4. List Dependencies
```bash
# List installed packages
pnpm list

# List outdated packages
pnpm outdated

# List dependency tree
pnpm list --depth=<level>
```

### 5. Script Execution
- Use `pnpm` instead of `npm run`
- Example: `pnpm dev` instead of `npm run dev`

## Troubleshooting

### Common Issues

**Issue**: Package not found in pnpm store
```bash
# Clear pnpm store and reinstall
pnpm store prune
pnpm install
```

**Issue**: Peer dependency conflicts
```bash
# Install with legacy peer deps handling
pnpm install --no-strict-peer-dependencies
```

**Issue**: Module resolution issues
```bash
# Use shamefully-hoist as last resort
echo "shamefully-hoist=true" >> .npmrc
pnpm install
```

## CI/CD Integration

### GitHub Actions
```yaml
- name: Setup pnpm
  uses: pnpm/action-setup@v2
  with:
    version: 8

- name: Setup Node.js
  uses: actions/setup-node@v3
  with:
    node-version: 18
    cache: 'pnpm'

- name: Install dependencies
  run: pnpm install --frozen-lockfile
```

### GitLab CI
```yaml
before_script:
  - curl -fsSL https://get.pnpm.io/install.sh | sh -
  - pnpm install --frozen-lockfile
```

---

**Use pnpm for all Node.js package management unless explicitly directed otherwise.**

---

<!-- Source: 502-nodejs-code-standards.mdc -->

# Node.js Code Standards

## Code Style & Formatting

### Use Modern JavaScript/TypeScript
- Prefer ES modules (`import/export`) over CommonJS (`require`)
- Use async/await over callbacks and raw Promises
- Leverage modern syntax (destructuring, spread, optional chaining)

### File Extensions
- `.js` - JavaScript (ESM or CommonJS based on package.json type)
- `.mjs` - Explicit ES module
- `.cjs` - Explicit CommonJS
- `.ts` - TypeScript
- `.d.ts` - TypeScript declarations

### Module System

#### ES Modules (Preferred)
```javascript
// package.json
{
  "type": "module"
}

// Import/Export
import { readFile } from 'fs/promises';
export const myFunction = () => {};
export default class MyClass {}
```

#### CommonJS (Legacy)
```javascript
// Only when necessary
const fs = require('fs');
module.exports = { myFunction };
```

## Project Structure

### Standard Directory Layout
```
project-root/
├── src/              # Source code
│   ├── index.js      # Main entry point
│   ├── routes/       # API routes
│   ├── controllers/  # Business logic
│   ├── models/       # Data models
│   ├── services/     # External services
│   ├── middleware/   # Express middleware
│   ├── utils/        # Utility functions
│   └── config/       # Configuration
├── tests/            # Test files
├── scripts/          # Build/deployment scripts
├── public/           # Static files (if applicable)
├── .env.example      # Environment template
├── package.json
├── pnpm-lock.yaml
└── README.md
```

### File Naming Conventions
- Use kebab-case for files: `user-controller.js`, `auth-middleware.js`
- Use PascalCase for classes: `UserService.js`, `DatabaseConnection.js`
- Use camelCase for utilities: `formatDate.js`, `validateEmail.js`

## Error Handling

### Always Handle Errors Properly

#### Async/Await Error Handling
```javascript
// Good
try {
  const data = await fetchData();
  return processData(data);
} catch (error) {
  logger.error('Failed to fetch data:', error);
  throw new AppError('Data fetch failed', 500);
}

// Avoid unhandled promises
async function riskyOperation() {
  // Always wrap in try-catch
  try {
    await database.query();
  } catch (error) {
    // Handle or rethrow
    throw error;
  }
}
```

#### Custom Error Classes
```javascript
class AppError extends Error {
  constructor(message, statusCode) {
    super(message);
    this.statusCode = statusCode;
    this.isOperational = true;
    Error.captureStackTrace(this, this.constructor);
  }
}

class ValidationError extends AppError {
  constructor(message) {
    super(message, 400);
  }
}
```

#### Express Error Middleware
```javascript
// Error handling middleware (last in chain)
app.use((err, req, res, next) => {
  logger.error(err);

  const statusCode = err.statusCode || 500;
  const message = err.isOperational ? err.message : 'Internal server error';

  res.status(statusCode).json({
    status: 'error',
    message,
    ...(process.env.NODE_ENV === 'development' && { stack: err.stack })
  });
});
```

### Process-Level Error Handling
```javascript
// Unhandled rejection
process.on('unhandledRejection', (reason, promise) => {
  logger.error('Unhandled Rejection at:', promise, 'reason:', reason);
  // Graceful shutdown
  process.exit(1);
});

// Uncaught exception
process.on('uncaughtException', (error) => {
  logger.error('Uncaught Exception:', error);
  // Graceful shutdown
  process.exit(1);
});
```

## Async Patterns

### Prefer Async/Await
```javascript
// Good
async function getUserData(userId) {
  const user = await User.findById(userId);
  const posts = await Post.findByUser(userId);
  return { user, posts };
}

// Avoid callback hell
function getUserData(userId, callback) {
  User.findById(userId, (err, user) => {
    if (err) return callback(err);
    Post.findByUser(userId, (err, posts) => {
      if (err) return callback(err);
      callback(null, { user, posts });
    });
  });
}
```

### Parallel Operations
```javascript
// Run independent operations in parallel
const [users, posts, comments] = await Promise.all([
  User.find(),
  Post.find(),
  Comment.find()
]);

// Use Promise.allSettled for non-critical operations
const results = await Promise.allSettled([
  fetchUserData(),
  fetchAnalytics(),
  fetchNotifications()
]);
```

## Environment & Configuration

### Use Environment Variables
```javascript
// Load from .env
import 'dotenv/config';

// Access environment variables
const config = {
  port: process.env.PORT || 3000,
  nodeEnv: process.env.NODE_ENV || 'development',
  database: {
    url: process.env.DATABASE_URL,
    poolSize: parseInt(process.env.DB_POOL_SIZE || '10')
  }
};

// Validate required env vars
const required = ['DATABASE_URL', 'JWT_SECRET'];
for (const key of required) {
  if (!process.env[key]) {
    throw new Error(`Missing required env var: ${key}`);
  }
}
```

### Configuration Module
```javascript
// config/index.js
export default {
  app: {
    port: process.env.PORT || 3000,
    env: process.env.NODE_ENV || 'development'
  },
  database: {
    url: process.env.DATABASE_URL,
    options: {
      maxPoolSize: 10,
      minPoolSize: 2
    }
  },
  jwt: {
    secret: process.env.JWT_SECRET,
    expiresIn: '7d'
  }
};
```

## Performance Best Practices

### 1. Stream Large Data
```javascript
// Good - streaming
import { createReadStream } from 'fs';
import { pipeline } from 'stream/promises';

await pipeline(
  createReadStream('large-file.txt'),
  transformStream,
  res
);

// Avoid - loading everything in memory
const data = await fs.readFile('large-file.txt');
res.send(data);
```

### 2. Proper Connection Pooling
```javascript
// Database connection pool
const pool = new Pool({
  max: 20,
  min: 5,
  idleTimeoutMillis: 30000
});

// Reuse connections
async function query(sql, params) {
  const client = await pool.connect();
  try {
    return await client.query(sql, params);
  } finally {
    client.release();
  }
}
```

### 3. Caching
```javascript
// Simple in-memory cache
const cache = new Map();

async function getCachedData(key, fetcher, ttl = 60000) {
  const cached = cache.get(key);
  if (cached && Date.now() - cached.timestamp < ttl) {
    return cached.data;
  }

  const data = await fetcher();
  cache.set(key, { data, timestamp: Date.now() });
  return data;
}
```

### 4. Avoid Blocking the Event Loop
```javascript
// Good - use worker threads for CPU-intensive tasks
import { Worker } from 'worker_threads';

function runInWorker(data) {
  return new Promise((resolve, reject) => {
    const worker = new Worker('./worker.js', { workerData: data });
    worker.on('message', resolve);
    worker.on('error', reject);
  });
}

// Avoid - blocking operations
function cpuIntensiveTask(data) {
  // This blocks the event loop
  for (let i = 0; i < 1e9; i++) {
    // heavy computation
  }
}
```

## Security Best Practices

### 1. Input Validation
```javascript
import Joi from 'joi';

const userSchema = Joi.object({
  email: Joi.string().email().required(),
  password: Joi.string().min(8).required(),
  age: Joi.number().integer().min(18)
});

async function createUser(req, res) {
  const { error, value } = userSchema.validate(req.body);
  if (error) {
    return res.status(400).json({ error: error.details[0].message });
  }
  // Use validated data
}
```

### 2. Sanitize User Input
```javascript
import sanitizeHtml from 'sanitize-html';

const clean = sanitizeHtml(userInput, {
  allowedTags: ['b', 'i', 'em', 'strong'],
  allowedAttributes: {}
});
```

### 3. Secure Headers
```javascript
import helmet from 'helmet';

app.use(helmet());
app.use(helmet.contentSecurityPolicy({
  directives: {
    defaultSrc: ["'self'"],
    styleSrc: ["'self'", "'unsafe-inline'"]
  }
}));
```

### 4. Rate Limiting
```javascript
import rateLimit from 'express-rate-limit';

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // limit each IP to 100 requests per windowMs
  message: 'Too many requests from this IP'
});

app.use('/api/', limiter);
```

## Logging

### Structured Logging
```javascript
import pino from 'pino';

const logger = pino({
  level: process.env.LOG_LEVEL || 'info',
  transport: {
    target: 'pino-pretty',
    options: { colorize: true }
  }
});

// Usage
logger.info({ userId, action: 'login' }, 'User logged in');
logger.error({ err, userId }, 'Failed to process request');
```

### Request Logging
```javascript
import pinoHttp from 'pino-http';

app.use(pinoHttp({ logger }));
```

## Testing Considerations

### Test File Location
- Place tests near source code or in `tests/` directory
- Name test files: `*.test.js` or `*.spec.js`
- Mirror source structure in test directory

### Test Database
- Use separate test database
- Clean up after each test
- Use transactions for isolation

---

**Follow these standards for consistent, maintainable Node.js code.**

---

<!-- Source: 503-nodejs-testing-standards.mdc -->

# Node.js Testing Standards

## Testing Framework

### Default: Vitest (Recommended)
**Use Vitest as the default testing framework for Node.js projects**

#### Why Vitest?
- Fast and lightweight
- Great TypeScript support
- Compatible with Jest API
- Built-in coverage
- ESM first

#### Installation
```bash
pnpm add -D vitest
```

#### Alternative: Jest
Use Jest for projects requiring:
- Extensive ecosystem compatibility
- Established patterns
- Legacy code compatibility

## Test File Organization

### Directory Structure
```
project-root/
├── src/
│   ├── users/
│   │   ├── user-service.js
│   │   └── user-service.test.js       # Co-located tests
│   └── utils/
│       ├── validators.js
│       └── validators.test.js
├── tests/                              # Integration/E2E tests
│   ├── integration/
│   │   └── api.test.js
│   ├── e2e/
│   │   └── user-flow.test.js
│   ├── fixtures/                       # Test data
│   │   └── users.json
│   └── helpers/                        # Test utilities
│       └── setup.js
└── vitest.config.js
```

### Test File Naming
- Unit tests: `<filename>.test.js` or `<filename>.spec.js`
- Integration tests: `<feature>.integration.test.js`
- E2E tests: `<flow>.e2e.test.js`

## Test Configuration

### vitest.config.js
```javascript
import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    globals: true,
    environment: 'node',
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html'],
      exclude: [
        'node_modules/',
        'tests/',
        '**/*.test.js',
        '**/*.config.js'
      ]
    },
    setupFiles: ['./tests/helpers/setup.js']
  }
});
```

### package.json Scripts
```json
{
  "scripts": {
    "test": "vitest",
    "test:unit": "vitest run --reporter=verbose",
    "test:watch": "vitest watch",
    "test:coverage": "vitest run --coverage",
    "test:ui": "vitest --ui",
    "test:integration": "vitest run tests/integration",
    "test:e2e": "vitest run tests/e2e"
  }
}
```

## Unit Testing Standards

### Test Structure
```javascript
import { describe, it, expect, beforeEach, afterEach } from 'vitest';
import { UserService } from './user-service.js';

describe('UserService', () => {
  let userService;

  beforeEach(() => {
    userService = new UserService();
  });

  afterEach(() => {
    // Cleanup
  });

  describe('createUser', () => {
    it('should create a user with valid data', async () => {
      const userData = { email: 'test@example.com', name: 'Test User' };
      const user = await userService.createUser(userData);

      expect(user).toBeDefined();
      expect(user.email).toBe(userData.email);
      expect(user.id).toBeDefined();
    });

    it('should throw error for invalid email', async () => {
      const userData = { email: 'invalid', name: 'Test' };

      await expect(userService.createUser(userData))
        .rejects
        .toThrow('Invalid email format');
    });

    it('should hash password before storing', async () => {
      const userData = {
        email: 'test@example.com',
        password: 'plain123'
      };
      const user = await userService.createUser(userData);

      expect(user.password).not.toBe('plain123');
      expect(user.password).toMatch(/^\$2[aby]\$/); // bcrypt hash pattern
    });
  });
});
```

### Assertion Best Practices
```javascript
// Be specific with assertions
expect(result).toBe(expected);           // Exact equality
expect(object).toEqual(expectedObject);  // Deep equality
expect(array).toHaveLength(3);
expect(string).toContain('substring');
expect(number).toBeGreaterThan(0);
expect(fn).toThrow(ErrorClass);

// Use custom matchers for clarity
expect(user).toMatchObject({
  email: expect.stringContaining('@'),
  createdAt: expect.any(Date)
});
```

## Mocking & Stubbing

### Module Mocking with Vitest
```javascript
import { vi } from 'vitest';
import { sendEmail } from './email-service.js';

// Mock entire module
vi.mock('./email-service.js', () => ({
  sendEmail: vi.fn()
}));

describe('User Registration', () => {
  it('should send welcome email', async () => {
    sendEmail.mockResolvedValue({ success: true });

    await registerUser({ email: 'test@example.com' });

    expect(sendEmail).toHaveBeenCalledWith({
      to: 'test@example.com',
      template: 'welcome'
    });
  });
});
```

### Spying on Functions
```javascript
import { vi } from 'vitest';

describe('Logger', () => {
  it('should log errors', () => {
    const consoleSpy = vi.spyOn(console, 'error');

    logger.error('Test error');

    expect(consoleSpy).toHaveBeenCalledWith(
      expect.stringContaining('Test error')
    );

    consoleSpy.mockRestore();
  });
});
```

### Database Mocking
```javascript
import { vi } from 'vitest';

// Mock database module
vi.mock('./database.js', () => ({
  default: {
    query: vi.fn(),
    connect: vi.fn(),
    disconnect: vi.fn()
  }
}));

describe('User Repository', () => {
  it('should query users from database', async () => {
    const mockUsers = [{ id: 1, name: 'John' }];
    db.query.mockResolvedValue(mockUsers);

    const users = await userRepository.findAll();

    expect(db.query).toHaveBeenCalledWith('SELECT * FROM users');
    expect(users).toEqual(mockUsers);
  });
});
```

## Integration Testing

### API Testing
```javascript
import { describe, it, expect, beforeAll, afterAll } from 'vitest';
import request from 'supertest';
import { app } from '../src/app.js';
import { setupTestDB, teardownTestDB } from './helpers/db.js';

describe('User API', () => {
  beforeAll(async () => {
    await setupTestDB();
  });

  afterAll(async () => {
    await teardownTestDB();
  });

  describe('POST /api/users', () => {
    it('should create a new user', async () => {
      const response = await request(app)
        .post('/api/users')
        .send({
          email: 'test@example.com',
          password: 'password123'
        })
        .expect(201);

      expect(response.body).toMatchObject({
        email: 'test@example.com',
        id: expect.any(String)
      });
      expect(response.body.password).toBeUndefined();
    });

    it('should return 400 for invalid data', async () => {
      const response = await request(app)
        .post('/api/users')
        .send({ email: 'invalid' })
        .expect(400);

      expect(response.body.error).toBeDefined();
    });
  });
});
```

### Test Database Setup
```javascript
// tests/helpers/db.js
import { MongoMemoryServer } from 'mongodb-memory-server';
import mongoose from 'mongoose';

let mongoServer;

export async function setupTestDB() {
  mongoServer = await MongoMemoryServer.create();
  const uri = mongoServer.getUri();
  await mongoose.connect(uri);
}

export async function teardownTestDB() {
  await mongoose.connection.dropDatabase();
  await mongoose.connection.close();
  await mongoServer.stop();
}

export async function clearTestDB() {
  const collections = mongoose.connection.collections;
  for (const key in collections) {
    await collections[key].deleteMany();
  }
}
```

## E2E Testing

### Using Playwright (for web apps)
```javascript
import { test, expect } from '@playwright/test';

test.describe('User Authentication', () => {
  test('should login successfully', async ({ page }) => {
    await page.goto('http://localhost:3000/login');

    await page.fill('[name="email"]', 'test@example.com');
    await page.fill('[name="password"]', 'password123');
    await page.click('button[type="submit"]');

    await expect(page).toHaveURL(/dashboard/);
    await expect(page.locator('.user-name')).toContainText('Test User');
  });
});
```

## Test Data Management

### Fixtures
```javascript
// tests/fixtures/users.json
{
  "validUser": {
    "email": "user@example.com",
    "name": "Test User",
    "role": "user"
  },
  "adminUser": {
    "email": "admin@example.com",
    "name": "Admin User",
    "role": "admin"
  }
}
```

### Factory Functions
```javascript
// tests/helpers/factories.js
let userIdCounter = 1;

export function createUser(overrides = {}) {
  return {
    id: userIdCounter++,
    email: `user${userIdCounter}@example.com`,
    name: 'Test User',
    createdAt: new Date(),
    ...overrides
  };
}

export function createUsers(count, overrides = {}) {
  return Array.from({ length: count }, () => createUser(overrides));
}
```

## Coverage Requirements

### Minimum Coverage Targets
- **Statements**: 80%
- **Branches**: 75%
- **Functions**: 80%
- **Lines**: 80%

### Critical Code Coverage
- **100% coverage required** for:
  - Authentication logic
  - Payment processing
  - Security-sensitive code
  - Data validation

### Running Coverage
```bash
# Generate coverage report
pnpm test:coverage

# View HTML report
open coverage/index.html
```

## Test Best Practices

### 1. Test Naming
```javascript
// Good - descriptive and specific
it('should return 404 when user does not exist', () => {});
it('should hash password with bcrypt before saving', () => {});

// Avoid - vague or generic
it('should work', () => {});
it('test user creation', () => {});
```

### 2. Arrange-Act-Assert Pattern
```javascript
it('should calculate total price with tax', () => {
  // Arrange
  const items = [{ price: 10 }, { price: 20 }];
  const taxRate = 0.1;

  // Act
  const total = calculateTotal(items, taxRate);

  // Assert
  expect(total).toBe(33); // (10 + 20) * 1.1
});
```

### 3. Test Isolation
```javascript
// Each test should be independent
describe('User Service', () => {
  let userService;

  beforeEach(() => {
    // Fresh instance for each test
    userService = new UserService();
  });

  it('test 1', () => {
    // This test doesn't affect others
  });

  it('test 2', () => {
    // Independent from test 1
  });
});
```

### 4. Avoid Test Interdependence
```javascript
// Bad - tests depend on execution order
it('should create user', () => {
  user = createUser();
});

it('should update user', () => {
  updateUser(user); // Depends on previous test
});

// Good - each test stands alone
it('should update user', () => {
  const user = createUser();
  updateUser(user);
  // Test is self-contained
});
```

### 5. Test Edge Cases
```javascript
describe('divide', () => {
  it('should divide positive numbers', () => {
    expect(divide(10, 2)).toBe(5);
  });

  it('should handle division by zero', () => {
    expect(() => divide(10, 0)).toThrow('Division by zero');
  });

  it('should handle negative numbers', () => {
    expect(divide(-10, 2)).toBe(-5);
  });

  it('should handle decimal results', () => {
    expect(divide(10, 3)).toBeCloseTo(3.333, 2);
  });
});
```

## Continuous Integration

### GitHub Actions
```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - uses: pnpm/action-setup@v2
        with:
          version: 8

      - uses: actions/setup-node@v3
        with:
          node-version: 18
          cache: 'pnpm'

      - name: Install dependencies
        run: pnpm install --frozen-lockfile

      - name: Run tests
        run: pnpm test:coverage

      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage/coverage-final.json
```

---

**Write comprehensive tests following these standards for reliable Node.js applications.**

---

<!-- Source: 504-express-api-standards.mdc -->

# Express.js API Standards

## Project Structure

### Standard Express App Structure
```
src/
├── app.js                 # Express app configuration
├── server.js              # Server startup
├── routes/                # Route definitions
│   ├── index.js          # Route aggregator
│   ├── users.js
│   └── auth.js
├── controllers/           # Request handlers
│   ├── user-controller.js
│   └── auth-controller.js
├── middleware/            # Custom middleware
│   ├── auth.js
│   ├── error-handler.js
│   └── validation.js
├── services/              # Business logic
│   ├── user-service.js
│   └── email-service.js
├── models/                # Data models
│   └── user.js
├── utils/                 # Utilities
│   ├── logger.js
│   └── response.js
└── config/                # Configuration
    └── index.js
```

## Application Setup

### app.js - Express Configuration
```javascript
import express from 'express';
import helmet from 'helmet';
import cors from 'cors';
import compression from 'compression';
import routes from './routes/index.js';
import { errorHandler } from './middleware/error-handler.js';
import { requestLogger } from './middleware/logger.js';

const app = express();

// Security middleware
app.use(helmet());
app.use(cors({
  origin: process.env.ALLOWED_ORIGINS?.split(',') || '*',
  credentials: true
}));

// Body parsing
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true, limit: '10mb' }));

// Compression
app.use(compression());

// Logging
app.use(requestLogger);

// Health check
app.get('/health', (req, res) => {
  res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

// API routes
app.use('/api', routes);

// 404 handler
app.use('*', (req, res) => {
  res.status(404).json({ error: 'Route not found' });
});

// Error handling (must be last)
app.use(errorHandler);

export default app;
```

### server.js - Server Startup
```javascript
import app from './app.js';
import { logger } from './utils/logger.js';
import { connectDatabase } from './config/database.js';

const PORT = process.env.PORT || 3000;

async function startServer() {
  try {
    // Connect to database
    await connectDatabase();
    logger.info('Database connected');

    // Start server
    const server = app.listen(PORT, () => {
      logger.info(`Server running on port ${PORT}`);
      logger.info(`Environment: ${process.env.NODE_ENV}`);
    });

    // Graceful shutdown
    process.on('SIGTERM', () => {
      logger.info('SIGTERM received, shutting down gracefully');
      server.close(() => {
        logger.info('Server closed');
        process.exit(0);
      });
    });

  } catch (error) {
    logger.error('Failed to start server:', error);
    process.exit(1);
  }
}

startServer();
```

## Routing Standards

### Route Organization
```javascript
// routes/index.js - Route aggregator
import { Router } from 'express';
import userRoutes from './users.js';
import authRoutes from './auth.js';

const router = Router();

router.use('/users', userRoutes);
router.use('/auth', authRoutes);

export default router;
```

### Route Definition
```javascript
// routes/users.js
import { Router } from 'express';
import * as userController from '../controllers/user-controller.js';
import { authenticate } from '../middleware/auth.js';
import { validate } from '../middleware/validation.js';
import { userSchemas } from '../schemas/user.js';

const router = Router();

// Public routes
router.post(
  '/register',
  validate(userSchemas.register),
  userController.register
);

// Protected routes
router.use(authenticate); // Apply auth to all routes below

router.get('/', userController.getUsers);
router.get('/:id', userController.getUserById);
router.put(
  '/:id',
  validate(userSchemas.update),
  userController.updateUser
);
router.delete('/:id', userController.deleteUser);

export default router;
```

### RESTful Route Patterns
```javascript
// Resource-based routing
GET    /api/users          # List users
POST   /api/users          # Create user
GET    /api/users/:id      # Get user
PUT    /api/users/:id      # Update user
PATCH  /api/users/:id      # Partial update
DELETE /api/users/:id      # Delete user

// Nested resources
GET    /api/users/:id/posts           # Get user's posts
POST   /api/users/:id/posts           # Create post for user
GET    /api/users/:id/posts/:postId   # Get specific post

// Actions (when REST doesn't fit)
POST   /api/users/:id/activate        # Activate user
POST   /api/users/:id/reset-password  # Reset password
```

## Controller Standards

### Controller Structure
```javascript
// controllers/user-controller.js
import * as userService from '../services/user-service.js';
import { AppError } from '../utils/errors.js';
import { successResponse } from '../utils/response.js';

export async function getUsers(req, res, next) {
  try {
    const { page = 1, limit = 10, search } = req.query;

    const result = await userService.getUsers({
      page: parseInt(page),
      limit: parseInt(limit),
      search
    });

    res.json(successResponse(result));
  } catch (error) {
    next(error);
  }
}

export async function getUserById(req, res, next) {
  try {
    const { id } = req.params;
    const user = await userService.getUserById(id);

    if (!user) {
      throw new AppError('User not found', 404);
    }

    res.json(successResponse(user));
  } catch (error) {
    next(error);
  }
}

export async function createUser(req, res, next) {
  try {
    const user = await userService.createUser(req.body);
    res.status(201).json(successResponse(user, 'User created successfully'));
  } catch (error) {
    next(error);
  }
}

export async function updateUser(req, res, next) {
  try {
    const { id } = req.params;
    const user = await userService.updateUser(id, req.body);

    if (!user) {
      throw new AppError('User not found', 404);
    }

    res.json(successResponse(user, 'User updated successfully'));
  } catch (error) {
    next(error);
  }
}

export async function deleteUser(req, res, next) {
  try {
    const { id } = req.params;
    await userService.deleteUser(id);
    res.status(204).send();
  } catch (error) {
    next(error);
  }
}
```

## Middleware Standards

### Authentication Middleware
```javascript
// middleware/auth.js
import jwt from 'jsonwebtoken';
import { AppError } from '../utils/errors.js';

export async function authenticate(req, res, next) {
  try {
    const token = req.headers.authorization?.replace('Bearer ', '');

    if (!token) {
      throw new AppError('Authentication required', 401);
    }

    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded;
    next();
  } catch (error) {
    if (error.name === 'JsonWebTokenError') {
      next(new AppError('Invalid token', 401));
    } else if (error.name === 'TokenExpiredError') {
      next(new AppError('Token expired', 401));
    } else {
      next(error);
    }
  }
}

export function authorize(...roles) {
  return (req, res, next) => {
    if (!roles.includes(req.user.role)) {
      return next(new AppError('Insufficient permissions', 403));
    }
    next();
  };
}
```

### Validation Middleware
```javascript
// middleware/validation.js
import { AppError } from '../utils/errors.js';

export function validate(schema) {
  return async (req, res, next) => {
    try {
      const validated = await schema.validateAsync(req.body, {
        abortEarly: false,
        stripUnknown: true
      });
      req.body = validated;
      next();
    } catch (error) {
      const errors = error.details.map(detail => ({
        field: detail.path.join('.'),
        message: detail.message
      }));
      next(new AppError('Validation failed', 400, { errors }));
    }
  };
}
```

### Error Handler Middleware
```javascript
// middleware/error-handler.js
import { logger } from '../utils/logger.js';

export function errorHandler(err, req, res, next) {
  // Log error
  logger.error({
    message: err.message,
    stack: err.stack,
    url: req.url,
    method: req.method,
    user: req.user?.id
  });

  // Operational errors (known errors)
  if (err.isOperational) {
    return res.status(err.statusCode).json({
      status: 'error',
      message: err.message,
      ...(err.data && { data: err.data })
    });
  }

  // Programming errors (unknown errors)
  // Don't leak error details in production
  const message = process.env.NODE_ENV === 'production'
    ? 'Internal server error'
    : err.message;

  res.status(500).json({
    status: 'error',
    message,
    ...(process.env.NODE_ENV === 'development' && { stack: err.stack })
  });
}
```

### Request Logger Middleware
```javascript
// middleware/logger.js
import { logger } from '../utils/logger.js';

export function requestLogger(req, res, next) {
  const start = Date.now();

  res.on('finish', () => {
    const duration = Date.now() - start;
    logger.info({
      method: req.method,
      url: req.url,
      status: res.statusCode,
      duration: `${duration}ms`,
      ip: req.ip,
      userAgent: req.get('user-agent')
    });
  });

  next();
}
```

## Response Standards

### Standardized Response Format
```javascript
// utils/response.js
export function successResponse(data, message = 'Success') {
  return {
    status: 'success',
    message,
    data
  };
}

export function paginatedResponse(items, page, limit, total) {
  return {
    status: 'success',
    data: items,
    pagination: {
      page,
      limit,
      total,
      pages: Math.ceil(total / limit)
    }
  };
}
```

### Error Response Format
```javascript
// utils/errors.js
export class AppError extends Error {
  constructor(message, statusCode = 500, data = null) {
    super(message);
    this.statusCode = statusCode;
    this.isOperational = true;
    this.data = data;
    Error.captureStackTrace(this, this.constructor);
  }
}

export class ValidationError extends AppError {
  constructor(errors) {
    super('Validation failed', 400, { errors });
  }
}

export class NotFoundError extends AppError {
  constructor(resource) {
    super(`${resource} not found`, 404);
  }
}

export class UnauthorizedError extends AppError {
  constructor(message = 'Unauthorized') {
    super(message, 401);
  }
}
```

## API Best Practices

### 1. Versioning
```javascript
// Version in URL
app.use('/api/v1', routesV1);
app.use('/api/v2', routesV2);

// Or version in headers
app.use((req, res, next) => {
  const version = req.get('API-Version') || '1';
  req.apiVersion = version;
  next();
});
```

### 2. Rate Limiting
```javascript
import rateLimit from 'express-rate-limit';

const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100,
  message: 'Too many requests, please try again later'
});

app.use('/api/', apiLimiter);
```

### 3. Request Validation
```javascript
import Joi from 'joi';

export const userSchemas = {
  register: Joi.object({
    email: Joi.string().email().required(),
    password: Joi.string().min(8).required(),
    name: Joi.string().min(2).max(100).required()
  }),

  update: Joi.object({
    email: Joi.string().email(),
    name: Joi.string().min(2).max(100)
  }).min(1) // At least one field required
};
```

### 4. CORS Configuration
```javascript
const corsOptions = {
  origin: (origin, callback) => {
    const allowedOrigins = process.env.ALLOWED_ORIGINS?.split(',') || [];
    if (!origin || allowedOrigins.includes(origin)) {
      callback(null, true);
    } else {
      callback(new Error('Not allowed by CORS'));
    }
  },
  credentials: true,
  optionsSuccessStatus: 200
};

app.use(cors(corsOptions));
```

### 5. Async Handler Wrapper
```javascript
// utils/async-handler.js
export const asyncHandler = (fn) => (req, res, next) => {
  Promise.resolve(fn(req, res, next)).catch(next);
};

// Usage
router.get('/users', asyncHandler(async (req, res) => {
  const users = await userService.getUsers();
  res.json(successResponse(users));
}));
```

---

**Follow these Express.js standards for consistent, maintainable API development.**

---

<!-- Source: 505-nextjs-vercel-standards.mdc -->

# Next.js & Vercel Standards

## Framework: Next.js

**Use Next.js as the preferred React framework for Node.js web applications**

### Why Next.js?
- Server-side rendering (SSR) and static site generation (SSG)
- App Router with React Server Components
- Built-in API routes
- Optimized performance and SEO
- Excellent developer experience

## Project Structure

### App Router Structure (Next.js 13+)
```
project-root/
├── app/
│   ├── layout.tsx              # Root layout
│   ├── page.tsx                # Home page
│   ├── error.tsx               # Error boundary
│   ├── loading.tsx             # Loading UI
│   ├── not-found.tsx           # 404 page
│   ├── (auth)/                 # Route group (no URL segment)
│   │   ├── login/
│   │   │   └── page.tsx
│   │   └── register/
│   │       └── page.tsx
│   ├── dashboard/
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   └── settings/
│   │       └── page.tsx
│   └── api/                    # API routes
│       ├── auth/
│       │   └── route.ts
│       └── users/
│           └── route.ts
├── components/
│   ├── ui/                     # Reusable UI components
│   ├── forms/                  # Form components
│   └── layouts/                # Layout components
├── lib/
│   ├── auth.ts                 # Auth utilities
│   ├── db.ts                   # Database client
│   └── utils.ts                # Utilities
├── public/                     # Static files
├── styles/                     # Global styles
├── next.config.mjs
├── middleware.ts               # Edge middleware
└── package.json
```

### File Naming Conventions
- **Pages**: `page.tsx` (App Router) or `index.tsx` (Pages Router)
- **Layouts**: `layout.tsx`
- **Loading States**: `loading.tsx`
- **Error Boundaries**: `error.tsx`
- **API Routes**: `route.ts`
- **Components**: `ComponentName.tsx` (PascalCase)

## Next.js Configuration

### next.config.mjs
```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,

  // Image optimization
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: '**.vercel.app',
      },
    ],
    formats: ['image/avif', 'image/webp'],
  },

  // Environment variables exposed to browser
  env: {
    NEXT_PUBLIC_APP_URL: process.env.NEXT_PUBLIC_APP_URL,
  },

  // Redirects
  async redirects() {
    return [
      {
        source: '/home',
        destination: '/',
        permanent: true,
      },
    ];
  },

  // Headers
  async headers() {
    return [
      {
        source: '/:path*',
        headers: [
          {
            key: 'X-Frame-Options',
            value: 'DENY',
          },
          {
            key: 'X-Content-Type-Options',
            value: 'nosniff',
          },
        ],
      },
    ];
  },
};

export default nextConfig;
```

## Server & Client Components

### Server Components (Default)
```typescript
// app/dashboard/page.tsx
// Server Component - runs on server, no 'use client' needed
import { getUser } from '@/lib/auth';
import { getUserData } from '@/lib/db';

export default async function DashboardPage() {
  const user = await getUser();
  const data = await getUserData(user.id);

  return (
    <div>
      <h1>Welcome {user.name}</h1>
      <UserData data={data} />
    </div>
  );
}
```

### Client Components
```typescript
// components/InteractiveButton.tsx
'use client'; // Required for client-side interactivity

import { useState } from 'react';

export function InteractiveButton() {
  const [count, setCount] = useState(0);

  return (
    <button onClick={() => setCount(count + 1)}>
      Clicked {count} times
    </button>
  );
}
```

### Component Composition Pattern
```typescript
// app/dashboard/page.tsx (Server Component)
import { ClientSidebar } from '@/components/ClientSidebar';

export default async function DashboardPage() {
  const data = await fetchData(); // Server-side data fetching

  return (
    <div>
      {/* Pass server-fetched data to client component */}
      <ClientSidebar initialData={data} />
    </div>
  );
}
```

## API Routes

### App Router API Routes
```typescript
// app/api/users/route.ts
import { NextRequest, NextResponse } from 'next/server';
import { getAuth } from '@/lib/auth';

export async function GET(request: NextRequest) {
  try {
    const auth = await getAuth(request);
    const users = await db.user.findMany();

    return NextResponse.json({ users });
  } catch (error) {
    return NextResponse.json(
      { error: 'Internal server error' },
      { status: 500 }
    );
  }
}

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const user = await db.user.create({ data: body });

    return NextResponse.json({ user }, { status: 201 });
  } catch (error) {
    return NextResponse.json(
      { error: 'Failed to create user' },
      { status: 400 }
    );
  }
}
```

### Dynamic API Routes
```typescript
// app/api/users/[id]/route.ts
import { NextRequest, NextResponse } from 'next/server';

export async function GET(
  request: NextRequest,
  { params }: { params: { id: string } }
) {
  const user = await db.user.findUnique({
    where: { id: params.id }
  });

  if (!user) {
    return NextResponse.json(
      { error: 'User not found' },
      { status: 404 }
    );
  }

  return NextResponse.json({ user });
}
```

## Middleware

### Edge Middleware
```typescript
// middleware.ts
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';
import { getToken } from '@/lib/auth';

export async function middleware(request: NextRequest) {
  const token = await getToken(request);

  // Protect dashboard routes
  if (request.nextUrl.pathname.startsWith('/dashboard')) {
    if (!token) {
      return NextResponse.redirect(new URL('/login', request.url));
    }
  }

  // Redirect authenticated users away from auth pages
  if (request.nextUrl.pathname.startsWith('/login')) {
    if (token) {
      return NextResponse.redirect(new URL('/dashboard', request.url));
    }
  }

  return NextResponse.next();
}

export const config = {
  matcher: ['/dashboard/:path*', '/login', '/register']
};
```

## Vercel Deployment

### Platform: Vercel

**Use Vercel as the preferred deployment platform for Next.js applications**

### Why Vercel?
- Built by the Next.js team
- Zero-config deployments
- Edge Functions and Middleware
- Automatic HTTPS and CDN
- Preview deployments for PRs
- Built-in analytics

### vercel.json Configuration
```json
{
  "buildCommand": "pnpm build",
  "devCommand": "pnpm dev",
  "installCommand": "pnpm install",
  "framework": "nextjs",
  "regions": ["iad1"],
  "env": {
    "DATABASE_URL": "@database-url",
    "NEXT_PUBLIC_APP_URL": "@app-url"
  },
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        {
          "key": "X-Content-Type-Options",
          "value": "nosniff"
        },
        {
          "key": "X-Frame-Options",
          "value": "DENY"
        },
        {
          "key": "X-XSS-Protection",
          "value": "1; mode=block"
        }
      ]
    }
  ]
}
```

### Environment Variables

#### .env.local (Development)
```bash
# Database
DATABASE_URL="postgresql://..."

# Auth
BETTER_AUTH_SECRET="your-secret-key"
BETTER_AUTH_URL="http://localhost:3000"

# Public vars (exposed to browser)
NEXT_PUBLIC_APP_URL="http://localhost:3000"
NEXT_PUBLIC_API_URL="http://localhost:3000/api"
```

#### Vercel Environment Variables
```bash
# Set via Vercel dashboard or CLI
vercel env add DATABASE_URL
vercel env add BETTER_AUTH_SECRET
vercel env add NEXT_PUBLIC_APP_URL
```

### Deployment Workflow

#### Automatic Deployments
- **Production**: Push to `main` branch → auto-deploy to production
- **Preview**: Open PR → auto-deploy preview environment
- **Development**: Push to any branch → preview deployment

#### Manual Deployment
```bash
# Install Vercel CLI
pnpm add -g vercel

# Deploy to preview
vercel

# Deploy to production
vercel --prod

# Set environment variable
vercel env add DATABASE_URL production
```

### Build Optimization

#### Static vs Dynamic Rendering
```typescript
// Force static generation
export const dynamic = 'force-static';

// Force dynamic rendering
export const dynamic = 'force-dynamic';

// Revalidate every 60 seconds (ISR)
export const revalidate = 60;
```

#### Edge Runtime
```typescript
// app/api/edge/route.ts
export const runtime = 'edge';

export async function GET() {
  return new Response('Hello from Edge');
}
```

## Performance Best Practices

### 1. Image Optimization
```typescript
import Image from 'next/image';

export function Avatar({ src, alt }: { src: string; alt: string }) {
  return (
    <Image
      src={src}
      alt={alt}
      width={40}
      height={40}
      priority={false}
      loading="lazy"
      placeholder="blur"
      blurDataURL="data:image/jpeg;base64,..."
    />
  );
}
```

### 2. Font Optimization
```typescript
// app/layout.tsx
import { Inter } from 'next/font/google';

const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-inter',
});

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={inter.variable}>
      <body>{children}</body>
    </html>
  );
}
```

### 3. Metadata & SEO
```typescript
// app/layout.tsx
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: {
    default: 'My App',
    template: '%s | My App',
  },
  description: 'App description',
  openGraph: {
    title: 'My App',
    description: 'App description',
    url: 'https://myapp.com',
    siteName: 'My App',
    images: [
      {
        url: 'https://myapp.com/og.png',
        width: 1200,
        height: 630,
      },
    ],
    locale: 'en_US',
    type: 'website',
  },
};
```

### 4. Code Splitting
```typescript
// Dynamic imports for client components
import dynamic from 'next/dynamic';

const HeavyComponent = dynamic(() => import('@/components/HeavyComponent'), {
  loading: () => <p>Loading...</p>,
  ssr: false, // Disable SSR if needed
});
```

### 5. Data Fetching Patterns
```typescript
// Parallel data fetching
async function ParallelPage() {
  const [users, posts] = await Promise.all([
    fetchUsers(),
    fetchPosts(),
  ]);

  return <div>{/* render */}</div>;
}

// Streaming with Suspense
import { Suspense } from 'react';

export default function StreamingPage() {
  return (
    <div>
      <Suspense fallback={<Skeleton />}>
        <AsyncComponent />
      </Suspense>
    </div>
  );
}
```

## Monitoring & Analytics

### Vercel Analytics
```typescript
// app/layout.tsx
import { Analytics } from '@vercel/analytics/react';

export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        {children}
        <Analytics />
      </body>
    </html>
  );
}
```

### Speed Insights
```typescript
import { SpeedInsights } from '@vercel/speed-insights/next';

export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        {children}
        <SpeedInsights />
      </body>
    </html>
  );
}
```

## Development Workflow

### package.json Scripts
```json
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "type-check": "tsc --noEmit",
    "preview": "vercel dev"
  }
}
```

### Pre-deployment Checklist
- ✅ Run `pnpm build` locally to catch build errors
- ✅ Test all environment variables are set in Vercel
- ✅ Verify API routes work correctly
- ✅ Check middleware logic
- ✅ Test authentication flows
- ✅ Review build output for static/dynamic pages
- ✅ Check bundle size and lighthouse scores

---

**Use Next.js with Vercel for optimized, production-ready web applications.**

---

<!-- Source: 506-better-auth-standards.mdc -->

# Better-Auth Authentication Standards

## Authentication Library: Better-Auth

**Use Better-Auth as the preferred authentication solution for Node.js/Next.js applications**

### Why Better-Auth?
- Type-safe authentication
- Multiple authentication methods (email/password, OAuth, magic links)
- Built-in session management
- Next.js optimized
- Extensible with plugins
- Database agnostic

## Installation & Setup

### Install Better-Auth
```bash
pnpm add better-auth
pnpm add -D @better-auth/cli
```

### Database Setup
Better-Auth works with any database. Common choices:

```bash
# PostgreSQL (recommended)
pnpm add @prisma/client
pnpm add -D prisma

# Or Drizzle ORM
pnpm add drizzle-orm
pnpm add -D drizzle-kit
```

## Configuration

### Auth Configuration File
```typescript
// lib/auth.ts
import { betterAuth } from "better-auth";
import { prismaAdapter } from "better-auth/adapters/prisma";
import { prisma } from "./db";

export const auth = betterAuth({
  database: prismaAdapter(prisma, {
    provider: "postgresql",
  }),

  emailAndPassword: {
    enabled: true,
    requireEmailVerification: true,
  },

  socialProviders: {
    google: {
      clientId: process.env.GOOGLE_CLIENT_ID!,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET!,
    },
    github: {
      clientId: process.env.GITHUB_CLIENT_ID!,
      clientSecret: process.env.GITHUB_CLIENT_SECRET!,
    },
  },

  session: {
    expiresIn: 60 * 60 * 24 * 7, // 7 days
    updateAge: 60 * 60 * 24, // 1 day
  },

  user: {
    additionalFields: {
      role: {
        type: "string",
        required: false,
        defaultValue: "user",
      },
    },
  },

  advanced: {
    cookiePrefix: "myapp",
    crossSubDomainCookies: {
      enabled: false,
    },
  },
});

export type Session = typeof auth.$Infer.Session;
```

### Environment Variables
```bash
# .env.local
DATABASE_URL="postgresql://..."

# Better Auth
BETTER_AUTH_SECRET="your-secret-key-min-32-chars"
BETTER_AUTH_URL="http://localhost:3000"

# OAuth Providers
GOOGLE_CLIENT_ID="..."
GOOGLE_CLIENT_SECRET="..."
GITHUB_CLIENT_ID="..."
GITHUB_CLIENT_SECRET="..."

# Email (optional)
SMTP_HOST="smtp.gmail.com"
SMTP_PORT="587"
SMTP_USER="..."
SMTP_PASSWORD="..."
```

## Database Schema

### Prisma Schema
```prisma
// prisma/schema.prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model User {
  id            String    @id @default(cuid())
  email         String    @unique
  emailVerified Boolean   @default(false)
  name          String?
  image         String?
  role          String    @default("user")
  createdAt     DateTime  @default(now())
  updatedAt     DateTime  @updatedAt

  accounts      Account[]
  sessions      Session[]
}

model Account {
  id                String  @id @default(cuid())
  userId            String
  type              String
  provider          String
  providerAccountId String
  refreshToken      String?
  accessToken       String?
  expiresAt         Int?
  tokenType         String?
  scope             String?
  idToken           String?

  user User @relation(fields: [userId], references: [id], onDelete: Cascade)

  @@unique([provider, providerAccountId])
}

model Session {
  id           String   @id @default(cuid())
  sessionToken String   @unique
  userId       String
  expiresAt    DateTime

  user User @relation(fields: [userId], references: [id], onDelete: Cascade)
}

model VerificationToken {
  identifier String
  token      String   @unique
  expires    DateTime

  @@unique([identifier, token])
}
```

## Next.js Integration

### API Route Handler
```typescript
// app/api/auth/[...all]/route.ts
import { auth } from "@/lib/auth";
import { toNextJsHandler } from "better-auth/next-js";

export const { GET, POST } = toNextJsHandler(auth);
```

### Client Setup
```typescript
// lib/auth-client.ts
import { createAuthClient } from "better-auth/react";

export const authClient = createAuthClient({
  baseURL: process.env.NEXT_PUBLIC_APP_URL,
});

export const {
  signIn,
  signOut,
  signUp,
  useSession,
} = authClient;
```

### Middleware Protection
```typescript
// middleware.ts
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";
import { auth } from "@/lib/auth";

const protectedRoutes = ["/dashboard", "/settings", "/profile"];
const authRoutes = ["/login", "/register"];

export async function middleware(request: NextRequest) {
  const session = await auth.api.getSession({
    headers: request.headers,
  });

  const isProtectedRoute = protectedRoutes.some((route) =>
    request.nextUrl.pathname.startsWith(route)
  );
  const isAuthRoute = authRoutes.some((route) =>
    request.nextUrl.pathname.startsWith(route)
  );

  // Redirect unauthenticated users to login
  if (isProtectedRoute && !session) {
    const loginUrl = new URL("/login", request.url);
    loginUrl.searchParams.set("callbackUrl", request.nextUrl.pathname);
    return NextResponse.redirect(loginUrl);
  }

  // Redirect authenticated users away from auth pages
  if (isAuthRoute && session) {
    return NextResponse.redirect(new URL("/dashboard", request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/((?!api|_next/static|_next/image|favicon.ico).*)"],
};
```

## Authentication Flows

### Email/Password Registration
```typescript
// components/RegisterForm.tsx
"use client";

import { useState } from "react";
import { signUp } from "@/lib/auth-client";
import { useRouter } from "next/navigation";

export function RegisterForm() {
  const router = useRouter();
  const [error, setError] = useState("");

  async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    const formData = new FormData(e.currentTarget);

    try {
      await signUp.email({
        email: formData.get("email") as string,
        password: formData.get("password") as string,
        name: formData.get("name") as string,
        callbackURL: "/dashboard",
      });

      router.push("/verify-email");
    } catch (err) {
      setError("Registration failed. Please try again.");
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <input name="name" type="text" placeholder="Name" required />
      <input name="email" type="email" placeholder="Email" required />
      <input name="password" type="password" placeholder="Password" required />
      {error && <p className="error">{error}</p>}
      <button type="submit">Sign Up</button>
    </form>
  );
}
```

### Email/Password Login
```typescript
// components/LoginForm.tsx
"use client";

import { useState } from "react";
import { signIn } from "@/lib/auth-client";
import { useRouter } from "next/navigation";

export function LoginForm() {
  const router = useRouter();
  const [error, setError] = useState("");

  async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    const formData = new FormData(e.currentTarget);

    try {
      await signIn.email({
        email: formData.get("email") as string,
        password: formData.get("password") as string,
        callbackURL: "/dashboard",
      });

      router.push("/dashboard");
    } catch (err) {
      setError("Invalid credentials. Please try again.");
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <input name="email" type="email" placeholder="Email" required />
      <input name="password" type="password" placeholder="Password" required />
      {error && <p className="error">{error}</p>}
      <button type="submit">Sign In</button>
    </form>
  );
}
```

### OAuth Login
```typescript
// components/SocialLogin.tsx
"use client";

import { signIn } from "@/lib/auth-client";

export function SocialLogin() {
  async function handleGoogleLogin() {
    await signIn.social({
      provider: "google",
      callbackURL: "/dashboard",
    });
  }

  async function handleGithubLogin() {
    await signIn.social({
      provider: "github",
      callbackURL: "/dashboard",
    });
  }

  return (
    <div>
      <button onClick={handleGoogleLogin}>
        Continue with Google
      </button>
      <button onClick={handleGithubLogin}>
        Continue with GitHub
      </button>
    </div>
  );
}
```

### Logout
```typescript
// components/LogoutButton.tsx
"use client";

import { signOut } from "@/lib/auth-client";
import { useRouter } from "next/navigation";

export function LogoutButton() {
  const router = useRouter();

  async function handleLogout() {
    await signOut({
      fetchOptions: {
        onSuccess: () => {
          router.push("/login");
        },
      },
    });
  }

  return (
    <button onClick={handleLogout}>
      Sign Out
    </button>
  );
}
```

## Session Management

### Get Session (Client Component)
```typescript
"use client";

import { useSession } from "@/lib/auth-client";

export function UserProfile() {
  const { data: session, isPending } = useSession();

  if (isPending) {
    return <div>Loading...</div>;
  }

  if (!session) {
    return <div>Not authenticated</div>;
  }

  return (
    <div>
      <p>Welcome {session.user.name}</p>
      <p>Email: {session.user.email}</p>
      <p>Role: {session.user.role}</p>
    </div>
  );
}
```

### Get Session (Server Component)
```typescript
// app/dashboard/page.tsx
import { auth } from "@/lib/auth";
import { headers } from "next/headers";
import { redirect } from "next/navigation";

export default async function DashboardPage() {
  const session = await auth.api.getSession({
    headers: await headers(),
  });

  if (!session) {
    redirect("/login");
  }

  return (
    <div>
      <h1>Dashboard</h1>
      <p>Welcome {session.user.name}</p>
    </div>
  );
}
```

### Get Session (API Route)
```typescript
// app/api/me/route.ts
import { auth } from "@/lib/auth";
import { NextRequest, NextResponse } from "next/server";

export async function GET(request: NextRequest) {
  const session = await auth.api.getSession({
    headers: request.headers,
  });

  if (!session) {
    return NextResponse.json(
      { error: "Unauthorized" },
      { status: 401 }
    );
  }

  return NextResponse.json({ user: session.user });
}
```

## Authorization & Roles

### Role-Based Access Control
```typescript
// lib/rbac.ts
import { auth } from "@/lib/auth";
import { headers } from "next/headers";
import { redirect } from "next/navigation";

export async function requireRole(role: string) {
  const session = await auth.api.getSession({
    headers: await headers(),
  });

  if (!session) {
    redirect("/login");
  }

  if (session.user.role !== role && session.user.role !== "admin") {
    redirect("/unauthorized");
  }

  return session;
}

// Usage in page
export default async function AdminPage() {
  await requireRole("admin");

  return <div>Admin Dashboard</div>;
}
```

### Permission Checking
```typescript
// lib/permissions.ts
export function hasPermission(user: User, permission: string): boolean {
  const permissions = {
    admin: ["*"],
    moderator: ["user.read", "user.update", "post.delete"],
    user: ["user.read"],
  };

  const userPermissions = permissions[user.role] || [];
  return userPermissions.includes("*") || userPermissions.includes(permission);
}

// Usage
if (!hasPermission(session.user, "user.update")) {
  return NextResponse.json({ error: "Forbidden" }, { status: 403 });
}
```

## Email Verification

### Send Verification Email
```typescript
// lib/auth.ts (extended config)
export const auth = betterAuth({
  // ... other config
  emailVerification: {
    sendOnSignUp: true,
    autoSignInAfterVerification: true,
    sendVerificationEmail: async ({ user, url }) => {
      // Send email using your email service
      await sendEmail({
        to: user.email,
        subject: "Verify your email",
        html: `<a href="${url}">Click here to verify your email</a>`,
      });
    },
  },
});
```

### Verify Email Page
```typescript
// app/verify-email/page.tsx
import { auth } from "@/lib/auth";
import { redirect } from "next/navigation";

export default async function VerifyEmailPage({
  searchParams,
}: {
  searchParams: { token?: string };
}) {
  if (!searchParams.token) {
    return <div>Invalid verification link</div>;
  }

  const result = await auth.api.verifyEmail({
    query: {
      token: searchParams.token,
    },
  });

  if (result.error) {
    return <div>Verification failed: {result.error.message}</div>;
  }

  redirect("/dashboard");
}
```

## Password Reset

### Request Password Reset
```typescript
"use client";

import { authClient } from "@/lib/auth-client";

export function ForgotPasswordForm() {
  async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    const formData = new FormData(e.currentTarget);

    await authClient.forgetPassword({
      email: formData.get("email") as string,
      redirectTo: "/reset-password",
    });

    alert("Password reset link sent to your email");
  }

  return (
    <form onSubmit={handleSubmit}>
      <input name="email" type="email" placeholder="Email" required />
      <button type="submit">Reset Password</button>
    </form>
  );
}
```

### Reset Password Page
```typescript
// app/reset-password/page.tsx
"use client";

import { authClient } from "@/lib/auth-client";
import { useRouter, useSearchParams } from "next/navigation";

export default function ResetPasswordPage() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const token = searchParams.get("token");

  async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    const formData = new FormData(e.currentTarget);

    await authClient.resetPassword({
      newPassword: formData.get("password") as string,
      token: token!,
    });

    router.push("/login");
  }

  return (
    <form onSubmit={handleSubmit}>
      <input name="password" type="password" placeholder="New Password" required />
      <button type="submit">Reset Password</button>
    </form>
  );
}
```

## Security Best Practices

### 1. Strong Password Requirements
```typescript
// lib/auth.ts
export const auth = betterAuth({
  emailAndPassword: {
    enabled: true,
    minPasswordLength: 8,
    maxPasswordLength: 128,
    password: {
      requireUppercase: true,
      requireLowercase: true,
      requireNumbers: true,
      requireSpecialChars: true,
    },
  },
});
```

### 2. Rate Limiting
```typescript
// middleware.ts
import { rateLimit } from "@/lib/rate-limit";

export async function middleware(request: NextRequest) {
  if (request.nextUrl.pathname.startsWith("/api/auth")) {
    const ip = request.ip ?? "127.0.0.1";
    const { success } = await rateLimit.limit(ip);

    if (!success) {
      return NextResponse.json(
        { error: "Too many requests" },
        { status: 429 }
      );
    }
  }

  return NextResponse.next();
}
```

### 3. CSRF Protection
Better-Auth includes built-in CSRF protection. Ensure it's enabled:

```typescript
export const auth = betterAuth({
  advanced: {
    useSecureCookies: process.env.NODE_ENV === "production",
    generateSessionToken: () => {
      return crypto.randomBytes(32).toString("hex");
    },
  },
});
```

---

**Use Better-Auth for type-safe, secure authentication in Next.js applications.**

---

<!-- Source: 507-proofkit-standards.mdc -->

# ProofKit Development Standards

## What is ProofKit?

**ProofKit is a comprehensive TypeScript toolset and CLI for building modern web applications integrated with Claris FileMaker.**

### Core Purpose
- Boilerplate and project scaffolding for FileMaker web apps
- Type-safe FileMaker Data API integration
- Authentication backed by FileMaker database
- Code generation from FileMaker layouts
- WebViewer integration utilities

### Why ProofKit?
- Rapid development of FileMaker-connected web apps
- Type safety with auto-generated TypeScript types
- Modern web stack (Next.js, Better-Auth, TypeScript)
- Opinionated structure with flexibility
- Progressive enhancement via CLI code mods

## Core Libraries

### @proofkit/fmdapi
**FileMaker Data API integration with type safety**

```typescript
import { fmdapi } from '@proofkit/fmdapi';

// Type-safe API calls to FileMaker
const users = await fmdapi.layouts.Users.find({
  query: [{ email: 'user@example.com' }]
});

// Automatic token management
// Runtime validation of responses
// TypeScript types from FileMaker layouts
```

### @proofkit/typegen
**Automatic TypeScript generation from FileMaker layouts**

```bash
# Generate types from FileMaker schema
pnpm proofkit typegen

# Creates TypeScript types and Zod validators
# Based on your FileMaker layout definitions
```

Generated files:
```typescript
// src/fmdapi/schemas/Users.fmschema.ts
import { z } from 'zod';

export const UsersSchema = z.object({
  id: z.string(),
  email: z.string().email(),
  name: z.string(),
  createdAt: z.string().datetime(),
});

export type Users = z.infer<typeof UsersSchema>;
```

### @proofkit/webviewer
**FileMaker WebViewer integration**

```typescript
import { executeScript } from '@proofkit/webviewer';

// Execute FileMaker script from web code
const result = await executeScript('GetUserData', { userId: '123' });

// Async functions in WebViewer
// Get results from FileMaker scripts
// Bidirectional communication
```

### @proofkit/better-auth
**Self-hosted authentication with FileMaker backend**

```typescript
import { betterAuth } from '@proofkit/better-auth';
import { fmAdapter } from '@proofkit/better-auth/adapters';

export const auth = betterAuth({
  database: fmAdapter({
    // Uses FileMaker as auth database
    layout: 'Users',
    // Automatic user management
  }),
  emailAndPassword: {
    enabled: true,
  },
});
```

## Project Setup

### Initialize ProofKit Project

```bash
# Create new ProofKit project
pnpm create proofkit@latest my-app

# Or with specific template
pnpm create proofkit@latest my-app --template filemaker-auth

# Navigate and install
cd my-app
pnpm install
```

### Project Structure

```
my-proofkit-app/
├── src/
│   ├── app/                    # Next.js App Router
│   │   ├── (auth)/            # Auth routes
│   │   ├── dashboard/         # Protected routes
│   │   └── api/               # API routes
│   ├── components/            # React components
│   ├── lib/                   # Utilities
│   │   ├── auth.ts           # Better-Auth config
│   │   └── fmdapi.ts         # FileMaker API config
│   ├── fmdapi/               # Generated FileMaker types
│   │   └── schemas/          # Auto-generated schemas
│   └── middleware.ts          # Auth middleware
├── proofkit.config.ts         # ProofKit configuration
├── .env.local                 # Environment variables
└── package.json
```

## Configuration

### proofkit.config.ts

```typescript
import { defineConfig } from '@proofkit/cli';

export default defineConfig({
  // FileMaker connection
  filemaker: {
    host: process.env.FM_HOST,
    database: process.env.FM_DATABASE,
    layouts: {
      users: 'Users',
      posts: 'Posts',
      comments: 'Comments',
    },
  },

  // Type generation
  typegen: {
    outputDir: './src/fmdapi/schemas',
    generateZod: true,
    generateTypes: true,
  },

  // Better-Auth integration
  auth: {
    adapter: 'filemaker',
    userLayout: 'Users',
  },
});
```

### Environment Variables

```bash
# .env.local

# FileMaker
FM_HOST="https://your-filemaker-server.com"
FM_DATABASE="YourDatabase"
FM_USERNAME="api_user"
FM_PASSWORD="api_password"

# Better Auth
BETTER_AUTH_SECRET="your-secret-key-min-32-chars"
BETTER_AUTH_URL="http://localhost:3000"

# App
NEXT_PUBLIC_APP_URL="http://localhost:3000"
```

## FileMaker Integration Patterns

### Data Fetching

```typescript
// lib/fmdapi.ts - Configure FileMaker API
import { createFMClient } from '@proofkit/fmdapi';

export const fm = createFMClient({
  host: process.env.FM_HOST!,
  database: process.env.FM_DATABASE!,
  auth: {
    username: process.env.FM_USERNAME!,
    password: process.env.FM_PASSWORD!,
  },
});

// app/api/users/route.ts - API route
import { fm } from '@/lib/fmdapi';
import { UsersSchema } from '@/fmdapi/schemas/Users.fmschema';

export async function GET() {
  const response = await fm.layouts.Users.find({
    query: [{ active: '1' }],
    sort: [{ fieldName: 'createdAt', sortOrder: 'descend' }],
  });

  // Automatic validation with generated schema
  const users = response.data.map(record =>
    UsersSchema.parse(record.fieldData)
  );

  return Response.json({ users });
}

// app/dashboard/page.tsx - Server Component
import { fm } from '@/lib/fmdapi';

export default async function DashboardPage() {
  const users = await fm.layouts.Users.find({});

  return (
    <div>
      <h1>Users</h1>
      {users.data.map(user => (
        <div key={user.recordId}>{user.fieldData.name}</div>
      ))}
    </div>
  );
}
```

### Creating Records

```typescript
import { fm } from '@/lib/fmdapi';

async function createUser(data: { email: string; name: string }) {
  const response = await fm.layouts.Users.create({
    fieldData: {
      email: data.email,
      name: data.name,
      createdAt: new Date().toISOString(),
    },
  });

  return response.data;
}
```

### Updating Records

```typescript
async function updateUser(recordId: string, data: Partial<Users>) {
  const response = await fm.layouts.Users.update(recordId, {
    fieldData: data,
  });

  return response.data;
}
```

### Deleting Records

```typescript
async function deleteUser(recordId: string) {
  await fm.layouts.Users.delete(recordId);
}
```

## Authentication with Better-Auth + FileMaker

### Auth Configuration

```typescript
// lib/auth.ts
import { betterAuth } from 'better-auth';
import { fmAdapter } from '@proofkit/better-auth/adapters';

export const auth = betterAuth({
  database: fmAdapter({
    host: process.env.FM_HOST!,
    database: process.env.FM_DATABASE!,
    layout: 'Users',
    auth: {
      username: process.env.FM_USERNAME!,
      password: process.env.FM_PASSWORD!,
    },
  }),

  emailAndPassword: {
    enabled: true,
    requireEmailVerification: false,
  },

  session: {
    expiresIn: 60 * 60 * 24 * 7, // 7 days
  },
});
```

### Auth API Route

```typescript
// app/api/auth/[...all]/route.ts
import { auth } from '@/lib/auth';
import { toNextJsHandler } from 'better-auth/next-js';

export const { GET, POST } = toNextJsHandler(auth);
```

### Protected Routes

```typescript
// middleware.ts
import { auth } from '@/lib/auth';
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export async function middleware(request: NextRequest) {
  const session = await auth.api.getSession({
    headers: request.headers,
  });

  if (!session && request.nextUrl.pathname.startsWith('/dashboard')) {
    return NextResponse.redirect(new URL('/login', request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ['/dashboard/:path*'],
};
```

## WebViewer Integration

### Execute FileMaker Scripts from Web

```typescript
import { executeScript } from '@proofkit/webviewer';

async function handleAction() {
  // Call FileMaker script and get result
  const result = await executeScript('ProcessPayment', {
    amount: 100,
    userId: '123',
  });

  console.log(result); // Result from FileMaker script
}
```

### Web Code in FileMaker WebViewer

```html
<!-- In FileMaker WebViewer -->
<script type="module">
  import { executeScript } from '@proofkit/webviewer';

  // This runs in FileMaker WebViewer
  async function getData() {
    const data = await executeScript('GetUserData');
    document.getElementById('result').textContent = JSON.stringify(data);
  }

  getData();
</script>
```

## CLI Code Mods

### Add Features to Existing Project

```bash
# Add authentication
pnpm proofkit add auth

# Add FileMaker layout integration
pnpm proofkit add layout Posts

# Add API route
pnpm proofkit add route users

# List available mods
pnpm proofkit add --list
```

### Generate Types from FileMaker

```bash
# Connect to FileMaker and generate types
pnpm proofkit typegen

# Watch mode for development
pnpm proofkit typegen --watch

# Generate for specific layouts
pnpm proofkit typegen --layouts Users,Posts
```

## Best Practices

### Type Safety
- Always run `proofkit typegen` after FileMaker schema changes
- Use generated Zod schemas for validation
- Leverage TypeScript types from generated schemas
- Never manually write FileMaker record types

### Error Handling
```typescript
import { FMError } from '@proofkit/fmdapi';

try {
  const user = await fm.layouts.Users.find({ query: [{ id: '123' }] });
} catch (error) {
  if (error instanceof FMError) {
    console.error('FileMaker error:', error.code, error.message);
  } else {
    console.error('Unexpected error:', error);
  }
}
```

### Authentication
- Use FileMaker as the source of truth for user data
- Leverage Better-Auth's built-in security features
- Implement proper session management
- Use middleware for route protection

### Performance
- Cache FileMaker API responses when appropriate
- Use Next.js Server Components for data fetching
- Implement proper loading states
- Consider using Supabase for real-time features alongside FileMaker

## Supabase Integration (Optional)

ProofKit projects can combine FileMaker and Supabase:

```typescript
// Use FileMaker for primary data
const users = await fm.layouts.Users.find({});

// Use Supabase for real-time features
import { createClient } from '@supabase/supabase-js';

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
);

// Real-time notifications
const { data } = await supabase
  .from('notifications')
  .select('*')
  .eq('user_id', userId)
  .order('created_at', { ascending: false });
```

## Development Workflow

### Initial Setup
1. Create ProofKit project: `pnpm create proofkit@latest`
2. Configure FileMaker connection in `.env.local`
3. Run `proofkit typegen` to generate types
4. Set up Better-Auth with FileMaker adapter
5. Start development: `pnpm dev`

### Adding Features
1. Define layout in FileMaker
2. Run `proofkit typegen` to generate types
3. Use `proofkit add` to scaffold code
4. Implement business logic
5. Test integration with FileMaker

### Deployment
1. Build Next.js app: `pnpm build`
2. Deploy to Vercel (recommended)
3. Configure environment variables
4. Ensure FileMaker server is accessible
5. Test production deployment

---

**Use ProofKit for rapid development of type-safe FileMaker web applications with modern web technologies.**

---

<!-- Source: 508-typescript-standards.mdc -->

# TypeScript Standards

## TypeScript Configuration

### tsconfig.json Standards

**Use strict mode and modern features:**

```json
{
  "compilerOptions": {
    // Type Checking
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,
    "noFallthroughCasesInSwitch": true,
    "noPropertyAccessFromIndexSignature": true,

    // Modules
    "module": "ESNext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "allowImportingTsExtensions": true,

    // Emit
    "noEmit": true,  // If using bundler (Vite, Next.js)
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "removeComments": false,

    // JavaScript Support
    "allowJs": true,
    "checkJs": false,

    // Interop
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "forceConsistentCasingInFileNames": true,
    "isolatedModules": true,

    // Language Features
    "target": "ES2022",
    "lib": ["ES2022", "DOM", "DOM.Iterable"],
    "jsx": "preserve",  // or "react-jsx" for React 17+
    "useDefineForClassFields": true,

    // Paths
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"],
      "@/components/*": ["./src/components/*"],
      "@/lib/*": ["./src/lib/*"],
      "@/types/*": ["./src/types/*"]
    },

    // Skip lib check for faster builds
    "skipLibCheck": true
  },
  "include": ["src/**/*", "**/*.ts", "**/*.tsx"],
  "exclude": ["node_modules", "dist", "build", ".next"]
}
```

### Project Structure

```
src/
├── types/
│   ├── index.ts           # Re-export all types
│   ├── api.ts             # API types
│   ├── models.ts          # Data models
│   └── utils.ts           # Utility types
├── lib/
│   ├── db.ts
│   └── utils.ts
├── components/
│   └── Button.tsx
└── index.ts
```

## Type Safety Best Practices

### Use Strict Types

```typescript
// Good - Explicit types
interface User {
  id: string;
  email: string;
  name: string | null;
  role: 'user' | 'admin' | 'moderator';
  createdAt: Date;
}

function getUser(id: string): Promise<User | null> {
  // implementation
}

// Bad - Any types
function getUser(id: any): any {
  // implementation
}
```

### Avoid `any`

```typescript
// Bad - Using any
function processData(data: any) {
  return data.value.toUpperCase();
}

// Good - Use unknown and type guards
function processData(data: unknown) {
  if (isDataWithValue(data)) {
    return data.value.toUpperCase();
  }
  throw new Error('Invalid data structure');
}

function isDataWithValue(data: unknown): data is { value: string } {
  return (
    typeof data === 'object' &&
    data !== null &&
    'value' in data &&
    typeof data.value === 'string'
  );
}
```

### Use Type Guards

```typescript
// Type guard for null/undefined
function isNotNull<T>(value: T | null | undefined): value is T {
  return value !== null && value !== undefined;
}

// Usage
const users = await getUsers();
const activeUsers = users.filter(isNotNull);

// Type guard for object shape
interface Post {
  id: string;
  title: string;
}

function isPost(value: unknown): value is Post {
  return (
    typeof value === 'object' &&
    value !== null &&
    'id' in value &&
    'title' in value &&
    typeof value.id === 'string' &&
    typeof value.title === 'string'
  );
}

// Discriminated unions
type Result<T> =
  | { success: true; data: T }
  | { success: false; error: string };

function handleResult<T>(result: Result<T>) {
  if (result.success) {
    console.log(result.data); // TypeScript knows data exists
  } else {
    console.error(result.error); // TypeScript knows error exists
  }
}
```

### Utility Types

```typescript
// Built-in utility types
type UserInput = Omit<User, 'id' | 'createdAt'>;
type PartialUser = Partial<User>;
type RequiredUser = Required<PartialUser>;
type UserKeys = keyof User;
type UserRecord = Record<string, User>;
type UserPick = Pick<User, 'id' | 'email'>;

// Custom utility types
type Nullable<T> = T | null;
type Optional<T> = T | undefined;
type AsyncReturnType<T extends (...args: any) => Promise<any>> =
  T extends (...args: any) => Promise<infer R> ? R : never;

// Make specific fields optional
type PartialBy<T, K extends keyof T> = Omit<T, K> & Partial<Pick<T, K>>;

// Make specific fields required
type RequiredBy<T, K extends keyof T> = Omit<T, K> & Required<Pick<T, K>>;

// Deep partial
type DeepPartial<T> = {
  [P in keyof T]?: T[P] extends object ? DeepPartial<T[P]> : T[P];
};
```

## Interface vs Type

### When to Use Each

```typescript
// Use interface for object shapes and when you need extension
interface BaseUser {
  id: string;
  email: string;
}

interface AdminUser extends BaseUser {
  role: 'admin';
  permissions: string[];
}

// Use type for unions, intersections, and mapped types
type Status = 'pending' | 'active' | 'inactive';
type ID = string | number;
type UserOrAdmin = User | Admin;
type ReadonlyUser = Readonly<User>;

// Type for computed property names
type EventMap = {
  [K in keyof HTMLElementEventMap as `on${Capitalize<K>}`]: (
    event: HTMLElementEventMap[K]
  ) => void;
};
```

### Prefer Interface for Objects

```typescript
// Good - Interface for object shapes
interface Config {
  apiUrl: string;
  timeout: number;
  retries: number;
}

// Also acceptable - Type alias
type Config = {
  apiUrl: string;
  timeout: number;
  retries: number;
};
```

## Generics

### Generic Functions

```typescript
// Good - Generic with constraints
function firstElement<T>(arr: T[]): T | undefined {
  return arr[0];
}

// Generic with multiple type parameters
function map<T, U>(arr: T[], fn: (item: T) => U): U[] {
  return arr.map(fn);
}

// Generic with constraints
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

// Generic with default type
function createArray<T = string>(length: number, value: T): T[] {
  return Array(length).fill(value);
}
```

### Generic Types

```typescript
// Generic interface
interface Repository<T> {
  find(id: string): Promise<T | null>;
  findAll(): Promise<T[]>;
  create(data: Omit<T, 'id'>): Promise<T>;
  update(id: string, data: Partial<T>): Promise<T>;
  delete(id: string): Promise<void>;
}

// Generic class
class InMemoryRepository<T extends { id: string }> implements Repository<T> {
  private items: T[] = [];

  async find(id: string): Promise<T | null> {
    return this.items.find(item => item.id === id) ?? null;
  }

  async findAll(): Promise<T[]> {
    return this.items;
  }

  async create(data: Omit<T, 'id'>): Promise<T> {
    const item = { ...data, id: crypto.randomUUID() } as T;
    this.items.push(item);
    return item;
  }

  async update(id: string, data: Partial<T>): Promise<T> {
    const index = this.items.findIndex(item => item.id === id);
    if (index === -1) throw new Error('Not found');
    this.items[index] = { ...this.items[index], ...data };
    return this.items[index];
  }

  async delete(id: string): Promise<void> {
    this.items = this.items.filter(item => item.id !== id);
  }
}
```

## React TypeScript Standards

### Component Props

```typescript
// Function component with props
interface ButtonProps {
  children: React.ReactNode;
  variant?: 'primary' | 'secondary' | 'danger';
  size?: 'sm' | 'md' | 'lg';
  onClick?: () => void;
  disabled?: boolean;
}

export function Button({
  children,
  variant = 'primary',
  size = 'md',
  onClick,
  disabled = false
}: ButtonProps) {
  return (
    <button
      className={`btn btn-${variant} btn-${size}`}
      onClick={onClick}
      disabled={disabled}
    >
      {children}
    </button>
  );
}

// Extending HTML attributes
interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label: string;
  error?: string;
}

export function Input({ label, error, ...props }: InputProps) {
  return (
    <div>
      <label>{label}</label>
      <input {...props} />
      {error && <span className="error">{error}</span>}
    </div>
  );
}
```

### Hooks Typing

```typescript
// useState with explicit type
const [user, setUser] = useState<User | null>(null);
const [items, setItems] = useState<string[]>([]);

// useRef with element type
const inputRef = useRef<HTMLInputElement>(null);

// useReducer with typed state and actions
type State = {
  count: number;
  status: 'idle' | 'loading' | 'success' | 'error';
};

type Action =
  | { type: 'increment' }
  | { type: 'decrement' }
  | { type: 'setStatus'; status: State['status'] };

function reducer(state: State, action: Action): State {
  switch (action.type) {
    case 'increment':
      return { ...state, count: state.count + 1 };
    case 'decrement':
      return { ...state, count: state.count - 1 };
    case 'setStatus':
      return { ...state, status: action.status };
  }
}

// Custom hooks with generic types
function useLocalStorage<T>(key: string, initialValue: T) {
  const [storedValue, setStoredValue] = useState<T>(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      return initialValue;
    }
  });

  const setValue = (value: T | ((val: T) => T)) => {
    try {
      const valueToStore = value instanceof Function ? value(storedValue) : value;
      setStoredValue(valueToStore);
      window.localStorage.setItem(key, JSON.stringify(valueToStore));
    } catch (error) {
      console.error(error);
    }
  };

  return [storedValue, setValue] as const;
}
```

### Event Handlers

```typescript
// Typed event handlers
function handleClick(event: React.MouseEvent<HTMLButtonElement>) {
  console.log(event.currentTarget.value);
}

function handleChange(event: React.ChangeEvent<HTMLInputElement>) {
  console.log(event.target.value);
}

function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
  event.preventDefault();
  // ...
}

// Generic event handler
type EventHandler<T extends HTMLElement> = (
  event: React.MouseEvent<T>
) => void;

const handleButtonClick: EventHandler<HTMLButtonElement> = (event) => {
  console.log(event.currentTarget.textContent);
};
```

## API & Data Fetching

### Type-Safe API Calls

```typescript
// API response types
interface ApiResponse<T> {
  data: T;
  message: string;
  success: boolean;
}

interface ApiError {
  message: string;
  code: string;
  details?: Record<string, string[]>;
}

// Generic fetch wrapper
async function fetchApi<T>(
  url: string,
  options?: RequestInit
): Promise<T> {
  const response = await fetch(url, options);

  if (!response.ok) {
    const error: ApiError = await response.json();
    throw new Error(error.message);
  }

  return response.json();
}

// Usage with specific types
interface User {
  id: string;
  email: string;
  name: string;
}

const user = await fetchApi<User>('/api/users/123');
const users = await fetchApi<User[]>('/api/users');
```

### Zod Integration

```typescript
import { z } from 'zod';

// Define schema
const UserSchema = z.object({
  id: z.string().uuid(),
  email: z.string().email(),
  name: z.string().min(2),
  role: z.enum(['user', 'admin', 'moderator']),
  createdAt: z.string().datetime().transform(s => new Date(s)),
});

// Infer TypeScript type from schema
type User = z.infer<typeof UserSchema>;

// Validate and parse
function parseUser(data: unknown): User {
  return UserSchema.parse(data);
}

// Safe parse with error handling
function safeParse User(data: unknown): User | null {
  const result = UserSchema.safeParse(data);
  if (result.success) {
    return result.data;
  }
  console.error(result.error);
  return null;
}
```

## Error Handling

### Type-Safe Errors

```typescript
// Custom error classes
class AppError extends Error {
  constructor(
    message: string,
    public code: string,
    public statusCode: number = 500
  ) {
    super(message);
    this.name = 'AppError';
  }
}

class ValidationError extends AppError {
  constructor(
    message: string,
    public fields: Record<string, string[]>
  ) {
    super(message, 'VALIDATION_ERROR', 400);
    this.name = 'ValidationError';
  }
}

// Type-safe error handling
function handleError(error: unknown): never {
  if (error instanceof ValidationError) {
    console.error('Validation failed:', error.fields);
  } else if (error instanceof AppError) {
    console.error(`${error.code}: ${error.message}`);
  } else if (error instanceof Error) {
    console.error(error.message);
  } else {
    console.error('Unknown error:', error);
  }
  throw error;
}

// Result type pattern
type Result<T, E = Error> =
  | { ok: true; value: T }
  | { ok: false; error: E };

async function fetchUser(id: string): Promise<Result<User>> {
  try {
    const user = await fetchApi<User>(`/api/users/${id}`);
    return { ok: true, value: user };
  } catch (error) {
    return { ok: false, error: error as Error };
  }
}
```

## Advanced Patterns

### Builder Pattern

```typescript
class QueryBuilder<T> {
  private filters: Array<(item: T) => boolean> = [];
  private sortFn?: (a: T, b: T) => number;
  private limitValue?: number;

  where(predicate: (item: T) => boolean): this {
    this.filters.push(predicate);
    return this;
  }

  orderBy(key: keyof T, direction: 'asc' | 'desc' = 'asc'): this {
    this.sortFn = (a, b) => {
      const aVal = a[key];
      const bVal = b[key];
      const comparison = aVal < bVal ? -1 : aVal > bVal ? 1 : 0;
      return direction === 'asc' ? comparison : -comparison;
    };
    return this;
  }

  limit(n: number): this {
    this.limitValue = n;
    return this;
  }

  execute(data: T[]): T[] {
    let result = [...data];

    // Apply filters
    for (const filter of this.filters) {
      result = result.filter(filter);
    }

    // Apply sorting
    if (this.sortFn) {
      result.sort(this.sortFn);
    }

    // Apply limit
    if (this.limitValue) {
      result = result.slice(0, this.limitValue);
    }

    return result;
  }
}

// Usage
const activeAdults = new QueryBuilder<User>()
  .where(u => u.age >= 18)
  .where(u => u.isActive)
  .orderBy('createdAt', 'desc')
  .limit(10)
  .execute(users);
```

### Template Literal Types

```typescript
// HTTP methods
type HttpMethod = 'GET' | 'POST' | 'PUT' | 'DELETE';

// Route patterns
type Route = `/${string}`;
type ApiRoute = `/api${Route}`;

// Event names
type EventName<T extends string> = `on${Capitalize<T>}`;
type ClickEvent = EventName<'click'>; // 'onClick'

// Branded types
type Brand<K, T> = K & { __brand: T };
type UserId = Brand<string, 'UserId'>;
type Email = Brand<string, 'Email'>;

function createUserId(id: string): UserId {
  return id as UserId;
}

function sendEmail(to: Email, subject: string) {
  // ...
}

const userId = createUserId('123');
const email = 'user@example.com' as Email;
sendEmail(email, 'Hello'); // OK
// sendEmail(userId, 'Hello'); // Error!
```

## Testing with TypeScript

### Type-Safe Tests

```typescript
import { describe, it, expect } from 'vitest';

describe('User service', () => {
  it('should create a user', async () => {
    const input: Omit<User, 'id' | 'createdAt'> = {
      email: 'test@example.com',
      name: 'Test User',
      role: 'user',
    };

    const user = await userService.create(input);

    expect(user).toMatchObject<Partial<User>>({
      email: input.email,
      name: input.name,
      role: input.role,
    });
  });
});

// Mock with types
const mockUserRepository: Repository<User> = {
  find: vi.fn(),
  findAll: vi.fn(),
  create: vi.fn(),
  update: vi.fn(),
  delete: vi.fn(),
};
```

---

**Follow these TypeScript standards for type-safe, maintainable code.**

---


# Database Rules

<!-- Source: 601-database-standards.mdc -->

# Database Standards

## Database Selection

### Recommended Databases

**Relational (SQL):**
- **PostgreSQL** - Recommended for most applications
- **MySQL/MariaDB** - Alternative for specific use cases
- **SQLite** - Development and small applications

**NoSQL:**
- **MongoDB** - Document storage
- **Redis** - Caching and sessions
- **DynamoDB** - AWS serverless applications

### PostgreSQL as Default

**Use PostgreSQL as the default database unless there's a specific reason not to.**

**Why PostgreSQL:**
- ACID compliance and reliability
- Rich data types (JSON, arrays, ranges)
- Excellent performance
- Strong community and ecosystem
- Advanced features (full-text search, geospatial)
- Great tooling and ORM support

## Schema Design Principles

### Naming Conventions

**Tables:**
- Use plural nouns: `users`, `posts`, `comments`
- Use snake_case: `user_profiles`, `blog_posts`
- Avoid abbreviations unless widely understood
- Use descriptive names

**Columns:**
- Use snake_case: `first_name`, `created_at`, `is_active`
- Be specific: `email_address` not just `email`
- Use consistent naming patterns
- Avoid reserved keywords

**Indexes:**
- Prefix with `idx_`: `idx_users_email`, `idx_posts_created_at`
- Include table and column names
- Use descriptive names for composite indexes

**Constraints:**
- Primary keys: `pk_<table>`
- Foreign keys: `fk_<table>_<referenced_table>`
- Unique constraints: `uq_<table>_<column>`
- Check constraints: `ck_<table>_<constraint_name>`

### Table Design

**Primary Keys:**
```sql
-- Use UUIDs for distributed systems
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Use auto-increment for single-server apps
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  title VARCHAR(255) NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

**Timestamps:**
```sql
-- Always include created_at and updated_at
CREATE TABLE articles (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  title TEXT NOT NULL,
  content TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW() NOT NULL,
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW() NOT NULL
);

-- Use trigger for auto-updating updated_at
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_articles_updated_at
BEFORE UPDATE ON articles
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();
```

**Soft Deletes:**
```sql
-- Include deleted_at for soft deletes
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  deleted_at TIMESTAMP WITH TIME ZONE,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create partial index for active records only
CREATE INDEX idx_users_active ON users(id) WHERE deleted_at IS NULL;
```

### Data Types

**Choose Appropriate Types:**

```sql
-- Text/Strings
email VARCHAR(255)          -- Limited length
bio TEXT                    -- Unlimited length
status VARCHAR(20)          -- Use ENUM or check constraint instead

-- Numbers
age INTEGER                 -- Whole numbers
price DECIMAL(10, 2)       -- Money (avoid FLOAT)
rating DECIMAL(3, 2)       -- Ratings (e.g., 4.5)
quantity BIGINT            -- Large numbers

-- Dates/Times
created_at TIMESTAMP WITH TIME ZONE  -- Preferred
birth_date DATE                      -- Date only
event_time TIME WITH TIME ZONE       -- Time only

-- Boolean
is_active BOOLEAN DEFAULT true
is_verified BOOLEAN DEFAULT false

-- JSON
metadata JSONB             -- Use JSONB not JSON
settings JSONB            -- Indexable, faster

-- Arrays
tags TEXT[]               -- PostgreSQL arrays
phone_numbers VARCHAR(20)[]
```

### Relationships

**One-to-Many:**
```sql
-- Users have many posts
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  username VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE posts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  title TEXT NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_posts_user_id ON posts(user_id);
```

**Many-to-Many:**
```sql
-- Posts have many tags, tags have many posts
CREATE TABLE posts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  title TEXT NOT NULL
);

CREATE TABLE tags (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE post_tags (
  post_id UUID REFERENCES posts(id) ON DELETE CASCADE,
  tag_id UUID REFERENCES tags(id) ON DELETE CASCADE,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  PRIMARY KEY (post_id, tag_id)
);

CREATE INDEX idx_post_tags_post_id ON post_tags(post_id);
CREATE INDEX idx_post_tags_tag_id ON post_tags(tag_id);
```

**One-to-One:**
```sql
-- User has one profile
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE user_profiles (
  user_id UUID PRIMARY KEY REFERENCES users(id) ON DELETE CASCADE,
  bio TEXT,
  avatar_url TEXT,
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

## Indexing Strategy

### When to Add Indexes

**Always Index:**
- Primary keys (automatic)
- Foreign keys
- Columns used in WHERE clauses frequently
- Columns used in JOIN conditions
- Columns used in ORDER BY frequently
- Unique constraints

**Consider Indexing:**
- Columns used in GROUP BY
- Columns with high cardinality
- Columns in composite searches
- JSONB fields with GIN indexes

**Avoid Indexing:**
- Small tables (< 1000 rows)
- Columns with low cardinality (e.g., boolean)
- Columns rarely queried
- Wide columns (TEXT, BLOB)

### Index Types

```sql
-- B-tree index (default, most common)
CREATE INDEX idx_users_email ON users(email);

-- Partial index (filtered)
CREATE INDEX idx_users_active_email ON users(email)
WHERE deleted_at IS NULL;

-- Composite index (order matters!)
CREATE INDEX idx_posts_user_created ON posts(user_id, created_at DESC);

-- GIN index (for JSONB, arrays, full-text search)
CREATE INDEX idx_products_metadata ON products USING GIN(metadata);
CREATE INDEX idx_posts_tags ON posts USING GIN(tags);

-- Full-text search
CREATE INDEX idx_articles_search ON articles
USING GIN(to_tsvector('english', title || ' ' || content));

-- Unique index
CREATE UNIQUE INDEX idx_users_email_unique ON users(LOWER(email));
```

### Index Monitoring

```sql
-- Find unused indexes
SELECT
  schemaname,
  tablename,
  indexname,
  idx_scan as index_scans
FROM pg_stat_user_indexes
WHERE idx_scan = 0
AND indexrelname NOT LIKE 'pk_%'
ORDER BY pg_relation_size(indexrelid) DESC;

-- Find missing indexes
SELECT
  schemaname,
  tablename,
  attname,
  n_distinct,
  correlation
FROM pg_stats
WHERE schemaname NOT IN ('pg_catalog', 'information_schema')
ORDER BY n_distinct DESC;
```

## ORM Standards

### Recommended ORMs

**Node.js/TypeScript:**
- **Prisma** - Recommended (type-safe, great DX)
- **Drizzle** - Alternative (lightweight, SQL-like)
- **TypeORM** - Full-featured ORM

**Python:**
- **SQLAlchemy** - Recommended (powerful, mature)
- **Django ORM** - For Django projects
- **Tortoise ORM** - Async ORM

### Prisma Standards (Node.js)

**Schema Organization:**
```prisma
// prisma/schema.prisma

generator client {
  provider = "prisma-client-js"
  previewFeatures = ["fullTextSearch", "postgresqlExtensions"]
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
  extensions = [uuid_ossp(map: "uuid-ossp"), pg_trgm]
}

// User model
model User {
  id        String   @id @default(uuid()) @db.Uuid
  email     String   @unique @db.VarChar(255)
  name      String?  @db.VarChar(100)
  role      Role     @default(USER)
  posts     Post[]
  profile   Profile?
  createdAt DateTime @default(now()) @map("created_at") @db.Timestamptz
  updatedAt DateTime @updatedAt @map("updated_at") @db.Timestamptz
  deletedAt DateTime? @map("deleted_at") @db.Timestamptz

  @@index([email])
  @@index([createdAt])
  @@map("users")
}

// One-to-one relationship
model Profile {
  userId    String   @id @map("user_id") @db.Uuid
  bio       String?  @db.Text
  avatarUrl String?  @map("avatar_url") @db.VarChar(500)
  user      User     @relation(fields: [userId], references: [id], onDelete: Cascade)
  updatedAt DateTime @updatedAt @map("updated_at") @db.Timestamptz

  @@map("user_profiles")
}

// One-to-many relationship
model Post {
  id        String   @id @default(uuid()) @db.Uuid
  title     String   @db.VarChar(255)
  content   String?  @db.Text
  published Boolean  @default(false)
  authorId  String   @map("author_id") @db.Uuid
  author    User     @relation(fields: [authorId], references: [id], onDelete: Cascade)
  tags      Tag[]
  createdAt DateTime @default(now()) @map("created_at") @db.Timestamptz
  updatedAt DateTime @updatedAt @map("updated_at") @db.Timestamptz

  @@index([authorId])
  @@index([published, createdAt])
  @@map("posts")
}

// Many-to-many relationship
model Tag {
  id    String @id @default(uuid()) @db.Uuid
  name  String @unique @db.VarChar(50)
  posts Post[]

  @@map("tags")
}

// Enums
enum Role {
  USER
  MODERATOR
  ADMIN
}
```

**Prisma Client Usage:**
```typescript
// Good practices
import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient({
  log: process.env.NODE_ENV === 'development'
    ? ['query', 'error', 'warn']
    : ['error'],
});

// Use transactions for related operations
async function createUserWithProfile(data) {
  return await prisma.$transaction(async (tx) => {
    const user = await tx.user.create({
      data: {
        email: data.email,
        name: data.name,
      },
    });

    const profile = await tx.profile.create({
      data: {
        userId: user.id,
        bio: data.bio,
      },
    });

    return { user, profile };
  });
}

// Use select to fetch only needed fields
const users = await prisma.user.findMany({
  select: {
    id: true,
    email: true,
    name: true,
    _count: {
      select: { posts: true }
    }
  },
  where: {
    deletedAt: null
  }
});

// Use cursor-based pagination for large datasets
async function getPaginatedPosts(cursor?: string, limit = 20) {
  return await prisma.post.findMany({
    take: limit,
    skip: cursor ? 1 : 0,
    cursor: cursor ? { id: cursor } : undefined,
    orderBy: { createdAt: 'desc' },
  });
}
```

## Migrations

### Migration Standards

**Rules:**
1. **Never edit existing migrations** - Create new ones
2. **Always review generated migrations** - Verify SQL
3. **Test migrations on staging** before production
4. **Keep migrations reversible** when possible
5. **One logical change per migration**
6. **Name migrations descriptively**

**Prisma Migrations:**
```bash
# Create migration
pnpm prisma migrate dev --name add_user_role

# Apply migrations (production)
pnpm prisma migrate deploy

# Reset database (dev only!)
pnpm prisma migrate reset

# Generate migration without applying
pnpm prisma migrate dev --create-only
```

**Migration Naming:**
```
Good:
- 20240101120000_add_user_role_column
- 20240102130000_create_posts_table
- 20240103140000_add_posts_user_id_index

Bad:
- migration_1
- update
- fixes
```

### Data Migrations

**Separate schema and data migrations:**

```sql
-- Schema migration (via Prisma)
ALTER TABLE users ADD COLUMN role VARCHAR(20) DEFAULT 'user';

-- Data migration (separate script)
-- scripts/migrations/backfill_user_roles.ts
import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

async function backfillUserRoles() {
  // Get admin emails from config
  const adminEmails = process.env.ADMIN_EMAILS?.split(',') || [];

  // Update in batches
  await prisma.user.updateMany({
    where: {
      email: {
        in: adminEmails
      }
    },
    data: {
      role: 'ADMIN'
    }
  });

  console.log(`Updated ${adminEmails.length} users to ADMIN role`);
}

backfillUserRoles()
  .catch(console.error)
  .finally(() => prisma.$disconnect());
```

## Query Optimization

### Query Best Practices

**Avoid N+1 Queries:**
```typescript
// Bad - N+1 query problem
const users = await prisma.user.findMany();
for (const user of users) {
  const posts = await prisma.post.findMany({
    where: { authorId: user.id }
  });
  console.log(user.name, posts.length);
}

// Good - Use include/select
const users = await prisma.user.findMany({
  include: {
    _count: {
      select: { posts: true }
    }
  }
});
```

**Use Appropriate Pagination:**
```typescript
// Offset pagination (simple, not for large datasets)
const page = 1;
const limit = 20;
const posts = await prisma.post.findMany({
  skip: (page - 1) * limit,
  take: limit,
  orderBy: { createdAt: 'desc' }
});

// Cursor pagination (better for large datasets)
const posts = await prisma.post.findMany({
  take: 20,
  skip: cursor ? 1 : 0,
  cursor: cursor ? { id: cursor } : undefined,
  orderBy: { createdAt: 'desc' }
});
```

**Select Only Needed Fields:**
```typescript
// Bad - Fetching everything
const users = await prisma.user.findMany();

// Good - Select specific fields
const users = await prisma.user.findMany({
  select: {
    id: true,
    email: true,
    name: true
  }
});
```

### Performance Monitoring

```typescript
// Log slow queries in development
const prisma = new PrismaClient({
  log: [
    {
      emit: 'event',
      level: 'query',
    },
  ],
});

prisma.$on('query', (e) => {
  if (e.duration > 1000) { // Log queries > 1s
    console.warn('Slow query detected:', {
      query: e.query,
      duration: `${e.duration}ms`,
      params: e.params,
    });
  }
});
```

## Security Best Practices

### SQL Injection Prevention

```typescript
// Always use parameterized queries with ORMs
// Prisma automatically prevents SQL injection

// Bad - Raw SQL with string concatenation (NEVER DO THIS)
const userId = req.params.id;
const user = await prisma.$queryRaw`SELECT * FROM users WHERE id = ${userId}`; // Still safe with Prisma

// Good - Use ORM methods
const user = await prisma.user.findUnique({
  where: { id: userId }
});

// If raw SQL is necessary, use parameters
const users = await prisma.$queryRaw`
  SELECT * FROM users WHERE role = ${role} AND created_at > ${date}
`;
```

### Database Credentials

```bash
# .env (never commit)
DATABASE_URL="postgresql://user:password@localhost:5432/myapp?schema=public"

# .env.example (safe to commit)
DATABASE_URL="postgresql://user:password@localhost:5432/dbname?schema=public"

# Use connection pooling
DATABASE_URL="postgresql://user:password@localhost:5432/myapp?schema=public&connection_limit=10"
```

### Access Control

```sql
-- Create role with limited permissions
CREATE ROLE app_user WITH LOGIN PASSWORD 'secure_password';

-- Grant only necessary permissions
GRANT CONNECT ON DATABASE myapp TO app_user;
GRANT USAGE ON SCHEMA public TO app_user;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO app_user;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO app_user;

-- Revoke dangerous permissions
REVOKE CREATE ON SCHEMA public FROM app_user;
REVOKE ALL ON pg_catalog.pg_authid FROM app_user;
```

## Backup & Recovery

### Backup Strategy

**Automated Backups:**
```bash
# Daily backup script
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
pg_dump -h localhost -U postgres myapp > backup_${DATE}.sql

# Keep last 30 days
find /backups -name "backup_*.sql" -mtime +30 -delete
```

**Point-in-Time Recovery:**
- Enable WAL archiving in PostgreSQL
- Use managed database services (AWS RDS, Supabase)
- Test restore procedures regularly
- Store backups in different geographic location

### Disaster Recovery

1. **Regular backup verification** - Test restores monthly
2. **Document recovery procedures** - Step-by-step guide
3. **Monitor backup status** - Alert on failures
4. **Encrypt backups** - Protect sensitive data
5. **Maintain backup retention policy** - 30 days minimum

---

**Follow these database standards for reliable, performant, and maintainable data storage.**

---


---

*This file is auto-generated from cursor rules. Do not edit directly.*
*To update, modify the source .mdc files and run sync-to-claude.py*
