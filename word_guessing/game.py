from dataclasses import dataclass, field
from word_guessing.words import get_random_word


@dataclass
class Game:
    target_word: str = field(default_factory=get_random_word)
    guessed_letters: list[str] = field(default_factory=list)
    lives: int = 5
    won: bool = False
    lost: bool = False

    def guess(self, letter: str) -> str:
        if len(letter) != 1:
            return "error"

        if not letter.isalpha():
            return "not_alpha"

        if letter in self.guessed_letters:
            return "duplicate"

        self.guessed_letters.append(letter)

        if letter in self.target_word:
            self._check_win()
            return "correct"
        else:
            self.lives -= 1
            if self.lives <= 0:
                self.lost = True
            return "wrong"

    def _check_win(self) -> None:
        if all(letter in self.guessed_letters for letter in self.target_word):
            self.won = True

    @property
    def is_over(self) -> bool:
        return self.won or self.lost

    @property
    def display_word(self) -> str:
        return "".join(
            letter if letter in self.guessed_letters else "_"
            for letter in self.target_word
        )

    @property
    def sorted_guessed(self) -> list[str]:
        return sorted(self.guessed_letters)

    @property
    def wrong_count(self) -> int:
        return 5 - self.lives
