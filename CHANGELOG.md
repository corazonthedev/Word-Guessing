# Changelog

## 2.0.0 (2026-06-17)

Full rewrite. Original mechanics preserved.

### Added
- Modular package structure with separate game, words, display, and main modules
- ANSI-colored terminal UI with box-drawing characters and hangman figure
- Category-based word selection — animals, food, nature, tech, mixed
- 50+ words across 5 categories
- Comprehensive test suite (16 tests)
- `pyproject.toml` with installable entry point
- `CONTRIBUTING.md` and `CHANGELOG.md`

### Changed
- Global state replaced with `Game` dataclass — testable, isolated rounds
- Recursive menu replaced with event loop — no stack buildup
- Single `word guessing.py` → organized module tree

## 1.0.0 (2024-01-28)

Initial release — single-file Python script with 6 words and no dependencies.
