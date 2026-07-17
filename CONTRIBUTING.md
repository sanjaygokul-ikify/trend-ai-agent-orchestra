# Contributing to AI Agent Orchestra

**Development Workflow:**

1. Fork repository
2. Create feature branch: `git checkout -b feature-name`
3. Run tests with `make ci`
4. Use `cargo fmt` for Rust code formatting
5. Open PR with clear changelog summary

**Code Style:**

Python code follows PEP8 with 99 character line limit. Rust code follows rustfmt defaults with `#[allow(clippy::all)]` for readability exceptions.

**Testing Requirements:**

- All new features must include property-based tests using `hypothesis` or equivalent
- 100% coverage for critical path code
- Fuzz testing for consensus store operations