from word_guessing.game import Game


def test_initial_state() -> None:
    game = Game(target_word="cat")
    assert game.lives == 5
    assert not game.won
    assert not game.lost
    assert game.guessed_letters == []
    assert game.display_word == "___"


def test_correct_guess() -> None:
    game = Game(target_word="cat")
    result = game.guess("a")
    assert result == "correct"
    assert "a" in game.guessed_letters
    assert game.lives == 5
    assert game.display_word == "_a_"
    assert not game.is_over


def test_wrong_guess() -> None:
    game = Game(target_word="cat")
    result = game.guess("x")
    assert result == "wrong"
    assert "x" in game.guessed_letters
    assert game.lives == 4


def test_duplicate_guess() -> None:
    game = Game(target_word="cat")
    game.guess("a")
    result = game.guess("a")
    assert result == "duplicate"
    assert game.lives == 5


def test_non_alpha_guess() -> None:
    game = Game(target_word="cat")
    result = game.guess("1")
    assert result == "not_alpha"
    assert game.lives == 5


def test_win_condition() -> None:
    game = Game(target_word="cat")
    game.guess("c")
    game.guess("a")
    assert not game.is_over
    game.guess("t")
    assert game.won
    assert game.is_over


def test_lose_condition() -> None:
    game = Game(target_word="cat")
    for letter in "xyzqb":
        game.guess(letter)
    assert game.lost
    assert game.is_over
    assert game.lives == 0


def test_display_shows_all_underscores_initially() -> None:
    game = Game(target_word="dog")
    assert game.display_word == "___"


def test_display_reveals_correct_letters() -> None:
    game = Game(target_word="dog")
    game.guess("d")
    assert game.display_word == "d__"
    game.guess("g")
    assert game.display_word == "d_g"


def test_wrong_count_increases() -> None:
    game = Game(target_word="cat")
    assert game.wrong_count == 0
    game.guess("x")
    assert game.wrong_count == 1
    game.guess("y")
    assert game.wrong_count == 2


def test_wrong_count_does_not_increase_on_correct() -> None:
    game = Game(target_word="cat")
    game.guess("c")
    assert game.wrong_count == 0


def test_sorted_guessed() -> None:
    game = Game(target_word="cat")
    game.guess("c")
    game.guess("a")
    game.guess("b")
    assert game.sorted_guessed == ["a", "b", "c"]
