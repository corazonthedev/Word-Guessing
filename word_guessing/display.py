HANGMAN_STAGES = [
    "",  # 0 wrong
    "\n  (｡)\n",  # 1 wrong
    "\n  (｡)\n   |\n",  # 2 wrong
    "\n  (｡)\n  /|\n",  # 3 wrong
    "\n  (｡)\n  /|\\\n",  # 4 wrong
    "\n  (｡)\n  /|\\\n  / \\\n",  # 5 wrong
]


def hangman(wrong_count: int) -> str:
    return HANGMAN_STAGES[min(wrong_count, 5)]


def lives_bar(lives: int) -> str:
    full = "\033[91m♥\033[0m" * lives
    empty = "\033[90m♥\033[0m" * (5 - lives)
    return full + empty


def c(text: str, color: str) -> str:
    codes = {"green": "\033[92m", "red": "\033[91m", "yellow": "\033[93m",
             "cyan": "\033[96m", "bold": "\033[1m", "dim": "\033[2m"}
    return f'{codes.get(color, "")}{text}\033[0m'


BOX_H = "\033[90m─\033[0m"
BOX_V = "\033[90m│\033[0m"


def line(top: bool) -> str:
    """Return a horizontal rule line (top or bottom) with corners."""
    a, b = ("┌", "┐") if top else ("└", "┘")
    return f"  \033[90m{a}\033[0m{BOX_H * 36}\033[90m{b}\033[0m"


def word_render(word: str, guessed: list[str]) -> str:
    return " ".join(
        c(l, "green") if l in guessed else c("_", "bold")
        for l in word
    )


def game_screen(game: object) -> None:
    hm = hangman(game.wrong_count)  # type: ignore
    hm_lines = hm.strip("\n").split("\n") if hm.strip() else []

    print()
    print(line(True))
    print(f"  {BOX_V}  {word_render(game.target_word, game.guessed_letters):^34s}  {BOX_V}")  # type: ignore
    print(f"  {BOX_V}  {'':>34s}  {BOX_V}")
    print(f"  {BOX_V}  {lives_bar(game.lives):<30s}  {BOX_V}")  # type: ignore
    print(line(False))
    print(line(True))
    for i in range(4):
        hline = hm_lines[i] if i < len(hm_lines) else ""
        if i == 1:
            guessed_str = ", ".join(game.sorted_guessed) or "—"  # type: ignore
            print(f"  {BOX_V}  {hline:<8s} Guessed: {c(guessed_str, 'yellow'):<21s}{BOX_V}")
        else:
            print(f"  {BOX_V}  {hline:<34s}  {BOX_V}")
    print(f"  {BOX_V}  {c('guess a letter (Ctrl+C to quit)', 'dim'):<34s}  {BOX_V}")
    print(line(False))
