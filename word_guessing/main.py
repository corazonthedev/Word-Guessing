import sys

from word_guessing.game import Game
from word_guessing.words import get_categories, get_random_word
from word_guessing.display import game_screen, c, line


def _cls() -> None:
    """Clear screen (ANSI)."""
    print("\033[2J\033[H", end="")


def _prompt(msg: str) -> str:
    """Print a colored inline prompt and return stripped input."""
    try:
        return input(f"  {c('>>', 'cyan')} {msg} ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print()
        sys.exit(0)


def play_round() -> None:
    category = _pick_category()
    word = get_random_word(category) if category else get_random_word()
    game = Game(target_word=word)

    while not game.is_over:
        _cls()
        game_screen(game)
        letter = _prompt("Guess a letter:")

        if not letter or len(letter) != 1:
            continue

        result = game.guess(letter)
        match result:
            case "correct":
                pass  # UI updates on next render
            case "wrong":
                pass
            case "duplicate":
                print(f"\n  {c('!', 'yellow')} Already guessed {c(letter, 'yellow')}")
                input("  Press Enter to continue...")
            case "not_alpha":
                print(f"\n  {c('!', 'yellow')} Letters only, please!")
                input("  Press Enter to continue...")

    # Final reveal
    _cls()
    game_screen(game)
    print()
    if game.won:
        print(f"  {c('★', 'green')} {c('YOU WON!', 'green')} "
              f"with {c(str(game.lives), 'cyan')} lives left! {c('★', 'green')}")
    else:
        print(f"  {c('✗', 'red')} The word was: {c(game.target_word, 'cyan')}")
    print()


def _pick_category() -> str | None:
    _cls()
    cats = get_categories()
    print(f"\n  {c('Pick a category', 'bold')}")
    for i, cat in enumerate(cats, 1):
        print(f"  {c(f'[{i}]', 'cyan')} {cat.capitalize()}")
    print(f"  {c('[0]', 'dim')} Random")
    print()
    choice = _prompt("Enter number:")

    if choice.isdigit():
        idx = int(choice)
        if 1 <= idx <= len(cats):
            return cats[idx - 1]
    return None


def main_menu() -> None:
    while True:
        _cls()
        print()
        print(f"  {c('╔════════════════════════════════════╗', 'cyan')}")
        print(f"  {c('║', 'cyan')}   {c('W O R D   G U E S S I N G', 'bold')}      {c('║', 'cyan')}")
        print(f"  {c('║', 'cyan')}   {'────────────────────────':<30s}  {c('║', 'cyan')}")
        print(f"  {c('║', 'cyan')}   {c('Guess the word — letter by letter', 'dim')}  {c('║', 'cyan')}")
        print(f"  {c('╚════════════════════════════════════╝', 'cyan')}")
        print()
        print(f"  {c('[p]', 'cyan')} Play")
        print(f"  {c('[q]', 'red')} Quit")
        print()
        choice = _prompt("Choose:")

        if choice in ("p", "play", "y"):
            play_round()
        elif choice in ("q", "quit", "n", "exit"):
            print(f"\n  {c('Goodbye!', 'dim')}\n")
            break


def main() -> None:
    main_menu()


if __name__ == "__main__":
    main()
