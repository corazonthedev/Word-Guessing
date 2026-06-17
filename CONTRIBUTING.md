# Contributing

## Setup

1. Use Python 3.10+
2. Clone the repo
3. Run the app: `python -m word_guessing`
4. Run tests: `python -m pytest`

## Code Style

- Keep game logic in `word_guessing/game.py` — no UI code
- Keep display in `word_guessing/display.py` — no game logic
- Type-annotate all function signatures
- Add or update tests for every behavior change

## Commit Style

```
feat: add score tracking across rounds
fix: handle empty input without crash
test: add coverage for category edge cases
docs: refresh setup instructions
```

## Pull Request Expectations

- App still launches
- Existing tests pass
- New behavior includes test coverage
- README stays accurate
