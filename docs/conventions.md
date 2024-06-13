# Conventions to Follow:

## Git:

### Commit Message Conventions

1. **Prefix with Type**: Start commit messages with a type indicating the purpose of the commit:
   - **`feat:`** A new feature
   - **`fix:`** A bug fix
   - **`docs:`** Documentation changes
   - **`style:`** Code style changes (formatting, missing semi-colons, etc.), not affecting logic
   - **`refactor:`** Code refactoring without changing any functionality or fixing a bug
   - **`perf:`** Performance improvements
   - **`test:`** Adding or updating tests
   - **`chore:`** Other changes that don't modify `src` or `test` files (e.g., build tasks, package manager configs)
   - **`ci:`** Changes to our CI configuration files and scripts (e.g., GitHub Actions, CircleCI, etc.)
   - **`build:`** Changes that affect the build system or external dependencies (e.g., `npm`, `gradle`, `gulp`, etc.)

2. **Message Structure**:
   - **Title**: 50 characters or less, prefixed with type, capitalized, and imperative mood
   - **Body (optional)**: Explain what and why vs. how, wrapped at 72 characters

### Examples

- **Feature**: `feat: Add user authentication module`
- **Bug Fix**: `fix: Resolve issue with login form validation`
- **Documentation**: `docs: Update README with setup instructions`
- **Style**: `style: Format code according to eslint rules`
- **Refactor**: `refactor: Rename variable for clarity`
- **Performance**: `perf: Improve database query efficiency`
- **Tests**: `test: Add unit tests for user model`
- **Chore**: `chore: Update npm dependencies`
- **CI**: `ci: Add GitHub Actions workflow for CI`
- **Build**: `build: Update webpack configuration`

### Summary

- **Prefix** commit messages with a type.
- **Capitalize** the first letter of the message.
- **Use imperative mood** (e.g., "add" not "added").
- Keep **titles concise** (50 characters or less).
- Optionally, add a **body** to explain what and why, wrapped at 72 characters.

This structure helps in maintaining a consistent and understandable commit history, making it easier to navigate and manage the project's changes.
