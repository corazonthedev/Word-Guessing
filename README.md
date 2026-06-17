# Word Guessing Game

A classic word-guessing (hangman-style) terminal game written in Python.

**Zero dependencies** — just Python 3.10+ and a terminal. ANSI colors, Unicode
box drawing, ASCII hangman figure. Pure terminal fun.

## How to Run

```bash
# Quick — no install
python -m word_guessing

# Or install system-wide
pip install -e .
word-guessing
```

## How to Play

1. Pick a category (animals, food, nature, tech — or random)
2. Guess one letter at a time
3. 5 wrong guesses and you're out
4. Reveal all letters to win

```
  ┌────────────────────────────────────┐
  │  _ _ _ _ _ _ _ _ _  word           │
  │                                    │
  │  ♥♥♥♥♥  lives                      │
  └────────────────────────────────────┘
  ┌────────────────────────────────────┐
  │  (｡)                               │
  │         Guessed: a, e              │
  │  /|\                               │
  │  / \                               │
  │  guess a letter (Ctrl+C to quit)   │
  └────────────────────────────────────┘
```

## Project Structure

```
word_guessing/           # Main package
├── game.py              # Game state (Dataclass) — pure logic
├── words.py             # Word lists by category
├── display.py           # ANSI terminal rendering
├── main.py              # Menu & game loop
├── __init__.py          # Public API exports
└── __main__.py          # python -m entry point

tests/                   # Test suite
├── test_game.py         # 11 tests — win/lose/guess edge cases
├── test_words.py        # 4 tests — category selection
└── test_display.py      # 10 tests — rendering functions

docs/
├── ADR.md               # Architecture Decision Record

.github/workflows/
└── ci.yml               # CI — runs tests on Python 3.10–3.13
```

## Development

```bash
python -m pytest tests/ -v
```

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

MIT
