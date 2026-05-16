# Release Note Generator Prompt

Generate release notes from commit messages, merged PRs, or a changelog draft.

Input:
- Version:
- Date:
- Previous version:
- Commits / PRs:
- Breaking changes:

Output:

## Version X.Y.Z — YYYY-MM-DD

### Highlights

### Added

### Changed

### Fixed

### Removed

### Migration notes

### Contributors

Rules:
- User-facing language only.
- Group internal refactors under Changed only when users benefit.
- Call out breaking changes first.
- Include exact migration steps when behavior changed.
