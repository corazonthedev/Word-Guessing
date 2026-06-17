# Word Guessing Game

A classic word-guessing (hangman-style) terminal game written in Python.

## How to Run

```bash
# Direct
python -m word_guessing

# Or install and run
pip install -e .
word-guessing
```

## How to Play

1. Pick a category (or random)
2. Guess one letter at a time
3. 5 wrong guesses and you're out
4. Reveal all letters to win

## Project Structure

```
word_guessing/
├── game.py      # Game state and logic
├── main.py      # Terminal UI and menu
├── words.py     # Word lists by category
└── __main__.py  # `python -m` entry point
tests/
├── test_game.py
└── test_words.py
```
