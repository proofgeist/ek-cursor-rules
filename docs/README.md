# Cursor Rules Documentation

**Central documentation hub for ek-cursor-rules**

## Quick Links

- [Getting Started](./getting-started/README.md) - Installation and setup
- [User Guide](./user-guide/README.md) - Using the rules
- [Developer Guide](./developer-guide/README.md) - Contributing and extending
- [API Reference](./api/README.md) - Script and tool documentation

## What is ek-cursor-rules?

ek-cursor-rules is a comprehensive set of AI assistant directives (`.mdc` files) that guide Cursor and Claude Code to follow software development best practices across multiple technology stacks.

## Documentation Structure

### Getting Started
New to cursor rules? Start here to understand the basics and get set up.

- **[Installation](./getting-started/installation.md)** - How to import rules into your projects
- **[Quick Start](./getting-started/quick-start.md)** - Get up and running in 5 minutes
- **[Configuration](./getting-started/configuration.md)** - Customize rules for your needs

### User Guide
Learn how to use the rules effectively in your projects.

- **[Rule Categories](./user-guide/rule-categories.md)** - Overview of all rule types
- **[Python Projects](./user-guide/python-projects.md)** - Using Python-specific rules
- **[Node.js Projects](./user-guide/nodejs-projects.md)** - Using Node.js/TypeScript rules
- **[Best Practices](./user-guide/best-practices.md)** - Tips for getting the most value

### Developer Guide
Contributing to the project or creating custom rules.

- **[Contributing](./developer-guide/contributing.md)** - How to contribute
- **[Rule Format](./developer-guide/rule-format.md)** - .mdc file structure
- **[Creating Rules](./developer-guide/creating-rules.md)** - Write your own rules
- **[Testing](./developer-guide/testing.md)** - Testing your rules

### API Reference
Technical documentation for scripts and tools.

- **[Import Scripts](./api/import-scripts.md)** - Script API documentation
- **[Sync Tool](./api/sync-tool.md)** - sync-to-claude.py documentation

## Core Principles

The rules are built on these principles:

1. **Seek first to understand** - Thoughtful analysis before action
2. **Small things, loosely coupled** - Functional and modular design
3. **Simple but not simpler** - Balance simplicity with functionality
4. **Critical thinking encouraged** - Don't agree automatically

## Technology Coverage

### Python Projects
- Package management with `uv`
- Testing with pytest
- Code standards and formatting
- Virtual environment setup

### Node.js/TypeScript Projects
- Package management with `pnpm`
- Testing with Vitest
- Express.js API standards
- Next.js and Vercel deployment
- Better-Auth authentication
- ProofKit for FileMaker apps
- TypeScript best practices

### Database
- PostgreSQL as default
- Prisma ORM
- Schema design
- Migration management

### General Standards
- Git workflow and commits
- Security best practices
- Documentation standards
- Versioning with semantic-release

## Support

### Getting Help
- Check the [User Guide](./user-guide/README.md) for common questions
- Review the [PROJECT_PLAN.md](../PROJECT_PLAN.md) for roadmap
- Open an issue on [GitHub](https://github.com/ernestkoe/ek-cursor-rules/issues)

### Contributing
See the [Developer Guide](./developer-guide/README.md) for contribution guidelines.

## Version Information

- **Current Version**: 1.0.0
- **Last Updated**: 2025-10-04
- **Changelog**: See [CHANGELOG.md](../CHANGELOG.md)

---

**Navigation**: [Home](../README.md) | [Project Plan](../PROJECT_PLAN.md) | [Contributing](./developer-guide/contributing.md)
