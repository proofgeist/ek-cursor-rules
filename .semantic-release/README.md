# Semantic Release Configuration

This directory contains the configuration for semantic-release, which automates version management and package publishing.

## Configuration Files

- `config.json`: Main semantic-release configuration file

## Commit Message Format

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

### Types
- `feat:` - New feature (MINOR version)
- `fix:` - Bug fix (PATCH version)
- `docs:` - Documentation changes
- `style:` - Code style changes
- `refactor:` - Code changes that neither fix bugs nor add features
- `perf:` - Performance improvements (PATCH version)
- `test:` - Adding or fixing tests
- `chore:` - Changes to build process, tools, etc.

### Breaking Changes
- Use `!` after type/scope: `feat!: change API`
- Or add `BREAKING CHANGE:` in commit body

### Scope (optional)
- Format: `type(scope): message`
- Example: `fix(auth): resolve login issue`

## Version Bumps
- MAJOR (1.0.0 → 2.0.0): Breaking changes
- MINOR (1.0.0 → 1.1.0): New features
- PATCH (1.0.0 → 1.0.1): Bug fixes 